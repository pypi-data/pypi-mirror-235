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
    'GetRecordsResult',
    'AwaitableGetRecordsResult',
    'get_records',
    'get_records_output',
]

@pulumi.output_type
class GetRecordsResult:
    """
    A collection of values returned by getRecords.
    """
    def __init__(__self__, compartment_id=None, domain=None, domain_contains=None, filters=None, id=None, records=None, rtype=None, sort_by=None, sort_order=None, zone_name_or_id=None, zone_version=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
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
        if records and not isinstance(records, list):
            raise TypeError("Expected argument 'records' to be a list")
        pulumi.set(__self__, "records", records)
        if rtype and not isinstance(rtype, str):
            raise TypeError("Expected argument 'rtype' to be a str")
        pulumi.set(__self__, "rtype", rtype)
        if sort_by and not isinstance(sort_by, str):
            raise TypeError("Expected argument 'sort_by' to be a str")
        pulumi.set(__self__, "sort_by", sort_by)
        if sort_order and not isinstance(sort_order, str):
            raise TypeError("Expected argument 'sort_order' to be a str")
        pulumi.set(__self__, "sort_order", sort_order)
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
    def filters(self) -> Optional[Sequence['outputs.GetRecordsFilterResult']]:
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
    def records(self) -> Sequence['outputs.GetRecordsRecordResult']:
        """
        The list of records.
        """
        return pulumi.get(self, "records")

    @property
    @pulumi.getter
    def rtype(self) -> Optional[str]:
        """
        The canonical name for the record's type, such as A or CNAME. For more information, see [Resource Record (RR) TYPEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).
        """
        return pulumi.get(self, "rtype")

    @property
    @pulumi.getter(name="sortBy")
    def sort_by(self) -> Optional[str]:
        return pulumi.get(self, "sort_by")

    @property
    @pulumi.getter(name="sortOrder")
    def sort_order(self) -> Optional[str]:
        return pulumi.get(self, "sort_order")

    @property
    @pulumi.getter(name="zoneNameOrId")
    def zone_name_or_id(self) -> str:
        """
        The name or OCID of the target zone.
        """
        warnings.warn("""The 'oci_dns_records' resource has been deprecated. Please use 'oci_dns_rrsets' instead.""", DeprecationWarning)
        pulumi.log.warn("""zone_name_or_id is deprecated: The 'oci_dns_records' resource has been deprecated. Please use 'oci_dns_rrsets' instead.""")

        return pulumi.get(self, "zone_name_or_id")

    @property
    @pulumi.getter(name="zoneVersion")
    def zone_version(self) -> Optional[str]:
        return pulumi.get(self, "zone_version")


class AwaitableGetRecordsResult(GetRecordsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRecordsResult(
            compartment_id=self.compartment_id,
            domain=self.domain,
            domain_contains=self.domain_contains,
            filters=self.filters,
            id=self.id,
            records=self.records,
            rtype=self.rtype,
            sort_by=self.sort_by,
            sort_order=self.sort_order,
            zone_name_or_id=self.zone_name_or_id,
            zone_version=self.zone_version)


def get_records(compartment_id: Optional[str] = None,
                domain: Optional[str] = None,
                domain_contains: Optional[str] = None,
                filters: Optional[Sequence[pulumi.InputType['GetRecordsFilterArgs']]] = None,
                rtype: Optional[str] = None,
                sort_by: Optional[str] = None,
                sort_order: Optional[str] = None,
                zone_name_or_id: Optional[str] = None,
                zone_version: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRecordsResult:
    """
    **Deprecated. Use dns_get_rrsets instead.**

    This data source provides the list of Records in Oracle Cloud Infrastructure DNS service.

    Gets all records in the specified zone. The results are sorted by `domain` in alphabetical order by default.
    For more information about records, see [Resource Record (RR) TYPEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).
    For private zones, the scope query parameter is required with a value of `PRIVATE`. When the zone name is
    provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query
    parameter is required.


    :param str compartment_id: The OCID of the compartment the resource belongs to.
    :param str domain: Search by domain. Will match any record whose domain (case-insensitive) equals the provided value.
    :param str domain_contains: Search by domain. Will match any record whose domain (case-insensitive) contains the provided value.
    :param str rtype: Search by record type. Will match any record whose [type](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4) (case-insensitive) equals the provided value.
    :param str sort_by: The field by which to sort records. Allowed values are: domain|rtype|ttl
    :param str sort_order: The order to sort the resources. Allowed values are: ASC|DESC
    :param str zone_name_or_id: The name or OCID of the target zone.
    :param str zone_version: The version of the zone for which data is requested.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['domain'] = domain
    __args__['domainContains'] = domain_contains
    __args__['filters'] = filters
    __args__['rtype'] = rtype
    __args__['sortBy'] = sort_by
    __args__['sortOrder'] = sort_order
    __args__['zoneNameOrId'] = zone_name_or_id
    __args__['zoneVersion'] = zone_version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Dns/getRecords:getRecords', __args__, opts=opts, typ=GetRecordsResult).value

    return AwaitableGetRecordsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        domain=pulumi.get(__ret__, 'domain'),
        domain_contains=pulumi.get(__ret__, 'domain_contains'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        records=pulumi.get(__ret__, 'records'),
        rtype=pulumi.get(__ret__, 'rtype'),
        sort_by=pulumi.get(__ret__, 'sort_by'),
        sort_order=pulumi.get(__ret__, 'sort_order'),
        zone_name_or_id=pulumi.get(__ret__, 'zone_name_or_id'),
        zone_version=pulumi.get(__ret__, 'zone_version'))


@_utilities.lift_output_func(get_records)
def get_records_output(compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                       domain: Optional[pulumi.Input[Optional[str]]] = None,
                       domain_contains: Optional[pulumi.Input[Optional[str]]] = None,
                       filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetRecordsFilterArgs']]]]] = None,
                       rtype: Optional[pulumi.Input[Optional[str]]] = None,
                       sort_by: Optional[pulumi.Input[Optional[str]]] = None,
                       sort_order: Optional[pulumi.Input[Optional[str]]] = None,
                       zone_name_or_id: Optional[pulumi.Input[str]] = None,
                       zone_version: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRecordsResult]:
    """
    **Deprecated. Use dns_get_rrsets instead.**

    This data source provides the list of Records in Oracle Cloud Infrastructure DNS service.

    Gets all records in the specified zone. The results are sorted by `domain` in alphabetical order by default.
    For more information about records, see [Resource Record (RR) TYPEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).
    For private zones, the scope query parameter is required with a value of `PRIVATE`. When the zone name is
    provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query
    parameter is required.


    :param str compartment_id: The OCID of the compartment the resource belongs to.
    :param str domain: Search by domain. Will match any record whose domain (case-insensitive) equals the provided value.
    :param str domain_contains: Search by domain. Will match any record whose domain (case-insensitive) contains the provided value.
    :param str rtype: Search by record type. Will match any record whose [type](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4) (case-insensitive) equals the provided value.
    :param str sort_by: The field by which to sort records. Allowed values are: domain|rtype|ttl
    :param str sort_order: The order to sort the resources. Allowed values are: ASC|DESC
    :param str zone_name_or_id: The name or OCID of the target zone.
    :param str zone_version: The version of the zone for which data is requested.
    """
    ...
