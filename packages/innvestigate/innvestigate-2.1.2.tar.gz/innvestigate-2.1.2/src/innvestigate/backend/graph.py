"""Low-level operations on Keras graph."""
from __future__ import annotations

import inspect
import warnings
from abc import ABCMeta, abstractmethod
from typing import Any, Callable

import numpy as np
import tensorflow.keras.backend as kbackend
import tensorflow.keras.layers as klayers
import tensorflow.keras.models as kmodels

import innvestigate.backend as ibackend
import innvestigate.backend.checks as ichecks
import innvestigate.layers as ilayers
from innvestigate.backend.types import (
    Layer,
    LayerCheck,
    Model,
    NodeDict,
    OptionalList,
    ReverseTensorDict,
    Tensor,
)

__all__ = [
    "get_kernel",
    "get_layer_inbound_count",
    "get_layer_neuronwise_io",
    "copy_layer_wo_activation",
    "copy_layer",
    "pre_output_tensors",
    "model_wo_softmax",
    "model_wo_output_activation",
    "get_model_layers",
    "model_contains",
    "trace_model_execution",
    "get_model_execution_trace",
    "get_model_execution_graph",
    "print_model_execution_graph",
    "get_bottleneck_nodes",
    "get_bottleneck_tensors",
    "ReverseMappingBase",
    "reverse_model",
]


def get_kernel(layer: Layer) -> np.ndarray:
    """Returns the kernel weights of a layer, i.e, w/o biases."""
    ret = [x for x in layer.get_weights() if len(x.shape) > 1]
    assert len(ret) == 1
    return ret[0]


###############################################################################


def get_layer_inbound_count(layer: Layer) -> int:
    """Returns the number inbound nodes of a layer."""
    return len(layer._inbound_nodes)


def get_layer_neuronwise_io(
    layer: Layer,
    node_index: int = 0,
    Xs: list[Tensor] = None,
    Ys: list[Tensor] = None,
    return_i: bool = True,
    return_o: bool = True,
) -> tuple[list[Tensor], list[Tensor]] | list[Tensor]:
    """Returns the input and output for each neuron in a layer

    Returns the symbolic input and output for each neuron in a layer.
    For a dense layer this is the input output itself.
    For convolutional layers this method extracts for each neuron
    the input output mapping.

    At the moment this function is designed
    to work with dense and conv2d layers.

    :param layer: The targeted layer.
    :param node_index: Index of the layer node to use.
    :param Xs: Ignore the layer's input but use Xs instead.
    :param Ys: Ignore the layer's output but use Ys instead.
    :param return_i: Return the inputs.
    :param return_o: Return the outputs.
    :return: Inputs and outputs, if specified, for each individual neuron.
    """
    if not ichecks.contains_kernel(layer):
        raise NotImplementedError()

    if Xs is None:
        Xs = ibackend.to_list(layer.get_input_at(node_index))
    if Ys is None:
        Ys = ibackend.to_list(layer.get_output_at(node_index))

    if isinstance(layer, klayers.Dense):
        # Xs and Ys are already in shape.
        ret_Xs = Xs
        ret_Ys = Ys
    elif isinstance(layer, klayers.Conv2D):
        kernel = get_kernel(layer)
        # Expect filter dimension to be last.
        n_channels = kernel.shape[-1]

        if return_i:
            extract_patches = ilayers.ExtractConv2DPatches(
                kernel.shape[:2],
                kernel.shape[2],
                layer.strides,
                layer.dilation_rate,
                layer.padding,
            )
            # shape [samples, out_row, out_col, weight_size]
            reshape = ilayers.Reshape((-1, np.product(kernel.shape[:3])))
            ret_Xs = [reshape(extract_patches(x)) for x in Xs]

        if return_o:
            # Get Ys into shape (samples, channels)
            if kbackend.image_data_format() == "channels_first":
                # Ys shape is [samples, channels, out_row, out_col]
                def _reshape(x):
                    x = kbackend.permute_dimensions(x, (0, 2, 3, 1))
                    x = ilayers.Reshape((-1, n_channels))(x)
                    return x

            else:
                # Ys shape is [samples, out_row, out_col, channels]
                def _reshape(x):
                    x = ilayers.Reshape((-1, n_channels))(x)
                    return x

            ret_Ys = [_reshape(x) for x in Ys]

    else:
        raise NotImplementedError()

    # Xs is (n, d) and Ys is (d, channels)
    if return_i and return_o:
        return ret_Xs, ret_Ys
    if return_i:
        return ret_Xs
    if return_o:
        return ret_Ys
    raise Exception()


def get_symbolic_weight_names(layer: Layer, weights: list[Tensor] = None) -> list[str]:
    """Attribute names for weights

    Looks up the attribute names of weight tensors.

    :param layer: Targeted layer.
    :param weights: A list of weight tensors.
    :return: The attribute names of the weights.
    """

    if weights is None:
        weights = layer.weights

    good_guesses = [
        "kernel",
        "bias",
        "gamma",
        "beta",
        "moving_mean",
        "moving_variance",
        "depthwise_kernel",
        "pointwise_kernel",
    ]

    ret = []
    for weight in weights:
        for attr_name in good_guesses + dir(layer):
            if hasattr(layer, attr_name) and id(weight) == id(
                getattr(layer, attr_name)
            ):
                ret.append(attr_name)
                break
    if len(weights) != len(ret):
        raise Exception("Could not find symoblic weight name(s).")

    return ret


