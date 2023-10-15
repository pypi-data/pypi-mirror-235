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
    'GetNamespacesResult',
    'AwaitableGetNamespacesResult',
    'get_namespaces',
    'get_namespaces_output',
]

@pulumi.output_type
class GetNamespacesResult:
    """
    A collection of values returned by getNamespaces.
    """
    def __init__(__self__, compartment_id=None, filters=None, id=None, namespace_collections=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if namespace_collections and not isinstance(namespace_collections, list):
            raise TypeError("Expected argument 'namespace_collections' to be a list")
        pulumi.set(__self__, "namespace_collections", namespace_collections)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The is the tenancy ID
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetNamespacesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="namespaceCollections")
    def namespace_collections(self) -> Sequence['outputs.GetNamespacesNamespaceCollectionResult']:
        """
        The list of namespace_collection.
        """
        return pulumi.get(self, "namespace_collections")


class AwaitableGetNamespacesResult(GetNamespacesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNamespacesResult(
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            namespace_collections=self.namespace_collections)


def get_namespaces(compartment_id: Optional[str] = None,
                   filters: Optional[Sequence[pulumi.InputType['GetNamespacesFilterArgs']]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNamespacesResult:
    """
    This data source provides the list of Namespaces in Oracle Cloud Infrastructure Log Analytics service.

    Given a tenancy OCID, this API returns the namespace of the tenancy if it is valid and subscribed to the region.  The
    result also indicates if the tenancy is onboarded with Logging Analytics.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_namespaces = oci.LogAnalytics.get_namespaces(compartment_id=var["compartment_id"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:LogAnalytics/getNamespaces:getNamespaces', __args__, opts=opts, typ=GetNamespacesResult).value

    return AwaitableGetNamespacesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        namespace_collections=pulumi.get(__ret__, 'namespace_collections'))


@_utilities.lift_output_func(get_namespaces)
def get_namespaces_output(compartment_id: Optional[pulumi.Input[str]] = None,
                          filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetNamespacesFilterArgs']]]]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNamespacesResult]:
    """
    This data source provides the list of Namespaces in Oracle Cloud Infrastructure Log Analytics service.

    Given a tenancy OCID, this API returns the namespace of the tenancy if it is valid and subscribed to the region.  The
    result also indicates if the tenancy is onboarded with Logging Analytics.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_namespaces = oci.LogAnalytics.get_namespaces(compartment_id=var["compartment_id"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    """
    ...
