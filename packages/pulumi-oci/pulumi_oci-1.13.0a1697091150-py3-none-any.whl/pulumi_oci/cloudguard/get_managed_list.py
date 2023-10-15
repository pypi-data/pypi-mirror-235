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
    'GetManagedListResult',
    'AwaitableGetManagedListResult',
    'get_managed_list',
    'get_managed_list_output',
]

@pulumi.output_type
class GetManagedListResult:
    """
    A collection of values returned by getManagedList.
    """
    def __init__(__self__, compartment_id=None, defined_tags=None, description=None, display_name=None, feed_provider=None, freeform_tags=None, id=None, is_editable=None, lifecyle_details=None, list_items=None, list_type=None, managed_list_id=None, source_managed_list_id=None, state=None, system_tags=None, time_created=None, time_updated=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if feed_provider and not isinstance(feed_provider, str):
            raise TypeError("Expected argument 'feed_provider' to be a str")
        pulumi.set(__self__, "feed_provider", feed_provider)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_editable and not isinstance(is_editable, bool):
            raise TypeError("Expected argument 'is_editable' to be a bool")
        pulumi.set(__self__, "is_editable", is_editable)
        if lifecyle_details and not isinstance(lifecyle_details, str):
            raise TypeError("Expected argument 'lifecyle_details' to be a str")
        pulumi.set(__self__, "lifecyle_details", lifecyle_details)
        if list_items and not isinstance(list_items, list):
            raise TypeError("Expected argument 'list_items' to be a list")
        pulumi.set(__self__, "list_items", list_items)
        if list_type and not isinstance(list_type, str):
            raise TypeError("Expected argument 'list_type' to be a str")
        pulumi.set(__self__, "list_type", list_type)
        if managed_list_id and not isinstance(managed_list_id, str):
            raise TypeError("Expected argument 'managed_list_id' to be a str")
        pulumi.set(__self__, "managed_list_id", managed_list_id)
        if source_managed_list_id and not isinstance(source_managed_list_id, str):
            raise TypeError("Expected argument 'source_managed_list_id' to be a str")
        pulumi.set(__self__, "source_managed_list_id", source_managed_list_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        Compartment Identifier where the resource is created
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        ManagedList description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        ManagedList display name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="feedProvider")
    def feed_provider(self) -> str:
        """
        provider of the feed
        """
        return pulumi.get(self, "feed_provider")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Unique identifier that is immutable on creation
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isEditable")
    def is_editable(self) -> bool:
        """
        If this list is editable or not
        """
        return pulumi.get(self, "is_editable")

    @property
    @pulumi.getter(name="lifecyleDetails")
    def lifecyle_details(self) -> str:
        """
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        """
        return pulumi.get(self, "lifecyle_details")

    @property
    @pulumi.getter(name="listItems")
    def list_items(self) -> Sequence[str]:
        """
        List of ManagedListItem
        """
        return pulumi.get(self, "list_items")

    @property
    @pulumi.getter(name="listType")
    def list_type(self) -> str:
        """
        type of the list
        """
        return pulumi.get(self, "list_type")

    @property
    @pulumi.getter(name="managedListId")
    def managed_list_id(self) -> str:
        return pulumi.get(self, "managed_list_id")

    @property
    @pulumi.getter(name="sourceManagedListId")
    def source_managed_list_id(self) -> str:
        """
        OCID of the Source ManagedList
        """
        return pulumi.get(self, "source_managed_list_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the resource.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system.  Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the managed list was created. Format defined by RFC3339.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The date and time the managed list was updated. Format defined by RFC3339.
        """
        return pulumi.get(self, "time_updated")


class AwaitableGetManagedListResult(GetManagedListResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedListResult(
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            description=self.description,
            display_name=self.display_name,
            feed_provider=self.feed_provider,
            freeform_tags=self.freeform_tags,
            id=self.id,
            is_editable=self.is_editable,
            lifecyle_details=self.lifecyle_details,
            list_items=self.list_items,
            list_type=self.list_type,
            managed_list_id=self.managed_list_id,
            source_managed_list_id=self.source_managed_list_id,
            state=self.state,
            system_tags=self.system_tags,
            time_created=self.time_created,
            time_updated=self.time_updated)


def get_managed_list(managed_list_id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedListResult:
    """
    This data source provides details about a specific Managed List resource in Oracle Cloud Infrastructure Cloud Guard service.

    Returns a managed list identified by managedListId

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_list = oci.CloudGuard.get_managed_list(managed_list_id=oci_cloud_guard_managed_list["test_managed_list"]["id"])
    ```


    :param str managed_list_id: The cloudguard list OCID to be passed in the request.
    """
    __args__ = dict()
    __args__['managedListId'] = managed_list_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:CloudGuard/getManagedList:getManagedList', __args__, opts=opts, typ=GetManagedListResult).value

    return AwaitableGetManagedListResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        feed_provider=pulumi.get(__ret__, 'feed_provider'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        is_editable=pulumi.get(__ret__, 'is_editable'),
        lifecyle_details=pulumi.get(__ret__, 'lifecyle_details'),
        list_items=pulumi.get(__ret__, 'list_items'),
        list_type=pulumi.get(__ret__, 'list_type'),
        managed_list_id=pulumi.get(__ret__, 'managed_list_id'),
        source_managed_list_id=pulumi.get(__ret__, 'source_managed_list_id'),
        state=pulumi.get(__ret__, 'state'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'))


@_utilities.lift_output_func(get_managed_list)
def get_managed_list_output(managed_list_id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedListResult]:
    """
    This data source provides details about a specific Managed List resource in Oracle Cloud Infrastructure Cloud Guard service.

    Returns a managed list identified by managedListId

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_list = oci.CloudGuard.get_managed_list(managed_list_id=oci_cloud_guard_managed_list["test_managed_list"]["id"])
    ```


    :param str managed_list_id: The cloudguard list OCID to be passed in the request.
    """
    ...
