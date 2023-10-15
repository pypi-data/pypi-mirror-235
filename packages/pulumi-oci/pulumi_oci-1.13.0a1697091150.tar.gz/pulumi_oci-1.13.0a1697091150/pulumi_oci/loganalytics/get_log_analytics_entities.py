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
    'GetLogAnalyticsEntitiesResult',
    'AwaitableGetLogAnalyticsEntitiesResult',
    'get_log_analytics_entities',
    'get_log_analytics_entities_output',
]

@pulumi.output_type
class GetLogAnalyticsEntitiesResult:
    """
    A collection of values returned by getLogAnalyticsEntities.
    """
    def __init__(__self__, cloud_resource_id=None, compartment_id=None, entity_type_names=None, filters=None, hostname=None, hostname_contains=None, id=None, is_management_agent_id_null=None, lifecycle_details_contains=None, log_analytics_entity_collections=None, name=None, name_contains=None, namespace=None, source_id=None, state=None):
        if cloud_resource_id and not isinstance(cloud_resource_id, str):
            raise TypeError("Expected argument 'cloud_resource_id' to be a str")
        pulumi.set(__self__, "cloud_resource_id", cloud_resource_id)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if entity_type_names and not isinstance(entity_type_names, list):
            raise TypeError("Expected argument 'entity_type_names' to be a list")
        pulumi.set(__self__, "entity_type_names", entity_type_names)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if hostname and not isinstance(hostname, str):
            raise TypeError("Expected argument 'hostname' to be a str")
        pulumi.set(__self__, "hostname", hostname)
        if hostname_contains and not isinstance(hostname_contains, str):
            raise TypeError("Expected argument 'hostname_contains' to be a str")
        pulumi.set(__self__, "hostname_contains", hostname_contains)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_management_agent_id_null and not isinstance(is_management_agent_id_null, str):
            raise TypeError("Expected argument 'is_management_agent_id_null' to be a str")
        pulumi.set(__self__, "is_management_agent_id_null", is_management_agent_id_null)
        if lifecycle_details_contains and not isinstance(lifecycle_details_contains, str):
            raise TypeError("Expected argument 'lifecycle_details_contains' to be a str")
        pulumi.set(__self__, "lifecycle_details_contains", lifecycle_details_contains)
        if log_analytics_entity_collections and not isinstance(log_analytics_entity_collections, list):
            raise TypeError("Expected argument 'log_analytics_entity_collections' to be a list")
        pulumi.set(__self__, "log_analytics_entity_collections", log_analytics_entity_collections)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if name_contains and not isinstance(name_contains, str):
            raise TypeError("Expected argument 'name_contains' to be a str")
        pulumi.set(__self__, "name_contains", name_contains)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if source_id and not isinstance(source_id, str):
            raise TypeError("Expected argument 'source_id' to be a str")
        pulumi.set(__self__, "source_id", source_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="cloudResourceId")
    def cloud_resource_id(self) -> Optional[str]:
        """
        The OCID of the Cloud resource which this entity is a representation of. This may be blank when the entity represents a non-cloud resource that the customer may have on their premises.
        """
        return pulumi.get(self, "cloud_resource_id")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        Compartment Identifier [OCID] (https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="entityTypeNames")
    def entity_type_names(self) -> Optional[Sequence[str]]:
        """
        Log analytics entity type name.
        """
        return pulumi.get(self, "entity_type_names")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetLogAnalyticsEntitiesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def hostname(self) -> Optional[str]:
        """
        The hostname where the entity represented here is actually present. This would be the output one would get if they run `echo $HOSTNAME` on Linux or an equivalent OS command. This may be different from management agents host since logs may be collected remotely.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="hostnameContains")
    def hostname_contains(self) -> Optional[str]:
        return pulumi.get(self, "hostname_contains")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isManagementAgentIdNull")
    def is_management_agent_id_null(self) -> Optional[str]:
        return pulumi.get(self, "is_management_agent_id_null")

    @property
    @pulumi.getter(name="lifecycleDetailsContains")
    def lifecycle_details_contains(self) -> Optional[str]:
        return pulumi.get(self, "lifecycle_details_contains")

    @property
    @pulumi.getter(name="logAnalyticsEntityCollections")
    def log_analytics_entity_collections(self) -> Sequence['outputs.GetLogAnalyticsEntitiesLogAnalyticsEntityCollectionResult']:
        """
        The list of log_analytics_entity_collection.
        """
        return pulumi.get(self, "log_analytics_entity_collections")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Log analytics entity name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nameContains")
    def name_contains(self) -> Optional[str]:
        return pulumi.get(self, "name_contains")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> Optional[str]:
        """
        This indicates the type of source. It is primarily for Enterprise Manager Repository ID.
        """
        return pulumi.get(self, "source_id")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the log analytics entity.
        """
        return pulumi.get(self, "state")


