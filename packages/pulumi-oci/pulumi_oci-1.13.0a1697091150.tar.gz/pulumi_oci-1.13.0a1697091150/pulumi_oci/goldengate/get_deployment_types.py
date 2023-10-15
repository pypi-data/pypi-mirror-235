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
    'GetDeploymentTypesResult',
    'AwaitableGetDeploymentTypesResult',
    'get_deployment_types',
    'get_deployment_types_output',
]

@pulumi.output_type
class GetDeploymentTypesResult:
    """
    A collection of values returned by getDeploymentTypes.
    """
    def __init__(__self__, compartment_id=None, deployment_type=None, deployment_type_collections=None, display_name=None, filters=None, id=None, ogg_version=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if deployment_type and not isinstance(deployment_type, str):
            raise TypeError("Expected argument 'deployment_type' to be a str")
        pulumi.set(__self__, "deployment_type", deployment_type)
        if deployment_type_collections and not isinstance(deployment_type_collections, list):
            raise TypeError("Expected argument 'deployment_type_collections' to be a list")
        pulumi.set(__self__, "deployment_type_collections", deployment_type_collections)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ogg_version and not isinstance(ogg_version, str):
            raise TypeError("Expected argument 'ogg_version' to be a str")
        pulumi.set(__self__, "ogg_version", ogg_version)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> Optional[str]:
        """
        The type of deployment, which can be any one of the Allowed values.  NOTE: Use of the value 'OGG' is maintained for backward compatibility purposes.  Its use is discouraged in favor of 'DATABASE_ORACLE'.
        """
        return pulumi.get(self, "deployment_type")

    @property
    @pulumi.getter(name="deploymentTypeCollections")
    def deployment_type_collections(self) -> Sequence['outputs.GetDeploymentTypesDeploymentTypeCollectionResult']:
        """
        The list of deployment_type_collection.
        """
        return pulumi.get(self, "deployment_type_collections")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        An object's Display Name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetDeploymentTypesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="oggVersion")
    def ogg_version(self) -> Optional[str]:
        """
        Version of OGG
        """
        return pulumi.get(self, "ogg_version")


class AwaitableGetDeploymentTypesResult(GetDeploymentTypesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDeploymentTypesResult(
            compartment_id=self.compartment_id,
            deployment_type=self.deployment_type,
            deployment_type_collections=self.deployment_type_collections,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            ogg_version=self.ogg_version)


def get_deployment_types(compartment_id: Optional[str] = None,
                         deployment_type: Optional[str] = None,
                         display_name: Optional[str] = None,
                         filters: Optional[Sequence[pulumi.InputType['GetDeploymentTypesFilterArgs']]] = None,
                         ogg_version: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDeploymentTypesResult:
    """
    This data source provides the list of Deployment Types in Oracle Cloud Infrastructure Golden Gate service.

    Returns an array of DeploymentTypeDescriptor

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_deployment_types = oci.GoldenGate.get_deployment_types(compartment_id=var["compartment_id"],
        deployment_type=var["deployment_type_deployment_type"],
        display_name=var["deployment_type_display_name"],
        ogg_version=var["deployment_type_ogg_version"])
    ```


    :param str compartment_id: The OCID of the compartment that contains the work request. Work requests should be scoped  to the same compartment as the resource the work request affects. If the work request concerns  multiple resources, and those resources are not in the same compartment, it is up to the service team  to pick the primary resource whose compartment should be used.
    :param str deployment_type: The type of deployment, the value determines the exact 'type' of the service executed in the deployment. Default value is DATABASE_ORACLE.
    :param str display_name: A filter to return only the resources that match the entire 'displayName' given.
    :param str ogg_version: Allows to query by a specific GoldenGate version.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['deploymentType'] = deployment_type
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['oggVersion'] = ogg_version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:GoldenGate/getDeploymentTypes:getDeploymentTypes', __args__, opts=opts, typ=GetDeploymentTypesResult).value

    return AwaitableGetDeploymentTypesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        deployment_type=pulumi.get(__ret__, 'deployment_type'),
        deployment_type_collections=pulumi.get(__ret__, 'deployment_type_collections'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        ogg_version=pulumi.get(__ret__, 'ogg_version'))


@_utilities.lift_output_func(get_deployment_types)
def get_deployment_types_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                deployment_type: Optional[pulumi.Input[Optional[str]]] = None,
                                display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDeploymentTypesFilterArgs']]]]] = None,
                                ogg_version: Optional[pulumi.Input[Optional[str]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDeploymentTypesResult]:
    """
    This data source provides the list of Deployment Types in Oracle Cloud Infrastructure Golden Gate service.

    Returns an array of DeploymentTypeDescriptor

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_deployment_types = oci.GoldenGate.get_deployment_types(compartment_id=var["compartment_id"],
        deployment_type=var["deployment_type_deployment_type"],
        display_name=var["deployment_type_display_name"],
        ogg_version=var["deployment_type_ogg_version"])
    ```


    :param str compartment_id: The OCID of the compartment that contains the work request. Work requests should be scoped  to the same compartment as the resource the work request affects. If the work request concerns  multiple resources, and those resources are not in the same compartment, it is up to the service team  to pick the primary resource whose compartment should be used.
    :param str deployment_type: The type of deployment, the value determines the exact 'type' of the service executed in the deployment. Default value is DATABASE_ORACLE.
    :param str display_name: A filter to return only the resources that match the entire 'displayName' given.
    :param str ogg_version: Allows to query by a specific GoldenGate version.
    """
    ...
