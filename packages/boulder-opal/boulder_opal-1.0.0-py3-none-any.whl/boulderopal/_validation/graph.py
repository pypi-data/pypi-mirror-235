# Copyright 2023 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#    https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.

from __future__ import annotations

from collections import deque
from itertools import chain
from typing import (
    TYPE_CHECKING,
    Iterable,
)

from qctrlcommons.exceptions import QctrlArgumentsValueError
from qctrlcommons.node.wrapper import (
    NodeData,
    Operation,
)
from qctrlcommons.preconditions import check_argument

from boulderopal._nodes.registry import PRIMARY_NODE_REGISTRY

if TYPE_CHECKING:
    from boulderopal.graph import Graph


def validate_output_node_names(
    node_names: str | list[str], graph: "Graph"
) -> list[str]:
    """
    Validate the names of the output nodes for fetching from a graph.

    If any node is not in the graph, raise an error. Otherwise, normalize the names to a list of
    strings.

    Parameters
    ---------
    node_names : str or list[str]
        Name of the nodes to be fetched.
    graph : Graph
        The graph where the nodes are supposed to be fetched from.

    Returns
    -------
    list[str]
        A list of valid node names.
    """

    if isinstance(node_names, str):
        node_names = [node_names]

    check_argument(
        isinstance(node_names, list)
        and all(isinstance(name, str) for name in node_names),
        "The output node names must be a string or a list of strings.",
        {"output_node_names": node_names},
    )

    check_argument(
        len(node_names) >= 1,
        "The output node names must have at least one element.",
        {"output_node_names": node_names},
    )

    for name in node_names:
        check_node_in_graph(
            name,
            graph,
            f"The requested output node name '{name}' is not present in the graph.",
        )

    return node_names


def check_node_in_graph(node: str, graph: "Graph", message: str) -> None:
    """
    Check if a node is in the Graph.

    Parameters
    ----------
    node : str
        The name of the node.
    graph : Graph
        The Graph to be validated.
    message : str
        The error message.
    """
    check_argument(
        node in graph.operations, message, {"graph": graph}, extras={"node name": node}
    )


def check_optimization_node_in_graph(graph: "Graph") -> None:
    """
    Check optimization graph at least has one optimization node.
    """
    for operation in graph.operations.values():
        if PRIMARY_NODE_REGISTRY.get_node_cls(
            operation.operation_name
        ).optimizable_variable:
            return
    raise QctrlArgumentsValueError(
        "At least one optimization variable is required in the optimization graph.",
        {"graph": graph},
    )


def check_cost_node(node: str, graph: Graph) -> None:
    """
    Check cost node:
        - if the node is in the graph.
        - if the node is a scalar Tensor.
    """
    check_argument(
        isinstance(node, str),
        "The cost node name must be a string.",
        {"cost_node_name": node},
    )
    check_node_in_graph(node, graph, "A cost node must be present in the graph.")
    check_argument(
        graph.operations[node].is_scalar_tensor,
        "The cost node must be a scalar Tensor.",
        {"cost": node},
        extras={"cost node operation": graph.operations[node]},
    )


def check_cost_node_for_optimization_graph(
    graph: Graph,
    cost_node_name: str,
    output_node_names: list[str],
    check_gradient_nodes: bool = True,
) -> None:
    """
    Traverse the graph from the cost node, and check:
        1. All connected the nodes should support gradient if `check_gradient_nodes` is True.
        2. Any optimizable node to be fetched should connect to the cost node.
    """

    connected_optimization_node_names = set()

    def _validate_node_from_operation(operation: Operation) -> None:
        node = PRIMARY_NODE_REGISTRY.get_node_cls(operation.operation_name)
        if check_gradient_nodes:
            check_argument(
                node.supports_gradient,
                f"The {operation.operation_name} node does not support gradient.",
                {"graph": graph},
            )
        if node.optimizable_variable:
            connected_optimization_node_names.add(operation.name)

    def _get_parent_operations(node: str) -> Iterable[Operation]:
        """
        Go through inputs of the nodes, which might include Python primitive iterables.
        Find all NodeData and flat them as a single iterable.
        """

        def _get_input_items(input_: Iterable) -> Iterable:
            if isinstance(input_, NodeData):
                return [input_.operation]
            if isinstance(input_, (list, tuple)):
                return chain.from_iterable(_get_input_items(item) for item in input_)
            if isinstance(input_, dict):
                return chain.from_iterable(
                    _get_input_items(item) for item in input_.values()
                )
            return []

        return chain.from_iterable(
            _get_input_items(input_)
            for input_ in graph.operations[node].kwargs.values()
        )

    visited_nodes: set[str] = set()
    nodes_to_check: deque = deque()

    # cost node is where we start with.
    _validate_node_from_operation(graph.operations[cost_node_name])
    visited_nodes.add(cost_node_name)
    nodes_to_check.appendleft(cost_node_name)

    while nodes_to_check:
        node = nodes_to_check.pop()

        for operation in _get_parent_operations(node):
            if operation.name not in visited_nodes:
                _validate_node_from_operation(operation)
                visited_nodes.add(operation.name)
                nodes_to_check.appendleft(operation.name)

    # Graph traverse is done and all connected optimization nodes are recorded.
    # Now check output nodes.
    for output_node in output_node_names:
        op_name = graph.operations[output_node].operation_name
        if PRIMARY_NODE_REGISTRY.get_node_cls(op_name).optimizable_variable:
            check_argument(
                output_node in connected_optimization_node_names,
                "The requested optimization node in `output_node_names` is not connected "
                "to the cost node.",
                {"output_node_names": output_node_names},
                extras={"disconnected output node name": output_node},
            )


def check_initial_value_for_optimization_node(graph: Graph) -> None:
    """
    Check optimization node has valid non-default initial values.
    """

    initial_value_info = {}

    for name, operation in graph.operations.items():
        node = PRIMARY_NODE_REGISTRY.get_node_cls(operation.operation_name)
        if (
            node.optimizable_variable
            and operation.kwargs.get("initial_values") is not None
        ):
            initial_value_info[name] = operation.kwargs["initial_values"]

    initial_values = list(initial_value_info.values())
    if len(initial_values) != 0:
        for val in initial_values[1:]:
            if not isinstance(val, type(initial_values[0])):
                raise QctrlArgumentsValueError(
                    "Non-default initial values of optimization variables in the graph"
                    " must all either be an array or a list of arrays.",
                    {"graph": graph},
                    extras=initial_value_info,
                )

        if isinstance(initial_values[0], list):
            for val in initial_values[1:]:
                if len(val) != len(initial_values[0]):
                    raise QctrlArgumentsValueError(
                        "Lists of initial values of optimization variables must have "
                        "the same length.",
                        {"graph": graph},
                        extras=initial_value_info,
                    )