class AwaitableGetLogAnalyticsEntitiesResult(GetLogAnalyticsEntitiesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLogAnalyticsEntitiesResult(
            cloud_resource_id=self.cloud_resource_id,
            compartment_id=self.compartment_id,
            entity_type_names=self.entity_type_names,
            filters=self.filters,
            hostname=self.hostname,
            hostname_contains=self.hostname_contains,
            id=self.id,
            is_management_agent_id_null=self.is_management_agent_id_null,
            lifecycle_details_contains=self.lifecycle_details_contains,
            log_analytics_entity_collections=self.log_analytics_entity_collections,
            name=self.name,
            name_contains=self.name_contains,
            namespace=self.namespace,
            source_id=self.source_id,
            state=self.state)


def get_log_analytics_entities(cloud_resource_id: Optional[str] = None,
                               compartment_id: Optional[str] = None,
                               entity_type_names: Optional[Sequence[str]] = None,
                               filters: Optional[Sequence[pulumi.InputType['GetLogAnalyticsEntitiesFilterArgs']]] = None,
                               hostname: Optional[str] = None,
                               hostname_contains: Optional[str] = None,
                               is_management_agent_id_null: Optional[str] = None,
                               lifecycle_details_contains: Optional[str] = None,
                               name: Optional[str] = None,
                               name_contains: Optional[str] = None,
                               namespace: Optional[str] = None,
                               source_id: Optional[str] = None,
                               state: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLogAnalyticsEntitiesResult:
    """
    This data source provides the list of Log Analytics Entities in Oracle Cloud Infrastructure Log Analytics service.

    Return a list of log analytics entities.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_log_analytics_entities = oci.LogAnalytics.get_log_analytics_entities(compartment_id=var["compartment_id"],
        namespace=var["log_analytics_entity_namespace"],
        cloud_resource_id=oci_log_analytics_cloud_resource["test_cloud_resource"]["id"],
        entity_type_names=var["log_analytics_entity_entity_type_name"],
        hostname=var["log_analytics_entity_hostname"],
        hostname_contains=var["log_analytics_entity_hostname_contains"],
        is_management_agent_id_null=var["log_analytics_entity_is_management_agent_id_null"],
        lifecycle_details_contains=var["log_analytics_entity_lifecycle_details_contains"],
        name=var["log_analytics_entity_name"],
        name_contains=var["log_analytics_entity_name_contains"],
        source_id=oci_log_analytics_source["test_source"]["id"],
        state=var["log_analytics_entity_state"])
    ```


    :param str cloud_resource_id: A filter to return only log analytics entities whose cloudResourceId matches the cloudResourceId given.
    :param str compartment_id: The ID of the compartment in which to list resources.
    :param Sequence[str] entity_type_names: A filter to return only log analytics entities whose entityTypeName matches the entire log analytics entity type name of one of the entityTypeNames given in the list. The match is case-insensitive.
    :param str hostname: A filter to return only log analytics entities whose hostname matches the entire hostname given.
    :param str hostname_contains: A filter to return only log analytics entities whose hostname contains the substring given. The match is case-insensitive.
    :param str is_management_agent_id_null: A filter to return only those log analytics entities whose managementAgentId is null or is not null.
    :param str lifecycle_details_contains: A filter to return only log analytics entities whose lifecycleDetails contains the specified string.
    :param str name: A filter to return only log analytics entities whose name matches the entire name given. The match is case-insensitive.
    :param str name_contains: A filter to return only log analytics entities whose name contains the name given. The match is case-insensitive.
    :param str namespace: The Logging Analytics namespace used for the request.
    :param str source_id: A filter to return only log analytics entities whose sourceId matches the sourceId given.
    :param str state: A filter to return only those log analytics entities with the specified lifecycle state. The state value is case-insensitive.
    """
    __args__ = dict()
    __args__['cloudResourceId'] = cloud_resource_id
    __args__['compartmentId'] = compartment_id
    __args__['entityTypeNames'] = entity_type_names
    __args__['filters'] = filters
    __args__['hostname'] = hostname
    __args__['hostnameContains'] = hostname_contains
    __args__['isManagementAgentIdNull'] = is_management_agent_id_null
    __args__['lifecycleDetailsContains'] = lifecycle_details_contains
    __args__['name'] = name
    __args__['nameContains'] = name_contains
    __args__['namespace'] = namespace
    __args__['sourceId'] = source_id
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:LogAnalytics/getLogAnalyticsEntities:getLogAnalyticsEntities', __args__, opts=opts, typ=GetLogAnalyticsEntitiesResult).value

    return AwaitableGetLogAnalyticsEntitiesResult(
        cloud_resource_id=pulumi.get(__ret__, 'cloud_resource_id'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        entity_type_names=pulumi.get(__ret__, 'entity_type_names'),
        filters=pulumi.get(__ret__, 'filters'),
        hostname=pulumi.get(__ret__, 'hostname'),
        hostname_contains=pulumi.get(__ret__, 'hostname_contains'),
        id=pulumi.get(__ret__, 'id'),
        is_management_agent_id_null=pulumi.get(__ret__, 'is_management_agent_id_null'),
        lifecycle_details_contains=pulumi.get(__ret__, 'lifecycle_details_contains'),
        log_analytics_entity_collections=pulumi.get(__ret__, 'log_analytics_entity_collections'),
        name=pulumi.get(__ret__, 'name'),
        name_contains=pulumi.get(__ret__, 'name_contains'),
        namespace=pulumi.get(__ret__, 'namespace'),
        source_id=pulumi.get(__ret__, 'source_id'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_log_analytics_entities)
def get_log_analytics_entities_output(cloud_resource_id: Optional[pulumi.Input[Optional[str]]] = None,
                                      compartment_id: Optional[pulumi.Input[str]] = None,
                                      entity_type_names: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                      filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetLogAnalyticsEntitiesFilterArgs']]]]] = None,
                                      hostname: Optional[pulumi.Input[Optional[str]]] = None,
                                      hostname_contains: Optional[pulumi.Input[Optional[str]]] = None,
                                      is_management_agent_id_null: Optional[pulumi.Input[Optional[str]]] = None,
                                      lifecycle_details_contains: Optional[pulumi.Input[Optional[str]]] = None,
                                      name: Optional[pulumi.Input[Optional[str]]] = None,
                                      name_contains: Optional[pulumi.Input[Optional[str]]] = None,
                                      namespace: Optional[pulumi.Input[str]] = None,
                                      source_id: Optional[pulumi.Input[Optional[str]]] = None,
                                      state: Optional[pulumi.Input[Optional[str]]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLogAnalyticsEntitiesResult]:
    """
    This data source provides the list of Log Analytics Entities in Oracle Cloud Infrastructure Log Analytics service.

    Return a list of log analytics entities.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_log_analytics_entities = oci.LogAnalytics.get_log_analytics_entities(compartment_id=var["compartment_id"],
        namespace=var["log_analytics_entity_namespace"],
        cloud_resource_id=oci_log_analytics_cloud_resource["test_cloud_resource"]["id"],
        entity_type_names=var["log_analytics_entity_entity_type_name"],
        hostname=var["log_analytics_entity_hostname"],
        hostname_contains=var["log_analytics_entity_hostname_contains"],
        is_management_agent_id_null=var["log_analytics_entity_is_management_agent_id_null"],
        lifecycle_details_contains=var["log_analytics_entity_lifecycle_details_contains"],
        name=var["log_analytics_entity_name"],
        name_contains=var["log_analytics_entity_name_contains"],
        source_id=oci_log_analytics_source["test_source"]["id"],
        state=var["log_analytics_entity_state"])
    ```


    :param str cloud_resource_id: A filter to return only log analytics entities whose cloudResourceId matches the cloudResourceId given.
    :param str compartment_id: The ID of the compartment in which to list resources.
    :param Sequence[str] entity_type_names: A filter to return only log analytics entities whose entityTypeName matches the entire log analytics entity type name of one of the entityTypeNames given in the list. The match is case-insensitive.
    :param str hostname: A filter to return only log analytics entities whose hostname matches the entire hostname given.
    :param str hostname_contains: A filter to return only log analytics entities whose hostname contains the substring given. The match is case-insensitive.
    :param str is_management_agent_id_null: A filter to return only those log analytics entities whose managementAgentId is null or is not null.
    :param str lifecycle_details_contains: A filter to return only log analytics entities whose lifecycleDetails contains the specified string.
    :param str name: A filter to return only log analytics entities whose name matches the entire name given. The match is case-insensitive.
    :param str name_contains: A filter to return only log analytics entities whose name contains the name given. The match is case-insensitive.
    :param str namespace: The Logging Analytics namespace used for the request.
    :param str source_id: A filter to return only log analytics entities whose sourceId matches the sourceId given.
    :param str state: A filter to return only those log analytics entities with the specified lifecycle state. The state value is case-insensitive.
    """
    ...
