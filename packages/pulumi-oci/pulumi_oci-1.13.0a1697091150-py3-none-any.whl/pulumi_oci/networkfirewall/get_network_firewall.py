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
    'GetNetworkFirewallResult',
    'AwaitableGetNetworkFirewallResult',
    'get_network_firewall',
    'get_network_firewall_output',
]

@pulumi.output_type
class GetNetworkFirewallResult:
    """
    A collection of values returned by getNetworkFirewall.
    """
    def __init__(__self__, availability_domain=None, compartment_id=None, defined_tags=None, display_name=None, freeform_tags=None, id=None, ipv4address=None, ipv6address=None, lifecycle_details=None, network_firewall_id=None, network_firewall_policy_id=None, network_security_group_ids=None, state=None, subnet_id=None, system_tags=None, time_created=None, time_updated=None):
        if availability_domain and not isinstance(availability_domain, str):
            raise TypeError("Expected argument 'availability_domain' to be a str")
        pulumi.set(__self__, "availability_domain", availability_domain)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ipv4address and not isinstance(ipv4address, str):
            raise TypeError("Expected argument 'ipv4address' to be a str")
        pulumi.set(__self__, "ipv4address", ipv4address)
        if ipv6address and not isinstance(ipv6address, str):
            raise TypeError("Expected argument 'ipv6address' to be a str")
        pulumi.set(__self__, "ipv6address", ipv6address)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if network_firewall_id and not isinstance(network_firewall_id, str):
            raise TypeError("Expected argument 'network_firewall_id' to be a str")
        pulumi.set(__self__, "network_firewall_id", network_firewall_id)
        if network_firewall_policy_id and not isinstance(network_firewall_policy_id, str):
            raise TypeError("Expected argument 'network_firewall_policy_id' to be a str")
        pulumi.set(__self__, "network_firewall_policy_id", network_firewall_policy_id)
        if network_security_group_ids and not isinstance(network_security_group_ids, list):
            raise TypeError("Expected argument 'network_security_group_ids' to be a list")
        pulumi.set(__self__, "network_security_group_ids", network_security_group_ids)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        pulumi.set(__self__, "subnet_id", subnet_id)
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
    @pulumi.getter(name="availabilityDomain")
    def availability_domain(self) -> str:
        """
        Availability Domain where Network Firewall instance is created. To get a list of availability domains for a tenancy, use [ListAvailabilityDomains](https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/AvailabilityDomain/ListAvailabilityDomains) operation. Example: `kIdk:PHX-AD-1`
        """
        return pulumi.get(self, "availability_domain")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the Network Firewall.
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
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        A user-friendly name for the Network Firewall. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

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
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Network Firewall resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ipv4address(self) -> str:
        """
        IPv4 address for the Network Firewall.
        """
        return pulumi.get(self, "ipv4address")

    @property
    @pulumi.getter
    def ipv6address(self) -> str:
        """
        IPv6 address for the Network Firewall.
        """
        return pulumi.get(self, "ipv6address")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="networkFirewallId")
    def network_firewall_id(self) -> str:
        return pulumi.get(self, "network_firewall_id")

    @property
    @pulumi.getter(name="networkFirewallPolicyId")
    def network_firewall_policy_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Network Firewall Policy.
        """
        return pulumi.get(self, "network_firewall_policy_id")

    @property
    @pulumi.getter(name="networkSecurityGroupIds")
    def network_security_group_ids(self) -> Sequence[str]:
        """
        An array of network security groups [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) associated with the Network Firewall.
        """
        return pulumi.get(self, "network_security_group_ids")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the Network Firewall.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet associated with the Network Firewall.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The time instant at which the Network Firewall was created in the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The time instant at which the Network Firewall was updated in the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`
        """
        return pulumi.get(self, "time_updated")


class AwaitableGetNetworkFirewallResult(GetNetworkFirewallResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkFirewallResult(
            availability_domain=self.availability_domain,
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            display_name=self.display_name,
            freeform_tags=self.freeform_tags,
            id=self.id,
            ipv4address=self.ipv4address,
            ipv6address=self.ipv6address,
            lifecycle_details=self.lifecycle_details,
            network_firewall_id=self.network_firewall_id,
            network_firewall_policy_id=self.network_firewall_policy_id,
            network_security_group_ids=self.network_security_group_ids,
            state=self.state,
            subnet_id=self.subnet_id,
            system_tags=self.system_tags,
            time_created=self.time_created,
            time_updated=self.time_updated)


def get_network_firewall(network_firewall_id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkFirewallResult:
    """
    This data source provides details about a specific Network Firewall resource in Oracle Cloud Infrastructure Network Firewall service.

    Gets a NetworkFirewall by identifier

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_network_firewall = oci.NetworkFirewall.get_network_firewall(network_firewall_id=oci_network_firewall_network_firewall["test_network_firewall"]["id"])
    ```


    :param str network_firewall_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Network Firewall resource.
    """
    __args__ = dict()
    __args__['networkFirewallId'] = network_firewall_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:NetworkFirewall/getNetworkFirewall:getNetworkFirewall', __args__, opts=opts, typ=GetNetworkFirewallResult).value

    return AwaitableGetNetworkFirewallResult(
        availability_domain=pulumi.get(__ret__, 'availability_domain'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        display_name=pulumi.get(__ret__, 'display_name'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        ipv4address=pulumi.get(__ret__, 'ipv4address'),
        ipv6address=pulumi.get(__ret__, 'ipv6address'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        network_firewall_id=pulumi.get(__ret__, 'network_firewall_id'),
        network_firewall_policy_id=pulumi.get(__ret__, 'network_firewall_policy_id'),
        network_security_group_ids=pulumi.get(__ret__, 'network_security_group_ids'),
        state=pulumi.get(__ret__, 'state'),
        subnet_id=pulumi.get(__ret__, 'subnet_id'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'))


@_utilities.lift_output_func(get_network_firewall)
def get_network_firewall_output(network_firewall_id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkFirewallResult]:
    """
    This data source provides details about a specific Network Firewall resource in Oracle Cloud Infrastructure Network Firewall service.

    Gets a NetworkFirewall by identifier

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_network_firewall = oci.NetworkFirewall.get_network_firewall(network_firewall_id=oci_network_firewall_network_firewall["test_network_firewall"]["id"])
    ```


    :param str network_firewall_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Network Firewall resource.
    """
    ...
