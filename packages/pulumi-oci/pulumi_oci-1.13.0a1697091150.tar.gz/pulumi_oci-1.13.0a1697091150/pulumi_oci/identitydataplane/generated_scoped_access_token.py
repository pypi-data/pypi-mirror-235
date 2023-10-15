# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['GeneratedScopedAccessTokenArgs', 'GeneratedScopedAccessToken']

@pulumi.input_type
class GeneratedScopedAccessTokenArgs:
    def __init__(__self__, *,
                 public_key: pulumi.Input[str],
                 scope: pulumi.Input[str]):
        """
        The set of arguments for constructing a GeneratedScopedAccessToken resource.
        :param pulumi.Input[str] public_key: A temporary public key, owned by the service. The service also owns the corresponding private key. This public key will by put inside the security token by the auth service after successful validation of the certificate.
        :param pulumi.Input[str] scope: Scope definition for the scoped access token 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        GeneratedScopedAccessTokenArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            public_key=public_key,
            scope=scope,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             public_key: pulumi.Input[str],
             scope: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("public_key", public_key)
        _setter("scope", scope)

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Input[str]:
        """
        A temporary public key, owned by the service. The service also owns the corresponding private key. This public key will by put inside the security token by the auth service after successful validation of the certificate.
        """
        return pulumi.get(self, "public_key")

    @public_key.setter
    def public_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "public_key", value)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input[str]:
        """
        Scope definition for the scoped access token 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope", value)


@pulumi.input_type
class _GeneratedScopedAccessTokenState:
    def __init__(__self__, *,
                 public_key: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering GeneratedScopedAccessToken resources.
        :param pulumi.Input[str] public_key: A temporary public key, owned by the service. The service also owns the corresponding private key. This public key will by put inside the security token by the auth service after successful validation of the certificate.
        :param pulumi.Input[str] scope: Scope definition for the scoped access token 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] token: The security token, signed by auth service
        """
        _GeneratedScopedAccessTokenState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            public_key=public_key,
            scope=scope,
            token=token,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             public_key: Optional[pulumi.Input[str]] = None,
             scope: Optional[pulumi.Input[str]] = None,
             token: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if public_key is not None:
            _setter("public_key", public_key)
        if scope is not None:
            _setter("scope", scope)
        if token is not None:
            _setter("token", token)

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[pulumi.Input[str]]:
        """
        A temporary public key, owned by the service. The service also owns the corresponding private key. This public key will by put inside the security token by the auth service after successful validation of the certificate.
        """
        return pulumi.get(self, "public_key")

    @public_key.setter
    def public_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_key", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        Scope definition for the scoped access token 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        The security token, signed by auth service
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)


class GeneratedScopedAccessToken(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Generate Scoped Access Token resource in Oracle Cloud Infrastructure Identity Data Plane service.

        Based on the calling principal and the input payload, derive the claims and create a security token.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_generate_scoped_access_token = oci.identity_data_plane.GeneratedScopedAccessToken("testGenerateScopedAccessToken",
            public_key=var["generate_scoped_access_token_public_key"],
            scope=var["generate_scoped_access_token_scope"])
        ```

        ## Import

        GenerateScopedAccessToken can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:IdentityDataPlane/generatedScopedAccessToken:GeneratedScopedAccessToken test_generate_scoped_access_token "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] public_key: A temporary public key, owned by the service. The service also owns the corresponding private key. This public key will by put inside the security token by the auth service after successful validation of the certificate.
        :param pulumi.Input[str] scope: Scope definition for the scoped access token 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GeneratedScopedAccessTokenArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Generate Scoped Access Token resource in Oracle Cloud Infrastructure Identity Data Plane service.

        Based on the calling principal and the input payload, derive the claims and create a security token.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_generate_scoped_access_token = oci.identity_data_plane.GeneratedScopedAccessToken("testGenerateScopedAccessToken",
            public_key=var["generate_scoped_access_token_public_key"],
            scope=var["generate_scoped_access_token_scope"])
        ```

        ## Import

        GenerateScopedAccessToken can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:IdentityDataPlane/generatedScopedAccessToken:GeneratedScopedAccessToken test_generate_scoped_access_token "id"
        ```

        :param str resource_name: The name of the resource.
        :param GeneratedScopedAccessTokenArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GeneratedScopedAccessTokenArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            GeneratedScopedAccessTokenArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GeneratedScopedAccessTokenArgs.__new__(GeneratedScopedAccessTokenArgs)

            if public_key is None and not opts.urn:
                raise TypeError("Missing required property 'public_key'")
            __props__.__dict__["public_key"] = public_key
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            __props__.__dict__["token"] = None
        super(GeneratedScopedAccessToken, __self__).__init__(
            'oci:IdentityDataPlane/generatedScopedAccessToken:GeneratedScopedAccessToken',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            public_key: Optional[pulumi.Input[str]] = None,
            scope: Optional[pulumi.Input[str]] = None,
            token: Optional[pulumi.Input[str]] = None) -> 'GeneratedScopedAccessToken':
        """
        Get an existing GeneratedScopedAccessToken resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] public_key: A temporary public key, owned by the service. The service also owns the corresponding private key. This public key will by put inside the security token by the auth service after successful validation of the certificate.
        :param pulumi.Input[str] scope: Scope definition for the scoped access token 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] token: The security token, signed by auth service
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GeneratedScopedAccessTokenState.__new__(_GeneratedScopedAccessTokenState)

        __props__.__dict__["public_key"] = public_key
        __props__.__dict__["scope"] = scope
        __props__.__dict__["token"] = token
        return GeneratedScopedAccessToken(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Output[str]:
        """
        A temporary public key, owned by the service. The service also owns the corresponding private key. This public key will by put inside the security token by the auth service after successful validation of the certificate.
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[str]:
        """
        Scope definition for the scoped access token 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def token(self) -> pulumi.Output[str]:
        """
        The security token, signed by auth service
        """
        return pulumi.get(self, "token")

