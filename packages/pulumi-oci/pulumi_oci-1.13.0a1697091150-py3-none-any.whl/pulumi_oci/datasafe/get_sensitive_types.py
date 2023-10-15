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
    'GetSensitiveTypesResult',
    'AwaitableGetSensitiveTypesResult',
    'get_sensitive_types',
    'get_sensitive_types_output',
]

@pulumi.output_type
class GetSensitiveTypesResult:
    """
    A collection of values returned by getSensitiveTypes.
    """
    def __init__(__self__, access_level=None, compartment_id=None, compartment_id_in_subtree=None, default_masking_format_id=None, display_name=None, entity_type=None, filters=None, id=None, parent_category_id=None, sensitive_type_collections=None, sensitive_type_id=None, sensitive_type_source=None, state=None, time_created_greater_than_or_equal_to=None, time_created_less_than=None):
        if access_level and not isinstance(access_level, str):
            raise TypeError("Expected argument 'access_level' to be a str")
        pulumi.set(__self__, "access_level", access_level)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if compartment_id_in_subtree and not isinstance(compartment_id_in_subtree, bool):
            raise TypeError("Expected argument 'compartment_id_in_subtree' to be a bool")
        pulumi.set(__self__, "compartment_id_in_subtree", compartment_id_in_subtree)
        if default_masking_format_id and not isinstance(default_masking_format_id, str):
            raise TypeError("Expected argument 'default_masking_format_id' to be a str")
        pulumi.set(__self__, "default_masking_format_id", default_masking_format_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if entity_type and not isinstance(entity_type, str):
            raise TypeError("Expected argument 'entity_type' to be a str")
        pulumi.set(__self__, "entity_type", entity_type)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if parent_category_id and not isinstance(parent_category_id, str):
            raise TypeError("Expected argument 'parent_category_id' to be a str")
        pulumi.set(__self__, "parent_category_id", parent_category_id)
        if sensitive_type_collections and not isinstance(sensitive_type_collections, list):
            raise TypeError("Expected argument 'sensitive_type_collections' to be a list")
        pulumi.set(__self__, "sensitive_type_collections", sensitive_type_collections)
        if sensitive_type_id and not isinstance(sensitive_type_id, str):
            raise TypeError("Expected argument 'sensitive_type_id' to be a str")
        pulumi.set(__self__, "sensitive_type_id", sensitive_type_id)
        if sensitive_type_source and not isinstance(sensitive_type_source, str):
            raise TypeError("Expected argument 'sensitive_type_source' to be a str")
        pulumi.set(__self__, "sensitive_type_source", sensitive_type_source)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if time_created_greater_than_or_equal_to and not isinstance(time_created_greater_than_or_equal_to, str):
            raise TypeError("Expected argument 'time_created_greater_than_or_equal_to' to be a str")
        pulumi.set(__self__, "time_created_greater_than_or_equal_to", time_created_greater_than_or_equal_to)
        if time_created_less_than and not isinstance(time_created_less_than, str):
            raise TypeError("Expected argument 'time_created_less_than' to be a str")
        pulumi.set(__self__, "time_created_less_than", time_created_less_than)

    @property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[str]:
        return pulumi.get(self, "access_level")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment that contains the sensitive type.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="compartmentIdInSubtree")
    def compartment_id_in_subtree(self) -> Optional[bool]:
        return pulumi.get(self, "compartment_id_in_subtree")

    @property
    @pulumi.getter(name="defaultMaskingFormatId")
    def default_masking_format_id(self) -> Optional[str]:
        """
        The OCID of the library masking format that should be used to mask the sensitive columns associated with the sensitive type.
        """
        return pulumi.get(self, "default_masking_format_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The display name of the sensitive type.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> Optional[str]:
        """
        The entity type. It can be either a sensitive type with regular expressions or a sensitive category used for grouping similar sensitive types.
        """
        return pulumi.get(self, "entity_type")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetSensitiveTypesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="parentCategoryId")
    def parent_category_id(self) -> Optional[str]:
        """
        The OCID of the parent sensitive category.
        """
        return pulumi.get(self, "parent_category_id")

    @property
    @pulumi.getter(name="sensitiveTypeCollections")
    def sensitive_type_collections(self) -> Sequence['outputs.GetSensitiveTypesSensitiveTypeCollectionResult']:
        """
        The list of sensitive_type_collection.
        """
        return pulumi.get(self, "sensitive_type_collections")

    @property
    @pulumi.getter(name="sensitiveTypeId")
    def sensitive_type_id(self) -> Optional[str]:
        return pulumi.get(self, "sensitive_type_id")

    @property
    @pulumi.getter(name="sensitiveTypeSource")
    def sensitive_type_source(self) -> Optional[str]:
        return pulumi.get(self, "sensitive_type_source")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the sensitive type.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreatedGreaterThanOrEqualTo")
    def time_created_greater_than_or_equal_to(self) -> Optional[str]:
        return pulumi.get(self, "time_created_greater_than_or_equal_to")

    @property
    @pulumi.getter(name="timeCreatedLessThan")
    def time_created_less_than(self) -> Optional[str]:
        return pulumi.get(self, "time_created_less_than")


