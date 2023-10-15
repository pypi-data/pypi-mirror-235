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

__all__ = ['ExternalExadataStorageConnectorArgs', 'ExternalExadataStorageConnector']

@pulumi.input_type
class ExternalExadataStorageConnectorArgs:
    def __init__(__self__, *,
                 agent_id: pulumi.Input[str],
                 connection_uri: pulumi.Input[str],
                 connector_name: pulumi.Input[str],
                 credential_info: pulumi.Input['ExternalExadataStorageConnectorCredentialInfoArgs'],
                 storage_server_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a ExternalExadataStorageConnector resource.
        :param pulumi.Input[str] agent_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the agent for the Exadata storage server.
        :param pulumi.Input[str] connection_uri: (Updatable) The unique string of the connection. For example, "https://<storage-server-name>/MS/RESTService/".
        :param pulumi.Input[str] connector_name: (Updatable) The name of the Exadata storage server connector.
        :param pulumi.Input['ExternalExadataStorageConnectorCredentialInfoArgs'] credential_info: (Updatable) The user credential information.
        :param pulumi.Input[str] storage_server_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Exadata storage server.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ExternalExadataStorageConnectorArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            agent_id=agent_id,
            connection_uri=connection_uri,
            connector_name=connector_name,
            credential_info=credential_info,
            storage_server_id=storage_server_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             agent_id: pulumi.Input[str],
             connection_uri: pulumi.Input[str],
             connector_name: pulumi.Input[str],
             credential_info: pulumi.Input['ExternalExadataStorageConnectorCredentialInfoArgs'],
             storage_server_id: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("agent_id", agent_id)
        _setter("connection_uri", connection_uri)
        _setter("connector_name", connector_name)
        _setter("credential_info", credential_info)
        _setter("storage_server_id", storage_server_id)

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Input[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the agent for the Exadata storage server.
        """
        return pulumi.get(self, "agent_id")

    @agent_id.setter
    def agent_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "agent_id", value)

    @property
    @pulumi.getter(name="connectionUri")
    def connection_uri(self) -> pulumi.Input[str]:
        """
        (Updatable) The unique string of the connection. For example, "https://<storage-server-name>/MS/RESTService/".
        """
        return pulumi.get(self, "connection_uri")

    @connection_uri.setter
    def connection_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "connection_uri", value)

    @property
    @pulumi.getter(name="connectorName")
    def connector_name(self) -> pulumi.Input[str]:
        """
        (Updatable) The name of the Exadata storage server connector.
        """
        return pulumi.get(self, "connector_name")

    @connector_name.setter
    def connector_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "connector_name", value)

    @property
    @pulumi.getter(name="credentialInfo")
    def credential_info(self) -> pulumi.Input['ExternalExadataStorageConnectorCredentialInfoArgs']:
        """
        (Updatable) The user credential information.
        """
        return pulumi.get(self, "credential_info")

    @credential_info.setter
    def credential_info(self, value: pulumi.Input['ExternalExadataStorageConnectorCredentialInfoArgs']):
        pulumi.set(self, "credential_info", value)

    @property
    @pulumi.getter(name="storageServerId")
    def storage_server_id(self) -> pulumi.Input[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Exadata storage server.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "storage_server_id")

    @storage_server_id.setter
    def storage_server_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_server_id", value)


@pulumi.input_type
class _ExternalExadataStorageConnectorState:
    def __init__(__self__, *,
                 additional_details: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 agent_id: Optional[pulumi.Input[str]] = None,
                 connection_uri: Optional[pulumi.Input[str]] = None,
                 connector_name: Optional[pulumi.Input[str]] = None,
                 credential_info: Optional[pulumi.Input['ExternalExadataStorageConnectorCredentialInfoArgs']] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 exadata_infrastructure_id: Optional[pulumi.Input[str]] = None,
                 internal_id: Optional[pulumi.Input[str]] = None,
                 lifecycle_details: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 storage_server_id: Optional[pulumi.Input[str]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 time_updated: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ExternalExadataStorageConnector resources.
        :param pulumi.Input[Mapping[str, Any]] additional_details: The additional details of the resource defined in `{"key": "value"}` format. Example: `{"bar-key": "value"}`
        :param pulumi.Input[str] agent_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the agent for the Exadata storage server.
        :param pulumi.Input[str] connection_uri: (Updatable) The unique string of the connection. For example, "https://<storage-server-name>/MS/RESTService/".
        :param pulumi.Input[str] connector_name: (Updatable) The name of the Exadata storage server connector.
        :param pulumi.Input['ExternalExadataStorageConnectorCredentialInfoArgs'] credential_info: (Updatable) The user credential information.
        :param pulumi.Input[str] display_name: The name of the Exadata resource. English letters, numbers, "-", "_" and "." only.
        :param pulumi.Input[str] exadata_infrastructure_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Exadata infrastructure.
        :param pulumi.Input[str] internal_id: The internal ID of the Exadata resource.
        :param pulumi.Input[str] lifecycle_details: The details of the lifecycle state of the Exadata resource.
        :param pulumi.Input[str] state: The current lifecycle state of the database resource.
        :param pulumi.Input[str] status: The status of the Exadata resource.
        :param pulumi.Input[str] storage_server_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Exadata storage server.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] time_created: The timestamp of the creation of the Exadata resource.
        :param pulumi.Input[str] time_updated: The timestamp of the last update of the Exadata resource.
        :param pulumi.Input[str] version: The version of the Exadata resource.
        """
        _ExternalExadataStorageConnectorState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            additional_details=additional_details,
            agent_id=agent_id,
            connection_uri=connection_uri,
            connector_name=connector_name,
            credential_info=credential_info,
            display_name=display_name,
            exadata_infrastructure_id=exadata_infrastructure_id,
            internal_id=internal_id,
            lifecycle_details=lifecycle_details,
            state=state,
            status=status,
            storage_server_id=storage_server_id,
            time_created=time_created,
            time_updated=time_updated,
            version=version,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             additional_details: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             agent_id: Optional[pulumi.Input[str]] = None,
             connection_uri: Optional[pulumi.Input[str]] = None,
             connector_name: Optional[pulumi.Input[str]] = None,
             credential_info: Optional[pulumi.Input['ExternalExadataStorageConnectorCredentialInfoArgs']] = None,
             display_name: Optional[pulumi.Input[str]] = None,
             exadata_infrastructure_id: Optional[pulumi.Input[str]] = None,
             internal_id: Optional[pulumi.Input[str]] = None,
             lifecycle_details: Optional[pulumi.Input[str]] = None,
             state: Optional[pulumi.Input[str]] = None,
             status: Optional[pulumi.Input[str]] = None,
             storage_server_id: Optional[pulumi.Input[str]] = None,
             time_created: Optional[pulumi.Input[str]] = None,
             time_updated: Optional[pulumi.Input[str]] = None,
             version: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if additional_details is not None:
            _setter("additional_details", additional_details)
        if agent_id is not None:
            _setter("agent_id", agent_id)
        if connection_uri is not None:
            _setter("connection_uri", connection_uri)
        if connector_name is not None:
            _setter("connector_name", connector_name)
        if credential_info is not None:
            _setter("credential_info", credential_info)
        if display_name is not None:
            _setter("display_name", display_name)
        if exadata_infrastructure_id is not None:
            _setter("exadata_infrastructure_id", exadata_infrastructure_id)
        if internal_id is not None:
            _setter("internal_id", internal_id)
        if lifecycle_details is not None:
            _setter("lifecycle_details", lifecycle_details)
        if state is not None:
            _setter("state", state)
        if status is not None:
            _setter("status", status)
        if storage_server_id is not None:
            _setter("storage_server_id", storage_server_id)
        if time_created is not None:
            _setter("time_created", time_created)
        if time_updated is not None:
            _setter("time_updated", time_updated)
        if version is not None:
            _setter("version", version)

    @property
    @pulumi.getter(name="additionalDetails")
    def additional_details(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        The additional details of the resource defined in `{"key": "value"}` format. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "additional_details")

    @additional_details.setter
    def additional_details(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "additional_details", value)

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the agent for the Exadata storage server.
        """
        return pulumi.get(self, "agent_id")

    @agent_id.setter
    def agent_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "agent_id", value)

    @property
    @pulumi.getter(name="connectionUri")
    def connection_uri(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The unique string of the connection. For example, "https://<storage-server-name>/MS/RESTService/".
        """
        return pulumi.get(self, "connection_uri")

    @connection_uri.setter
    def connection_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_uri", value)

    @property
    @pulumi.getter(name="connectorName")
    def connector_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The name of the Exadata storage server connector.
        """
        return pulumi.get(self, "connector_name")

    @connector_name.setter
    def connector_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connector_name", value)

    @property
    @pulumi.getter(name="credentialInfo")
    def credential_info(self) -> Optional[pulumi.Input['ExternalExadataStorageConnectorCredentialInfoArgs']]:
        """
        (Updatable) The user credential information.
        """
        return pulumi.get(self, "credential_info")

    @credential_info.setter
    def credential_info(self, value: Optional[pulumi.Input['ExternalExadataStorageConnectorCredentialInfoArgs']]):
        pulumi.set(self, "credential_info", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Exadata resource. English letters, numbers, "-", "_" and "." only.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="exadataInfrastructureId")
    def exadata_infrastructure_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Exadata infrastructure.
        """
        return pulumi.get(self, "exadata_infrastructure_id")

    @exadata_infrastructure_id.setter
    def exadata_infrastructure_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "exadata_infrastructure_id", value)

    @property
    @pulumi.getter(name="internalId")
    def internal_id(self) -> Optional[pulumi.Input[str]]:
        """
        The internal ID of the Exadata resource.
        """
        return pulumi.get(self, "internal_id")

    @internal_id.setter
    def internal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "internal_id", value)

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> Optional[pulumi.Input[str]]:
        """
        The details of the lifecycle state of the Exadata resource.
        """
        return pulumi.get(self, "lifecycle_details")

    @lifecycle_details.setter
    def lifecycle_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_details", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current lifecycle state of the database resource.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the Exadata resource.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="storageServerId")
    def storage_server_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Exadata storage server.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "storage_server_id")

    @storage_server_id.setter
    def storage_server_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_server_id", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp of the creation of the Exadata resource.
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp of the last update of the Exadata resource.
        """
        return pulumi.get(self, "time_updated")

    @time_updated.setter
    def time_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_updated", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the Exadata resource.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class ExternalExadataStorageConnector(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_id: Optional[pulumi.Input[str]] = None,
                 connection_uri: Optional[pulumi.Input[str]] = None,
                 connector_name: Optional[pulumi.Input[str]] = None,
                 credential_info: Optional[pulumi.Input[pulumi.InputType['ExternalExadataStorageConnectorCredentialInfoArgs']]] = None,
                 storage_server_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the External Exadata Storage Connector resource in Oracle Cloud Infrastructure Database Management service.

        Creates the Exadata storage server connector after validating the connection information.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_external_exadata_storage_connector = oci.database_management.ExternalExadataStorageConnector("testExternalExadataStorageConnector",
            agent_id=oci_cloud_bridge_agent["test_agent"]["id"],
            connection_uri=var["external_exadata_storage_connector_connection_uri"],
            connector_name=var["external_exadata_storage_connector_connector_name"],
            credential_info=oci.database_management.ExternalExadataStorageConnectorCredentialInfoArgs(
                password=var["external_exadata_storage_connector_credential_info_password"],
                username=var["external_exadata_storage_connector_credential_info_username"],
                ssl_trust_store_location=var["external_exadata_storage_connector_credential_info_ssl_trust_store_location"],
                ssl_trust_store_password=var["external_exadata_storage_connector_credential_info_ssl_trust_store_password"],
                ssl_trust_store_type=var["external_exadata_storage_connector_credential_info_ssl_trust_store_type"],
            ),
            storage_server_id=oci_database_management_storage_server["test_storage_server"]["id"])
        ```

        ## Import

        ExternalExadataStorageConnectors can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:DatabaseManagement/externalExadataStorageConnector:ExternalExadataStorageConnector test_external_exadata_storage_connector "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] agent_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the agent for the Exadata storage server.
        :param pulumi.Input[str] connection_uri: (Updatable) The unique string of the connection. For example, "https://<storage-server-name>/MS/RESTService/".
        :param pulumi.Input[str] connector_name: (Updatable) The name of the Exadata storage server connector.
        :param pulumi.Input[pulumi.InputType['ExternalExadataStorageConnectorCredentialInfoArgs']] credential_info: (Updatable) The user credential information.
        :param pulumi.Input[str] storage_server_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Exadata storage server.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExternalExadataStorageConnectorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the External Exadata Storage Connector resource in Oracle Cloud Infrastructure Database Management service.

        Creates the Exadata storage server connector after validating the connection information.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_external_exadata_storage_connector = oci.database_management.ExternalExadataStorageConnector("testExternalExadataStorageConnector",
            agent_id=oci_cloud_bridge_agent["test_agent"]["id"],
            connection_uri=var["external_exadata_storage_connector_connection_uri"],
            connector_name=var["external_exadata_storage_connector_connector_name"],
            credential_info=oci.database_management.ExternalExadataStorageConnectorCredentialInfoArgs(
                password=var["external_exadata_storage_connector_credential_info_password"],
                username=var["external_exadata_storage_connector_credential_info_username"],
                ssl_trust_store_location=var["external_exadata_storage_connector_credential_info_ssl_trust_store_location"],
                ssl_trust_store_password=var["external_exadata_storage_connector_credential_info_ssl_trust_store_password"],
                ssl_trust_store_type=var["external_exadata_storage_connector_credential_info_ssl_trust_store_type"],
            ),
            storage_server_id=oci_database_management_storage_server["test_storage_server"]["id"])
        ```

        ## Import

        ExternalExadataStorageConnectors can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:DatabaseManagement/externalExadataStorageConnector:ExternalExadataStorageConnector test_external_exadata_storage_connector "id"
        ```

        :param str resource_name: The name of the resource.
        :param ExternalExadataStorageConnectorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExternalExadataStorageConnectorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ExternalExadataStorageConnectorArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_id: Optional[pulumi.Input[str]] = None,
                 connection_uri: Optional[pulumi.Input[str]] = None,
                 connector_name: Optional[pulumi.Input[str]] = None,
                 credential_info: Optional[pulumi.Input[pulumi.InputType['ExternalExadataStorageConnectorCredentialInfoArgs']]] = None,
                 storage_server_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ExternalExadataStorageConnectorArgs.__new__(ExternalExadataStorageConnectorArgs)

            if agent_id is None and not opts.urn:
                raise TypeError("Missing required property 'agent_id'")
            __props__.__dict__["agent_id"] = agent_id
            if connection_uri is None and not opts.urn:
                raise TypeError("Missing required property 'connection_uri'")
            __props__.__dict__["connection_uri"] = connection_uri
            if connector_name is None and not opts.urn:
                raise TypeError("Missing required property 'connector_name'")
            __props__.__dict__["connector_name"] = connector_name
            if credential_info is not None and not isinstance(credential_info, ExternalExadataStorageConnectorCredentialInfoArgs):
                credential_info = credential_info or {}
                def _setter(key, value):
                    credential_info[key] = value
                ExternalExadataStorageConnectorCredentialInfoArgs._configure(_setter, **credential_info)
            if credential_info is None and not opts.urn:
                raise TypeError("Missing required property 'credential_info'")
            __props__.__dict__["credential_info"] = credential_info
            if storage_server_id is None and not opts.urn:
                raise TypeError("Missing required property 'storage_server_id'")
            __props__.__dict__["storage_server_id"] = storage_server_id
            __props__.__dict__["additional_details"] = None
            __props__.__dict__["display_name"] = None
            __props__.__dict__["exadata_infrastructure_id"] = None
            __props__.__dict__["internal_id"] = None
            __props__.__dict__["lifecycle_details"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["time_created"] = None
            __props__.__dict__["time_updated"] = None
            __props__.__dict__["version"] = None
        super(ExternalExadataStorageConnector, __self__).__init__(
            'oci:DatabaseManagement/externalExadataStorageConnector:ExternalExadataStorageConnector',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            additional_details: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            agent_id: Optional[pulumi.Input[str]] = None,
            connection_uri: Optional[pulumi.Input[str]] = None,
            connector_name: Optional[pulumi.Input[str]] = None,
            credential_info: Optional[pulumi.Input[pulumi.InputType['ExternalExadataStorageConnectorCredentialInfoArgs']]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            exadata_infrastructure_id: Optional[pulumi.Input[str]] = None,
            internal_id: Optional[pulumi.Input[str]] = None,
            lifecycle_details: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            storage_server_id: Optional[pulumi.Input[str]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            time_updated: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[str]] = None) -> 'ExternalExadataStorageConnector':
        """
        Get an existing ExternalExadataStorageConnector resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] additional_details: The additional details of the resource defined in `{"key": "value"}` format. Example: `{"bar-key": "value"}`
        :param pulumi.Input[str] agent_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the agent for the Exadata storage server.
        :param pulumi.Input[str] connection_uri: (Updatable) The unique string of the connection. For example, "https://<storage-server-name>/MS/RESTService/".
        :param pulumi.Input[str] connector_name: (Updatable) The name of the Exadata storage server connector.
        :param pulumi.Input[pulumi.InputType['ExternalExadataStorageConnectorCredentialInfoArgs']] credential_info: (Updatable) The user credential information.
        :param pulumi.Input[str] display_name: The name of the Exadata resource. English letters, numbers, "-", "_" and "." only.
        :param pulumi.Input[str] exadata_infrastructure_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Exadata infrastructure.
        :param pulumi.Input[str] internal_id: The internal ID of the Exadata resource.
        :param pulumi.Input[str] lifecycle_details: The details of the lifecycle state of the Exadata resource.
        :param pulumi.Input[str] state: The current lifecycle state of the database resource.
        :param pulumi.Input[str] status: The status of the Exadata resource.
        :param pulumi.Input[str] storage_server_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Exadata storage server.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] time_created: The timestamp of the creation of the Exadata resource.
        :param pulumi.Input[str] time_updated: The timestamp of the last update of the Exadata resource.
        :param pulumi.Input[str] version: The version of the Exadata resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ExternalExadataStorageConnectorState.__new__(_ExternalExadataStorageConnectorState)

        __props__.__dict__["additional_details"] = additional_details
        __props__.__dict__["agent_id"] = agent_id
        __props__.__dict__["connection_uri"] = connection_uri
        __props__.__dict__["connector_name"] = connector_name
        __props__.__dict__["credential_info"] = credential_info
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["exadata_infrastructure_id"] = exadata_infrastructure_id
        __props__.__dict__["internal_id"] = internal_id
        __props__.__dict__["lifecycle_details"] = lifecycle_details
        __props__.__dict__["state"] = state
        __props__.__dict__["status"] = status
        __props__.__dict__["storage_server_id"] = storage_server_id
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["time_updated"] = time_updated
        __props__.__dict__["version"] = version
        return ExternalExadataStorageConnector(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalDetails")
    def additional_details(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        The additional details of the resource defined in `{"key": "value"}` format. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "additional_details")

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the agent for the Exadata storage server.
        """
        return pulumi.get(self, "agent_id")

    @property
    @pulumi.getter(name="connectionUri")
    def connection_uri(self) -> pulumi.Output[str]:
        """
        (Updatable) The unique string of the connection. For example, "https://<storage-server-name>/MS/RESTService/".
        """
        return pulumi.get(self, "connection_uri")

    @property
    @pulumi.getter(name="connectorName")
    def connector_name(self) -> pulumi.Output[str]:
        """
        (Updatable) The name of the Exadata storage server connector.
        """
        return pulumi.get(self, "connector_name")

    @property
    @pulumi.getter(name="credentialInfo")
    def credential_info(self) -> pulumi.Output['outputs.ExternalExadataStorageConnectorCredentialInfo']:
        """
        (Updatable) The user credential information.
        """
        return pulumi.get(self, "credential_info")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The name of the Exadata resource. English letters, numbers, "-", "_" and "." only.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="exadataInfrastructureId")
    def exadata_infrastructure_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Exadata infrastructure.
        """
        return pulumi.get(self, "exadata_infrastructure_id")

    @property
    @pulumi.getter(name="internalId")
    def internal_id(self) -> pulumi.Output[str]:
        """
        The internal ID of the Exadata resource.
        """
        return pulumi.get(self, "internal_id")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> pulumi.Output[str]:
        """
        The details of the lifecycle state of the Exadata resource.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current lifecycle state of the database resource.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the Exadata resource.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageServerId")
    def storage_server_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Exadata storage server.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "storage_server_id")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The timestamp of the creation of the Exadata resource.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> pulumi.Output[str]:
        """
        The timestamp of the last update of the Exadata resource.
        """
        return pulumi.get(self, "time_updated")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        The version of the Exadata resource.
        """
        return pulumi.get(self, "version")

