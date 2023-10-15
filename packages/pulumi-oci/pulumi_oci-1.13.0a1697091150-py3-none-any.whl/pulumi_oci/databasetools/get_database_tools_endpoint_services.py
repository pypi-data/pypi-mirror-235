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
    'GetDatabaseToolsEndpointServicesResult',
    'AwaitableGetDatabaseToolsEndpointServicesResult',
    'get_database_tools_endpoint_services',
    'get_database_tools_endpoint_services_output',
]

@pulumi.output_type
class GetDatabaseToolsEndpointServicesResult:
    """
    A collection of values returned by getDatabaseToolsEndpointServices.
    """
    def __init__(__self__, compartment_id=None, database_tools_endpoint_service_collections=None, display_name=None, filters=None, id=None, name=None, state=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if database_tools_endpoint_service_collections and not isinstance(database_tools_endpoint_service_collections, list):
            raise TypeError("Expected argument 'database_tools_endpoint_service_collections' to be a list")
        pulumi.set(__self__, "database_tools_endpoint_service_collections", database_tools_endpoint_service_collections)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
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

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the Database Tools Endpoint Service.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="databaseToolsEndpointServiceCollections")
    def database_tools_endpoint_service_collections(self) -> Sequence['outputs.GetDatabaseToolsEndpointServicesDatabaseToolsEndpointServiceCollectionResult']:
        """
        The list of database_tools_endpoint_service_collection.
        """
        return pulumi.get(self, "database_tools_endpoint_service_collections")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetDatabaseToolsEndpointServicesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        A unique, non-changeable resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the Database Tools Endpoint Service.
        """
        return pulumi.get(self, "state")


class AwaitableGetDatabaseToolsEndpointServicesResult(GetDatabaseToolsEndpointServicesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseToolsEndpointServicesResult(
            compartment_id=self.compartment_id,
            database_tools_endpoint_service_collections=self.database_tools_endpoint_service_collections,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            name=self.name,
            state=self.state)


def get_database_tools_endpoint_services(compartment_id: Optional[str] = None,
                                         display_name: Optional[str] = None,
                                         filters: Optional[Sequence[pulumi.InputType['GetDatabaseToolsEndpointServicesFilterArgs']]] = None,
                                         name: Optional[str] = None,
                                         state: Optional[str] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabaseToolsEndpointServicesResult:
    """
    This data source provides the list of Database Tools Endpoint Services in Oracle Cloud Infrastructure Database Tools service.

    Returns a list of Database Tools endpoint services.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_database_tools_endpoint_services = oci.DatabaseTools.get_database_tools_endpoint_services(compartment_id=var["compartment_id"],
        display_name=var["database_tools_endpoint_service_display_name"],
        name=var["database_tools_endpoint_service_name"],
        state=var["database_tools_endpoint_service_state"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire specified display name.
    :param str name: A filter to return only resources that match the entire specified name.
    :param str state: A filter to return only resources their `lifecycleState` matches the specified `lifecycleState`.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['name'] = name
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseTools/getDatabaseToolsEndpointServices:getDatabaseToolsEndpointServices', __args__, opts=opts, typ=GetDatabaseToolsEndpointServicesResult).value

    return AwaitableGetDatabaseToolsEndpointServicesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        database_tools_endpoint_service_collections=pulumi.get(__ret__, 'database_tools_endpoint_service_collections'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_database_tools_endpoint_services)
def get_database_tools_endpoint_services_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                                display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                                filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDatabaseToolsEndpointServicesFilterArgs']]]]] = None,
                                                name: Optional[pulumi.Input[Optional[str]]] = None,
                                                state: Optional[pulumi.Input[Optional[str]]] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatabaseToolsEndpointServicesResult]:
    """
    This data source provides the list of Database Tools Endpoint Services in Oracle Cloud Infrastructure Database Tools service.

    Returns a list of Database Tools endpoint services.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_database_tools_endpoint_services = oci.DatabaseTools.get_database_tools_endpoint_services(compartment_id=var["compartment_id"],
        display_name=var["database_tools_endpoint_service_display_name"],
        name=var["database_tools_endpoint_service_name"],
        state=var["database_tools_endpoint_service_state"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire specified display name.
    :param str name: A filter to return only resources that match the entire specified name.
    :param str state: A filter to return only resources their `lifecycleState` matches the specified `lifecycleState`.
    """
    ...
