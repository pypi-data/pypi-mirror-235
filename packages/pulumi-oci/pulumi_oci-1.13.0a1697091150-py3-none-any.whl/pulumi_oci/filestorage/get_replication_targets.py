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
    'GetReplicationTargetsResult',
    'AwaitableGetReplicationTargetsResult',
    'get_replication_targets',
    'get_replication_targets_output',
]

@pulumi.output_type
class GetReplicationTargetsResult:
    """
    A collection of values returned by getReplicationTargets.
    """
    def __init__(__self__, availability_domain=None, compartment_id=None, display_name=None, filters=None, id=None, replication_targets=None, state=None):
        if availability_domain and not isinstance(availability_domain, str):
            raise TypeError("Expected argument 'availability_domain' to be a str")
        pulumi.set(__self__, "availability_domain", availability_domain)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if replication_targets and not isinstance(replication_targets, list):
            raise TypeError("Expected argument 'replication_targets' to be a list")
        pulumi.set(__self__, "replication_targets", replication_targets)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="availabilityDomain")
    def availability_domain(self) -> str:
        """
        The availability domain the replication target is in. Must be in the same availability domain as the target file system. Example: `Uocm:PHX-AD-1`
        """
        return pulumi.get(self, "availability_domain")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the replication.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A user-friendly name. This name is same as the replication display name for the associated resource. Example: `My Replication`
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetReplicationTargetsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the replication target.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="replicationTargets")
    def replication_targets(self) -> Sequence['outputs.GetReplicationTargetsReplicationTargetResult']:
        """
        The list of replication_targets.
        """
        return pulumi.get(self, "replication_targets")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of this replication.
        """
        return pulumi.get(self, "state")


class AwaitableGetReplicationTargetsResult(GetReplicationTargetsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReplicationTargetsResult(
            availability_domain=self.availability_domain,
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            replication_targets=self.replication_targets,
            state=self.state)


def get_replication_targets(availability_domain: Optional[str] = None,
                            compartment_id: Optional[str] = None,
                            display_name: Optional[str] = None,
                            filters: Optional[Sequence[pulumi.InputType['GetReplicationTargetsFilterArgs']]] = None,
                            id: Optional[str] = None,
                            state: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReplicationTargetsResult:
    """
    This data source provides the list of Replication Targets in Oracle Cloud Infrastructure File Storage service.

    Lists the replication target resources in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_replication_targets = oci.FileStorage.get_replication_targets(availability_domain=var["replication_target_availability_domain"],
        compartment_id=var["compartment_id"],
        display_name=var["replication_target_display_name"],
        id=var["replication_target_id"],
        state=var["replication_target_state"])
    ```


    :param str availability_domain: The name of the availability domain.  Example: `Uocm:PHX-AD-1`
    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A user-friendly name. It does not have to be unique, and it is changeable.  Example: `My resource`
    :param str id: Filter results by [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resouce type.
    :param str state: Filter results by the specified lifecycle state. Must be a valid state for the resource type.
    """
    __args__ = dict()
    __args__['availabilityDomain'] = availability_domain
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:FileStorage/getReplicationTargets:getReplicationTargets', __args__, opts=opts, typ=GetReplicationTargetsResult).value

    return AwaitableGetReplicationTargetsResult(
        availability_domain=pulumi.get(__ret__, 'availability_domain'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        replication_targets=pulumi.get(__ret__, 'replication_targets'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_replication_targets)
def get_replication_targets_output(availability_domain: Optional[pulumi.Input[str]] = None,
                                   compartment_id: Optional[pulumi.Input[str]] = None,
                                   display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                   filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetReplicationTargetsFilterArgs']]]]] = None,
                                   id: Optional[pulumi.Input[Optional[str]]] = None,
                                   state: Optional[pulumi.Input[Optional[str]]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReplicationTargetsResult]:
    """
    This data source provides the list of Replication Targets in Oracle Cloud Infrastructure File Storage service.

    Lists the replication target resources in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_replication_targets = oci.FileStorage.get_replication_targets(availability_domain=var["replication_target_availability_domain"],
        compartment_id=var["compartment_id"],
        display_name=var["replication_target_display_name"],
        id=var["replication_target_id"],
        state=var["replication_target_state"])
    ```


    :param str availability_domain: The name of the availability domain.  Example: `Uocm:PHX-AD-1`
    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A user-friendly name. It does not have to be unique, and it is changeable.  Example: `My resource`
    :param str id: Filter results by [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resouce type.
    :param str state: Filter results by the specified lifecycle state. Must be a valid state for the resource type.
    """
    ...
