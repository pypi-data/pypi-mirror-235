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
    'GetDhcpOptionsResult',
    'AwaitableGetDhcpOptionsResult',
    'get_dhcp_options',
    'get_dhcp_options_output',
]

@pulumi.output_type
class GetDhcpOptionsResult:
    """
    A collection of values returned by getDhcpOptions.
    """
    def __init__(__self__, compartment_id=None, display_name=None, filters=None, id=None, options=None, state=None, vcn_id=None):
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
        if options and not isinstance(options, list):
            raise TypeError("Expected argument 'options' to be a list")
        pulumi.set(__self__, "options", options)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if vcn_id and not isinstance(vcn_id, str):
            raise TypeError("Expected argument 'vcn_id' to be a str")
        pulumi.set(__self__, "vcn_id", vcn_id)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the set of DHCP options.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetDhcpOptionsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def options(self) -> Sequence['outputs.GetDhcpOptionsOptionResult']:
        """
        The collection of individual DHCP options.
        """
        return pulumi.get(self, "options")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the set of DHCP options.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="vcnId")
    def vcn_id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN the set of DHCP options belongs to.
        """
        return pulumi.get(self, "vcn_id")


class AwaitableGetDhcpOptionsResult(GetDhcpOptionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDhcpOptionsResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            options=self.options,
            state=self.state,
            vcn_id=self.vcn_id)


def get_dhcp_options(compartment_id: Optional[str] = None,
                     display_name: Optional[str] = None,
                     filters: Optional[Sequence[pulumi.InputType['GetDhcpOptionsFilterArgs']]] = None,
                     state: Optional[str] = None,
                     vcn_id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDhcpOptionsResult:
    """
    This data source provides the list of Dhcp Options in Oracle Cloud Infrastructure Core service.

    Lists the sets of DHCP options in the specified VCN and specified compartment.
    If the VCN ID is not provided, then the list includes the sets of DHCP options from all VCNs in the specified compartment.
    The response includes the default set of options that automatically comes with each VCN,
    plus any other sets you've created.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_dhcp_options = oci.Core.get_dhcp_options(compartment_id=var["compartment_id"],
        display_name=var["dhcp_options_display_name"],
        state=var["dhcp_options_state"],
        vcn_id=oci_core_vcn["test_vcn"]["id"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A filter to return only resources that match the given display name exactly.
    :param str state: A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.
    :param str vcn_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['state'] = state
    __args__['vcnId'] = vcn_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Core/getDhcpOptions:getDhcpOptions', __args__, opts=opts, typ=GetDhcpOptionsResult).value

    return AwaitableGetDhcpOptionsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        options=pulumi.get(__ret__, 'options'),
        state=pulumi.get(__ret__, 'state'),
        vcn_id=pulumi.get(__ret__, 'vcn_id'))


@_utilities.lift_output_func(get_dhcp_options)
def get_dhcp_options_output(compartment_id: Optional[pulumi.Input[str]] = None,
                            display_name: Optional[pulumi.Input[Optional[str]]] = None,
                            filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDhcpOptionsFilterArgs']]]]] = None,
                            state: Optional[pulumi.Input[Optional[str]]] = None,
                            vcn_id: Optional[pulumi.Input[Optional[str]]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDhcpOptionsResult]:
    """
    This data source provides the list of Dhcp Options in Oracle Cloud Infrastructure Core service.

    Lists the sets of DHCP options in the specified VCN and specified compartment.
    If the VCN ID is not provided, then the list includes the sets of DHCP options from all VCNs in the specified compartment.
    The response includes the default set of options that automatically comes with each VCN,
    plus any other sets you've created.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_dhcp_options = oci.Core.get_dhcp_options(compartment_id=var["compartment_id"],
        display_name=var["dhcp_options_display_name"],
        state=var["dhcp_options_state"],
        vcn_id=oci_core_vcn["test_vcn"]["id"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A filter to return only resources that match the given display name exactly.
    :param str state: A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.
    :param str vcn_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN.
    """
    ...
