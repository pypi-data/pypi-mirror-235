# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetManagedInstanceStreamProfileResult',
    'AwaitableGetManagedInstanceStreamProfileResult',
    'get_managed_instance_stream_profile',
    'get_managed_instance_stream_profile_output',
]

@pulumi.output_type
class GetManagedInstanceStreamProfileResult:
    """
    A collection of values returned by getManagedInstanceStreamProfile.
    """
    def __init__(__self__, compartment_id=None, filters=None, id=None, managed_instance_id=None, module_name=None, module_stream_profile_on_managed_instances=None, profile_name=None, profile_status=None, stream_name=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if managed_instance_id and not isinstance(managed_instance_id, str):
            raise TypeError("Expected argument 'managed_instance_id' to be a str")
        pulumi.set(__self__, "managed_instance_id", managed_instance_id)
        if module_name and not isinstance(module_name, str):
            raise TypeError("Expected argument 'module_name' to be a str")
        pulumi.set(__self__, "module_name", module_name)
        if module_stream_profile_on_managed_instances and not isinstance(module_stream_profile_on_managed_instances, list):
            raise TypeError("Expected argument 'module_stream_profile_on_managed_instances' to be a list")
        pulumi.set(__self__, "module_stream_profile_on_managed_instances", module_stream_profile_on_managed_instances)
        if profile_name and not isinstance(profile_name, str):
            raise TypeError("Expected argument 'profile_name' to be a str")
        pulumi.set(__self__, "profile_name", profile_name)
        if profile_status and not isinstance(profile_status, str):
            raise TypeError("Expected argument 'profile_status' to be a str")
        pulumi.set(__self__, "profile_status", profile_status)
        if stream_name and not isinstance(stream_name, str):
            raise TypeError("Expected argument 'stream_name' to be a str")
        pulumi.set(__self__, "stream_name", stream_name)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetManagedInstanceStreamProfileFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="managedInstanceId")
    def managed_instance_id(self) -> str:
        return pulumi.get(self, "managed_instance_id")

    @property
    @pulumi.getter(name="moduleName")
    def module_name(self) -> Optional[str]:
        """
        The name of the module that contains the stream profile
        """
        return pulumi.get(self, "module_name")

    @property
    @pulumi.getter(name="moduleStreamProfileOnManagedInstances")
    def module_stream_profile_on_managed_instances(self) -> Sequence['outputs.GetManagedInstanceStreamProfileModuleStreamProfileOnManagedInstanceResult']:
        """
        The list of module_stream_profile_on_managed_instances.
        """
        return pulumi.get(self, "module_stream_profile_on_managed_instances")

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> Optional[str]:
        """
        The name of the profile
        """
        return pulumi.get(self, "profile_name")

    @property
    @pulumi.getter(name="profileStatus")
    def profile_status(self) -> Optional[str]:
        return pulumi.get(self, "profile_status")

    @property
    @pulumi.getter(name="streamName")
    def stream_name(self) -> Optional[str]:
        """
        The name of the stream that contains the profile
        """
        return pulumi.get(self, "stream_name")


