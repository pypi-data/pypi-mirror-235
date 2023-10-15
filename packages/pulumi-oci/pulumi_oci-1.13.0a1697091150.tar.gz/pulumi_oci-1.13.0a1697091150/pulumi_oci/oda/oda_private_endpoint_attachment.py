# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['OdaPrivateEndpointAttachmentArgs', 'OdaPrivateEndpointAttachment']

@pulumi.input_type
class OdaPrivateEndpointAttachmentArgs:
    def __init__(__self__, *,
                 oda_instance_id: pulumi.Input[str],
                 oda_private_endpoint_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a OdaPrivateEndpointAttachment resource.
        :param pulumi.Input[str] oda_instance_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the attached ODA Instance.
        :param pulumi.Input[str] oda_private_endpoint_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the ODA Private Endpoint.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        OdaPrivateEndpointAttachmentArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            oda_instance_id=oda_instance_id,
            oda_private_endpoint_id=oda_private_endpoint_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             oda_instance_id: pulumi.Input[str],
             oda_private_endpoint_id: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("oda_instance_id", oda_instance_id)
        _setter("oda_private_endpoint_id", oda_private_endpoint_id)

    @property
    @pulumi.getter(name="odaInstanceId")
    def oda_instance_id(self) -> pulumi.Input[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the attached ODA Instance.
        """
        return pulumi.get(self, "oda_instance_id")

    @oda_instance_id.setter
    def oda_instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "oda_instance_id", value)

    @property
    @pulumi.getter(name="odaPrivateEndpointId")
    def oda_private_endpoint_id(self) -> pulumi.Input[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the ODA Private Endpoint.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "oda_private_endpoint_id")

    @oda_private_endpoint_id.setter
    def oda_private_endpoint_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "oda_private_endpoint_id", value)


@pulumi.input_type
class _OdaPrivateEndpointAttachmentState:
    def __init__(__self__, *,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 oda_instance_id: Optional[pulumi.Input[str]] = None,
                 oda_private_endpoint_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 time_updated: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering OdaPrivateEndpointAttachment resources.
        :param pulumi.Input[str] compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that the ODA private endpoint attachment belongs to.
        :param pulumi.Input[str] oda_instance_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the attached ODA Instance.
        :param pulumi.Input[str] oda_private_endpoint_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the ODA Private Endpoint.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] state: The current state of the ODA Private Endpoint attachment.
        :param pulumi.Input[str] time_created: When the resource was created. A date-time string as described in [RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.
        :param pulumi.Input[str] time_updated: When the resource was last updated. A date-time string as described in [RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.
        """
        _OdaPrivateEndpointAttachmentState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            compartment_id=compartment_id,
            oda_instance_id=oda_instance_id,
            oda_private_endpoint_id=oda_private_endpoint_id,
            state=state,
            time_created=time_created,
            time_updated=time_updated,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             compartment_id: Optional[pulumi.Input[str]] = None,
             oda_instance_id: Optional[pulumi.Input[str]] = None,
             oda_private_endpoint_id: Optional[pulumi.Input[str]] = None,
             state: Optional[pulumi.Input[str]] = None,
             time_created: Optional[pulumi.Input[str]] = None,
             time_updated: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if compartment_id is not None:
            _setter("compartment_id", compartment_id)
        if oda_instance_id is not None:
            _setter("oda_instance_id", oda_instance_id)
        if oda_private_endpoint_id is not None:
            _setter("oda_private_endpoint_id", oda_private_endpoint_id)
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
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that the ODA private endpoint attachment belongs to.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="odaInstanceId")
    def oda_instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the attached ODA Instance.
        """
        return pulumi.get(self, "oda_instance_id")

    @oda_instance_id.setter
    def oda_instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oda_instance_id", value)

    @property
    @pulumi.getter(name="odaPrivateEndpointId")
    def oda_private_endpoint_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the ODA Private Endpoint.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "oda_private_endpoint_id")

    @oda_private_endpoint_id.setter
    def oda_private_endpoint_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oda_private_endpoint_id", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current state of the ODA Private Endpoint attachment.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        When the resource was created. A date-time string as described in [RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> Optional[pulumi.Input[str]]:
        """
        When the resource was last updated. A date-time string as described in [RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.
        """
        return pulumi.get(self, "time_updated")

    @time_updated.setter
    def time_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_updated", value)


class OdaPrivateEndpointAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 oda_instance_id: Optional[pulumi.Input[str]] = None,
                 oda_private_endpoint_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Oda Private Endpoint Attachment resource in Oracle Cloud Infrastructure Digital Assistant service.

        Starts an asynchronous job to create an ODA Private Endpoint Attachment.

        To monitor the status of the job, take the `opc-work-request-id` response
        header value and use it to call `GET /workRequests/{workRequestID}`.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_oda_private_endpoint_attachment = oci.oda.OdaPrivateEndpointAttachment("testOdaPrivateEndpointAttachment",
            oda_instance_id=oci_oda_oda_instance["test_oda_instance"]["id"],
            oda_private_endpoint_id=oci_oda_oda_private_endpoint["test_oda_private_endpoint"]["id"])
        ```

        ## Import

        OdaPrivateEndpointAttachments can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:Oda/odaPrivateEndpointAttachment:OdaPrivateEndpointAttachment test_oda_private_endpoint_attachment "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] oda_instance_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the attached ODA Instance.
        :param pulumi.Input[str] oda_private_endpoint_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the ODA Private Endpoint.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OdaPrivateEndpointAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Oda Private Endpoint Attachment resource in Oracle Cloud Infrastructure Digital Assistant service.

        Starts an asynchronous job to create an ODA Private Endpoint Attachment.

        To monitor the status of the job, take the `opc-work-request-id` response
        header value and use it to call `GET /workRequests/{workRequestID}`.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_oda_private_endpoint_attachment = oci.oda.OdaPrivateEndpointAttachment("testOdaPrivateEndpointAttachment",
            oda_instance_id=oci_oda_oda_instance["test_oda_instance"]["id"],
            oda_private_endpoint_id=oci_oda_oda_private_endpoint["test_oda_private_endpoint"]["id"])
        ```

        ## Import

        OdaPrivateEndpointAttachments can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:Oda/odaPrivateEndpointAttachment:OdaPrivateEndpointAttachment test_oda_private_endpoint_attachment "id"
        ```

        :param str resource_name: The name of the resource.
        :param OdaPrivateEndpointAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OdaPrivateEndpointAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            OdaPrivateEndpointAttachmentArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 oda_instance_id: Optional[pulumi.Input[str]] = None,
                 oda_private_endpoint_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OdaPrivateEndpointAttachmentArgs.__new__(OdaPrivateEndpointAttachmentArgs)

            if oda_instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'oda_instance_id'")
            __props__.__dict__["oda_instance_id"] = oda_instance_id
            if oda_private_endpoint_id is None and not opts.urn:
                raise TypeError("Missing required property 'oda_private_endpoint_id'")
            __props__.__dict__["oda_private_endpoint_id"] = oda_private_endpoint_id
            __props__.__dict__["compartment_id"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["time_created"] = None
            __props__.__dict__["time_updated"] = None
        super(OdaPrivateEndpointAttachment, __self__).__init__(
            'oci:Oda/odaPrivateEndpointAttachment:OdaPrivateEndpointAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            oda_instance_id: Optional[pulumi.Input[str]] = None,
            oda_private_endpoint_id: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            time_updated: Optional[pulumi.Input[str]] = None) -> 'OdaPrivateEndpointAttachment':
        """
        Get an existing OdaPrivateEndpointAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that the ODA private endpoint attachment belongs to.
        :param pulumi.Input[str] oda_instance_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the attached ODA Instance.
        :param pulumi.Input[str] oda_private_endpoint_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the ODA Private Endpoint.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] state: The current state of the ODA Private Endpoint attachment.
        :param pulumi.Input[str] time_created: When the resource was created. A date-time string as described in [RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.
        :param pulumi.Input[str] time_updated: When the resource was last updated. A date-time string as described in [RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OdaPrivateEndpointAttachmentState.__new__(_OdaPrivateEndpointAttachmentState)

        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["oda_instance_id"] = oda_instance_id
        __props__.__dict__["oda_private_endpoint_id"] = oda_private_endpoint_id
        __props__.__dict__["state"] = state
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["time_updated"] = time_updated
        return OdaPrivateEndpointAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that the ODA private endpoint attachment belongs to.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="odaInstanceId")
    def oda_instance_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the attached ODA Instance.
        """
        return pulumi.get(self, "oda_instance_id")

    @property
    @pulumi.getter(name="odaPrivateEndpointId")
    def oda_private_endpoint_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the ODA Private Endpoint.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "oda_private_endpoint_id")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of the ODA Private Endpoint attachment.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        When the resource was created. A date-time string as described in [RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> pulumi.Output[str]:
        """
        When the resource was last updated. A date-time string as described in [RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.
        """
        return pulumi.get(self, "time_updated")

