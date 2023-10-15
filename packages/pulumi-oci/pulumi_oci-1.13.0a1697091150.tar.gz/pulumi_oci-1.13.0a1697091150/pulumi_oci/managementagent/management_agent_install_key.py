# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ManagementAgentInstallKeyArgs', 'ManagementAgentInstallKey']

@pulumi.input_type
class ManagementAgentInstallKeyArgs:
    def __init__(__self__, *,
                 compartment_id: pulumi.Input[str],
                 display_name: pulumi.Input[str],
                 allowed_key_install_count: Optional[pulumi.Input[int]] = None,
                 is_unlimited: Optional[pulumi.Input[bool]] = None,
                 time_expires: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ManagementAgentInstallKey resource.
        :param pulumi.Input[str] compartment_id: Compartment Identifier
        :param pulumi.Input[str] display_name: (Updatable) Management Agent install Key Name
        :param pulumi.Input[int] allowed_key_install_count: Total number of install for this keys
        :param pulumi.Input[bool] is_unlimited: If set to true, the install key has no expiration date or usage limit. Defaults to false
        :param pulumi.Input[str] time_expires: date after which key would expire after creation
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ManagementAgentInstallKeyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            compartment_id=compartment_id,
            display_name=display_name,
            allowed_key_install_count=allowed_key_install_count,
            is_unlimited=is_unlimited,
            time_expires=time_expires,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             compartment_id: pulumi.Input[str],
             display_name: pulumi.Input[str],
             allowed_key_install_count: Optional[pulumi.Input[int]] = None,
             is_unlimited: Optional[pulumi.Input[bool]] = None,
             time_expires: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("compartment_id", compartment_id)
        _setter("display_name", display_name)
        if allowed_key_install_count is not None:
            _setter("allowed_key_install_count", allowed_key_install_count)
        if is_unlimited is not None:
            _setter("is_unlimited", is_unlimited)
        if time_expires is not None:
            _setter("time_expires", time_expires)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Input[str]:
        """
        Compartment Identifier
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        (Updatable) Management Agent install Key Name
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="allowedKeyInstallCount")
    def allowed_key_install_count(self) -> Optional[pulumi.Input[int]]:
        """
        Total number of install for this keys
        """
        return pulumi.get(self, "allowed_key_install_count")

    @allowed_key_install_count.setter
    def allowed_key_install_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "allowed_key_install_count", value)

    @property
    @pulumi.getter(name="isUnlimited")
    def is_unlimited(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to true, the install key has no expiration date or usage limit. Defaults to false
        """
        return pulumi.get(self, "is_unlimited")

    @is_unlimited.setter
    def is_unlimited(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_unlimited", value)

    @property
    @pulumi.getter(name="timeExpires")
    def time_expires(self) -> Optional[pulumi.Input[str]]:
        """
        date after which key would expire after creation


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "time_expires")

    @time_expires.setter
    def time_expires(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_expires", value)


@pulumi.input_type
class _ManagementAgentInstallKeyState:
    def __init__(__self__, *,
                 allowed_key_install_count: Optional[pulumi.Input[int]] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 created_by_principal_id: Optional[pulumi.Input[str]] = None,
                 current_key_install_count: Optional[pulumi.Input[int]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 is_unlimited: Optional[pulumi.Input[bool]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 lifecycle_details: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 time_expires: Optional[pulumi.Input[str]] = None,
                 time_updated: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ManagementAgentInstallKey resources.
        :param pulumi.Input[int] allowed_key_install_count: Total number of install for this keys
        :param pulumi.Input[str] compartment_id: Compartment Identifier
        :param pulumi.Input[str] created_by_principal_id: Principal id of user who created the Agent Install key
        :param pulumi.Input[int] current_key_install_count: Total number of install for this keys
        :param pulumi.Input[str] display_name: (Updatable) Management Agent install Key Name
        :param pulumi.Input[bool] is_unlimited: If set to true, the install key has no expiration date or usage limit. Defaults to false
        :param pulumi.Input[str] key: Management Agent Install Key
        :param pulumi.Input[str] lifecycle_details: A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        :param pulumi.Input[str] state: Status of Key
        :param pulumi.Input[str] time_created: The time when Management Agent install Key was created. An RFC3339 formatted date time string
        :param pulumi.Input[str] time_expires: date after which key would expire after creation
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] time_updated: The time when Management Agent install Key was updated. An RFC3339 formatted date time string
        """
        _ManagementAgentInstallKeyState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            allowed_key_install_count=allowed_key_install_count,
            compartment_id=compartment_id,
            created_by_principal_id=created_by_principal_id,
            current_key_install_count=current_key_install_count,
            display_name=display_name,
            is_unlimited=is_unlimited,
            key=key,
            lifecycle_details=lifecycle_details,
            state=state,
            time_created=time_created,
            time_expires=time_expires,
            time_updated=time_updated,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             allowed_key_install_count: Optional[pulumi.Input[int]] = None,
             compartment_id: Optional[pulumi.Input[str]] = None,
             created_by_principal_id: Optional[pulumi.Input[str]] = None,
             current_key_install_count: Optional[pulumi.Input[int]] = None,
             display_name: Optional[pulumi.Input[str]] = None,
             is_unlimited: Optional[pulumi.Input[bool]] = None,
             key: Optional[pulumi.Input[str]] = None,
             lifecycle_details: Optional[pulumi.Input[str]] = None,
             state: Optional[pulumi.Input[str]] = None,
             time_created: Optional[pulumi.Input[str]] = None,
             time_expires: Optional[pulumi.Input[str]] = None,
             time_updated: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if allowed_key_install_count is not None:
            _setter("allowed_key_install_count", allowed_key_install_count)
        if compartment_id is not None:
            _setter("compartment_id", compartment_id)
        if created_by_principal_id is not None:
            _setter("created_by_principal_id", created_by_principal_id)
        if current_key_install_count is not None:
            _setter("current_key_install_count", current_key_install_count)
        if display_name is not None:
            _setter("display_name", display_name)
        if is_unlimited is not None:
            _setter("is_unlimited", is_unlimited)
        if key is not None:
            _setter("key", key)
        if lifecycle_details is not None:
            _setter("lifecycle_details", lifecycle_details)
        if state is not None:
            _setter("state", state)
        if time_created is not None:
            _setter("time_created", time_created)
        if time_expires is not None:
            _setter("time_expires", time_expires)
        if time_updated is not None:
            _setter("time_updated", time_updated)

    @property
    @pulumi.getter(name="allowedKeyInstallCount")
    def allowed_key_install_count(self) -> Optional[pulumi.Input[int]]:
        """
        Total number of install for this keys
        """
        return pulumi.get(self, "allowed_key_install_count")

    @allowed_key_install_count.setter
    def allowed_key_install_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "allowed_key_install_count", value)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        Compartment Identifier
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="createdByPrincipalId")
    def created_by_principal_id(self) -> Optional[pulumi.Input[str]]:
        """
        Principal id of user who created the Agent Install key
        """
        return pulumi.get(self, "created_by_principal_id")

    @created_by_principal_id.setter
    def created_by_principal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by_principal_id", value)

    @property
    @pulumi.getter(name="currentKeyInstallCount")
    def current_key_install_count(self) -> Optional[pulumi.Input[int]]:
        """
        Total number of install for this keys
        """
        return pulumi.get(self, "current_key_install_count")

    @current_key_install_count.setter
    def current_key_install_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "current_key_install_count", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Management Agent install Key Name
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="isUnlimited")
    def is_unlimited(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to true, the install key has no expiration date or usage limit. Defaults to false
        """
        return pulumi.get(self, "is_unlimited")

    @is_unlimited.setter
    def is_unlimited(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_unlimited", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        Management Agent Install Key
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> Optional[pulumi.Input[str]]:
        """
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @lifecycle_details.setter
    def lifecycle_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_details", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        Status of Key
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The time when Management Agent install Key was created. An RFC3339 formatted date time string
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="timeExpires")
    def time_expires(self) -> Optional[pulumi.Input[str]]:
        """
        date after which key would expire after creation


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "time_expires")

    @time_expires.setter
    def time_expires(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_expires", value)

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> Optional[pulumi.Input[str]]:
        """
        The time when Management Agent install Key was updated. An RFC3339 formatted date time string
        """
        return pulumi.get(self, "time_updated")

    @time_updated.setter
    def time_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_updated", value)


class ManagementAgentInstallKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_key_install_count: Optional[pulumi.Input[int]] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 is_unlimited: Optional[pulumi.Input[bool]] = None,
                 time_expires: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Management Agent Install Key resource in Oracle Cloud Infrastructure Management Agent service.

        User creates a new install key as part of this API.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_management_agent_install_key = oci.management_agent.ManagementAgentInstallKey("testManagementAgentInstallKey",
            compartment_id=var["compartment_id"],
            display_name=var["management_agent_install_key_display_name"],
            allowed_key_install_count=var["management_agent_install_key_allowed_key_install_count"],
            is_unlimited=var["management_agent_install_key_is_unlimited"],
            time_expires=var["management_agent_install_key_time_expires"])
        ```

        ## Import

        ManagementAgentInstallKeys can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:ManagementAgent/managementAgentInstallKey:ManagementAgentInstallKey test_management_agent_install_key "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] allowed_key_install_count: Total number of install for this keys
        :param pulumi.Input[str] compartment_id: Compartment Identifier
        :param pulumi.Input[str] display_name: (Updatable) Management Agent install Key Name
        :param pulumi.Input[bool] is_unlimited: If set to true, the install key has no expiration date or usage limit. Defaults to false
        :param pulumi.Input[str] time_expires: date after which key would expire after creation
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagementAgentInstallKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Management Agent Install Key resource in Oracle Cloud Infrastructure Management Agent service.

        User creates a new install key as part of this API.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_management_agent_install_key = oci.management_agent.ManagementAgentInstallKey("testManagementAgentInstallKey",
            compartment_id=var["compartment_id"],
            display_name=var["management_agent_install_key_display_name"],
            allowed_key_install_count=var["management_agent_install_key_allowed_key_install_count"],
            is_unlimited=var["management_agent_install_key_is_unlimited"],
            time_expires=var["management_agent_install_key_time_expires"])
        ```

        ## Import

        ManagementAgentInstallKeys can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:ManagementAgent/managementAgentInstallKey:ManagementAgentInstallKey test_management_agent_install_key "id"
        ```

        :param str resource_name: The name of the resource.
        :param ManagementAgentInstallKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagementAgentInstallKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ManagementAgentInstallKeyArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_key_install_count: Optional[pulumi.Input[int]] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 is_unlimited: Optional[pulumi.Input[bool]] = None,
                 time_expires: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ManagementAgentInstallKeyArgs.__new__(ManagementAgentInstallKeyArgs)

            __props__.__dict__["allowed_key_install_count"] = allowed_key_install_count
            if compartment_id is None and not opts.urn:
                raise TypeError("Missing required property 'compartment_id'")
            __props__.__dict__["compartment_id"] = compartment_id
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["is_unlimited"] = is_unlimited
            __props__.__dict__["time_expires"] = time_expires
            __props__.__dict__["created_by_principal_id"] = None
            __props__.__dict__["current_key_install_count"] = None
            __props__.__dict__["key"] = None
            __props__.__dict__["lifecycle_details"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["time_created"] = None
            __props__.__dict__["time_updated"] = None
        super(ManagementAgentInstallKey, __self__).__init__(
            'oci:ManagementAgent/managementAgentInstallKey:ManagementAgentInstallKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allowed_key_install_count: Optional[pulumi.Input[int]] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            created_by_principal_id: Optional[pulumi.Input[str]] = None,
            current_key_install_count: Optional[pulumi.Input[int]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            is_unlimited: Optional[pulumi.Input[bool]] = None,
            key: Optional[pulumi.Input[str]] = None,
            lifecycle_details: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            time_expires: Optional[pulumi.Input[str]] = None,
            time_updated: Optional[pulumi.Input[str]] = None) -> 'ManagementAgentInstallKey':
        """
        Get an existing ManagementAgentInstallKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] allowed_key_install_count: Total number of install for this keys
        :param pulumi.Input[str] compartment_id: Compartment Identifier
        :param pulumi.Input[str] created_by_principal_id: Principal id of user who created the Agent Install key
        :param pulumi.Input[int] current_key_install_count: Total number of install for this keys
        :param pulumi.Input[str] display_name: (Updatable) Management Agent install Key Name
        :param pulumi.Input[bool] is_unlimited: If set to true, the install key has no expiration date or usage limit. Defaults to false
        :param pulumi.Input[str] key: Management Agent Install Key
        :param pulumi.Input[str] lifecycle_details: A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        :param pulumi.Input[str] state: Status of Key
        :param pulumi.Input[str] time_created: The time when Management Agent install Key was created. An RFC3339 formatted date time string
        :param pulumi.Input[str] time_expires: date after which key would expire after creation
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] time_updated: The time when Management Agent install Key was updated. An RFC3339 formatted date time string
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ManagementAgentInstallKeyState.__new__(_ManagementAgentInstallKeyState)

        __props__.__dict__["allowed_key_install_count"] = allowed_key_install_count
        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["created_by_principal_id"] = created_by_principal_id
        __props__.__dict__["current_key_install_count"] = current_key_install_count
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["is_unlimited"] = is_unlimited
        __props__.__dict__["key"] = key
        __props__.__dict__["lifecycle_details"] = lifecycle_details
        __props__.__dict__["state"] = state
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["time_expires"] = time_expires
        __props__.__dict__["time_updated"] = time_updated
        return ManagementAgentInstallKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowedKeyInstallCount")
    def allowed_key_install_count(self) -> pulumi.Output[int]:
        """
        Total number of install for this keys
        """
        return pulumi.get(self, "allowed_key_install_count")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        Compartment Identifier
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="createdByPrincipalId")
    def created_by_principal_id(self) -> pulumi.Output[str]:
        """
        Principal id of user who created the Agent Install key
        """
        return pulumi.get(self, "created_by_principal_id")

    @property
    @pulumi.getter(name="currentKeyInstallCount")
    def current_key_install_count(self) -> pulumi.Output[int]:
        """
        Total number of install for this keys
        """
        return pulumi.get(self, "current_key_install_count")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        (Updatable) Management Agent install Key Name
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="isUnlimited")
    def is_unlimited(self) -> pulumi.Output[bool]:
        """
        If set to true, the install key has no expiration date or usage limit. Defaults to false
        """
        return pulumi.get(self, "is_unlimited")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        Management Agent Install Key
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> pulumi.Output[str]:
        """
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        Status of Key
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The time when Management Agent install Key was created. An RFC3339 formatted date time string
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeExpires")
    def time_expires(self) -> pulumi.Output[str]:
        """
        date after which key would expire after creation


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "time_expires")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> pulumi.Output[str]:
        """
        The time when Management Agent install Key was updated. An RFC3339 formatted date time string
        """
        return pulumi.get(self, "time_updated")