def update_symbolic_weights(layer: Layer, weight_mapping: dict[str, Tensor]) -> None:
    """Updates the symbolic tensors of a layer

    Updates the symbolic tensors of a layer by replacing them.

    Note this does not update the loss or anything alike!
    Use with caution!

    :param layer: Targeted layer.
    :param weight_mapping: Dict with attribute name and weight tensors
      as keys and values.
    """

    trainable_weight_ids = [id(x) for x in layer._trainable_weights]
    non_trainable_weight_ids = [id(x) for x in layer._non_trainable_weights]

    for name, weight in weight_mapping.items():
        current_weight = getattr(layer, name)
        current_weight_id = id(current_weight)

        if current_weight_id in trainable_weight_ids:
            idx = trainable_weight_ids.index(current_weight_id)
            layer._trainable_weights[idx] = weight
        else:
            idx = non_trainable_weight_ids.index(current_weight_id)
            layer._non_trainable_weights[idx] = weight

        setattr(layer, name, weight)


def get_layer_from_config(
    old_layer: Layer,
    new_config: dict[str, Any],
    weights: list[np.ndarray] | list[Tensor] | None = None,
    reuse_symbolic_tensors: bool = True,
) -> Layer:
    """Creates a new layer from a config

    Creates a new layer given a changed config and weights etc.

    :param old_layer: A layer that shall be used as base.
    :param new_config: The config to create the new layer.
    :param weights: Weights to set in the new layer.
      Options: np tensors, symbolic tensors, or None,
      in which case the weights from old_layers are used.
    :param reuse_symbolic_tensors: If the weights of the
      old_layer are used copy the symbolic ones or copy
      the Numpy weights.
    :return: The new layer instance.
    """
    new_layer = old_layer.__class__.from_config(new_config)

    if weights is None:
        if reuse_symbolic_tensors:
            weights = old_layer.weights
        else:
            weights = old_layer.get_weights()

    if len(weights) > 0:
        input_shapes = old_layer.get_input_shape_at(0)
        # todo: inspect and set initializers to something fast for speedup
        new_layer.build(input_shapes)

        is_np_weight = [isinstance(x, np.ndarray) for x in weights]
        if all(is_np_weight):
            new_layer.set_weights(weights)
        else:
            if any(is_np_weight):
                raise ValueError(
                    "Expect either all weights to be " "np tensors or symbolic tensors."
                )

            symbolic_names = get_symbolic_weight_names(old_layer)
            update = dict(zip(symbolic_names, weights))
            update_symbolic_weights(new_layer, update)

    return new_layer


def copy_layer_wo_activation(
    layer: Layer,
    keep_bias: bool = True,
    name_template: str | None = None,
    weights: list[np.ndarray] | list[Tensor] | None = None,
    reuse_symbolic_tensors: bool = True,
    **kwargs,
) -> Layer:
    """Copy a Keras layer and remove the activations

    Copies a Keras layer but remove potential activations.

    :param layer: A layer that should be copied.
    :param keep_bias: Keep a potential bias.
    :param weights: Weights to set in the new layer.
      Options: np tensors, symbolic tensors, or None,
      in which case the weights from old_layers are used.
    :param reuse_symbolic_tensors: If the weights of the
      old_layer are used copy the symbolic ones or copy
      the Numpy weights.
    :return: The new layer instance.
    """
    config = layer.get_config()
    if name_template is None:
        config["name"] = None
    else:
        config["name"] = name_template % config["name"]
    if ichecks.contains_activation(layer):
        config["activation"] = None
    if hasattr(layer, "use_bias"):
        if keep_bias is False and config.get("use_bias", True):
            config["use_bias"] = False
            if weights is None:
                if reuse_symbolic_tensors:
                    weights = layer.weights[:-1]
                else:
                    weights = layer.get_weights()[:-1]
    return get_layer_from_config(layer, config, weights=weights, **kwargs)


def copy_layer(
    layer: Layer,
    keep_bias: bool = True,
    name_template: bool = None,
    weights: list[Tensor] | list[np.ndarray] | None = None,
    reuse_symbolic_tensors: bool = True,
    **kwargs,
) -> Layer:
    """Copy a Keras layer.

    :param layer: A layer that should be copied.
    :param keep_bias: Keep a potential bias.
    :param weights: Weights to set in the new layer.
      Options: np tensors, symbolic tensors, or None,
      in which case the weights from old_layers are used.
    :param reuse_symbolic_tensors: If the weights of the
      old_layer are used copy the symbolic ones or copy
      the Numpy weights.
    :return: The new layer instance.
    """
    config = layer.get_config()
    if name_template is None:
        config["name"] = None
    else:
        config["name"] = name_template % config["name"]
    if hasattr(layer, "use_bias"):
        if keep_bias is False and config.get("use_bias", True):
            config["use_bias"] = False
            if weights is None:
                if reuse_symbolic_tensors:
                    weights = layer.weights[:-1]
                else:
                    weights = layer.get_weights()[:-1]
    return get_layer_from_config(layer, config, weights=weights, **kwargs)


