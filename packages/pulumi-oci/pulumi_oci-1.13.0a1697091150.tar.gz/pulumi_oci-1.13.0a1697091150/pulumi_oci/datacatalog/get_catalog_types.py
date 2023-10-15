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
    'GetCatalogTypesResult',
    'AwaitableGetCatalogTypesResult',
    'get_catalog_types',
    'get_catalog_types_output',
]

@pulumi.output_type
class GetCatalogTypesResult:
    """
    A collection of values returned by getCatalogTypes.
    """
    def __init__(__self__, catalog_id=None, external_type_name=None, fields=None, filters=None, id=None, is_approved=None, is_internal=None, is_tag=None, name=None, state=None, type_category=None, type_collections=None):
        if catalog_id and not isinstance(catalog_id, str):
            raise TypeError("Expected argument 'catalog_id' to be a str")
        pulumi.set(__self__, "catalog_id", catalog_id)
        if external_type_name and not isinstance(external_type_name, str):
            raise TypeError("Expected argument 'external_type_name' to be a str")
        pulumi.set(__self__, "external_type_name", external_type_name)
        if fields and not isinstance(fields, list):
            raise TypeError("Expected argument 'fields' to be a list")
        pulumi.set(__self__, "fields", fields)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_approved and not isinstance(is_approved, str):
            raise TypeError("Expected argument 'is_approved' to be a str")
        pulumi.set(__self__, "is_approved", is_approved)
        if is_internal and not isinstance(is_internal, str):
            raise TypeError("Expected argument 'is_internal' to be a str")
        pulumi.set(__self__, "is_internal", is_internal)
        if is_tag and not isinstance(is_tag, str):
            raise TypeError("Expected argument 'is_tag' to be a str")
        pulumi.set(__self__, "is_tag", is_tag)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if type_category and not isinstance(type_category, str):
            raise TypeError("Expected argument 'type_category' to be a str")
        pulumi.set(__self__, "type_category", type_category)
        if type_collections and not isinstance(type_collections, list):
            raise TypeError("Expected argument 'type_collections' to be a list")
        pulumi.set(__self__, "type_collections", type_collections)

    @property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> str:
        """
        The data catalog's OCID.
        """
        return pulumi.get(self, "catalog_id")

    @property
    @pulumi.getter(name="externalTypeName")
    def external_type_name(self) -> Optional[str]:
        """
        Mapping type equivalence in the external system.
        """
        return pulumi.get(self, "external_type_name")

    @property
    @pulumi.getter
    def fields(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetCatalogTypesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isApproved")
    def is_approved(self) -> Optional[str]:
        """
        Indicates whether the type is approved for use as a classifying object.
        """
        return pulumi.get(self, "is_approved")

    @property
    @pulumi.getter(name="isInternal")
    def is_internal(self) -> Optional[str]:
        """
        Indicates whether the type is internal, making it unavailable for use by metadata elements.
        """
        return pulumi.get(self, "is_internal")

    @property
    @pulumi.getter(name="isTag")
    def is_tag(self) -> Optional[str]:
        """
        Indicates whether the type can be used for tagging metadata elements.
        """
        return pulumi.get(self, "is_tag")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The immutable name of the type.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the type.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="typeCategory")
    def type_category(self) -> Optional[str]:
        """
        Indicates the category this type belongs to. For instance, data assets, connections.
        """
        return pulumi.get(self, "type_category")

    @property
    @pulumi.getter(name="typeCollections")
    def type_collections(self) -> Sequence['outputs.GetCatalogTypesTypeCollectionResult']:
        """
        The list of type_collection.
        """
        return pulumi.get(self, "type_collections")


