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
    'GetMaskingPoliciesMaskingColumnsResult',
    'AwaitableGetMaskingPoliciesMaskingColumnsResult',
    'get_masking_policies_masking_columns',
    'get_masking_policies_masking_columns_output',
]

@pulumi.output_type
class GetMaskingPoliciesMaskingColumnsResult:
    """
    A collection of values returned by getMaskingPoliciesMaskingColumns.
    """
    def __init__(__self__, column_names=None, data_types=None, filters=None, id=None, is_masking_enabled=None, is_seed_required=None, masking_column_collections=None, masking_column_groups=None, masking_column_lifecycle_state=None, masking_policy_id=None, object_types=None, objects=None, schema_names=None, sensitive_type_id=None, time_created_greater_than_or_equal_to=None, time_created_less_than=None, time_updated_greater_than_or_equal_to=None, time_updated_less_than=None):
        if column_names and not isinstance(column_names, list):
            raise TypeError("Expected argument 'column_names' to be a list")
        pulumi.set(__self__, "column_names", column_names)
        if data_types and not isinstance(data_types, list):
            raise TypeError("Expected argument 'data_types' to be a list")
        pulumi.set(__self__, "data_types", data_types)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_masking_enabled and not isinstance(is_masking_enabled, bool):
            raise TypeError("Expected argument 'is_masking_enabled' to be a bool")
        pulumi.set(__self__, "is_masking_enabled", is_masking_enabled)
        if is_seed_required and not isinstance(is_seed_required, bool):
            raise TypeError("Expected argument 'is_seed_required' to be a bool")
        pulumi.set(__self__, "is_seed_required", is_seed_required)
        if masking_column_collections and not isinstance(masking_column_collections, list):
            raise TypeError("Expected argument 'masking_column_collections' to be a list")
        pulumi.set(__self__, "masking_column_collections", masking_column_collections)
        if masking_column_groups and not isinstance(masking_column_groups, list):
            raise TypeError("Expected argument 'masking_column_groups' to be a list")
        pulumi.set(__self__, "masking_column_groups", masking_column_groups)
        if masking_column_lifecycle_state and not isinstance(masking_column_lifecycle_state, str):
            raise TypeError("Expected argument 'masking_column_lifecycle_state' to be a str")
        pulumi.set(__self__, "masking_column_lifecycle_state", masking_column_lifecycle_state)
        if masking_policy_id and not isinstance(masking_policy_id, str):
            raise TypeError("Expected argument 'masking_policy_id' to be a str")
        pulumi.set(__self__, "masking_policy_id", masking_policy_id)
        if object_types and not isinstance(object_types, list):
            raise TypeError("Expected argument 'object_types' to be a list")
        pulumi.set(__self__, "object_types", object_types)
        if objects and not isinstance(objects, list):
            raise TypeError("Expected argument 'objects' to be a list")
        pulumi.set(__self__, "objects", objects)
        if schema_names and not isinstance(schema_names, list):
            raise TypeError("Expected argument 'schema_names' to be a list")
        pulumi.set(__self__, "schema_names", schema_names)
        if sensitive_type_id and not isinstance(sensitive_type_id, str):
            raise TypeError("Expected argument 'sensitive_type_id' to be a str")
        pulumi.set(__self__, "sensitive_type_id", sensitive_type_id)
        if time_created_greater_than_or_equal_to and not isinstance(time_created_greater_than_or_equal_to, str):
            raise TypeError("Expected argument 'time_created_greater_than_or_equal_to' to be a str")
        pulumi.set(__self__, "time_created_greater_than_or_equal_to", time_created_greater_than_or_equal_to)
        if time_created_less_than and not isinstance(time_created_less_than, str):
            raise TypeError("Expected argument 'time_created_less_than' to be a str")
        pulumi.set(__self__, "time_created_less_than", time_created_less_than)
        if time_updated_greater_than_or_equal_to and not isinstance(time_updated_greater_than_or_equal_to, str):
            raise TypeError("Expected argument 'time_updated_greater_than_or_equal_to' to be a str")
        pulumi.set(__self__, "time_updated_greater_than_or_equal_to", time_updated_greater_than_or_equal_to)
        if time_updated_less_than and not isinstance(time_updated_less_than, str):
            raise TypeError("Expected argument 'time_updated_less_than' to be a str")
        pulumi.set(__self__, "time_updated_less_than", time_updated_less_than)

    @property
    @pulumi.getter(name="columnNames")
    def column_names(self) -> Optional[Sequence[str]]:
        """
        The name of the substitution column.
        """
        return pulumi.get(self, "column_names")

    @property
    @pulumi.getter(name="dataTypes")
    def data_types(self) -> Optional[Sequence[str]]:
        """
        The data type of the masking column.
        """
        return pulumi.get(self, "data_types")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetMaskingPoliciesMaskingColumnsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isMaskingEnabled")
    def is_masking_enabled(self) -> Optional[bool]:
        """
        Indicates if data masking is enabled for the masking column.
        """
        return pulumi.get(self, "is_masking_enabled")

    @property
    @pulumi.getter(name="isSeedRequired")
    def is_seed_required(self) -> Optional[bool]:
        return pulumi.get(self, "is_seed_required")

    @property
    @pulumi.getter(name="maskingColumnCollections")
    def masking_column_collections(self) -> Sequence['outputs.GetMaskingPoliciesMaskingColumnsMaskingColumnCollectionResult']:
        """
        The list of masking_column_collection.
        """
        return pulumi.get(self, "masking_column_collections")

    @property
    @pulumi.getter(name="maskingColumnGroups")
    def masking_column_groups(self) -> Optional[Sequence[str]]:
        """
        The group of the masking column. All the columns in a group are masked together to ensure  that the masked data across these columns continue to retain the same logical relationship.  For more details, check <a href=https://docs.oracle.com/en/cloud/paas/data-safe/udscs/group-masking1.html#GUID-755056B9-9540-48C0-9491-262A44A85037>Group Masking in the Data Safe documentation.</a>
        """
        return pulumi.get(self, "masking_column_groups")

    @property
    @pulumi.getter(name="maskingColumnLifecycleState")
    def masking_column_lifecycle_state(self) -> Optional[str]:
        return pulumi.get(self, "masking_column_lifecycle_state")

    @property
    @pulumi.getter(name="maskingPolicyId")
    def masking_policy_id(self) -> str:
        """
        The OCID of the masking policy that contains the masking column.
        """
        return pulumi.get(self, "masking_policy_id")

    @property
    @pulumi.getter(name="objectTypes")
    def object_types(self) -> Optional[Sequence[str]]:
        """
        The type of the object that contains the database column.
        """
        return pulumi.get(self, "object_types")

    @property
    @pulumi.getter
    def objects(self) -> Optional[Sequence[str]]:
        """
        The name of the object (table or editioning view) that contains the database column.
        """
        return pulumi.get(self, "objects")

    @property
    @pulumi.getter(name="schemaNames")
    def schema_names(self) -> Optional[Sequence[str]]:
        """
        The name of the schema that contains the database column.
        """
        return pulumi.get(self, "schema_names")

    @property
    @pulumi.getter(name="sensitiveTypeId")
    def sensitive_type_id(self) -> Optional[str]:
        """
        The OCID of the sensitive type associated with the masking column.
        """
        return pulumi.get(self, "sensitive_type_id")

    @property
    @pulumi.getter(name="timeCreatedGreaterThanOrEqualTo")
    def time_created_greater_than_or_equal_to(self) -> Optional[str]:
        return pulumi.get(self, "time_created_greater_than_or_equal_to")

    @property
    @pulumi.getter(name="timeCreatedLessThan")
    def time_created_less_than(self) -> Optional[str]:
        return pulumi.get(self, "time_created_less_than")

    @property
    @pulumi.getter(name="timeUpdatedGreaterThanOrEqualTo")
    def time_updated_greater_than_or_equal_to(self) -> Optional[str]:
        return pulumi.get(self, "time_updated_greater_than_or_equal_to")

    @property
    @pulumi.getter(name="timeUpdatedLessThan")
    def time_updated_less_than(self) -> Optional[str]:
        return pulumi.get(self, "time_updated_less_than")


