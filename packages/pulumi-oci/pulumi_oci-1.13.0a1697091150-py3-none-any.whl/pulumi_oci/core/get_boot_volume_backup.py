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
    'GetBootVolumeBackupResult',
    'AwaitableGetBootVolumeBackupResult',
    'get_boot_volume_backup',
    'get_boot_volume_backup_output',
]

@pulumi.output_type
class GetBootVolumeBackupResult:
    """
    A collection of values returned by getBootVolumeBackup.
    """
    def __init__(__self__, boot_volume_backup_id=None, boot_volume_id=None, compartment_id=None, defined_tags=None, display_name=None, expiration_time=None, freeform_tags=None, id=None, image_id=None, kms_key_id=None, size_in_gbs=None, source_boot_volume_backup_id=None, source_details=None, source_type=None, state=None, system_tags=None, time_created=None, time_request_received=None, type=None, unique_size_in_gbs=None):
        if boot_volume_backup_id and not isinstance(boot_volume_backup_id, str):
            raise TypeError("Expected argument 'boot_volume_backup_id' to be a str")
        pulumi.set(__self__, "boot_volume_backup_id", boot_volume_backup_id)
        if boot_volume_id and not isinstance(boot_volume_id, str):
            raise TypeError("Expected argument 'boot_volume_id' to be a str")
        pulumi.set(__self__, "boot_volume_id", boot_volume_id)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if expiration_time and not isinstance(expiration_time, str):
            raise TypeError("Expected argument 'expiration_time' to be a str")
        pulumi.set(__self__, "expiration_time", expiration_time)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_id and not isinstance(image_id, str):
            raise TypeError("Expected argument 'image_id' to be a str")
        pulumi.set(__self__, "image_id", image_id)
        if kms_key_id and not isinstance(kms_key_id, str):
            raise TypeError("Expected argument 'kms_key_id' to be a str")
        pulumi.set(__self__, "kms_key_id", kms_key_id)
        if size_in_gbs and not isinstance(size_in_gbs, str):
            raise TypeError("Expected argument 'size_in_gbs' to be a str")
        pulumi.set(__self__, "size_in_gbs", size_in_gbs)
        if source_boot_volume_backup_id and not isinstance(source_boot_volume_backup_id, str):
            raise TypeError("Expected argument 'source_boot_volume_backup_id' to be a str")
        pulumi.set(__self__, "source_boot_volume_backup_id", source_boot_volume_backup_id)
        if source_details and not isinstance(source_details, list):
            raise TypeError("Expected argument 'source_details' to be a list")
        pulumi.set(__self__, "source_details", source_details)
        if source_type and not isinstance(source_type, str):
            raise TypeError("Expected argument 'source_type' to be a str")
        pulumi.set(__self__, "source_type", source_type)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_request_received and not isinstance(time_request_received, str):
            raise TypeError("Expected argument 'time_request_received' to be a str")
        pulumi.set(__self__, "time_request_received", time_request_received)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if unique_size_in_gbs and not isinstance(unique_size_in_gbs, str):
            raise TypeError("Expected argument 'unique_size_in_gbs' to be a str")
        pulumi.set(__self__, "unique_size_in_gbs", unique_size_in_gbs)

    @property
    @pulumi.getter(name="bootVolumeBackupId")
    def boot_volume_backup_id(self) -> str:
        return pulumi.get(self, "boot_volume_backup_id")

    @property
    @pulumi.getter(name="bootVolumeId")
    def boot_volume_id(self) -> str:
        """
        The OCID of the boot volume.
        """
        return pulumi.get(self, "boot_volume_id")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment that contains the boot volume backup.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> str:
        """
        The date and time the volume backup will expire and be automatically deleted. Format defined by [RFC3339](https://tools.ietf.org/html/rfc3339). This parameter will always be present for backups that were created automatically by a scheduled-backup policy. For manually created backups, it will be absent, signifying that there is no expiration time and the backup will last forever until manually deleted.
        """
        return pulumi.get(self, "expiration_time")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The OCID of the boot volume backup.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> str:
        """
        The image OCID used to create the boot volume the backup is taken from.
        """
        return pulumi.get(self, "image_id")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> str:
        """
        The OCID of the Vault service master encryption assigned to the boot volume backup. For more information about the Vault service and encryption keys, see [Overview of Vault service](https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm) and [Using Keys](https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Tasks/usingkeys.htm).
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="sizeInGbs")
    def size_in_gbs(self) -> str:
        """
        The size of the boot volume, in GBs.
        """
        return pulumi.get(self, "size_in_gbs")

    @property
    @pulumi.getter(name="sourceBootVolumeBackupId")
    def source_boot_volume_backup_id(self) -> str:
        """
        The OCID of the source boot volume backup.
        """
        return pulumi.get(self, "source_boot_volume_backup_id")

    @property
    @pulumi.getter(name="sourceDetails")
    def source_details(self) -> Sequence['outputs.GetBootVolumeBackupSourceDetailResult']:
        return pulumi.get(self, "source_details")

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> str:
        """
        Specifies whether the backup was created manually, or via scheduled backup policy.
        """
        return pulumi.get(self, "source_type")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of a boot volume backup.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the boot volume backup was created. This is the time the actual point-in-time image of the volume data was taken. Format defined by [RFC3339](https://tools.ietf.org/html/rfc3339).
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeRequestReceived")
    def time_request_received(self) -> str:
        """
        The date and time the request to create the boot volume backup was received. Format defined by [RFC3339](https://tools.ietf.org/html/rfc3339).
        """
        return pulumi.get(self, "time_request_received")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of a volume backup. Supported values are 'FULL' or 'INCREMENTAL'.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uniqueSizeInGbs")
    def unique_size_in_gbs(self) -> str:
        """
        The size used by the backup, in GBs. It is typically smaller than sizeInGBs, depending on the space consumed on the boot volume and whether the backup is full or incremental.
        """
        return pulumi.get(self, "unique_size_in_gbs")


class AwaitableGetBootVolumeBackupResult(GetBootVolumeBackupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBootVolumeBackupResult(
            boot_volume_backup_id=self.boot_volume_backup_id,
            boot_volume_id=self.boot_volume_id,
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            display_name=self.display_name,
            expiration_time=self.expiration_time,
            freeform_tags=self.freeform_tags,
            id=self.id,
            image_id=self.image_id,
            kms_key_id=self.kms_key_id,
            size_in_gbs=self.size_in_gbs,
            source_boot_volume_backup_id=self.source_boot_volume_backup_id,
            source_details=self.source_details,
            source_type=self.source_type,
            state=self.state,
            system_tags=self.system_tags,
            time_created=self.time_created,
            time_request_received=self.time_request_received,
            type=self.type,
            unique_size_in_gbs=self.unique_size_in_gbs)


def get_boot_volume_backup(boot_volume_backup_id: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBootVolumeBackupResult:
    """
    This data source provides details about a specific Boot Volume Backup resource in Oracle Cloud Infrastructure Core service.

    Gets information for the specified boot volume backup.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_boot_volume_backup = oci.Core.get_boot_volume_backup(boot_volume_backup_id=oci_core_boot_volume_backup["test_boot_volume_backup"]["id"])
    ```


    :param str boot_volume_backup_id: The OCID of the boot volume backup.
    """
    __args__ = dict()
    __args__['bootVolumeBackupId'] = boot_volume_backup_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Core/getBootVolumeBackup:getBootVolumeBackup', __args__, opts=opts, typ=GetBootVolumeBackupResult).value

    return AwaitableGetBootVolumeBackupResult(
        boot_volume_backup_id=pulumi.get(__ret__, 'boot_volume_backup_id'),
        boot_volume_id=pulumi.get(__ret__, 'boot_volume_id'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        display_name=pulumi.get(__ret__, 'display_name'),
        expiration_time=pulumi.get(__ret__, 'expiration_time'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        image_id=pulumi.get(__ret__, 'image_id'),
        kms_key_id=pulumi.get(__ret__, 'kms_key_id'),
        size_in_gbs=pulumi.get(__ret__, 'size_in_gbs'),
        source_boot_volume_backup_id=pulumi.get(__ret__, 'source_boot_volume_backup_id'),
        source_details=pulumi.get(__ret__, 'source_details'),
        source_type=pulumi.get(__ret__, 'source_type'),
        state=pulumi.get(__ret__, 'state'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_request_received=pulumi.get(__ret__, 'time_request_received'),
        type=pulumi.get(__ret__, 'type'),
        unique_size_in_gbs=pulumi.get(__ret__, 'unique_size_in_gbs'))


@_utilities.lift_output_func(get_boot_volume_backup)
def get_boot_volume_backup_output(boot_volume_backup_id: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBootVolumeBackupResult]:
    """
    This data source provides details about a specific Boot Volume Backup resource in Oracle Cloud Infrastructure Core service.

    Gets information for the specified boot volume backup.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_boot_volume_backup = oci.Core.get_boot_volume_backup(boot_volume_backup_id=oci_core_boot_volume_backup["test_boot_volume_backup"]["id"])
    ```


    :param str boot_volume_backup_id: The OCID of the boot volume backup.
    """
    ...
