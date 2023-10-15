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
    'GetExternalClusterInstancesResult',
    'AwaitableGetExternalClusterInstancesResult',
    'get_external_cluster_instances',
    'get_external_cluster_instances_output',
]

@pulumi.output_type
class GetExternalClusterInstancesResult:
    """
    A collection of values returned by getExternalClusterInstances.
    """
    def __init__(__self__, compartment_id=None, display_name=None, external_cluster_id=None, external_cluster_instance_collections=None, filters=None, id=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if external_cluster_id and not isinstance(external_cluster_id, str):
            raise TypeError("Expected argument 'external_cluster_id' to be a str")
        pulumi.set(__self__, "external_cluster_id", external_cluster_id)
        if external_cluster_instance_collections and not isinstance(external_cluster_instance_collections, list):
            raise TypeError("Expected argument 'external_cluster_instance_collections' to be a list")
        pulumi.set(__self__, "external_cluster_instance_collections", external_cluster_instance_collections)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The user-friendly name for the cluster instance. The name does not have to be unique.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="externalClusterId")
    def external_cluster_id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external cluster that the cluster instance belongs to.
        """
        return pulumi.get(self, "external_cluster_id")

    @property
    @pulumi.getter(name="externalClusterInstanceCollections")
    def external_cluster_instance_collections(self) -> Sequence['outputs.GetExternalClusterInstancesExternalClusterInstanceCollectionResult']:
        """
        The list of external_cluster_instance_collection.
        """
        return pulumi.get(self, "external_cluster_instance_collections")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetExternalClusterInstancesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetExternalClusterInstancesResult(GetExternalClusterInstancesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExternalClusterInstancesResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            external_cluster_id=self.external_cluster_id,
            external_cluster_instance_collections=self.external_cluster_instance_collections,
            filters=self.filters,
            id=self.id)


def get_external_cluster_instances(compartment_id: Optional[str] = None,
                                   display_name: Optional[str] = None,
                                   external_cluster_id: Optional[str] = None,
                                   filters: Optional[Sequence[pulumi.InputType['GetExternalClusterInstancesFilterArgs']]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExternalClusterInstancesResult:
    """
    This data source provides the list of External Cluster Instances in Oracle Cloud Infrastructure Database Management service.

    Lists the cluster instances in the specified external cluster.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_external_cluster_instances = oci.DatabaseManagement.get_external_cluster_instances(compartment_id=var["compartment_id"],
        display_name=var["external_cluster_instance_display_name"],
        external_cluster_id=oci_database_management_external_cluster["test_external_cluster"]["id"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A filter to only return the resources that match the entire display name.
    :param str external_cluster_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external cluster.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['externalClusterId'] = external_cluster_id
    __args__['filters'] = filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseManagement/getExternalClusterInstances:getExternalClusterInstances', __args__, opts=opts, typ=GetExternalClusterInstancesResult).value

    return AwaitableGetExternalClusterInstancesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        external_cluster_id=pulumi.get(__ret__, 'external_cluster_id'),
        external_cluster_instance_collections=pulumi.get(__ret__, 'external_cluster_instance_collections'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_external_cluster_instances)
def get_external_cluster_instances_output(compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                                          display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                          external_cluster_id: Optional[pulumi.Input[Optional[str]]] = None,
                                          filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetExternalClusterInstancesFilterArgs']]]]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExternalClusterInstancesResult]:
    """
    This data source provides the list of External Cluster Instances in Oracle Cloud Infrastructure Database Management service.

    Lists the cluster instances in the specified external cluster.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_external_cluster_instances = oci.DatabaseManagement.get_external_cluster_instances(compartment_id=var["compartment_id"],
        display_name=var["external_cluster_instance_display_name"],
        external_cluster_id=oci_database_management_external_cluster["test_external_cluster"]["id"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A filter to only return the resources that match the entire display name.
    :param str external_cluster_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external cluster.
    """
    ...