class AwaitableGetSensitiveTypesResult(GetSensitiveTypesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSensitiveTypesResult(
            access_level=self.access_level,
            compartment_id=self.compartment_id,
            compartment_id_in_subtree=self.compartment_id_in_subtree,
            default_masking_format_id=self.default_masking_format_id,
            display_name=self.display_name,
            entity_type=self.entity_type,
            filters=self.filters,
            id=self.id,
            parent_category_id=self.parent_category_id,
            sensitive_type_collections=self.sensitive_type_collections,
            sensitive_type_id=self.sensitive_type_id,
            sensitive_type_source=self.sensitive_type_source,
            state=self.state,
            time_created_greater_than_or_equal_to=self.time_created_greater_than_or_equal_to,
            time_created_less_than=self.time_created_less_than)


def get_sensitive_types(access_level: Optional[str] = None,
                        compartment_id: Optional[str] = None,
                        compartment_id_in_subtree: Optional[bool] = None,
                        default_masking_format_id: Optional[str] = None,
                        display_name: Optional[str] = None,
                        entity_type: Optional[str] = None,
                        filters: Optional[Sequence[pulumi.InputType['GetSensitiveTypesFilterArgs']]] = None,
                        parent_category_id: Optional[str] = None,
                        sensitive_type_id: Optional[str] = None,
                        sensitive_type_source: Optional[str] = None,
                        state: Optional[str] = None,
                        time_created_greater_than_or_equal_to: Optional[str] = None,
                        time_created_less_than: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSensitiveTypesResult:
    """
    This data source provides the list of Sensitive Types in Oracle Cloud Infrastructure Data Safe service.

    Gets a list of sensitive types based on the specified query parameters.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_sensitive_types = oci.DataSafe.get_sensitive_types(compartment_id=var["compartment_id"],
        access_level=var["sensitive_type_access_level"],
        compartment_id_in_subtree=var["sensitive_type_compartment_id_in_subtree"],
        default_masking_format_id=oci_data_safe_default_masking_format["test_default_masking_format"]["id"],
        display_name=var["sensitive_type_display_name"],
        entity_type=var["sensitive_type_entity_type"],
        parent_category_id=oci_marketplace_category["test_category"]["id"],
        sensitive_type_id=oci_data_safe_sensitive_type["test_sensitive_type"]["id"],
        sensitive_type_source=var["sensitive_type_sensitive_type_source"],
        state=var["sensitive_type_state"],
        time_created_greater_than_or_equal_to=var["sensitive_type_time_created_greater_than_or_equal_to"],
        time_created_less_than=var["sensitive_type_time_created_less_than"])
    ```


    :param str access_level: Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.
    :param str compartment_id: A filter to return only resources that match the specified compartment OCID.
    :param bool compartment_id_in_subtree: Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.
    :param str default_masking_format_id: A filter to return only the sensitive types that have the default masking format identified by the specified OCID.
    :param str display_name: A filter to return only resources that match the specified display name.
    :param str entity_type: A filter to return the sensitive type resources based on the value of their entityType attribute.
    :param str parent_category_id: A filter to return only the sensitive types that are children of the sensitive category identified by the specified OCID.
    :param str sensitive_type_id: A filter to return only items related to a specific sensitive type OCID.
    :param str sensitive_type_source: A filter to return the sensitive type resources based on the value of their source attribute.
    :param str state: A filter to return only the resources that match the specified lifecycle state.
    :param str time_created_greater_than_or_equal_to: A filter to return only the resources that were created after the specified date and time, as defined by [RFC3339](https://tools.ietf.org/html/rfc3339). Using TimeCreatedGreaterThanOrEqualToQueryParam parameter retrieves all resources created after that date.
           
           **Example:** 2016-12-19T16:39:57.600Z
    :param str time_created_less_than: Search for resources that were created before a specific date. Specifying this parameter corresponding `timeCreatedLessThan` parameter will retrieve all resources created before the specified created date, in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.
           
           **Example:** 2016-12-19T16:39:57.600Z
    """
    __args__ = dict()
    __args__['accessLevel'] = access_level
    __args__['compartmentId'] = compartment_id
    __args__['compartmentIdInSubtree'] = compartment_id_in_subtree
    __args__['defaultMaskingFormatId'] = default_masking_format_id
    __args__['displayName'] = display_name
    __args__['entityType'] = entity_type
    __args__['filters'] = filters
    __args__['parentCategoryId'] = parent_category_id
    __args__['sensitiveTypeId'] = sensitive_type_id
    __args__['sensitiveTypeSource'] = sensitive_type_source
    __args__['state'] = state
    __args__['timeCreatedGreaterThanOrEqualTo'] = time_created_greater_than_or_equal_to
    __args__['timeCreatedLessThan'] = time_created_less_than
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataSafe/getSensitiveTypes:getSensitiveTypes', __args__, opts=opts, typ=GetSensitiveTypesResult).value

    return AwaitableGetSensitiveTypesResult(
        access_level=pulumi.get(__ret__, 'access_level'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        compartment_id_in_subtree=pulumi.get(__ret__, 'compartment_id_in_subtree'),
        default_masking_format_id=pulumi.get(__ret__, 'default_masking_format_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        entity_type=pulumi.get(__ret__, 'entity_type'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        parent_category_id=pulumi.get(__ret__, 'parent_category_id'),
        sensitive_type_collections=pulumi.get(__ret__, 'sensitive_type_collections'),
        sensitive_type_id=pulumi.get(__ret__, 'sensitive_type_id'),
        sensitive_type_source=pulumi.get(__ret__, 'sensitive_type_source'),
        state=pulumi.get(__ret__, 'state'),
        time_created_greater_than_or_equal_to=pulumi.get(__ret__, 'time_created_greater_than_or_equal_to'),
        time_created_less_than=pulumi.get(__ret__, 'time_created_less_than'))


@_utilities.lift_output_func(get_sensitive_types)
def get_sensitive_types_output(access_level: Optional[pulumi.Input[Optional[str]]] = None,
                               compartment_id: Optional[pulumi.Input[str]] = None,
                               compartment_id_in_subtree: Optional[pulumi.Input[Optional[bool]]] = None,
                               default_masking_format_id: Optional[pulumi.Input[Optional[str]]] = None,
                               display_name: Optional[pulumi.Input[Optional[str]]] = None,
                               entity_type: Optional[pulumi.Input[Optional[str]]] = None,
                               filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetSensitiveTypesFilterArgs']]]]] = None,
                               parent_category_id: Optional[pulumi.Input[Optional[str]]] = None,
                               sensitive_type_id: Optional[pulumi.Input[Optional[str]]] = None,
                               sensitive_type_source: Optional[pulumi.Input[Optional[str]]] = None,
                               state: Optional[pulumi.Input[Optional[str]]] = None,
                               time_created_greater_than_or_equal_to: Optional[pulumi.Input[Optional[str]]] = None,
                               time_created_less_than: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSensitiveTypesResult]:
    """
    This data source provides the list of Sensitive Types in Oracle Cloud Infrastructure Data Safe service.

    Gets a list of sensitive types based on the specified query parameters.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_sensitive_types = oci.DataSafe.get_sensitive_types(compartment_id=var["compartment_id"],
        access_level=var["sensitive_type_access_level"],
        compartment_id_in_subtree=var["sensitive_type_compartment_id_in_subtree"],
        default_masking_format_id=oci_data_safe_default_masking_format["test_default_masking_format"]["id"],
        display_name=var["sensitive_type_display_name"],
        entity_type=var["sensitive_type_entity_type"],
        parent_category_id=oci_marketplace_category["test_category"]["id"],
        sensitive_type_id=oci_data_safe_sensitive_type["test_sensitive_type"]["id"],
        sensitive_type_source=var["sensitive_type_sensitive_type_source"],
        state=var["sensitive_type_state"],
        time_created_greater_than_or_equal_to=var["sensitive_type_time_created_greater_than_or_equal_to"],
        time_created_less_than=var["sensitive_type_time_created_less_than"])
    ```


    :param str access_level: Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.
    :param str compartment_id: A filter to return only resources that match the specified compartment OCID.
    :param bool compartment_id_in_subtree: Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.
    :param str default_masking_format_id: A filter to return only the sensitive types that have the default masking format identified by the specified OCID.
    :param str display_name: A filter to return only resources that match the specified display name.
    :param str entity_type: A filter to return the sensitive type resources based on the value of their entityType attribute.
    :param str parent_category_id: A filter to return only the sensitive types that are children of the sensitive category identified by the specified OCID.
    :param str sensitive_type_id: A filter to return only items related to a specific sensitive type OCID.
    :param str sensitive_type_source: A filter to return the sensitive type resources based on the value of their source attribute.
    :param str state: A filter to return only the resources that match the specified lifecycle state.
    :param str time_created_greater_than_or_equal_to: A filter to return only the resources that were created after the specified date and time, as defined by [RFC3339](https://tools.ietf.org/html/rfc3339). Using TimeCreatedGreaterThanOrEqualToQueryParam parameter retrieves all resources created after that date.
           
           **Example:** 2016-12-19T16:39:57.600Z
    :param str time_created_less_than: Search for resources that were created before a specific date. Specifying this parameter corresponding `timeCreatedLessThan` parameter will retrieve all resources created before the specified created date, in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.
           
           **Example:** 2016-12-19T16:39:57.600Z
    """
    ...
