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
    'GetVaultsResult',
    'AwaitableGetVaultsResult',
    'get_vaults',
    'get_vaults_output',
]

@pulumi.output_type
class GetVaultsResult:
    """
    A collection of values returned by getVaults.
    """
    def __init__(__self__, compartment_id=None, filters=None, id=None, vaults=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if vaults and not isinstance(vaults, list):
            raise TypeError("Expected argument 'vaults' to be a list")
        pulumi.set(__self__, "vaults", vaults)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment that contains a particular vault.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetVaultsFilterResult']]:
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
    def vaults(self) -> Sequence['outputs.GetVaultsVaultResult']:
        """
        The list of vaults.
        """
        return pulumi.get(self, "vaults")


class AwaitableGetVaultsResult(GetVaultsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVaultsResult(
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            vaults=self.vaults)


def get_vaults(compartment_id: Optional[str] = None,
               filters: Optional[Sequence[pulumi.InputType['GetVaultsFilterArgs']]] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVaultsResult:
    """
    This data source provides the list of Vaults in Oracle Cloud Infrastructure Kms service.

    Lists the vaults in the specified compartment.

    As a provisioning operation, this call is subject to a Key Management limit that applies to
    the total number of requests across all provisioning read operations. Key Management might
    throttle this call to reject an otherwise valid request when the total rate of provisioning
    read operations exceeds 10 requests per second for a given tenancy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_vaults = oci.Kms.get_vaults(compartment_id=var["compartment_id"])
    ```


    :param str compartment_id: The OCID of the compartment.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Kms/getVaults:getVaults', __args__, opts=opts, typ=GetVaultsResult).value

    return AwaitableGetVaultsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        vaults=pulumi.get(__ret__, 'vaults'))


@_utilities.lift_output_func(get_vaults)
def get_vaults_output(compartment_id: Optional[pulumi.Input[str]] = None,
                      filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetVaultsFilterArgs']]]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVaultsResult]:
    """
    This data source provides the list of Vaults in Oracle Cloud Infrastructure Kms service.

    Lists the vaults in the specified compartment.

    As a provisioning operation, this call is subject to a Key Management limit that applies to
    the total number of requests across all provisioning read operations. Key Management might
    throttle this call to reject an otherwise valid request when the total rate of provisioning
    read operations exceeds 10 requests per second for a given tenancy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_vaults = oci.Kms.get_vaults(compartment_id=var["compartment_id"])
    ```


    :param str compartment_id: The OCID of the compartment.
    """
    ...
