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
    'GetIngressGatewayRouteTablesResult',
    'AwaitableGetIngressGatewayRouteTablesResult',
    'get_ingress_gateway_route_tables',
    'get_ingress_gateway_route_tables_output',
]

@pulumi.output_type
class GetIngressGatewayRouteTablesResult:
    """
    A collection of values returned by getIngressGatewayRouteTables.
    """
    def __init__(__self__, compartment_id=None, filters=None, id=None, ingress_gateway_id=None, ingress_gateway_route_table_collections=None, name=None, state=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ingress_gateway_id and not isinstance(ingress_gateway_id, str):
            raise TypeError("Expected argument 'ingress_gateway_id' to be a str")
        pulumi.set(__self__, "ingress_gateway_id", ingress_gateway_id)
        if ingress_gateway_route_table_collections and not isinstance(ingress_gateway_route_table_collections, list):
            raise TypeError("Expected argument 'ingress_gateway_route_table_collections' to be a list")
        pulumi.set(__self__, "ingress_gateway_route_table_collections", ingress_gateway_route_table_collections)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetIngressGatewayRouteTablesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Unique identifier that is immutable on creation.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ingressGatewayId")
    def ingress_gateway_id(self) -> Optional[str]:
        """
        The OCID of the ingress gateway.
        """
        return pulumi.get(self, "ingress_gateway_id")

    @property
    @pulumi.getter(name="ingressGatewayRouteTableCollections")
    def ingress_gateway_route_table_collections(self) -> Sequence['outputs.GetIngressGatewayRouteTablesIngressGatewayRouteTableCollectionResult']:
        """
        The list of ingress_gateway_route_table_collection.
        """
        return pulumi.get(self, "ingress_gateway_route_table_collections")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the ingress gateway host that this route should apply to.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the Resource.
        """
        return pulumi.get(self, "state")


class AwaitableGetIngressGatewayRouteTablesResult(GetIngressGatewayRouteTablesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIngressGatewayRouteTablesResult(
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            ingress_gateway_id=self.ingress_gateway_id,
            ingress_gateway_route_table_collections=self.ingress_gateway_route_table_collections,
            name=self.name,
            state=self.state)


def get_ingress_gateway_route_tables(compartment_id: Optional[str] = None,
                                     filters: Optional[Sequence[pulumi.InputType['GetIngressGatewayRouteTablesFilterArgs']]] = None,
                                     id: Optional[str] = None,
                                     ingress_gateway_id: Optional[str] = None,
                                     name: Optional[str] = None,
                                     state: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIngressGatewayRouteTablesResult:
    """
    This data source provides the list of Ingress Gateway Route Tables in Oracle Cloud Infrastructure Service Mesh service.

    Returns a list of IngressGatewayRouteTable objects.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_ingress_gateway_route_tables = oci.ServiceMesh.get_ingress_gateway_route_tables(compartment_id=var["compartment_id"],
        id=var["ingress_gateway_route_table_id"],
        ingress_gateway_id=oci_service_mesh_ingress_gateway["test_ingress_gateway"]["id"],
        name=var["ingress_gateway_route_table_name"],
        state=var["ingress_gateway_route_table_state"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str id: Unique IngressGatewayRouteTable identifier.
    :param str ingress_gateway_id: Unique IngressGateway identifier.
    :param str name: A filter to return only resources that match the entire name given.
    :param str state: A filter to return only resources that match the life cycle state given.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['ingressGatewayId'] = ingress_gateway_id
    __args__['name'] = name
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:ServiceMesh/getIngressGatewayRouteTables:getIngressGatewayRouteTables', __args__, opts=opts, typ=GetIngressGatewayRouteTablesResult).value

    return AwaitableGetIngressGatewayRouteTablesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        ingress_gateway_id=pulumi.get(__ret__, 'ingress_gateway_id'),
        ingress_gateway_route_table_collections=pulumi.get(__ret__, 'ingress_gateway_route_table_collections'),
        name=pulumi.get(__ret__, 'name'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_ingress_gateway_route_tables)
def get_ingress_gateway_route_tables_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                            filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetIngressGatewayRouteTablesFilterArgs']]]]] = None,
                                            id: Optional[pulumi.Input[Optional[str]]] = None,
                                            ingress_gateway_id: Optional[pulumi.Input[Optional[str]]] = None,
                                            name: Optional[pulumi.Input[Optional[str]]] = None,
                                            state: Optional[pulumi.Input[Optional[str]]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIngressGatewayRouteTablesResult]:
    """
    This data source provides the list of Ingress Gateway Route Tables in Oracle Cloud Infrastructure Service Mesh service.

    Returns a list of IngressGatewayRouteTable objects.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_ingress_gateway_route_tables = oci.ServiceMesh.get_ingress_gateway_route_tables(compartment_id=var["compartment_id"],
        id=var["ingress_gateway_route_table_id"],
        ingress_gateway_id=oci_service_mesh_ingress_gateway["test_ingress_gateway"]["id"],
        name=var["ingress_gateway_route_table_name"],
        state=var["ingress_gateway_route_table_state"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str id: Unique IngressGatewayRouteTable identifier.
    :param str ingress_gateway_id: Unique IngressGateway identifier.
    :param str name: A filter to return only resources that match the entire name given.
    :param str state: A filter to return only resources that match the life cycle state given.
    """
    ...
