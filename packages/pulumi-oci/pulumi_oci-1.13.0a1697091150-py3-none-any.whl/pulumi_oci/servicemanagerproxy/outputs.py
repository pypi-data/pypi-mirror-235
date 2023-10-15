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
    'GetServiceEnvironmentServiceDefinitionResult',
    'GetServiceEnvironmentServiceEnvironmentEndpointResult',
    'GetServiceEnvironmentsFilterResult',
    'GetServiceEnvironmentsServiceEnvironmentCollectionResult',
    'GetServiceEnvironmentsServiceEnvironmentCollectionItemResult',
    'GetServiceEnvironmentsServiceEnvironmentCollectionItemServiceDefinitionResult',
    'GetServiceEnvironmentsServiceEnvironmentCollectionItemServiceEnvironmentEndpointResult',
]

@pulumi.output_type
class GetServiceEnvironmentServiceDefinitionResult(dict):
    def __init__(__self__, *,
                 display_name: str,
                 short_display_name: str,
                 type: str):
        """
        :param str display_name: Display name of the service. For example, "Oracle Retail Order Management Cloud Service".
        :param str short_display_name: Short display name of the service. For example, "Retail Order Management".
        :param str type: The service definition type. For example, a service definition type "RGBUOROMS"  would be for the service "Oracle Retail Order Management Cloud Service".
        """
        GetServiceEnvironmentServiceDefinitionResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            display_name=display_name,
            short_display_name=short_display_name,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             display_name: str,
             short_display_name: str,
             type: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("display_name", display_name)
        _setter("short_display_name", short_display_name)
        _setter("type", type)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Display name of the service. For example, "Oracle Retail Order Management Cloud Service".
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="shortDisplayName")
    def short_display_name(self) -> str:
        """
        Short display name of the service. For example, "Retail Order Management".
        """
        return pulumi.get(self, "short_display_name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The service definition type. For example, a service definition type "RGBUOROMS"  would be for the service "Oracle Retail Order Management Cloud Service".
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class GetServiceEnvironmentServiceEnvironmentEndpointResult(dict):
    def __init__(__self__, *,
                 description: str,
                 environment_type: str,
                 url: str):
        """
        :param str description: Description of the environment link
        :param str environment_type: Service environment endpoint type.
        :param str url: Service environment instance URL.
        """
        GetServiceEnvironmentServiceEnvironmentEndpointResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            description=description,
            environment_type=environment_type,
            url=url,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             description: str,
             environment_type: str,
             url: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("description", description)
        _setter("environment_type", environment_type)
        _setter("url", url)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the environment link
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="environmentType")
    def environment_type(self) -> str:
        """
        Service environment endpoint type.
        """
        return pulumi.get(self, "environment_type")

    @property
    @pulumi.getter
    def url(self) -> str:
        """
        Service environment instance URL.
        """
        return pulumi.get(self, "url")


@pulumi.output_type
class GetServiceEnvironmentsFilterResult(dict):
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str],
                 regex: Optional[bool] = None):
        GetServiceEnvironmentsFilterResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            values=values,
            regex=regex,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: str,
             values: Sequence[str],
             regex: Optional[bool] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("name", name)
        _setter("values", values)
        if regex is not None:
            _setter("regex", regex)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @property
    @pulumi.getter
    def regex(self) -> Optional[bool]:
        return pulumi.get(self, "regex")


@pulumi.output_type
class GetServiceEnvironmentsServiceEnvironmentCollectionResult(dict):
    def __init__(__self__, *,
                 items: Sequence['outputs.GetServiceEnvironmentsServiceEnvironmentCollectionItemResult']):
        GetServiceEnvironmentsServiceEnvironmentCollectionResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            items=items,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             items: Sequence['outputs.GetServiceEnvironmentsServiceEnvironmentCollectionItemResult'],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("items", items)

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.GetServiceEnvironmentsServiceEnvironmentCollectionItemResult']:
        return pulumi.get(self, "items")


