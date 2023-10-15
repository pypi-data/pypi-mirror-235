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
    'GetSubscriptionRewardsResult',
    'AwaitableGetSubscriptionRewardsResult',
    'get_subscription_rewards',
    'get_subscription_rewards_output',
]

@pulumi.output_type
class GetSubscriptionRewardsResult:
    """
    A collection of values returned by getSubscriptionRewards.
    """
    def __init__(__self__, filters=None, id=None, reward_collections=None, subscription_id=None, tenancy_id=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if reward_collections and not isinstance(reward_collections, list):
            raise TypeError("Expected argument 'reward_collections' to be a list")
        pulumi.set(__self__, "reward_collections", reward_collections)
        if subscription_id and not isinstance(subscription_id, str):
            raise TypeError("Expected argument 'subscription_id' to be a str")
        pulumi.set(__self__, "subscription_id", subscription_id)
        if tenancy_id and not isinstance(tenancy_id, str):
            raise TypeError("Expected argument 'tenancy_id' to be a str")
        pulumi.set(__self__, "tenancy_id", tenancy_id)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetSubscriptionRewardsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="rewardCollections")
    def reward_collections(self) -> Sequence['outputs.GetSubscriptionRewardsRewardCollectionResult']:
        """
        The list of reward_collection.
        """
        return pulumi.get(self, "reward_collections")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> str:
        """
        The entitlement ID from MQS, which is the same as the subcription ID.
        """
        return pulumi.get(self, "subscription_id")

    @property
    @pulumi.getter(name="tenancyId")
    def tenancy_id(self) -> str:
        """
        The OCID of the target tenancy.
        """
        return pulumi.get(self, "tenancy_id")


class AwaitableGetSubscriptionRewardsResult(GetSubscriptionRewardsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSubscriptionRewardsResult(
            filters=self.filters,
            id=self.id,
            reward_collections=self.reward_collections,
            subscription_id=self.subscription_id,
            tenancy_id=self.tenancy_id)


def get_subscription_rewards(filters: Optional[Sequence[pulumi.InputType['GetSubscriptionRewardsFilterArgs']]] = None,
                             subscription_id: Optional[str] = None,
                             tenancy_id: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSubscriptionRewardsResult:
    """
    This data source provides the list of Subscription Rewards in Oracle Cloud Infrastructure Usage Proxy service.

    Returns the list of rewards for a subscription ID.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_subscription_rewards = oci.UsageProxy.get_subscription_rewards(subscription_id=oci_ons_subscription["test_subscription"]["id"],
        tenancy_id=oci_identity_tenancy["test_tenancy"]["id"])
    ```


    :param str subscription_id: The subscription ID for which rewards information is requested for.
    :param str tenancy_id: The OCID of the tenancy.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['subscriptionId'] = subscription_id
    __args__['tenancyId'] = tenancy_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:UsageProxy/getSubscriptionRewards:getSubscriptionRewards', __args__, opts=opts, typ=GetSubscriptionRewardsResult).value

    return AwaitableGetSubscriptionRewardsResult(
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        reward_collections=pulumi.get(__ret__, 'reward_collections'),
        subscription_id=pulumi.get(__ret__, 'subscription_id'),
        tenancy_id=pulumi.get(__ret__, 'tenancy_id'))


@_utilities.lift_output_func(get_subscription_rewards)
def get_subscription_rewards_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetSubscriptionRewardsFilterArgs']]]]] = None,
                                    subscription_id: Optional[pulumi.Input[str]] = None,
                                    tenancy_id: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSubscriptionRewardsResult]:
    """
    This data source provides the list of Subscription Rewards in Oracle Cloud Infrastructure Usage Proxy service.

    Returns the list of rewards for a subscription ID.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_subscription_rewards = oci.UsageProxy.get_subscription_rewards(subscription_id=oci_ons_subscription["test_subscription"]["id"],
        tenancy_id=oci_identity_tenancy["test_tenancy"]["id"])
    ```


    :param str subscription_id: The subscription ID for which rewards information is requested for.
    :param str tenancy_id: The OCID of the tenancy.
    """
    ...
