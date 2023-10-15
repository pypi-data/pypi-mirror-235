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
    'GetMigrationPlanAvailableShapesResult',
    'AwaitableGetMigrationPlanAvailableShapesResult',
    'get_migration_plan_available_shapes',
    'get_migration_plan_available_shapes_output',
]

@pulumi.output_type
class GetMigrationPlanAvailableShapesResult:
    """
    A collection of values returned by getMigrationPlanAvailableShapes.
    """
    def __init__(__self__, availability_domain=None, available_shapes_collections=None, compartment_id=None, dvh_host_id=None, filters=None, id=None, migration_plan_id=None, reserved_capacity_id=None):
        if availability_domain and not isinstance(availability_domain, str):
            raise TypeError("Expected argument 'availability_domain' to be a str")
        pulumi.set(__self__, "availability_domain", availability_domain)
        if available_shapes_collections and not isinstance(available_shapes_collections, list):
            raise TypeError("Expected argument 'available_shapes_collections' to be a list")
        pulumi.set(__self__, "available_shapes_collections", available_shapes_collections)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if dvh_host_id and not isinstance(dvh_host_id, str):
            raise TypeError("Expected argument 'dvh_host_id' to be a str")
        pulumi.set(__self__, "dvh_host_id", dvh_host_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if migration_plan_id and not isinstance(migration_plan_id, str):
            raise TypeError("Expected argument 'migration_plan_id' to be a str")
        pulumi.set(__self__, "migration_plan_id", migration_plan_id)
        if reserved_capacity_id and not isinstance(reserved_capacity_id, str):
            raise TypeError("Expected argument 'reserved_capacity_id' to be a str")
        pulumi.set(__self__, "reserved_capacity_id", reserved_capacity_id)

    @property
    @pulumi.getter(name="availabilityDomain")
    def availability_domain(self) -> Optional[str]:
        """
        Availability domain of the shape.
        """
        return pulumi.get(self, "availability_domain")

    @property
    @pulumi.getter(name="availableShapesCollections")
    def available_shapes_collections(self) -> Sequence['outputs.GetMigrationPlanAvailableShapesAvailableShapesCollectionResult']:
        """
        The list of available_shapes_collection.
        """
        return pulumi.get(self, "available_shapes_collections")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="dvhHostId")
    def dvh_host_id(self) -> Optional[str]:
        return pulumi.get(self, "dvh_host_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetMigrationPlanAvailableShapesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="migrationPlanId")
    def migration_plan_id(self) -> str:
        return pulumi.get(self, "migration_plan_id")

    @property
    @pulumi.getter(name="reservedCapacityId")
    def reserved_capacity_id(self) -> Optional[str]:
        return pulumi.get(self, "reserved_capacity_id")


class AwaitableGetMigrationPlanAvailableShapesResult(GetMigrationPlanAvailableShapesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMigrationPlanAvailableShapesResult(
            availability_domain=self.availability_domain,
            available_shapes_collections=self.available_shapes_collections,
            compartment_id=self.compartment_id,
            dvh_host_id=self.dvh_host_id,
            filters=self.filters,
            id=self.id,
            migration_plan_id=self.migration_plan_id,
            reserved_capacity_id=self.reserved_capacity_id)


def get_migration_plan_available_shapes(availability_domain: Optional[str] = None,
                                        compartment_id: Optional[str] = None,
                                        dvh_host_id: Optional[str] = None,
                                        filters: Optional[Sequence[pulumi.InputType['GetMigrationPlanAvailableShapesFilterArgs']]] = None,
                                        migration_plan_id: Optional[str] = None,
                                        reserved_capacity_id: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMigrationPlanAvailableShapesResult:
    """
    This data source provides the list of Migration Plan Available Shapes in Oracle Cloud Infrastructure Cloud Migrations service.

    List of shapes by parameters.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_migration_plan_available_shapes = oci.CloudMigrations.get_migration_plan_available_shapes(migration_plan_id=oci_cloud_migrations_migration_plan["test_migration_plan"]["id"],
        availability_domain=var["migration_plan_available_shape_availability_domain"],
        compartment_id=var["compartment_id"],
        dvh_host_id=oci_cloud_migrations_dvh_host["test_dvh_host"]["id"],
        reserved_capacity_id=oci_cloud_migrations_reserved_capacity["test_reserved_capacity"]["id"])
    ```


    :param str availability_domain: The availability domain in which to list resources.
    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str dvh_host_id: The ID of the Dvh in which to list resources.
    :param str migration_plan_id: Unique migration plan identifier
    :param str reserved_capacity_id: The reserved capacity ID for which to list resources.
    """
    __args__ = dict()
    __args__['availabilityDomain'] = availability_domain
    __args__['compartmentId'] = compartment_id
    __args__['dvhHostId'] = dvh_host_id
    __args__['filters'] = filters
    __args__['migrationPlanId'] = migration_plan_id
    __args__['reservedCapacityId'] = reserved_capacity_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:CloudMigrations/getMigrationPlanAvailableShapes:getMigrationPlanAvailableShapes', __args__, opts=opts, typ=GetMigrationPlanAvailableShapesResult).value

    return AwaitableGetMigrationPlanAvailableShapesResult(
        availability_domain=pulumi.get(__ret__, 'availability_domain'),
        available_shapes_collections=pulumi.get(__ret__, 'available_shapes_collections'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        dvh_host_id=pulumi.get(__ret__, 'dvh_host_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        migration_plan_id=pulumi.get(__ret__, 'migration_plan_id'),
        reserved_capacity_id=pulumi.get(__ret__, 'reserved_capacity_id'))


@_utilities.lift_output_func(get_migration_plan_available_shapes)
def get_migration_plan_available_shapes_output(availability_domain: Optional[pulumi.Input[Optional[str]]] = None,
                                               compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                                               dvh_host_id: Optional[pulumi.Input[Optional[str]]] = None,
                                               filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetMigrationPlanAvailableShapesFilterArgs']]]]] = None,
                                               migration_plan_id: Optional[pulumi.Input[str]] = None,
                                               reserved_capacity_id: Optional[pulumi.Input[Optional[str]]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMigrationPlanAvailableShapesResult]:
    """
    This data source provides the list of Migration Plan Available Shapes in Oracle Cloud Infrastructure Cloud Migrations service.

    List of shapes by parameters.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_migration_plan_available_shapes = oci.CloudMigrations.get_migration_plan_available_shapes(migration_plan_id=oci_cloud_migrations_migration_plan["test_migration_plan"]["id"],
        availability_domain=var["migration_plan_available_shape_availability_domain"],
        compartment_id=var["compartment_id"],
        dvh_host_id=oci_cloud_migrations_dvh_host["test_dvh_host"]["id"],
        reserved_capacity_id=oci_cloud_migrations_reserved_capacity["test_reserved_capacity"]["id"])
    ```


    :param str availability_domain: The availability domain in which to list resources.
    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str dvh_host_id: The ID of the Dvh in which to list resources.
    :param str migration_plan_id: Unique migration plan identifier
    :param str reserved_capacity_id: The reserved capacity ID for which to list resources.
    """
    ...
