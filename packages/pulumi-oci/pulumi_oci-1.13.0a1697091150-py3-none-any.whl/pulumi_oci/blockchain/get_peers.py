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

__all__ = [
    'GetPeersResult',
    'AwaitableGetPeersResult',
    'get_peers',
    'get_peers_output',
]

@pulumi.output_type
class GetPeersResult:
    """
    A collection of values returned by getPeers.
    """
    def __init__(__self__, blockchain_platform_id=None, display_name=None, filters=None, id=None, peer_collections=None):
        if blockchain_platform_id and not isinstance(blockchain_platform_id, str):
            raise TypeError("Expected argument 'blockchain_platform_id' to be a str")
        pulumi.set(__self__, "blockchain_platform_id", blockchain_platform_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if peer_collections and not isinstance(peer_collections, list):
            raise TypeError("Expected argument 'peer_collections' to be a list")
        pulumi.set(__self__, "peer_collections", peer_collections)

    @property
    @pulumi.getter(name="blockchainPlatformId")
    def blockchain_platform_id(self) -> str:
        return pulumi.get(self, "blockchain_platform_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetPeersFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="peerCollections")
    def peer_collections(self) -> Sequence['outputs.GetPeersPeerCollectionResult']:
        """
        The list of peer_collection.
        """
        return pulumi.get(self, "peer_collections")


class AwaitableGetPeersResult(GetPeersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPeersResult(
            blockchain_platform_id=self.blockchain_platform_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            peer_collections=self.peer_collections)


def get_peers(blockchain_platform_id: Optional[str] = None,
              display_name: Optional[str] = None,
              filters: Optional[Sequence[pulumi.InputType['GetPeersFilterArgs']]] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPeersResult:
    """
    This data source provides the list of Peers in Oracle Cloud Infrastructure Blockchain service.

    List Blockchain Platform Peers

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_peers = oci.Blockchain.get_peers(blockchain_platform_id=oci_blockchain_blockchain_platform["test_blockchain_platform"]["id"],
        display_name=var["peer_display_name"])
    ```


    :param str blockchain_platform_id: Unique service identifier.
    :param str display_name: A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`
    """
    __args__ = dict()
    __args__['blockchainPlatformId'] = blockchain_platform_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Blockchain/getPeers:getPeers', __args__, opts=opts, typ=GetPeersResult).value

    return AwaitableGetPeersResult(
        blockchain_platform_id=pulumi.get(__ret__, 'blockchain_platform_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        peer_collections=pulumi.get(__ret__, 'peer_collections'))


@_utilities.lift_output_func(get_peers)
def get_peers_output(blockchain_platform_id: Optional[pulumi.Input[str]] = None,
                     display_name: Optional[pulumi.Input[Optional[str]]] = None,
                     filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetPeersFilterArgs']]]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPeersResult]:
    """
    This data source provides the list of Peers in Oracle Cloud Infrastructure Blockchain service.

    List Blockchain Platform Peers

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_peers = oci.Blockchain.get_peers(blockchain_platform_id=oci_blockchain_blockchain_platform["test_blockchain_platform"]["id"],
        display_name=var["peer_display_name"])
    ```


    :param str blockchain_platform_id: Unique service identifier.
    :param str display_name: A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`
    """
    ...