class AwaitableGetMaskingPoliciesMaskingColumnsResult(GetMaskingPoliciesMaskingColumnsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMaskingPoliciesMaskingColumnsResult(
            column_names=self.column_names,
            data_types=self.data_types,
            filters=self.filters,
            id=self.id,
            is_masking_enabled=self.is_masking_enabled,
            is_seed_required=self.is_seed_required,
            masking_column_collections=self.masking_column_collections,
            masking_column_groups=self.masking_column_groups,
            masking_column_lifecycle_state=self.masking_column_lifecycle_state,
            masking_policy_id=self.masking_policy_id,
            object_types=self.object_types,
            objects=self.objects,
            schema_names=self.schema_names,
            sensitive_type_id=self.sensitive_type_id,
            time_created_greater_than_or_equal_to=self.time_created_greater_than_or_equal_to,
            time_created_less_than=self.time_created_less_than,
            time_updated_greater_than_or_equal_to=self.time_updated_greater_than_or_equal_to,
            time_updated_less_than=self.time_updated_less_than)


def get_masking_policies_masking_columns(column_names: Optional[Sequence[str]] = None,
                                         data_types: Optional[Sequence[str]] = None,
                                         filters: Optional[Sequence[pulumi.InputType['GetMaskingPoliciesMaskingColumnsFilterArgs']]] = None,
                                         is_masking_enabled: Optional[bool] = None,
                                         is_seed_required: Optional[bool] = None,
                                         masking_column_groups: Optional[Sequence[str]] = None,
                                         masking_column_lifecycle_state: Optional[str] = None,
                                         masking_policy_id: Optional[str] = None,
                                         object_types: Optional[Sequence[str]] = None,
                                         objects: Optional[Sequence[str]] = None,
                                         schema_names: Optional[Sequence[str]] = None,
                                         sensitive_type_id: Optional[str] = None,
                                         time_created_greater_than_or_equal_to: Optional[str] = None,
                                         time_created_less_than: Optional[str] = None,
                                         time_updated_greater_than_or_equal_to: Optional[str] = None,
                                         time_updated_less_than: Optional[str] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMaskingPoliciesMaskingColumnsResult:
    """
    This data source provides the list of Masking Policies Masking Columns in Oracle Cloud Infrastructure Data Safe service.

    Gets a list of masking columns present in the specified masking policy and based on the specified query parameters.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_masking_policies_masking_columns = oci.DataSafe.get_masking_policies_masking_columns(masking_policy_id=oci_data_safe_masking_policy["test_masking_policy"]["id"],
        column_names=var["masking_policies_masking_column_column_name"],
        data_types=var["masking_policies_masking_column_data_type"],
        is_masking_enabled=var["masking_policies_masking_column_is_masking_enabled"],
        is_seed_required=var["masking_policies_masking_column_is_seed_required"],
        masking_column_groups=var["masking_policies_masking_column_masking_column_group"],
        masking_column_lifecycle_state=var["masking_policies_masking_column_masking_column_lifecycle_state"],
        objects=var["masking_policies_masking_column_object"],
        object_types=var["masking_policies_masking_column_object_type"],
        schema_names=var["masking_policies_masking_column_schema_name"],
        sensitive_type_id=oci_data_safe_sensitive_type["test_sensitive_type"]["id"],
        time_created_greater_than_or_equal_to=var["masking_policies_masking_column_time_created_greater_than_or_equal_to"],
        time_created_less_than=var["masking_policies_masking_column_time_created_less_than"],
        time_updated_greater_than_or_equal_to=var["masking_policies_masking_column_time_updated_greater_than_or_equal_to"],
        time_updated_less_than=var["masking_policies_masking_column_time_updated_less_than"])
    ```


    :param Sequence[str] column_names: A filter to return only a specific column based on column name.
    :param Sequence[str] data_types: A filter to return only resources that match the specified data types.
    :param bool is_masking_enabled: A filter to return the masking column resources based on the value of their isMaskingEnabled attribute. A value of true returns only those columns for which masking is enabled. A value of false returns only those columns for which masking is disabled. Omitting this parameter returns all the masking columns in a masking policy.
    :param bool is_seed_required: A filter to return masking columns based on whether the assigned masking formats need a seed value for masking. A value of true returns those masking columns that are using Deterministic Encryption or Deterministic Substitution masking format.
    :param Sequence[str] masking_column_groups: A filter to return only the resources that match the specified masking column group.
    :param str masking_column_lifecycle_state: A filter to return only the resources that match the specified lifecycle states.
    :param str masking_policy_id: The OCID of the masking policy.
    :param Sequence[str] object_types: A filter to return only items related to a specific object type.
    :param Sequence[str] objects: A filter to return only items related to a specific object name.
    :param Sequence[str] schema_names: A filter to return only items related to specific schema name.
    :param str sensitive_type_id: A filter to return only items related to a specific sensitive type OCID.
    :param str time_created_greater_than_or_equal_to: A filter to return only the resources that were created after the specified date and time, as defined by [RFC3339](https://tools.ietf.org/html/rfc3339). Using TimeCreatedGreaterThanOrEqualToQueryParam parameter retrieves all resources created after that date.
           
           **Example:** 2016-12-19T16:39:57.600Z
    :param str time_created_less_than: Search for resources that were created before a specific date. Specifying this parameter corresponding `timeCreatedLessThan` parameter will retrieve all resources created before the specified created date, in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.
           
           **Example:** 2016-12-19T16:39:57.600Z
    :param str time_updated_greater_than_or_equal_to: Search for resources that were updated after a specific date. Specifying this parameter corresponding `timeUpdatedGreaterThanOrEqualTo` parameter will retrieve all resources updated after the specified created date, in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.
    :param str time_updated_less_than: Search for resources that were updated before a specific date. Specifying this parameter corresponding `timeUpdatedLessThan` parameter will retrieve all resources updated before the specified created date, in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.
    """
    __args__ = dict()
    __args__['columnNames'] = column_names
    __args__['dataTypes'] = data_types
    __args__['filters'] = filters
    __args__['isMaskingEnabled'] = is_masking_enabled
    __args__['isSeedRequired'] = is_seed_required
    __args__['maskingColumnGroups'] = masking_column_groups
    __args__['maskingColumnLifecycleState'] = masking_column_lifecycle_state
    __args__['maskingPolicyId'] = masking_policy_id
    __args__['objectTypes'] = object_types
    __args__['objects'] = objects
    __args__['schemaNames'] = schema_names
    __args__['sensitiveTypeId'] = sensitive_type_id
    __args__['timeCreatedGreaterThanOrEqualTo'] = time_created_greater_than_or_equal_to
    __args__['timeCreatedLessThan'] = time_created_less_than
    __args__['timeUpdatedGreaterThanOrEqualTo'] = time_updated_greater_than_or_equal_to
    __args__['timeUpdatedLessThan'] = time_updated_less_than
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataSafe/getMaskingPoliciesMaskingColumns:getMaskingPoliciesMaskingColumns', __args__, opts=opts, typ=GetMaskingPoliciesMaskingColumnsResult).value

    return AwaitableGetMaskingPoliciesMaskingColumnsResult(
        column_names=pulumi.get(__ret__, 'column_names'),
        data_types=pulumi.get(__ret__, 'data_types'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        is_masking_enabled=pulumi.get(__ret__, 'is_masking_enabled'),
        is_seed_required=pulumi.get(__ret__, 'is_seed_required'),
        masking_column_collections=pulumi.get(__ret__, 'masking_column_collections'),
        masking_column_groups=pulumi.get(__ret__, 'masking_column_groups'),
        masking_column_lifecycle_state=pulumi.get(__ret__, 'masking_column_lifecycle_state'),
        masking_policy_id=pulumi.get(__ret__, 'masking_policy_id'),
        object_types=pulumi.get(__ret__, 'object_types'),
        objects=pulumi.get(__ret__, 'objects'),
        schema_names=pulumi.get(__ret__, 'schema_names'),
        sensitive_type_id=pulumi.get(__ret__, 'sensitive_type_id'),
        time_created_greater_than_or_equal_to=pulumi.get(__ret__, 'time_created_greater_than_or_equal_to'),
        time_created_less_than=pulumi.get(__ret__, 'time_created_less_than'),
        time_updated_greater_than_or_equal_to=pulumi.get(__ret__, 'time_updated_greater_than_or_equal_to'),
        time_updated_less_than=pulumi.get(__ret__, 'time_updated_less_than'))


@_utilities.lift_output_func(get_masking_policies_masking_columns)
def get_masking_policies_masking_columns_output(column_names: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                                data_types: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                                filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetMaskingPoliciesMaskingColumnsFilterArgs']]]]] = None,
                                                is_masking_enabled: Optional[pulumi.Input[Optional[bool]]] = None,
                                                is_seed_required: Optional[pulumi.Input[Optional[bool]]] = None,
                                                masking_column_groups: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                                masking_column_lifecycle_state: Optional[pulumi.Input[Optional[str]]] = None,
                                                masking_policy_id: Optional[pulumi.Input[str]] = None,
                                                object_types: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                                objects: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                                schema_names: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                                sensitive_type_id: Optional[pulumi.Input[Optional[str]]] = None,
                                                time_created_greater_than_or_equal_to: Optional[pulumi.Input[Optional[str]]] = None,
                                                time_created_less_than: Optional[pulumi.Input[Optional[str]]] = None,
                                                time_updated_greater_than_or_equal_to: Optional[pulumi.Input[Optional[str]]] = None,
                                                time_updated_less_than: Optional[pulumi.Input[Optional[str]]] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMaskingPoliciesMaskingColumnsResult]:
    """
    This data source provides the list of Masking Policies Masking Columns in Oracle Cloud Infrastructure Data Safe service.

    Gets a list of masking columns present in the specified masking policy and based on the specified query parameters.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_masking_policies_masking_columns = oci.DataSafe.get_masking_policies_masking_columns(masking_policy_id=oci_data_safe_masking_policy["test_masking_policy"]["id"],
        column_names=var["masking_policies_masking_column_column_name"],
        data_types=var["masking_policies_masking_column_data_type"],
        is_masking_enabled=var["masking_policies_masking_column_is_masking_enabled"],
        is_seed_required=var["masking_policies_masking_column_is_seed_required"],
        masking_column_groups=var["masking_policies_masking_column_masking_column_group"],
        masking_column_lifecycle_state=var["masking_policies_masking_column_masking_column_lifecycle_state"],
        objects=var["masking_policies_masking_column_object"],
        object_types=var["masking_policies_masking_column_object_type"],
        schema_names=var["masking_policies_masking_column_schema_name"],
        sensitive_type_id=oci_data_safe_sensitive_type["test_sensitive_type"]["id"],
        time_created_greater_than_or_equal_to=var["masking_policies_masking_column_time_created_greater_than_or_equal_to"],
        time_created_less_than=var["masking_policies_masking_column_time_created_less_than"],
        time_updated_greater_than_or_equal_to=var["masking_policies_masking_column_time_updated_greater_than_or_equal_to"],
        time_updated_less_than=var["masking_policies_masking_column_time_updated_less_than"])
    ```


    :param Sequence[str] column_names: A filter to return only a specific column based on column name.
    :param Sequence[str] data_types: A filter to return only resources that match the specified data types.
    :param bool is_masking_enabled: A filter to return the masking column resources based on the value of their isMaskingEnabled attribute. A value of true returns only those columns for which masking is enabled. A value of false returns only those columns for which masking is disabled. Omitting this parameter returns all the masking columns in a masking policy.
    :param bool is_seed_required: A filter to return masking columns based on whether the assigned masking formats need a seed value for masking. A value of true returns those masking columns that are using Deterministic Encryption or Deterministic Substitution masking format.
    :param Sequence[str] masking_column_groups: A filter to return only the resources that match the specified masking column group.
    :param str masking_column_lifecycle_state: A filter to return only the resources that match the specified lifecycle states.
    :param str masking_policy_id: The OCID of the masking policy.
    :param Sequence[str] object_types: A filter to return only items related to a specific object type.
    :param Sequence[str] objects: A filter to return only items related to a specific object name.
    :param Sequence[str] schema_names: A filter to return only items related to specific schema name.
    :param str sensitive_type_id: A filter to return only items related to a specific sensitive type OCID.
    :param str time_created_greater_than_or_equal_to: A filter to return only the resources that were created after the specified date and time, as defined by [RFC3339](https://tools.ietf.org/html/rfc3339). Using TimeCreatedGreaterThanOrEqualToQueryParam parameter retrieves all resources created after that date.
           
           **Example:** 2016-12-19T16:39:57.600Z
    :param str time_created_less_than: Search for resources that were created before a specific date. Specifying this parameter corresponding `timeCreatedLessThan` parameter will retrieve all resources created before the specified created date, in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.
           
           **Example:** 2016-12-19T16:39:57.600Z
    :param str time_updated_greater_than_or_equal_to: Search for resources that were updated after a specific date. Specifying this parameter corresponding `timeUpdatedGreaterThanOrEqualTo` parameter will retrieve all resources updated after the specified created date, in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.
    :param str time_updated_less_than: Search for resources that were updated before a specific date. Specifying this parameter corresponding `timeUpdatedLessThan` parameter will retrieve all resources updated before the specified created date, in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.
    """
    ...
