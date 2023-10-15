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
    'GetDbVersionsResult',
    'AwaitableGetDbVersionsResult',
    'get_db_versions',
    'get_db_versions_output',
]

@pulumi.output_type
class GetDbVersionsResult:
    """
    A collection of values returned by getDbVersions.
    """
    def __init__(__self__, compartment_id=None, db_system_id=None, db_system_shape=None, db_versions=None, filters=None, id=None, is_database_software_image_supported=None, is_upgrade_supported=None, storage_management=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if db_system_id and not isinstance(db_system_id, str):
            raise TypeError("Expected argument 'db_system_id' to be a str")
        pulumi.set(__self__, "db_system_id", db_system_id)
        if db_system_shape and not isinstance(db_system_shape, str):
            raise TypeError("Expected argument 'db_system_shape' to be a str")
        pulumi.set(__self__, "db_system_shape", db_system_shape)
        if db_versions and not isinstance(db_versions, list):
            raise TypeError("Expected argument 'db_versions' to be a list")
        pulumi.set(__self__, "db_versions", db_versions)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_database_software_image_supported and not isinstance(is_database_software_image_supported, bool):
            raise TypeError("Expected argument 'is_database_software_image_supported' to be a bool")
        pulumi.set(__self__, "is_database_software_image_supported", is_database_software_image_supported)
        if is_upgrade_supported and not isinstance(is_upgrade_supported, bool):
            raise TypeError("Expected argument 'is_upgrade_supported' to be a bool")
        pulumi.set(__self__, "is_upgrade_supported", is_upgrade_supported)
        if storage_management and not isinstance(storage_management, str):
            raise TypeError("Expected argument 'storage_management' to be a str")
        pulumi.set(__self__, "storage_management", storage_management)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="dbSystemId")
    def db_system_id(self) -> Optional[str]:
        return pulumi.get(self, "db_system_id")

    @property
    @pulumi.getter(name="dbSystemShape")
    def db_system_shape(self) -> Optional[str]:
        return pulumi.get(self, "db_system_shape")

    @property
    @pulumi.getter(name="dbVersions")
    def db_versions(self) -> Sequence['outputs.GetDbVersionsDbVersionResult']:
        """
        The list of db_versions.
        """
        return pulumi.get(self, "db_versions")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetDbVersionsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isDatabaseSoftwareImageSupported")
    def is_database_software_image_supported(self) -> Optional[bool]:
        return pulumi.get(self, "is_database_software_image_supported")

    @property
    @pulumi.getter(name="isUpgradeSupported")
    def is_upgrade_supported(self) -> Optional[bool]:
        """
        True if this version of the Oracle Database software is supported for Upgrade.
        """
        return pulumi.get(self, "is_upgrade_supported")

    @property
    @pulumi.getter(name="storageManagement")
    def storage_management(self) -> Optional[str]:
        return pulumi.get(self, "storage_management")


