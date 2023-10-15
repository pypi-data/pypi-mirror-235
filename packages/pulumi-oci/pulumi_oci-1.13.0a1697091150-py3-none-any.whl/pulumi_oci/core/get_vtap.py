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
    'GetVtapResult',
    'AwaitableGetVtapResult',
    'get_vtap',
    'get_vtap_output',
]

@pulumi.output_type
class GetVtapResult:
    """
    A collection of values returned by getVtap.
    """
    def __init__(__self__, capture_filter_id=None, compartment_id=None, defined_tags=None, display_name=None, encapsulation_protocol=None, freeform_tags=None, id=None, is_vtap_enabled=None, lifecycle_state_details=None, max_packet_size=None, source_id=None, source_private_endpoint_ip=None, source_private_endpoint_subnet_id=None, source_type=None, state=None, target_id=None, target_ip=None, target_type=None, time_created=None, traffic_mode=None, vcn_id=None, vtap_id=None, vxlan_network_identifier=None):
        if capture_filter_id and not isinstance(capture_filter_id, str):
            raise TypeError("Expected argument 'capture_filter_id' to be a str")
        pulumi.set(__self__, "capture_filter_id", capture_filter_id)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if encapsulation_protocol and not isinstance(encapsulation_protocol, str):
            raise TypeError("Expected argument 'encapsulation_protocol' to be a str")
        pulumi.set(__self__, "encapsulation_protocol", encapsulation_protocol)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_vtap_enabled and not isinstance(is_vtap_enabled, bool):
            raise TypeError("Expected argument 'is_vtap_enabled' to be a bool")
        pulumi.set(__self__, "is_vtap_enabled", is_vtap_enabled)
        if lifecycle_state_details and not isinstance(lifecycle_state_details, str):
            raise TypeError("Expected argument 'lifecycle_state_details' to be a str")
        pulumi.set(__self__, "lifecycle_state_details", lifecycle_state_details)
        if max_packet_size and not isinstance(max_packet_size, int):
            raise TypeError("Expected argument 'max_packet_size' to be a int")
        pulumi.set(__self__, "max_packet_size", max_packet_size)
        if source_id and not isinstance(source_id, str):
            raise TypeError("Expected argument 'source_id' to be a str")
        pulumi.set(__self__, "source_id", source_id)
        if source_private_endpoint_ip and not isinstance(source_private_endpoint_ip, str):
            raise TypeError("Expected argument 'source_private_endpoint_ip' to be a str")
        pulumi.set(__self__, "source_private_endpoint_ip", source_private_endpoint_ip)
        if source_private_endpoint_subnet_id and not isinstance(source_private_endpoint_subnet_id, str):
            raise TypeError("Expected argument 'source_private_endpoint_subnet_id' to be a str")
        pulumi.set(__self__, "source_private_endpoint_subnet_id", source_private_endpoint_subnet_id)
        if source_type and not isinstance(source_type, str):
            raise TypeError("Expected argument 'source_type' to be a str")
        pulumi.set(__self__, "source_type", source_type)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if target_id and not isinstance(target_id, str):
            raise TypeError("Expected argument 'target_id' to be a str")
        pulumi.set(__self__, "target_id", target_id)
        if target_ip and not isinstance(target_ip, str):
            raise TypeError("Expected argument 'target_ip' to be a str")
        pulumi.set(__self__, "target_ip", target_ip)
        if target_type and not isinstance(target_type, str):
            raise TypeError("Expected argument 'target_type' to be a str")
        pulumi.set(__self__, "target_type", target_type)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if traffic_mode and not isinstance(traffic_mode, str):
            raise TypeError("Expected argument 'traffic_mode' to be a str")
        pulumi.set(__self__, "traffic_mode", traffic_mode)
        if vcn_id and not isinstance(vcn_id, str):
            raise TypeError("Expected argument 'vcn_id' to be a str")
        pulumi.set(__self__, "vcn_id", vcn_id)
        if vtap_id and not isinstance(vtap_id, str):
            raise TypeError("Expected argument 'vtap_id' to be a str")
        pulumi.set(__self__, "vtap_id", vtap_id)
        if vxlan_network_identifier and not isinstance(vxlan_network_identifier, str):
            raise TypeError("Expected argument 'vxlan_network_identifier' to be a str")
        pulumi.set(__self__, "vxlan_network_identifier", vxlan_network_identifier)

    @property
    @pulumi.getter(name="captureFilterId")
    def capture_filter_id(self) -> str:
        """
        The capture filter's Oracle ID ([OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).
        """
        return pulumi.get(self, "capture_filter_id")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the `Vtap` resource.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="encapsulationProtocol")
    def encapsulation_protocol(self) -> str:
        """
        Defines an encapsulation header type for the VTAP's mirrored traffic.
        """
        return pulumi.get(self, "encapsulation_protocol")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The VTAP's Oracle ID ([OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isVtapEnabled")
    def is_vtap_enabled(self) -> bool:
        """
        Used to start or stop a `Vtap` resource.
        """
        return pulumi.get(self, "is_vtap_enabled")

    @property
    @pulumi.getter(name="lifecycleStateDetails")
    def lifecycle_state_details(self) -> str:
        """
        The VTAP's current running state.
        """
        return pulumi.get(self, "lifecycle_state_details")

    @property
    @pulumi.getter(name="maxPacketSize")
    def max_packet_size(self) -> int:
        """
        The maximum size of the packets to be included in the filter.
        """
        return pulumi.get(self, "max_packet_size")

    @property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the source point where packets are captured.
        """
        return pulumi.get(self, "source_id")

    @property
    @pulumi.getter(name="sourcePrivateEndpointIp")
    def source_private_endpoint_ip(self) -> str:
        """
        The IP Address of the source private endpoint.
        """
        return pulumi.get(self, "source_private_endpoint_ip")

    @property
    @pulumi.getter(name="sourcePrivateEndpointSubnetId")
    def source_private_endpoint_subnet_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet that source private endpoint belongs to.
        """
        return pulumi.get(self, "source_private_endpoint_subnet_id")

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> str:
        """
        The source type for the VTAP.
        """
        return pulumi.get(self, "source_type")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The VTAP's administrative lifecycle state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the destination resource where mirrored packets are sent.
        """
        return pulumi.get(self, "target_id")

    @property
    @pulumi.getter(name="targetIp")
    def target_ip(self) -> str:
        """
        The IP address of the destination resource where mirrored packets are sent.
        """
        return pulumi.get(self, "target_ip")

    @property
    @pulumi.getter(name="targetType")
    def target_type(self) -> str:
        """
        The target type for the VTAP.
        """
        return pulumi.get(self, "target_type")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the VTAP was created, in the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339).  Example: `2020-08-25T21:10:29.600Z`
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="trafficMode")
    def traffic_mode(self) -> str:
        """
        Used to control the priority of traffic. It is an optional field. If it not passed, the value is DEFAULT
        """
        return pulumi.get(self, "traffic_mode")

    @property
    @pulumi.getter(name="vcnId")
    def vcn_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN containing the `Vtap` resource.
        """
        return pulumi.get(self, "vcn_id")

    @property
    @pulumi.getter(name="vtapId")
    def vtap_id(self) -> str:
        return pulumi.get(self, "vtap_id")

    @property
    @pulumi.getter(name="vxlanNetworkIdentifier")
    def vxlan_network_identifier(self) -> str:
        """
        The virtual extensible LAN (VXLAN) network identifier (or VXLAN segment ID) that uniquely identifies the VXLAN.
        """
        return pulumi.get(self, "vxlan_network_identifier")


