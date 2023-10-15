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
    'GetManagementAgentInstallKeyResult',
    'AwaitableGetManagementAgentInstallKeyResult',
    'get_management_agent_install_key',
    'get_management_agent_install_key_output',
]

@pulumi.output_type
class GetManagementAgentInstallKeyResult:
    """
    A collection of values returned by getManagementAgentInstallKey.
    """
    def __init__(__self__, allowed_key_install_count=None, compartment_id=None, created_by_principal_id=None, current_key_install_count=None, display_name=None, id=None, is_unlimited=None, key=None, lifecycle_details=None, management_agent_install_key_id=None, state=None, time_created=None, time_expires=None, time_updated=None):
        if allowed_key_install_count and not isinstance(allowed_key_install_count, int):
            raise TypeError("Expected argument 'allowed_key_install_count' to be a int")
        pulumi.set(__self__, "allowed_key_install_count", allowed_key_install_count)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if created_by_principal_id and not isinstance(created_by_principal_id, str):
            raise TypeError("Expected argument 'created_by_principal_id' to be a str")
        pulumi.set(__self__, "created_by_principal_id", created_by_principal_id)
        if current_key_install_count and not isinstance(current_key_install_count, int):
            raise TypeError("Expected argument 'current_key_install_count' to be a int")
        pulumi.set(__self__, "current_key_install_count", current_key_install_count)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_unlimited and not isinstance(is_unlimited, bool):
            raise TypeError("Expected argument 'is_unlimited' to be a bool")
        pulumi.set(__self__, "is_unlimited", is_unlimited)
        if key and not isinstance(key, str):
            raise TypeError("Expected argument 'key' to be a str")
        pulumi.set(__self__, "key", key)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if management_agent_install_key_id and not isinstance(management_agent_install_key_id, str):
            raise TypeError("Expected argument 'management_agent_install_key_id' to be a str")
        pulumi.set(__self__, "management_agent_install_key_id", management_agent_install_key_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_expires and not isinstance(time_expires, str):
            raise TypeError("Expected argument 'time_expires' to be a str")
        pulumi.set(__self__, "time_expires", time_expires)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)

    @property
    @pulumi.getter(name="allowedKeyInstallCount")
    def allowed_key_install_count(self) -> int:
        """
        Total number of install for this keys
        """
        return pulumi.get(self, "allowed_key_install_count")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        Compartment Identifier
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="createdByPrincipalId")
    def created_by_principal_id(self) -> str:
        """
        Principal id of user who created the Agent Install key
        """
        return pulumi.get(self, "created_by_principal_id")

    @property
    @pulumi.getter(name="currentKeyInstallCount")
    def current_key_install_count(self) -> int:
        """
        Total number of install for this keys
        """
        return pulumi.get(self, "current_key_install_count")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Management Agent Install Key Name
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Agent install Key identifier
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isUnlimited")
    def is_unlimited(self) -> bool:
        """
        If set to true, the install key has no expiration date or usage limit. Properties allowedKeyInstallCount and timeExpires are ignored if set to true. Defaults to false.
        """
        return pulumi.get(self, "is_unlimited")

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Management Agent Install Key
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="managementAgentInstallKeyId")
    def management_agent_install_key_id(self) -> str:
        return pulumi.get(self, "management_agent_install_key_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        Status of Key
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The time when Management Agent install Key was created. An RFC3339 formatted date time string
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeExpires")
    def time_expires(self) -> str:
        """
        date after which key would expire after creation
        """
        return pulumi.get(self, "time_expires")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The time when Management Agent install Key was updated. An RFC3339 formatted date time string
        """
        return pulumi.get(self, "time_updated")


class AwaitableGetManagementAgentInstallKeyResult(GetManagementAgentInstallKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagementAgentInstallKeyResult(
            allowed_key_install_count=self.allowed_key_install_count,
            compartment_id=self.compartment_id,
            created_by_principal_id=self.created_by_principal_id,
            current_key_install_count=self.current_key_install_count,
            display_name=self.display_name,
            id=self.id,
            is_unlimited=self.is_unlimited,
            key=self.key,
            lifecycle_details=self.lifecycle_details,
            management_agent_install_key_id=self.management_agent_install_key_id,
            state=self.state,
            time_created=self.time_created,
            time_expires=self.time_expires,
            time_updated=self.time_updated)


def get_management_agent_install_key(management_agent_install_key_id: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagementAgentInstallKeyResult:
    """
    This data source provides details about a specific Management Agent Install Key resource in Oracle Cloud Infrastructure Management Agent service.

    Gets complete details of the Agent install Key for a given key id

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_management_agent_install_key = oci.ManagementAgent.get_management_agent_install_key(management_agent_install_key_id=oci_management_agent_management_agent_install_key["test_management_agent_install_key"]["id"])
    ```


    :param str management_agent_install_key_id: Unique Management Agent Install Key identifier
    """
    __args__ = dict()
    __args__['managementAgentInstallKeyId'] = management_agent_install_key_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:ManagementAgent/getManagementAgentInstallKey:getManagementAgentInstallKey', __args__, opts=opts, typ=GetManagementAgentInstallKeyResult).value

    return AwaitableGetManagementAgentInstallKeyResult(
        allowed_key_install_count=pulumi.get(__ret__, 'allowed_key_install_count'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        created_by_principal_id=pulumi.get(__ret__, 'created_by_principal_id'),
        current_key_install_count=pulumi.get(__ret__, 'current_key_install_count'),
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        is_unlimited=pulumi.get(__ret__, 'is_unlimited'),
        key=pulumi.get(__ret__, 'key'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        management_agent_install_key_id=pulumi.get(__ret__, 'management_agent_install_key_id'),
        state=pulumi.get(__ret__, 'state'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_expires=pulumi.get(__ret__, 'time_expires'),
        time_updated=pulumi.get(__ret__, 'time_updated'))


@_utilities.lift_output_func(get_management_agent_install_key)
def get_management_agent_install_key_output(management_agent_install_key_id: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagementAgentInstallKeyResult]:
    """
    This data source provides details about a specific Management Agent Install Key resource in Oracle Cloud Infrastructure Management Agent service.

    Gets complete details of the Agent install Key for a given key id

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_management_agent_install_key = oci.ManagementAgent.get_management_agent_install_key(management_agent_install_key_id=oci_management_agent_management_agent_install_key["test_management_agent_install_key"]["id"])
    ```


    :param str management_agent_install_key_id: Unique Management Agent Install Key identifier
    """
    ...
