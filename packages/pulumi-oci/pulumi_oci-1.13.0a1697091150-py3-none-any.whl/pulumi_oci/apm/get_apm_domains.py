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
    'GetApmDomainsResult',
    'AwaitableGetApmDomainsResult',
    'get_apm_domains',
    'get_apm_domains_output',
]

@pulumi.output_type
class GetApmDomainsResult:
    """
    A collection of values returned by getApmDomains.
    """
    def __init__(__self__, apm_domains=None, compartment_id=None, display_name=None, filters=None, id=None, state=None):
        if apm_domains and not isinstance(apm_domains, list):
            raise TypeError("Expected argument 'apm_domains' to be a list")
        pulumi.set(__self__, "apm_domains", apm_domains)
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
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="apmDomains")
    def apm_domains(self) -> Sequence['outputs.GetApmDomainsApmDomainResult']:
        """
        The list of apm_domains.
        """
        return pulumi.get(self, "apm_domains")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment corresponding to the APM domain.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        Display name of the APM domain, which can be updated.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetApmDomainsFilterResult']]:
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
    def state(self) -> Optional[str]:
        """
        The current lifecycle state of the APM domain.
        """
        return pulumi.get(self, "state")


class AwaitableGetApmDomainsResult(GetApmDomainsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApmDomainsResult(
            apm_domains=self.apm_domains,
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            state=self.state)


def get_apm_domains(compartment_id: Optional[str] = None,
                    display_name: Optional[str] = None,
                    filters: Optional[Sequence[pulumi.InputType['GetApmDomainsFilterArgs']]] = None,
                    state: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApmDomainsResult:
    """
    This data source provides the list of Apm Domains in Oracle Cloud Infrastructure Apm service.

    Lists all APM domains for the specified tenant compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_apm_domains = oci.Apm.get_apm_domains(compartment_id=var["compartment_id"],
        display_name=var["apm_domain_display_name"],
        state=var["apm_domain_state"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str state: A filter to return only resources that match the given life-cycle state.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Apm/getApmDomains:getApmDomains', __args__, opts=opts, typ=GetApmDomainsResult).value

    return AwaitableGetApmDomainsResult(
        apm_domains=pulumi.get(__ret__, 'apm_domains'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_apm_domains)
def get_apm_domains_output(compartment_id: Optional[pulumi.Input[str]] = None,
                           display_name: Optional[pulumi.Input[Optional[str]]] = None,
                           filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetApmDomainsFilterArgs']]]]] = None,
                           state: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApmDomainsResult]:
    """
    This data source provides the list of Apm Domains in Oracle Cloud Infrastructure Apm service.

    Lists all APM domains for the specified tenant compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_apm_domains = oci.Apm.get_apm_domains(compartment_id=var["compartment_id"],
        display_name=var["apm_domain_display_name"],
        state=var["apm_domain_state"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str state: A filter to return only resources that match the given life-cycle state.
    """
    ...
