# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetReplicationPolicyResult',
    'AwaitableGetReplicationPolicyResult',
    'get_replication_policy',
    'get_replication_policy_output',
]

@pulumi.output_type
class GetReplicationPolicyResult:
    """
    A collection of values returned by getReplicationPolicy.
    """
    def __init__(__self__, bucket=None, delete_object_in_destination_bucket=None, destination_bucket_name=None, destination_region_name=None, id=None, name=None, namespace=None, replication_id=None, status=None, status_message=None, time_created=None, time_last_sync=None):
        if bucket and not isinstance(bucket, str):
            raise TypeError("Expected argument 'bucket' to be a str")
        pulumi.set(__self__, "bucket", bucket)
        if delete_object_in_destination_bucket and not isinstance(delete_object_in_destination_bucket, str):
            raise TypeError("Expected argument 'delete_object_in_destination_bucket' to be a str")
        pulumi.set(__self__, "delete_object_in_destination_bucket", delete_object_in_destination_bucket)
        if destination_bucket_name and not isinstance(destination_bucket_name, str):
            raise TypeError("Expected argument 'destination_bucket_name' to be a str")
        pulumi.set(__self__, "destination_bucket_name", destination_bucket_name)
        if destination_region_name and not isinstance(destination_region_name, str):
            raise TypeError("Expected argument 'destination_region_name' to be a str")
        pulumi.set(__self__, "destination_region_name", destination_region_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if replication_id and not isinstance(replication_id, str):
            raise TypeError("Expected argument 'replication_id' to be a str")
        pulumi.set(__self__, "replication_id", replication_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if status_message and not isinstance(status_message, str):
            raise TypeError("Expected argument 'status_message' to be a str")
        pulumi.set(__self__, "status_message", status_message)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_last_sync and not isinstance(time_last_sync, str):
            raise TypeError("Expected argument 'time_last_sync' to be a str")
        pulumi.set(__self__, "time_last_sync", time_last_sync)

    @property
    @pulumi.getter
    def bucket(self) -> str:
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter(name="deleteObjectInDestinationBucket")
    def delete_object_in_destination_bucket(self) -> str:
        warnings.warn("""The 'delete_object_in_destination_bucket' field has been deprecated. It is no longer supported.""", DeprecationWarning)
        pulumi.log.warn("""delete_object_in_destination_bucket is deprecated: The 'delete_object_in_destination_bucket' field has been deprecated. It is no longer supported.""")

        return pulumi.get(self, "delete_object_in_destination_bucket")

    @property
    @pulumi.getter(name="destinationBucketName")
    def destination_bucket_name(self) -> str:
        """
        The bucket to replicate to in the destination region. Replication policy creation does not automatically create a destination bucket. Create the destination bucket before creating the policy.
        """
        return pulumi.get(self, "destination_bucket_name")

    @property
    @pulumi.getter(name="destinationRegionName")
    def destination_region_name(self) -> str:
        """
        The destination region to replicate to, for example "us-ashburn-1".
        """
        return pulumi.get(self, "destination_region_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The id of the replication policy.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the policy.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="replicationId")
    def replication_id(self) -> str:
        return pulumi.get(self, "replication_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The replication status of the policy. If the status is CLIENT_ERROR, once the user fixes the issue described in the status message, the status will become ACTIVE.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> str:
        """
        A human-readable description of the status.
        """
        return pulumi.get(self, "status_message")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date when the replication policy was created as per [RFC 3339](https://tools.ietf.org/html/rfc3339).
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeLastSync")
    def time_last_sync(self) -> str:
        """
        Changes made to the source bucket before this time has been replicated.
        """
        return pulumi.get(self, "time_last_sync")


class AwaitableGetReplicationPolicyResult(GetReplicationPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReplicationPolicyResult(
            bucket=self.bucket,
            delete_object_in_destination_bucket=self.delete_object_in_destination_bucket,
            destination_bucket_name=self.destination_bucket_name,
            destination_region_name=self.destination_region_name,
            id=self.id,
            name=self.name,
            namespace=self.namespace,
            replication_id=self.replication_id,
            status=self.status,
            status_message=self.status_message,
            time_created=self.time_created,
            time_last_sync=self.time_last_sync)


def get_replication_policy(bucket: Optional[str] = None,
                           namespace: Optional[str] = None,
                           replication_id: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReplicationPolicyResult:
    """
    This data source provides details about a specific Replication Policy resource in Oracle Cloud Infrastructure Object Storage service.

    Get the replication policy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_replication_policy = oci.ObjectStorage.get_replication_policy(bucket=var["replication_policy_bucket"],
        namespace=var["replication_policy_namespace"],
        replication_id=oci_objectstorage_replication["test_replication"]["id"])
    ```


    :param str bucket: The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`
    :param str namespace: The Object Storage namespace used for the request.
    :param str replication_id: The ID of the replication policy.
    """
    __args__ = dict()
    __args__['bucket'] = bucket
    __args__['namespace'] = namespace
    __args__['replicationId'] = replication_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:ObjectStorage/getReplicationPolicy:getReplicationPolicy', __args__, opts=opts, typ=GetReplicationPolicyResult).value

    return AwaitableGetReplicationPolicyResult(
        bucket=pulumi.get(__ret__, 'bucket'),
        delete_object_in_destination_bucket=pulumi.get(__ret__, 'delete_object_in_destination_bucket'),
        destination_bucket_name=pulumi.get(__ret__, 'destination_bucket_name'),
        destination_region_name=pulumi.get(__ret__, 'destination_region_name'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        namespace=pulumi.get(__ret__, 'namespace'),
        replication_id=pulumi.get(__ret__, 'replication_id'),
        status=pulumi.get(__ret__, 'status'),
        status_message=pulumi.get(__ret__, 'status_message'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_last_sync=pulumi.get(__ret__, 'time_last_sync'))


@_utilities.lift_output_func(get_replication_policy)
def get_replication_policy_output(bucket: Optional[pulumi.Input[str]] = None,
                                  namespace: Optional[pulumi.Input[str]] = None,
                                  replication_id: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReplicationPolicyResult]:
    """
    This data source provides details about a specific Replication Policy resource in Oracle Cloud Infrastructure Object Storage service.

    Get the replication policy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_replication_policy = oci.ObjectStorage.get_replication_policy(bucket=var["replication_policy_bucket"],
        namespace=var["replication_policy_namespace"],
        replication_id=oci_objectstorage_replication["test_replication"]["id"])
    ```


    :param str bucket: The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`
    :param str namespace: The Object Storage namespace used for the request.
    :param str replication_id: The ID of the replication policy.
    """
    ...
