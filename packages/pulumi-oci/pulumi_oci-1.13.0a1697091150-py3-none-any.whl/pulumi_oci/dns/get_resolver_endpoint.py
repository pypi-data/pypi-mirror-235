# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetResolverEndpointResult',
    'AwaitableGetResolverEndpointResult',
    'get_resolver_endpoint',
    'get_resolver_endpoint_output',
]

@pulumi.output_type
class GetResolverEndpointResult:
    """
    A collection of values returned by getResolverEndpoint.
    """
    def __init__(__self__, compartment_id=None, endpoint_type=None, forwarding_address=None, id=None, is_forwarding=None, is_listening=None, listening_address=None, name=None, nsg_ids=None, resolver_endpoint_name=None, resolver_id=None, scope=None, self=None, state=None, subnet_id=None, time_created=None, time_updated=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if endpoint_type and not isinstance(endpoint_type, str):
            raise TypeError("Expected argument 'endpoint_type' to be a str")
        pulumi.set(__self__, "endpoint_type", endpoint_type)
        if forwarding_address and not isinstance(forwarding_address, str):
            raise TypeError("Expected argument 'forwarding_address' to be a str")
        pulumi.set(__self__, "forwarding_address", forwarding_address)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_forwarding and not isinstance(is_forwarding, bool):
            raise TypeError("Expected argument 'is_forwarding' to be a bool")
        pulumi.set(__self__, "is_forwarding", is_forwarding)
        if is_listening and not isinstance(is_listening, bool):
            raise TypeError("Expected argument 'is_listening' to be a bool")
        pulumi.set(__self__, "is_listening", is_listening)
        if listening_address and not isinstance(listening_address, str):
            raise TypeError("Expected argument 'listening_address' to be a str")
        pulumi.set(__self__, "listening_address", listening_address)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if nsg_ids and not isinstance(nsg_ids, list):
            raise TypeError("Expected argument 'nsg_ids' to be a list")
        pulumi.set(__self__, "nsg_ids", nsg_ids)
        if resolver_endpoint_name and not isinstance(resolver_endpoint_name, str):
            raise TypeError("Expected argument 'resolver_endpoint_name' to be a str")
        pulumi.set(__self__, "resolver_endpoint_name", resolver_endpoint_name)
        if resolver_id and not isinstance(resolver_id, str):
            raise TypeError("Expected argument 'resolver_id' to be a str")
        pulumi.set(__self__, "resolver_id", resolver_id)
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        pulumi.set(__self__, "scope", scope)
        if self and not isinstance(self, str):
            raise TypeError("Expected argument 'self' to be a str")
        pulumi.set(__self__, "self", self)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the owning compartment. This will match the resolver that the resolver endpoint is under and will be updated if the resolver's compartment is changed.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> str:
        """
        The type of resolver endpoint. VNIC is currently the only supported type.
        """
        return pulumi.get(self, "endpoint_type")

    @property
    @pulumi.getter(name="forwardingAddress")
    def forwarding_address(self) -> str:
        """
        An IP address from which forwarded queries may be sent. For VNIC endpoints, this IP address must be part of the subnet and will be assigned by the system if unspecified when isForwarding is true.
        """
        return pulumi.get(self, "forwarding_address")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isForwarding")
    def is_forwarding(self) -> bool:
        """
        A Boolean flag indicating whether or not the resolver endpoint is for forwarding.
        """
        return pulumi.get(self, "is_forwarding")

    @property
    @pulumi.getter(name="isListening")
    def is_listening(self) -> bool:
        """
        A Boolean flag indicating whether or not the resolver endpoint is for listening.
        """
        return pulumi.get(self, "is_listening")

    @property
    @pulumi.getter(name="listeningAddress")
    def listening_address(self) -> str:
        """
        An IP address to listen to queries on. For VNIC endpoints this IP address must be part of the subnet and will be assigned by the system if unspecified when isListening is true.
        """
        return pulumi.get(self, "listening_address")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resolver endpoint. Must be unique, case-insensitive, within the resolver.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nsgIds")
    def nsg_ids(self) -> Sequence[str]:
        """
        An array of network security group OCIDs for the resolver endpoint. These must be part of the VCN that the resolver endpoint is a part of.
        """
        return pulumi.get(self, "nsg_ids")

    @property
    @pulumi.getter(name="resolverEndpointName")
    def resolver_endpoint_name(self) -> str:
        return pulumi.get(self, "resolver_endpoint_name")

    @property
    @pulumi.getter(name="resolverId")
    def resolver_id(self) -> str:
        return pulumi.get(self, "resolver_id")

    @property
    @pulumi.getter
    def scope(self) -> Optional[str]:
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def self(self) -> str:
        """
        The canonical absolute URL of the resource.
        """
        return pulumi.get(self, "self")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the resource.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        The OCID of a subnet. Must be part of the VCN that the resolver is attached to.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the resource was created in "YYYY-MM-ddThh:mm:ssZ" format with a Z offset, as defined by RFC 3339.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The date and time the resource was last updated in "YYYY-MM-ddThh:mm:ssZ" format with a Z offset, as defined by RFC 3339.
        """
        return pulumi.get(self, "time_updated")


class AwaitableGetResolverEndpointResult(GetResolverEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResolverEndpointResult(
            compartment_id=self.compartment_id,
            endpoint_type=self.endpoint_type,
            forwarding_address=self.forwarding_address,
            id=self.id,
            is_forwarding=self.is_forwarding,
            is_listening=self.is_listening,
            listening_address=self.listening_address,
            name=self.name,
            nsg_ids=self.nsg_ids,
            resolver_endpoint_name=self.resolver_endpoint_name,
            resolver_id=self.resolver_id,
            scope=self.scope,
            self=self.self,
            state=self.state,
            subnet_id=self.subnet_id,
            time_created=self.time_created,
            time_updated=self.time_updated)


def get_resolver_endpoint(resolver_endpoint_name: Optional[str] = None,
                          resolver_id: Optional[str] = None,
                          scope: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResolverEndpointResult:
    """
    This data source provides details about a specific Resolver Endpoint resource in Oracle Cloud Infrastructure DNS service.

    Gets information about a specific resolver endpoint. Note that attempting to get a resolver endpoint
    in the DELETED lifecycle state will result in a `404` response to be consistent with other operations of the
    API. Requires a `PRIVATE` scope query parameter.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_resolver_endpoint = oci.Dns.get_resolver_endpoint(resolver_endpoint_name=oci_dns_resolver_endpoint["test_resolver_endpoint"]["name"],
        resolver_id=oci_dns_resolver["test_resolver"]["id"],
        scope="PRIVATE")
    ```


    :param str resolver_endpoint_name: The name of the target resolver endpoint.
    :param str resolver_id: The OCID of the target resolver.
    :param str scope: Value must be `PRIVATE` when listing private name resolver endpoints.
    """
    __args__ = dict()
    __args__['resolverEndpointName'] = resolver_endpoint_name
    __args__['resolverId'] = resolver_id
    __args__['scope'] = scope
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Dns/getResolverEndpoint:getResolverEndpoint', __args__, opts=opts, typ=GetResolverEndpointResult).value

    return AwaitableGetResolverEndpointResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        endpoint_type=pulumi.get(__ret__, 'endpoint_type'),
        forwarding_address=pulumi.get(__ret__, 'forwarding_address'),
        id=pulumi.get(__ret__, 'id'),
        is_forwarding=pulumi.get(__ret__, 'is_forwarding'),
        is_listening=pulumi.get(__ret__, 'is_listening'),
        listening_address=pulumi.get(__ret__, 'listening_address'),
        name=pulumi.get(__ret__, 'name'),
        nsg_ids=pulumi.get(__ret__, 'nsg_ids'),
        resolver_endpoint_name=pulumi.get(__ret__, 'resolver_endpoint_name'),
        resolver_id=pulumi.get(__ret__, 'resolver_id'),
        scope=pulumi.get(__ret__, 'scope'),
        self=pulumi.get(__ret__, 'self'),
        state=pulumi.get(__ret__, 'state'),
        subnet_id=pulumi.get(__ret__, 'subnet_id'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'))


@_utilities.lift_output_func(get_resolver_endpoint)
def get_resolver_endpoint_output(resolver_endpoint_name: Optional[pulumi.Input[str]] = None,
                                 resolver_id: Optional[pulumi.Input[str]] = None,
                                 scope: Optional[pulumi.Input[Optional[str]]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResolverEndpointResult]:
    """
    This data source provides details about a specific Resolver Endpoint resource in Oracle Cloud Infrastructure DNS service.

    Gets information about a specific resolver endpoint. Note that attempting to get a resolver endpoint
    in the DELETED lifecycle state will result in a `404` response to be consistent with other operations of the
    API. Requires a `PRIVATE` scope query parameter.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_resolver_endpoint = oci.Dns.get_resolver_endpoint(resolver_endpoint_name=oci_dns_resolver_endpoint["test_resolver_endpoint"]["name"],
        resolver_id=oci_dns_resolver["test_resolver"]["id"],
        scope="PRIVATE")
    ```


    :param str resolver_endpoint_name: The name of the target resolver endpoint.
    :param str resolver_id: The OCID of the target resolver.
    :param str scope: Value must be `PRIVATE` when listing private name resolver endpoints.
    """
    ...
