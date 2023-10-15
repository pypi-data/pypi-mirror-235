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
    'GetVirtualServiceRouteTablesResult',
    'AwaitableGetVirtualServiceRouteTablesResult',
    'get_virtual_service_route_tables',
    'get_virtual_service_route_tables_output',
]

@pulumi.output_type
class GetVirtualServiceRouteTablesResult:
    """
    A collection of values returned by getVirtualServiceRouteTables.
    """
    def __init__(__self__, compartment_id=None, filters=None, id=None, name=None, state=None, virtual_service_id=None, virtual_service_route_table_collections=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if virtual_service_id and not isinstance(virtual_service_id, str):
            raise TypeError("Expected argument 'virtual_service_id' to be a str")
        pulumi.set(__self__, "virtual_service_id", virtual_service_id)
        if virtual_service_route_table_collections and not isinstance(virtual_service_route_table_collections, list):
            raise TypeError("Expected argument 'virtual_service_route_table_collections' to be a list")
        pulumi.set(__self__, "virtual_service_route_table_collections", virtual_service_route_table_collections)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetVirtualServiceRouteTablesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Unique identifier that is immutable on creation.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        A user-friendly name. The name must be unique within the same virtual service and cannot be changed after creation. Avoid entering confidential information.  Example: `My unique resource name`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the Resource.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="virtualServiceId")
    def virtual_service_id(self) -> Optional[str]:
        """
        The OCID of the virtual service in which this virtual service route table is created.
        """
        return pulumi.get(self, "virtual_service_id")

    @property
    @pulumi.getter(name="virtualServiceRouteTableCollections")
    def virtual_service_route_table_collections(self) -> Sequence['outputs.GetVirtualServiceRouteTablesVirtualServiceRouteTableCollectionResult']:
        """
        The list of virtual_service_route_table_collection.
        """
        return pulumi.get(self, "virtual_service_route_table_collections")


class AwaitableGetVirtualServiceRouteTablesResult(GetVirtualServiceRouteTablesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualServiceRouteTablesResult(
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            name=self.name,
            state=self.state,
            virtual_service_id=self.virtual_service_id,
            virtual_service_route_table_collections=self.virtual_service_route_table_collections)


def get_virtual_service_route_tables(compartment_id: Optional[str] = None,
                                     filters: Optional[Sequence[pulumi.InputType['GetVirtualServiceRouteTablesFilterArgs']]] = None,
                                     id: Optional[str] = None,
                                     name: Optional[str] = None,
                                     state: Optional[str] = None,
                                     virtual_service_id: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualServiceRouteTablesResult:
    """
    This data source provides the list of Virtual Service Route Tables in Oracle Cloud Infrastructure Service Mesh service.

    Returns a list of VirtualServiceRouteTable objects.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_virtual_service_route_tables = oci.ServiceMesh.get_virtual_service_route_tables(compartment_id=var["compartment_id"],
        id=var["virtual_service_route_table_id"],
        name=var["virtual_service_route_table_name"],
        state=var["virtual_service_route_table_state"],
        virtual_service_id=oci_service_mesh_virtual_service["test_virtual_service"]["id"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str id: Unique VirtualServiceRouteTable identifier.
    :param str name: A filter to return only resources that match the entire name given.
    :param str state: A filter to return only resources that match the life cycle state given.
    :param str virtual_service_id: Unique VirtualService identifier.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['name'] = name
    __args__['state'] = state
    __args__['virtualServiceId'] = virtual_service_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:ServiceMesh/getVirtualServiceRouteTables:getVirtualServiceRouteTables', __args__, opts=opts, typ=GetVirtualServiceRouteTablesResult).value

    return AwaitableGetVirtualServiceRouteTablesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        state=pulumi.get(__ret__, 'state'),
        virtual_service_id=pulumi.get(__ret__, 'virtual_service_id'),
        virtual_service_route_table_collections=pulumi.get(__ret__, 'virtual_service_route_table_collections'))


@_utilities.lift_output_func(get_virtual_service_route_tables)
def get_virtual_service_route_tables_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                            filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetVirtualServiceRouteTablesFilterArgs']]]]] = None,
                                            id: Optional[pulumi.Input[Optional[str]]] = None,
                                            name: Optional[pulumi.Input[Optional[str]]] = None,
                                            state: Optional[pulumi.Input[Optional[str]]] = None,
                                            virtual_service_id: Optional[pulumi.Input[Optional[str]]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualServiceRouteTablesResult]:
    """
    This data source provides the list of Virtual Service Route Tables in Oracle Cloud Infrastructure Service Mesh service.

    Returns a list of VirtualServiceRouteTable objects.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_virtual_service_route_tables = oci.ServiceMesh.get_virtual_service_route_tables(compartment_id=var["compartment_id"],
        id=var["virtual_service_route_table_id"],
        name=var["virtual_service_route_table_name"],
        state=var["virtual_service_route_table_state"],
        virtual_service_id=oci_service_mesh_virtual_service["test_virtual_service"]["id"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str id: Unique VirtualServiceRouteTable identifier.
    :param str name: A filter to return only resources that match the entire name given.
    :param str state: A filter to return only resources that match the life cycle state given.
    :param str virtual_service_id: Unique VirtualService identifier.
    """
    ...