def pre_output_tensors(Xs: Tensor, activation: str = None) -> list[Tensor]:
    """Finds the tensors that were preceeding a potential activation."""
    activation_found = False

    Xs = ibackend.to_list(Xs)
    ret = []
    for x in Xs:
        layer, node_index, _tensor_index = x._keras_history
        if ichecks.contains_activation(layer, activation=activation):
            activation_found = True
            if isinstance(layer, klayers.Activation):
                ret.append(layer.get_input_at(node_index))
            else:
                layer_wo_act = copy_layer_wo_activation(layer)
                ret.append(layer_wo_act(layer.get_input_at(node_index)))

    if not activation_found:
        if not activation == None:
            raise Exception(f"No output activation found.")
        else:
            raise Exception(f"No {activation} found.")

    return ret


def model_wo_softmax(model: Model) -> Model:
    """Creates a new model w/o the final softmax activation."""
    return kmodels.Model(
        inputs=model.inputs,
        outputs=pre_output_tensors(model.outputs, activation="softmax"),
        name=model.name,
    )


def model_wo_output_activation(model: Model) -> Model:
    """Creates a new model w/o the final activation."""
    return kmodels.Model(
        inputs=model.inputs,
        outputs=pre_output_tensors(model.outputs),
        name=model.name,
    )


###############################################################################


def get_model_layers(model: Model) -> list[Layer]:
    """Returns all layers of a model."""
    layers = []

    def collect_layers(container: Model) -> None:
        for layer in container.layers:
            if layer in layers:
                raise ValueError(f"Collected layer {layer} twice.")
            layers.append(layer)
            if ichecks.is_module(layer):
                collect_layers(layer)

    collect_layers(model)

    return layers


def model_contains(
    model: Model,
    layer_condition: OptionalList[LayerCheck],
) -> list[list[Layer]]:
    """
    Collect layers in model which satisfy `layer_condition`.
    If multiple conditions are given in `layer_condition`,
    the collected layers are returned for each condition.

    :param model: A Keras model.
    :type model: Model
    :param layer_condition: A boolean function or list of functions that
        check Keras layers.
    :type layer_condition: Union[LayerCheck, List[LayerCheck]]
    :return: List, which for each condition in layer_condition
        contains a list of layers which satisfy that condition.
    :rtype: List[List[Layer]]
    """
    conditions = ibackend.to_list(layer_condition)
    layers = get_model_layers(model)

    # return layers for which condition c holds true
    return [[l for l in layers if c(l)] for c in conditions]


###############################################################################


def apply_mapping_to_fused_bn_layer(mapping, fuse_mode: str = "one_linear") -> Callable:
    """
    Applies a mapping to a linearized Batch Normalization layer.

    :param mapping: The mapping to be applied.
      Should take parameters layer and reverse_state and
      return a mapping function.
    :param fuse_mode: Either 'one_linear': apply the mapping
      to a once linearized layer, or
      'two_linear': apply to twice to a twice linearized layer.
    """
    if fuse_mode not in ["one_linear", "two_linear"]:
        raise ValueError("fuse_mode can only be 'one_linear' or 'two_linear'")

    # TODO (alber): remove this workaround and make a proper class
    def get_scale_layer(kernel, bias):
        _kernel = kernel
        _bias = bias

        class ScaleLayer(klayers.Layer):
            def __init__(self, use_bias=True, **kwargs):
                self._kernel_to_be = _kernel
                self._bias_to_be = _bias
                self.use_bias = use_bias
                super().__init__(**kwargs)

            def get_config(self):
                config = super().get_config()
                config["use_bias"] = self.use_bias
                return config

            def build(self, input_shape):
                def kernel_initializer(_shape, dtype=None):
                    if dtype is not None:
                        warnings.warn(f"Ignore dtype {dtype} as bias type.")
                    return self._kernel_to_be

                self.kernel = self.add_weight(
                    name="kernel",
                    shape=kbackend.int_shape(self._kernel_to_be),
                    initializer=kernel_initializer,
                    trainable=False,
                )
                if self.use_bias:

                    def bias_initializer(_shape, dtype=None):
                        if dtype is not None:
                            warnings.warn(f"Ignore dtype {dtype} as bias type.")
                        return self._bias_to_be

                    self.bias = self.add_weight(
                        name="bias",
                        shape=kbackend.int_shape(self._bias_to_be),
                        initializer=bias_initializer,
                        trainable=False,
                    )
                super().build(input_shape)

            def call(self, inputs, *_args, **_kwargs):
                ret = inputs * self.kernel
                if self.use_bias:
                    ret += self.bias
                return ret

        return ScaleLayer()

    def meta_mapping(layer: Layer, reverse_state: dict):
        # get bn params
        weights = layer.weights.copy()
        if layer.scale:
            gamma = weights.pop(0)
        else:
            gamma = kbackend.ones_like(weights[0])
        if layer.center:
            beta = weights.pop(0)
        else:
            beta = kbackend.zeros_like(weights[0])
        mean, variance = weights

        if fuse_mode == "one_linear":
            tmp = kbackend.sqrt(variance**2 + layer.epsilon)
            tmp_k = gamma / tmp
            tmp_b = -mean / tmp + beta

            inputs = layer.get_input_at(0)
            surrogate_layer = get_scale_layer(tmp_k, tmp_b)
            # init layer
            surrogate_layer(inputs)
            actual_mapping = mapping(surrogate_layer, reverse_state).apply
        else:
            tmp = kbackend.sqrt(variance**2 + layer.epsilon)
            tmp_k1 = 1 / tmp
            tmp_b1 = -mean / tmp
            tmp_k2 = gamma
            tmp_b2 = beta

            inputs = layer.get_input_at(0)
            surrogate_layer1 = get_scale_layer(tmp_k1, tmp_b1)
            surrogate_layer2 = get_scale_layer(tmp_k2, tmp_b2)
            # init layers
            surrogate_layer1(inputs)
            surrogate_layer2(inputs)
            # TODO (alber): update reverse state
            actual_mapping_1 = mapping(surrogate_layer1, reverse_state).apply
            actual_mapping_2 = mapping(surrogate_layer2, reverse_state).apply

            def actual_mapping(
                Xs: list[Tensor],
                Ys: list[Tensor],
                reversed_Ys: list[Tensor],
                reverse_state,
            ):
                X2s = ibackend.apply(surrogate_layer1, Xs)
                # Apply first mapping
                # TODO (alber): update reverse state
                reversed_X2s = actual_mapping_2(X2s, Ys, reversed_Ys, reverse_state)
                return actual_mapping_1(Xs, X2s, reversed_X2s, reverse_state)

        return actual_mapping

    return meta_mapping


