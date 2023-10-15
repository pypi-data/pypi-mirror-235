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
    'GetSoftwareSourcesResult',
    'AwaitableGetSoftwareSourcesResult',
    'get_software_sources',
    'get_software_sources_output',
]

@pulumi.output_type
class GetSoftwareSourcesResult:
    """
    A collection of values returned by getSoftwareSources.
    """
    def __init__(__self__, compartment_id=None, display_name=None, filters=None, id=None, software_sources=None, state=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if software_sources and not isinstance(software_sources, list):
            raise TypeError("Expected argument 'software_sources' to be a list")
        pulumi.set(__self__, "software_sources", software_sources)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        OCID for the Compartment
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        User friendly name for the software source
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetSoftwareSourcesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="softwareSources")
    def software_sources(self) -> Sequence['outputs.GetSoftwareSourcesSoftwareSourceResult']:
        """
        The list of software_sources.
        """
        return pulumi.get(self, "software_sources")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the Software Source.
        """
        return pulumi.get(self, "state")


class AwaitableGetSoftwareSourcesResult(GetSoftwareSourcesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSoftwareSourcesResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            software_sources=self.software_sources,
            state=self.state)


def get_software_sources(compartment_id: Optional[str] = None,
                         display_name: Optional[str] = None,
                         filters: Optional[Sequence[pulumi.InputType['GetSoftwareSourcesFilterArgs']]] = None,
                         state: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSoftwareSourcesResult:
    """
    This data source provides the list of Software Sources in Oracle Cloud Infrastructure OS Management service.

    Returns a list of all Software Sources.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_software_sources = oci.OsManagement.get_software_sources(compartment_id=var["compartment_id"],
        display_name=var["software_source_display_name"],
        state=var["software_source_state"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A user-friendly name. Does not have to be unique, and it's changeable.  Example: `My new resource`
    :param str state: The current lifecycle state for the object.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:OsManagement/getSoftwareSources:getSoftwareSources', __args__, opts=opts, typ=GetSoftwareSourcesResult).value

    return AwaitableGetSoftwareSourcesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        software_sources=pulumi.get(__ret__, 'software_sources'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_software_sources)
def get_software_sources_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetSoftwareSourcesFilterArgs']]]]] = None,
                                state: Optional[pulumi.Input[Optional[str]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSoftwareSourcesResult]:
    """
    This data source provides the list of Software Sources in Oracle Cloud Infrastructure OS Management service.

    Returns a list of all Software Sources.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_software_sources = oci.OsManagement.get_software_sources(compartment_id=var["compartment_id"],
        display_name=var["software_source_display_name"],
        state=var["software_source_state"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A user-friendly name. Does not have to be unique, and it's changeable.  Example: `My new resource`
    :param str state: The current lifecycle state for the object.
    """
    ...
