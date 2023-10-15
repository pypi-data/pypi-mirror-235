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
    'GetSddcsResult',
    'AwaitableGetSddcsResult',
    'get_sddcs',
    'get_sddcs_output',
]

@pulumi.output_type
class GetSddcsResult:
    """
    A collection of values returned by getSddcs.
    """
    def __init__(__self__, compartment_id=None, compute_availability_domain=None, display_name=None, filters=None, id=None, sddc_collections=None, state=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if compute_availability_domain and not isinstance(compute_availability_domain, str):
            raise TypeError("Expected argument 'compute_availability_domain' to be a str")
        pulumi.set(__self__, "compute_availability_domain", compute_availability_domain)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if sddc_collections and not isinstance(sddc_collections, list):
            raise TypeError("Expected argument 'sddc_collections' to be a list")
        pulumi.set(__self__, "sddc_collections", sddc_collections)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the SDDC.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="computeAvailabilityDomain")
    def compute_availability_domain(self) -> Optional[str]:
        """
        The availability domain the ESXi hosts are running in. For Multi-AD SDDC, it is `multi-AD`.  Example: `Uocm:PHX-AD-1`, `multi-AD`
        """
        return pulumi.get(self, "compute_availability_domain")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A descriptive name for the SDDC. It must be unique, start with a letter, and contain only letters, digits, whitespaces, dashes and underscores. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetSddcsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="sddcCollections")
    def sddc_collections(self) -> Sequence['outputs.GetSddcsSddcCollectionResult']:
        """
        The list of sddc_collection.
        """
        return pulumi.get(self, "sddc_collections")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the SDDC.
        """
        return pulumi.get(self, "state")


class AwaitableGetSddcsResult(GetSddcsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSddcsResult(
            compartment_id=self.compartment_id,
            compute_availability_domain=self.compute_availability_domain,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            sddc_collections=self.sddc_collections,
            state=self.state)


def get_sddcs(compartment_id: Optional[str] = None,
              compute_availability_domain: Optional[str] = None,
              display_name: Optional[str] = None,
              filters: Optional[Sequence[pulumi.InputType['GetSddcsFilterArgs']]] = None,
              state: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSddcsResult:
    """
    This data source provides the list of Sddcs in Oracle Cloud Infrastructure Oracle Cloud VMware Solution service.

    Lists the SDDCs in the specified compartment. The list can be
    filtered by display name or availability domain.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_sddcs = oci.Ocvp.get_sddcs(compartment_id=var["compartment_id"],
        compute_availability_domain=var["sddc_compute_availability_domain"],
        display_name=var["sddc_display_name"],
        state=var["sddc_state"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str compute_availability_domain: The name of the availability domain that the Compute instances are running in.  Example: `Uocm:PHX-AD-1`
    :param str display_name: A filter to return only resources that match the given display name exactly.
    :param str state: The lifecycle state of the resource.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['computeAvailabilityDomain'] = compute_availability_domain
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Ocvp/getSddcs:getSddcs', __args__, opts=opts, typ=GetSddcsResult).value

    return AwaitableGetSddcsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        compute_availability_domain=pulumi.get(__ret__, 'compute_availability_domain'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        sddc_collections=pulumi.get(__ret__, 'sddc_collections'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_sddcs)
def get_sddcs_output(compartment_id: Optional[pulumi.Input[str]] = None,
                     compute_availability_domain: Optional[pulumi.Input[Optional[str]]] = None,
                     display_name: Optional[pulumi.Input[Optional[str]]] = None,
                     filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetSddcsFilterArgs']]]]] = None,
                     state: Optional[pulumi.Input[Optional[str]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSddcsResult]:
    """
    This data source provides the list of Sddcs in Oracle Cloud Infrastructure Oracle Cloud VMware Solution service.

    Lists the SDDCs in the specified compartment. The list can be
    filtered by display name or availability domain.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_sddcs = oci.Ocvp.get_sddcs(compartment_id=var["compartment_id"],
        compute_availability_domain=var["sddc_compute_availability_domain"],
        display_name=var["sddc_display_name"],
        state=var["sddc_state"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str compute_availability_domain: The name of the availability domain that the Compute instances are running in.  Example: `Uocm:PHX-AD-1`
    :param str display_name: A filter to return only resources that match the given display name exactly.
    :param str state: The lifecycle state of the resource.
    """
    ...
