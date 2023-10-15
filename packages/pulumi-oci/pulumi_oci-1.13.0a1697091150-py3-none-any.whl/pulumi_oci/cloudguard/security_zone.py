# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SecurityZoneArgs', 'SecurityZone']

@pulumi.input_type
class SecurityZoneArgs:
    def __init__(__self__, *,
                 compartment_id: pulumi.Input[str],
                 display_name: pulumi.Input[str],
                 security_zone_recipe_id: pulumi.Input[str],
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a SecurityZone resource.
        :param pulumi.Input[str] compartment_id: (Updatable) The OCID of the compartment for the security zone
        :param pulumi.Input[str] display_name: (Updatable) The security zone's name
        :param pulumi.Input[str] security_zone_recipe_id: (Updatable) The OCID of the recipe (`SecurityRecipe`) for the security zone
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) The security zone's description
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
               
               Avoid entering confidential information.
        """
        SecurityZoneArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            compartment_id=compartment_id,
            display_name=display_name,
            security_zone_recipe_id=security_zone_recipe_id,
            defined_tags=defined_tags,
            description=description,
            freeform_tags=freeform_tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             compartment_id: pulumi.Input[str],
             display_name: pulumi.Input[str],
             security_zone_recipe_id: pulumi.Input[str],
             defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             description: Optional[pulumi.Input[str]] = None,
             freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("compartment_id", compartment_id)
        _setter("display_name", display_name)
        _setter("security_zone_recipe_id", security_zone_recipe_id)
        if defined_tags is not None:
            _setter("defined_tags", defined_tags)
        if description is not None:
            _setter("description", description)
        if freeform_tags is not None:
            _setter("freeform_tags", freeform_tags)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Input[str]:
        """
        (Updatable) The OCID of the compartment for the security zone
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        (Updatable) The security zone's name
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="securityZoneRecipeId")
    def security_zone_recipe_id(self) -> pulumi.Input[str]:
        """
        (Updatable) The OCID of the recipe (`SecurityRecipe`) for the security zone


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "security_zone_recipe_id")

    @security_zone_recipe_id.setter
    def security_zone_recipe_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "security_zone_recipe_id", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The security zone's description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`

        Avoid entering confidential information.
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)


@pulumi.input_type
class _SecurityZoneState:
    def __init__(__self__, *,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 inherited_by_compartments: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 lifecycle_details: Optional[pulumi.Input[str]] = None,
                 security_zone_recipe_id: Optional[pulumi.Input[str]] = None,
                 security_zone_target_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 time_updated: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SecurityZone resources.
        :param pulumi.Input[str] compartment_id: (Updatable) The OCID of the compartment for the security zone
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) The security zone's description
        :param pulumi.Input[str] display_name: (Updatable) The security zone's name
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
               
               Avoid entering confidential information.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] inherited_by_compartments: List of inherited compartments
        :param pulumi.Input[str] lifecycle_details: A message describing the current state in more detail. For example, this can be used to provide actionable information for a zone in the `Failed` state.
        :param pulumi.Input[str] security_zone_recipe_id: (Updatable) The OCID of the recipe (`SecurityRecipe`) for the security zone
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] security_zone_target_id: The OCID of the target associated with the security zone
        :param pulumi.Input[str] state: The current state of the security zone
        :param pulumi.Input[str] time_created: The time the security zone was created. An RFC3339 formatted datetime string.
        :param pulumi.Input[str] time_updated: The time the security zone was last updated. An RFC3339 formatted datetime string.
        """
        _SecurityZoneState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            compartment_id=compartment_id,
            defined_tags=defined_tags,
            description=description,
            display_name=display_name,
            freeform_tags=freeform_tags,
            inherited_by_compartments=inherited_by_compartments,
            lifecycle_details=lifecycle_details,
            security_zone_recipe_id=security_zone_recipe_id,
            security_zone_target_id=security_zone_target_id,
            state=state,
            time_created=time_created,
            time_updated=time_updated,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             compartment_id: Optional[pulumi.Input[str]] = None,
             defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             description: Optional[pulumi.Input[str]] = None,
             display_name: Optional[pulumi.Input[str]] = None,
             freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             inherited_by_compartments: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             lifecycle_details: Optional[pulumi.Input[str]] = None,
             security_zone_recipe_id: Optional[pulumi.Input[str]] = None,
             security_zone_target_id: Optional[pulumi.Input[str]] = None,
             state: Optional[pulumi.Input[str]] = None,
             time_created: Optional[pulumi.Input[str]] = None,
             time_updated: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if compartment_id is not None:
            _setter("compartment_id", compartment_id)
        if defined_tags is not None:
            _setter("defined_tags", defined_tags)
        if description is not None:
            _setter("description", description)
        if display_name is not None:
            _setter("display_name", display_name)
        if freeform_tags is not None:
            _setter("freeform_tags", freeform_tags)
        if inherited_by_compartments is not None:
            _setter("inherited_by_compartments", inherited_by_compartments)
        if lifecycle_details is not None:
            _setter("lifecycle_details", lifecycle_details)
        if security_zone_recipe_id is not None:
            _setter("security_zone_recipe_id", security_zone_recipe_id)
        if security_zone_target_id is not None:
            _setter("security_zone_target_id", security_zone_target_id)
        if state is not None:
            _setter("state", state)
        if time_created is not None:
            _setter("time_created", time_created)
        if time_updated is not None:
            _setter("time_updated", time_updated)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The OCID of the compartment for the security zone
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The security zone's description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The security zone's name
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`

        Avoid entering confidential information.
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="inheritedByCompartments")
    def inherited_by_compartments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of inherited compartments
        """
        return pulumi.get(self, "inherited_by_compartments")

    @inherited_by_compartments.setter
    def inherited_by_compartments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "inherited_by_compartments", value)

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> Optional[pulumi.Input[str]]:
        """
        A message describing the current state in more detail. For example, this can be used to provide actionable information for a zone in the `Failed` state.
        """
        return pulumi.get(self, "lifecycle_details")

    @lifecycle_details.setter
    def lifecycle_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_details", value)

    @property
    @pulumi.getter(name="securityZoneRecipeId")
    def security_zone_recipe_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The OCID of the recipe (`SecurityRecipe`) for the security zone


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "security_zone_recipe_id")

    @security_zone_recipe_id.setter
    def security_zone_recipe_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_zone_recipe_id", value)

    @property
    @pulumi.getter(name="securityZoneTargetId")
    def security_zone_target_id(self) -> Optional[pulumi.Input[str]]:
        """
        The OCID of the target associated with the security zone
        """
        return pulumi.get(self, "security_zone_target_id")

    @security_zone_target_id.setter
    def security_zone_target_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_zone_target_id", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current state of the security zone
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The time the security zone was created. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> Optional[pulumi.Input[str]]:
        """
        The time the security zone was last updated. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_updated")

    @time_updated.setter
    def time_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_updated", value)


class SecurityZone(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 security_zone_recipe_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Security Zone resource in Oracle Cloud Infrastructure Cloud Guard service.

        Creates a security zone for a compartment. A security zone enforces all security zone policies in a given security zone recipe. Any actions that violate a policy are denied. By default, any subcompartments are also in the same security zone.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_security_zone = oci.cloud_guard.SecurityZone("testSecurityZone",
            compartment_id=var["compartment_id"],
            display_name=var["security_zone_display_name"],
            security_zone_recipe_id=oci_cloud_guard_security_zone_recipe["test_security_zone_recipe"]["id"],
            defined_tags={
                "foo-namespace.bar-key": "value",
            },
            description=var["security_zone_description"],
            freeform_tags={
                "bar-key": "value",
            })
        ```

        ## Import

        SecurityZones can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:CloudGuard/securityZone:SecurityZone test_security_zone "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: (Updatable) The OCID of the compartment for the security zone
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) The security zone's description
        :param pulumi.Input[str] display_name: (Updatable) The security zone's name
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
               
               Avoid entering confidential information.
        :param pulumi.Input[str] security_zone_recipe_id: (Updatable) The OCID of the recipe (`SecurityRecipe`) for the security zone
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecurityZoneArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Security Zone resource in Oracle Cloud Infrastructure Cloud Guard service.

        Creates a security zone for a compartment. A security zone enforces all security zone policies in a given security zone recipe. Any actions that violate a policy are denied. By default, any subcompartments are also in the same security zone.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_security_zone = oci.cloud_guard.SecurityZone("testSecurityZone",
            compartment_id=var["compartment_id"],
            display_name=var["security_zone_display_name"],
            security_zone_recipe_id=oci_cloud_guard_security_zone_recipe["test_security_zone_recipe"]["id"],
            defined_tags={
                "foo-namespace.bar-key": "value",
            },
            description=var["security_zone_description"],
            freeform_tags={
                "bar-key": "value",
            })
        ```

        ## Import

        SecurityZones can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:CloudGuard/securityZone:SecurityZone test_security_zone "id"
        ```

        :param str resource_name: The name of the resource.
        :param SecurityZoneArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecurityZoneArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            SecurityZoneArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 security_zone_recipe_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SecurityZoneArgs.__new__(SecurityZoneArgs)

            if compartment_id is None and not opts.urn:
                raise TypeError("Missing required property 'compartment_id'")
            __props__.__dict__["compartment_id"] = compartment_id
            __props__.__dict__["defined_tags"] = defined_tags
            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["freeform_tags"] = freeform_tags
            if security_zone_recipe_id is None and not opts.urn:
                raise TypeError("Missing required property 'security_zone_recipe_id'")
            __props__.__dict__["security_zone_recipe_id"] = security_zone_recipe_id
            __props__.__dict__["inherited_by_compartments"] = None
            __props__.__dict__["lifecycle_details"] = None
            __props__.__dict__["security_zone_target_id"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["time_created"] = None
            __props__.__dict__["time_updated"] = None
        super(SecurityZone, __self__).__init__(
            'oci:CloudGuard/securityZone:SecurityZone',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            inherited_by_compartments: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            lifecycle_details: Optional[pulumi.Input[str]] = None,
            security_zone_recipe_id: Optional[pulumi.Input[str]] = None,
            security_zone_target_id: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            time_updated: Optional[pulumi.Input[str]] = None) -> 'SecurityZone':
        """
        Get an existing SecurityZone resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: (Updatable) The OCID of the compartment for the security zone
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) The security zone's description
        :param pulumi.Input[str] display_name: (Updatable) The security zone's name
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
               
               Avoid entering confidential information.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] inherited_by_compartments: List of inherited compartments
        :param pulumi.Input[str] lifecycle_details: A message describing the current state in more detail. For example, this can be used to provide actionable information for a zone in the `Failed` state.
        :param pulumi.Input[str] security_zone_recipe_id: (Updatable) The OCID of the recipe (`SecurityRecipe`) for the security zone
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] security_zone_target_id: The OCID of the target associated with the security zone
        :param pulumi.Input[str] state: The current state of the security zone
        :param pulumi.Input[str] time_created: The time the security zone was created. An RFC3339 formatted datetime string.
        :param pulumi.Input[str] time_updated: The time the security zone was last updated. An RFC3339 formatted datetime string.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SecurityZoneState.__new__(_SecurityZoneState)

        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["defined_tags"] = defined_tags
        __props__.__dict__["description"] = description
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["freeform_tags"] = freeform_tags
        __props__.__dict__["inherited_by_compartments"] = inherited_by_compartments
        __props__.__dict__["lifecycle_details"] = lifecycle_details
        __props__.__dict__["security_zone_recipe_id"] = security_zone_recipe_id
        __props__.__dict__["security_zone_target_id"] = security_zone_target_id
        __props__.__dict__["state"] = state
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["time_updated"] = time_updated
        return SecurityZone(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        (Updatable) The OCID of the compartment for the security zone
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        (Updatable) The security zone's description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        (Updatable) The security zone's name
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`

        Avoid entering confidential information.
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="inheritedByCompartments")
    def inherited_by_compartments(self) -> pulumi.Output[Sequence[str]]:
        """
        List of inherited compartments
        """
        return pulumi.get(self, "inherited_by_compartments")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> pulumi.Output[str]:
        """
        A message describing the current state in more detail. For example, this can be used to provide actionable information for a zone in the `Failed` state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="securityZoneRecipeId")
    def security_zone_recipe_id(self) -> pulumi.Output[str]:
        """
        (Updatable) The OCID of the recipe (`SecurityRecipe`) for the security zone


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "security_zone_recipe_id")

    @property
    @pulumi.getter(name="securityZoneTargetId")
    def security_zone_target_id(self) -> pulumi.Output[str]:
        """
        The OCID of the target associated with the security zone
        """
        return pulumi.get(self, "security_zone_target_id")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of the security zone
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The time the security zone was created. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> pulumi.Output[str]:
        """
        The time the security zone was last updated. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_updated")

