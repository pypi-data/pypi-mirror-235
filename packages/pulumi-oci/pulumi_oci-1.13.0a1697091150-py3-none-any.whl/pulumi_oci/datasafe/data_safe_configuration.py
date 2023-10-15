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

__all__ = ['DataSafeConfigurationArgs', 'DataSafeConfiguration']

@pulumi.input_type
class DataSafeConfigurationArgs:
    def __init__(__self__, *,
                 is_enabled: pulumi.Input[bool],
                 compartment_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DataSafeConfiguration resource.
        :param pulumi.Input[bool] is_enabled: (Updatable) Indicates if Data Safe is enabled.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] compartment_id: (Updatable) A filter to return only resources that match the specified compartment OCID.
        """
        DataSafeConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            is_enabled=is_enabled,
            compartment_id=compartment_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             is_enabled: pulumi.Input[bool],
             compartment_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("is_enabled", is_enabled)
        if compartment_id is not None:
            _setter("compartment_id", compartment_id)

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Input[bool]:
        """
        (Updatable) Indicates if Data Safe is enabled.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "is_enabled")

    @is_enabled.setter
    def is_enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "is_enabled", value)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) A filter to return only resources that match the specified compartment OCID.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)


@pulumi.input_type
class _DataSafeConfigurationState:
    def __init__(__self__, *,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 data_safe_nat_gateway_ip_address: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 global_settings: Optional[pulumi.Input[Sequence[pulumi.Input['DataSafeConfigurationGlobalSettingArgs']]]] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 time_enabled: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DataSafeConfiguration resources.
        :param pulumi.Input[str] compartment_id: (Updatable) A filter to return only resources that match the specified compartment OCID.
        :param pulumi.Input[str] data_safe_nat_gateway_ip_address: The Oracle Data Safe's NAT Gateway IP Address.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)  Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)  Example: `{"Department": "Finance"}`
        :param pulumi.Input[Sequence[pulumi.Input['DataSafeConfigurationGlobalSettingArgs']]] global_settings: Details of the tenancy level global settings in Data Safe.
        :param pulumi.Input[bool] is_enabled: (Updatable) Indicates if Data Safe is enabled.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] state: The current state of Data Safe.
        :param pulumi.Input[str] time_enabled: The date and time Data Safe was enabled, in the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339).
        :param pulumi.Input[str] url: The URL of the Data Safe service.
        """
        _DataSafeConfigurationState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            compartment_id=compartment_id,
            data_safe_nat_gateway_ip_address=data_safe_nat_gateway_ip_address,
            defined_tags=defined_tags,
            freeform_tags=freeform_tags,
            global_settings=global_settings,
            is_enabled=is_enabled,
            state=state,
            time_enabled=time_enabled,
            url=url,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             compartment_id: Optional[pulumi.Input[str]] = None,
             data_safe_nat_gateway_ip_address: Optional[pulumi.Input[str]] = None,
             defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             global_settings: Optional[pulumi.Input[Sequence[pulumi.Input['DataSafeConfigurationGlobalSettingArgs']]]] = None,
             is_enabled: Optional[pulumi.Input[bool]] = None,
             state: Optional[pulumi.Input[str]] = None,
             time_enabled: Optional[pulumi.Input[str]] = None,
             url: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if compartment_id is not None:
            _setter("compartment_id", compartment_id)
        if data_safe_nat_gateway_ip_address is not None:
            _setter("data_safe_nat_gateway_ip_address", data_safe_nat_gateway_ip_address)
        if defined_tags is not None:
            _setter("defined_tags", defined_tags)
        if freeform_tags is not None:
            _setter("freeform_tags", freeform_tags)
        if global_settings is not None:
            _setter("global_settings", global_settings)
        if is_enabled is not None:
            _setter("is_enabled", is_enabled)
        if state is not None:
            _setter("state", state)
        if time_enabled is not None:
            _setter("time_enabled", time_enabled)
        if url is not None:
            _setter("url", url)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) A filter to return only resources that match the specified compartment OCID.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="dataSafeNatGatewayIpAddress")
    def data_safe_nat_gateway_ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The Oracle Data Safe's NAT Gateway IP Address.
        """
        return pulumi.get(self, "data_safe_nat_gateway_ip_address")

    @data_safe_nat_gateway_ip_address.setter
    def data_safe_nat_gateway_ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_safe_nat_gateway_ip_address", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="globalSettings")
    def global_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataSafeConfigurationGlobalSettingArgs']]]]:
        """
        Details of the tenancy level global settings in Data Safe.
        """
        return pulumi.get(self, "global_settings")

    @global_settings.setter
    def global_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataSafeConfigurationGlobalSettingArgs']]]]):
        pulumi.set(self, "global_settings", value)

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Indicates if Data Safe is enabled.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "is_enabled")

    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_enabled", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current state of Data Safe.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="timeEnabled")
    def time_enabled(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time Data Safe was enabled, in the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339).
        """
        return pulumi.get(self, "time_enabled")

    @time_enabled.setter
    def time_enabled(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_enabled", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of the Data Safe service.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class DataSafeConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        This resource provides the Data Safe Configuration resource in Oracle Cloud Infrastructure Data Safe service.

        Enables Data Safe in the tenancy and region.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_data_safe_configuration = oci.data_safe.DataSafeConfiguration("testDataSafeConfiguration",
            is_enabled=var["data_safe_configuration_is_enabled"],
            compartment_id=var["compartment_id"])
        ```

        ## Import

        Import is not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: (Updatable) A filter to return only resources that match the specified compartment OCID.
        :param pulumi.Input[bool] is_enabled: (Updatable) Indicates if Data Safe is enabled.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DataSafeConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Data Safe Configuration resource in Oracle Cloud Infrastructure Data Safe service.

        Enables Data Safe in the tenancy and region.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_data_safe_configuration = oci.data_safe.DataSafeConfiguration("testDataSafeConfiguration",
            is_enabled=var["data_safe_configuration_is_enabled"],
            compartment_id=var["compartment_id"])
        ```

        ## Import

        Import is not supported for this resource.

        :param str resource_name: The name of the resource.
        :param DataSafeConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DataSafeConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DataSafeConfigurationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DataSafeConfigurationArgs.__new__(DataSafeConfigurationArgs)

            __props__.__dict__["compartment_id"] = compartment_id
            if is_enabled is None and not opts.urn:
                raise TypeError("Missing required property 'is_enabled'")
            __props__.__dict__["is_enabled"] = is_enabled
            __props__.__dict__["data_safe_nat_gateway_ip_address"] = None
            __props__.__dict__["defined_tags"] = None
            __props__.__dict__["freeform_tags"] = None
            __props__.__dict__["global_settings"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["time_enabled"] = None
            __props__.__dict__["url"] = None
        super(DataSafeConfiguration, __self__).__init__(
            'oci:DataSafe/dataSafeConfiguration:DataSafeConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            data_safe_nat_gateway_ip_address: Optional[pulumi.Input[str]] = None,
            defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            global_settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataSafeConfigurationGlobalSettingArgs']]]]] = None,
            is_enabled: Optional[pulumi.Input[bool]] = None,
            state: Optional[pulumi.Input[str]] = None,
            time_enabled: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'DataSafeConfiguration':
        """
        Get an existing DataSafeConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: (Updatable) A filter to return only resources that match the specified compartment OCID.
        :param pulumi.Input[str] data_safe_nat_gateway_ip_address: The Oracle Data Safe's NAT Gateway IP Address.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)  Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)  Example: `{"Department": "Finance"}`
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataSafeConfigurationGlobalSettingArgs']]]] global_settings: Details of the tenancy level global settings in Data Safe.
        :param pulumi.Input[bool] is_enabled: (Updatable) Indicates if Data Safe is enabled.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] state: The current state of Data Safe.
        :param pulumi.Input[str] time_enabled: The date and time Data Safe was enabled, in the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339).
        :param pulumi.Input[str] url: The URL of the Data Safe service.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DataSafeConfigurationState.__new__(_DataSafeConfigurationState)

        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["data_safe_nat_gateway_ip_address"] = data_safe_nat_gateway_ip_address
        __props__.__dict__["defined_tags"] = defined_tags
        __props__.__dict__["freeform_tags"] = freeform_tags
        __props__.__dict__["global_settings"] = global_settings
        __props__.__dict__["is_enabled"] = is_enabled
        __props__.__dict__["state"] = state
        __props__.__dict__["time_enabled"] = time_enabled
        __props__.__dict__["url"] = url
        return DataSafeConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        (Updatable) A filter to return only resources that match the specified compartment OCID.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="dataSafeNatGatewayIpAddress")
    def data_safe_nat_gateway_ip_address(self) -> pulumi.Output[str]:
        """
        The Oracle Data Safe's NAT Gateway IP Address.
        """
        return pulumi.get(self, "data_safe_nat_gateway_ip_address")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="globalSettings")
    def global_settings(self) -> pulumi.Output[Sequence['outputs.DataSafeConfigurationGlobalSetting']]:
        """
        Details of the tenancy level global settings in Data Safe.
        """
        return pulumi.get(self, "global_settings")

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Output[bool]:
        """
        (Updatable) Indicates if Data Safe is enabled.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "is_enabled")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of Data Safe.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeEnabled")
    def time_enabled(self) -> pulumi.Output[str]:
        """
        The date and time Data Safe was enabled, in the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339).
        """
        return pulumi.get(self, "time_enabled")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        The URL of the Data Safe service.
        """
        return pulumi.get(self, "url")