class AwaitableGetDbVersionsResult(GetDbVersionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDbVersionsResult(
            compartment_id=self.compartment_id,
            db_system_id=self.db_system_id,
            db_system_shape=self.db_system_shape,
            db_versions=self.db_versions,
            filters=self.filters,
            id=self.id,
            is_database_software_image_supported=self.is_database_software_image_supported,
            is_upgrade_supported=self.is_upgrade_supported,
            storage_management=self.storage_management)


def get_db_versions(compartment_id: Optional[str] = None,
                    db_system_id: Optional[str] = None,
                    db_system_shape: Optional[str] = None,
                    filters: Optional[Sequence[pulumi.InputType['GetDbVersionsFilterArgs']]] = None,
                    is_database_software_image_supported: Optional[bool] = None,
                    is_upgrade_supported: Optional[bool] = None,
                    storage_management: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDbVersionsResult:
    """
    This data source provides the list of Db Versions in Oracle Cloud Infrastructure Database service.

    Gets a list of supported Oracle Database versions.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_db_versions = oci.Database.get_db_versions(compartment_id=var["compartment_id"],
        db_system_id=oci_database_db_system["test_db_system"]["id"],
        db_system_shape=var["db_version_db_system_shape"],
        is_database_software_image_supported=var["db_version_is_database_software_image_supported"],
        is_upgrade_supported=var["db_version_is_upgrade_supported"],
        storage_management=var["db_version_storage_management"])
    ```


    :param str compartment_id: The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str db_system_id: The DB system [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). If provided, filters the results to the set of database versions which are supported for the DB system.
    :param str db_system_shape: If provided, filters the results to the set of database versions which are supported for the given shape.
    :param bool is_database_software_image_supported: If true, filters the results to the set of Oracle Database versions that are supported for Oracle Cloud Infrastructure database software images.
    :param bool is_upgrade_supported: If provided, filters the results to the set of database versions which are supported for Upgrade.
    :param str storage_management: The DB system storage management option. Used to list database versions available for that storage manager. Valid values are `ASM` and `LVM`.
           * ASM specifies Oracle Automatic Storage Management
           * LVM specifies logical volume manager, sometimes called logical disk manager.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['dbSystemId'] = db_system_id
    __args__['dbSystemShape'] = db_system_shape
    __args__['filters'] = filters
    __args__['isDatabaseSoftwareImageSupported'] = is_database_software_image_supported
    __args__['isUpgradeSupported'] = is_upgrade_supported
    __args__['storageManagement'] = storage_management
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Database/getDbVersions:getDbVersions', __args__, opts=opts, typ=GetDbVersionsResult).value

    return AwaitableGetDbVersionsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        db_system_id=pulumi.get(__ret__, 'db_system_id'),
        db_system_shape=pulumi.get(__ret__, 'db_system_shape'),
        db_versions=pulumi.get(__ret__, 'db_versions'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        is_database_software_image_supported=pulumi.get(__ret__, 'is_database_software_image_supported'),
        is_upgrade_supported=pulumi.get(__ret__, 'is_upgrade_supported'),
        storage_management=pulumi.get(__ret__, 'storage_management'))


@_utilities.lift_output_func(get_db_versions)
def get_db_versions_output(compartment_id: Optional[pulumi.Input[str]] = None,
                           db_system_id: Optional[pulumi.Input[Optional[str]]] = None,
                           db_system_shape: Optional[pulumi.Input[Optional[str]]] = None,
                           filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDbVersionsFilterArgs']]]]] = None,
                           is_database_software_image_supported: Optional[pulumi.Input[Optional[bool]]] = None,
                           is_upgrade_supported: Optional[pulumi.Input[Optional[bool]]] = None,
                           storage_management: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDbVersionsResult]:
    """
    This data source provides the list of Db Versions in Oracle Cloud Infrastructure Database service.

    Gets a list of supported Oracle Database versions.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_db_versions = oci.Database.get_db_versions(compartment_id=var["compartment_id"],
        db_system_id=oci_database_db_system["test_db_system"]["id"],
        db_system_shape=var["db_version_db_system_shape"],
        is_database_software_image_supported=var["db_version_is_database_software_image_supported"],
        is_upgrade_supported=var["db_version_is_upgrade_supported"],
        storage_management=var["db_version_storage_management"])
    ```


    :param str compartment_id: The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str db_system_id: The DB system [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). If provided, filters the results to the set of database versions which are supported for the DB system.
    :param str db_system_shape: If provided, filters the results to the set of database versions which are supported for the given shape.
    :param bool is_database_software_image_supported: If true, filters the results to the set of Oracle Database versions that are supported for Oracle Cloud Infrastructure database software images.
    :param bool is_upgrade_supported: If provided, filters the results to the set of database versions which are supported for Upgrade.
    :param str storage_management: The DB system storage management option. Used to list database versions available for that storage manager. Valid values are `ASM` and `LVM`.
           * ASM specifies Oracle Automatic Storage Management
           * LVM specifies logical volume manager, sometimes called logical disk manager.
    """
    ...
