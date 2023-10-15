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
    'GetDetectionProjectsResult',
    'AwaitableGetDetectionProjectsResult',
    'get_detection_projects',
    'get_detection_projects_output',
]

@pulumi.output_type
class GetDetectionProjectsResult:
    """
    A collection of values returned by getDetectionProjects.
    """
    def __init__(__self__, compartment_id=None, display_name=None, filters=None, id=None, project_collections=None, state=None):
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
        if project_collections and not isinstance(project_collections, list):
            raise TypeError("Expected argument 'project_collections' to be a list")
        pulumi.set(__self__, "project_collections", project_collections)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID for the project's compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetDetectionProjectsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="projectCollections")
    def project_collections(self) -> Sequence['outputs.GetDetectionProjectsProjectCollectionResult']:
        """
        The list of project_collection.
        """
        return pulumi.get(self, "project_collections")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The lifecycle state of the Project.
        """
        return pulumi.get(self, "state")


class AwaitableGetDetectionProjectsResult(GetDetectionProjectsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDetectionProjectsResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            project_collections=self.project_collections,
            state=self.state)


def get_detection_projects(compartment_id: Optional[str] = None,
                           display_name: Optional[str] = None,
                           filters: Optional[Sequence[pulumi.InputType['GetDetectionProjectsFilterArgs']]] = None,
                           state: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDetectionProjectsResult:
    """
    This data source provides the list of Projects in Oracle Cloud Infrastructure Ai Anomaly Detection service.

    Returns a list of  Projects.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_projects = oci.AiAnomalyDetection.get_detection_projects(compartment_id=var["compartment_id"],
        display_name=var["project_display_name"],
        state=var["project_state"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str state: <b>Filter</b> results by the specified lifecycle state. Must be a valid state for the resource type.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:AiAnomalyDetection/getDetectionProjects:getDetectionProjects', __args__, opts=opts, typ=GetDetectionProjectsResult).value

    return AwaitableGetDetectionProjectsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        project_collections=pulumi.get(__ret__, 'project_collections'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_detection_projects)
def get_detection_projects_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                  display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                  filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDetectionProjectsFilterArgs']]]]] = None,
                                  state: Optional[pulumi.Input[Optional[str]]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDetectionProjectsResult]:
    """
    This data source provides the list of Projects in Oracle Cloud Infrastructure Ai Anomaly Detection service.

    Returns a list of  Projects.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_projects = oci.AiAnomalyDetection.get_detection_projects(compartment_id=var["compartment_id"],
        display_name=var["project_display_name"],
        state=var["project_state"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str state: <b>Filter</b> results by the specified lifecycle state. Must be a valid state for the resource type.
    """
    ...
