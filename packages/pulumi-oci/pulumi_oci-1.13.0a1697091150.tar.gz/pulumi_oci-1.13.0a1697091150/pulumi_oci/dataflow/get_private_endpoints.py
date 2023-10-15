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
    'GetPrivateEndpointsResult',
    'AwaitableGetPrivateEndpointsResult',
    'get_private_endpoints',
    'get_private_endpoints_output',
]

@pulumi.output_type
class GetPrivateEndpointsResult:
    """
    A collection of values returned by getPrivateEndpoints.
    """
    def __init__(__self__, compartment_id=None, display_name=None, display_name_starts_with=None, filters=None, id=None, owner_principal_id=None, private_endpoint_collections=None, state=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if display_name_starts_with and not isinstance(display_name_starts_with, str):
            raise TypeError("Expected argument 'display_name_starts_with' to be a str")
        pulumi.set(__self__, "display_name_starts_with", display_name_starts_with)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if owner_principal_id and not isinstance(owner_principal_id, str):
            raise TypeError("Expected argument 'owner_principal_id' to be a str")
        pulumi.set(__self__, "owner_principal_id", owner_principal_id)
        if private_endpoint_collections and not isinstance(private_endpoint_collections, list):
            raise TypeError("Expected argument 'private_endpoint_collections' to be a list")
        pulumi.set(__self__, "private_endpoint_collections", private_endpoint_collections)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of a compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A user-friendly name. It does not have to be unique. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="displayNameStartsWith")
    def display_name_starts_with(self) -> Optional[str]:
        return pulumi.get(self, "display_name_starts_with")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetPrivateEndpointsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ownerPrincipalId")
    def owner_principal_id(self) -> Optional[str]:
        """
        The OCID of the user who created the resource.
        """
        return pulumi.get(self, "owner_principal_id")

    @property
    @pulumi.getter(name="privateEndpointCollections")
    def private_endpoint_collections(self) -> Sequence['outputs.GetPrivateEndpointsPrivateEndpointCollectionResult']:
        """
        The list of private_endpoint_collection.
        """
        return pulumi.get(self, "private_endpoint_collections")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of this private endpoint.
        """
        return pulumi.get(self, "state")


class AwaitableGetPrivateEndpointsResult(GetPrivateEndpointsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrivateEndpointsResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            display_name_starts_with=self.display_name_starts_with,
            filters=self.filters,
            id=self.id,
            owner_principal_id=self.owner_principal_id,
            private_endpoint_collections=self.private_endpoint_collections,
            state=self.state)


def get_private_endpoints(compartment_id: Optional[str] = None,
                          display_name: Optional[str] = None,
                          display_name_starts_with: Optional[str] = None,
                          filters: Optional[Sequence[pulumi.InputType['GetPrivateEndpointsFilterArgs']]] = None,
                          owner_principal_id: Optional[str] = None,
                          state: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrivateEndpointsResult:
    """
    This data source provides the list of Private Endpoints in Oracle Cloud Infrastructure Data Flow service.

    Lists all private endpoints in the specified compartment. The query must include compartmentId. The query may also include one other parameter. If the query does not include compartmentId, or includes compartmentId, but with two or more other parameters, an error is returned.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_private_endpoints = oci.DataFlow.get_private_endpoints(compartment_id=var["compartment_id"],
        display_name=var["private_endpoint_display_name"],
        display_name_starts_with=var["private_endpoint_display_name_starts_with"],
        owner_principal_id=var["owner_principal_id"],
        state=var["private_endpoint_state"])
    ```


    :param str compartment_id: The OCID of the compartment.
    :param str display_name: The query parameter for the Spark application name. Note: At a time only one optional filter can be used with `compartment_id` to get the list of Private Endpoint resources.
    :param str display_name_starts_with: The displayName prefix.
    :param str owner_principal_id: The OCID of the user who created the resource.
    :param str state: The LifecycleState of the private endpoint.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['displayNameStartsWith'] = display_name_starts_with
    __args__['filters'] = filters
    __args__['ownerPrincipalId'] = owner_principal_id
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataFlow/getPrivateEndpoints:getPrivateEndpoints', __args__, opts=opts, typ=GetPrivateEndpointsResult).value

    return AwaitableGetPrivateEndpointsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        display_name_starts_with=pulumi.get(__ret__, 'display_name_starts_with'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        owner_principal_id=pulumi.get(__ret__, 'owner_principal_id'),
        private_endpoint_collections=pulumi.get(__ret__, 'private_endpoint_collections'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_private_endpoints)
def get_private_endpoints_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                 display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                 display_name_starts_with: Optional[pulumi.Input[Optional[str]]] = None,
                                 filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetPrivateEndpointsFilterArgs']]]]] = None,
                                 owner_principal_id: Optional[pulumi.Input[Optional[str]]] = None,
                                 state: Optional[pulumi.Input[Optional[str]]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPrivateEndpointsResult]:
    """
    This data source provides the list of Private Endpoints in Oracle Cloud Infrastructure Data Flow service.

    Lists all private endpoints in the specified compartment. The query must include compartmentId. The query may also include one other parameter. If the query does not include compartmentId, or includes compartmentId, but with two or more other parameters, an error is returned.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_private_endpoints = oci.DataFlow.get_private_endpoints(compartment_id=var["compartment_id"],
        display_name=var["private_endpoint_display_name"],
        display_name_starts_with=var["private_endpoint_display_name_starts_with"],
        owner_principal_id=var["owner_principal_id"],
        state=var["private_endpoint_state"])
    ```


    :param str compartment_id: The OCID of the compartment.
    :param str display_name: The query parameter for the Spark application name. Note: At a time only one optional filter can be used with `compartment_id` to get the list of Private Endpoint resources.
    :param str display_name_starts_with: The displayName prefix.
    :param str owner_principal_id: The OCID of the user who created the resource.
    :param str state: The LifecycleState of the private endpoint.
    """
    ...
