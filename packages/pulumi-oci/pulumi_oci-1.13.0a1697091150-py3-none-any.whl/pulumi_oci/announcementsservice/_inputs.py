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
    'AnnouncementSubscriptionFilterGroupsArgs',
    'AnnouncementSubscriptionFilterGroupsFilterArgs',
    'AnnouncementSubscriptionsFilterGroupFilterArgs',
    'GetAnnouncementSubscriptionsFilterArgs',
]

@pulumi.input_type
class AnnouncementSubscriptionFilterGroupsArgs:
    def __init__(__self__, *,
                 filters: pulumi.Input[Sequence[pulumi.Input['AnnouncementSubscriptionFilterGroupsFilterArgs']]],
                 name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input['AnnouncementSubscriptionFilterGroupsFilterArgs']]] filters: A list of filters against which the Announcements service matches announcements. You cannot have more than one of any given filter type within a filter group.
        :param pulumi.Input[str] name: The name of the group. The name must be unique and it cannot be changed. Avoid entering confidential information.
        """
        AnnouncementSubscriptionFilterGroupsArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            filters=filters,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             filters: pulumi.Input[Sequence[pulumi.Input['AnnouncementSubscriptionFilterGroupsFilterArgs']]],
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("filters", filters)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter
    def filters(self) -> pulumi.Input[Sequence[pulumi.Input['AnnouncementSubscriptionFilterGroupsFilterArgs']]]:
        """
        A list of filters against which the Announcements service matches announcements. You cannot have more than one of any given filter type within a filter group.
        """
        return pulumi.get(self, "filters")

    @filters.setter
    def filters(self, value: pulumi.Input[Sequence[pulumi.Input['AnnouncementSubscriptionFilterGroupsFilterArgs']]]):
        pulumi.set(self, "filters", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the group. The name must be unique and it cannot be changed. Avoid entering confidential information.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class AnnouncementSubscriptionFilterGroupsFilterArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        :param pulumi.Input[str] type: The type of filter.
        :param pulumi.Input[str] value: The value of the filter.
        """
        AnnouncementSubscriptionFilterGroupsFilterArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            type=type,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             type: pulumi.Input[str],
             value: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("type", type)
        _setter("value", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of filter.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value of the filter.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class AnnouncementSubscriptionsFilterGroupFilterArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        :param pulumi.Input[str] type: (Updatable) The type of filter.
        :param pulumi.Input[str] value: (Updatable) The value of the filter.
        """
        AnnouncementSubscriptionsFilterGroupFilterArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            type=type,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             type: pulumi.Input[str],
             value: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("type", type)
        _setter("value", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        (Updatable) The type of filter.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        (Updatable) The value of the filter.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class GetAnnouncementSubscriptionsFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str],
                 regex: Optional[bool] = None):
        """
        :param str name: The name of the group. The name must be unique and it cannot be changed. Avoid entering confidential information.
        """
        GetAnnouncementSubscriptionsFilterArgs._configure(
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
        The name of the group. The name must be unique and it cannot be changed. Avoid entering confidential information.
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


