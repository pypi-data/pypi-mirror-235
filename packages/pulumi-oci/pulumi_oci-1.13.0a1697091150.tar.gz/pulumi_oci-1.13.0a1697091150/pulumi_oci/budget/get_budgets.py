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
    'GetBudgetsResult',
    'AwaitableGetBudgetsResult',
    'get_budgets',
    'get_budgets_output',
]

@pulumi.output_type
class GetBudgetsResult:
    """
    A collection of values returned by getBudgets.
    """
    def __init__(__self__, budgets=None, compartment_id=None, display_name=None, filters=None, id=None, state=None, target_type=None):
        if budgets and not isinstance(budgets, list):
            raise TypeError("Expected argument 'budgets' to be a list")
        pulumi.set(__self__, "budgets", budgets)
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
        if target_type and not isinstance(target_type, str):
            raise TypeError("Expected argument 'target_type' to be a str")
        pulumi.set(__self__, "target_type", target_type)

    @property
    @pulumi.getter
    def budgets(self) -> Sequence['outputs.GetBudgetsBudgetResult']:
        """
        The list of budgets.
        """
        return pulumi.get(self, "budgets")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The display name of the budget. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetBudgetsFilterResult']]:
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
        The current state of the budget.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="targetType")
    def target_type(self) -> Optional[str]:
        """
        The type of target on which the budget is applied.
        """
        return pulumi.get(self, "target_type")


class AwaitableGetBudgetsResult(GetBudgetsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBudgetsResult(
            budgets=self.budgets,
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            state=self.state,
            target_type=self.target_type)


def get_budgets(compartment_id: Optional[str] = None,
                display_name: Optional[str] = None,
                filters: Optional[Sequence[pulumi.InputType['GetBudgetsFilterArgs']]] = None,
                state: Optional[str] = None,
                target_type: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBudgetsResult:
    """
    This data source provides the list of Budgets in Oracle Cloud Infrastructure Budget service.

    Gets a list of budgets in a compartment.

    By default, ListBudgets returns budgets of the 'COMPARTMENT' target type, and the budget records with only one target compartment OCID.

    To list all budgets, set the targetType query parameter to ALL (for example: 'targetType=ALL').

    Clients should ignore new targetTypes, or upgrade to the latest version of the client SDK to handle new targetTypes.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_budgets = oci.Budget.get_budgets(compartment_id=var["tenancy_ocid"],
        display_name=var["budget_display_name"],
        state=var["budget_state"],
        target_type=var["budget_target_type"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A user-friendly name. This does not have to be unique, and it's changeable.  Example: `My new resource`
    :param str state: The current state of the resource to filter by.
    :param str target_type: The type of target to filter by:
           * ALL - List all budgets
           * COMPARTMENT - List all budgets with targetType == "COMPARTMENT"
           * TAG - List all budgets with targetType == "TAG"
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['state'] = state
    __args__['targetType'] = target_type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Budget/getBudgets:getBudgets', __args__, opts=opts, typ=GetBudgetsResult).value

    return AwaitableGetBudgetsResult(
        budgets=pulumi.get(__ret__, 'budgets'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        state=pulumi.get(__ret__, 'state'),
        target_type=pulumi.get(__ret__, 'target_type'))


@_utilities.lift_output_func(get_budgets)
def get_budgets_output(compartment_id: Optional[pulumi.Input[str]] = None,
                       display_name: Optional[pulumi.Input[Optional[str]]] = None,
                       filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetBudgetsFilterArgs']]]]] = None,
                       state: Optional[pulumi.Input[Optional[str]]] = None,
                       target_type: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBudgetsResult]:
    """
    This data source provides the list of Budgets in Oracle Cloud Infrastructure Budget service.

    Gets a list of budgets in a compartment.

    By default, ListBudgets returns budgets of the 'COMPARTMENT' target type, and the budget records with only one target compartment OCID.

    To list all budgets, set the targetType query parameter to ALL (for example: 'targetType=ALL').

    Clients should ignore new targetTypes, or upgrade to the latest version of the client SDK to handle new targetTypes.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_budgets = oci.Budget.get_budgets(compartment_id=var["tenancy_ocid"],
        display_name=var["budget_display_name"],
        state=var["budget_state"],
        target_type=var["budget_target_type"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A user-friendly name. This does not have to be unique, and it's changeable.  Example: `My new resource`
    :param str state: The current state of the resource to filter by.
    :param str target_type: The type of target to filter by:
           * ALL - List all budgets
           * COMPARTMENT - List all budgets with targetType == "COMPARTMENT"
           * TAG - List all budgets with targetType == "TAG"
    """
    ...
