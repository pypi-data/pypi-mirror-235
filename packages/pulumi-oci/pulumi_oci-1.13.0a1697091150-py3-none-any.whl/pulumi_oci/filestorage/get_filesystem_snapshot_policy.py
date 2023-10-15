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
    'GetFilesystemSnapshotPolicyResult',
    'AwaitableGetFilesystemSnapshotPolicyResult',
    'get_filesystem_snapshot_policy',
    'get_filesystem_snapshot_policy_output',
]

@pulumi.output_type
class GetFilesystemSnapshotPolicyResult:
    """
    A collection of values returned by getFilesystemSnapshotPolicy.
    """
    def __init__(__self__, availability_domain=None, compartment_id=None, defined_tags=None, display_name=None, filesystem_snapshot_policy_id=None, freeform_tags=None, id=None, policy_prefix=None, schedules=None, state=None, time_created=None):
        if availability_domain and not isinstance(availability_domain, str):
            raise TypeError("Expected argument 'availability_domain' to be a str")
        pulumi.set(__self__, "availability_domain", availability_domain)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filesystem_snapshot_policy_id and not isinstance(filesystem_snapshot_policy_id, str):
            raise TypeError("Expected argument 'filesystem_snapshot_policy_id' to be a str")
        pulumi.set(__self__, "filesystem_snapshot_policy_id", filesystem_snapshot_policy_id)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if policy_prefix and not isinstance(policy_prefix, str):
            raise TypeError("Expected argument 'policy_prefix' to be a str")
        pulumi.set(__self__, "policy_prefix", policy_prefix)
        if schedules and not isinstance(schedules, list):
            raise TypeError("Expected argument 'schedules' to be a list")
        pulumi.set(__self__, "schedules", schedules)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)

    @property
    @pulumi.getter(name="availabilityDomain")
    def availability_domain(self) -> str:
        """
        The availability domain that the file system snapshot policy is in. May be unset using a blank or NULL value.  Example: `Uocm:PHX-AD-2`
        """
        return pulumi.get(self, "availability_domain")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the file system snapshot policy.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.  Example: `My Filesystem Snapshot Policy`
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="filesystemSnapshotPolicyId")
    def filesystem_snapshot_policy_id(self) -> str:
        return pulumi.get(self, "filesystem_snapshot_policy_id")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the file system snapshot policy.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="policyPrefix")
    def policy_prefix(self) -> str:
        """
        The prefix to apply to all snapshots created by this policy.  Example: `acme`
        """
        return pulumi.get(self, "policy_prefix")

    @property
    @pulumi.getter
    def schedules(self) -> Sequence['outputs.GetFilesystemSnapshotPolicyScheduleResult']:
        """
        The list of associated snapshot schedules. A maximum of 10 schedules can be associated with a policy.
        """
        return pulumi.get(self, "schedules")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of this file system snapshot policy.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the file system snapshot policy was created, expressed in [RFC 3339](https://tools.ietf.org/rfc/rfc3339) timestamp format.  Example: `2016-08-25T21:10:29.600Z`
        """
        return pulumi.get(self, "time_created")


class AwaitableGetFilesystemSnapshotPolicyResult(GetFilesystemSnapshotPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFilesystemSnapshotPolicyResult(
            availability_domain=self.availability_domain,
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            display_name=self.display_name,
            filesystem_snapshot_policy_id=self.filesystem_snapshot_policy_id,
            freeform_tags=self.freeform_tags,
            id=self.id,
            policy_prefix=self.policy_prefix,
            schedules=self.schedules,
            state=self.state,
            time_created=self.time_created)


def get_filesystem_snapshot_policy(filesystem_snapshot_policy_id: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFilesystemSnapshotPolicyResult:
    """
    This data source provides details about a specific Filesystem Snapshot Policy resource in Oracle Cloud Infrastructure File Storage service.

    Gets the specified file system snapshot policy's information.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_filesystem_snapshot_policy = oci.FileStorage.get_filesystem_snapshot_policy(filesystem_snapshot_policy_id=oci_file_storage_filesystem_snapshot_policy["test_filesystem_snapshot_policy"]["id"])
    ```


    :param str filesystem_snapshot_policy_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the file system snapshot policy.
    """
    __args__ = dict()
    __args__['filesystemSnapshotPolicyId'] = filesystem_snapshot_policy_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:FileStorage/getFilesystemSnapshotPolicy:getFilesystemSnapshotPolicy', __args__, opts=opts, typ=GetFilesystemSnapshotPolicyResult).value

    return AwaitableGetFilesystemSnapshotPolicyResult(
        availability_domain=pulumi.get(__ret__, 'availability_domain'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filesystem_snapshot_policy_id=pulumi.get(__ret__, 'filesystem_snapshot_policy_id'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        policy_prefix=pulumi.get(__ret__, 'policy_prefix'),
        schedules=pulumi.get(__ret__, 'schedules'),
        state=pulumi.get(__ret__, 'state'),
        time_created=pulumi.get(__ret__, 'time_created'))


@_utilities.lift_output_func(get_filesystem_snapshot_policy)
def get_filesystem_snapshot_policy_output(filesystem_snapshot_policy_id: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFilesystemSnapshotPolicyResult]:
    """
    This data source provides details about a specific Filesystem Snapshot Policy resource in Oracle Cloud Infrastructure File Storage service.

    Gets the specified file system snapshot policy's information.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_filesystem_snapshot_policy = oci.FileStorage.get_filesystem_snapshot_policy(filesystem_snapshot_policy_id=oci_file_storage_filesystem_snapshot_policy["test_filesystem_snapshot_policy"]["id"])
    ```


    :param str filesystem_snapshot_policy_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the file system snapshot policy.
    """
    ...