###############################################################################


def trace_model_execution(
    model: Model, reapply_on_copied_layers: bool = False
) -> tuple[list[Layer], list[tuple[Layer, list[Tensor], list[Tensor]]], list[Tensor]]:
    """
    Trace and linearize excecution of a model and it's possible containers.
    Return a triple with all layers, a list with a linearized execution
    with (layer, input_tensors, output_tensors), and, possible regenerated,
    outputs of the exectution.

    :param model: A kera model.
    :param reapply_on_copied_layers: If the execution needs to be linearized,
      reapply with copied layers. Might be slow. Prevents changes of the
      original layer's node lists.
    """

    # Get all layers in model.
    layers: list[Layer] = get_model_layers(model)

    # Check if some layers are containers.
    # Ignoring the outermost container, i.e. the passed model.
    contains_container: bool = any(
        l is not model and ichecks.is_module(l) for l in layers
    )

    outputs: list[Tensor]

    # If so rebuild the graph, otherwise recycle computations,
    # and create executed node list. (Keep track of paths?)
    if contains_container is True:
        # When containers/models are used as layers, then layers
        # inside the container/model do not keep track of nodes.
        # This makes it impossible to iterate of the nodes list and
        # recover the input output tensors. (see else clause)
        #
        # To recover the computational graph we need to re-apply it.
        # This implies that the tensors-object we use for the forward
        # pass are different to the passed model. This it not the case
        # for the else clause.
        #
        # Note that reapplying the model does only change the inbound
        # and outbound nodes of the model itself. We copy the model
        # so the passed model should not be affected from the
        # reapplication.

        # For each layer in the model (in forward order),
        # this list tracks the tensors going in and out of it
        executed_nodes: list[tuple[Layer, list[Tensor], list[Tensor]]] = []

        # Monkeypatch the call function in all the used layer classes.
        monkey_patches: list[tuple[Layer, Callable]] = [
            (layer, layer.call) for layer in layers
        ]
        try:

            def patch(self, method: Callable):
                if hasattr(method, "__patched__") is True:
                    raise Exception(
                        "Should not happen as we patch objects, not classes."
                    )

                def patched_fn(*args, **kwargs):
                    input_tensors = args[0]
                    output_tensors = method(*args, **kwargs)
                    executed_nodes.append((self, input_tensors, output_tensors))
                    return output_tensors

                patched_fn.__patched__ = True  # type: ignore
                return patched_fn

            # Apply the patches.
            for layer in layers:
                layer.call = patch(layer, layer.call)

            # Trigger reapplication of model.
            model_copy: Model = kmodels.Model(
                inputs=model.inputs, outputs=model.outputs
            )
            outputs = ibackend.to_list(model_copy(model.inputs))
        finally:
            # Revert the monkey patches
            for layer, old_method in monkey_patches:
                layer.call = old_method

        # Now we have the problem that all the tensors
        # do not have a keras_history attribute as they are not part
        # of any node. Apply the flat model to get it.

        tensor_mapping: dict[Tensor, Tensor] = {tmp: tmp for tmp in model.inputs}
        layer_mapping: dict[Layer, Layer]
        new_executed_nodes: list[tuple[Layer, list[Tensor], list[Tensor]]] = []

        if reapply_on_copied_layers is True:
            layer_mapping = {layer: copy_layer(layer) for layer in layers}
        else:
            layer_mapping = {layer: layer for layer in layers}

        for layer, Xs, Ys in executed_nodes:
            layer = layer_mapping[layer]
            Xs, Ys = ibackend.to_list(Xs), ibackend.to_list(Ys)

            if isinstance(layer, klayers.InputLayer):
                # Special case. Do nothing.
                new_Xs, new_Ys = Xs, Ys
            else:
                new_Xs = [tensor_mapping[x] for x in Xs]
                new_Ys = ibackend.to_list(ibackend.apply(layer, new_Xs))

            # Update values of Ys in tensor_mapping with new_Ys
            tensor_mapping.update(dict(zip(Ys, new_Ys)))
            new_executed_nodes.append((layer, new_Xs, new_Ys))

        layers = [layer_mapping[layer] for layer in layers]
        outputs = [tensor_mapping[x] for x in outputs]
        executed_nodes = new_executed_nodes
    else:
        # Easy and safe way.
        # For each layer in the model (in reverse order),
        # this list tracks the tensors going in and out of it
        reverse_executed_nodes: list[tuple[Layer, list[Tensor], list[Tensor]]]
        reverse_executed_nodes = [
            (
                node.outbound_layer,
                ibackend.to_list(node.input_tensors),
                ibackend.to_list(node.output_tensors),
            )
            for depth in sorted(model._nodes_by_depth.keys())
            for node in model._nodes_by_depth[depth]
        ]
        outputs = model.outputs

        executed_nodes = list(reversed(reverse_executed_nodes))

    # `executed_nodes` potentially contains nodes that are not part
    # of the final execution graph.
    # E.g. if a layer was also applied outside of the model. Then its
    # node list contains nodes that do not contribute to the model's output.
    # Those nodes are filtered here.
    used_as_input = [id(out) for out in outputs]
    tmp = []
    for l, Xs, Ys in reversed(executed_nodes):
        if all(id(Y) in used_as_input for Y in Ys):
            used_as_input += [id(X) for X in Xs]
            tmp.append((l, Xs, Ys))
    executed_nodes = list(reversed(tmp))

    return layers, executed_nodes, outputs