class AwaitableGetCatalogTypesResult(GetCatalogTypesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCatalogTypesResult(
            catalog_id=self.catalog_id,
            external_type_name=self.external_type_name,
            fields=self.fields,
            filters=self.filters,
            id=self.id,
            is_approved=self.is_approved,
            is_internal=self.is_internal,
            is_tag=self.is_tag,
            name=self.name,
            state=self.state,
            type_category=self.type_category,
            type_collections=self.type_collections)


def get_catalog_types(catalog_id: Optional[str] = None,
                      external_type_name: Optional[str] = None,
                      fields: Optional[Sequence[str]] = None,
                      filters: Optional[Sequence[pulumi.InputType['GetCatalogTypesFilterArgs']]] = None,
                      is_approved: Optional[str] = None,
                      is_internal: Optional[str] = None,
                      is_tag: Optional[str] = None,
                      name: Optional[str] = None,
                      state: Optional[str] = None,
                      type_category: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCatalogTypesResult:
    """
    This data source provides the list of Catalog Types in Oracle Cloud Infrastructure Data Catalog service.

    Returns a list of all types within a data catalog.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_catalog_types = oci.DataCatalog.get_catalog_types(catalog_id=oci_datacatalog_catalog["test_catalog"]["id"],
        external_type_name=var["catalog_type_external_type_name"],
        fields=var["catalog_type_fields"],
        is_approved=var["catalog_type_is_approved"],
        is_internal=var["catalog_type_is_internal"],
        is_tag=var["catalog_type_is_tag"],
        name=var["catalog_type_name"],
        state=var["catalog_type_state"],
        type_category=var["catalog_type_type_category"])
    ```


    :param str catalog_id: Unique catalog identifier.
    :param str external_type_name: Data type as defined in an external system.
    :param Sequence[str] fields: Specifies the fields to return in a type summary response.
    :param str is_approved: Indicates whether the type is approved for use as a classifying object.
    :param str is_internal: Indicates whether the type is internal, making it unavailable for use by metadata elements.
    :param str is_tag: Indicates whether the type can be used for tagging metadata elements.
    :param str name: Immutable resource name.
    :param str state: A filter to return only resources that match the specified lifecycle state. The value is case insensitive.
    :param str type_category: Indicates the category of this type . For example, data assets or connections.
    """
    __args__ = dict()
    __args__['catalogId'] = catalog_id
    __args__['externalTypeName'] = external_type_name
    __args__['fields'] = fields
    __args__['filters'] = filters
    __args__['isApproved'] = is_approved
    __args__['isInternal'] = is_internal
    __args__['isTag'] = is_tag
    __args__['name'] = name
    __args__['state'] = state
    __args__['typeCategory'] = type_category
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataCatalog/getCatalogTypes:getCatalogTypes', __args__, opts=opts, typ=GetCatalogTypesResult).value

    return AwaitableGetCatalogTypesResult(
        catalog_id=pulumi.get(__ret__, 'catalog_id'),
        external_type_name=pulumi.get(__ret__, 'external_type_name'),
        fields=pulumi.get(__ret__, 'fields'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        is_approved=pulumi.get(__ret__, 'is_approved'),
        is_internal=pulumi.get(__ret__, 'is_internal'),
        is_tag=pulumi.get(__ret__, 'is_tag'),
        name=pulumi.get(__ret__, 'name'),
        state=pulumi.get(__ret__, 'state'),
        type_category=pulumi.get(__ret__, 'type_category'),
        type_collections=pulumi.get(__ret__, 'type_collections'))


@_utilities.lift_output_func(get_catalog_types)
def get_catalog_types_output(catalog_id: Optional[pulumi.Input[str]] = None,
                             external_type_name: Optional[pulumi.Input[Optional[str]]] = None,
                             fields: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                             filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetCatalogTypesFilterArgs']]]]] = None,
                             is_approved: Optional[pulumi.Input[Optional[str]]] = None,
                             is_internal: Optional[pulumi.Input[Optional[str]]] = None,
                             is_tag: Optional[pulumi.Input[Optional[str]]] = None,
                             name: Optional[pulumi.Input[Optional[str]]] = None,
                             state: Optional[pulumi.Input[Optional[str]]] = None,
                             type_category: Optional[pulumi.Input[Optional[str]]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCatalogTypesResult]:
    """
    This data source provides the list of Catalog Types in Oracle Cloud Infrastructure Data Catalog service.

    Returns a list of all types within a data catalog.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_catalog_types = oci.DataCatalog.get_catalog_types(catalog_id=oci_datacatalog_catalog["test_catalog"]["id"],
        external_type_name=var["catalog_type_external_type_name"],
        fields=var["catalog_type_fields"],
        is_approved=var["catalog_type_is_approved"],
        is_internal=var["catalog_type_is_internal"],
        is_tag=var["catalog_type_is_tag"],
        name=var["catalog_type_name"],
        state=var["catalog_type_state"],
        type_category=var["catalog_type_type_category"])
    ```


    :param str catalog_id: Unique catalog identifier.
    :param str external_type_name: Data type as defined in an external system.
    :param Sequence[str] fields: Specifies the fields to return in a type summary response.
    :param str is_approved: Indicates whether the type is approved for use as a classifying object.
    :param str is_internal: Indicates whether the type is internal, making it unavailable for use by metadata elements.
    :param str is_tag: Indicates whether the type can be used for tagging metadata elements.
    :param str name: Immutable resource name.
    :param str state: A filter to return only resources that match the specified lifecycle state. The value is case insensitive.
    :param str type_category: Indicates the category of this type . For example, data assets or connections.
    """
    ...
