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
    'GetRepositoryMirrorRecordResult',
    'AwaitableGetRepositoryMirrorRecordResult',
    'get_repository_mirror_record',
    'get_repository_mirror_record_output',
]

@pulumi.output_type
class GetRepositoryMirrorRecordResult:
    """
    A collection of values returned by getRepositoryMirrorRecord.
    """
    def __init__(__self__, id=None, mirror_record_type=None, mirror_status=None, repository_id=None, time_ended=None, time_enqueued=None, time_started=None, work_request_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if mirror_record_type and not isinstance(mirror_record_type, str):
            raise TypeError("Expected argument 'mirror_record_type' to be a str")
        pulumi.set(__self__, "mirror_record_type", mirror_record_type)
        if mirror_status and not isinstance(mirror_status, str):
            raise TypeError("Expected argument 'mirror_status' to be a str")
        pulumi.set(__self__, "mirror_status", mirror_status)
        if repository_id and not isinstance(repository_id, str):
            raise TypeError("Expected argument 'repository_id' to be a str")
        pulumi.set(__self__, "repository_id", repository_id)
        if time_ended and not isinstance(time_ended, str):
            raise TypeError("Expected argument 'time_ended' to be a str")
        pulumi.set(__self__, "time_ended", time_ended)
        if time_enqueued and not isinstance(time_enqueued, str):
            raise TypeError("Expected argument 'time_enqueued' to be a str")
        pulumi.set(__self__, "time_enqueued", time_enqueued)
        if time_started and not isinstance(time_started, str):
            raise TypeError("Expected argument 'time_started' to be a str")
        pulumi.set(__self__, "time_started", time_started)
        if work_request_id and not isinstance(work_request_id, str):
            raise TypeError("Expected argument 'work_request_id' to be a str")
        pulumi.set(__self__, "work_request_id", work_request_id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="mirrorRecordType")
    def mirror_record_type(self) -> str:
        return pulumi.get(self, "mirror_record_type")

    @property
    @pulumi.getter(name="mirrorStatus")
    def mirror_status(self) -> str:
        """
        Mirror status of current mirror entry. QUEUED - Mirroring Queued RUNNING - Mirroring is Running PASSED - Mirroring Passed FAILED - Mirroring Failed
        """
        return pulumi.get(self, "mirror_status")

    @property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> str:
        return pulumi.get(self, "repository_id")

    @property
    @pulumi.getter(name="timeEnded")
    def time_ended(self) -> str:
        """
        The time taken to complete a mirror operation. Value is null if not completed.
        """
        return pulumi.get(self, "time_ended")

    @property
    @pulumi.getter(name="timeEnqueued")
    def time_enqueued(self) -> str:
        """
        The time to enqueue a mirror operation.
        """
        return pulumi.get(self, "time_enqueued")

    @property
    @pulumi.getter(name="timeStarted")
    def time_started(self) -> str:
        """
        The time to start a mirror operation.
        """
        return pulumi.get(self, "time_started")

    @property
    @pulumi.getter(name="workRequestId")
    def work_request_id(self) -> str:
        """
        Workrequest ID to track current mirror operation.
        """
        return pulumi.get(self, "work_request_id")


class AwaitableGetRepositoryMirrorRecordResult(GetRepositoryMirrorRecordResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRepositoryMirrorRecordResult(
            id=self.id,
            mirror_record_type=self.mirror_record_type,
            mirror_status=self.mirror_status,
            repository_id=self.repository_id,
            time_ended=self.time_ended,
            time_enqueued=self.time_enqueued,
            time_started=self.time_started,
            work_request_id=self.work_request_id)


def get_repository_mirror_record(mirror_record_type: Optional[str] = None,
                                 repository_id: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRepositoryMirrorRecordResult:
    """
    This data source provides details about a specific Repository Mirror Record resource in Oracle Cloud Infrastructure Devops service.

    Returns either current mirror record or last successful mirror record for a specific mirror repository.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_repository_mirror_record = oci.DevOps.get_repository_mirror_record(mirror_record_type=var["repository_mirror_record_mirror_record_type"],
        repository_id=oci_devops_repository["test_repository"]["id"])
    ```


    :param str mirror_record_type: The field of mirror record type. Only one mirror record type can be provided: current - The current mirror record. lastSuccessful - The last successful mirror record.
    :param str repository_id: Unique repository identifier.
    """
    __args__ = dict()
    __args__['mirrorRecordType'] = mirror_record_type
    __args__['repositoryId'] = repository_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DevOps/getRepositoryMirrorRecord:getRepositoryMirrorRecord', __args__, opts=opts, typ=GetRepositoryMirrorRecordResult).value

    return AwaitableGetRepositoryMirrorRecordResult(
        id=pulumi.get(__ret__, 'id'),
        mirror_record_type=pulumi.get(__ret__, 'mirror_record_type'),
        mirror_status=pulumi.get(__ret__, 'mirror_status'),
        repository_id=pulumi.get(__ret__, 'repository_id'),
        time_ended=pulumi.get(__ret__, 'time_ended'),
        time_enqueued=pulumi.get(__ret__, 'time_enqueued'),
        time_started=pulumi.get(__ret__, 'time_started'),
        work_request_id=pulumi.get(__ret__, 'work_request_id'))


@_utilities.lift_output_func(get_repository_mirror_record)
def get_repository_mirror_record_output(mirror_record_type: Optional[pulumi.Input[str]] = None,
                                        repository_id: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRepositoryMirrorRecordResult]:
    """
    This data source provides details about a specific Repository Mirror Record resource in Oracle Cloud Infrastructure Devops service.

    Returns either current mirror record or last successful mirror record for a specific mirror repository.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_repository_mirror_record = oci.DevOps.get_repository_mirror_record(mirror_record_type=var["repository_mirror_record_mirror_record_type"],
        repository_id=oci_devops_repository["test_repository"]["id"])
    ```


    :param str mirror_record_type: The field of mirror record type. Only one mirror record type can be provided: current - The current mirror record. lastSuccessful - The last successful mirror record.
    :param str repository_id: Unique repository identifier.
    """
    ...
