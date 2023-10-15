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
    'GetDeploymentsResult',
    'AwaitableGetDeploymentsResult',
    'get_deployments',
    'get_deployments_output',
]

@pulumi.output_type
class GetDeploymentsResult:
    """
    A collection of values returned by getDeployments.
    """
    def __init__(__self__, assignable_connection_id=None, assigned_connection_id=None, compartment_id=None, deployment_collections=None, display_name=None, filters=None, fqdn=None, id=None, lifecycle_sub_state=None, state=None, supported_connection_type=None):
        if assignable_connection_id and not isinstance(assignable_connection_id, str):
            raise TypeError("Expected argument 'assignable_connection_id' to be a str")
        pulumi.set(__self__, "assignable_connection_id", assignable_connection_id)
        if assigned_connection_id and not isinstance(assigned_connection_id, str):
            raise TypeError("Expected argument 'assigned_connection_id' to be a str")
        pulumi.set(__self__, "assigned_connection_id", assigned_connection_id)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if deployment_collections and not isinstance(deployment_collections, list):
            raise TypeError("Expected argument 'deployment_collections' to be a list")
        pulumi.set(__self__, "deployment_collections", deployment_collections)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if fqdn and not isinstance(fqdn, str):
            raise TypeError("Expected argument 'fqdn' to be a str")
        pulumi.set(__self__, "fqdn", fqdn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lifecycle_sub_state and not isinstance(lifecycle_sub_state, str):
            raise TypeError("Expected argument 'lifecycle_sub_state' to be a str")
        pulumi.set(__self__, "lifecycle_sub_state", lifecycle_sub_state)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if supported_connection_type and not isinstance(supported_connection_type, str):
            raise TypeError("Expected argument 'supported_connection_type' to be a str")
        pulumi.set(__self__, "supported_connection_type", supported_connection_type)

    @property
    @pulumi.getter(name="assignableConnectionId")
    def assignable_connection_id(self) -> Optional[str]:
        return pulumi.get(self, "assignable_connection_id")

    @property
    @pulumi.getter(name="assignedConnectionId")
    def assigned_connection_id(self) -> Optional[str]:
        return pulumi.get(self, "assigned_connection_id")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment being referenced.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="deploymentCollections")
    def deployment_collections(self) -> Sequence['outputs.GetDeploymentsDeploymentCollectionResult']:
        """
        The list of deployment_collection.
        """
        return pulumi.get(self, "deployment_collections")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        An object's Display Name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetDeploymentsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def fqdn(self) -> Optional[str]:
        """
        A three-label Fully Qualified Domain Name (FQDN) for a resource.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lifecycleSubState")
    def lifecycle_sub_state(self) -> Optional[str]:
        """
        Possible GGS lifecycle sub-states.
        """
        return pulumi.get(self, "lifecycle_sub_state")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        Possible lifecycle states.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="supportedConnectionType")
    def supported_connection_type(self) -> Optional[str]:
        return pulumi.get(self, "supported_connection_type")


class AwaitableGetDeploymentsResult(GetDeploymentsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDeploymentsResult(
            assignable_connection_id=self.assignable_connection_id,
            assigned_connection_id=self.assigned_connection_id,
            compartment_id=self.compartment_id,
            deployment_collections=self.deployment_collections,
            display_name=self.display_name,
            filters=self.filters,
            fqdn=self.fqdn,
            id=self.id,
            lifecycle_sub_state=self.lifecycle_sub_state,
            state=self.state,
            supported_connection_type=self.supported_connection_type)


def get_deployments(assignable_connection_id: Optional[str] = None,
                    assigned_connection_id: Optional[str] = None,
                    compartment_id: Optional[str] = None,
                    display_name: Optional[str] = None,
                    filters: Optional[Sequence[pulumi.InputType['GetDeploymentsFilterArgs']]] = None,
                    fqdn: Optional[str] = None,
                    lifecycle_sub_state: Optional[str] = None,
                    state: Optional[str] = None,
                    supported_connection_type: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDeploymentsResult:
    """
    This data source provides the list of Deployments in Oracle Cloud Infrastructure Golden Gate service.

    Lists the Deployments in a compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_deployments = oci.GoldenGate.get_deployments(compartment_id=var["compartment_id"],
        assignable_connection_id=oci_golden_gate_connection["test_connection"]["id"],
        assigned_connection_id=oci_golden_gate_connection["test_connection"]["id"],
        display_name=var["deployment_display_name"],
        fqdn=var["deployment_fqdn"],
        lifecycle_sub_state=var["deployment_lifecycle_sub_state"],
        state=var["deployment_state"],
        supported_connection_type=var["deployment_supported_connection_type"])
    ```


    :param str assignable_connection_id: Return the deployments to which the specified connectionId may be assigned.
    :param str assigned_connection_id: The OCID of the connection which for the deployment must be assigned.
    :param str compartment_id: The OCID of the compartment that contains the work request. Work requests should be scoped  to the same compartment as the resource the work request affects. If the work request concerns  multiple resources, and those resources are not in the same compartment, it is up to the service team  to pick the primary resource whose compartment should be used.
    :param str display_name: A filter to return only the resources that match the entire 'displayName' given.
    :param str fqdn: A filter to return only the resources that match the 'fqdn' given.
    :param str lifecycle_sub_state: A filter to return only the resources that match the 'lifecycleSubState' given.
    :param str state: A filter to return only the resources that match the 'lifecycleState' given.
    :param str supported_connection_type: The connection type which the deployment must support.
    """
    __args__ = dict()
    __args__['assignableConnectionId'] = assignable_connection_id
    __args__['assignedConnectionId'] = assigned_connection_id
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['fqdn'] = fqdn
    __args__['lifecycleSubState'] = lifecycle_sub_state
    __args__['state'] = state
    __args__['supportedConnectionType'] = supported_connection_type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:GoldenGate/getDeployments:getDeployments', __args__, opts=opts, typ=GetDeploymentsResult).value

    return AwaitableGetDeploymentsResult(
        assignable_connection_id=pulumi.get(__ret__, 'assignable_connection_id'),
        assigned_connection_id=pulumi.get(__ret__, 'assigned_connection_id'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        deployment_collections=pulumi.get(__ret__, 'deployment_collections'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        fqdn=pulumi.get(__ret__, 'fqdn'),
        id=pulumi.get(__ret__, 'id'),
        lifecycle_sub_state=pulumi.get(__ret__, 'lifecycle_sub_state'),
        state=pulumi.get(__ret__, 'state'),
        supported_connection_type=pulumi.get(__ret__, 'supported_connection_type'))


@_utilities.lift_output_func(get_deployments)
def get_deployments_output(assignable_connection_id: Optional[pulumi.Input[Optional[str]]] = None,
                           assigned_connection_id: Optional[pulumi.Input[Optional[str]]] = None,
                           compartment_id: Optional[pulumi.Input[str]] = None,
                           display_name: Optional[pulumi.Input[Optional[str]]] = None,
                           filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDeploymentsFilterArgs']]]]] = None,
                           fqdn: Optional[pulumi.Input[Optional[str]]] = None,
                           lifecycle_sub_state: Optional[pulumi.Input[Optional[str]]] = None,
                           state: Optional[pulumi.Input[Optional[str]]] = None,
                           supported_connection_type: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDeploymentsResult]:
    """
    This data source provides the list of Deployments in Oracle Cloud Infrastructure Golden Gate service.

    Lists the Deployments in a compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_deployments = oci.GoldenGate.get_deployments(compartment_id=var["compartment_id"],
        assignable_connection_id=oci_golden_gate_connection["test_connection"]["id"],
        assigned_connection_id=oci_golden_gate_connection["test_connection"]["id"],
        display_name=var["deployment_display_name"],
        fqdn=var["deployment_fqdn"],
        lifecycle_sub_state=var["deployment_lifecycle_sub_state"],
        state=var["deployment_state"],
        supported_connection_type=var["deployment_supported_connection_type"])
    ```


    :param str assignable_connection_id: Return the deployments to which the specified connectionId may be assigned.
    :param str assigned_connection_id: The OCID of the connection which for the deployment must be assigned.
    :param str compartment_id: The OCID of the compartment that contains the work request. Work requests should be scoped  to the same compartment as the resource the work request affects. If the work request concerns  multiple resources, and those resources are not in the same compartment, it is up to the service team  to pick the primary resource whose compartment should be used.
    :param str display_name: A filter to return only the resources that match the entire 'displayName' given.
    :param str fqdn: A filter to return only the resources that match the 'fqdn' given.
    :param str lifecycle_sub_state: A filter to return only the resources that match the 'lifecycleSubState' given.
    :param str state: A filter to return only the resources that match the 'lifecycleState' given.
    :param str supported_connection_type: The connection type which the deployment must support.
    """
    ...
