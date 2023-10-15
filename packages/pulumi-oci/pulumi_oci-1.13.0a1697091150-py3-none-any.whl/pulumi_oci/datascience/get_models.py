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
    'GetModelsResult',
    'AwaitableGetModelsResult',
    'get_models',
    'get_models_output',
]

@pulumi.output_type
class GetModelsResult:
    """
    A collection of values returned by getModels.
    """
    def __init__(__self__, compartment_id=None, created_by=None, display_name=None, filters=None, id=None, model_version_set_name=None, models=None, project_id=None, state=None, version_label=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if created_by and not isinstance(created_by, str):
            raise TypeError("Expected argument 'created_by' to be a str")
        pulumi.set(__self__, "created_by", created_by)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if model_version_set_name and not isinstance(model_version_set_name, str):
            raise TypeError("Expected argument 'model_version_set_name' to be a str")
        pulumi.set(__self__, "model_version_set_name", model_version_set_name)
        if models and not isinstance(models, list):
            raise TypeError("Expected argument 'models' to be a list")
        pulumi.set(__self__, "models", models)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if version_label and not isinstance(version_label, str):
            raise TypeError("Expected argument 'version_label' to be a str")
        pulumi.set(__self__, "version_label", version_label)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the model's compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the user who created the model.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetModelsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the model.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="modelVersionSetName")
    def model_version_set_name(self) -> str:
        return pulumi.get(self, "model_version_set_name")

    @property
    @pulumi.getter
    def models(self) -> Sequence['outputs.GetModelsModelResult']:
        """
        The list of models.
        """
        return pulumi.get(self, "models")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project associated with the model.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The state of the model.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="versionLabel")
    def version_label(self) -> str:
        return pulumi.get(self, "version_label")


class AwaitableGetModelsResult(GetModelsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetModelsResult(
            compartment_id=self.compartment_id,
            created_by=self.created_by,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            model_version_set_name=self.model_version_set_name,
            models=self.models,
            project_id=self.project_id,
            state=self.state,
            version_label=self.version_label)


def get_models(compartment_id: Optional[str] = None,
               created_by: Optional[str] = None,
               display_name: Optional[str] = None,
               filters: Optional[Sequence[pulumi.InputType['GetModelsFilterArgs']]] = None,
               id: Optional[str] = None,
               model_version_set_name: Optional[str] = None,
               project_id: Optional[str] = None,
               state: Optional[str] = None,
               version_label: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetModelsResult:
    """
    This data source provides the list of Models in Oracle Cloud Infrastructure Data Science service.

    Lists models in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_models = oci.DataScience.get_models(compartment_id=var["compartment_id"],
        created_by=var["model_created_by"],
        display_name=var["model_display_name"],
        id=var["model_id"],
        model_version_set_name=oci_datascience_model_version_set["test_model_version_set"]["name"],
        project_id=oci_datascience_project["test_project"]["id"],
        state=var["model_state"])
    ```


    :param str compartment_id: <b>Filter</b> results by the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str created_by: <b>Filter</b> results by the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the user who created the resource.
    :param str display_name: <b>Filter</b> results by its user-friendly name.
    :param str id: <b>Filter</b> results by [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resource type.
    :param str project_id: <b>Filter</b> results by the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project.
    :param str state: <b>Filter</b> results by the specified lifecycle state. Must be a valid state for the resource type.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['createdBy'] = created_by
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['modelVersionSetName'] = model_version_set_name
    __args__['projectId'] = project_id
    __args__['state'] = state
    __args__['versionLabel'] = version_label
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataScience/getModels:getModels', __args__, opts=opts, typ=GetModelsResult).value

    return AwaitableGetModelsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        created_by=pulumi.get(__ret__, 'created_by'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        model_version_set_name=pulumi.get(__ret__, 'model_version_set_name'),
        models=pulumi.get(__ret__, 'models'),
        project_id=pulumi.get(__ret__, 'project_id'),
        state=pulumi.get(__ret__, 'state'),
        version_label=pulumi.get(__ret__, 'version_label'))


@_utilities.lift_output_func(get_models)
def get_models_output(compartment_id: Optional[pulumi.Input[str]] = None,
                      created_by: Optional[pulumi.Input[Optional[str]]] = None,
                      display_name: Optional[pulumi.Input[Optional[str]]] = None,
                      filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetModelsFilterArgs']]]]] = None,
                      id: Optional[pulumi.Input[Optional[str]]] = None,
                      model_version_set_name: Optional[pulumi.Input[str]] = None,
                      project_id: Optional[pulumi.Input[Optional[str]]] = None,
                      state: Optional[pulumi.Input[Optional[str]]] = None,
                      version_label: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetModelsResult]:
    """
    This data source provides the list of Models in Oracle Cloud Infrastructure Data Science service.

    Lists models in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_models = oci.DataScience.get_models(compartment_id=var["compartment_id"],
        created_by=var["model_created_by"],
        display_name=var["model_display_name"],
        id=var["model_id"],
        model_version_set_name=oci_datascience_model_version_set["test_model_version_set"]["name"],
        project_id=oci_datascience_project["test_project"]["id"],
        state=var["model_state"])
    ```


    :param str compartment_id: <b>Filter</b> results by the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str created_by: <b>Filter</b> results by the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the user who created the resource.
    :param str display_name: <b>Filter</b> results by its user-friendly name.
    :param str id: <b>Filter</b> results by [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resource type.
    :param str project_id: <b>Filter</b> results by the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project.
    :param str state: <b>Filter</b> results by the specified lifecycle state. Must be a valid state for the resource type.
    """
    ...