def get_model_execution_trace(
    model: Model,
    keep_input_layers: bool = False,
    reapply_on_copied_layers: bool = False,
) -> list[NodeDict]:
    """
    Returns a list representing the execution graph.
    Each key is the node's id as it is used by the reverse_model method.

    Each associated value contains a dictionary with the following items:

    * `nid`: the node id.
    * `layer`: the layer creating this node.
    * `Xs`: the input tensors (only valid if not in a nested container).
    * `Ys`: the output tensors (only valid if not in a nested container).
    * `Xs_nids`: the ids of the nodes creating the Xs.
    * `Ys_nids`: the ids of nodes using the according output tensor.
    * `Xs_layers`: the layer that created the according input tensor.
    * `Ys_layers`: the layers using the according output tensor.

    :param model: A kera model.
    :param keep_input_layers: Keep input layers.
    :param reapply_on_copied_layers: If the execution needs to be linearized,
      reapply with copied layers. Might be slow. Prevents changes of the
      original layer's node lists.
    """
    # Get execution_trace: list with a linearized execution
    # consisting of `(layer, input_tensors, output_tensors)`.
    execution_trace: list[tuple[Layer, list[Tensor], list[Tensor]]]
    _, execution_trace, _ = trace_model_execution(
        model, reapply_on_copied_layers=reapply_on_copied_layers
    )

    # Enrich execution_trace with node ids to get id_execution_trace
    nid: int | None
    current_nid: int
    id_execution_trace: list[tuple[int | None, Layer, list[Tensor], list[Tensor]]]

    current_nid = 0
    id_execution_trace = []
    for l, Xs, Ys in execution_trace:
        if isinstance(l, klayers.InputLayer):
            id_execution_trace.append((None, l, Xs, Ys))
        else:
            id_execution_trace.append((current_nid, l, Xs, Ys))
            current_nid += 1

    # Create lookups from tensor to creating or receiving layer-node
    inputs_to_node: dict[int, list[int]]
    outputs_to_node: dict[int, int | None]

    inputs_to_node = {}
    outputs_to_node = {}
    for nid, _l, Xs, Ys in id_execution_trace:
        if nid is not None:
            for X in Xs:
                Xid = id(X)
                if Xid in inputs_to_node:
                    inputs_to_node[Xid].append(nid)
                else:
                    inputs_to_node[Xid] = [nid]

        if keep_input_layers or nid is not None:
            for Y in Ys:
                Yid = id(Y)
                if Yid in inputs_to_node:
                    raise Exception("Cannot be more than one creating node.")
                outputs_to_node[Yid] = nid

    # Enrich trace with this info.
    nid_to_nodes: dict[Layer, tuple[int | None, Layer, list[Tensor], list[Tensor]]]
    model_execution_trace: list[NodeDict]

    # TODO: fix invariance of type hints
    Xs_nids: list[int | None]
    Ys_nids: list[list[int] | list[None]]
    # Xs_layers = List[Layer]
    # Ys_layers = List[List[Layer]]

    nid_to_nodes = {t[0]: t for t in id_execution_trace}

    model_execution_trace = []
    for nid, l, Xs, Ys in id_execution_trace:
        if isinstance(l, klayers.InputLayer):
            # The nids that created or receive the tensors.
            Xs_nids = []  # Input layer does not receive.
            Ys_nids = [inputs_to_node[id(Y)] for Y in Ys]
            # The layers that created or receive the tensors.
            Xs_layers = []  # Input layer does not receive.
            Ys_layers = [
                [nid_to_nodes[Ynid][1] for Ynid in Ynids2] for Ynids2 in Ys_nids
            ]
        else:
            # The nids that created or receive the tensors.
            Xs_nids = [outputs_to_node.get(id(X), None) for X in Xs]
            Ys_nids = [inputs_to_node.get(id(Y), [None]) for Y in Ys]
            # The layers that created or receive the tensors.
            Xs_layers = [nid_to_nodes[Xnid][1] for Xnid in Xs_nids if Xnid is not None]
            Ys_layers = [
                [nid_to_nodes[Ynid][1] for Ynid in Ynids2 if Ynid is not None]
                for Ynids2 in Ys_nids
            ]

        entry: NodeDict = {
            "nid": nid,
            "layer": l,
            "Xs": Xs,
            "Ys": Ys,
            "Xs_nids": Xs_nids,
            "Ys_nids": Ys_nids,
            "Xs_layers": Xs_layers,
            "Ys_layers": Ys_layers,
        }
        model_execution_trace.append(entry)

    if not keep_input_layers:
        model_execution_trace = [
            t for t in model_execution_trace if t["nid"] is not None
        ]

    return model_execution_trace


