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

__all__ = ['HttpRedirectArgs', 'HttpRedirect']

@pulumi.input_type
class HttpRedirectArgs:
    def __init__(__self__, *,
                 compartment_id: pulumi.Input[str],
                 domain: pulumi.Input[str],
                 target: pulumi.Input['HttpRedirectTargetArgs'],
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 response_code: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a HttpRedirect resource.
        :param pulumi.Input[str] compartment_id: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the HTTP Redirects compartment.
        :param pulumi.Input[str] domain: The domain from which traffic will be redirected.
        :param pulumi.Input['HttpRedirectTargetArgs'] target: (Updatable) The redirect target object including all the redirect data.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] display_name: (Updatable) The user-friendly name of the HTTP Redirect. The name can be changed and does not need to be unique.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        :param pulumi.Input[int] response_code: (Updatable) The response code returned for the redirect to the client. For more information, see [RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.4).
        """
        HttpRedirectArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            compartment_id=compartment_id,
            domain=domain,
            target=target,
            defined_tags=defined_tags,
            display_name=display_name,
            freeform_tags=freeform_tags,
            response_code=response_code,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             compartment_id: pulumi.Input[str],
             domain: pulumi.Input[str],
             target: pulumi.Input['HttpRedirectTargetArgs'],
             defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             display_name: Optional[pulumi.Input[str]] = None,
             freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             response_code: Optional[pulumi.Input[int]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("compartment_id", compartment_id)
        _setter("domain", domain)
        _setter("target", target)
        if defined_tags is not None:
            _setter("defined_tags", defined_tags)
        if display_name is not None:
            _setter("display_name", display_name)
        if freeform_tags is not None:
            _setter("freeform_tags", freeform_tags)
        if response_code is not None:
            _setter("response_code", response_code)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Input[str]:
        """
        (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the HTTP Redirects compartment.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Input[str]:
        """
        The domain from which traffic will be redirected.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter
    def target(self) -> pulumi.Input['HttpRedirectTargetArgs']:
        """
        (Updatable) The redirect target object including all the redirect data.
        """
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: pulumi.Input['HttpRedirectTargetArgs']):
        pulumi.set(self, "target", value)

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
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The user-friendly name of the HTTP Redirect. The name can be changed and does not need to be unique.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="responseCode")
    def response_code(self) -> Optional[pulumi.Input[int]]:
        """
        (Updatable) The response code returned for the redirect to the client. For more information, see [RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.4).
        """
        return pulumi.get(self, "response_code")

    @response_code.setter
    def response_code(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "response_code", value)


@pulumi.input_type
class _HttpRedirectState:
    def __init__(__self__, *,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 response_code: Optional[pulumi.Input[int]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input['HttpRedirectTargetArgs']] = None,
                 time_created: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering HttpRedirect resources.
        :param pulumi.Input[str] compartment_id: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the HTTP Redirects compartment.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] display_name: (Updatable) The user-friendly name of the HTTP Redirect. The name can be changed and does not need to be unique.
        :param pulumi.Input[str] domain: The domain from which traffic will be redirected.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        :param pulumi.Input[int] response_code: (Updatable) The response code returned for the redirect to the client. For more information, see [RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.4).
        :param pulumi.Input[str] state: The current lifecycle state of the HTTP Redirect.
        :param pulumi.Input['HttpRedirectTargetArgs'] target: (Updatable) The redirect target object including all the redirect data.
        :param pulumi.Input[str] time_created: The date and time the policy was created, expressed in RFC 3339 timestamp format.
        """
        _HttpRedirectState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            compartment_id=compartment_id,
            defined_tags=defined_tags,
            display_name=display_name,
            domain=domain,
            freeform_tags=freeform_tags,
            response_code=response_code,
            state=state,
            target=target,
            time_created=time_created,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             compartment_id: Optional[pulumi.Input[str]] = None,
             defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             display_name: Optional[pulumi.Input[str]] = None,
             domain: Optional[pulumi.Input[str]] = None,
             freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             response_code: Optional[pulumi.Input[int]] = None,
             state: Optional[pulumi.Input[str]] = None,
             target: Optional[pulumi.Input['HttpRedirectTargetArgs']] = None,
             time_created: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if compartment_id is not None:
            _setter("compartment_id", compartment_id)
        if defined_tags is not None:
            _setter("defined_tags", defined_tags)
        if display_name is not None:
            _setter("display_name", display_name)
        if domain is not None:
            _setter("domain", domain)
        if freeform_tags is not None:
            _setter("freeform_tags", freeform_tags)
        if response_code is not None:
            _setter("response_code", response_code)
        if state is not None:
            _setter("state", state)
        if target is not None:
            _setter("target", target)
        if time_created is not None:
            _setter("time_created", time_created)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the HTTP Redirects compartment.
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
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The user-friendly name of the HTTP Redirect. The name can be changed and does not need to be unique.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        The domain from which traffic will be redirected.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="responseCode")
    def response_code(self) -> Optional[pulumi.Input[int]]:
        """
        (Updatable) The response code returned for the redirect to the client. For more information, see [RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.4).
        """
        return pulumi.get(self, "response_code")

    @response_code.setter
    def response_code(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "response_code", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current lifecycle state of the HTTP Redirect.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input['HttpRedirectTargetArgs']]:
        """
        (Updatable) The redirect target object including all the redirect data.
        """
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: Optional[pulumi.Input['HttpRedirectTargetArgs']]):
        pulumi.set(self, "target", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time the policy was created, expressed in RFC 3339 timestamp format.
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)


