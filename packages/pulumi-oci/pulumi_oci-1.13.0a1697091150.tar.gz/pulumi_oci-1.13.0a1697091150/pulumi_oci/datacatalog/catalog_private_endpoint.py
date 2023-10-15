# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['CatalogPrivateEndpointArgs', 'CatalogPrivateEndpoint']

@pulumi.input_type
class CatalogPrivateEndpointArgs:
    def __init__(__self__, *,
                 compartment_id: pulumi.Input[str],
                 dns_zones: pulumi.Input[Sequence[pulumi.Input[str]]],
                 subnet_id: pulumi.Input[str],
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a CatalogPrivateEndpoint resource.
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment identifier.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_zones: (Updatable) List of DNS zones to be used by the data assets to be harvested. Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com
        :param pulumi.Input[str] subnet_id: The OCID of subnet to which the reverse connection is to be created 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] display_name: (Updatable) Display name of the private endpoint resource being created.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        CatalogPrivateEndpointArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            compartment_id=compartment_id,
            dns_zones=dns_zones,
            subnet_id=subnet_id,
            defined_tags=defined_tags,
            display_name=display_name,
            freeform_tags=freeform_tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             compartment_id: pulumi.Input[str],
             dns_zones: pulumi.Input[Sequence[pulumi.Input[str]]],
             subnet_id: pulumi.Input[str],
             defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             display_name: Optional[pulumi.Input[str]] = None,
             freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("compartment_id", compartment_id)
        _setter("dns_zones", dns_zones)
        _setter("subnet_id", subnet_id)
        if defined_tags is not None:
            _setter("defined_tags", defined_tags)
        if display_name is not None:
            _setter("display_name", display_name)
        if freeform_tags is not None:
            _setter("freeform_tags", freeform_tags)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Input[str]:
        """
        (Updatable) Compartment identifier.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="dnsZones")
    def dns_zones(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        (Updatable) List of DNS zones to be used by the data assets to be harvested. Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com
        """
        return pulumi.get(self, "dns_zones")

    @dns_zones.setter
    def dns_zones(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "dns_zones", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[str]:
        """
        The OCID of subnet to which the reverse connection is to be created 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Display name of the private endpoint resource being created.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)


@pulumi.input_type
class _CatalogPrivateEndpointState:
    def __init__(__self__, *,
                 attached_catalogs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 dns_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 lifecycle_details: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 time_updated: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CatalogPrivateEndpoint resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] attached_catalogs: The list of catalogs using the private reverse connection endpoint
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment identifier.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] display_name: (Updatable) Display name of the private endpoint resource being created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_zones: (Updatable) List of DNS zones to be used by the data assets to be harvested. Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input[str] lifecycle_details: A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in 'Failed' state.
        :param pulumi.Input[str] state: The current state of the private endpoint resource.
        :param pulumi.Input[str] subnet_id: The OCID of subnet to which the reverse connection is to be created 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] time_created: The time the private endpoint was created. An [RFC3339](https://tools.ietf.org/html/rfc3339) formatted datetime string.
        :param pulumi.Input[str] time_updated: The time the private endpoint was updated. An [RFC3339](https://tools.ietf.org/html/rfc3339) formatted datetime string.
        """
        _CatalogPrivateEndpointState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            attached_catalogs=attached_catalogs,
            compartment_id=compartment_id,
            defined_tags=defined_tags,
            display_name=display_name,
            dns_zones=dns_zones,
            freeform_tags=freeform_tags,
            lifecycle_details=lifecycle_details,
            state=state,
            subnet_id=subnet_id,
            time_created=time_created,
            time_updated=time_updated,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             attached_catalogs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             compartment_id: Optional[pulumi.Input[str]] = None,
             defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             display_name: Optional[pulumi.Input[str]] = None,
             dns_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             lifecycle_details: Optional[pulumi.Input[str]] = None,
             state: Optional[pulumi.Input[str]] = None,
             subnet_id: Optional[pulumi.Input[str]] = None,
             time_created: Optional[pulumi.Input[str]] = None,
             time_updated: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if attached_catalogs is not None:
            _setter("attached_catalogs", attached_catalogs)
        if compartment_id is not None:
            _setter("compartment_id", compartment_id)
        if defined_tags is not None:
            _setter("defined_tags", defined_tags)
        if display_name is not None:
            _setter("display_name", display_name)
        if dns_zones is not None:
            _setter("dns_zones", dns_zones)
        if freeform_tags is not None:
            _setter("freeform_tags", freeform_tags)
        if lifecycle_details is not None:
            _setter("lifecycle_details", lifecycle_details)
        if state is not None:
            _setter("state", state)
        if subnet_id is not None:
            _setter("subnet_id", subnet_id)
        if time_created is not None:
            _setter("time_created", time_created)
        if time_updated is not None:
            _setter("time_updated", time_updated)

    @property
    @pulumi.getter(name="attachedCatalogs")
    def attached_catalogs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of catalogs using the private reverse connection endpoint
        """
        return pulumi.get(self, "attached_catalogs")

    @attached_catalogs.setter
    def attached_catalogs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "attached_catalogs", value)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Compartment identifier.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Display name of the private endpoint resource being created.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="dnsZones")
    def dns_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        (Updatable) List of DNS zones to be used by the data assets to be harvested. Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com
        """
        return pulumi.get(self, "dns_zones")

    @dns_zones.setter
    def dns_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "dns_zones", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> Optional[pulumi.Input[str]]:
        """
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in 'Failed' state.
        """
        return pulumi.get(self, "lifecycle_details")

    @lifecycle_details.setter
    def lifecycle_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_details", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current state of the private endpoint resource.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[str]]:
        """
        The OCID of subnet to which the reverse connection is to be created 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The time the private endpoint was created. An [RFC3339](https://tools.ietf.org/html/rfc3339) formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> Optional[pulumi.Input[str]]:
        """
        The time the private endpoint was updated. An [RFC3339](https://tools.ietf.org/html/rfc3339) formatted datetime string.
        """
        return pulumi.get(self, "time_updated")

    @time_updated.setter
    def time_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_updated", value)


class CatalogPrivateEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 dns_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Catalog Private Endpoint resource in Oracle Cloud Infrastructure Data Catalog service.

        Create a new private reverse connection endpoint.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_catalog_private_endpoint = oci.data_catalog.CatalogPrivateEndpoint("testCatalogPrivateEndpoint",
            compartment_id=var["compartment_id"],
            dns_zones=var["catalog_private_endpoint_dns_zones"],
            subnet_id=oci_core_subnet["test_subnet"]["id"],
            defined_tags={
                "foo-namespace.bar-key": "value",
            },
            display_name=var["catalog_private_endpoint_display_name"],
            freeform_tags={
                "bar-key": "value",
            })
        ```

        ## Import

        CatalogPrivateEndpoints can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:DataCatalog/catalogPrivateEndpoint:CatalogPrivateEndpoint test_catalog_private_endpoint "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment identifier.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] display_name: (Updatable) Display name of the private endpoint resource being created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_zones: (Updatable) List of DNS zones to be used by the data assets to be harvested. Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input[str] subnet_id: The OCID of subnet to which the reverse connection is to be created 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CatalogPrivateEndpointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Catalog Private Endpoint resource in Oracle Cloud Infrastructure Data Catalog service.

        Create a new private reverse connection endpoint.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_catalog_private_endpoint = oci.data_catalog.CatalogPrivateEndpoint("testCatalogPrivateEndpoint",
            compartment_id=var["compartment_id"],
            dns_zones=var["catalog_private_endpoint_dns_zones"],
            subnet_id=oci_core_subnet["test_subnet"]["id"],
            defined_tags={
                "foo-namespace.bar-key": "value",
            },
            display_name=var["catalog_private_endpoint_display_name"],
            freeform_tags={
                "bar-key": "value",
            })
        ```

        ## Import

        CatalogPrivateEndpoints can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:DataCatalog/catalogPrivateEndpoint:CatalogPrivateEndpoint test_catalog_private_endpoint "id"
        ```

        :param str resource_name: The name of the resource.
        :param CatalogPrivateEndpointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CatalogPrivateEndpointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            CatalogPrivateEndpointArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 dns_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CatalogPrivateEndpointArgs.__new__(CatalogPrivateEndpointArgs)

            if compartment_id is None and not opts.urn:
                raise TypeError("Missing required property 'compartment_id'")
            __props__.__dict__["compartment_id"] = compartment_id
            __props__.__dict__["defined_tags"] = defined_tags
            __props__.__dict__["display_name"] = display_name
            if dns_zones is None and not opts.urn:
                raise TypeError("Missing required property 'dns_zones'")
            __props__.__dict__["dns_zones"] = dns_zones
            __props__.__dict__["freeform_tags"] = freeform_tags
            if subnet_id is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_id'")
            __props__.__dict__["subnet_id"] = subnet_id
            __props__.__dict__["attached_catalogs"] = None
            __props__.__dict__["lifecycle_details"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["time_created"] = None
            __props__.__dict__["time_updated"] = None
        super(CatalogPrivateEndpoint, __self__).__init__(
            'oci:DataCatalog/catalogPrivateEndpoint:CatalogPrivateEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            attached_catalogs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            dns_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            lifecycle_details: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            subnet_id: Optional[pulumi.Input[str]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            time_updated: Optional[pulumi.Input[str]] = None) -> 'CatalogPrivateEndpoint':
        """
        Get an existing CatalogPrivateEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] attached_catalogs: The list of catalogs using the private reverse connection endpoint
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment identifier.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] display_name: (Updatable) Display name of the private endpoint resource being created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_zones: (Updatable) List of DNS zones to be used by the data assets to be harvested. Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input[str] lifecycle_details: A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in 'Failed' state.
        :param pulumi.Input[str] state: The current state of the private endpoint resource.
        :param pulumi.Input[str] subnet_id: The OCID of subnet to which the reverse connection is to be created 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] time_created: The time the private endpoint was created. An [RFC3339](https://tools.ietf.org/html/rfc3339) formatted datetime string.
        :param pulumi.Input[str] time_updated: The time the private endpoint was updated. An [RFC3339](https://tools.ietf.org/html/rfc3339) formatted datetime string.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CatalogPrivateEndpointState.__new__(_CatalogPrivateEndpointState)

        __props__.__dict__["attached_catalogs"] = attached_catalogs
        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["defined_tags"] = defined_tags
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["dns_zones"] = dns_zones
        __props__.__dict__["freeform_tags"] = freeform_tags
        __props__.__dict__["lifecycle_details"] = lifecycle_details
        __props__.__dict__["state"] = state
        __props__.__dict__["subnet_id"] = subnet_id
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["time_updated"] = time_updated
        return CatalogPrivateEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="attachedCatalogs")
    def attached_catalogs(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of catalogs using the private reverse connection endpoint
        """
        return pulumi.get(self, "attached_catalogs")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        (Updatable) Compartment identifier.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        (Updatable) Display name of the private endpoint resource being created.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="dnsZones")
    def dns_zones(self) -> pulumi.Output[Sequence[str]]:
        """
        (Updatable) List of DNS zones to be used by the data assets to be harvested. Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com
        """
        return pulumi.get(self, "dns_zones")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> pulumi.Output[str]:
        """
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in 'Failed' state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of the private endpoint resource.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        """
        The OCID of subnet to which the reverse connection is to be created 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The time the private endpoint was created. An [RFC3339](https://tools.ietf.org/html/rfc3339) formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> pulumi.Output[str]:
        """
        The time the private endpoint was updated. An [RFC3339](https://tools.ietf.org/html/rfc3339) formatted datetime string.
        """
        return pulumi.get(self, "time_updated")

