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
    'GetAgentsResult',
    'AwaitableGetAgentsResult',
    'get_agents',
    'get_agents_output',
]

@pulumi.output_type
class GetAgentsResult:
    """
    A collection of values returned by getAgents.
    """
    def __init__(__self__, agent_collections=None, compartment_id=None, display_name=None, filters=None, id=None, state=None):
        if agent_collections and not isinstance(agent_collections, list):
            raise TypeError("Expected argument 'agent_collections' to be a list")
        pulumi.set(__self__, "agent_collections", agent_collections)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="agentCollections")
    def agent_collections(self) -> Sequence['outputs.GetAgentsAgentCollectionResult']:
        """
        The list of agent_collection.
        """
        return pulumi.get(self, "agent_collections")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        OCID of the compartment
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        ODMS Agent name
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetAgentsFilterResult']]:
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
    def state(self) -> Optional[str]:
        """
        The current state of the ODMS on-premises Agent.
        """
        return pulumi.get(self, "state")


class AwaitableGetAgentsResult(GetAgentsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAgentsResult(
            agent_collections=self.agent_collections,
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            state=self.state)


def get_agents(compartment_id: Optional[str] = None,
               display_name: Optional[str] = None,
               filters: Optional[Sequence[pulumi.InputType['GetAgentsFilterArgs']]] = None,
               state: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAgentsResult:
    """
    This data source provides the list of Agents in Oracle Cloud Infrastructure Database Migration service.

    Display the name of all the existing ODMS Agents in the server.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_agents = oci.DatabaseMigration.get_agents(compartment_id=var["compartment_id"],
        display_name=var["agent_display_name"],
        state=var["agent_state"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str state: The current state of the Database Migration Deployment.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseMigration/getAgents:getAgents', __args__, opts=opts, typ=GetAgentsResult).value

    return AwaitableGetAgentsResult(
        agent_collections=pulumi.get(__ret__, 'agent_collections'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_agents)
def get_agents_output(compartment_id: Optional[pulumi.Input[str]] = None,
                      display_name: Optional[pulumi.Input[Optional[str]]] = None,
                      filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetAgentsFilterArgs']]]]] = None,
                      state: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAgentsResult]:
    """
    This data source provides the list of Agents in Oracle Cloud Infrastructure Database Migration service.

    Display the name of all the existing ODMS Agents in the server.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_agents = oci.DatabaseMigration.get_agents(compartment_id=var["compartment_id"],
        display_name=var["agent_display_name"],
        state=var["agent_state"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str state: The current state of the Database Migration Deployment.
    """
    ...
