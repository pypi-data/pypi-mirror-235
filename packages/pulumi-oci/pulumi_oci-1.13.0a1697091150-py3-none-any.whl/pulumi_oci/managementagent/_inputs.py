# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'ManagementAgentManagementAgentPropertyArgs',
    'ManagementAgentPluginListArgs',
    'GetManagementAgentAvailableHistoriesFilterArgs',
    'GetManagementAgentImagesFilterArgs',
    'GetManagementAgentInstallKeysFilterArgs',
    'GetManagementAgentPluginsFilterArgs',
    'GetManagementAgentsFilterArgs',
]

@pulumi.input_type
class ManagementAgentManagementAgentPropertyArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 units: Optional[pulumi.Input[str]] = None,
                 values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] name: Name of the property
        :param pulumi.Input[str] units: Unit for the property
        :param pulumi.Input[Sequence[pulumi.Input[str]]] values: Values of the property
        """
        ManagementAgentManagementAgentPropertyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            units=units,
            values=values,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[pulumi.Input[str]] = None,
             units: Optional[pulumi.Input[str]] = None,
             values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if name is not None:
            _setter("name", name)
        if units is not None:
            _setter("units", units)
        if values is not None:
            _setter("values", values)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the property
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def units(self) -> Optional[pulumi.Input[str]]:
        """
        Unit for the property
        """
        return pulumi.get(self, "units")

    @units.setter
    def units(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "units", value)

    @property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Values of the property
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "values", value)


@pulumi.input_type
class ManagementAgentPluginListArgs:
    def __init__(__self__, *,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 plugin_display_name: Optional[pulumi.Input[str]] = None,
                 plugin_id: Optional[pulumi.Input[str]] = None,
                 plugin_name: Optional[pulumi.Input[str]] = None,
                 plugin_status: Optional[pulumi.Input[str]] = None,
                 plugin_status_message: Optional[pulumi.Input[str]] = None,
                 plugin_version: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[bool] is_enabled: flag indicating whether the plugin is in enabled mode or disabled mode.
        :param pulumi.Input[str] plugin_display_name: Management Agent Plugin Identifier, can be renamed
        :param pulumi.Input[str] plugin_id: Plugin Id
        :param pulumi.Input[str] plugin_name: Management Agent Plugin Name
        :param pulumi.Input[str] plugin_status: Plugin Status
        :param pulumi.Input[str] plugin_status_message: Status message of the Plugin
        :param pulumi.Input[str] plugin_version: Plugin Version
        """
        ManagementAgentPluginListArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            is_enabled=is_enabled,
            plugin_display_name=plugin_display_name,
            plugin_id=plugin_id,
            plugin_name=plugin_name,
            plugin_status=plugin_status,
            plugin_status_message=plugin_status_message,
            plugin_version=plugin_version,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             is_enabled: Optional[pulumi.Input[bool]] = None,
             plugin_display_name: Optional[pulumi.Input[str]] = None,
             plugin_id: Optional[pulumi.Input[str]] = None,
             plugin_name: Optional[pulumi.Input[str]] = None,
             plugin_status: Optional[pulumi.Input[str]] = None,
             plugin_status_message: Optional[pulumi.Input[str]] = None,
             plugin_version: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if is_enabled is not None:
            _setter("is_enabled", is_enabled)
        if plugin_display_name is not None:
            _setter("plugin_display_name", plugin_display_name)
        if plugin_id is not None:
            _setter("plugin_id", plugin_id)
        if plugin_name is not None:
            _setter("plugin_name", plugin_name)
        if plugin_status is not None:
            _setter("plugin_status", plugin_status)
        if plugin_status_message is not None:
            _setter("plugin_status_message", plugin_status_message)
        if plugin_version is not None:
            _setter("plugin_version", plugin_version)

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        flag indicating whether the plugin is in enabled mode or disabled mode.
        """
        return pulumi.get(self, "is_enabled")

    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_enabled", value)

    @property
    @pulumi.getter(name="pluginDisplayName")
    def plugin_display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Management Agent Plugin Identifier, can be renamed
        """
        return pulumi.get(self, "plugin_display_name")

    @plugin_display_name.setter
    def plugin_display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "plugin_display_name", value)

    @property
    @pulumi.getter(name="pluginId")
    def plugin_id(self) -> Optional[pulumi.Input[str]]:
        """
        Plugin Id
        """
        return pulumi.get(self, "plugin_id")

    @plugin_id.setter
    def plugin_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "plugin_id", value)

    @property
    @pulumi.getter(name="pluginName")
    def plugin_name(self) -> Optional[pulumi.Input[str]]:
        """
        Management Agent Plugin Name
        """
        return pulumi.get(self, "plugin_name")

    @plugin_name.setter
    def plugin_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "plugin_name", value)

    @property
    @pulumi.getter(name="pluginStatus")
    def plugin_status(self) -> Optional[pulumi.Input[str]]:
        """
        Plugin Status
        """
        return pulumi.get(self, "plugin_status")

    @plugin_status.setter
    def plugin_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "plugin_status", value)

    @property
    @pulumi.getter(name="pluginStatusMessage")
    def plugin_status_message(self) -> Optional[pulumi.Input[str]]:
        """
        Status message of the Plugin
        """
        return pulumi.get(self, "plugin_status_message")

    @plugin_status_message.setter
    def plugin_status_message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "plugin_status_message", value)

    @property
    @pulumi.getter(name="pluginVersion")
    def plugin_version(self) -> Optional[pulumi.Input[str]]:
        """
        Plugin Version
        """
        return pulumi.get(self, "plugin_version")

    @plugin_version.setter
    def plugin_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "plugin_version", value)


