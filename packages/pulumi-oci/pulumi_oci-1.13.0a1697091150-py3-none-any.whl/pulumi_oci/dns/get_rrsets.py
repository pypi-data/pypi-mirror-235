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
    'GetRrsetsResult',
    'AwaitableGetRrsetsResult',
    'get_rrsets',
    'get_rrsets_output',
]

@pulumi.output_type
class GetRrsetsResult:
    """
    A collection of values returned by getRrsets.
    """
    def __init__(__self__, domain=None, domain_contains=None, filters=None, id=None, rrsets=None, rtype=None, scope=None, view_id=None, zone_name_or_id=None):
        if domain and not isinstance(domain, str):
            raise TypeError("Expected argument 'domain' to be a str")
        pulumi.set(__self__, "domain", domain)
        if domain_contains and not isinstance(domain_contains, str):
            raise TypeError("Expected argument 'domain_contains' to be a str")
        pulumi.set(__self__, "domain_contains", domain_contains)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if rrsets and not isinstance(rrsets, list):
            raise TypeError("Expected argument 'rrsets' to be a list")
        pulumi.set(__self__, "rrsets", rrsets)
        if rtype and not isinstance(rtype, str):
            raise TypeError("Expected argument 'rtype' to be a str")
        pulumi.set(__self__, "rtype", rtype)
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        pulumi.set(__self__, "scope", scope)
        if view_id and not isinstance(view_id, str):
            raise TypeError("Expected argument 'view_id' to be a str")
        pulumi.set(__self__, "view_id", view_id)
        if zone_name_or_id and not isinstance(zone_name_or_id, str):
            raise TypeError("Expected argument 'zone_name_or_id' to be a str")
        pulumi.set(__self__, "zone_name_or_id", zone_name_or_id)

    @property
    @pulumi.getter
    def domain(self) -> Optional[str]:
        """
        The fully qualified domain name where the record can be located.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="domainContains")
    def domain_contains(self) -> Optional[str]:
        return pulumi.get(self, "domain_contains")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetRrsetsFilterResult']]:
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
    def rrsets(self) -> Sequence['outputs.GetRrsetsRrsetResult']:
        """
        The list of rrsets.
        """
        return pulumi.get(self, "rrsets")

    @property
    @pulumi.getter
    def rtype(self) -> Optional[str]:
        """
        The type of DNS record, such as A or CNAME. For more information, see [Resource Record (RR) TYPEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).
        """
        return pulumi.get(self, "rtype")

    @property
    @pulumi.getter
    def scope(self) -> Optional[str]:
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="viewId")
    def view_id(self) -> Optional[str]:
        return pulumi.get(self, "view_id")

    @property
    @pulumi.getter(name="zoneNameOrId")
    def zone_name_or_id(self) -> str:
        return pulumi.get(self, "zone_name_or_id")


class AwaitableGetRrsetsResult(GetRrsetsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRrsetsResult(
            domain=self.domain,
            domain_contains=self.domain_contains,
            filters=self.filters,
            id=self.id,
            rrsets=self.rrsets,
            rtype=self.rtype,
            scope=self.scope,
            view_id=self.view_id,
            zone_name_or_id=self.zone_name_or_id)


def get_rrsets(domain: Optional[str] = None,
               domain_contains: Optional[str] = None,
               filters: Optional[Sequence[pulumi.InputType['GetRrsetsFilterArgs']]] = None,
               rtype: Optional[str] = None,
               scope: Optional[str] = None,
               view_id: Optional[str] = None,
               zone_name_or_id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRrsetsResult:
    """
    This data source provides the list of RRsets in Oracle Cloud Infrastructure DNS service.

    Gets a list of all rrsets in the specified zone. You can optionally filter the results using the listed parameters.
    For private zones, the scope query parameter is required with a value of `PRIVATE`. When the zone name is
    provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query
    parameter is required.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_rrsets = oci.Dns.get_rrsets(zone_name_or_id=oci_dns_zone["test_zone"]["id"],
        domain=var["rrset_domain"],
        domain_contains=var["rrset_domain"],
        rtype=var["rrset_rtype"],
        scope=var["rrset_scope"],
        view_id=oci_dns_view["test_view"]["id"])
    ```


    :param str domain: The target fully-qualified domain name (FQDN) within the target zone.
    :param str domain_contains: Matches any rrset whose fully-qualified domain name (FQDN) contains the provided value.
    :param str rtype: Search by record type. Will match any record whose [type](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4) (case-insensitive) equals the provided value.
    :param str scope: Specifies to operate only on resources that have a matching DNS scope.
    :param str view_id: The OCID of the view the resource is associated with.
    :param str zone_name_or_id: The name or OCID of the target zone.
    """
    __args__ = dict()
    __args__['domain'] = domain
    __args__['domainContains'] = domain_contains
    __args__['filters'] = filters
    __args__['rtype'] = rtype
    __args__['scope'] = scope
    __args__['viewId'] = view_id
    __args__['zoneNameOrId'] = zone_name_or_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Dns/getRrsets:getRrsets', __args__, opts=opts, typ=GetRrsetsResult).value

    return AwaitableGetRrsetsResult(
        domain=pulumi.get(__ret__, 'domain'),
        domain_contains=pulumi.get(__ret__, 'domain_contains'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        rrsets=pulumi.get(__ret__, 'rrsets'),
        rtype=pulumi.get(__ret__, 'rtype'),
        scope=pulumi.get(__ret__, 'scope'),
        view_id=pulumi.get(__ret__, 'view_id'),
        zone_name_or_id=pulumi.get(__ret__, 'zone_name_or_id'))


@_utilities.lift_output_func(get_rrsets)
def get_rrsets_output(domain: Optional[pulumi.Input[Optional[str]]] = None,
                      domain_contains: Optional[pulumi.Input[Optional[str]]] = None,
                      filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetRrsetsFilterArgs']]]]] = None,
                      rtype: Optional[pulumi.Input[Optional[str]]] = None,
                      scope: Optional[pulumi.Input[Optional[str]]] = None,
                      view_id: Optional[pulumi.Input[Optional[str]]] = None,
                      zone_name_or_id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRrsetsResult]:
    """
    This data source provides the list of RRsets in Oracle Cloud Infrastructure DNS service.

    Gets a list of all rrsets in the specified zone. You can optionally filter the results using the listed parameters.
    For private zones, the scope query parameter is required with a value of `PRIVATE`. When the zone name is
    provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query
    parameter is required.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_rrsets = oci.Dns.get_rrsets(zone_name_or_id=oci_dns_zone["test_zone"]["id"],
        domain=var["rrset_domain"],
        domain_contains=var["rrset_domain"],
        rtype=var["rrset_rtype"],
        scope=var["rrset_scope"],
        view_id=oci_dns_view["test_view"]["id"])
    ```


    :param str domain: The target fully-qualified domain name (FQDN) within the target zone.
    :param str domain_contains: Matches any rrset whose fully-qualified domain name (FQDN) contains the provided value.
    :param str rtype: Search by record type. Will match any record whose [type](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4) (case-insensitive) equals the provided value.
    :param str scope: Specifies to operate only on resources that have a matching DNS scope.
    :param str view_id: The OCID of the view the resource is associated with.
    :param str zone_name_or_id: The name or OCID of the target zone.
    """
    ...