class AwaitableGetVtapResult(GetVtapResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVtapResult(
            capture_filter_id=self.capture_filter_id,
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            display_name=self.display_name,
            encapsulation_protocol=self.encapsulation_protocol,
            freeform_tags=self.freeform_tags,
            id=self.id,
            is_vtap_enabled=self.is_vtap_enabled,
            lifecycle_state_details=self.lifecycle_state_details,
            max_packet_size=self.max_packet_size,
            source_id=self.source_id,
            source_private_endpoint_ip=self.source_private_endpoint_ip,
            source_private_endpoint_subnet_id=self.source_private_endpoint_subnet_id,
            source_type=self.source_type,
            state=self.state,
            target_id=self.target_id,
            target_ip=self.target_ip,
            target_type=self.target_type,
            time_created=self.time_created,
            traffic_mode=self.traffic_mode,
            vcn_id=self.vcn_id,
            vtap_id=self.vtap_id,
            vxlan_network_identifier=self.vxlan_network_identifier)


def get_vtap(vtap_id: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVtapResult:
    """
    This data source provides details about a specific Vtap resource in Oracle Cloud Infrastructure Core service.

    Gets the specified `Vtap` resource.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_vtap = oci.Core.get_vtap(vtap_id=oci_core_vtap["test_vtap"]["id"])
    ```


    :param str vtap_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VTAP.
    """
    __args__ = dict()
    __args__['vtapId'] = vtap_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Core/getVtap:getVtap', __args__, opts=opts, typ=GetVtapResult).value

    return AwaitableGetVtapResult(
        capture_filter_id=pulumi.get(__ret__, 'capture_filter_id'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        display_name=pulumi.get(__ret__, 'display_name'),
        encapsulation_protocol=pulumi.get(__ret__, 'encapsulation_protocol'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        is_vtap_enabled=pulumi.get(__ret__, 'is_vtap_enabled'),
        lifecycle_state_details=pulumi.get(__ret__, 'lifecycle_state_details'),
        max_packet_size=pulumi.get(__ret__, 'max_packet_size'),
        source_id=pulumi.get(__ret__, 'source_id'),
        source_private_endpoint_ip=pulumi.get(__ret__, 'source_private_endpoint_ip'),
        source_private_endpoint_subnet_id=pulumi.get(__ret__, 'source_private_endpoint_subnet_id'),
        source_type=pulumi.get(__ret__, 'source_type'),
        state=pulumi.get(__ret__, 'state'),
        target_id=pulumi.get(__ret__, 'target_id'),
        target_ip=pulumi.get(__ret__, 'target_ip'),
        target_type=pulumi.get(__ret__, 'target_type'),
        time_created=pulumi.get(__ret__, 'time_created'),
        traffic_mode=pulumi.get(__ret__, 'traffic_mode'),
        vcn_id=pulumi.get(__ret__, 'vcn_id'),
        vtap_id=pulumi.get(__ret__, 'vtap_id'),
        vxlan_network_identifier=pulumi.get(__ret__, 'vxlan_network_identifier'))


@_utilities.lift_output_func(get_vtap)
def get_vtap_output(vtap_id: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVtapResult]:
    """
    This data source provides details about a specific Vtap resource in Oracle Cloud Infrastructure Core service.

    Gets the specified `Vtap` resource.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_vtap = oci.Core.get_vtap(vtap_id=oci_core_vtap["test_vtap"]["id"])
    ```


    :param str vtap_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VTAP.
    """
    ...
