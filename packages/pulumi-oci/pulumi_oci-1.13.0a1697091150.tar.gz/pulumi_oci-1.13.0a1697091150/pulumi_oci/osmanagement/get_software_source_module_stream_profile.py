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
    'GetSoftwareSourceModuleStreamProfileResult',
    'AwaitableGetSoftwareSourceModuleStreamProfileResult',
    'get_software_source_module_stream_profile',
    'get_software_source_module_stream_profile_output',
]

@pulumi.output_type
class GetSoftwareSourceModuleStreamProfileResult:
    """
    A collection of values returned by getSoftwareSourceModuleStreamProfile.
    """
    def __init__(__self__, description=None, id=None, is_default=None, module_name=None, packages=None, profile_name=None, software_source_id=None, stream_name=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_default and not isinstance(is_default, bool):
            raise TypeError("Expected argument 'is_default' to be a bool")
        pulumi.set(__self__, "is_default", is_default)
        if module_name and not isinstance(module_name, str):
            raise TypeError("Expected argument 'module_name' to be a str")
        pulumi.set(__self__, "module_name", module_name)
        if packages and not isinstance(packages, list):
            raise TypeError("Expected argument 'packages' to be a list")
        pulumi.set(__self__, "packages", packages)
        if profile_name and not isinstance(profile_name, str):
            raise TypeError("Expected argument 'profile_name' to be a str")
        pulumi.set(__self__, "profile_name", profile_name)
        if software_source_id and not isinstance(software_source_id, str):
            raise TypeError("Expected argument 'software_source_id' to be a str")
        pulumi.set(__self__, "software_source_id", software_source_id)
        if stream_name and not isinstance(stream_name, str):
            raise TypeError("Expected argument 'stream_name' to be a str")
        pulumi.set(__self__, "stream_name", stream_name)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A description of the contents of the module stream profile
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> bool:
        """
        Indicates if this profile is the default for its module stream.
        """
        return pulumi.get(self, "is_default")

    @property
    @pulumi.getter(name="moduleName")
    def module_name(self) -> str:
        """
        The name of the module that contains the stream profile
        """
        return pulumi.get(self, "module_name")

    @property
    @pulumi.getter
    def packages(self) -> Sequence[str]:
        """
        A list of packages that constitute the profile.  Each element in the list is the name of a package.  The name is suitable to use as an argument to other OS Management APIs that interact directly with packages.
        """
        return pulumi.get(self, "packages")

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> str:
        """
        The name of the profile
        """
        return pulumi.get(self, "profile_name")

    @property
    @pulumi.getter(name="softwareSourceId")
    def software_source_id(self) -> str:
        return pulumi.get(self, "software_source_id")

    @property
    @pulumi.getter(name="streamName")
    def stream_name(self) -> str:
        """
        The name of the stream that contains the profile
        """
        return pulumi.get(self, "stream_name")


class AwaitableGetSoftwareSourceModuleStreamProfileResult(GetSoftwareSourceModuleStreamProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSoftwareSourceModuleStreamProfileResult(
            description=self.description,
            id=self.id,
            is_default=self.is_default,
            module_name=self.module_name,
            packages=self.packages,
            profile_name=self.profile_name,
            software_source_id=self.software_source_id,
            stream_name=self.stream_name)


def get_software_source_module_stream_profile(module_name: Optional[str] = None,
                                              profile_name: Optional[str] = None,
                                              software_source_id: Optional[str] = None,
                                              stream_name: Optional[str] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSoftwareSourceModuleStreamProfileResult:
    """
    This data source provides details about a specific Software Source Module Stream Profile resource in Oracle Cloud Infrastructure OS Management service.

    Retrieve a detailed description of a module stream profile from a software source.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_software_source_module_stream_profile = oci.OsManagement.get_software_source_module_stream_profile(module_name=var["software_source_module_name"],
        profile_name=var["software_source_module_stream_profile_name"],
        software_source_id=var["software_source"]["id"],
        stream_name=var["software_source_module_stream_name"])
    ```


    :param str module_name: The name of the module
    :param str profile_name: The name of the profile of the containing module stream
    :param str software_source_id: The OCID of the software source.
    :param str stream_name: The name of the stream of the containing module
    """
    __args__ = dict()
    __args__['moduleName'] = module_name
    __args__['profileName'] = profile_name
    __args__['softwareSourceId'] = software_source_id
    __args__['streamName'] = stream_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:OsManagement/getSoftwareSourceModuleStreamProfile:getSoftwareSourceModuleStreamProfile', __args__, opts=opts, typ=GetSoftwareSourceModuleStreamProfileResult).value

    return AwaitableGetSoftwareSourceModuleStreamProfileResult(
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        is_default=pulumi.get(__ret__, 'is_default'),
        module_name=pulumi.get(__ret__, 'module_name'),
        packages=pulumi.get(__ret__, 'packages'),
        profile_name=pulumi.get(__ret__, 'profile_name'),
        software_source_id=pulumi.get(__ret__, 'software_source_id'),
        stream_name=pulumi.get(__ret__, 'stream_name'))


@_utilities.lift_output_func(get_software_source_module_stream_profile)
def get_software_source_module_stream_profile_output(module_name: Optional[pulumi.Input[str]] = None,
                                                     profile_name: Optional[pulumi.Input[str]] = None,
                                                     software_source_id: Optional[pulumi.Input[str]] = None,
                                                     stream_name: Optional[pulumi.Input[str]] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSoftwareSourceModuleStreamProfileResult]:
    """
    This data source provides details about a specific Software Source Module Stream Profile resource in Oracle Cloud Infrastructure OS Management service.

    Retrieve a detailed description of a module stream profile from a software source.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_software_source_module_stream_profile = oci.OsManagement.get_software_source_module_stream_profile(module_name=var["software_source_module_name"],
        profile_name=var["software_source_module_stream_profile_name"],
        software_source_id=var["software_source"]["id"],
        stream_name=var["software_source_module_stream_name"])
    ```


    :param str module_name: The name of the module
    :param str profile_name: The name of the profile of the containing module stream
    :param str software_source_id: The OCID of the software source.
    :param str stream_name: The name of the stream of the containing module
    """
    ...