@pulumi.output_type
class GetServiceEnvironmentsServiceEnvironmentCollectionItemResult(dict):
    def __init__(__self__, *,
                 compartment_id: str,
                 console_url: str,
                 defined_tags: Mapping[str, Any],
                 freeform_tags: Mapping[str, Any],
                 id: str,
                 service_definitions: Sequence['outputs.GetServiceEnvironmentsServiceEnvironmentCollectionItemServiceDefinitionResult'],
                 service_environment_endpoints: Sequence['outputs.GetServiceEnvironmentsServiceEnvironmentCollectionItemServiceEnvironmentEndpointResult'],
                 status: str,
                 subscription_id: str):
        """
        :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the compartment.
        :param str console_url: The URL for the console.
        :param str id: Unqiue identifier for the entitlement related to the environment.
        :param Sequence['GetServiceEnvironmentsServiceEnvironmentCollectionItemServiceDefinitionArgs'] service_definitions: Details for a service definition.
        :param Sequence['GetServiceEnvironmentsServiceEnvironmentCollectionItemServiceEnvironmentEndpointArgs'] service_environment_endpoints: Array of service environment end points.
        :param str status: Status of the entitlement registration for the service.
        :param str subscription_id: The unique subscription ID associated with the service environment ID.
        """
        GetServiceEnvironmentsServiceEnvironmentCollectionItemResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            compartment_id=compartment_id,
            console_url=console_url,
            defined_tags=defined_tags,
            freeform_tags=freeform_tags,
            id=id,
            service_definitions=service_definitions,
            service_environment_endpoints=service_environment_endpoints,
            status=status,
            subscription_id=subscription_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             compartment_id: str,
             console_url: str,
             defined_tags: Mapping[str, Any],
             freeform_tags: Mapping[str, Any],
             id: str,
             service_definitions: Sequence['outputs.GetServiceEnvironmentsServiceEnvironmentCollectionItemServiceDefinitionResult'],
             service_environment_endpoints: Sequence['outputs.GetServiceEnvironmentsServiceEnvironmentCollectionItemServiceEnvironmentEndpointResult'],
             status: str,
             subscription_id: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("compartment_id", compartment_id)
        _setter("console_url", console_url)
        _setter("defined_tags", defined_tags)
        _setter("freeform_tags", freeform_tags)
        _setter("id", id)
        _setter("service_definitions", service_definitions)
        _setter("service_environment_endpoints", service_environment_endpoints)
        _setter("status", status)
        _setter("subscription_id", subscription_id)

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
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Unqiue identifier for the entitlement related to the environment.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="serviceDefinitions")
    def service_definitions(self) -> Sequence['outputs.GetServiceEnvironmentsServiceEnvironmentCollectionItemServiceDefinitionResult']:
        """
        Details for a service definition.
        """
        return pulumi.get(self, "service_definitions")

    @property
    @pulumi.getter(name="serviceEnvironmentEndpoints")
    def service_environment_endpoints(self) -> Sequence['outputs.GetServiceEnvironmentsServiceEnvironmentCollectionItemServiceEnvironmentEndpointResult']:
        """
        Array of service environment end points.
        """
        return pulumi.get(self, "service_environment_endpoints")

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


@pulumi.output_type
class GetServiceEnvironmentsServiceEnvironmentCollectionItemServiceDefinitionResult(dict):
    def __init__(__self__, *,
                 display_name: str,
                 short_display_name: str,
                 type: str):
        """
        :param str display_name: The display name of the resource.
        :param str short_display_name: Short display name of the service. For example, "Retail Order Management".
        :param str type: The service definition type. For example, a service definition type "RGBUOROMS"  would be for the service "Oracle Retail Order Management Cloud Service".
        """
        GetServiceEnvironmentsServiceEnvironmentCollectionItemServiceDefinitionResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            display_name=display_name,
            short_display_name=short_display_name,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             display_name: str,
             short_display_name: str,
             type: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("display_name", display_name)
        _setter("short_display_name", short_display_name)
        _setter("type", type)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name of the resource.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="shortDisplayName")
    def short_display_name(self) -> str:
        """
        Short display name of the service. For example, "Retail Order Management".
        """
        return pulumi.get(self, "short_display_name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The service definition type. For example, a service definition type "RGBUOROMS"  would be for the service "Oracle Retail Order Management Cloud Service".
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class GetServiceEnvironmentsServiceEnvironmentCollectionItemServiceEnvironmentEndpointResult(dict):
    def __init__(__self__, *,
                 description: str,
                 environment_type: str,
                 url: str):
        """
        :param str description: Description of the environment link
        :param str environment_type: Service environment endpoint type.
        :param str url: Service environment instance URL.
        """
        GetServiceEnvironmentsServiceEnvironmentCollectionItemServiceEnvironmentEndpointResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            description=description,
            environment_type=environment_type,
            url=url,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             description: str,
             environment_type: str,
             url: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("description", description)
        _setter("environment_type", environment_type)
        _setter("url", url)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the environment link
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="environmentType")
    def environment_type(self) -> str:
        """
        Service environment endpoint type.
        """
        return pulumi.get(self, "environment_type")

    @property
    @pulumi.getter
    def url(self) -> str:
        """
        Service environment instance URL.
        """
        return pulumi.get(self, "url")


