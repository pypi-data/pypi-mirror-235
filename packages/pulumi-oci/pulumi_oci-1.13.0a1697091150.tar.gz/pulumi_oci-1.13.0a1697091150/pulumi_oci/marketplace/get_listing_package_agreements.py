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
    'GetListingPackageAgreementsResult',
    'AwaitableGetListingPackageAgreementsResult',
    'get_listing_package_agreements',
    'get_listing_package_agreements_output',
]

@pulumi.output_type
class GetListingPackageAgreementsResult:
    """
    A collection of values returned by getListingPackageAgreements.
    """
    def __init__(__self__, agreements=None, compartment_id=None, filters=None, id=None, listing_id=None, package_version=None):
        if agreements and not isinstance(agreements, list):
            raise TypeError("Expected argument 'agreements' to be a list")
        pulumi.set(__self__, "agreements", agreements)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if listing_id and not isinstance(listing_id, str):
            raise TypeError("Expected argument 'listing_id' to be a str")
        pulumi.set(__self__, "listing_id", listing_id)
        if package_version and not isinstance(package_version, str):
            raise TypeError("Expected argument 'package_version' to be a str")
        pulumi.set(__self__, "package_version", package_version)

    @property
    @pulumi.getter
    def agreements(self) -> Sequence['outputs.GetListingPackageAgreementsAgreementResult']:
        """
        The list of agreements.
        """
        return pulumi.get(self, "agreements")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        """
        The unique identifier for the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetListingPackageAgreementsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="listingId")
    def listing_id(self) -> str:
        return pulumi.get(self, "listing_id")

    @property
    @pulumi.getter(name="packageVersion")
    def package_version(self) -> str:
        return pulumi.get(self, "package_version")


class AwaitableGetListingPackageAgreementsResult(GetListingPackageAgreementsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetListingPackageAgreementsResult(
            agreements=self.agreements,
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            listing_id=self.listing_id,
            package_version=self.package_version)


def get_listing_package_agreements(compartment_id: Optional[str] = None,
                                   filters: Optional[Sequence[pulumi.InputType['GetListingPackageAgreementsFilterArgs']]] = None,
                                   listing_id: Optional[str] = None,
                                   package_version: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetListingPackageAgreementsResult:
    """
    This data source provides the list of Listing Package Agreements in Oracle Cloud Infrastructure Marketplace service.

    Returns the terms of use agreements that must be accepted before you can deploy the specified version of a package.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_listing_package_agreements = oci.Marketplace.get_listing_package_agreements(listing_id=oci_marketplace_listing["test_listing"]["id"],
        package_version=var["listing_package_agreement_package_version"],
        compartment_id=var["compartment_id"])
    ```


    :param str compartment_id: The unique identifier for the compartment.
    :param str listing_id: The unique identifier for the listing.
    :param str package_version: The version of the package. Package versions are unique within a listing.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['listingId'] = listing_id
    __args__['packageVersion'] = package_version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Marketplace/getListingPackageAgreements:getListingPackageAgreements', __args__, opts=opts, typ=GetListingPackageAgreementsResult).value

    return AwaitableGetListingPackageAgreementsResult(
        agreements=pulumi.get(__ret__, 'agreements'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        listing_id=pulumi.get(__ret__, 'listing_id'),
        package_version=pulumi.get(__ret__, 'package_version'))


@_utilities.lift_output_func(get_listing_package_agreements)
def get_listing_package_agreements_output(compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                                          filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetListingPackageAgreementsFilterArgs']]]]] = None,
                                          listing_id: Optional[pulumi.Input[str]] = None,
                                          package_version: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetListingPackageAgreementsResult]:
    """
    This data source provides the list of Listing Package Agreements in Oracle Cloud Infrastructure Marketplace service.

    Returns the terms of use agreements that must be accepted before you can deploy the specified version of a package.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_listing_package_agreements = oci.Marketplace.get_listing_package_agreements(listing_id=oci_marketplace_listing["test_listing"]["id"],
        package_version=var["listing_package_agreement_package_version"],
        compartment_id=var["compartment_id"])
    ```


    :param str compartment_id: The unique identifier for the compartment.
    :param str listing_id: The unique identifier for the listing.
    :param str package_version: The version of the package. Package versions are unique within a listing.
    """
    ...