def get_model_execution_graph(
    model: Model, keep_input_layers: bool = False
) -> dict[int | None, NodeDict | list[NodeDict]]:
    """
    Returns a dictionary representing the execution graph.
    Each key is the node's id as it is used by the reverse_model method.

    Each associated value contains a dictionary with the following items:

    * `nid`: the node id.
    * `layer`: the layer creating this node.
    * `Xs`: the input tensors (only valid if not in a nested container).
    * `Ys`: the output tensors (only valid if not in a nested container).
    * `Xs_nids`: the ids of the nodes creating the Xs.
    * `Ys_nids`: the ids of nodes using the according output tensor.
    * `Xs_layers`: the layer that created the according input tensor.
    * `Ys_layers`: the layers using the according output tensor.

    :param model: A kera model.
    :param keep_input_layers: Keep input layers.
    """
    trace: list[NodeDict]
    input_layers: list[NodeDict]
    graph: dict[int | None, NodeDict | list[NodeDict]]

    trace = get_model_execution_trace(
        model, keep_input_layers=keep_input_layers, reapply_on_copied_layers=False
    )

    # Input layers in graph have Node-ID `nid=None`.
    # Extract these from list of all nodes `trace`.
    input_layers = [node for node in trace if node["nid"] is None]

    # Create graph which maps Node-IDs to node information from full trace.
    graph = {node["nid"]: node for node in trace}
    if keep_input_layers:
        graph[None] = input_layers

    return graph


def print_model_execution_graph(
    graph: dict[int | None, OptionalList[NodeDict]]
) -> None:
    """Pretty print of a model execution graph."""
    # TODO: check types

    def nids_as_str(nids: list[int | None]) -> str:  # type: ignore
        return ", ".join([str(nid) for nid in nids])  # type: ignore

    def print_node(node) -> None:
        print(
            f"""[NID: {node["nid"]:d}]
            [Layer: {node["layer"].name:20s}]
            [Inputs from: {nids_as_str(node["Xs_nids"]):20s}]
            [Outputs to: {nids_as_str(node["Ys_nids"]):20s}]"""
        )

    def print_input_node(node) -> None:  # node of type NodeDict?
        print(
            f"""[Layer: {node["layer"].name:20s}]
            [Outputs to: {nids_as_str(node["Ys_nids"]):20s}]"""
        )

    if None in graph:  # Input layers in graph have Node-ID `None`
        print("Graph input layers:")
        for input_node in graph[None]:
            print_input_node(input_node)

    print("Graph nodes:")
    for nid in sorted(key for key in graph if key is not None):
        if nid is None:
            continue
        print_node(graph[nid])


def get_bottleneck_nodes(
    inputs: list[Tensor],
    outputs: list[Tensor],
    execution_list: list[tuple[Layer, list[Tensor], list[Tensor]]],
) -> list[tuple[Layer, tuple[list[Tensor], list[Tensor]]]]:
    """
    Given an execution list this function returns all nodes that
    are a bottleneck in the network, i.e., "all information" must pass
    through this node.
    """
    forward_connections: dict[int, list[Tensor]] = {}
    for l, Xs, Ys in execution_list:
        if isinstance(l, klayers.InputLayer):
            # Special case, do nothing.
            continue

        for X in Xs:
            if id(X) in forward_connections:
                forward_connections[id(X)] += Ys
            else:
                forward_connections[id(X)] = list(Ys)

    open_connections: dict[int, bool] = {}
    for X in inputs:
        for fw_c in forward_connections[id(X)]:
            open_connections[id(fw_c)] = True

    ret = []
    for l, Xs, Ys in execution_list:
        if isinstance(l, klayers.InputLayer):
            # Special case, do nothing.
            # Note: if a single input branches
            # this is not detected.
            continue

        for Y in Ys:
            assert id(Y) in open_connections
            del open_connections[id(Y)]

        if len(open_connections) == 0:
            ret.append((l, (Xs, Ys)))

        for Y in Ys:
            if Y not in outputs:
                for fwc in forward_connections[id(Y)]:
                    open_connections[id(fwc)] = True

    return ret


def get_bottleneck_tensors(
    inputs: list[Tensor],
    outputs: list[Tensor],
    execution_list: list[tuple[Layer, list[Tensor], list[Tensor]]],
) -> list[Tensor]:
    """
    Given an execution list this function returns all tensors that
    are a bottleneck in the network, i.e., "all information" must pass
    through this tensor.
    """
    nodes: list[tuple[Layer, tuple[list[Tensor], list[Tensor]]]]
    nodes = get_bottleneck_nodes(inputs, outputs, execution_list)

    ret: dict[int, Tensor] = {}
    for _l, (Xs, Ys) in nodes:
        for tensor_list in (Xs, Ys):
            if len(tensor_list) == 1:
                tensor = tensor_list[0]
                if id(tensor) not in ret:
                    ret[id(tensor)] = tensor
            else:
                # TODO(albermax): put warning here?
                pass
    return list(ret.values())


