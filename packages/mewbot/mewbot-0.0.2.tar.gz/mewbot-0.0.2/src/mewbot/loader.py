#!/use/bin/env python3

# SPDX-FileCopyrightText: 2021 - 2023 Mewbot Developers <mewbot@quicksilver.london>
#
# SPDX-License-Identifier: BSD-2-Clause

"""
Provides functions to load mewbot components from YAML.
"""

from __future__ import annotations

from typing import Any, TextIO, Type

import importlib
import sys

import yaml

from mewbot.bot import Bot
from mewbot.core import (
    ActionInterface,
    BehaviourConfigBlock,
    BehaviourInterface,
    Component,
    ComponentKind,
    ConditionInterface,
    ConfigBlock,
    IOConfigInterface,
    TriggerInterface,
)

_REQUIRED_KEYS = set(ConfigBlock.__annotations__.keys())  # pylint: disable=no-member


def assert_message(obj: Any, interface: Type[Any]) -> str:
    """Generates the assert error message for an incomplete interface."""

    uuid = getattr(obj, "uuid", "<unknown>")
    return (
        f"Loaded component did not implemented expected interface {interface}. "
        f"Loaded component: type={type(obj)}, uuid={uuid}, info={str(obj)}"
    )


def configure_bot(name: str, stream: TextIO) -> Bot:
    """
    Loads a series of components from a YAML file to crate a bot.

    The YAML is expected to be a series of IOConfig, DataSource, and Behaviour blocks.

    :param name: The name of the bot
    :param stream: YAML which defined the bot.
    """

    bot = Bot(name)
    number = 0

    for document in yaml.load_all(stream, Loader=yaml.CSafeLoader):
        number += 1

        if not _REQUIRED_KEYS.issubset(document.keys()):
            raise ValueError(
                f"Document {number} missing some keys: {_REQUIRED_KEYS.difference(document.keys())}"
            )

        if document["kind"] == ComponentKind.Behaviour:
            bot.add_behaviour(load_behaviour(document))
        if document["kind"] == ComponentKind.DataSource:
            ...
        if document["kind"] == ComponentKind.IOConfig:
            component = load_component(document)
            assert isinstance(component, IOConfigInterface), assert_message(
                component, IOConfigInterface
            )
            bot.add_io_config(component)

    return bot


def load_behaviour(config: BehaviourConfigBlock) -> BehaviourInterface:
    """Creates a behaviour and its components based on a configuration block."""

    behaviour = load_component(config)

    assert isinstance(behaviour, BehaviourInterface)

    for trigger_definition in config["triggers"]:
        trigger = load_component(trigger_definition)
        assert isinstance(trigger, TriggerInterface), assert_message(
            trigger, TriggerInterface
        )
        behaviour.add(trigger)

    for condition_definition in config["conditions"]:
        condition = load_component(condition_definition)
        assert isinstance(condition, ConditionInterface), assert_message(
            condition, ConditionInterface
        )
        behaviour.add(condition)

    for action_definition in config["actions"]:
        action = load_component(action_definition)
        assert isinstance(action, ActionInterface), assert_message(action, ActionInterface)
        behaviour.add(action)

    return behaviour


def load_component(config: ConfigBlock) -> Component:
    """Creates a component based on a configuration block."""

    # Ensure that the object we have been passed contains all required fields.
    if not _REQUIRED_KEYS.issubset(config.keys()):
        raise ValueError(
            f"Config missing some keys: {_REQUIRED_KEYS.difference(config.keys())}"
        )

    # Identify the kind of component we should be loading, and the interface that implies.
    try:
        kind = ComponentKind[config["kind"]]
        interface = ComponentKind.interface(kind)
    except KeyError as err:
        raise ValueError(f"Invalid component kind {config['kind']}") from err

    # Locate the implementation class to be loaded
    target_class = get_implementation(config["implementation"])

    # Verify that the implementation class matches the interface we got from
    # the `kind:` hint.
    if not issubclass(target_class, interface):
        raise TypeError(
            f"Class {target_class} does not implement {interface}, requested by {config}"
        )

    # Create the class instance, passing in the properties.
    component = target_class(uid=config["uuid"], **config["properties"])

    # Verify the instance implements a valid interface.
    # The second call is to reassure the linter that the types are correct.
    assert isinstance(component, interface), assert_message(component, interface)
    assert isinstance(
        component,
        (
            IOConfigInterface,
            BehaviourInterface,
            TriggerInterface,
            ConditionInterface,
            ActionInterface,
        ),
    )

    return component


def get_implementation(implementation: str) -> Type[Any]:
    """
    Gets a Class object from a module based on a fully-qualified name.

    This will attempt to load the module if it is not already loaded.
    """

    # Load the module the component is expected to be in.
    module_name, class_name = implementation.rsplit(".", 1)

    if module_name not in sys.modules:
        importlib.import_module(module_name)

    module = sys.modules[module_name]

    if not hasattr(module, class_name):
        raise TypeError(f"Unable to find implementation {class_name} in module {module_name}")

    target_class: Type[Component] = getattr(module, class_name)

    return target_class
