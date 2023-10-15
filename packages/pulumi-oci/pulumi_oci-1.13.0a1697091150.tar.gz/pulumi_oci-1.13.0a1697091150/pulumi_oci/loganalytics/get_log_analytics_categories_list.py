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
    'GetLogAnalyticsCategoriesListResult',
    'AwaitableGetLogAnalyticsCategoriesListResult',
    'get_log_analytics_categories_list',
    'get_log_analytics_categories_list_output',
]

@pulumi.output_type
class GetLogAnalyticsCategoriesListResult:
    """
    A collection of values returned by getLogAnalyticsCategoriesList.
    """
    def __init__(__self__, category_display_text=None, category_type=None, id=None, items=None, name=None, namespace=None):
        if category_display_text and not isinstance(category_display_text, str):
            raise TypeError("Expected argument 'category_display_text' to be a str")
        pulumi.set(__self__, "category_display_text", category_display_text)
        if category_type and not isinstance(category_type, str):
            raise TypeError("Expected argument 'category_type' to be a str")
        pulumi.set(__self__, "category_type", category_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if items and not isinstance(items, list):
            raise TypeError("Expected argument 'items' to be a list")
        pulumi.set(__self__, "items", items)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter(name="categoryDisplayText")
    def category_display_text(self) -> Optional[str]:
        return pulumi.get(self, "category_display_text")

    @property
    @pulumi.getter(name="categoryType")
    def category_type(self) -> Optional[str]:
        return pulumi.get(self, "category_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.GetLogAnalyticsCategoriesListItemResult']:
        """
        An array of categories.
        """
        return pulumi.get(self, "items")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The unique name that identifies the category.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        return pulumi.get(self, "namespace")


class AwaitableGetLogAnalyticsCategoriesListResult(GetLogAnalyticsCategoriesListResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLogAnalyticsCategoriesListResult(
            category_display_text=self.category_display_text,
            category_type=self.category_type,
            id=self.id,
            items=self.items,
            name=self.name,
            namespace=self.namespace)


def get_log_analytics_categories_list(category_display_text: Optional[str] = None,
                                      category_type: Optional[str] = None,
                                      name: Optional[str] = None,
                                      namespace: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLogAnalyticsCategoriesListResult:
    """
    This data source provides details about Categories in Oracle Cloud Infrastructure Log Analytics service.

    Returns a list of categories, containing detailed information about them. You may limit the number of results, provide sorting order, and filter by information such as category name or description.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_log_analytics_categories_list = oci.LogAnalytics.get_log_analytics_categories_list(namespace=var["log_analytics_categories_list_namespace"],
        category_display_text=var["log_analytics_categories_list_category_display_text"],
        category_type=var["log_analytics_categories_list_category_type"],
        name=var["log_analytics_categories_list_name"])
    ```


    :param str category_display_text: The category display text used for filtering. Only categories matching the specified display name or description will be returned.
    :param str category_type: A comma-separated list of category types used for filtering. Only categories of the specified types will be returned.
    :param str name: A filter to return only log analytics category whose name matches the entire name given. The match is case-insensitive.
    :param str namespace: The Logging Analytics namespace used for the request.
    """
    __args__ = dict()
    __args__['categoryDisplayText'] = category_display_text
    __args__['categoryType'] = category_type
    __args__['name'] = name
    __args__['namespace'] = namespace
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:LogAnalytics/getLogAnalyticsCategoriesList:getLogAnalyticsCategoriesList', __args__, opts=opts, typ=GetLogAnalyticsCategoriesListResult).value

    return AwaitableGetLogAnalyticsCategoriesListResult(
        category_display_text=pulumi.get(__ret__, 'category_display_text'),
        category_type=pulumi.get(__ret__, 'category_type'),
        id=pulumi.get(__ret__, 'id'),
        items=pulumi.get(__ret__, 'items'),
        name=pulumi.get(__ret__, 'name'),
        namespace=pulumi.get(__ret__, 'namespace'))


@_utilities.lift_output_func(get_log_analytics_categories_list)
def get_log_analytics_categories_list_output(category_display_text: Optional[pulumi.Input[Optional[str]]] = None,
                                             category_type: Optional[pulumi.Input[Optional[str]]] = None,
                                             name: Optional[pulumi.Input[Optional[str]]] = None,
                                             namespace: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLogAnalyticsCategoriesListResult]:
    """
    This data source provides details about Categories in Oracle Cloud Infrastructure Log Analytics service.

    Returns a list of categories, containing detailed information about them. You may limit the number of results, provide sorting order, and filter by information such as category name or description.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_log_analytics_categories_list = oci.LogAnalytics.get_log_analytics_categories_list(namespace=var["log_analytics_categories_list_namespace"],
        category_display_text=var["log_analytics_categories_list_category_display_text"],
        category_type=var["log_analytics_categories_list_category_type"],
        name=var["log_analytics_categories_list_name"])
    ```


    :param str category_display_text: The category display text used for filtering. Only categories matching the specified display name or description will be returned.
    :param str category_type: A comma-separated list of category types used for filtering. Only categories of the specified types will be returned.
    :param str name: A filter to return only log analytics category whose name matches the entire name given. The match is case-insensitive.
    :param str namespace: The Logging Analytics namespace used for the request.
    """
    ...