###############################################################################


class ReverseMappingBase(metaclass=ABCMeta):
    @abstractmethod
    def apply(
        self,
        Xs: list[Tensor],
        Ys: list[Tensor],
        Rs: list[Tensor],
        reverse_state: dict,
    ) -> list[Tensor]:
        pass


def reverse_model(
    model: Model,
    reverse_mappings,  # TODO: type annotate reverse_mappings
    default_reverse_mapping: Callable | None = None,
    head_mapping: Callable = None,
    stop_mapping_at_tensors: list[Tensor] = None,
    verbose: bool = False,
    return_all_reversed_tensors: bool = False,
    clip_all_reversed_tensors: bool | tuple[float, float] = False,
    project_bottleneck_tensors: bool | tuple[float, float] = False,
    execution_trace: None
    | (
        tuple[list[Layer], list[tuple[Layer, list[Tensor], list[Tensor]]], list[Tensor]]
    ) = None,
    reapply_on_copied_layers: bool = False,
) -> tuple[list[Tensor], dict[Tensor, ReverseTensorDict] | None]:
    """
    Reverses a Keras model based on the given reverse functions.
    Returns two values:

    1. the reverted tensors for the according model inputs.
    2. If `return_all_reversed_tensors` is true, a dictionary of all reversed tensors,
        otherwise None.

    :param model: A Keras model.
    :param reverse_mappings: Either a callable that matches layers to
      mappings or a dictionary with layers as keys and mappings as values.
      Allowed as mapping forms are:

          * A function of form (A) f(Xs, Ys, reversed_Ys, reverse_state).
          * A function of form f(B) f(layer, reverse_state) that returns
            a function of form (A).
          * A :class:`ReverseMappingBase` subclass.

    :param default_reverse_mapping: A function that reverses layers for
      which no mapping was given by param "reverse_mappings".
    :param head_mapping: Map output tensors to new values before passing
      them into the reverted network.
    :param stop_mapping_at_tensors: Tensors at which to stop the mapping.
      Similar to stop_gradient parameters for gradient computation.
    :param verbose: Print what's going on.
    :param return_all_reversed_tensors: Return all reverted tensors in addition
      to reverted model input tensors.
    :param clip_all_reversed_tensors: Clip each reverted tensor. False or tuple
      with min/max value.
    :param project_bottleneck_tensors: Project bottleneck layers in the
      reverting process into a given value range. False, True or (a, b) for
      projection range.
    :param reapply_on_copied_layers: When a model execution needs to
      linearized and copy layers before reapplying them. See
      :func:`trace_model_execution`.
    """

    # Set default values ######################################################
    if stop_mapping_at_tensors is None:
        stop_mapping_at_tensors = []

    stop_mapping_at_ids = [id(X) for X in stop_mapping_at_tensors]

    if head_mapping is None:

        def head_mapping(X):
            return X

    if not callable(reverse_mappings):
        # not callable, assume a dict that maps from layer to mapping
        reverse_mapping_data = reverse_mappings

        def reverse_mappings(layer):
            try:
                return reverse_mapping_data[type(layer)]
            except KeyError:
                return None

    if clip_all_reversed_tensors is True:
        raise NotImplementedError(
            "Keyword argument `clip_all_reversed_tensors` ",
            "expected to be `False` or tuple with min/max values.",
        )

    def _print(x):
        if verbose is True:
            print(x)

    # Initialize structure that keeps track of reversed tensors
    # maps tensor to reverse tensor and additional node information
    reversed_tensors: dict[int, ReverseTensorDict]
    reversed_tensors = {}

    bottleneck_tensor_ids: set[int] = set()

    def add_reversed_tensors(nid, tensors_list, reversed_tensors_list) -> None:
        def add_reversed_tensor(i, X: Tensor, reversed_X: Tensor) -> None:
            # reversed_X corresponds to the reverse-propagated relevance
            # or the output (e.g. max neuron activation)

            # Do not keep tensors that should stop the mapping.
            if id(X) in stop_mapping_at_ids:
                return

            if reversed_X is None:
                raise TypeError(
                    "Propagated relevance `reversed_X` is None, "
                    "is expected to be Tensor."
                )

            if (
                id(X) not in reversed_tensors
            ):  # no duplicate entries for forward tensors
                reversed_tensors[id(X)] = {
                    "nid": (nid, i),
                    "tensors": [reversed_X],
                    "final_tensor": None,
                }
            else:  # more than one tensor propagating relevance to X
                reversed_tensors[id(X)]["tensors"].append(reversed_X)

        tmp = zip(tensors_list, reversed_tensors_list)
        for i, (X, reversed_X) in enumerate(tmp):
            add_reversed_tensor(i, X, reversed_X)

    def get_reversed_tensor(tensor: Tensor) -> Tensor:
        tmp: ReverseTensorDict
        tmp = reversed_tensors[id(tensor)]

        if tmp["final_tensor"] is None:
            if len(tmp["tensors"]) == 1:
                final_tensor = tmp["tensors"][0]
            elif len(tmp["tensors"]) > 1:
                final_tensor = klayers.Add()(tmp["tensors"])
            else:
                raise RuntimeError(
                    f"Error during graph reversal: no tensors connected to {tensor}."
                )

            if project_bottleneck_tensors is True:
                if id(tensor) in bottleneck_tensor_ids:
                    project = ilayers.Project(project_bottleneck_tensors)
                    final_tensor = project(final_tensor)

            if isinstance(clip_all_reversed_tensors, tuple):
                clip = ilayers.Clip(*clip_all_reversed_tensors)
                final_tensor = clip(final_tensor)

            tmp["final_tensor"] = final_tensor

        return tmp["final_tensor"]

    # Reverse the model #######################################################
    _print(f"Reverse model: {model}")

    # Create a list with nodes in reverse execution order.
    if execution_trace is None:
        execution_trace = trace_model_execution(
            model, reapply_on_copied_layers=reapply_on_copied_layers
        )
    layers, execution_list, outputs = execution_trace
    reverse_execution_list = reversed(execution_list)

    len_execution_list = len(execution_list)
    num_input_layers = sum(isinstance(l, klayers.InputLayer) for l in layers)
    len_execution_list_wo_inputs_layers = len_execution_list - num_input_layers

    # Initialize the reverse mapping functions.
    initialized_reverse_mappings: dict[Layer, Callable]  # TODO: specify Callable
    initialized_reverse_mappings = {}
    for layer in layers:
        # A layer can be shared, i.e., applied several times.
        # Allow to share a ReverMappingBase for each layer instance
        # in order to reduce the overhead.

        meta_reverse_mapping = reverse_mappings(layer)
        if meta_reverse_mapping is None:
            reverse_mapping = default_reverse_mapping
        elif inspect.isclass(meta_reverse_mapping) and issubclass(
            meta_reverse_mapping, ReverseMappingBase
        ):
            # Mapping is a class
            reverse_mapping_obj = meta_reverse_mapping(
                layer,
                {
                    "model": model,
                    "layer": layer,
                },
            )
            reverse_mapping = reverse_mapping_obj.apply
        else:

            def parameter_count(func):
                if hasattr(inspect, "signature"):
                    ret = len(inspect.signature(func).parameters)
                else:
                    spec = inspect.getargspec(func)
                    ret = len(spec.args)
                    if spec.varargs is not None:
                        ret += len(spec.varargs)
                    if spec.keywords is not None:
                        ret += len(spec.keywords)
                    if ret == 3:
                        # assume class function with self
                        ret -= 1
                return ret

            if (
                callable(meta_reverse_mapping)
                and parameter_count(meta_reverse_mapping) == 2
            ):
                # Function that returns mapping
                reverse_mapping = meta_reverse_mapping(
                    layer,
                    {
                        "model": model,
                        "layer": layer,
                    },
                )
            else:
                # Nothing meta here
                reverse_mapping = meta_reverse_mapping

        # TODO: add annotations
        initialized_reverse_mappings[layer] = reverse_mapping  # type: ignore

    if project_bottleneck_tensors:
        ids = [
            id(X) for X in get_bottleneck_tensors(model.inputs, outputs, execution_list)
        ]
        bottleneck_tensor_ids.update(ids)

    # Initialize the reverse tensor mappings.
    add_reversed_tensors(-1, outputs, [head_mapping(tmp) for tmp in outputs])  # type: ignore # noqa

    # Follow the list and revert the graph.
    for _nid, (layer, Xs, Ys) in enumerate(reverse_execution_list):
        nid = len_execution_list_wo_inputs_layers - _nid - 1

        if isinstance(layer, klayers.InputLayer):
            # Special case. Do nothing.
            pass
        elif ichecks.is_module(layer):
            raise Exception("This is not supposed to happen!")
        else:
            Xs, Ys = ibackend.to_list(Xs), ibackend.to_list(Ys)
            if not all(id(Y) in reversed_tensors for Y in Ys):
                # This node is not part of our computational graph.
                # The (node-)world is bigger than this model.
                # Potentially this node is also not part of the
                # reversed tensor set because it depends on a tensor
                # that is listed in stop_mapping_at_ids.
                continue
            reversed_Ys = [get_reversed_tensor(Y) for Y in Ys]
            local_stop_mapping_at_ids = [
                id(X) for X in Xs if id(X) in stop_mapping_at_ids
            ]

            _print(f"[NID: {nid}] Reverse layer-node {layer}")
            reverse_mapping = initialized_reverse_mappings[layer]
            reversed_Xs = reverse_mapping(
                Xs,
                Ys,
                reversed_Ys,
                {
                    "nid": nid,
                    "model": model,
                    "layer": layer,
                    "stop_mapping_at_ids": local_stop_mapping_at_ids,
                },
            )
            reversed_Xs = ibackend.to_list(reversed_Xs)
            add_reversed_tensors(nid, Xs, reversed_Xs)

    # Return requested values
    reversed_input_tensors = [
        get_reversed_tensor(tmp)
        for tmp in model.inputs
        if id(tmp) not in stop_mapping_at_ids
    ]
    if return_all_reversed_tensors is True:
        return reversed_input_tensors, reversed_tensors
    return reversed_input_tensors, None
