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
    'GetRecommendationStrategyResult',
    'AwaitableGetRecommendationStrategyResult',
    'get_recommendation_strategy',
    'get_recommendation_strategy_output',
]

@pulumi.output_type
class GetRecommendationStrategyResult:
    """
    A collection of values returned by getRecommendationStrategy.
    """
    def __init__(__self__, compartment_id=None, compartment_id_in_subtree=None, id=None, items=None, name=None, recommendation_name=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if compartment_id_in_subtree and not isinstance(compartment_id_in_subtree, bool):
            raise TypeError("Expected argument 'compartment_id_in_subtree' to be a bool")
        pulumi.set(__self__, "compartment_id_in_subtree", compartment_id_in_subtree)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if items and not isinstance(items, list):
            raise TypeError("Expected argument 'items' to be a list")
        pulumi.set(__self__, "items", items)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if recommendation_name and not isinstance(recommendation_name, str):
            raise TypeError("Expected argument 'recommendation_name' to be a str")
        pulumi.set(__self__, "recommendation_name", recommendation_name)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="compartmentIdInSubtree")
    def compartment_id_in_subtree(self) -> bool:
        return pulumi.get(self, "compartment_id_in_subtree")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.GetRecommendationStrategyItemResult']:
        """
        A collection of recommendation strategy summaries.
        """
        return pulumi.get(self, "items")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the strategy parameter.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="recommendationName")
    def recommendation_name(self) -> Optional[str]:
        return pulumi.get(self, "recommendation_name")


class AwaitableGetRecommendationStrategyResult(GetRecommendationStrategyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRecommendationStrategyResult(
            compartment_id=self.compartment_id,
            compartment_id_in_subtree=self.compartment_id_in_subtree,
            id=self.id,
            items=self.items,
            name=self.name,
            recommendation_name=self.recommendation_name)


def get_recommendation_strategy(compartment_id: Optional[str] = None,
                                compartment_id_in_subtree: Optional[bool] = None,
                                name: Optional[str] = None,
                                recommendation_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRecommendationStrategyResult:
    """
    This data source provides details about a specific Recommendation Strategy resource in Oracle Cloud Infrastructure Optimizer service.

    Lists the existing strategies.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_recommendation_strategy = oci.Optimizer.get_recommendation_strategy(compartment_id=var["compartment_id"],
        compartment_id_in_subtree=var["recommendation_strategy_compartment_id_in_subtree"],
        name=var["recommendation_strategy_name"],
        recommendation_name=oci_optimizer_recommendation["test_recommendation"]["name"])
    ```


    :param str compartment_id: The OCID of the compartment.
    :param bool compartment_id_in_subtree: When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.
           
           Can only be set to true when performing ListCompartments on the tenancy (root compartment).
    :param str name: Optional. A filter that returns results that match the name specified.
    :param str recommendation_name: Optional. A filter that returns results that match the recommendation name specified.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['compartmentIdInSubtree'] = compartment_id_in_subtree
    __args__['name'] = name
    __args__['recommendationName'] = recommendation_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Optimizer/getRecommendationStrategy:getRecommendationStrategy', __args__, opts=opts, typ=GetRecommendationStrategyResult).value

    return AwaitableGetRecommendationStrategyResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        compartment_id_in_subtree=pulumi.get(__ret__, 'compartment_id_in_subtree'),
        id=pulumi.get(__ret__, 'id'),
        items=pulumi.get(__ret__, 'items'),
        name=pulumi.get(__ret__, 'name'),
        recommendation_name=pulumi.get(__ret__, 'recommendation_name'))


@_utilities.lift_output_func(get_recommendation_strategy)
def get_recommendation_strategy_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                       compartment_id_in_subtree: Optional[pulumi.Input[bool]] = None,
                                       name: Optional[pulumi.Input[Optional[str]]] = None,
                                       recommendation_name: Optional[pulumi.Input[Optional[str]]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRecommendationStrategyResult]:
    """
    This data source provides details about a specific Recommendation Strategy resource in Oracle Cloud Infrastructure Optimizer service.

    Lists the existing strategies.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_recommendation_strategy = oci.Optimizer.get_recommendation_strategy(compartment_id=var["compartment_id"],
        compartment_id_in_subtree=var["recommendation_strategy_compartment_id_in_subtree"],
        name=var["recommendation_strategy_name"],
        recommendation_name=oci_optimizer_recommendation["test_recommendation"]["name"])
    ```


    :param str compartment_id: The OCID of the compartment.
    :param bool compartment_id_in_subtree: When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.
           
           Can only be set to true when performing ListCompartments on the tenancy (root compartment).
    :param str name: Optional. A filter that returns results that match the name specified.
    :param str recommendation_name: Optional. A filter that returns results that match the recommendation name specified.
    """
    ...
