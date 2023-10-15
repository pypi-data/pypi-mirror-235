# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'SessionKeyDetailsArgs',
    'SessionTargetResourceDetailsArgs',
    'GetBastionsFilterArgs',
    'GetSessionsFilterArgs',
]

@pulumi.input_type
class SessionKeyDetailsArgs:
    def __init__(__self__, *,
                 public_key_content: pulumi.Input[str]):
        """
        :param pulumi.Input[str] public_key_content: The public key in OpenSSH format of the SSH key pair for the session. When you connect to the session, you must provide the private key of the same SSH key pair.
        """
        SessionKeyDetailsArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            public_key_content=public_key_content,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             public_key_content: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("public_key_content", public_key_content)

    @property
    @pulumi.getter(name="publicKeyContent")
    def public_key_content(self) -> pulumi.Input[str]:
        """
        The public key in OpenSSH format of the SSH key pair for the session. When you connect to the session, you must provide the private key of the same SSH key pair.
        """
        return pulumi.get(self, "public_key_content")

    @public_key_content.setter
    def public_key_content(self, value: pulumi.Input[str]):
        pulumi.set(self, "public_key_content", value)


@pulumi.input_type
class SessionTargetResourceDetailsArgs:
    def __init__(__self__, *,
                 session_type: pulumi.Input[str],
                 target_resource_display_name: Optional[pulumi.Input[str]] = None,
                 target_resource_fqdn: Optional[pulumi.Input[str]] = None,
                 target_resource_id: Optional[pulumi.Input[str]] = None,
                 target_resource_operating_system_user_name: Optional[pulumi.Input[str]] = None,
                 target_resource_port: Optional[pulumi.Input[int]] = None,
                 target_resource_private_ip_address: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] session_type: The session type.
        :param pulumi.Input[str] target_resource_display_name: The display name of the target Compute instance that the session connects to.
        :param pulumi.Input[str] target_resource_fqdn: The Fully Qualified Domain Name of the target resource that the session connects to.
        :param pulumi.Input[str] target_resource_id: The unique identifier (OCID) of the target resource (a Compute instance, for example) that the session connects to.
        :param pulumi.Input[str] target_resource_operating_system_user_name: The name of the user on the target resource operating system that the session uses for the connection.
        :param pulumi.Input[int] target_resource_port: The port number to connect to on the target resource.
        :param pulumi.Input[str] target_resource_private_ip_address: The private IP address of the target resource that the session connects to.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        SessionTargetResourceDetailsArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            session_type=session_type,
            target_resource_display_name=target_resource_display_name,
            target_resource_fqdn=target_resource_fqdn,
            target_resource_id=target_resource_id,
            target_resource_operating_system_user_name=target_resource_operating_system_user_name,
            target_resource_port=target_resource_port,
            target_resource_private_ip_address=target_resource_private_ip_address,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             session_type: pulumi.Input[str],
             target_resource_display_name: Optional[pulumi.Input[str]] = None,
             target_resource_fqdn: Optional[pulumi.Input[str]] = None,
             target_resource_id: Optional[pulumi.Input[str]] = None,
             target_resource_operating_system_user_name: Optional[pulumi.Input[str]] = None,
             target_resource_port: Optional[pulumi.Input[int]] = None,
             target_resource_private_ip_address: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("session_type", session_type)
        if target_resource_display_name is not None:
            _setter("target_resource_display_name", target_resource_display_name)
        if target_resource_fqdn is not None:
            _setter("target_resource_fqdn", target_resource_fqdn)
        if target_resource_id is not None:
            _setter("target_resource_id", target_resource_id)
        if target_resource_operating_system_user_name is not None:
            _setter("target_resource_operating_system_user_name", target_resource_operating_system_user_name)
        if target_resource_port is not None:
            _setter("target_resource_port", target_resource_port)
        if target_resource_private_ip_address is not None:
            _setter("target_resource_private_ip_address", target_resource_private_ip_address)

    @property
    @pulumi.getter(name="sessionType")
    def session_type(self) -> pulumi.Input[str]:
        """
        The session type.
        """
        return pulumi.get(self, "session_type")

    @session_type.setter
    def session_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "session_type", value)

    @property
    @pulumi.getter(name="targetResourceDisplayName")
    def target_resource_display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the target Compute instance that the session connects to.
        """
        return pulumi.get(self, "target_resource_display_name")

    @target_resource_display_name.setter
    def target_resource_display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_resource_display_name", value)

    @property
    @pulumi.getter(name="targetResourceFqdn")
    def target_resource_fqdn(self) -> Optional[pulumi.Input[str]]:
        """
        The Fully Qualified Domain Name of the target resource that the session connects to.
        """
        return pulumi.get(self, "target_resource_fqdn")

    @target_resource_fqdn.setter
    def target_resource_fqdn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_resource_fqdn", value)

    @property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identifier (OCID) of the target resource (a Compute instance, for example) that the session connects to.
        """
        return pulumi.get(self, "target_resource_id")

    @target_resource_id.setter
    def target_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_resource_id", value)

    @property
    @pulumi.getter(name="targetResourceOperatingSystemUserName")
    def target_resource_operating_system_user_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the user on the target resource operating system that the session uses for the connection.
        """
        return pulumi.get(self, "target_resource_operating_system_user_name")

    @target_resource_operating_system_user_name.setter
    def target_resource_operating_system_user_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_resource_operating_system_user_name", value)

    @property
    @pulumi.getter(name="targetResourcePort")
    def target_resource_port(self) -> Optional[pulumi.Input[int]]:
        """
        The port number to connect to on the target resource.
        """
        return pulumi.get(self, "target_resource_port")

    @target_resource_port.setter
    def target_resource_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "target_resource_port", value)

    @property
    @pulumi.getter(name="targetResourcePrivateIpAddress")
    def target_resource_private_ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The private IP address of the target resource that the session connects to.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "target_resource_private_ip_address")

    @target_resource_private_ip_address.setter
    def target_resource_private_ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_resource_private_ip_address", value)


@pulumi.input_type
class GetBastionsFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str],
                 regex: Optional[bool] = None):
        """
        :param str name: A filter to return only resources that match the entire name given.
        """
        GetBastionsFilterArgs._configure(
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
        """
        A filter to return only resources that match the entire name given.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def regex(self) -> Optional[bool]:
        return pulumi.get(self, "regex")

    @regex.setter
    def regex(self, value: Optional[bool]):
        pulumi.set(self, "regex", value)


@pulumi.input_type
class GetSessionsFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str],
                 regex: Optional[bool] = None):
        GetSessionsFilterArgs._configure(
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

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def regex(self) -> Optional[bool]:
        return pulumi.get(self, "regex")

    @regex.setter
    def regex(self, value: Optional[bool]):
        pulumi.set(self, "regex", value)


