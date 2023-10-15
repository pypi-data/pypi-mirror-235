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
    'GetExternalClusterResult',
    'AwaitableGetExternalClusterResult',
    'get_external_cluster',
    'get_external_cluster_output',
]

@pulumi.output_type
class GetExternalClusterResult:
    """
    A collection of values returned by getExternalCluster.
    """
    def __init__(__self__, additional_details=None, compartment_id=None, component_name=None, display_name=None, external_cluster_id=None, external_connector_id=None, external_db_system_id=None, grid_home=None, id=None, is_flex_cluster=None, lifecycle_details=None, network_configurations=None, ocr_file_location=None, scan_configurations=None, state=None, time_created=None, time_updated=None, version=None, vip_configurations=None):
        if additional_details and not isinstance(additional_details, dict):
            raise TypeError("Expected argument 'additional_details' to be a dict")
        pulumi.set(__self__, "additional_details", additional_details)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if component_name and not isinstance(component_name, str):
            raise TypeError("Expected argument 'component_name' to be a str")
        pulumi.set(__self__, "component_name", component_name)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if external_cluster_id and not isinstance(external_cluster_id, str):
            raise TypeError("Expected argument 'external_cluster_id' to be a str")
        pulumi.set(__self__, "external_cluster_id", external_cluster_id)
        if external_connector_id and not isinstance(external_connector_id, str):
            raise TypeError("Expected argument 'external_connector_id' to be a str")
        pulumi.set(__self__, "external_connector_id", external_connector_id)
        if external_db_system_id and not isinstance(external_db_system_id, str):
            raise TypeError("Expected argument 'external_db_system_id' to be a str")
        pulumi.set(__self__, "external_db_system_id", external_db_system_id)
        if grid_home and not isinstance(grid_home, str):
            raise TypeError("Expected argument 'grid_home' to be a str")
        pulumi.set(__self__, "grid_home", grid_home)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_flex_cluster and not isinstance(is_flex_cluster, bool):
            raise TypeError("Expected argument 'is_flex_cluster' to be a bool")
        pulumi.set(__self__, "is_flex_cluster", is_flex_cluster)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if network_configurations and not isinstance(network_configurations, list):
            raise TypeError("Expected argument 'network_configurations' to be a list")
        pulumi.set(__self__, "network_configurations", network_configurations)
        if ocr_file_location and not isinstance(ocr_file_location, str):
            raise TypeError("Expected argument 'ocr_file_location' to be a str")
        pulumi.set(__self__, "ocr_file_location", ocr_file_location)
        if scan_configurations and not isinstance(scan_configurations, list):
            raise TypeError("Expected argument 'scan_configurations' to be a list")
        pulumi.set(__self__, "scan_configurations", scan_configurations)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)
        if vip_configurations and not isinstance(vip_configurations, list):
            raise TypeError("Expected argument 'vip_configurations' to be a list")
        pulumi.set(__self__, "vip_configurations", vip_configurations)

    @property
    @pulumi.getter(name="additionalDetails")
    def additional_details(self) -> Mapping[str, Any]:
        """
        The additional details of the external cluster defined in `{"key": "value"}` format. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "additional_details")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="componentName")
    def component_name(self) -> str:
        """
        The name of the external cluster.
        """
        return pulumi.get(self, "component_name")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The user-friendly name for the external cluster. The name does not have to be unique.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="externalClusterId")
    def external_cluster_id(self) -> str:
        return pulumi.get(self, "external_cluster_id")

    @property
    @pulumi.getter(name="externalConnectorId")
    def external_connector_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external connector.
        """
        return pulumi.get(self, "external_connector_id")

    @property
    @pulumi.getter(name="externalDbSystemId")
    def external_db_system_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system that the cluster is a part of.
        """
        return pulumi.get(self, "external_db_system_id")

    @property
    @pulumi.getter(name="gridHome")
    def grid_home(self) -> str:
        """
        The directory in which Oracle Grid Infrastructure is installed.
        """
        return pulumi.get(self, "grid_home")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external cluster.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isFlexCluster")
    def is_flex_cluster(self) -> bool:
        """
        Indicates whether the cluster is Oracle Flex Cluster or not.
        """
        return pulumi.get(self, "is_flex_cluster")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        Additional information about the current lifecycle state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="networkConfigurations")
    def network_configurations(self) -> Sequence['outputs.GetExternalClusterNetworkConfigurationResult']:
        """
        The list of network address configurations of the external cluster.
        """
        return pulumi.get(self, "network_configurations")

    @property
    @pulumi.getter(name="ocrFileLocation")
    def ocr_file_location(self) -> str:
        """
        The location of the Oracle Cluster Registry (OCR).
        """
        return pulumi.get(self, "ocr_file_location")

    @property
    @pulumi.getter(name="scanConfigurations")
    def scan_configurations(self) -> Sequence['outputs.GetExternalClusterScanConfigurationResult']:
        """
        The list of Single Client Access Name (SCAN) configurations of the external cluster.
        """
        return pulumi.get(self, "scan_configurations")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current lifecycle state of the external cluster.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the external cluster was created.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The date and time the external cluster was last updated.
        """
        return pulumi.get(self, "time_updated")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        The cluster version.
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="vipConfigurations")
    def vip_configurations(self) -> Sequence['outputs.GetExternalClusterVipConfigurationResult']:
        """
        The list of Virtual IP (VIP) configurations of the external cluster.
        """
        return pulumi.get(self, "vip_configurations")


