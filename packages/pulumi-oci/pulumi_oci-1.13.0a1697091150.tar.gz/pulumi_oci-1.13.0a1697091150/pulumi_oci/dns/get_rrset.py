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

__all__ = [
    'GetRrsetResult',
    'AwaitableGetRrsetResult',
    'get_rrset',
    'get_rrset_output',
]

@pulumi.output_type
class GetRrsetResult:
    """
    A collection of values returned by getRrset.
    """
    def __init__(__self__, compartment_id=None, domain=None, id=None, items=None, rtype=None, scope=None, view_id=None, zone_name_or_id=None, zone_version=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if domain and not isinstance(domain, str):
            raise TypeError("Expected argument 'domain' to be a str")
        pulumi.set(__self__, "domain", domain)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if items and not isinstance(items, list):
            raise TypeError("Expected argument 'items' to be a list")
        pulumi.set(__self__, "items", items)
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
        if zone_version and not isinstance(zone_version, str):
            raise TypeError("Expected argument 'zone_version' to be a str")
        pulumi.set(__self__, "zone_version", zone_version)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def domain(self) -> str:
        """
        The fully qualified domain name where the record can be located.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.GetRrsetItemResult']:
        return pulumi.get(self, "items")

    @property
    @pulumi.getter
    def rtype(self) -> str:
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

    @property
    @pulumi.getter(name="zoneVersion")
    def zone_version(self) -> Optional[str]:
        return pulumi.get(self, "zone_version")


class AwaitableGetRrsetResult(GetRrsetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRrsetResult(
            compartment_id=self.compartment_id,
            domain=self.domain,
            id=self.id,
            items=self.items,
            rtype=self.rtype,
            scope=self.scope,
            view_id=self.view_id,
            zone_name_or_id=self.zone_name_or_id,
            zone_version=self.zone_version)


def get_rrset(compartment_id: Optional[str] = None,
              domain: Optional[str] = None,
              rtype: Optional[str] = None,
              scope: Optional[str] = None,
              view_id: Optional[str] = None,
              zone_name_or_id: Optional[str] = None,
              zone_version: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRrsetResult:
    """
    This data source provides details about a specific Rrset resource in Oracle Cloud Infrastructure DNS service.

    Gets a list of all records in the specified RRSet. The results are sorted by `recordHash` by default. For
    private zones, the scope query parameter is required with a value of `PRIVATE`. When the zone name is
    provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query
    parameter is required.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_rrset = oci.Dns.get_rrset(domain=var["rrset_domain"],
        rtype=var["rrset_rtype"],
        zone_name_or_id=oci_dns_zone["test_zone"]["id"],
        compartment_id=var["compartment_id"],
        scope=var["rrset_scope"],
        view_id=oci_dns_view["test_view"]["id"])
    ```


    :param str compartment_id: The OCID of the compartment the resource belongs to.
    :param str domain: The target fully-qualified domain name (FQDN) within the target zone.
    :param str rtype: The type of the target RRSet within the target zone.
    :param str scope: Specifies to operate only on resources that have a matching DNS scope.
           This value will be null for zones in the global DNS and `PRIVATE` when listing private Rrsets.
    :param str view_id: The OCID of the view the resource is associated with.
    :param str zone_name_or_id: The name or OCID of the target zone.
    :param str zone_version: The version of the zone for which data is requested.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['domain'] = domain
    __args__['rtype'] = rtype
    __args__['scope'] = scope
    __args__['viewId'] = view_id
    __args__['zoneNameOrId'] = zone_name_or_id
    __args__['zoneVersion'] = zone_version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Dns/getRrset:getRrset', __args__, opts=opts, typ=GetRrsetResult).value

    return AwaitableGetRrsetResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        domain=pulumi.get(__ret__, 'domain'),
        id=pulumi.get(__ret__, 'id'),
        items=pulumi.get(__ret__, 'items'),
        rtype=pulumi.get(__ret__, 'rtype'),
        scope=pulumi.get(__ret__, 'scope'),
        view_id=pulumi.get(__ret__, 'view_id'),
        zone_name_or_id=pulumi.get(__ret__, 'zone_name_or_id'),
        zone_version=pulumi.get(__ret__, 'zone_version'))


@_utilities.lift_output_func(get_rrset)
def get_rrset_output(compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                     domain: Optional[pulumi.Input[str]] = None,
                     rtype: Optional[pulumi.Input[str]] = None,
                     scope: Optional[pulumi.Input[Optional[str]]] = None,
                     view_id: Optional[pulumi.Input[Optional[str]]] = None,
                     zone_name_or_id: Optional[pulumi.Input[str]] = None,
                     zone_version: Optional[pulumi.Input[Optional[str]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRrsetResult]:
    """
    This data source provides details about a specific Rrset resource in Oracle Cloud Infrastructure DNS service.

    Gets a list of all records in the specified RRSet. The results are sorted by `recordHash` by default. For
    private zones, the scope query parameter is required with a value of `PRIVATE`. When the zone name is
    provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query
    parameter is required.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_rrset = oci.Dns.get_rrset(domain=var["rrset_domain"],
        rtype=var["rrset_rtype"],
        zone_name_or_id=oci_dns_zone["test_zone"]["id"],
        compartment_id=var["compartment_id"],
        scope=var["rrset_scope"],
        view_id=oci_dns_view["test_view"]["id"])
    ```


    :param str compartment_id: The OCID of the compartment the resource belongs to.
    :param str domain: The target fully-qualified domain name (FQDN) within the target zone.
    :param str rtype: The type of the target RRSet within the target zone.
    :param str scope: Specifies to operate only on resources that have a matching DNS scope.
           This value will be null for zones in the global DNS and `PRIVATE` when listing private Rrsets.
    :param str view_id: The OCID of the view the resource is associated with.
    :param str zone_name_or_id: The name or OCID of the target zone.
    :param str zone_version: The version of the zone for which data is requested.
    """
    ...
