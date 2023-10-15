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
    'GetServiceEnvironmentResult',
    'AwaitableGetServiceEnvironmentResult',
    'get_service_environment',
    'get_service_environment_output',
]

@pulumi.output_type
class GetServiceEnvironmentResult:
    """
    A collection of values returned by getServiceEnvironment.
    """
    def __init__(__self__, compartment_id=None, console_url=None, id=None, service_definitions=None, service_environment_endpoints=None, service_environment_id=None, status=None, subscription_id=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if console_url and not isinstance(console_url, str):
            raise TypeError("Expected argument 'console_url' to be a str")
        pulumi.set(__self__, "console_url", console_url)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if service_definitions and not isinstance(service_definitions, list):
            raise TypeError("Expected argument 'service_definitions' to be a list")
        pulumi.set(__self__, "service_definitions", service_definitions)
        if service_environment_endpoints and not isinstance(service_environment_endpoints, list):
            raise TypeError("Expected argument 'service_environment_endpoints' to be a list")
        pulumi.set(__self__, "service_environment_endpoints", service_environment_endpoints)
        if service_environment_id and not isinstance(service_environment_id, str):
            raise TypeError("Expected argument 'service_environment_id' to be a str")
        pulumi.set(__self__, "service_environment_id", service_environment_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if subscription_id and not isinstance(subscription_id, str):
            raise TypeError("Expected argument 'subscription_id' to be a str")
        pulumi.set(__self__, "subscription_id", subscription_id)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="consoleUrl")
    def console_url(self) -> str:
        """
        The URL for the console.
        """
        return pulumi.get(self, "console_url")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="serviceDefinitions")
    def service_definitions(self) -> Sequence['outputs.GetServiceEnvironmentServiceDefinitionResult']:
        """
        Details for a service definition.
        """
        return pulumi.get(self, "service_definitions")

    @property
    @pulumi.getter(name="serviceEnvironmentEndpoints")
    def service_environment_endpoints(self) -> Sequence['outputs.GetServiceEnvironmentServiceEnvironmentEndpointResult']:
        """
        Array of service environment end points.
        """
        return pulumi.get(self, "service_environment_endpoints")

    @property
    @pulumi.getter(name="serviceEnvironmentId")
    def service_environment_id(self) -> str:
        return pulumi.get(self, "service_environment_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Status of the entitlement registration for the service.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> str:
        """
        The unique subscription ID associated with the service environment ID.
        """
        return pulumi.get(self, "subscription_id")


class AwaitableGetServiceEnvironmentResult(GetServiceEnvironmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceEnvironmentResult(
            compartment_id=self.compartment_id,
            console_url=self.console_url,
            id=self.id,
            service_definitions=self.service_definitions,
            service_environment_endpoints=self.service_environment_endpoints,
            service_environment_id=self.service_environment_id,
            status=self.status,
            subscription_id=self.subscription_id)


def get_service_environment(compartment_id: Optional[str] = None,
                            service_environment_id: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceEnvironmentResult:
    """
    This data source provides details about a specific Service Environment resource in Oracle Cloud Infrastructure Service Manager Proxy service.

    Get the detailed information for a specific service environment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_service_environment = oci.ServiceManagerProxy.get_service_environment(compartment_id=var["compartment_id"],
        service_environment_id=oci_service_manager_proxy_service_environment["test_service_environment"]["id"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the compartment.
    :param str service_environment_id: The unique identifier associated with the service environment. 
           
           **Note:** Not an [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['serviceEnvironmentId'] = service_environment_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:ServiceManagerProxy/getServiceEnvironment:getServiceEnvironment', __args__, opts=opts, typ=GetServiceEnvironmentResult).value

    return AwaitableGetServiceEnvironmentResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        console_url=pulumi.get(__ret__, 'console_url'),
        id=pulumi.get(__ret__, 'id'),
        service_definitions=pulumi.get(__ret__, 'service_definitions'),
        service_environment_endpoints=pulumi.get(__ret__, 'service_environment_endpoints'),
        service_environment_id=pulumi.get(__ret__, 'service_environment_id'),
        status=pulumi.get(__ret__, 'status'),
        subscription_id=pulumi.get(__ret__, 'subscription_id'))


@_utilities.lift_output_func(get_service_environment)
def get_service_environment_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                   service_environment_id: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServiceEnvironmentResult]:
    """
    This data source provides details about a specific Service Environment resource in Oracle Cloud Infrastructure Service Manager Proxy service.

    Get the detailed information for a specific service environment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_service_environment = oci.ServiceManagerProxy.get_service_environment(compartment_id=var["compartment_id"],
        service_environment_id=oci_service_manager_proxy_service_environment["test_service_environment"]["id"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the compartment.
    :param str service_environment_id: The unique identifier associated with the service environment. 
           
           **Note:** Not an [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    """
    ...
