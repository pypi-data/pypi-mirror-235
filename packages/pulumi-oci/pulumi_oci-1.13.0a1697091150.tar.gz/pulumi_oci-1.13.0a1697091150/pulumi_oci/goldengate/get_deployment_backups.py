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
    'GetDeploymentBackupsResult',
    'AwaitableGetDeploymentBackupsResult',
    'get_deployment_backups',
    'get_deployment_backups_output',
]

@pulumi.output_type
class GetDeploymentBackupsResult:
    """
    A collection of values returned by getDeploymentBackups.
    """
    def __init__(__self__, compartment_id=None, deployment_backup_collections=None, deployment_id=None, display_name=None, filters=None, id=None, state=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if deployment_backup_collections and not isinstance(deployment_backup_collections, list):
            raise TypeError("Expected argument 'deployment_backup_collections' to be a list")
        pulumi.set(__self__, "deployment_backup_collections", deployment_backup_collections)
        if deployment_id and not isinstance(deployment_id, str):
            raise TypeError("Expected argument 'deployment_id' to be a str")
        pulumi.set(__self__, "deployment_id", deployment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment being referenced.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="deploymentBackupCollections")
    def deployment_backup_collections(self) -> Sequence['outputs.GetDeploymentBackupsDeploymentBackupCollectionResult']:
        """
        The list of deployment_backup_collection.
        """
        return pulumi.get(self, "deployment_backup_collections")

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the deployment being referenced.
        """
        return pulumi.get(self, "deployment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        An object's Display Name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetDeploymentBackupsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        Possible lifecycle states.
        """
        return pulumi.get(self, "state")


class AwaitableGetDeploymentBackupsResult(GetDeploymentBackupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDeploymentBackupsResult(
            compartment_id=self.compartment_id,
            deployment_backup_collections=self.deployment_backup_collections,
            deployment_id=self.deployment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            state=self.state)


def get_deployment_backups(compartment_id: Optional[str] = None,
                           deployment_id: Optional[str] = None,
                           display_name: Optional[str] = None,
                           filters: Optional[Sequence[pulumi.InputType['GetDeploymentBackupsFilterArgs']]] = None,
                           state: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDeploymentBackupsResult:
    """
    This data source provides the list of Deployment Backups in Oracle Cloud Infrastructure Golden Gate service.

    Lists the Backups in a compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_deployment_backups = oci.GoldenGate.get_deployment_backups(compartment_id=var["compartment_id"],
        deployment_id=oci_golden_gate_deployment["test_deployment"]["id"],
        display_name=var["deployment_backup_display_name"],
        state=var["deployment_backup_state"])
    ```


    :param str compartment_id: The OCID of the compartment that contains the work request. Work requests should be scoped  to the same compartment as the resource the work request affects. If the work request concerns  multiple resources, and those resources are not in the same compartment, it is up to the service team  to pick the primary resource whose compartment should be used.
    :param str deployment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the deployment in which to list resources.
    :param str display_name: A filter to return only the resources that match the entire 'displayName' given.
    :param str state: A filter to return only the resources that match the 'lifecycleState' given.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['deploymentId'] = deployment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:GoldenGate/getDeploymentBackups:getDeploymentBackups', __args__, opts=opts, typ=GetDeploymentBackupsResult).value

    return AwaitableGetDeploymentBackupsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        deployment_backup_collections=pulumi.get(__ret__, 'deployment_backup_collections'),
        deployment_id=pulumi.get(__ret__, 'deployment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_deployment_backups)
def get_deployment_backups_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                  deployment_id: Optional[pulumi.Input[Optional[str]]] = None,
                                  display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                  filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDeploymentBackupsFilterArgs']]]]] = None,
                                  state: Optional[pulumi.Input[Optional[str]]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDeploymentBackupsResult]:
    """
    This data source provides the list of Deployment Backups in Oracle Cloud Infrastructure Golden Gate service.

    Lists the Backups in a compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_deployment_backups = oci.GoldenGate.get_deployment_backups(compartment_id=var["compartment_id"],
        deployment_id=oci_golden_gate_deployment["test_deployment"]["id"],
        display_name=var["deployment_backup_display_name"],
        state=var["deployment_backup_state"])
    ```


    :param str compartment_id: The OCID of the compartment that contains the work request. Work requests should be scoped  to the same compartment as the resource the work request affects. If the work request concerns  multiple resources, and those resources are not in the same compartment, it is up to the service team  to pick the primary resource whose compartment should be used.
    :param str deployment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the deployment in which to list resources.
    :param str display_name: A filter to return only the resources that match the entire 'displayName' given.
    :param str state: A filter to return only the resources that match the 'lifecycleState' given.
    """
    ...
