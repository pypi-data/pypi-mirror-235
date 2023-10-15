# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SteeringPolicyAttachmentArgs', 'SteeringPolicyAttachment']

@pulumi.input_type
class SteeringPolicyAttachmentArgs:
    def __init__(__self__, *,
                 domain_name: pulumi.Input[str],
                 steering_policy_id: pulumi.Input[str],
                 zone_id: pulumi.Input[str],
                 display_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SteeringPolicyAttachment resource.
        :param pulumi.Input[str] domain_name: The attached domain within the attached zone. `domain_name` is case insensitive.
        :param pulumi.Input[str] steering_policy_id: The OCID of the attached steering policy.
        :param pulumi.Input[str] zone_id: The OCID of the attached zone.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] display_name: (Updatable) A user-friendly name for the steering policy attachment. Does not have to be unique and can be changed. Avoid entering confidential information.
        """
        SteeringPolicyAttachmentArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            domain_name=domain_name,
            steering_policy_id=steering_policy_id,
            zone_id=zone_id,
            display_name=display_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             domain_name: pulumi.Input[str],
             steering_policy_id: pulumi.Input[str],
             zone_id: pulumi.Input[str],
             display_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("domain_name", domain_name)
        _setter("steering_policy_id", steering_policy_id)
        _setter("zone_id", zone_id)
        if display_name is not None:
            _setter("display_name", display_name)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        The attached domain within the attached zone. `domain_name` is case insensitive.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="steeringPolicyId")
    def steering_policy_id(self) -> pulumi.Input[str]:
        """
        The OCID of the attached steering policy.
        """
        return pulumi.get(self, "steering_policy_id")

    @steering_policy_id.setter
    def steering_policy_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "steering_policy_id", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Input[str]:
        """
        The OCID of the attached zone.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "zone_id", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) A user-friendly name for the steering policy attachment. Does not have to be unique and can be changed. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)


@pulumi.input_type
class _SteeringPolicyAttachmentState:
    def __init__(__self__, *,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 rtypes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 self: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 steering_policy_id: Optional[pulumi.Input[str]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SteeringPolicyAttachment resources.
        :param pulumi.Input[str] compartment_id: The OCID of the compartment containing the steering policy attachment.
        :param pulumi.Input[str] display_name: (Updatable) A user-friendly name for the steering policy attachment. Does not have to be unique and can be changed. Avoid entering confidential information.
        :param pulumi.Input[str] domain_name: The attached domain within the attached zone. `domain_name` is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] rtypes: The record types covered by the attachment at the domain. The set of record types is determined by aggregating the record types from the answers defined in the steering policy.
        :param pulumi.Input[str] self: The canonical absolute URL of the resource.
        :param pulumi.Input[str] state: The current state of the resource.
        :param pulumi.Input[str] steering_policy_id: The OCID of the attached steering policy.
        :param pulumi.Input[str] time_created: The date and time the resource was created, expressed in RFC 3339 timestamp format.
        :param pulumi.Input[str] zone_id: The OCID of the attached zone.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        _SteeringPolicyAttachmentState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            compartment_id=compartment_id,
            display_name=display_name,
            domain_name=domain_name,
            rtypes=rtypes,
            self=self,
            state=state,
            steering_policy_id=steering_policy_id,
            time_created=time_created,
            zone_id=zone_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             compartment_id: Optional[pulumi.Input[str]] = None,
             display_name: Optional[pulumi.Input[str]] = None,
             domain_name: Optional[pulumi.Input[str]] = None,
             rtypes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             self: Optional[pulumi.Input[str]] = None,
             state: Optional[pulumi.Input[str]] = None,
             steering_policy_id: Optional[pulumi.Input[str]] = None,
             time_created: Optional[pulumi.Input[str]] = None,
             zone_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if compartment_id is not None:
            _setter("compartment_id", compartment_id)
        if display_name is not None:
            _setter("display_name", display_name)
        if domain_name is not None:
            _setter("domain_name", domain_name)
        if rtypes is not None:
            _setter("rtypes", rtypes)
        if self is not None:
            _setter("self", self)
        if state is not None:
            _setter("state", state)
        if steering_policy_id is not None:
            _setter("steering_policy_id", steering_policy_id)
        if time_created is not None:
            _setter("time_created", time_created)
        if zone_id is not None:
            _setter("zone_id", zone_id)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The OCID of the compartment containing the steering policy attachment.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) A user-friendly name for the steering policy attachment. Does not have to be unique and can be changed. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        The attached domain within the attached zone. `domain_name` is case insensitive.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter
    def rtypes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The record types covered by the attachment at the domain. The set of record types is determined by aggregating the record types from the answers defined in the steering policy.
        """
        return pulumi.get(self, "rtypes")

    @rtypes.setter
    def rtypes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "rtypes", value)

    @property
    @pulumi.getter
    def self(self) -> Optional[pulumi.Input[str]]:
        """
        The canonical absolute URL of the resource.
        """
        return pulumi.get(self, "self")

    @self.setter
    def self(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "self", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current state of the resource.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="steeringPolicyId")
    def steering_policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        The OCID of the attached steering policy.
        """
        return pulumi.get(self, "steering_policy_id")

    @steering_policy_id.setter
    def steering_policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "steering_policy_id", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time the resource was created, expressed in RFC 3339 timestamp format.
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The OCID of the attached zone.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


class SteeringPolicyAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 steering_policy_id: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Steering Policy Attachment resource in Oracle Cloud Infrastructure DNS service.

        Creates a new attachment between a steering policy and a domain, giving the
        policy permission to answer queries for the specified domain. A steering policy must
        be attached to a domain for the policy to answer DNS queries for that domain.

        For the purposes of access control, the attachment is automatically placed
        into the same compartment as the domain's zone.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_steering_policy_attachment = oci.dns.SteeringPolicyAttachment("testSteeringPolicyAttachment",
            domain_name=var["steering_policy_attachment_domain_name"],
            steering_policy_id=oci_dns_steering_policy["test_steering_policy"]["id"],
            zone_id=oci_dns_zone["test_zone"]["id"],
            display_name=var["steering_policy_attachment_display_name"])
        ```

        ## Import

        SteeringPolicyAttachments can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:Dns/steeringPolicyAttachment:SteeringPolicyAttachment test_steering_policy_attachment "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: (Updatable) A user-friendly name for the steering policy attachment. Does not have to be unique and can be changed. Avoid entering confidential information.
        :param pulumi.Input[str] domain_name: The attached domain within the attached zone. `domain_name` is case insensitive.
        :param pulumi.Input[str] steering_policy_id: The OCID of the attached steering policy.
        :param pulumi.Input[str] zone_id: The OCID of the attached zone.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SteeringPolicyAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Steering Policy Attachment resource in Oracle Cloud Infrastructure DNS service.

        Creates a new attachment between a steering policy and a domain, giving the
        policy permission to answer queries for the specified domain. A steering policy must
        be attached to a domain for the policy to answer DNS queries for that domain.

        For the purposes of access control, the attachment is automatically placed
        into the same compartment as the domain's zone.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_steering_policy_attachment = oci.dns.SteeringPolicyAttachment("testSteeringPolicyAttachment",
            domain_name=var["steering_policy_attachment_domain_name"],
            steering_policy_id=oci_dns_steering_policy["test_steering_policy"]["id"],
            zone_id=oci_dns_zone["test_zone"]["id"],
            display_name=var["steering_policy_attachment_display_name"])
        ```

        ## Import

        SteeringPolicyAttachments can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:Dns/steeringPolicyAttachment:SteeringPolicyAttachment test_steering_policy_attachment "id"
        ```

        :param str resource_name: The name of the resource.
        :param SteeringPolicyAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SteeringPolicyAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            SteeringPolicyAttachmentArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 steering_policy_id: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SteeringPolicyAttachmentArgs.__new__(SteeringPolicyAttachmentArgs)

            __props__.__dict__["display_name"] = display_name
            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            if steering_policy_id is None and not opts.urn:
                raise TypeError("Missing required property 'steering_policy_id'")
            __props__.__dict__["steering_policy_id"] = steering_policy_id
            if zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'zone_id'")
            __props__.__dict__["zone_id"] = zone_id
            __props__.__dict__["compartment_id"] = None
            __props__.__dict__["rtypes"] = None
            __props__.__dict__["self"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["time_created"] = None
        super(SteeringPolicyAttachment, __self__).__init__(
            'oci:Dns/steeringPolicyAttachment:SteeringPolicyAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            domain_name: Optional[pulumi.Input[str]] = None,
            rtypes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            self: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            steering_policy_id: Optional[pulumi.Input[str]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'SteeringPolicyAttachment':
        """
        Get an existing SteeringPolicyAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: The OCID of the compartment containing the steering policy attachment.
        :param pulumi.Input[str] display_name: (Updatable) A user-friendly name for the steering policy attachment. Does not have to be unique and can be changed. Avoid entering confidential information.
        :param pulumi.Input[str] domain_name: The attached domain within the attached zone. `domain_name` is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] rtypes: The record types covered by the attachment at the domain. The set of record types is determined by aggregating the record types from the answers defined in the steering policy.
        :param pulumi.Input[str] self: The canonical absolute URL of the resource.
        :param pulumi.Input[str] state: The current state of the resource.
        :param pulumi.Input[str] steering_policy_id: The OCID of the attached steering policy.
        :param pulumi.Input[str] time_created: The date and time the resource was created, expressed in RFC 3339 timestamp format.
        :param pulumi.Input[str] zone_id: The OCID of the attached zone.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SteeringPolicyAttachmentState.__new__(_SteeringPolicyAttachmentState)

        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["domain_name"] = domain_name
        __props__.__dict__["rtypes"] = rtypes
        __props__.__dict__["self"] = self
        __props__.__dict__["state"] = state
        __props__.__dict__["steering_policy_id"] = steering_policy_id
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["zone_id"] = zone_id
        return SteeringPolicyAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        The OCID of the compartment containing the steering policy attachment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        (Updatable) A user-friendly name for the steering policy attachment. Does not have to be unique and can be changed. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        The attached domain within the attached zone. `domain_name` is case insensitive.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter
    def rtypes(self) -> pulumi.Output[Sequence[str]]:
        """
        The record types covered by the attachment at the domain. The set of record types is determined by aggregating the record types from the answers defined in the steering policy.
        """
        return pulumi.get(self, "rtypes")

    @property
    @pulumi.getter
    def self(self) -> pulumi.Output[str]:
        """
        The canonical absolute URL of the resource.
        """
        return pulumi.get(self, "self")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of the resource.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="steeringPolicyId")
    def steering_policy_id(self) -> pulumi.Output[str]:
        """
        The OCID of the attached steering policy.
        """
        return pulumi.get(self, "steering_policy_id")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The date and time the resource was created, expressed in RFC 3339 timestamp format.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        The OCID of the attached zone.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "zone_id")