@pulumi.input_type
class GetManagementAgentAvailableHistoriesFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str],
                 regex: Optional[bool] = None):
        GetManagementAgentAvailableHistoriesFilterArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            values=values,
            regex=regex,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: str,
             values: Sequence[str],
             regex: Optional[bool] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("name", name)
        _setter("values", values)
        if regex is not None:
            _setter("regex", regex)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def regex(self) -> Optional[bool]:
        return pulumi.get(self, "regex")

    @regex.setter
    def regex(self, value: Optional[bool]):
        pulumi.set(self, "regex", value)


@pulumi.input_type
class GetManagementAgentImagesFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str],
                 regex: Optional[bool] = None):
        """
        :param str name: A filter to return only resources that match the entire platform name given.
        """
        GetManagementAgentImagesFilterArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            values=values,
            regex=regex,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: str,
             values: Sequence[str],
             regex: Optional[bool] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("name", name)
        _setter("values", values)
        if regex is not None:
            _setter("regex", regex)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A filter to return only resources that match the entire platform name given.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def regex(self) -> Optional[bool]:
        return pulumi.get(self, "regex")

    @regex.setter
    def regex(self, value: Optional[bool]):
        pulumi.set(self, "regex", value)


@pulumi.input_type
class GetManagementAgentInstallKeysFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str],
                 regex: Optional[bool] = None):
        GetManagementAgentInstallKeysFilterArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            values=values,
            regex=regex,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: str,
             values: Sequence[str],
             regex: Optional[bool] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("name", name)
        _setter("values", values)
        if regex is not None:
            _setter("regex", regex)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def regex(self) -> Optional[bool]:
        return pulumi.get(self, "regex")

    @regex.setter
    def regex(self, value: Optional[bool]):
        pulumi.set(self, "regex", value)


@pulumi.input_type
class GetManagementAgentPluginsFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str],
                 regex: Optional[bool] = None):
        """
        :param str name: Management Agent Plugin Name
        """
        GetManagementAgentPluginsFilterArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            values=values,
            regex=regex,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: str,
             values: Sequence[str],
             regex: Optional[bool] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("name", name)
        _setter("values", values)
        if regex is not None:
            _setter("regex", regex)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Management Agent Plugin Name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def regex(self) -> Optional[bool]:
        return pulumi.get(self, "regex")

    @regex.setter
    def regex(self, value: Optional[bool]):
        pulumi.set(self, "regex", value)


@pulumi.input_type
class GetManagementAgentsFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str],
                 regex: Optional[bool] = None):
        """
        :param str name: Name of the property
        :param Sequence[str] values: Values of the property
        """
        GetManagementAgentsFilterArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            values=values,
            regex=regex,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: str,
             values: Sequence[str],
             regex: Optional[bool] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("name", name)
        _setter("values", values)
        if regex is not None:
            _setter("regex", regex)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the property
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        """
        Values of the property
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def regex(self) -> Optional[bool]:
        return pulumi.get(self, "regex")

    @regex.setter
    def regex(self, value: Optional[bool]):
        pulumi.set(self, "regex", value)


