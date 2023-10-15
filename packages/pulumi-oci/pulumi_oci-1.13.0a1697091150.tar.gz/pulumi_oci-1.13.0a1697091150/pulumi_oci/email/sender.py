# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SenderArgs', 'Sender']

@pulumi.input_type
class SenderArgs:
    def __init__(__self__, *,
                 compartment_id: pulumi.Input[str],
                 email_address: pulumi.Input[str],
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a Sender resource.
        :param pulumi.Input[str] compartment_id: (Updatable) The OCID of the compartment that contains the sender.
        :param pulumi.Input[str] email_address: The email address of the sender.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        SenderArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            compartment_id=compartment_id,
            email_address=email_address,
            defined_tags=defined_tags,
            freeform_tags=freeform_tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             compartment_id: pulumi.Input[str],
             email_address: pulumi.Input[str],
             defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("compartment_id", compartment_id)
        _setter("email_address", email_address)
        if defined_tags is not None:
            _setter("defined_tags", defined_tags)
        if freeform_tags is not None:
            _setter("freeform_tags", freeform_tags)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Input[str]:
        """
        (Updatable) The OCID of the compartment that contains the sender.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> pulumi.Input[str]:
        """
        The email address of the sender.
        """
        return pulumi.get(self, "email_address")

    @email_address.setter
    def email_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "email_address", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}` 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)


@pulumi.input_type
class _SenderState:
    def __init__(__self__, *,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 email_address: Optional[pulumi.Input[str]] = None,
                 email_domain_id: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 is_spf: Optional[pulumi.Input[bool]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 time_created: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Sender resources.
        :param pulumi.Input[str] compartment_id: (Updatable) The OCID of the compartment that contains the sender.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] email_address: The email address of the sender.
        :param pulumi.Input[str] email_domain_id: The email domain used to assert responsibility for emails sent from this sender.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[bool] is_spf: Value of the SPF field. For more information about SPF, please see [SPF Authentication](https://docs.cloud.oracle.com/iaas/Content/Email/Concepts/overview.htm#components).
        :param pulumi.Input[str] state: The current status of the approved sender.
        :param pulumi.Input[str] time_created: The date and time the approved sender was added in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.
        """
        _SenderState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            compartment_id=compartment_id,
            defined_tags=defined_tags,
            email_address=email_address,
            email_domain_id=email_domain_id,
            freeform_tags=freeform_tags,
            is_spf=is_spf,
            state=state,
            time_created=time_created,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             compartment_id: Optional[pulumi.Input[str]] = None,
             defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             email_address: Optional[pulumi.Input[str]] = None,
             email_domain_id: Optional[pulumi.Input[str]] = None,
             freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             is_spf: Optional[pulumi.Input[bool]] = None,
             state: Optional[pulumi.Input[str]] = None,
             time_created: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if compartment_id is not None:
            _setter("compartment_id", compartment_id)
        if defined_tags is not None:
            _setter("defined_tags", defined_tags)
        if email_address is not None:
            _setter("email_address", email_address)
        if email_domain_id is not None:
            _setter("email_domain_id", email_domain_id)
        if freeform_tags is not None:
            _setter("freeform_tags", freeform_tags)
        if is_spf is not None:
            _setter("is_spf", is_spf)
        if state is not None:
            _setter("state", state)
        if time_created is not None:
            _setter("time_created", time_created)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The OCID of the compartment that contains the sender.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[pulumi.Input[str]]:
        """
        The email address of the sender.
        """
        return pulumi.get(self, "email_address")

    @email_address.setter
    def email_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email_address", value)

    @property
    @pulumi.getter(name="emailDomainId")
    def email_domain_id(self) -> Optional[pulumi.Input[str]]:
        """
        The email domain used to assert responsibility for emails sent from this sender.
        """
        return pulumi.get(self, "email_domain_id")

    @email_domain_id.setter
    def email_domain_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email_domain_id", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}` 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="isSpf")
    def is_spf(self) -> Optional[pulumi.Input[bool]]:
        """
        Value of the SPF field. For more information about SPF, please see [SPF Authentication](https://docs.cloud.oracle.com/iaas/Content/Email/Concepts/overview.htm#components).
        """
        return pulumi.get(self, "is_spf")

    @is_spf.setter
    def is_spf(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_spf", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current status of the approved sender.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time the approved sender was added in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)


class Sender(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 email_address: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        """
        This resource provides the Sender resource in Oracle Cloud Infrastructure Email service.

        Creates a sender for a tenancy in a given compartment.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_sender = oci.email.Sender("testSender",
            compartment_id=var["compartment_id"],
            email_address=var["sender_email_address"],
            defined_tags={
                "Operations.CostCenter": "42",
            },
            freeform_tags={
                "Department": "Finance",
            })
        ```

        ## Import

        Senders can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:Email/sender:Sender test_sender "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: (Updatable) The OCID of the compartment that contains the sender.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] email_address: The email address of the sender.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SenderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Sender resource in Oracle Cloud Infrastructure Email service.

        Creates a sender for a tenancy in a given compartment.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_sender = oci.email.Sender("testSender",
            compartment_id=var["compartment_id"],
            email_address=var["sender_email_address"],
            defined_tags={
                "Operations.CostCenter": "42",
            },
            freeform_tags={
                "Department": "Finance",
            })
        ```

        ## Import

        Senders can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:Email/sender:Sender test_sender "id"
        ```

        :param str resource_name: The name of the resource.
        :param SenderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SenderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            SenderArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 email_address: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SenderArgs.__new__(SenderArgs)

            if compartment_id is None and not opts.urn:
                raise TypeError("Missing required property 'compartment_id'")
            __props__.__dict__["compartment_id"] = compartment_id
            __props__.__dict__["defined_tags"] = defined_tags
            if email_address is None and not opts.urn:
                raise TypeError("Missing required property 'email_address'")
            __props__.__dict__["email_address"] = email_address
            __props__.__dict__["freeform_tags"] = freeform_tags
            __props__.__dict__["email_domain_id"] = None
            __props__.__dict__["is_spf"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["time_created"] = None
        super(Sender, __self__).__init__(
            'oci:Email/sender:Sender',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            email_address: Optional[pulumi.Input[str]] = None,
            email_domain_id: Optional[pulumi.Input[str]] = None,
            freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            is_spf: Optional[pulumi.Input[bool]] = None,
            state: Optional[pulumi.Input[str]] = None,
            time_created: Optional[pulumi.Input[str]] = None) -> 'Sender':
        """
        Get an existing Sender resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: (Updatable) The OCID of the compartment that contains the sender.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] email_address: The email address of the sender.
        :param pulumi.Input[str] email_domain_id: The email domain used to assert responsibility for emails sent from this sender.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[bool] is_spf: Value of the SPF field. For more information about SPF, please see [SPF Authentication](https://docs.cloud.oracle.com/iaas/Content/Email/Concepts/overview.htm#components).
        :param pulumi.Input[str] state: The current status of the approved sender.
        :param pulumi.Input[str] time_created: The date and time the approved sender was added in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SenderState.__new__(_SenderState)

        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["defined_tags"] = defined_tags
        __props__.__dict__["email_address"] = email_address
        __props__.__dict__["email_domain_id"] = email_domain_id
        __props__.__dict__["freeform_tags"] = freeform_tags
        __props__.__dict__["is_spf"] = is_spf
        __props__.__dict__["state"] = state
        __props__.__dict__["time_created"] = time_created
        return Sender(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        (Updatable) The OCID of the compartment that contains the sender.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> pulumi.Output[str]:
        """
        The email address of the sender.
        """
        return pulumi.get(self, "email_address")

    @property
    @pulumi.getter(name="emailDomainId")
    def email_domain_id(self) -> pulumi.Output[str]:
        """
        The email domain used to assert responsibility for emails sent from this sender.
        """
        return pulumi.get(self, "email_domain_id")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}` 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="isSpf")
    def is_spf(self) -> pulumi.Output[bool]:
        """
        Value of the SPF field. For more information about SPF, please see [SPF Authentication](https://docs.cloud.oracle.com/iaas/Content/Email/Concepts/overview.htm#components).
        """
        return pulumi.get(self, "is_spf")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current status of the approved sender.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The date and time the approved sender was added in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.
        """
        return pulumi.get(self, "time_created")

