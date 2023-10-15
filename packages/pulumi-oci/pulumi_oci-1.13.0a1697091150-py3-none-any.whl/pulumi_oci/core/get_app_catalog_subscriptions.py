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
    'GetAppCatalogSubscriptionsResult',
    'AwaitableGetAppCatalogSubscriptionsResult',
    'get_app_catalog_subscriptions',
    'get_app_catalog_subscriptions_output',
]

@pulumi.output_type
class GetAppCatalogSubscriptionsResult:
    """
    A collection of values returned by getAppCatalogSubscriptions.
    """
    def __init__(__self__, app_catalog_subscriptions=None, compartment_id=None, filters=None, id=None, listing_id=None):
        if app_catalog_subscriptions and not isinstance(app_catalog_subscriptions, list):
            raise TypeError("Expected argument 'app_catalog_subscriptions' to be a list")
        pulumi.set(__self__, "app_catalog_subscriptions", app_catalog_subscriptions)
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

    @property
    @pulumi.getter(name="appCatalogSubscriptions")
    def app_catalog_subscriptions(self) -> Sequence['outputs.GetAppCatalogSubscriptionsAppCatalogSubscriptionResult']:
        """
        The list of app_catalog_subscriptions.
        """
        return pulumi.get(self, "app_catalog_subscriptions")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The compartmentID of the subscription.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetAppCatalogSubscriptionsFilterResult']]:
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
    def listing_id(self) -> Optional[str]:
        """
        The ocid of the listing resource.
        """
        return pulumi.get(self, "listing_id")


class AwaitableGetAppCatalogSubscriptionsResult(GetAppCatalogSubscriptionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAppCatalogSubscriptionsResult(
            app_catalog_subscriptions=self.app_catalog_subscriptions,
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            listing_id=self.listing_id)


def get_app_catalog_subscriptions(compartment_id: Optional[str] = None,
                                  filters: Optional[Sequence[pulumi.InputType['GetAppCatalogSubscriptionsFilterArgs']]] = None,
                                  listing_id: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAppCatalogSubscriptionsResult:
    """
    This data source provides the list of App Catalog Subscriptions in Oracle Cloud Infrastructure Core service.

    Lists subscriptions for a compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_app_catalog_subscriptions = oci.Core.get_app_catalog_subscriptions(compartment_id=var["compartment_id"],
        listing_id=data["oci_core_app_catalog_listing"]["test_listing"]["id"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str listing_id: A filter to return only the listings that matches the given listing id.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['listingId'] = listing_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Core/getAppCatalogSubscriptions:getAppCatalogSubscriptions', __args__, opts=opts, typ=GetAppCatalogSubscriptionsResult).value

    return AwaitableGetAppCatalogSubscriptionsResult(
        app_catalog_subscriptions=pulumi.get(__ret__, 'app_catalog_subscriptions'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        listing_id=pulumi.get(__ret__, 'listing_id'))


@_utilities.lift_output_func(get_app_catalog_subscriptions)
def get_app_catalog_subscriptions_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                         filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetAppCatalogSubscriptionsFilterArgs']]]]] = None,
                                         listing_id: Optional[pulumi.Input[Optional[str]]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAppCatalogSubscriptionsResult]:
    """
    This data source provides the list of App Catalog Subscriptions in Oracle Cloud Infrastructure Core service.

    Lists subscriptions for a compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_app_catalog_subscriptions = oci.Core.get_app_catalog_subscriptions(compartment_id=var["compartment_id"],
        listing_id=data["oci_core_app_catalog_listing"]["test_listing"]["id"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str listing_id: A filter to return only the listings that matches the given listing id.
    """
    ...
