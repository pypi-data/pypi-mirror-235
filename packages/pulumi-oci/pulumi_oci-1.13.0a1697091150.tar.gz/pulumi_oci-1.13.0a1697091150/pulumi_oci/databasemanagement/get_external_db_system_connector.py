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

__all__ = [
    'GetExternalDbSystemConnectorResult',
    'AwaitableGetExternalDbSystemConnectorResult',
    'get_external_db_system_connector',
    'get_external_db_system_connector_output',
]

@pulumi.output_type
class GetExternalDbSystemConnectorResult:
    """
    A collection of values returned by getExternalDbSystemConnector.
    """
    def __init__(__self__, agent_id=None, compartment_id=None, connection_failure_message=None, connection_infos=None, connection_status=None, connector_type=None, display_name=None, external_db_system_connector_id=None, external_db_system_id=None, id=None, lifecycle_details=None, state=None, time_connection_status_last_updated=None, time_created=None, time_updated=None):
        if agent_id and not isinstance(agent_id, str):
            raise TypeError("Expected argument 'agent_id' to be a str")
        pulumi.set(__self__, "agent_id", agent_id)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if connection_failure_message and not isinstance(connection_failure_message, str):
            raise TypeError("Expected argument 'connection_failure_message' to be a str")
        pulumi.set(__self__, "connection_failure_message", connection_failure_message)
        if connection_infos and not isinstance(connection_infos, list):
            raise TypeError("Expected argument 'connection_infos' to be a list")
        pulumi.set(__self__, "connection_infos", connection_infos)
        if connection_status and not isinstance(connection_status, str):
            raise TypeError("Expected argument 'connection_status' to be a str")
        pulumi.set(__self__, "connection_status", connection_status)
        if connector_type and not isinstance(connector_type, str):
            raise TypeError("Expected argument 'connector_type' to be a str")
        pulumi.set(__self__, "connector_type", connector_type)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if external_db_system_connector_id and not isinstance(external_db_system_connector_id, str):
            raise TypeError("Expected argument 'external_db_system_connector_id' to be a str")
        pulumi.set(__self__, "external_db_system_connector_id", external_db_system_connector_id)
        if external_db_system_id and not isinstance(external_db_system_id, str):
            raise TypeError("Expected argument 'external_db_system_id' to be a str")
        pulumi.set(__self__, "external_db_system_id", external_db_system_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if time_connection_status_last_updated and not isinstance(time_connection_status_last_updated, str):
            raise TypeError("Expected argument 'time_connection_status_last_updated' to be a str")
        pulumi.set(__self__, "time_connection_status_last_updated", time_connection_status_last_updated)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the management agent used for the external DB system connector.
        """
        return pulumi.get(self, "agent_id")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="connectionFailureMessage")
    def connection_failure_message(self) -> str:
        """
        The error message indicating the reason for connection failure or `null` if the connection was successful.
        """
        return pulumi.get(self, "connection_failure_message")

    @property
    @pulumi.getter(name="connectionInfos")
    def connection_infos(self) -> Sequence['outputs.GetExternalDbSystemConnectorConnectionInfoResult']:
        """
        The connection details required to connect to an external DB system component.
        """
        return pulumi.get(self, "connection_infos")

    @property
    @pulumi.getter(name="connectionStatus")
    def connection_status(self) -> str:
        """
        The status of connectivity to the external DB system component.
        """
        return pulumi.get(self, "connection_status")

    @property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> str:
        """
        The type of connector.
        """
        return pulumi.get(self, "connector_type")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The user-friendly name for the external connector. The name does not have to be unique.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="externalDbSystemConnectorId")
    def external_db_system_connector_id(self) -> str:
        return pulumi.get(self, "external_db_system_connector_id")

    @property
    @pulumi.getter(name="externalDbSystemId")
    def external_db_system_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system that the connector is a part of.
        """
        return pulumi.get(self, "external_db_system_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system connector.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        Additional information about the current lifecycle state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current lifecycle state of the external DB system connector.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeConnectionStatusLastUpdated")
    def time_connection_status_last_updated(self) -> str:
        """
        The date and time the connectionStatus of the external DB system connector was last updated.
        """
        return pulumi.get(self, "time_connection_status_last_updated")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the external DB system connector was created.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The date and time the external DB system connector was last updated.
        """
        return pulumi.get(self, "time_updated")


class AwaitableGetExternalDbSystemConnectorResult(GetExternalDbSystemConnectorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExternalDbSystemConnectorResult(
            agent_id=self.agent_id,
            compartment_id=self.compartment_id,
            connection_failure_message=self.connection_failure_message,
            connection_infos=self.connection_infos,
            connection_status=self.connection_status,
            connector_type=self.connector_type,
            display_name=self.display_name,
            external_db_system_connector_id=self.external_db_system_connector_id,
            external_db_system_id=self.external_db_system_id,
            id=self.id,
            lifecycle_details=self.lifecycle_details,
            state=self.state,
            time_connection_status_last_updated=self.time_connection_status_last_updated,
            time_created=self.time_created,
            time_updated=self.time_updated)


def get_external_db_system_connector(external_db_system_connector_id: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExternalDbSystemConnectorResult:
    """
    This data source provides details about a specific External Db System Connector resource in Oracle Cloud Infrastructure Database Management service.

    Gets the details for the external connector specified by `externalDbSystemConnectorId`.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_external_db_system_connector = oci.DatabaseManagement.get_external_db_system_connector(external_db_system_connector_id=oci_database_management_external_db_system_connector["test_external_db_system_connector"]["id"])
    ```


    :param str external_db_system_connector_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external connector.
    """
    __args__ = dict()
    __args__['externalDbSystemConnectorId'] = external_db_system_connector_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseManagement/getExternalDbSystemConnector:getExternalDbSystemConnector', __args__, opts=opts, typ=GetExternalDbSystemConnectorResult).value

    return AwaitableGetExternalDbSystemConnectorResult(
        agent_id=pulumi.get(__ret__, 'agent_id'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        connection_failure_message=pulumi.get(__ret__, 'connection_failure_message'),
        connection_infos=pulumi.get(__ret__, 'connection_infos'),
        connection_status=pulumi.get(__ret__, 'connection_status'),
        connector_type=pulumi.get(__ret__, 'connector_type'),
        display_name=pulumi.get(__ret__, 'display_name'),
        external_db_system_connector_id=pulumi.get(__ret__, 'external_db_system_connector_id'),
        external_db_system_id=pulumi.get(__ret__, 'external_db_system_id'),
        id=pulumi.get(__ret__, 'id'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        state=pulumi.get(__ret__, 'state'),
        time_connection_status_last_updated=pulumi.get(__ret__, 'time_connection_status_last_updated'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'))


@_utilities.lift_output_func(get_external_db_system_connector)
def get_external_db_system_connector_output(external_db_system_connector_id: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExternalDbSystemConnectorResult]:
    """
    This data source provides details about a specific External Db System Connector resource in Oracle Cloud Infrastructure Database Management service.

    Gets the details for the external connector specified by `externalDbSystemConnectorId`.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_external_db_system_connector = oci.DatabaseManagement.get_external_db_system_connector(external_db_system_connector_id=oci_database_management_external_db_system_connector["test_external_db_system_connector"]["id"])
    ```


    :param str external_db_system_connector_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external connector.
    """
    ...
