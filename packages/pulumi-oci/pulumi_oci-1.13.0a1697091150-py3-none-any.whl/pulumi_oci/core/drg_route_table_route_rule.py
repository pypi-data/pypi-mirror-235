# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DrgRouteTableRouteRuleArgs', 'DrgRouteTableRouteRule']

@pulumi.input_type
class DrgRouteTableRouteRuleArgs:
    def __init__(__self__, *,
                 destination: pulumi.Input[str],
                 destination_type: pulumi.Input[str],
                 drg_route_table_id: pulumi.Input[str],
                 next_hop_drg_attachment_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a DrgRouteTableRouteRule resource.
        :param pulumi.Input[str] destination: (Updatable) This is the range of IP addresses used for matching when routing traffic. Only CIDR_BLOCK values are allowed.
               
               Potential values:
               * IP address range in CIDR notation. This can be an IPv4 or IPv6 CIDR. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`.
        :param pulumi.Input[str] destination_type: Type of destination for the rule. Required if `direction` = `EGRESS`. Allowed values:
        :param pulumi.Input[str] drg_route_table_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table.
               
               Potential values:
               * IP address range in CIDR notation. This can be an IPv4 CIDR block or IPv6 prefix. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`.
        :param pulumi.Input[str] next_hop_drg_attachment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the next hop DRG attachment. The next hop DRG attachment is responsible for reaching the network destination.
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        DrgRouteTableRouteRuleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            destination=destination,
            destination_type=destination_type,
            drg_route_table_id=drg_route_table_id,
            next_hop_drg_attachment_id=next_hop_drg_attachment_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             destination: pulumi.Input[str],
             destination_type: pulumi.Input[str],
             drg_route_table_id: pulumi.Input[str],
             next_hop_drg_attachment_id: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("destination", destination)
        _setter("destination_type", destination_type)
        _setter("drg_route_table_id", drg_route_table_id)
        _setter("next_hop_drg_attachment_id", next_hop_drg_attachment_id)

    @property
    @pulumi.getter
    def destination(self) -> pulumi.Input[str]:
        """
        (Updatable) This is the range of IP addresses used for matching when routing traffic. Only CIDR_BLOCK values are allowed.

        Potential values:
        * IP address range in CIDR notation. This can be an IPv4 or IPv6 CIDR. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`.
        """
        return pulumi.get(self, "destination")

    @destination.setter
    def destination(self, value: pulumi.Input[str]):
        pulumi.set(self, "destination", value)

    @property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> pulumi.Input[str]:
        """
        Type of destination for the rule. Required if `direction` = `EGRESS`. Allowed values:
        """
        return pulumi.get(self, "destination_type")

    @destination_type.setter
    def destination_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "destination_type", value)

    @property
    @pulumi.getter(name="drgRouteTableId")
    def drg_route_table_id(self) -> pulumi.Input[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table.

        Potential values:
        * IP address range in CIDR notation. This can be an IPv4 CIDR block or IPv6 prefix. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`.
        """
        return pulumi.get(self, "drg_route_table_id")

    @drg_route_table_id.setter
    def drg_route_table_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "drg_route_table_id", value)

    @property
    @pulumi.getter(name="nextHopDrgAttachmentId")
    def next_hop_drg_attachment_id(self) -> pulumi.Input[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the next hop DRG attachment. The next hop DRG attachment is responsible for reaching the network destination.

        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "next_hop_drg_attachment_id")

    @next_hop_drg_attachment_id.setter
    def next_hop_drg_attachment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "next_hop_drg_attachment_id", value)


@pulumi.input_type
class _DrgRouteTableRouteRuleState:
    def __init__(__self__, *,
                 attributes: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 destination: Optional[pulumi.Input[str]] = None,
                 destination_type: Optional[pulumi.Input[str]] = None,
                 drg_route_table_id: Optional[pulumi.Input[str]] = None,
                 is_blackhole: Optional[pulumi.Input[bool]] = None,
                 is_conflict: Optional[pulumi.Input[bool]] = None,
                 next_hop_drg_attachment_id: Optional[pulumi.Input[str]] = None,
                 route_provenance: Optional[pulumi.Input[str]] = None,
                 route_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DrgRouteTableRouteRule resources.
        :param pulumi.Input[Mapping[str, Any]] attributes: Additional properties for the route, computed by the service.
        :param pulumi.Input[str] destination: (Updatable) This is the range of IP addresses used for matching when routing traffic. Only CIDR_BLOCK values are allowed.
               
               Potential values:
               * IP address range in CIDR notation. This can be an IPv4 or IPv6 CIDR. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`.
        :param pulumi.Input[str] destination_type: Type of destination for the rule. Required if `direction` = `EGRESS`. Allowed values:
        :param pulumi.Input[str] drg_route_table_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table.
               
               Potential values:
               * IP address range in CIDR notation. This can be an IPv4 CIDR block or IPv6 prefix. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`.
        :param pulumi.Input[bool] is_blackhole: Indicates that if the next hop attachment does not exist, so traffic for this route is discarded without notification.
        :param pulumi.Input[bool] is_conflict: Indicates that the route was not imported due to a conflict between route rules.
        :param pulumi.Input[str] next_hop_drg_attachment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the next hop DRG attachment. The next hop DRG attachment is responsible for reaching the network destination.
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] route_provenance: The earliest origin of a route. If a route is advertised to a DRG through an IPsec tunnel attachment, and is propagated to peered DRGs via RPC attachments, the route's provenance in the peered DRGs remains `IPSEC_TUNNEL`, because that is the earliest origin.
        :param pulumi.Input[str] route_type: You can specify static routes for the DRG route table using the API. The DRG learns dynamic routes from the DRG attachments using various routing protocols.
        """
        _DrgRouteTableRouteRuleState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            attributes=attributes,
            destination=destination,
            destination_type=destination_type,
            drg_route_table_id=drg_route_table_id,
            is_blackhole=is_blackhole,
            is_conflict=is_conflict,
            next_hop_drg_attachment_id=next_hop_drg_attachment_id,
            route_provenance=route_provenance,
            route_type=route_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             attributes: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             destination: Optional[pulumi.Input[str]] = None,
             destination_type: Optional[pulumi.Input[str]] = None,
             drg_route_table_id: Optional[pulumi.Input[str]] = None,
             is_blackhole: Optional[pulumi.Input[bool]] = None,
             is_conflict: Optional[pulumi.Input[bool]] = None,
             next_hop_drg_attachment_id: Optional[pulumi.Input[str]] = None,
             route_provenance: Optional[pulumi.Input[str]] = None,
             route_type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if attributes is not None:
            _setter("attributes", attributes)
        if destination is not None:
            _setter("destination", destination)
        if destination_type is not None:
            _setter("destination_type", destination_type)
        if drg_route_table_id is not None:
            _setter("drg_route_table_id", drg_route_table_id)
        if is_blackhole is not None:
            _setter("is_blackhole", is_blackhole)
        if is_conflict is not None:
            _setter("is_conflict", is_conflict)
        if next_hop_drg_attachment_id is not None:
            _setter("next_hop_drg_attachment_id", next_hop_drg_attachment_id)
        if route_provenance is not None:
            _setter("route_provenance", route_provenance)
        if route_type is not None:
            _setter("route_type", route_type)

    @property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Additional properties for the route, computed by the service.
        """
        return pulumi.get(self, "attributes")

    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "attributes", value)

    @property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) This is the range of IP addresses used for matching when routing traffic. Only CIDR_BLOCK values are allowed.

        Potential values:
        * IP address range in CIDR notation. This can be an IPv4 or IPv6 CIDR. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`.
        """
        return pulumi.get(self, "destination")

    @destination.setter
    def destination(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination", value)

    @property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of destination for the rule. Required if `direction` = `EGRESS`. Allowed values:
        """
        return pulumi.get(self, "destination_type")

    @destination_type.setter
    def destination_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_type", value)

    @property
    @pulumi.getter(name="drgRouteTableId")
    def drg_route_table_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table.

        Potential values:
        * IP address range in CIDR notation. This can be an IPv4 CIDR block or IPv6 prefix. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`.
        """
        return pulumi.get(self, "drg_route_table_id")

    @drg_route_table_id.setter
    def drg_route_table_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "drg_route_table_id", value)

    @property
    @pulumi.getter(name="isBlackhole")
    def is_blackhole(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates that if the next hop attachment does not exist, so traffic for this route is discarded without notification.
        """
        return pulumi.get(self, "is_blackhole")

    @is_blackhole.setter
    def is_blackhole(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_blackhole", value)

    @property
    @pulumi.getter(name="isConflict")
    def is_conflict(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates that the route was not imported due to a conflict between route rules.
        """
        return pulumi.get(self, "is_conflict")

    @is_conflict.setter
    def is_conflict(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_conflict", value)

    @property
    @pulumi.getter(name="nextHopDrgAttachmentId")
    def next_hop_drg_attachment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the next hop DRG attachment. The next hop DRG attachment is responsible for reaching the network destination.

        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "next_hop_drg_attachment_id")

    @next_hop_drg_attachment_id.setter
    def next_hop_drg_attachment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "next_hop_drg_attachment_id", value)

    @property
    @pulumi.getter(name="routeProvenance")
    def route_provenance(self) -> Optional[pulumi.Input[str]]:
        """
        The earliest origin of a route. If a route is advertised to a DRG through an IPsec tunnel attachment, and is propagated to peered DRGs via RPC attachments, the route's provenance in the peered DRGs remains `IPSEC_TUNNEL`, because that is the earliest origin.
        """
        return pulumi.get(self, "route_provenance")

    @route_provenance.setter
    def route_provenance(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "route_provenance", value)

    @property
    @pulumi.getter(name="routeType")
    def route_type(self) -> Optional[pulumi.Input[str]]:
        """
        You can specify static routes for the DRG route table using the API. The DRG learns dynamic routes from the DRG attachments using various routing protocols.
        """
        return pulumi.get(self, "route_type")

    @route_type.setter
    def route_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "route_type", value)


class DrgRouteTableRouteRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination: Optional[pulumi.Input[str]] = None,
                 destination_type: Optional[pulumi.Input[str]] = None,
                 drg_route_table_id: Optional[pulumi.Input[str]] = None,
                 next_hop_drg_attachment_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Drg Route Table Route Rule resource in Oracle Cloud Infrastructure Core service.

        Adds one static route rule to the specified DRG route table.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_drg_route_table_route_rule = oci.core.DrgRouteTableRouteRule("testDrgRouteTableRouteRule",
            drg_route_table_id=oci_core_drg_route_table["test_drg_route_table"]["id"],
            destination=var["drg_route_table_route_rule_route_rules_destination"],
            destination_type=var["drg_route_table_route_rule_route_rules_destination_type"],
            next_hop_drg_attachment_id=oci_core_drg_attachment["test_drg_attachment"]["id"])
        ```

        ## Import

        DrgRouteTableRouteRule can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:Core/drgRouteTableRouteRule:DrgRouteTableRouteRule test_drg_route_table_route_rule "drgRouteTables/{drgRouteTableId}/routeRules/{id}"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] destination: (Updatable) This is the range of IP addresses used for matching when routing traffic. Only CIDR_BLOCK values are allowed.
               
               Potential values:
               * IP address range in CIDR notation. This can be an IPv4 or IPv6 CIDR. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`.
        :param pulumi.Input[str] destination_type: Type of destination for the rule. Required if `direction` = `EGRESS`. Allowed values:
        :param pulumi.Input[str] drg_route_table_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table.
               
               Potential values:
               * IP address range in CIDR notation. This can be an IPv4 CIDR block or IPv6 prefix. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`.
        :param pulumi.Input[str] next_hop_drg_attachment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the next hop DRG attachment. The next hop DRG attachment is responsible for reaching the network destination.
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DrgRouteTableRouteRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Drg Route Table Route Rule resource in Oracle Cloud Infrastructure Core service.

        Adds one static route rule to the specified DRG route table.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_drg_route_table_route_rule = oci.core.DrgRouteTableRouteRule("testDrgRouteTableRouteRule",
            drg_route_table_id=oci_core_drg_route_table["test_drg_route_table"]["id"],
            destination=var["drg_route_table_route_rule_route_rules_destination"],
            destination_type=var["drg_route_table_route_rule_route_rules_destination_type"],
            next_hop_drg_attachment_id=oci_core_drg_attachment["test_drg_attachment"]["id"])
        ```

        ## Import

        DrgRouteTableRouteRule can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:Core/drgRouteTableRouteRule:DrgRouteTableRouteRule test_drg_route_table_route_rule "drgRouteTables/{drgRouteTableId}/routeRules/{id}"
        ```

        :param str resource_name: The name of the resource.
        :param DrgRouteTableRouteRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DrgRouteTableRouteRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DrgRouteTableRouteRuleArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination: Optional[pulumi.Input[str]] = None,
                 destination_type: Optional[pulumi.Input[str]] = None,
                 drg_route_table_id: Optional[pulumi.Input[str]] = None,
                 next_hop_drg_attachment_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DrgRouteTableRouteRuleArgs.__new__(DrgRouteTableRouteRuleArgs)

            if destination is None and not opts.urn:
                raise TypeError("Missing required property 'destination'")
            __props__.__dict__["destination"] = destination
            if destination_type is None and not opts.urn:
                raise TypeError("Missing required property 'destination_type'")
            __props__.__dict__["destination_type"] = destination_type
            if drg_route_table_id is None and not opts.urn:
                raise TypeError("Missing required property 'drg_route_table_id'")
            __props__.__dict__["drg_route_table_id"] = drg_route_table_id
            if next_hop_drg_attachment_id is None and not opts.urn:
                raise TypeError("Missing required property 'next_hop_drg_attachment_id'")
            __props__.__dict__["next_hop_drg_attachment_id"] = next_hop_drg_attachment_id
            __props__.__dict__["attributes"] = None
            __props__.__dict__["is_blackhole"] = None
            __props__.__dict__["is_conflict"] = None
            __props__.__dict__["route_provenance"] = None
            __props__.__dict__["route_type"] = None
        super(DrgRouteTableRouteRule, __self__).__init__(
            'oci:Core/drgRouteTableRouteRule:DrgRouteTableRouteRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            attributes: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            destination: Optional[pulumi.Input[str]] = None,
            destination_type: Optional[pulumi.Input[str]] = None,
            drg_route_table_id: Optional[pulumi.Input[str]] = None,
            is_blackhole: Optional[pulumi.Input[bool]] = None,
            is_conflict: Optional[pulumi.Input[bool]] = None,
            next_hop_drg_attachment_id: Optional[pulumi.Input[str]] = None,
            route_provenance: Optional[pulumi.Input[str]] = None,
            route_type: Optional[pulumi.Input[str]] = None) -> 'DrgRouteTableRouteRule':
        """
        Get an existing DrgRouteTableRouteRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] attributes: Additional properties for the route, computed by the service.
        :param pulumi.Input[str] destination: (Updatable) This is the range of IP addresses used for matching when routing traffic. Only CIDR_BLOCK values are allowed.
               
               Potential values:
               * IP address range in CIDR notation. This can be an IPv4 or IPv6 CIDR. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`.
        :param pulumi.Input[str] destination_type: Type of destination for the rule. Required if `direction` = `EGRESS`. Allowed values:
        :param pulumi.Input[str] drg_route_table_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table.
               
               Potential values:
               * IP address range in CIDR notation. This can be an IPv4 CIDR block or IPv6 prefix. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`.
        :param pulumi.Input[bool] is_blackhole: Indicates that if the next hop attachment does not exist, so traffic for this route is discarded without notification.
        :param pulumi.Input[bool] is_conflict: Indicates that the route was not imported due to a conflict between route rules.
        :param pulumi.Input[str] next_hop_drg_attachment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the next hop DRG attachment. The next hop DRG attachment is responsible for reaching the network destination.
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] route_provenance: The earliest origin of a route. If a route is advertised to a DRG through an IPsec tunnel attachment, and is propagated to peered DRGs via RPC attachments, the route's provenance in the peered DRGs remains `IPSEC_TUNNEL`, because that is the earliest origin.
        :param pulumi.Input[str] route_type: You can specify static routes for the DRG route table using the API. The DRG learns dynamic routes from the DRG attachments using various routing protocols.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DrgRouteTableRouteRuleState.__new__(_DrgRouteTableRouteRuleState)

        __props__.__dict__["attributes"] = attributes
        __props__.__dict__["destination"] = destination
        __props__.__dict__["destination_type"] = destination_type
        __props__.__dict__["drg_route_table_id"] = drg_route_table_id
        __props__.__dict__["is_blackhole"] = is_blackhole
        __props__.__dict__["is_conflict"] = is_conflict
        __props__.__dict__["next_hop_drg_attachment_id"] = next_hop_drg_attachment_id
        __props__.__dict__["route_provenance"] = route_provenance
        __props__.__dict__["route_type"] = route_type
        return DrgRouteTableRouteRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def attributes(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        Additional properties for the route, computed by the service.
        """
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter
    def destination(self) -> pulumi.Output[str]:
        """
        (Updatable) This is the range of IP addresses used for matching when routing traffic. Only CIDR_BLOCK values are allowed.

        Potential values:
        * IP address range in CIDR notation. This can be an IPv4 or IPv6 CIDR. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`.
        """
        return pulumi.get(self, "destination")

    @property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> pulumi.Output[str]:
        """
        Type of destination for the rule. Required if `direction` = `EGRESS`. Allowed values:
        """
        return pulumi.get(self, "destination_type")

    @property
    @pulumi.getter(name="drgRouteTableId")
    def drg_route_table_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table.

        Potential values:
        * IP address range in CIDR notation. This can be an IPv4 CIDR block or IPv6 prefix. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`.
        """
        return pulumi.get(self, "drg_route_table_id")

    @property
    @pulumi.getter(name="isBlackhole")
    def is_blackhole(self) -> pulumi.Output[bool]:
        """
        Indicates that if the next hop attachment does not exist, so traffic for this route is discarded without notification.
        """
        return pulumi.get(self, "is_blackhole")

    @property
    @pulumi.getter(name="isConflict")
    def is_conflict(self) -> pulumi.Output[bool]:
        """
        Indicates that the route was not imported due to a conflict between route rules.
        """
        return pulumi.get(self, "is_conflict")

    @property
    @pulumi.getter(name="nextHopDrgAttachmentId")
    def next_hop_drg_attachment_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the next hop DRG attachment. The next hop DRG attachment is responsible for reaching the network destination.

        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "next_hop_drg_attachment_id")

    @property
    @pulumi.getter(name="routeProvenance")
    def route_provenance(self) -> pulumi.Output[str]:
        """
        The earliest origin of a route. If a route is advertised to a DRG through an IPsec tunnel attachment, and is propagated to peered DRGs via RPC attachments, the route's provenance in the peered DRGs remains `IPSEC_TUNNEL`, because that is the earliest origin.
        """
        return pulumi.get(self, "route_provenance")

    @property
    @pulumi.getter(name="routeType")
    def route_type(self) -> pulumi.Output[str]:
        """
        You can specify static routes for the DRG route table using the API. The DRG learns dynamic routes from the DRG attachments using various routing protocols.
        """
        return pulumi.get(self, "route_type")

