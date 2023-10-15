# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ConfigurationArgs', 'Configuration']

@pulumi.input_type
class ConfigurationArgs:
    def __init__(__self__, *,
                 compartment_id: pulumi.Input[str],
                 email_ids: pulumi.Input[Sequence[pulumi.Input[str]]]):
        """
        The set of arguments for constructing a Configuration resource.
        :param pulumi.Input[str] compartment_id: (Updatable) The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) used for the license record, product license, and configuration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] email_ids: (Updatable) List of email IDs associated with the configuration.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            compartment_id=compartment_id,
            email_ids=email_ids,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             compartment_id: pulumi.Input[str],
             email_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("compartment_id", compartment_id)
        _setter("email_ids", email_ids)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Input[str]:
        """
        (Updatable) The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) used for the license record, product license, and configuration.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="emailIds")
    def email_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        (Updatable) List of email IDs associated with the configuration.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "email_ids")

    @email_ids.setter
    def email_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "email_ids", value)


@pulumi.input_type
class _ConfigurationState:
    def __init__(__self__, *,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 email_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 time_updated: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Configuration resources.
        :param pulumi.Input[str] compartment_id: (Updatable) The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) used for the license record, product license, and configuration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] email_ids: (Updatable) List of email IDs associated with the configuration.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] time_created: The time the configuration was created. An [RFC 3339](https://tools.ietf.org/html/rfc3339)-formatted datetime string.
        :param pulumi.Input[str] time_updated: The time the configuration was updated. An [RFC 3339](https://tools.ietf.org/html/rfc3339)-formatted datetime string.
        """
        _ConfigurationState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            compartment_id=compartment_id,
            email_ids=email_ids,
            time_created=time_created,
            time_updated=time_updated,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             compartment_id: Optional[pulumi.Input[str]] = None,
             email_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             time_created: Optional[pulumi.Input[str]] = None,
             time_updated: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if compartment_id is not None:
            _setter("compartment_id", compartment_id)
        if email_ids is not None:
            _setter("email_ids", email_ids)
        if time_created is not None:
            _setter("time_created", time_created)
        if time_updated is not None:
            _setter("time_updated", time_updated)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) used for the license record, product license, and configuration.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="emailIds")
    def email_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        (Updatable) List of email IDs associated with the configuration.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "email_ids")

    @email_ids.setter
    def email_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "email_ids", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The time the configuration was created. An [RFC 3339](https://tools.ietf.org/html/rfc3339)-formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> Optional[pulumi.Input[str]]:
        """
        The time the configuration was updated. An [RFC 3339](https://tools.ietf.org/html/rfc3339)-formatted datetime string.
        """
        return pulumi.get(self, "time_updated")

    @time_updated.setter
    def time_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_updated", value)


class Configuration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 email_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        This resource provides the Configuration resource in Oracle Cloud Infrastructure License Manager service.

        Updates the configuration for the compartment.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_configuration = oci.license_manager.Configuration("testConfiguration",
            compartment_id=var["compartment_id"],
            email_ids=var["configuration_email_ids"])
        ```

        ## Import

        Configurations can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:LicenseManager/configuration:Configuration test_configuration "configuration/compartmentId/{compartmentId}"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: (Updatable) The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) used for the license record, product license, and configuration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] email_ids: (Updatable) List of email IDs associated with the configuration.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Configuration resource in Oracle Cloud Infrastructure License Manager service.

        Updates the configuration for the compartment.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_configuration = oci.license_manager.Configuration("testConfiguration",
            compartment_id=var["compartment_id"],
            email_ids=var["configuration_email_ids"])
        ```

        ## Import

        Configurations can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:LicenseManager/configuration:Configuration test_configuration "configuration/compartmentId/{compartmentId}"
        ```

        :param str resource_name: The name of the resource.
        :param ConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ConfigurationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 email_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConfigurationArgs.__new__(ConfigurationArgs)

            if compartment_id is None and not opts.urn:
                raise TypeError("Missing required property 'compartment_id'")
            __props__.__dict__["compartment_id"] = compartment_id
            if email_ids is None and not opts.urn:
                raise TypeError("Missing required property 'email_ids'")
            __props__.__dict__["email_ids"] = email_ids
            __props__.__dict__["time_created"] = None
            __props__.__dict__["time_updated"] = None
        super(Configuration, __self__).__init__(
            'oci:LicenseManager/configuration:Configuration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            email_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            time_updated: Optional[pulumi.Input[str]] = None) -> 'Configuration':
        """
        Get an existing Configuration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: (Updatable) The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) used for the license record, product license, and configuration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] email_ids: (Updatable) List of email IDs associated with the configuration.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] time_created: The time the configuration was created. An [RFC 3339](https://tools.ietf.org/html/rfc3339)-formatted datetime string.
        :param pulumi.Input[str] time_updated: The time the configuration was updated. An [RFC 3339](https://tools.ietf.org/html/rfc3339)-formatted datetime string.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConfigurationState.__new__(_ConfigurationState)

        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["email_ids"] = email_ids
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["time_updated"] = time_updated
        return Configuration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        (Updatable) The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) used for the license record, product license, and configuration.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="emailIds")
    def email_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        (Updatable) List of email IDs associated with the configuration.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "email_ids")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The time the configuration was created. An [RFC 3339](https://tools.ietf.org/html/rfc3339)-formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> pulumi.Output[str]:
        """
        The time the configuration was updated. An [RFC 3339](https://tools.ietf.org/html/rfc3339)-formatted datetime string.
        """
        return pulumi.get(self, "time_updated")

