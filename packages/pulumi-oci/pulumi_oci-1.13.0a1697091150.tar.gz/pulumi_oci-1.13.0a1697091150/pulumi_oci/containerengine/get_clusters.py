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
    'GetClustersResult',
    'AwaitableGetClustersResult',
    'get_clusters',
    'get_clusters_output',
]

@pulumi.output_type
class GetClustersResult:
    """
    A collection of values returned by getClusters.
    """
    def __init__(__self__, clusters=None, compartment_id=None, filters=None, id=None, name=None, states=None):
        if clusters and not isinstance(clusters, list):
            raise TypeError("Expected argument 'clusters' to be a list")
        pulumi.set(__self__, "clusters", clusters)
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
        if states and not isinstance(states, list):
            raise TypeError("Expected argument 'states' to be a list")
        pulumi.set(__self__, "states", states)

    @property
    @pulumi.getter
    def clusters(self) -> Sequence['outputs.GetClustersClusterResult']:
        """
        The list of clusters.
        """
        return pulumi.get(self, "clusters")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment in which the cluster exists.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetClustersFilterResult']]:
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
        The name of the cluster.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def states(self) -> Optional[Sequence[str]]:
        """
        The state of the cluster masters.
        """
        return pulumi.get(self, "states")


class AwaitableGetClustersResult(GetClustersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClustersResult(
            clusters=self.clusters,
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            name=self.name,
            states=self.states)


def get_clusters(compartment_id: Optional[str] = None,
                 filters: Optional[Sequence[pulumi.InputType['GetClustersFilterArgs']]] = None,
                 name: Optional[str] = None,
                 states: Optional[Sequence[str]] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClustersResult:
    """
    This data source provides the list of Clusters in Oracle Cloud Infrastructure Container Engine service.

    List all the cluster objects in a compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_clusters = oci.ContainerEngine.get_clusters(compartment_id=var["compartment_id"],
        name=var["cluster_name"],
        states=var["cluster_state"])
    ```


    :param str compartment_id: The OCID of the compartment.
    :param str name: The name to filter on.
    :param Sequence[str] states: A cluster lifecycle state to filter on. Can have multiple parameters of this name.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['name'] = name
    __args__['states'] = states
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:ContainerEngine/getClusters:getClusters', __args__, opts=opts, typ=GetClustersResult).value

    return AwaitableGetClustersResult(
        clusters=pulumi.get(__ret__, 'clusters'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        states=pulumi.get(__ret__, 'states'))


@_utilities.lift_output_func(get_clusters)
def get_clusters_output(compartment_id: Optional[pulumi.Input[str]] = None,
                        filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetClustersFilterArgs']]]]] = None,
                        name: Optional[pulumi.Input[Optional[str]]] = None,
                        states: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClustersResult]:
    """
    This data source provides the list of Clusters in Oracle Cloud Infrastructure Container Engine service.

    List all the cluster objects in a compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_clusters = oci.ContainerEngine.get_clusters(compartment_id=var["compartment_id"],
        name=var["cluster_name"],
        states=var["cluster_state"])
    ```


    :param str compartment_id: The OCID of the compartment.
    :param str name: The name to filter on.
    :param Sequence[str] states: A cluster lifecycle state to filter on. Can have multiple parameters of this name.
    """
    ...
