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
    def __init__(__self__, compartment_id=None, deploy_pipeline_id=None, deployment_collections=None, display_name=None, filters=None, id=None, project_id=None, state=None, time_created_greater_than_or_equal_to=None, time_created_less_than=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if deploy_pipeline_id and not isinstance(deploy_pipeline_id, str):
            raise TypeError("Expected argument 'deploy_pipeline_id' to be a str")
        pulumi.set(__self__, "deploy_pipeline_id", deploy_pipeline_id)
        if deployment_collections and not isinstance(deployment_collections, list):
            raise TypeError("Expected argument 'deployment_collections' to be a list")
        pulumi.set(__self__, "deployment_collections", deployment_collections)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if time_created_greater_than_or_equal_to and not isinstance(time_created_greater_than_or_equal_to, str):
            raise TypeError("Expected argument 'time_created_greater_than_or_equal_to' to be a str")
        pulumi.set(__self__, "time_created_greater_than_or_equal_to", time_created_greater_than_or_equal_to)
        if time_created_less_than and not isinstance(time_created_less_than, str):
            raise TypeError("Expected argument 'time_created_less_than' to be a str")
        pulumi.set(__self__, "time_created_less_than", time_created_less_than)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        """
        The OCID of a compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="deployPipelineId")
    def deploy_pipeline_id(self) -> Optional[str]:
        """
        The OCID of a pipeline.
        """
        return pulumi.get(self, "deploy_pipeline_id")

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
        Deployment identifier which can be renamed and is not necessarily unique. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetDeploymentsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Unique identifier that is immutable on creation.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[str]:
        """
        The OCID of a project.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the deployment.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreatedGreaterThanOrEqualTo")
    def time_created_greater_than_or_equal_to(self) -> Optional[str]:
        return pulumi.get(self, "time_created_greater_than_or_equal_to")

    @property
    @pulumi.getter(name="timeCreatedLessThan")
    def time_created_less_than(self) -> Optional[str]:
        return pulumi.get(self, "time_created_less_than")


class AwaitableGetDeploymentsResult(GetDeploymentsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDeploymentsResult(
            compartment_id=self.compartment_id,
            deploy_pipeline_id=self.deploy_pipeline_id,
            deployment_collections=self.deployment_collections,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            project_id=self.project_id,
            state=self.state,
            time_created_greater_than_or_equal_to=self.time_created_greater_than_or_equal_to,
            time_created_less_than=self.time_created_less_than)


def get_deployments(compartment_id: Optional[str] = None,
                    deploy_pipeline_id: Optional[str] = None,
                    display_name: Optional[str] = None,
                    filters: Optional[Sequence[pulumi.InputType['GetDeploymentsFilterArgs']]] = None,
                    id: Optional[str] = None,
                    project_id: Optional[str] = None,
                    state: Optional[str] = None,
                    time_created_greater_than_or_equal_to: Optional[str] = None,
                    time_created_less_than: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDeploymentsResult:
    """
    This data source provides the list of Deployments in Oracle Cloud Infrastructure Devops service.

    Returns a list of deployments.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_deployments = oci.DevOps.get_deployments(compartment_id=var["compartment_id"],
        deploy_pipeline_id=oci_devops_deploy_pipeline["test_deploy_pipeline"]["id"],
        display_name=var["deployment_display_name"],
        id=var["deployment_id"],
        project_id=oci_devops_project["test_project"]["id"],
        state=var["deployment_state"],
        time_created_greater_than_or_equal_to=var["deployment_time_created_greater_than_or_equal_to"],
        time_created_less_than=var["deployment_time_created_less_than"])
    ```


    :param str compartment_id: The OCID of the compartment in which to list resources.
    :param str deploy_pipeline_id: The ID of the parent pipeline.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str id: Unique identifier or OCID for listing a single resource by ID.
    :param str project_id: unique project identifier
    :param str state: A filter to return only Deployments that matches the given lifecycleState.
    :param str time_created_greater_than_or_equal_to: Search for DevOps resources that were created after a specific date. Specifying this parameter corresponding to `timeCreatedGreaterThanOrEqualTo` parameter will retrieve all security assessments created after the specified created date, in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).
    :param str time_created_less_than: Search for DevOps resources that were created before a specific date. Specifying this parameter corresponding to `timeCreatedLessThan` parameter will retrieve all assessments created before the specified created date, in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['deployPipelineId'] = deploy_pipeline_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['projectId'] = project_id
    __args__['state'] = state
    __args__['timeCreatedGreaterThanOrEqualTo'] = time_created_greater_than_or_equal_to
    __args__['timeCreatedLessThan'] = time_created_less_than
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DevOps/getDeployments:getDeployments', __args__, opts=opts, typ=GetDeploymentsResult).value

    return AwaitableGetDeploymentsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        deploy_pipeline_id=pulumi.get(__ret__, 'deploy_pipeline_id'),
        deployment_collections=pulumi.get(__ret__, 'deployment_collections'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        project_id=pulumi.get(__ret__, 'project_id'),
        state=pulumi.get(__ret__, 'state'),
        time_created_greater_than_or_equal_to=pulumi.get(__ret__, 'time_created_greater_than_or_equal_to'),
        time_created_less_than=pulumi.get(__ret__, 'time_created_less_than'))


@_utilities.lift_output_func(get_deployments)
def get_deployments_output(compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                           deploy_pipeline_id: Optional[pulumi.Input[Optional[str]]] = None,
                           display_name: Optional[pulumi.Input[Optional[str]]] = None,
                           filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDeploymentsFilterArgs']]]]] = None,
                           id: Optional[pulumi.Input[Optional[str]]] = None,
                           project_id: Optional[pulumi.Input[Optional[str]]] = None,
                           state: Optional[pulumi.Input[Optional[str]]] = None,
                           time_created_greater_than_or_equal_to: Optional[pulumi.Input[Optional[str]]] = None,
                           time_created_less_than: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDeploymentsResult]:
    """
    This data source provides the list of Deployments in Oracle Cloud Infrastructure Devops service.

    Returns a list of deployments.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_deployments = oci.DevOps.get_deployments(compartment_id=var["compartment_id"],
        deploy_pipeline_id=oci_devops_deploy_pipeline["test_deploy_pipeline"]["id"],
        display_name=var["deployment_display_name"],
        id=var["deployment_id"],
        project_id=oci_devops_project["test_project"]["id"],
        state=var["deployment_state"],
        time_created_greater_than_or_equal_to=var["deployment_time_created_greater_than_or_equal_to"],
        time_created_less_than=var["deployment_time_created_less_than"])
    ```


    :param str compartment_id: The OCID of the compartment in which to list resources.
    :param str deploy_pipeline_id: The ID of the parent pipeline.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str id: Unique identifier or OCID for listing a single resource by ID.
    :param str project_id: unique project identifier
    :param str state: A filter to return only Deployments that matches the given lifecycleState.
    :param str time_created_greater_than_or_equal_to: Search for DevOps resources that were created after a specific date. Specifying this parameter corresponding to `timeCreatedGreaterThanOrEqualTo` parameter will retrieve all security assessments created after the specified created date, in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).
    :param str time_created_less_than: Search for DevOps resources that were created before a specific date. Specifying this parameter corresponding to `timeCreatedLessThan` parameter will retrieve all assessments created before the specified created date, in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).
    """
    ...
