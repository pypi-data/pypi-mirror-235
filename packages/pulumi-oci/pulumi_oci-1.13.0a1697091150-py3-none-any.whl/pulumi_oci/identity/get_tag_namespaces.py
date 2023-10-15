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
    'GetTagNamespacesResult',
    'AwaitableGetTagNamespacesResult',
    'get_tag_namespaces',
    'get_tag_namespaces_output',
]

@pulumi.output_type
class GetTagNamespacesResult:
    """
    A collection of values returned by getTagNamespaces.
    """
    def __init__(__self__, compartment_id=None, filters=None, id=None, include_subcompartments=None, state=None, tag_namespaces=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if include_subcompartments and not isinstance(include_subcompartments, bool):
            raise TypeError("Expected argument 'include_subcompartments' to be a bool")
        pulumi.set(__self__, "include_subcompartments", include_subcompartments)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tag_namespaces and not isinstance(tag_namespaces, list):
            raise TypeError("Expected argument 'tag_namespaces' to be a list")
        pulumi.set(__self__, "tag_namespaces", tag_namespaces)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment that contains the tag namespace.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetTagNamespacesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="includeSubcompartments")
    def include_subcompartments(self) -> Optional[bool]:
        return pulumi.get(self, "include_subcompartments")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The tagnamespace's current state. After creating a tagnamespace, make sure its `lifecycleState` is ACTIVE before using it. After retiring a tagnamespace, make sure its `lifecycleState` is INACTIVE before using it.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="tagNamespaces")
    def tag_namespaces(self) -> Sequence['outputs.GetTagNamespacesTagNamespaceResult']:
        """
        The list of tag_namespaces.
        """
        return pulumi.get(self, "tag_namespaces")


class AwaitableGetTagNamespacesResult(GetTagNamespacesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTagNamespacesResult(
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            include_subcompartments=self.include_subcompartments,
            state=self.state,
            tag_namespaces=self.tag_namespaces)


def get_tag_namespaces(compartment_id: Optional[str] = None,
                       filters: Optional[Sequence[pulumi.InputType['GetTagNamespacesFilterArgs']]] = None,
                       include_subcompartments: Optional[bool] = None,
                       state: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTagNamespacesResult:
    """
    This data source provides the list of Tag Namespaces in Oracle Cloud Infrastructure Identity service.

    Lists the tag namespaces in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_tag_namespaces = oci.Identity.get_tag_namespaces(compartment_id=var["compartment_id"],
        include_subcompartments=var["tag_namespace_include_subcompartments"],
        state=var["tag_namespace_state"])
    ```


    :param str compartment_id: The OCID of the compartment (remember that the tenancy is simply the root compartment).
    :param bool include_subcompartments: An optional boolean parameter indicating whether to retrieve all tag namespaces in subcompartments. If this parameter is not specified, only the tag namespaces defined in the specified compartment are retrieved.
    :param str state: A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['includeSubcompartments'] = include_subcompartments
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Identity/getTagNamespaces:getTagNamespaces', __args__, opts=opts, typ=GetTagNamespacesResult).value

    return AwaitableGetTagNamespacesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        include_subcompartments=pulumi.get(__ret__, 'include_subcompartments'),
        state=pulumi.get(__ret__, 'state'),
        tag_namespaces=pulumi.get(__ret__, 'tag_namespaces'))


@_utilities.lift_output_func(get_tag_namespaces)
def get_tag_namespaces_output(compartment_id: Optional[pulumi.Input[str]] = None,
                              filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetTagNamespacesFilterArgs']]]]] = None,
                              include_subcompartments: Optional[pulumi.Input[Optional[bool]]] = None,
                              state: Optional[pulumi.Input[Optional[str]]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTagNamespacesResult]:
    """
    This data source provides the list of Tag Namespaces in Oracle Cloud Infrastructure Identity service.

    Lists the tag namespaces in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_tag_namespaces = oci.Identity.get_tag_namespaces(compartment_id=var["compartment_id"],
        include_subcompartments=var["tag_namespace_include_subcompartments"],
        state=var["tag_namespace_state"])
    ```


    :param str compartment_id: The OCID of the compartment (remember that the tenancy is simply the root compartment).
    :param bool include_subcompartments: An optional boolean parameter indicating whether to retrieve all tag namespaces in subcompartments. If this parameter is not specified, only the tag namespaces defined in the specified compartment are retrieved.
    :param str state: A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.
    """
    ...
