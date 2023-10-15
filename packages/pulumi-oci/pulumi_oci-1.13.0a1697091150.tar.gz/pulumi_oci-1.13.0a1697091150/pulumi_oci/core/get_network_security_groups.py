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
    'GetNetworkSecurityGroupsResult',
    'AwaitableGetNetworkSecurityGroupsResult',
    'get_network_security_groups',
    'get_network_security_groups_output',
]

@pulumi.output_type
class GetNetworkSecurityGroupsResult:
    """
    A collection of values returned by getNetworkSecurityGroups.
    """
    def __init__(__self__, compartment_id=None, display_name=None, filters=None, id=None, network_security_groups=None, state=None, vcn_id=None, vlan_id=None):
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
        if network_security_groups and not isinstance(network_security_groups, list):
            raise TypeError("Expected argument 'network_security_groups' to be a list")
        pulumi.set(__self__, "network_security_groups", network_security_groups)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if vcn_id and not isinstance(vcn_id, str):
            raise TypeError("Expected argument 'vcn_id' to be a str")
        pulumi.set(__self__, "vcn_id", vcn_id)
        if vlan_id and not isinstance(vlan_id, str):
            raise TypeError("Expected argument 'vlan_id' to be a str")
        pulumi.set(__self__, "vlan_id", vlan_id)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment the network security group is in.
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
    def filters(self) -> Optional[Sequence['outputs.GetNetworkSecurityGroupsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="networkSecurityGroups")
    def network_security_groups(self) -> Sequence['outputs.GetNetworkSecurityGroupsNetworkSecurityGroupResult']:
        """
        The list of network_security_groups.
        """
        return pulumi.get(self, "network_security_groups")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The network security group's current state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="vcnId")
    def vcn_id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network security group's VCN.
        """
        return pulumi.get(self, "vcn_id")

    @property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> Optional[str]:
        return pulumi.get(self, "vlan_id")


class AwaitableGetNetworkSecurityGroupsResult(GetNetworkSecurityGroupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkSecurityGroupsResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            network_security_groups=self.network_security_groups,
            state=self.state,
            vcn_id=self.vcn_id,
            vlan_id=self.vlan_id)


def get_network_security_groups(compartment_id: Optional[str] = None,
                                display_name: Optional[str] = None,
                                filters: Optional[Sequence[pulumi.InputType['GetNetworkSecurityGroupsFilterArgs']]] = None,
                                state: Optional[str] = None,
                                vcn_id: Optional[str] = None,
                                vlan_id: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkSecurityGroupsResult:
    """
    This data source provides the list of Network Security Groups in Oracle Cloud Infrastructure Core service.

    Lists either the network security groups in the specified compartment, or those associated with the specified VLAN.
    You must specify either a `vlanId` or a `compartmentId`, but not both. If you specify a `vlanId`, all other parameters are ignored.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_network_security_groups = oci.Core.get_network_security_groups(compartment_id=var["compartment_id"],
        display_name=var["network_security_group_display_name"],
        state=var["network_security_group_state"],
        vcn_id=oci_core_vcn["test_vcn"]["id"],
        vlan_id=oci_core_vlan["test_vlan"]["id"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A filter to return only resources that match the given display name exactly.
    :param str state: A filter to return only resources that match the specified lifecycle state. The value is case insensitive.
    :param str vcn_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN.
    :param str vlan_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VLAN.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['state'] = state
    __args__['vcnId'] = vcn_id
    __args__['vlanId'] = vlan_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Core/getNetworkSecurityGroups:getNetworkSecurityGroups', __args__, opts=opts, typ=GetNetworkSecurityGroupsResult).value

    return AwaitableGetNetworkSecurityGroupsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        network_security_groups=pulumi.get(__ret__, 'network_security_groups'),
        state=pulumi.get(__ret__, 'state'),
        vcn_id=pulumi.get(__ret__, 'vcn_id'),
        vlan_id=pulumi.get(__ret__, 'vlan_id'))


@_utilities.lift_output_func(get_network_security_groups)
def get_network_security_groups_output(compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                                       display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                       filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetNetworkSecurityGroupsFilterArgs']]]]] = None,
                                       state: Optional[pulumi.Input[Optional[str]]] = None,
                                       vcn_id: Optional[pulumi.Input[Optional[str]]] = None,
                                       vlan_id: Optional[pulumi.Input[Optional[str]]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkSecurityGroupsResult]:
    """
    This data source provides the list of Network Security Groups in Oracle Cloud Infrastructure Core service.

    Lists either the network security groups in the specified compartment, or those associated with the specified VLAN.
    You must specify either a `vlanId` or a `compartmentId`, but not both. If you specify a `vlanId`, all other parameters are ignored.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_network_security_groups = oci.Core.get_network_security_groups(compartment_id=var["compartment_id"],
        display_name=var["network_security_group_display_name"],
        state=var["network_security_group_state"],
        vcn_id=oci_core_vcn["test_vcn"]["id"],
        vlan_id=oci_core_vlan["test_vlan"]["id"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A filter to return only resources that match the given display name exactly.
    :param str state: A filter to return only resources that match the specified lifecycle state. The value is case insensitive.
    :param str vcn_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN.
    :param str vlan_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VLAN.
    """
    ...