class AwaitableGetExternalClusterResult(GetExternalClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExternalClusterResult(
            additional_details=self.additional_details,
            compartment_id=self.compartment_id,
            component_name=self.component_name,
            display_name=self.display_name,
            external_cluster_id=self.external_cluster_id,
            external_connector_id=self.external_connector_id,
            external_db_system_id=self.external_db_system_id,
            grid_home=self.grid_home,
            id=self.id,
            is_flex_cluster=self.is_flex_cluster,
            lifecycle_details=self.lifecycle_details,
            network_configurations=self.network_configurations,
            ocr_file_location=self.ocr_file_location,
            scan_configurations=self.scan_configurations,
            state=self.state,
            time_created=self.time_created,
            time_updated=self.time_updated,
            version=self.version,
            vip_configurations=self.vip_configurations)


def get_external_cluster(external_cluster_id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExternalClusterResult:
    """
    This data source provides details about a specific External Cluster resource in Oracle Cloud Infrastructure Database Management service.

    Gets the details for the external cluster specified by `externalClusterId`.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_external_cluster = oci.DatabaseManagement.get_external_cluster(external_cluster_id=oci_database_management_external_cluster["test_external_cluster"]["id"])
    ```


    :param str external_cluster_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external cluster.
    """
    __args__ = dict()
    __args__['externalClusterId'] = external_cluster_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseManagement/getExternalCluster:getExternalCluster', __args__, opts=opts, typ=GetExternalClusterResult).value

    return AwaitableGetExternalClusterResult(
        additional_details=pulumi.get(__ret__, 'additional_details'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        component_name=pulumi.get(__ret__, 'component_name'),
        display_name=pulumi.get(__ret__, 'display_name'),
        external_cluster_id=pulumi.get(__ret__, 'external_cluster_id'),
        external_connector_id=pulumi.get(__ret__, 'external_connector_id'),
        external_db_system_id=pulumi.get(__ret__, 'external_db_system_id'),
        grid_home=pulumi.get(__ret__, 'grid_home'),
        id=pulumi.get(__ret__, 'id'),
        is_flex_cluster=pulumi.get(__ret__, 'is_flex_cluster'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        network_configurations=pulumi.get(__ret__, 'network_configurations'),
        ocr_file_location=pulumi.get(__ret__, 'ocr_file_location'),
        scan_configurations=pulumi.get(__ret__, 'scan_configurations'),
        state=pulumi.get(__ret__, 'state'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'),
        version=pulumi.get(__ret__, 'version'),
        vip_configurations=pulumi.get(__ret__, 'vip_configurations'))


@_utilities.lift_output_func(get_external_cluster)
def get_external_cluster_output(external_cluster_id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExternalClusterResult]:
    """
    This data source provides details about a specific External Cluster resource in Oracle Cloud Infrastructure Database Management service.

    Gets the details for the external cluster specified by `externalClusterId`.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_external_cluster = oci.DatabaseManagement.get_external_cluster(external_cluster_id=oci_database_management_external_cluster["test_external_cluster"]["id"])
    ```


    :param str external_cluster_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external cluster.
    """
    ...