class AwaitableGetManagedInstanceStreamProfileResult(GetManagedInstanceStreamProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedInstanceStreamProfileResult(
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            managed_instance_id=self.managed_instance_id,
            module_name=self.module_name,
            module_stream_profile_on_managed_instances=self.module_stream_profile_on_managed_instances,
            profile_name=self.profile_name,
            profile_status=self.profile_status,
            stream_name=self.stream_name)


def get_managed_instance_stream_profile(compartment_id: Optional[str] = None,
                                        filters: Optional[Sequence[pulumi.InputType['GetManagedInstanceStreamProfileFilterArgs']]] = None,
                                        managed_instance_id: Optional[str] = None,
                                        module_name: Optional[str] = None,
                                        profile_name: Optional[str] = None,
                                        profile_status: Optional[str] = None,
                                        stream_name: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedInstanceStreamProfileResult:
    """
    This data source provides the list of Managed Instance Stream Profiles in Oracle Cloud Infrastructure OS Management service.

    Retrieve a list of module stream profiles, along with a summary of their
    of their status, from a managed instance.  Filters may be applied to
    select a subset of profiles based on the filter criteria.

    The "moduleName", "streamName", and "profileName" attributes combine
    to form a set of filters on the list of module stream profiles.  If
    a "modulName" is provided, only profiles that belong to that module
    are returned.  If both a "moduleName" and "streamName" are given,
    only profiles belonging to that module stream are returned.  Finally,
    if all three are given then only the particular profile indicated
    by the triple is returned.  It is not valid to supply a "streamName"
    without a "moduleName".  It is also not valid to supply a "profileName"
    without a "streamName".

    The "status" attribute filters against the state of a module stream
    profile.  Valid values are "INSTALLED" and "AVAILABLE".  If the
    attribute is set to "INSTALLED", only module stream profiles that
    are installed are included in the result set.  If the attribute is
    set to "AVAILABLE", only module stream profiles that are not
    installed are included in the result set.  If the attribute is not
    defined, the request is not subject to this filter.

    When sorting by display name, the result set is sorted first by
    module name, then by stream name, and finally by profile name.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_instance_stream_profiles = oci.OsManagement.get_managed_instance_stream_profile(managed_instance_id=var["managed_instance_id"],
        compartment_id=var["compartment_id"],
        module_name=var["managed_instance_module_name"],
        profile_name=var["managed_instance_module_stream_profile_name"],
        profile_status=var["managed_instance_profile_status"],
        stream_name=var["managed_instance_module_stream_name"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.
    :param str managed_instance_id: OCID for the managed instance
    :param str module_name: The name of a module.  This parameter is required if a streamName is specified.
    :param str profile_name: The name of the profile of the containing module stream
    :param str profile_status: The status of the profile.
           
           A profile with the "INSTALLED" status indicates that the profile has been installed.
           
           A profile with the "AVAILABLE" status indicates that the profile is not installed, but can be.
    :param str stream_name: The name of the stream of the containing module.  This parameter is required if a profileName is specified.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['managedInstanceId'] = managed_instance_id
    __args__['moduleName'] = module_name
    __args__['profileName'] = profile_name
    __args__['profileStatus'] = profile_status
    __args__['streamName'] = stream_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:OsManagement/getManagedInstanceStreamProfile:getManagedInstanceStreamProfile', __args__, opts=opts, typ=GetManagedInstanceStreamProfileResult).value

    return AwaitableGetManagedInstanceStreamProfileResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        managed_instance_id=pulumi.get(__ret__, 'managed_instance_id'),
        module_name=pulumi.get(__ret__, 'module_name'),
        module_stream_profile_on_managed_instances=pulumi.get(__ret__, 'module_stream_profile_on_managed_instances'),
        profile_name=pulumi.get(__ret__, 'profile_name'),
        profile_status=pulumi.get(__ret__, 'profile_status'),
        stream_name=pulumi.get(__ret__, 'stream_name'))


@_utilities.lift_output_func(get_managed_instance_stream_profile)
def get_managed_instance_stream_profile_output(compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                                               filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetManagedInstanceStreamProfileFilterArgs']]]]] = None,
                                               managed_instance_id: Optional[pulumi.Input[str]] = None,
                                               module_name: Optional[pulumi.Input[Optional[str]]] = None,
                                               profile_name: Optional[pulumi.Input[Optional[str]]] = None,
                                               profile_status: Optional[pulumi.Input[Optional[str]]] = None,
                                               stream_name: Optional[pulumi.Input[Optional[str]]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedInstanceStreamProfileResult]:
    """
    This data source provides the list of Managed Instance Stream Profiles in Oracle Cloud Infrastructure OS Management service.

    Retrieve a list of module stream profiles, along with a summary of their
    of their status, from a managed instance.  Filters may be applied to
    select a subset of profiles based on the filter criteria.

    The "moduleName", "streamName", and "profileName" attributes combine
    to form a set of filters on the list of module stream profiles.  If
    a "modulName" is provided, only profiles that belong to that module
    are returned.  If both a "moduleName" and "streamName" are given,
    only profiles belonging to that module stream are returned.  Finally,
    if all three are given then only the particular profile indicated
    by the triple is returned.  It is not valid to supply a "streamName"
    without a "moduleName".  It is also not valid to supply a "profileName"
    without a "streamName".

    The "status" attribute filters against the state of a module stream
    profile.  Valid values are "INSTALLED" and "AVAILABLE".  If the
    attribute is set to "INSTALLED", only module stream profiles that
    are installed are included in the result set.  If the attribute is
    set to "AVAILABLE", only module stream profiles that are not
    installed are included in the result set.  If the attribute is not
    defined, the request is not subject to this filter.

    When sorting by display name, the result set is sorted first by
    module name, then by stream name, and finally by profile name.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_instance_stream_profiles = oci.OsManagement.get_managed_instance_stream_profile(managed_instance_id=var["managed_instance_id"],
        compartment_id=var["compartment_id"],
        module_name=var["managed_instance_module_name"],
        profile_name=var["managed_instance_module_stream_profile_name"],
        profile_status=var["managed_instance_profile_status"],
        stream_name=var["managed_instance_module_stream_name"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.
    :param str managed_instance_id: OCID for the managed instance
    :param str module_name: The name of a module.  This parameter is required if a streamName is specified.
    :param str profile_name: The name of the profile of the containing module stream
    :param str profile_status: The status of the profile.
           
           A profile with the "INSTALLED" status indicates that the profile has been installed.
           
           A profile with the "AVAILABLE" status indicates that the profile is not installed, but can be.
    :param str stream_name: The name of the stream of the containing module.  This parameter is required if a profileName is specified.
    """
    ...
