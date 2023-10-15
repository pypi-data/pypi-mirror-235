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
    'GetQuotasResult',
    'AwaitableGetQuotasResult',
    'get_quotas',
    'get_quotas_output',
]

@pulumi.output_type
class GetQuotasResult:
    """
    A collection of values returned by getQuotas.
    """
    def __init__(__self__, compartment_id=None, filters=None, id=None, name=None, quotas=None, state=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if quotas and not isinstance(quotas, list):
            raise TypeError("Expected argument 'quotas' to be a list")
        pulumi.set(__self__, "quotas", quotas)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment containing the resource this quota applies to.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetQuotasFilterResult']]:
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
    def name(self) -> Optional[str]:
        """
        The name you assign to the quota during creation. The name must be unique across all quotas in the tenancy and cannot be changed.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def quotas(self) -> Sequence['outputs.GetQuotasQuotaResult']:
        """
        The list of quotas.
        """
        return pulumi.get(self, "quotas")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The quota's current state.
        """
        return pulumi.get(self, "state")


class AwaitableGetQuotasResult(GetQuotasResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetQuotasResult(
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            name=self.name,
            quotas=self.quotas,
            state=self.state)


def get_quotas(compartment_id: Optional[str] = None,
               filters: Optional[Sequence[pulumi.InputType['GetQuotasFilterArgs']]] = None,
               name: Optional[str] = None,
               state: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetQuotasResult:
    """
    This data source provides the list of Quotas in Oracle Cloud Infrastructure Limits service.

    Lists all quotas on resources from the given compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_quotas = oci.Limits.get_quotas(compartment_id=var["tenancy_ocid"],
        name=var["quota_name"],
        state=var["quota_state"])
    ```


    :param str compartment_id: The OCID of the parent compartment (remember that the tenancy is simply the root compartment).
    :param str name: name
    :param str state: Filters returned quotas based on the given state.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['name'] = name
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Limits/getQuotas:getQuotas', __args__, opts=opts, typ=GetQuotasResult).value

    return AwaitableGetQuotasResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        quotas=pulumi.get(__ret__, 'quotas'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_quotas)
def get_quotas_output(compartment_id: Optional[pulumi.Input[str]] = None,
                      filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetQuotasFilterArgs']]]]] = None,
                      name: Optional[pulumi.Input[Optional[str]]] = None,
                      state: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetQuotasResult]:
    """
    This data source provides the list of Quotas in Oracle Cloud Infrastructure Limits service.

    Lists all quotas on resources from the given compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_quotas = oci.Limits.get_quotas(compartment_id=var["tenancy_ocid"],
        name=var["quota_name"],
        state=var["quota_state"])
    ```


    :param str compartment_id: The OCID of the parent compartment (remember that the tenancy is simply the root compartment).
    :param str name: name
    :param str state: Filters returned quotas based on the given state.
    """
    ...
