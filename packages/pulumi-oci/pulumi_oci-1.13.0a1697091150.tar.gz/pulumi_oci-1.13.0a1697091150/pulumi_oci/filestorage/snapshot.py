# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SnapshotArgs', 'Snapshot']

@pulumi.input_type
class SnapshotArgs:
    def __init__(__self__, *,
                 file_system_id: pulumi.Input[str],
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 expiration_time: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Snapshot resource.
        :param pulumi.Input[str] file_system_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the file system to take a snapshot of.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] expiration_time: (Updatable) The time when this snapshot will be deleted.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        :param pulumi.Input[str] name: Name of the snapshot. This value is immutable. It must also be unique with respect to all other non-DELETED snapshots on the associated file system.
               
               Avoid entering confidential information.
               
               Example: `Sunday`
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        SnapshotArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            file_system_id=file_system_id,
            defined_tags=defined_tags,
            expiration_time=expiration_time,
            freeform_tags=freeform_tags,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             file_system_id: pulumi.Input[str],
             defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             expiration_time: Optional[pulumi.Input[str]] = None,
             freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("file_system_id", file_system_id)
        if defined_tags is not None:
            _setter("defined_tags", defined_tags)
        if expiration_time is not None:
            _setter("expiration_time", expiration_time)
        if freeform_tags is not None:
            _setter("freeform_tags", freeform_tags)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Input[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the file system to take a snapshot of.
        """
        return pulumi.get(self, "file_system_id")

    @file_system_id.setter
    def file_system_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "file_system_id", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The time when this snapshot will be deleted.
        """
        return pulumi.get(self, "expiration_time")

    @expiration_time.setter
    def expiration_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiration_time", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the snapshot. This value is immutable. It must also be unique with respect to all other non-DELETED snapshots on the associated file system.

        Avoid entering confidential information.

        Example: `Sunday`


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _SnapshotState:
    def __init__(__self__, *,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 expiration_time: Optional[pulumi.Input[str]] = None,
                 file_system_id: Optional[pulumi.Input[str]] = None,
                 filesystem_snapshot_policy_id: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 is_clone_source: Optional[pulumi.Input[bool]] = None,
                 lifecycle_details: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provenance_id: Optional[pulumi.Input[str]] = None,
                 snapshot_time: Optional[pulumi.Input[str]] = None,
                 snapshot_type: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 time_created: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Snapshot resources.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] expiration_time: (Updatable) The time when this snapshot will be deleted.
        :param pulumi.Input[str] file_system_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the file system to take a snapshot of.
        :param pulumi.Input[str] filesystem_snapshot_policy_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the file system snapshot policy that created this snapshot.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        :param pulumi.Input[bool] is_clone_source: Specifies whether the snapshot has been cloned. See [Cloning a File System](https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).
        :param pulumi.Input[str] lifecycle_details: Additional information about the current `lifecycleState`.
        :param pulumi.Input[str] name: Name of the snapshot. This value is immutable. It must also be unique with respect to all other non-DELETED snapshots on the associated file system.
               
               Avoid entering confidential information.
               
               Example: `Sunday`
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] provenance_id: An [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) identifying the parent from which this snapshot was cloned. If this snapshot was not cloned, then the `provenanceId` is the same as the snapshot `id` value. If this snapshot was cloned, then the `provenanceId` value is the parent's `provenanceId`. See [Cloning a File System](https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).
        :param pulumi.Input[str] snapshot_time: The date and time the snapshot was taken, expressed in [RFC 3339](https://tools.ietf.org/rfc/rfc3339) timestamp format. This value might be the same or different from `timeCreated` depending on the following factors:
               * If the snapshot is created in the original file system directory.
               * If the snapshot is cloned from a file system.
               * If the snapshot is replicated from a file system.
        :param pulumi.Input[str] snapshot_type: Specifies the generation type of the snapshot.
        :param pulumi.Input[str] state: The current state of the snapshot.
        :param pulumi.Input[str] time_created: The date and time the snapshot was created, expressed in [RFC 3339](https://tools.ietf.org/rfc/rfc3339) timestamp format.  Example: `2016-08-25T21:10:29.600Z`
        """
        _SnapshotState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            defined_tags=defined_tags,
            expiration_time=expiration_time,
            file_system_id=file_system_id,
            filesystem_snapshot_policy_id=filesystem_snapshot_policy_id,
            freeform_tags=freeform_tags,
            is_clone_source=is_clone_source,
            lifecycle_details=lifecycle_details,
            name=name,
            provenance_id=provenance_id,
            snapshot_time=snapshot_time,
            snapshot_type=snapshot_type,
            state=state,
            time_created=time_created,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             expiration_time: Optional[pulumi.Input[str]] = None,
             file_system_id: Optional[pulumi.Input[str]] = None,
             filesystem_snapshot_policy_id: Optional[pulumi.Input[str]] = None,
             freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             is_clone_source: Optional[pulumi.Input[bool]] = None,
             lifecycle_details: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             provenance_id: Optional[pulumi.Input[str]] = None,
             snapshot_time: Optional[pulumi.Input[str]] = None,
             snapshot_type: Optional[pulumi.Input[str]] = None,
             state: Optional[pulumi.Input[str]] = None,
             time_created: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if defined_tags is not None:
            _setter("defined_tags", defined_tags)
        if expiration_time is not None:
            _setter("expiration_time", expiration_time)
        if file_system_id is not None:
            _setter("file_system_id", file_system_id)
        if filesystem_snapshot_policy_id is not None:
            _setter("filesystem_snapshot_policy_id", filesystem_snapshot_policy_id)
        if freeform_tags is not None:
            _setter("freeform_tags", freeform_tags)
        if is_clone_source is not None:
            _setter("is_clone_source", is_clone_source)
        if lifecycle_details is not None:
            _setter("lifecycle_details", lifecycle_details)
        if name is not None:
            _setter("name", name)
        if provenance_id is not None:
            _setter("provenance_id", provenance_id)
        if snapshot_time is not None:
            _setter("snapshot_time", snapshot_time)
        if snapshot_type is not None:
            _setter("snapshot_type", snapshot_type)
        if state is not None:
            _setter("state", state)
        if time_created is not None:
            _setter("time_created", time_created)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The time when this snapshot will be deleted.
        """
        return pulumi.get(self, "expiration_time")

    @expiration_time.setter
    def expiration_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiration_time", value)

    @property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the file system to take a snapshot of.
        """
        return pulumi.get(self, "file_system_id")

    @file_system_id.setter
    def file_system_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_system_id", value)

    @property
    @pulumi.getter(name="filesystemSnapshotPolicyId")
    def filesystem_snapshot_policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the file system snapshot policy that created this snapshot.
        """
        return pulumi.get(self, "filesystem_snapshot_policy_id")

    @filesystem_snapshot_policy_id.setter
    def filesystem_snapshot_policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filesystem_snapshot_policy_id", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="isCloneSource")
    def is_clone_source(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether the snapshot has been cloned. See [Cloning a File System](https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).
        """
        return pulumi.get(self, "is_clone_source")

    @is_clone_source.setter
    def is_clone_source(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_clone_source", value)

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> Optional[pulumi.Input[str]]:
        """
        Additional information about the current `lifecycleState`.
        """
        return pulumi.get(self, "lifecycle_details")

    @lifecycle_details.setter
    def lifecycle_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_details", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the snapshot. This value is immutable. It must also be unique with respect to all other non-DELETED snapshots on the associated file system.

        Avoid entering confidential information.

        Example: `Sunday`


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="provenanceId")
    def provenance_id(self) -> Optional[pulumi.Input[str]]:
        """
        An [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) identifying the parent from which this snapshot was cloned. If this snapshot was not cloned, then the `provenanceId` is the same as the snapshot `id` value. If this snapshot was cloned, then the `provenanceId` value is the parent's `provenanceId`. See [Cloning a File System](https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).
        """
        return pulumi.get(self, "provenance_id")

    @provenance_id.setter
    def provenance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provenance_id", value)

    @property
    @pulumi.getter(name="snapshotTime")
    def snapshot_time(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time the snapshot was taken, expressed in [RFC 3339](https://tools.ietf.org/rfc/rfc3339) timestamp format. This value might be the same or different from `timeCreated` depending on the following factors:
        * If the snapshot is created in the original file system directory.
        * If the snapshot is cloned from a file system.
        * If the snapshot is replicated from a file system.
        """
        return pulumi.get(self, "snapshot_time")

    @snapshot_time.setter
    def snapshot_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "snapshot_time", value)

    @property
    @pulumi.getter(name="snapshotType")
    def snapshot_type(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the generation type of the snapshot.
        """
        return pulumi.get(self, "snapshot_type")

    @snapshot_type.setter
    def snapshot_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "snapshot_type", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current state of the snapshot.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time the snapshot was created, expressed in [RFC 3339](https://tools.ietf.org/rfc/rfc3339) timestamp format.  Example: `2016-08-25T21:10:29.600Z`
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)


class Snapshot(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 expiration_time: Optional[pulumi.Input[str]] = None,
                 file_system_id: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Snapshot resource in Oracle Cloud Infrastructure File Storage service.

        Creates a new snapshot of the specified file system. You
        can access the snapshot at `.snapshot/<name>`.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_snapshot = oci.file_storage.Snapshot("testSnapshot",
            file_system_id=oci_file_storage_file_system["test_file_system"]["id"],
            defined_tags={
                "Operations.CostCenter": "42",
            },
            expiration_time=var["snapshot_expiration_time"],
            freeform_tags={
                "Department": "Finance",
            })
        ```

        ## Import

        Snapshots can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:FileStorage/snapshot:Snapshot test_snapshot "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] expiration_time: (Updatable) The time when this snapshot will be deleted.
        :param pulumi.Input[str] file_system_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the file system to take a snapshot of.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        :param pulumi.Input[str] name: Name of the snapshot. This value is immutable. It must also be unique with respect to all other non-DELETED snapshots on the associated file system.
               
               Avoid entering confidential information.
               
               Example: `Sunday`
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SnapshotArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Snapshot resource in Oracle Cloud Infrastructure File Storage service.

        Creates a new snapshot of the specified file system. You
        can access the snapshot at `.snapshot/<name>`.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_snapshot = oci.file_storage.Snapshot("testSnapshot",
            file_system_id=oci_file_storage_file_system["test_file_system"]["id"],
            defined_tags={
                "Operations.CostCenter": "42",
            },
            expiration_time=var["snapshot_expiration_time"],
            freeform_tags={
                "Department": "Finance",
            })
        ```

        ## Import

        Snapshots can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:FileStorage/snapshot:Snapshot test_snapshot "id"
        ```

        :param str resource_name: The name of the resource.
        :param SnapshotArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SnapshotArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            SnapshotArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 expiration_time: Optional[pulumi.Input[str]] = None,
                 file_system_id: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SnapshotArgs.__new__(SnapshotArgs)

            __props__.__dict__["defined_tags"] = defined_tags
            __props__.__dict__["expiration_time"] = expiration_time
            if file_system_id is None and not opts.urn:
                raise TypeError("Missing required property 'file_system_id'")
            __props__.__dict__["file_system_id"] = file_system_id
            __props__.__dict__["freeform_tags"] = freeform_tags
            __props__.__dict__["name"] = name
            __props__.__dict__["filesystem_snapshot_policy_id"] = None
            __props__.__dict__["is_clone_source"] = None
            __props__.__dict__["lifecycle_details"] = None
            __props__.__dict__["provenance_id"] = None
            __props__.__dict__["snapshot_time"] = None
            __props__.__dict__["snapshot_type"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["time_created"] = None
        super(Snapshot, __self__).__init__(
            'oci:FileStorage/snapshot:Snapshot',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            expiration_time: Optional[pulumi.Input[str]] = None,
            file_system_id: Optional[pulumi.Input[str]] = None,
            filesystem_snapshot_policy_id: Optional[pulumi.Input[str]] = None,
            freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            is_clone_source: Optional[pulumi.Input[bool]] = None,
            lifecycle_details: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            provenance_id: Optional[pulumi.Input[str]] = None,
            snapshot_time: Optional[pulumi.Input[str]] = None,
            snapshot_type: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            time_created: Optional[pulumi.Input[str]] = None) -> 'Snapshot':
        """
        Get an existing Snapshot resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] expiration_time: (Updatable) The time when this snapshot will be deleted.
        :param pulumi.Input[str] file_system_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the file system to take a snapshot of.
        :param pulumi.Input[str] filesystem_snapshot_policy_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the file system snapshot policy that created this snapshot.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        :param pulumi.Input[bool] is_clone_source: Specifies whether the snapshot has been cloned. See [Cloning a File System](https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).
        :param pulumi.Input[str] lifecycle_details: Additional information about the current `lifecycleState`.
        :param pulumi.Input[str] name: Name of the snapshot. This value is immutable. It must also be unique with respect to all other non-DELETED snapshots on the associated file system.
               
               Avoid entering confidential information.
               
               Example: `Sunday`
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] provenance_id: An [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) identifying the parent from which this snapshot was cloned. If this snapshot was not cloned, then the `provenanceId` is the same as the snapshot `id` value. If this snapshot was cloned, then the `provenanceId` value is the parent's `provenanceId`. See [Cloning a File System](https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).
        :param pulumi.Input[str] snapshot_time: The date and time the snapshot was taken, expressed in [RFC 3339](https://tools.ietf.org/rfc/rfc3339) timestamp format. This value might be the same or different from `timeCreated` depending on the following factors:
               * If the snapshot is created in the original file system directory.
               * If the snapshot is cloned from a file system.
               * If the snapshot is replicated from a file system.
        :param pulumi.Input[str] snapshot_type: Specifies the generation type of the snapshot.
        :param pulumi.Input[str] state: The current state of the snapshot.
        :param pulumi.Input[str] time_created: The date and time the snapshot was created, expressed in [RFC 3339](https://tools.ietf.org/rfc/rfc3339) timestamp format.  Example: `2016-08-25T21:10:29.600Z`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SnapshotState.__new__(_SnapshotState)

        __props__.__dict__["defined_tags"] = defined_tags
        __props__.__dict__["expiration_time"] = expiration_time
        __props__.__dict__["file_system_id"] = file_system_id
        __props__.__dict__["filesystem_snapshot_policy_id"] = filesystem_snapshot_policy_id
        __props__.__dict__["freeform_tags"] = freeform_tags
        __props__.__dict__["is_clone_source"] = is_clone_source
        __props__.__dict__["lifecycle_details"] = lifecycle_details
        __props__.__dict__["name"] = name
        __props__.__dict__["provenance_id"] = provenance_id
        __props__.__dict__["snapshot_time"] = snapshot_time
        __props__.__dict__["snapshot_type"] = snapshot_type
        __props__.__dict__["state"] = state
        __props__.__dict__["time_created"] = time_created
        return Snapshot(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> pulumi.Output[str]:
        """
        (Updatable) The time when this snapshot will be deleted.
        """
        return pulumi.get(self, "expiration_time")

    @property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the file system to take a snapshot of.
        """
        return pulumi.get(self, "file_system_id")

    @property
    @pulumi.getter(name="filesystemSnapshotPolicyId")
    def filesystem_snapshot_policy_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the file system snapshot policy that created this snapshot.
        """
        return pulumi.get(self, "filesystem_snapshot_policy_id")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="isCloneSource")
    def is_clone_source(self) -> pulumi.Output[bool]:
        """
        Specifies whether the snapshot has been cloned. See [Cloning a File System](https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).
        """
        return pulumi.get(self, "is_clone_source")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> pulumi.Output[str]:
        """
        Additional information about the current `lifecycleState`.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the snapshot. This value is immutable. It must also be unique with respect to all other non-DELETED snapshots on the associated file system.

        Avoid entering confidential information.

        Example: `Sunday`


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provenanceId")
    def provenance_id(self) -> pulumi.Output[str]:
        """
        An [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) identifying the parent from which this snapshot was cloned. If this snapshot was not cloned, then the `provenanceId` is the same as the snapshot `id` value. If this snapshot was cloned, then the `provenanceId` value is the parent's `provenanceId`. See [Cloning a File System](https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).
        """
        return pulumi.get(self, "provenance_id")

    @property
    @pulumi.getter(name="snapshotTime")
    def snapshot_time(self) -> pulumi.Output[str]:
        """
        The date and time the snapshot was taken, expressed in [RFC 3339](https://tools.ietf.org/rfc/rfc3339) timestamp format. This value might be the same or different from `timeCreated` depending on the following factors:
        * If the snapshot is created in the original file system directory.
        * If the snapshot is cloned from a file system.
        * If the snapshot is replicated from a file system.
        """
        return pulumi.get(self, "snapshot_time")

    @property
    @pulumi.getter(name="snapshotType")
    def snapshot_type(self) -> pulumi.Output[str]:
        """
        Specifies the generation type of the snapshot.
        """
        return pulumi.get(self, "snapshot_type")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of the snapshot.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The date and time the snapshot was created, expressed in [RFC 3339](https://tools.ietf.org/rfc/rfc3339) timestamp format.  Example: `2016-08-25T21:10:29.600Z`
        """
        return pulumi.get(self, "time_created")

