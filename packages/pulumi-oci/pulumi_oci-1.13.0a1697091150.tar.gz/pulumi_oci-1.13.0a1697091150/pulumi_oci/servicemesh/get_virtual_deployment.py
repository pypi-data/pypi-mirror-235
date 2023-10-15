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
    'GetVirtualDeploymentResult',
    'AwaitableGetVirtualDeploymentResult',
    'get_virtual_deployment',
    'get_virtual_deployment_output',
]

@pulumi.output_type
class GetVirtualDeploymentResult:
    """
    A collection of values returned by getVirtualDeployment.
    """
    def __init__(__self__, access_loggings=None, compartment_id=None, defined_tags=None, description=None, freeform_tags=None, id=None, lifecycle_details=None, listeners=None, name=None, service_discoveries=None, state=None, system_tags=None, time_created=None, time_updated=None, virtual_deployment_id=None, virtual_service_id=None):
        if access_loggings and not isinstance(access_loggings, list):
            raise TypeError("Expected argument 'access_loggings' to be a list")
        pulumi.set(__self__, "access_loggings", access_loggings)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if listeners and not isinstance(listeners, list):
            raise TypeError("Expected argument 'listeners' to be a list")
        pulumi.set(__self__, "listeners", listeners)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if service_discoveries and not isinstance(service_discoveries, list):
            raise TypeError("Expected argument 'service_discoveries' to be a list")
        pulumi.set(__self__, "service_discoveries", service_discoveries)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)
        if virtual_deployment_id and not isinstance(virtual_deployment_id, str):
            raise TypeError("Expected argument 'virtual_deployment_id' to be a str")
        pulumi.set(__self__, "virtual_deployment_id", virtual_deployment_id)
        if virtual_service_id and not isinstance(virtual_service_id, str):
            raise TypeError("Expected argument 'virtual_service_id' to be a str")
        pulumi.set(__self__, "virtual_service_id", virtual_service_id)

    @property
    @pulumi.getter(name="accessLoggings")
    def access_loggings(self) -> Sequence['outputs.GetVirtualDeploymentAccessLoggingResult']:
        """
        This configuration determines if logging is enabled and where the logs will be output.
        """
        return pulumi.get(self, "access_loggings")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the resource. It can be changed after creation. Avoid entering confidential information.  Example: `This is my new resource`
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Unique identifier that is immutable on creation.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter
    def listeners(self) -> Sequence['outputs.GetVirtualDeploymentListenerResult']:
        """
        The listeners for the virtual deployment
        """
        return pulumi.get(self, "listeners")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A user-friendly name. The name must be unique within the same virtual service and cannot be changed after creation. Avoid entering confidential information.  Example: `My unique resource name`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="serviceDiscoveries")
    def service_discoveries(self) -> Sequence['outputs.GetVirtualDeploymentServiceDiscoveryResult']:
        """
        Service Discovery configuration for virtual deployments.
        """
        return pulumi.get(self, "service_discoveries")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the Resource.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The time when this resource was created in an RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The time when this resource was updated in an RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_updated")

    @property
    @pulumi.getter(name="virtualDeploymentId")
    def virtual_deployment_id(self) -> str:
        return pulumi.get(self, "virtual_deployment_id")

    @property
    @pulumi.getter(name="virtualServiceId")
    def virtual_service_id(self) -> str:
        """
        The OCID of the virtual service in which this virtual deployment is created.
        """
        return pulumi.get(self, "virtual_service_id")


class AwaitableGetVirtualDeploymentResult(GetVirtualDeploymentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualDeploymentResult(
            access_loggings=self.access_loggings,
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            description=self.description,
            freeform_tags=self.freeform_tags,
            id=self.id,
            lifecycle_details=self.lifecycle_details,
            listeners=self.listeners,
            name=self.name,
            service_discoveries=self.service_discoveries,
            state=self.state,
            system_tags=self.system_tags,
            time_created=self.time_created,
            time_updated=self.time_updated,
            virtual_deployment_id=self.virtual_deployment_id,
            virtual_service_id=self.virtual_service_id)


def get_virtual_deployment(virtual_deployment_id: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualDeploymentResult:
    """
    This data source provides details about a specific Virtual Deployment resource in Oracle Cloud Infrastructure Service Mesh service.

    Gets a VirtualDeployment by identifier.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_virtual_deployment = oci.ServiceMesh.get_virtual_deployment(virtual_deployment_id=oci_service_mesh_virtual_deployment["test_virtual_deployment"]["id"])
    ```


    :param str virtual_deployment_id: Unique VirtualDeployment identifier.
    """
    __args__ = dict()
    __args__['virtualDeploymentId'] = virtual_deployment_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:ServiceMesh/getVirtualDeployment:getVirtualDeployment', __args__, opts=opts, typ=GetVirtualDeploymentResult).value

    return AwaitableGetVirtualDeploymentResult(
        access_loggings=pulumi.get(__ret__, 'access_loggings'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        description=pulumi.get(__ret__, 'description'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        listeners=pulumi.get(__ret__, 'listeners'),
        name=pulumi.get(__ret__, 'name'),
        service_discoveries=pulumi.get(__ret__, 'service_discoveries'),
        state=pulumi.get(__ret__, 'state'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'),
        virtual_deployment_id=pulumi.get(__ret__, 'virtual_deployment_id'),
        virtual_service_id=pulumi.get(__ret__, 'virtual_service_id'))


@_utilities.lift_output_func(get_virtual_deployment)
def get_virtual_deployment_output(virtual_deployment_id: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualDeploymentResult]:
    """
    This data source provides details about a specific Virtual Deployment resource in Oracle Cloud Infrastructure Service Mesh service.

    Gets a VirtualDeployment by identifier.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_virtual_deployment = oci.ServiceMesh.get_virtual_deployment(virtual_deployment_id=oci_service_mesh_virtual_deployment["test_virtual_deployment"]["id"])
    ```


    :param str virtual_deployment_id: Unique VirtualDeployment identifier.
    """
    ...
