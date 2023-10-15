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
    'GetSubscriptionRedemptionsResult',
    'AwaitableGetSubscriptionRedemptionsResult',
    'get_subscription_redemptions',
    'get_subscription_redemptions_output',
]

@pulumi.output_type
class GetSubscriptionRedemptionsResult:
    """
    A collection of values returned by getSubscriptionRedemptions.
    """
    def __init__(__self__, filters=None, id=None, redemption_collections=None, subscription_id=None, tenancy_id=None, time_redeemed_greater_than_or_equal_to=None, time_redeemed_less_than=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if redemption_collections and not isinstance(redemption_collections, list):
            raise TypeError("Expected argument 'redemption_collections' to be a list")
        pulumi.set(__self__, "redemption_collections", redemption_collections)
        if subscription_id and not isinstance(subscription_id, str):
            raise TypeError("Expected argument 'subscription_id' to be a str")
        pulumi.set(__self__, "subscription_id", subscription_id)
        if tenancy_id and not isinstance(tenancy_id, str):
            raise TypeError("Expected argument 'tenancy_id' to be a str")
        pulumi.set(__self__, "tenancy_id", tenancy_id)
        if time_redeemed_greater_than_or_equal_to and not isinstance(time_redeemed_greater_than_or_equal_to, str):
            raise TypeError("Expected argument 'time_redeemed_greater_than_or_equal_to' to be a str")
        pulumi.set(__self__, "time_redeemed_greater_than_or_equal_to", time_redeemed_greater_than_or_equal_to)
        if time_redeemed_less_than and not isinstance(time_redeemed_less_than, str):
            raise TypeError("Expected argument 'time_redeemed_less_than' to be a str")
        pulumi.set(__self__, "time_redeemed_less_than", time_redeemed_less_than)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetSubscriptionRedemptionsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="redemptionCollections")
    def redemption_collections(self) -> Sequence['outputs.GetSubscriptionRedemptionsRedemptionCollectionResult']:
        """
        The list of redemption_collection.
        """
        return pulumi.get(self, "redemption_collections")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> str:
        return pulumi.get(self, "subscription_id")

    @property
    @pulumi.getter(name="tenancyId")
    def tenancy_id(self) -> str:
        return pulumi.get(self, "tenancy_id")

    @property
    @pulumi.getter(name="timeRedeemedGreaterThanOrEqualTo")
    def time_redeemed_greater_than_or_equal_to(self) -> Optional[str]:
        return pulumi.get(self, "time_redeemed_greater_than_or_equal_to")

    @property
    @pulumi.getter(name="timeRedeemedLessThan")
    def time_redeemed_less_than(self) -> Optional[str]:
        return pulumi.get(self, "time_redeemed_less_than")


class AwaitableGetSubscriptionRedemptionsResult(GetSubscriptionRedemptionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSubscriptionRedemptionsResult(
            filters=self.filters,
            id=self.id,
            redemption_collections=self.redemption_collections,
            subscription_id=self.subscription_id,
            tenancy_id=self.tenancy_id,
            time_redeemed_greater_than_or_equal_to=self.time_redeemed_greater_than_or_equal_to,
            time_redeemed_less_than=self.time_redeemed_less_than)


def get_subscription_redemptions(filters: Optional[Sequence[pulumi.InputType['GetSubscriptionRedemptionsFilterArgs']]] = None,
                                 subscription_id: Optional[str] = None,
                                 tenancy_id: Optional[str] = None,
                                 time_redeemed_greater_than_or_equal_to: Optional[str] = None,
                                 time_redeemed_less_than: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSubscriptionRedemptionsResult:
    """
    This data source provides the list of Subscription Redemptions in Oracle Cloud Infrastructure Usage Proxy service.

    Returns the list of redemption for the subscription ID.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_subscription_redemptions = oci.UsageProxy.get_subscription_redemptions(subscription_id=oci_onesubscription_subscription["test_subscription"]["id"],
        tenancy_id=oci_identity_tenancy["test_tenancy"]["id"],
        time_redeemed_greater_than_or_equal_to=var["subscription_redemption_time_redeemed_greater_than_or_equal_to"],
        time_redeemed_less_than=var["subscription_redemption_time_redeemed_less_than"])
    ```


    :param str subscription_id: The subscription ID for which rewards information is requested for.
    :param str tenancy_id: The OCID of the tenancy.
    :param str time_redeemed_greater_than_or_equal_to: The starting redeemed date filter for the redemption history.
    :param str time_redeemed_less_than: The ending redeemed date filter for the redemption history.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['subscriptionId'] = subscription_id
    __args__['tenancyId'] = tenancy_id
    __args__['timeRedeemedGreaterThanOrEqualTo'] = time_redeemed_greater_than_or_equal_to
    __args__['timeRedeemedLessThan'] = time_redeemed_less_than
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:UsageProxy/getSubscriptionRedemptions:getSubscriptionRedemptions', __args__, opts=opts, typ=GetSubscriptionRedemptionsResult).value

    return AwaitableGetSubscriptionRedemptionsResult(
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        redemption_collections=pulumi.get(__ret__, 'redemption_collections'),
        subscription_id=pulumi.get(__ret__, 'subscription_id'),
        tenancy_id=pulumi.get(__ret__, 'tenancy_id'),
        time_redeemed_greater_than_or_equal_to=pulumi.get(__ret__, 'time_redeemed_greater_than_or_equal_to'),
        time_redeemed_less_than=pulumi.get(__ret__, 'time_redeemed_less_than'))


@_utilities.lift_output_func(get_subscription_redemptions)
def get_subscription_redemptions_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetSubscriptionRedemptionsFilterArgs']]]]] = None,
                                        subscription_id: Optional[pulumi.Input[str]] = None,
                                        tenancy_id: Optional[pulumi.Input[str]] = None,
                                        time_redeemed_greater_than_or_equal_to: Optional[pulumi.Input[Optional[str]]] = None,
                                        time_redeemed_less_than: Optional[pulumi.Input[Optional[str]]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSubscriptionRedemptionsResult]:
    """
    This data source provides the list of Subscription Redemptions in Oracle Cloud Infrastructure Usage Proxy service.

    Returns the list of redemption for the subscription ID.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_subscription_redemptions = oci.UsageProxy.get_subscription_redemptions(subscription_id=oci_onesubscription_subscription["test_subscription"]["id"],
        tenancy_id=oci_identity_tenancy["test_tenancy"]["id"],
        time_redeemed_greater_than_or_equal_to=var["subscription_redemption_time_redeemed_greater_than_or_equal_to"],
        time_redeemed_less_than=var["subscription_redemption_time_redeemed_less_than"])
    ```


    :param str subscription_id: The subscription ID for which rewards information is requested for.
    :param str tenancy_id: The OCID of the tenancy.
    :param str time_redeemed_greater_than_or_equal_to: The starting redeemed date filter for the redemption history.
    :param str time_redeemed_less_than: The ending redeemed date filter for the redemption history.
    """
    ...
