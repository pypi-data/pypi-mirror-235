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
    'GetVtapsResult',
    'AwaitableGetVtapsResult',
    'get_vtaps',
    'get_vtaps_output',
]

@pulumi.output_type
class GetVtapsResult:
    """
    A collection of values returned by getVtaps.
    """
    def __init__(__self__, compartment_id=None, display_name=None, filters=None, id=None, is_vtap_enabled=None, source=None, state=None, target_id=None, target_ip=None, vcn_id=None, vtaps=None):
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
        if is_vtap_enabled and not isinstance(is_vtap_enabled, bool):
            raise TypeError("Expected argument 'is_vtap_enabled' to be a bool")
        pulumi.set(__self__, "is_vtap_enabled", is_vtap_enabled)
        if source and not isinstance(source, str):
            raise TypeError("Expected argument 'source' to be a str")
        pulumi.set(__self__, "source", source)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if target_id and not isinstance(target_id, str):
            raise TypeError("Expected argument 'target_id' to be a str")
        pulumi.set(__self__, "target_id", target_id)
        if target_ip and not isinstance(target_ip, str):
            raise TypeError("Expected argument 'target_ip' to be a str")
        pulumi.set(__self__, "target_ip", target_ip)
        if vcn_id and not isinstance(vcn_id, str):
            raise TypeError("Expected argument 'vcn_id' to be a str")
        pulumi.set(__self__, "vcn_id", vcn_id)
        if vtaps and not isinstance(vtaps, list):
            raise TypeError("Expected argument 'vtaps' to be a list")
        pulumi.set(__self__, "vtaps", vtaps)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the `Vtap` resource.
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
    def filters(self) -> Optional[Sequence['outputs.GetVtapsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isVtapEnabled")
    def is_vtap_enabled(self) -> Optional[bool]:
        """
        Used to start or stop a `Vtap` resource.
        """
        return pulumi.get(self, "is_vtap_enabled")

    @property
    @pulumi.getter
    def source(self) -> Optional[str]:
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The VTAP's administrative lifecycle state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the destination resource where mirrored packets are sent.
        """
        return pulumi.get(self, "target_id")

    @property
    @pulumi.getter(name="targetIp")
    def target_ip(self) -> Optional[str]:
        """
        The IP address of the destination resource where mirrored packets are sent.
        """
        return pulumi.get(self, "target_ip")

    @property
    @pulumi.getter(name="vcnId")
    def vcn_id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN containing the `Vtap` resource.
        """
        return pulumi.get(self, "vcn_id")

    @property
    @pulumi.getter
    def vtaps(self) -> Sequence['outputs.GetVtapsVtapResult']:
        """
        The list of vtaps.
        """
        return pulumi.get(self, "vtaps")


class AwaitableGetVtapsResult(GetVtapsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVtapsResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            is_vtap_enabled=self.is_vtap_enabled,
            source=self.source,
            state=self.state,
            target_id=self.target_id,
            target_ip=self.target_ip,
            vcn_id=self.vcn_id,
            vtaps=self.vtaps)


def get_vtaps(compartment_id: Optional[str] = None,
              display_name: Optional[str] = None,
              filters: Optional[Sequence[pulumi.InputType['GetVtapsFilterArgs']]] = None,
              is_vtap_enabled: Optional[bool] = None,
              source: Optional[str] = None,
              state: Optional[str] = None,
              target_id: Optional[str] = None,
              target_ip: Optional[str] = None,
              vcn_id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVtapsResult:
    """
    This data source provides the list of Vtaps in Oracle Cloud Infrastructure Core service.

    Lists the virtual test access points (VTAPs) in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_vtaps = oci.Core.get_vtaps(compartment_id=var["compartment_id"],
        display_name=var["vtap_display_name"],
        is_vtap_enabled=var["vtap_is_vtap_enabled"],
        source=var["vtap_source"],
        state=var["vtap_state"],
        target_id=oci_cloud_guard_target["test_target"]["id"],
        target_ip=var["vtap_target_ip"],
        vcn_id=oci_core_vcn["test_vcn"]["id"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A filter to return only resources that match the given display name exactly.
    :param bool is_vtap_enabled: Indicates whether to list all VTAPs or only running VTAPs.
           * When `FALSE`, lists ALL running and stopped VTAPs.
           * When `TRUE`, lists only running VTAPs (VTAPs where isVtapEnabled = `TRUE`).
    :param str source: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VTAP source.
    :param str state: A filter to return only resources that match the given VTAP administrative lifecycle state. The state value is case-insensitive.
    :param str target_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VTAP target.
    :param str target_ip: The IP address of the VTAP target.
    :param str vcn_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['isVtapEnabled'] = is_vtap_enabled
    __args__['source'] = source
    __args__['state'] = state
    __args__['targetId'] = target_id
    __args__['targetIp'] = target_ip
    __args__['vcnId'] = vcn_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Core/getVtaps:getVtaps', __args__, opts=opts, typ=GetVtapsResult).value

    return AwaitableGetVtapsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        is_vtap_enabled=pulumi.get(__ret__, 'is_vtap_enabled'),
        source=pulumi.get(__ret__, 'source'),
        state=pulumi.get(__ret__, 'state'),
        target_id=pulumi.get(__ret__, 'target_id'),
        target_ip=pulumi.get(__ret__, 'target_ip'),
        vcn_id=pulumi.get(__ret__, 'vcn_id'),
        vtaps=pulumi.get(__ret__, 'vtaps'))


@_utilities.lift_output_func(get_vtaps)
def get_vtaps_output(compartment_id: Optional[pulumi.Input[str]] = None,
                     display_name: Optional[pulumi.Input[Optional[str]]] = None,
                     filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetVtapsFilterArgs']]]]] = None,
                     is_vtap_enabled: Optional[pulumi.Input[Optional[bool]]] = None,
                     source: Optional[pulumi.Input[Optional[str]]] = None,
                     state: Optional[pulumi.Input[Optional[str]]] = None,
                     target_id: Optional[pulumi.Input[Optional[str]]] = None,
                     target_ip: Optional[pulumi.Input[Optional[str]]] = None,
                     vcn_id: Optional[pulumi.Input[Optional[str]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVtapsResult]:
    """
    This data source provides the list of Vtaps in Oracle Cloud Infrastructure Core service.

    Lists the virtual test access points (VTAPs) in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_vtaps = oci.Core.get_vtaps(compartment_id=var["compartment_id"],
        display_name=var["vtap_display_name"],
        is_vtap_enabled=var["vtap_is_vtap_enabled"],
        source=var["vtap_source"],
        state=var["vtap_state"],
        target_id=oci_cloud_guard_target["test_target"]["id"],
        target_ip=var["vtap_target_ip"],
        vcn_id=oci_core_vcn["test_vcn"]["id"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A filter to return only resources that match the given display name exactly.
    :param bool is_vtap_enabled: Indicates whether to list all VTAPs or only running VTAPs.
           * When `FALSE`, lists ALL running and stopped VTAPs.
           * When `TRUE`, lists only running VTAPs (VTAPs where isVtapEnabled = `TRUE`).
    :param str source: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VTAP source.
    :param str state: A filter to return only resources that match the given VTAP administrative lifecycle state. The state value is case-insensitive.
    :param str target_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VTAP target.
    :param str target_ip: The IP address of the VTAP target.
    :param str vcn_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN.
    """
    ...
