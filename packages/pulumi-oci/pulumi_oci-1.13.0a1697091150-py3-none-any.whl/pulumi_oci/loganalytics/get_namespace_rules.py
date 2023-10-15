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
    'GetNamespaceRulesResult',
    'AwaitableGetNamespaceRulesResult',
    'get_namespace_rules',
    'get_namespace_rules_output',
]

@pulumi.output_type
class GetNamespaceRulesResult:
    """
    A collection of values returned by getNamespaceRules.
    """
    def __init__(__self__, compartment_id=None, display_name=None, filters=None, id=None, kind=None, namespace=None, rule_summary_collections=None, state=None):
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
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if rule_summary_collections and not isinstance(rule_summary_collections, list):
            raise TypeError("Expected argument 'rule_summary_collections' to be a list")
        pulumi.set(__self__, "rule_summary_collections", rule_summary_collections)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        Compartment Identifier [OCID] (https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The ingest time rule or scheduled task display name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetNamespaceRulesFilterResult']]:
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
    def kind(self) -> Optional[str]:
        """
        The kind of rule - either an ingest time rule or a scheduled task.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="ruleSummaryCollections")
    def rule_summary_collections(self) -> Sequence['outputs.GetNamespaceRulesRuleSummaryCollectionResult']:
        """
        The list of rule_summary_collection.
        """
        return pulumi.get(self, "rule_summary_collections")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the logging analytics rule.
        """
        return pulumi.get(self, "state")


class AwaitableGetNamespaceRulesResult(GetNamespaceRulesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNamespaceRulesResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            kind=self.kind,
            namespace=self.namespace,
            rule_summary_collections=self.rule_summary_collections,
            state=self.state)


def get_namespace_rules(compartment_id: Optional[str] = None,
                        display_name: Optional[str] = None,
                        filters: Optional[Sequence[pulumi.InputType['GetNamespaceRulesFilterArgs']]] = None,
                        kind: Optional[str] = None,
                        namespace: Optional[str] = None,
                        state: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNamespaceRulesResult:
    """
    This data source provides the list of Namespace Rules in Oracle Cloud Infrastructure Log Analytics service.

    Returns a list of ingest time rules and scheduled tasks in a compartment. You may limit the number of items returned, provide sorting options, and filter the results.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_namespace_rules = oci.LogAnalytics.get_namespace_rules(compartment_id=var["compartment_id"],
        namespace=var["namespace_rule_namespace"],
        display_name=var["namespace_rule_display_name"],
        kind=var["namespace_rule_kind"],
        state=var["namespace_rule_state"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return rules whose displayName matches in whole or in part the specified value. The match is case-insensitive.
    :param str kind: The rule kind used for filtering. Only rules of the specified kind will be returned.
    :param str namespace: The Logging Analytics namespace used for the request.
    :param str state: The rule lifecycle state used for filtering. Currently supported values are ACTIVE and DELETED.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['kind'] = kind
    __args__['namespace'] = namespace
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:LogAnalytics/getNamespaceRules:getNamespaceRules', __args__, opts=opts, typ=GetNamespaceRulesResult).value

    return AwaitableGetNamespaceRulesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        namespace=pulumi.get(__ret__, 'namespace'),
        rule_summary_collections=pulumi.get(__ret__, 'rule_summary_collections'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_namespace_rules)
def get_namespace_rules_output(compartment_id: Optional[pulumi.Input[str]] = None,
                               display_name: Optional[pulumi.Input[Optional[str]]] = None,
                               filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetNamespaceRulesFilterArgs']]]]] = None,
                               kind: Optional[pulumi.Input[Optional[str]]] = None,
                               namespace: Optional[pulumi.Input[str]] = None,
                               state: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNamespaceRulesResult]:
    """
    This data source provides the list of Namespace Rules in Oracle Cloud Infrastructure Log Analytics service.

    Returns a list of ingest time rules and scheduled tasks in a compartment. You may limit the number of items returned, provide sorting options, and filter the results.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_namespace_rules = oci.LogAnalytics.get_namespace_rules(compartment_id=var["compartment_id"],
        namespace=var["namespace_rule_namespace"],
        display_name=var["namespace_rule_display_name"],
        kind=var["namespace_rule_kind"],
        state=var["namespace_rule_state"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return rules whose displayName matches in whole or in part the specified value. The match is case-insensitive.
    :param str kind: The rule kind used for filtering. Only rules of the specified kind will be returned.
    :param str namespace: The Logging Analytics namespace used for the request.
    :param str state: The rule lifecycle state used for filtering. Currently supported values are ACTIVE and DELETED.
    """
    ...
