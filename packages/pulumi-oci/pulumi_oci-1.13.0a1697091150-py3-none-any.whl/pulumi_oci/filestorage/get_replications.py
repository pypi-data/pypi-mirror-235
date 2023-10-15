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
    'GetReplicationsResult',
    'AwaitableGetReplicationsResult',
    'get_replications',
    'get_replications_output',
]

@pulumi.output_type
class GetReplicationsResult:
    """
    A collection of values returned by getReplications.
    """
    def __init__(__self__, availability_domain=None, compartment_id=None, display_name=None, file_system_id=None, filters=None, id=None, replications=None, state=None):
        if availability_domain and not isinstance(availability_domain, str):
            raise TypeError("Expected argument 'availability_domain' to be a str")
        pulumi.set(__self__, "availability_domain", availability_domain)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if file_system_id and not isinstance(file_system_id, str):
            raise TypeError("Expected argument 'file_system_id' to be a str")
        pulumi.set(__self__, "file_system_id", file_system_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if replications and not isinstance(replications, list):
            raise TypeError("Expected argument 'replications' to be a list")
        pulumi.set(__self__, "replications", replications)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="availabilityDomain")
    def availability_domain(self) -> str:
        """
        The availability domain the replication is in. The replication must be in the same availability domain as the source file system. Example: `Uocm:PHX-AD-1`
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
        A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.  Example: `My replication`
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> Optional[str]:
        return pulumi.get(self, "file_system_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetReplicationsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the replication.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def replications(self) -> Sequence['outputs.GetReplicationsReplicationResult']:
        """
        The list of replications.
        """
        return pulumi.get(self, "replications")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of this replication. This resource can be in a `FAILED` state if replication target is deleted instead of the replication resource.
        """
        return pulumi.get(self, "state")


class AwaitableGetReplicationsResult(GetReplicationsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReplicationsResult(
            availability_domain=self.availability_domain,
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            file_system_id=self.file_system_id,
            filters=self.filters,
            id=self.id,
            replications=self.replications,
            state=self.state)


def get_replications(availability_domain: Optional[str] = None,
                     compartment_id: Optional[str] = None,
                     display_name: Optional[str] = None,
                     file_system_id: Optional[str] = None,
                     filters: Optional[Sequence[pulumi.InputType['GetReplicationsFilterArgs']]] = None,
                     id: Optional[str] = None,
                     state: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReplicationsResult:
    """
    This data source provides the list of Replications in Oracle Cloud Infrastructure File Storage service.

    Lists the replication resources in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_replications = oci.FileStorage.get_replications(availability_domain=var["replication_availability_domain"],
        compartment_id=var["compartment_id"],
        display_name=var["replication_display_name"],
        file_system_id=oci_file_storage_file_system["test_file_system"]["id"],
        id=var["replication_id"],
        state=var["replication_state"])
    ```


    :param str availability_domain: The name of the availability domain.  Example: `Uocm:PHX-AD-1`
    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A user-friendly name. It does not have to be unique, and it is changeable.  Example: `My resource`
    :param str file_system_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the source file system.
    :param str id: Filter results by [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resouce type.
    :param str state: Filter results by the specified lifecycle state. Must be a valid state for the resource type.
    """
    __args__ = dict()
    __args__['availabilityDomain'] = availability_domain
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['fileSystemId'] = file_system_id
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:FileStorage/getReplications:getReplications', __args__, opts=opts, typ=GetReplicationsResult).value

    return AwaitableGetReplicationsResult(
        availability_domain=pulumi.get(__ret__, 'availability_domain'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        file_system_id=pulumi.get(__ret__, 'file_system_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        replications=pulumi.get(__ret__, 'replications'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_replications)
def get_replications_output(availability_domain: Optional[pulumi.Input[str]] = None,
                            compartment_id: Optional[pulumi.Input[str]] = None,
                            display_name: Optional[pulumi.Input[Optional[str]]] = None,
                            file_system_id: Optional[pulumi.Input[Optional[str]]] = None,
                            filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetReplicationsFilterArgs']]]]] = None,
                            id: Optional[pulumi.Input[Optional[str]]] = None,
                            state: Optional[pulumi.Input[Optional[str]]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReplicationsResult]:
    """
    This data source provides the list of Replications in Oracle Cloud Infrastructure File Storage service.

    Lists the replication resources in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_replications = oci.FileStorage.get_replications(availability_domain=var["replication_availability_domain"],
        compartment_id=var["compartment_id"],
        display_name=var["replication_display_name"],
        file_system_id=oci_file_storage_file_system["test_file_system"]["id"],
        id=var["replication_id"],
        state=var["replication_state"])
    ```


    :param str availability_domain: The name of the availability domain.  Example: `Uocm:PHX-AD-1`
    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A user-friendly name. It does not have to be unique, and it is changeable.  Example: `My resource`
    :param str file_system_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the source file system.
    :param str id: Filter results by [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resouce type.
    :param str state: Filter results by the specified lifecycle state. Must be a valid state for the resource type.
    """
    ...