class HttpRedirect(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 response_code: Optional[pulumi.Input[int]] = None,
                 target: Optional[pulumi.Input[pulumi.InputType['HttpRedirectTargetArgs']]] = None,
                 __props__=None):
        """
        This resource provides the Http Redirect resource in Oracle Cloud Infrastructure Web Application Acceleration and Security service.

        Creates a new HTTP Redirect on the WAF edge.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_http_redirect = oci.waas.HttpRedirect("testHttpRedirect",
            compartment_id=var["compartment_id"],
            domain=var["http_redirect_domain"],
            target=oci.waas.HttpRedirectTargetArgs(
                host=var["http_redirect_target_host"],
                path=var["http_redirect_target_path"],
                protocol=var["http_redirect_target_protocol"],
                query=var["http_redirect_target_query"],
                port=var["http_redirect_target_port"],
            ),
            defined_tags={
                "Operations.CostCenter": "42",
            },
            display_name=var["http_redirect_display_name"],
            freeform_tags={
                "Department": "Finance",
            },
            response_code=var["http_redirect_response_code"])
        ```

        ## Import

        HttpRedirects can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:Waas/httpRedirect:HttpRedirect test_http_redirect "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the HTTP Redirects compartment.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] display_name: (Updatable) The user-friendly name of the HTTP Redirect. The name can be changed and does not need to be unique.
        :param pulumi.Input[str] domain: The domain from which traffic will be redirected.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        :param pulumi.Input[int] response_code: (Updatable) The response code returned for the redirect to the client. For more information, see [RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.4).
        :param pulumi.Input[pulumi.InputType['HttpRedirectTargetArgs']] target: (Updatable) The redirect target object including all the redirect data.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HttpRedirectArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Http Redirect resource in Oracle Cloud Infrastructure Web Application Acceleration and Security service.

        Creates a new HTTP Redirect on the WAF edge.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_http_redirect = oci.waas.HttpRedirect("testHttpRedirect",
            compartment_id=var["compartment_id"],
            domain=var["http_redirect_domain"],
            target=oci.waas.HttpRedirectTargetArgs(
                host=var["http_redirect_target_host"],
                path=var["http_redirect_target_path"],
                protocol=var["http_redirect_target_protocol"],
                query=var["http_redirect_target_query"],
                port=var["http_redirect_target_port"],
            ),
            defined_tags={
                "Operations.CostCenter": "42",
            },
            display_name=var["http_redirect_display_name"],
            freeform_tags={
                "Department": "Finance",
            },
            response_code=var["http_redirect_response_code"])
        ```

        ## Import

        HttpRedirects can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:Waas/httpRedirect:HttpRedirect test_http_redirect "id"
        ```

        :param str resource_name: The name of the resource.
        :param HttpRedirectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HttpRedirectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            HttpRedirectArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 response_code: Optional[pulumi.Input[int]] = None,
                 target: Optional[pulumi.Input[pulumi.InputType['HttpRedirectTargetArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HttpRedirectArgs.__new__(HttpRedirectArgs)

            if compartment_id is None and not opts.urn:
                raise TypeError("Missing required property 'compartment_id'")
            __props__.__dict__["compartment_id"] = compartment_id
            __props__.__dict__["defined_tags"] = defined_tags
            __props__.__dict__["display_name"] = display_name
            if domain is None and not opts.urn:
                raise TypeError("Missing required property 'domain'")
            __props__.__dict__["domain"] = domain
            __props__.__dict__["freeform_tags"] = freeform_tags
            __props__.__dict__["response_code"] = response_code
            if target is not None and not isinstance(target, HttpRedirectTargetArgs):
                target = target or {}
                def _setter(key, value):
                    target[key] = value
                HttpRedirectTargetArgs._configure(_setter, **target)
            if target is None and not opts.urn:
                raise TypeError("Missing required property 'target'")
            __props__.__dict__["target"] = target
            __props__.__dict__["state"] = None
            __props__.__dict__["time_created"] = None
        super(HttpRedirect, __self__).__init__(
            'oci:Waas/httpRedirect:HttpRedirect',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            domain: Optional[pulumi.Input[str]] = None,
            freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            response_code: Optional[pulumi.Input[int]] = None,
            state: Optional[pulumi.Input[str]] = None,
            target: Optional[pulumi.Input[pulumi.InputType['HttpRedirectTargetArgs']]] = None,
            time_created: Optional[pulumi.Input[str]] = None) -> 'HttpRedirect':
        """
        Get an existing HttpRedirect resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the HTTP Redirects compartment.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] display_name: (Updatable) The user-friendly name of the HTTP Redirect. The name can be changed and does not need to be unique.
        :param pulumi.Input[str] domain: The domain from which traffic will be redirected.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        :param pulumi.Input[int] response_code: (Updatable) The response code returned for the redirect to the client. For more information, see [RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.4).
        :param pulumi.Input[str] state: The current lifecycle state of the HTTP Redirect.
        :param pulumi.Input[pulumi.InputType['HttpRedirectTargetArgs']] target: (Updatable) The redirect target object including all the redirect data.
        :param pulumi.Input[str] time_created: The date and time the policy was created, expressed in RFC 3339 timestamp format.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _HttpRedirectState.__new__(_HttpRedirectState)

        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["defined_tags"] = defined_tags
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["domain"] = domain
        __props__.__dict__["freeform_tags"] = freeform_tags
        __props__.__dict__["response_code"] = response_code
        __props__.__dict__["state"] = state
        __props__.__dict__["target"] = target
        __props__.__dict__["time_created"] = time_created
        return HttpRedirect(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the HTTP Redirects compartment.
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
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        (Updatable) The user-friendly name of the HTTP Redirect. The name can be changed and does not need to be unique.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[str]:
        """
        The domain from which traffic will be redirected.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="responseCode")
    def response_code(self) -> pulumi.Output[int]:
        """
        (Updatable) The response code returned for the redirect to the client. For more information, see [RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.4).
        """
        return pulumi.get(self, "response_code")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current lifecycle state of the HTTP Redirect.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def target(self) -> pulumi.Output['outputs.HttpRedirectTarget']:
        """
        (Updatable) The redirect target object including all the redirect data.
        """
        return pulumi.get(self, "target")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The date and time the policy was created, expressed in RFC 3339 timestamp format.
        """
        return pulumi.get(self, "time_created")

