# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ExternalClusterInstanceArgs', 'ExternalClusterInstance']

@pulumi.input_type
class ExternalClusterInstanceArgs:
    def __init__(__self__, *,
                 external_cluster_instance_id: pulumi.Input[str],
                 external_connector_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ExternalClusterInstance resource.
        :param pulumi.Input[str] external_cluster_instance_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external cluster instance.
        :param pulumi.Input[str] external_connector_id: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external connector.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ExternalClusterInstanceArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            external_cluster_instance_id=external_cluster_instance_id,
            external_connector_id=external_connector_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             external_cluster_instance_id: pulumi.Input[str],
             external_connector_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("external_cluster_instance_id", external_cluster_instance_id)
        if external_connector_id is not None:
            _setter("external_connector_id", external_connector_id)

    @property
    @pulumi.getter(name="externalClusterInstanceId")
    def external_cluster_instance_id(self) -> pulumi.Input[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external cluster instance.
        """
        return pulumi.get(self, "external_cluster_instance_id")

    @external_cluster_instance_id.setter
    def external_cluster_instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "external_cluster_instance_id", value)

    @property
    @pulumi.getter(name="externalConnectorId")
    def external_connector_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external connector.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "external_connector_id")

    @external_connector_id.setter
    def external_connector_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_connector_id", value)


@pulumi.input_type
class _ExternalClusterInstanceState:
    def __init__(__self__, *,
                 adr_home_directory: Optional[pulumi.Input[str]] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 component_name: Optional[pulumi.Input[str]] = None,
                 crs_base_directory: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 external_cluster_id: Optional[pulumi.Input[str]] = None,
                 external_cluster_instance_id: Optional[pulumi.Input[str]] = None,
                 external_connector_id: Optional[pulumi.Input[str]] = None,
                 external_db_node_id: Optional[pulumi.Input[str]] = None,
                 external_db_system_id: Optional[pulumi.Input[str]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 lifecycle_details: Optional[pulumi.Input[str]] = None,
                 node_role: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 time_updated: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ExternalClusterInstance resources.
        :param pulumi.Input[str] adr_home_directory: The Automatic Diagnostic Repository (ADR) home directory for the cluster instance.
        :param pulumi.Input[str] compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        :param pulumi.Input[str] component_name: The name of the external cluster instance.
        :param pulumi.Input[str] crs_base_directory: The Oracle base location of Cluster Ready Services (CRS).
        :param pulumi.Input[str] display_name: The user-friendly name for the cluster instance. The name does not have to be unique.
        :param pulumi.Input[str] external_cluster_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external cluster that the cluster instance belongs to.
        :param pulumi.Input[str] external_cluster_instance_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external cluster instance.
        :param pulumi.Input[str] external_connector_id: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external connector.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] external_db_node_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB node.
        :param pulumi.Input[str] external_db_system_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system that the cluster instance is a part of.
        :param pulumi.Input[str] host_name: The name of the host on which the cluster instance is running.
        :param pulumi.Input[str] lifecycle_details: Additional information about the current lifecycle state.
        :param pulumi.Input[str] node_role: The role of the cluster node.
        :param pulumi.Input[str] state: The current lifecycle state of the external cluster instance.
        :param pulumi.Input[str] time_created: The date and time the external cluster instance was created.
        :param pulumi.Input[str] time_updated: The date and time the external cluster instance was last updated.
        """
        _ExternalClusterInstanceState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            adr_home_directory=adr_home_directory,
            compartment_id=compartment_id,
            component_name=component_name,
            crs_base_directory=crs_base_directory,
            display_name=display_name,
            external_cluster_id=external_cluster_id,
            external_cluster_instance_id=external_cluster_instance_id,
            external_connector_id=external_connector_id,
            external_db_node_id=external_db_node_id,
            external_db_system_id=external_db_system_id,
            host_name=host_name,
            lifecycle_details=lifecycle_details,
            node_role=node_role,
            state=state,
            time_created=time_created,
            time_updated=time_updated,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             adr_home_directory: Optional[pulumi.Input[str]] = None,
             compartment_id: Optional[pulumi.Input[str]] = None,
             component_name: Optional[pulumi.Input[str]] = None,
             crs_base_directory: Optional[pulumi.Input[str]] = None,
             display_name: Optional[pulumi.Input[str]] = None,
             external_cluster_id: Optional[pulumi.Input[str]] = None,
             external_cluster_instance_id: Optional[pulumi.Input[str]] = None,
             external_connector_id: Optional[pulumi.Input[str]] = None,
             external_db_node_id: Optional[pulumi.Input[str]] = None,
             external_db_system_id: Optional[pulumi.Input[str]] = None,
             host_name: Optional[pulumi.Input[str]] = None,
             lifecycle_details: Optional[pulumi.Input[str]] = None,
             node_role: Optional[pulumi.Input[str]] = None,
             state: Optional[pulumi.Input[str]] = None,
             time_created: Optional[pulumi.Input[str]] = None,
             time_updated: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if adr_home_directory is not None:
            _setter("adr_home_directory", adr_home_directory)
        if compartment_id is not None:
            _setter("compartment_id", compartment_id)
        if component_name is not None:
            _setter("component_name", component_name)
        if crs_base_directory is not None:
            _setter("crs_base_directory", crs_base_directory)
        if display_name is not None:
            _setter("display_name", display_name)
        if external_cluster_id is not None:
            _setter("external_cluster_id", external_cluster_id)
        if external_cluster_instance_id is not None:
            _setter("external_cluster_instance_id", external_cluster_instance_id)
        if external_connector_id is not None:
            _setter("external_connector_id", external_connector_id)
        if external_db_node_id is not None:
            _setter("external_db_node_id", external_db_node_id)
        if external_db_system_id is not None:
            _setter("external_db_system_id", external_db_system_id)
        if host_name is not None:
            _setter("host_name", host_name)
        if lifecycle_details is not None:
            _setter("lifecycle_details", lifecycle_details)
        if node_role is not None:
            _setter("node_role", node_role)
        if state is not None:
            _setter("state", state)
        if time_created is not None:
            _setter("time_created", time_created)
        if time_updated is not None:
            _setter("time_updated", time_updated)

    @property
    @pulumi.getter(name="adrHomeDirectory")
    def adr_home_directory(self) -> Optional[pulumi.Input[str]]:
        """
        The Automatic Diagnostic Repository (ADR) home directory for the cluster instance.
        """
        return pulumi.get(self, "adr_home_directory")

    @adr_home_directory.setter
    def adr_home_directory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "adr_home_directory", value)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="componentName")
    def component_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the external cluster instance.
        """
        return pulumi.get(self, "component_name")

    @component_name.setter
    def component_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "component_name", value)

    @property
    @pulumi.getter(name="crsBaseDirectory")
    def crs_base_directory(self) -> Optional[pulumi.Input[str]]:
        """
        The Oracle base location of Cluster Ready Services (CRS).
        """
        return pulumi.get(self, "crs_base_directory")

    @crs_base_directory.setter
    def crs_base_directory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "crs_base_directory", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The user-friendly name for the cluster instance. The name does not have to be unique.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="externalClusterId")
    def external_cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external cluster that the cluster instance belongs to.
        """
        return pulumi.get(self, "external_cluster_id")

    @external_cluster_id.setter
    def external_cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_cluster_id", value)

    @property
    @pulumi.getter(name="externalClusterInstanceId")
    def external_cluster_instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external cluster instance.
        """
        return pulumi.get(self, "external_cluster_instance_id")

    @external_cluster_instance_id.setter
    def external_cluster_instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_cluster_instance_id", value)

    @property
    @pulumi.getter(name="externalConnectorId")
    def external_connector_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external connector.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "external_connector_id")

    @external_connector_id.setter
    def external_connector_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_connector_id", value)

    @property
    @pulumi.getter(name="externalDbNodeId")
    def external_db_node_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB node.
        """
        return pulumi.get(self, "external_db_node_id")

    @external_db_node_id.setter
    def external_db_node_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_db_node_id", value)

    @property
    @pulumi.getter(name="externalDbSystemId")
    def external_db_system_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system that the cluster instance is a part of.
        """
        return pulumi.get(self, "external_db_system_id")

    @external_db_system_id.setter
    def external_db_system_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_db_system_id", value)

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the host on which the cluster instance is running.
        """
        return pulumi.get(self, "host_name")

    @host_name.setter
    def host_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host_name", value)

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> Optional[pulumi.Input[str]]:
        """
        Additional information about the current lifecycle state.
        """
        return pulumi.get(self, "lifecycle_details")

    @lifecycle_details.setter
    def lifecycle_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_details", value)

    @property
    @pulumi.getter(name="nodeRole")
    def node_role(self) -> Optional[pulumi.Input[str]]:
        """
        The role of the cluster node.
        """
        return pulumi.get(self, "node_role")

    @node_role.setter
    def node_role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_role", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current lifecycle state of the external cluster instance.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time the external cluster instance was created.
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time the external cluster instance was last updated.
        """
        return pulumi.get(self, "time_updated")

    @time_updated.setter
    def time_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_updated", value)


class ExternalClusterInstance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 external_cluster_instance_id: Optional[pulumi.Input[str]] = None,
                 external_connector_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the External Cluster Instance resource in Oracle Cloud Infrastructure Database Management service.

        Updates the external cluster instance specified by `externalClusterInstanceId`.

        ## Import

        ExternalClusterInstances can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:DatabaseManagement/externalClusterInstance:ExternalClusterInstance test_external_cluster_instance "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] external_cluster_instance_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external cluster instance.
        :param pulumi.Input[str] external_connector_id: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external connector.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExternalClusterInstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the External Cluster Instance resource in Oracle Cloud Infrastructure Database Management service.

        Updates the external cluster instance specified by `externalClusterInstanceId`.

        ## Import

        ExternalClusterInstances can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:DatabaseManagement/externalClusterInstance:ExternalClusterInstance test_external_cluster_instance "id"
        ```

        :param str resource_name: The name of the resource.
        :param ExternalClusterInstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExternalClusterInstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ExternalClusterInstanceArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 external_cluster_instance_id: Optional[pulumi.Input[str]] = None,
                 external_connector_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ExternalClusterInstanceArgs.__new__(ExternalClusterInstanceArgs)

            if external_cluster_instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'external_cluster_instance_id'")
            __props__.__dict__["external_cluster_instance_id"] = external_cluster_instance_id
            __props__.__dict__["external_connector_id"] = external_connector_id
            __props__.__dict__["adr_home_directory"] = None
            __props__.__dict__["compartment_id"] = None
            __props__.__dict__["component_name"] = None
            __props__.__dict__["crs_base_directory"] = None
            __props__.__dict__["display_name"] = None
            __props__.__dict__["external_cluster_id"] = None
            __props__.__dict__["external_db_node_id"] = None
            __props__.__dict__["external_db_system_id"] = None
            __props__.__dict__["host_name"] = None
            __props__.__dict__["lifecycle_details"] = None
            __props__.__dict__["node_role"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["time_created"] = None
            __props__.__dict__["time_updated"] = None
        super(ExternalClusterInstance, __self__).__init__(
            'oci:DatabaseManagement/externalClusterInstance:ExternalClusterInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            adr_home_directory: Optional[pulumi.Input[str]] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            component_name: Optional[pulumi.Input[str]] = None,
            crs_base_directory: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            external_cluster_id: Optional[pulumi.Input[str]] = None,
            external_cluster_instance_id: Optional[pulumi.Input[str]] = None,
            external_connector_id: Optional[pulumi.Input[str]] = None,
            external_db_node_id: Optional[pulumi.Input[str]] = None,
            external_db_system_id: Optional[pulumi.Input[str]] = None,
            host_name: Optional[pulumi.Input[str]] = None,
            lifecycle_details: Optional[pulumi.Input[str]] = None,
            node_role: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            time_updated: Optional[pulumi.Input[str]] = None) -> 'ExternalClusterInstance':
        """
        Get an existing ExternalClusterInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] adr_home_directory: The Automatic Diagnostic Repository (ADR) home directory for the cluster instance.
        :param pulumi.Input[str] compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        :param pulumi.Input[str] component_name: The name of the external cluster instance.
        :param pulumi.Input[str] crs_base_directory: The Oracle base location of Cluster Ready Services (CRS).
        :param pulumi.Input[str] display_name: The user-friendly name for the cluster instance. The name does not have to be unique.
        :param pulumi.Input[str] external_cluster_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external cluster that the cluster instance belongs to.
        :param pulumi.Input[str] external_cluster_instance_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external cluster instance.
        :param pulumi.Input[str] external_connector_id: (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external connector.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] external_db_node_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB node.
        :param pulumi.Input[str] external_db_system_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system that the cluster instance is a part of.
        :param pulumi.Input[str] host_name: The name of the host on which the cluster instance is running.
        :param pulumi.Input[str] lifecycle_details: Additional information about the current lifecycle state.
        :param pulumi.Input[str] node_role: The role of the cluster node.
        :param pulumi.Input[str] state: The current lifecycle state of the external cluster instance.
        :param pulumi.Input[str] time_created: The date and time the external cluster instance was created.
        :param pulumi.Input[str] time_updated: The date and time the external cluster instance was last updated.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ExternalClusterInstanceState.__new__(_ExternalClusterInstanceState)

        __props__.__dict__["adr_home_directory"] = adr_home_directory
        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["component_name"] = component_name
        __props__.__dict__["crs_base_directory"] = crs_base_directory
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["external_cluster_id"] = external_cluster_id
        __props__.__dict__["external_cluster_instance_id"] = external_cluster_instance_id
        __props__.__dict__["external_connector_id"] = external_connector_id
        __props__.__dict__["external_db_node_id"] = external_db_node_id
        __props__.__dict__["external_db_system_id"] = external_db_system_id
        __props__.__dict__["host_name"] = host_name
        __props__.__dict__["lifecycle_details"] = lifecycle_details
        __props__.__dict__["node_role"] = node_role
        __props__.__dict__["state"] = state
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["time_updated"] = time_updated
        return ExternalClusterInstance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adrHomeDirectory")
    def adr_home_directory(self) -> pulumi.Output[str]:
        """
        The Automatic Diagnostic Repository (ADR) home directory for the cluster instance.
        """
        return pulumi.get(self, "adr_home_directory")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="componentName")
    def component_name(self) -> pulumi.Output[str]:
        """
        The name of the external cluster instance.
        """
        return pulumi.get(self, "component_name")

    @property
    @pulumi.getter(name="crsBaseDirectory")
    def crs_base_directory(self) -> pulumi.Output[str]:
        """
        The Oracle base location of Cluster Ready Services (CRS).
        """
        return pulumi.get(self, "crs_base_directory")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The user-friendly name for the cluster instance. The name does not have to be unique.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="externalClusterId")
    def external_cluster_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external cluster that the cluster instance belongs to.
        """
        return pulumi.get(self, "external_cluster_id")

    @property
    @pulumi.getter(name="externalClusterInstanceId")
    def external_cluster_instance_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external cluster instance.
        """
        return pulumi.get(self, "external_cluster_instance_id")

    @property
    @pulumi.getter(name="externalConnectorId")
    def external_connector_id(self) -> pulumi.Output[str]:
        """
        (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external connector.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "external_connector_id")

    @property
    @pulumi.getter(name="externalDbNodeId")
    def external_db_node_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB node.
        """
        return pulumi.get(self, "external_db_node_id")

    @property
    @pulumi.getter(name="externalDbSystemId")
    def external_db_system_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system that the cluster instance is a part of.
        """
        return pulumi.get(self, "external_db_system_id")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Output[str]:
        """
        The name of the host on which the cluster instance is running.
        """
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> pulumi.Output[str]:
        """
        Additional information about the current lifecycle state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="nodeRole")
    def node_role(self) -> pulumi.Output[str]:
        """
        The role of the cluster node.
        """
        return pulumi.get(self, "node_role")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current lifecycle state of the external cluster instance.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The date and time the external cluster instance was created.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> pulumi.Output[str]:
        """
        The date and time the external cluster instance was last updated.
        """
        return pulumi.get(self, "time_updated")

