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
    'GetAutonomousVmClusterResult',
    'AwaitableGetAutonomousVmClusterResult',
    'get_autonomous_vm_cluster',
    'get_autonomous_vm_cluster_output',
]

@pulumi.output_type
class GetAutonomousVmClusterResult:
    """
    A collection of values returned by getAutonomousVmCluster.
    """
    def __init__(__self__, autonomous_data_storage_size_in_tbs=None, autonomous_vm_cluster_id=None, available_autonomous_data_storage_size_in_tbs=None, available_container_databases=None, available_cpus=None, available_data_storage_size_in_tbs=None, compartment_id=None, compute_model=None, cpu_core_count_per_node=None, cpus_enabled=None, data_storage_size_in_gb=None, data_storage_size_in_tbs=None, db_node_storage_size_in_gbs=None, db_servers=None, defined_tags=None, display_name=None, exadata_infrastructure_id=None, freeform_tags=None, id=None, is_local_backup_enabled=None, is_mtls_enabled=None, last_maintenance_run_id=None, license_model=None, lifecycle_details=None, maintenance_window_details=None, maintenance_windows=None, memory_per_oracle_compute_unit_in_gbs=None, memory_size_in_gbs=None, next_maintenance_run_id=None, node_count=None, ocpus_enabled=None, reclaimable_cpus=None, scan_listener_port_non_tls=None, scan_listener_port_tls=None, state=None, time_created=None, time_database_ssl_certificate_expires=None, time_ords_certificate_expires=None, time_zone=None, total_container_databases=None, vm_cluster_network_id=None):
        if autonomous_data_storage_size_in_tbs and not isinstance(autonomous_data_storage_size_in_tbs, float):
            raise TypeError("Expected argument 'autonomous_data_storage_size_in_tbs' to be a float")
        pulumi.set(__self__, "autonomous_data_storage_size_in_tbs", autonomous_data_storage_size_in_tbs)
        if autonomous_vm_cluster_id and not isinstance(autonomous_vm_cluster_id, str):
            raise TypeError("Expected argument 'autonomous_vm_cluster_id' to be a str")
        pulumi.set(__self__, "autonomous_vm_cluster_id", autonomous_vm_cluster_id)
        if available_autonomous_data_storage_size_in_tbs and not isinstance(available_autonomous_data_storage_size_in_tbs, float):
            raise TypeError("Expected argument 'available_autonomous_data_storage_size_in_tbs' to be a float")
        pulumi.set(__self__, "available_autonomous_data_storage_size_in_tbs", available_autonomous_data_storage_size_in_tbs)
        if available_container_databases and not isinstance(available_container_databases, int):
            raise TypeError("Expected argument 'available_container_databases' to be a int")
        pulumi.set(__self__, "available_container_databases", available_container_databases)
        if available_cpus and not isinstance(available_cpus, int):
            raise TypeError("Expected argument 'available_cpus' to be a int")
        pulumi.set(__self__, "available_cpus", available_cpus)
        if available_data_storage_size_in_tbs and not isinstance(available_data_storage_size_in_tbs, float):
            raise TypeError("Expected argument 'available_data_storage_size_in_tbs' to be a float")
        pulumi.set(__self__, "available_data_storage_size_in_tbs", available_data_storage_size_in_tbs)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if compute_model and not isinstance(compute_model, str):
            raise TypeError("Expected argument 'compute_model' to be a str")
        pulumi.set(__self__, "compute_model", compute_model)
        if cpu_core_count_per_node and not isinstance(cpu_core_count_per_node, int):
            raise TypeError("Expected argument 'cpu_core_count_per_node' to be a int")
        pulumi.set(__self__, "cpu_core_count_per_node", cpu_core_count_per_node)
        if cpus_enabled and not isinstance(cpus_enabled, int):
            raise TypeError("Expected argument 'cpus_enabled' to be a int")
        pulumi.set(__self__, "cpus_enabled", cpus_enabled)
        if data_storage_size_in_gb and not isinstance(data_storage_size_in_gb, float):
            raise TypeError("Expected argument 'data_storage_size_in_gb' to be a float")
        pulumi.set(__self__, "data_storage_size_in_gb", data_storage_size_in_gb)
        if data_storage_size_in_tbs and not isinstance(data_storage_size_in_tbs, float):
            raise TypeError("Expected argument 'data_storage_size_in_tbs' to be a float")
        pulumi.set(__self__, "data_storage_size_in_tbs", data_storage_size_in_tbs)
        if db_node_storage_size_in_gbs and not isinstance(db_node_storage_size_in_gbs, int):
            raise TypeError("Expected argument 'db_node_storage_size_in_gbs' to be a int")
        pulumi.set(__self__, "db_node_storage_size_in_gbs", db_node_storage_size_in_gbs)
        if db_servers and not isinstance(db_servers, list):
            raise TypeError("Expected argument 'db_servers' to be a list")
        pulumi.set(__self__, "db_servers", db_servers)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if exadata_infrastructure_id and not isinstance(exadata_infrastructure_id, str):
            raise TypeError("Expected argument 'exadata_infrastructure_id' to be a str")
        pulumi.set(__self__, "exadata_infrastructure_id", exadata_infrastructure_id)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_local_backup_enabled and not isinstance(is_local_backup_enabled, bool):
            raise TypeError("Expected argument 'is_local_backup_enabled' to be a bool")
        pulumi.set(__self__, "is_local_backup_enabled", is_local_backup_enabled)
        if is_mtls_enabled and not isinstance(is_mtls_enabled, bool):
            raise TypeError("Expected argument 'is_mtls_enabled' to be a bool")
        pulumi.set(__self__, "is_mtls_enabled", is_mtls_enabled)
        if last_maintenance_run_id and not isinstance(last_maintenance_run_id, str):
            raise TypeError("Expected argument 'last_maintenance_run_id' to be a str")
        pulumi.set(__self__, "last_maintenance_run_id", last_maintenance_run_id)
        if license_model and not isinstance(license_model, str):
            raise TypeError("Expected argument 'license_model' to be a str")
        pulumi.set(__self__, "license_model", license_model)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if maintenance_window_details and not isinstance(maintenance_window_details, list):
            raise TypeError("Expected argument 'maintenance_window_details' to be a list")
        pulumi.set(__self__, "maintenance_window_details", maintenance_window_details)
        if maintenance_windows and not isinstance(maintenance_windows, list):
            raise TypeError("Expected argument 'maintenance_windows' to be a list")
        pulumi.set(__self__, "maintenance_windows", maintenance_windows)
        if memory_per_oracle_compute_unit_in_gbs and not isinstance(memory_per_oracle_compute_unit_in_gbs, int):
            raise TypeError("Expected argument 'memory_per_oracle_compute_unit_in_gbs' to be a int")
        pulumi.set(__self__, "memory_per_oracle_compute_unit_in_gbs", memory_per_oracle_compute_unit_in_gbs)
        if memory_size_in_gbs and not isinstance(memory_size_in_gbs, int):
            raise TypeError("Expected argument 'memory_size_in_gbs' to be a int")
        pulumi.set(__self__, "memory_size_in_gbs", memory_size_in_gbs)
        if next_maintenance_run_id and not isinstance(next_maintenance_run_id, str):
            raise TypeError("Expected argument 'next_maintenance_run_id' to be a str")
        pulumi.set(__self__, "next_maintenance_run_id", next_maintenance_run_id)
        if node_count and not isinstance(node_count, int):
            raise TypeError("Expected argument 'node_count' to be a int")
        pulumi.set(__self__, "node_count", node_count)
        if ocpus_enabled and not isinstance(ocpus_enabled, float):
            raise TypeError("Expected argument 'ocpus_enabled' to be a float")
        pulumi.set(__self__, "ocpus_enabled", ocpus_enabled)
        if reclaimable_cpus and not isinstance(reclaimable_cpus, int):
            raise TypeError("Expected argument 'reclaimable_cpus' to be a int")
        pulumi.set(__self__, "reclaimable_cpus", reclaimable_cpus)
        if scan_listener_port_non_tls and not isinstance(scan_listener_port_non_tls, int):
            raise TypeError("Expected argument 'scan_listener_port_non_tls' to be a int")
        pulumi.set(__self__, "scan_listener_port_non_tls", scan_listener_port_non_tls)
        if scan_listener_port_tls and not isinstance(scan_listener_port_tls, int):
            raise TypeError("Expected argument 'scan_listener_port_tls' to be a int")
        pulumi.set(__self__, "scan_listener_port_tls", scan_listener_port_tls)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_database_ssl_certificate_expires and not isinstance(time_database_ssl_certificate_expires, str):
            raise TypeError("Expected argument 'time_database_ssl_certificate_expires' to be a str")
        pulumi.set(__self__, "time_database_ssl_certificate_expires", time_database_ssl_certificate_expires)
        if time_ords_certificate_expires and not isinstance(time_ords_certificate_expires, str):
            raise TypeError("Expected argument 'time_ords_certificate_expires' to be a str")
        pulumi.set(__self__, "time_ords_certificate_expires", time_ords_certificate_expires)
        if time_zone and not isinstance(time_zone, str):
            raise TypeError("Expected argument 'time_zone' to be a str")
        pulumi.set(__self__, "time_zone", time_zone)
        if total_container_databases and not isinstance(total_container_databases, int):
            raise TypeError("Expected argument 'total_container_databases' to be a int")
        pulumi.set(__self__, "total_container_databases", total_container_databases)
        if vm_cluster_network_id and not isinstance(vm_cluster_network_id, str):
            raise TypeError("Expected argument 'vm_cluster_network_id' to be a str")
        pulumi.set(__self__, "vm_cluster_network_id", vm_cluster_network_id)

    @property
    @pulumi.getter(name="autonomousDataStorageSizeInTbs")
    def autonomous_data_storage_size_in_tbs(self) -> float:
        """
        The data disk group size allocated for Autonomous Databases, in TBs.
        """
        return pulumi.get(self, "autonomous_data_storage_size_in_tbs")

    @property
    @pulumi.getter(name="autonomousVmClusterId")
    def autonomous_vm_cluster_id(self) -> str:
        return pulumi.get(self, "autonomous_vm_cluster_id")

    @property
    @pulumi.getter(name="availableAutonomousDataStorageSizeInTbs")
    def available_autonomous_data_storage_size_in_tbs(self) -> float:
        """
        The data disk group size available for Autonomous Databases, in TBs.
        """
        return pulumi.get(self, "available_autonomous_data_storage_size_in_tbs")

    @property
    @pulumi.getter(name="availableContainerDatabases")
    def available_container_databases(self) -> int:
        """
        The number of Autonomous Container Databases that can be created with the currently available local storage.
        """
        return pulumi.get(self, "available_container_databases")

    @property
    @pulumi.getter(name="availableCpus")
    def available_cpus(self) -> int:
        """
        The numnber of CPU cores available.
        """
        return pulumi.get(self, "available_cpus")

    @property
    @pulumi.getter(name="availableDataStorageSizeInTbs")
    def available_data_storage_size_in_tbs(self) -> float:
        """
        **Deprecated.** Use `availableAutonomousDataStorageSizeInTBs` for Autonomous Databases' data storage availability in TBs.
        """
        return pulumi.get(self, "available_data_storage_size_in_tbs")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="computeModel")
    def compute_model(self) -> str:
        """
        The compute model of the Autonomous VM Cluster.
        """
        return pulumi.get(self, "compute_model")

    @property
    @pulumi.getter(name="cpuCoreCountPerNode")
    def cpu_core_count_per_node(self) -> int:
        """
        The number of CPU cores enabled per VM cluster node.
        """
        return pulumi.get(self, "cpu_core_count_per_node")

    @property
    @pulumi.getter(name="cpusEnabled")
    def cpus_enabled(self) -> int:
        """
        The number of enabled CPU cores.
        """
        return pulumi.get(self, "cpus_enabled")

    @property
    @pulumi.getter(name="dataStorageSizeInGb")
    def data_storage_size_in_gb(self) -> float:
        """
        The total data storage allocated in GBs.
        """
        return pulumi.get(self, "data_storage_size_in_gb")

    @property
    @pulumi.getter(name="dataStorageSizeInTbs")
    def data_storage_size_in_tbs(self) -> float:
        """
        The total data storage allocated in TBs
        """
        return pulumi.get(self, "data_storage_size_in_tbs")

    @property
    @pulumi.getter(name="dbNodeStorageSizeInGbs")
    def db_node_storage_size_in_gbs(self) -> int:
        """
        The local node storage allocated in GBs.
        """
        return pulumi.get(self, "db_node_storage_size_in_gbs")

    @property
    @pulumi.getter(name="dbServers")
    def db_servers(self) -> Sequence[str]:
        """
        The list of [OCIDs](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Db servers.
        """
        return pulumi.get(self, "db_servers")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The user-friendly name for the Autonomous VM cluster. The name does not need to be unique.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="exadataInfrastructureId")
    def exadata_infrastructure_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Exadata infrastructure.
        """
        return pulumi.get(self, "exadata_infrastructure_id")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Autonomous VM cluster.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isLocalBackupEnabled")
    def is_local_backup_enabled(self) -> bool:
        """
        If true, database backup on local Exadata storage is configured for the Autonomous VM cluster. If false, database backup on local Exadata storage is not available in the Autonomous VM cluster.
        """
        return pulumi.get(self, "is_local_backup_enabled")

    @property
    @pulumi.getter(name="isMtlsEnabled")
    def is_mtls_enabled(self) -> bool:
        """
        Enable mutual TLS(mTLS) authentication for database while provisioning a VMCluster. Default is TLS.
        """
        return pulumi.get(self, "is_mtls_enabled")

    @property
    @pulumi.getter(name="lastMaintenanceRunId")
    def last_maintenance_run_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the last maintenance run.
        """
        return pulumi.get(self, "last_maintenance_run_id")

    @property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> str:
        """
        The Oracle license model that applies to the Autonomous VM cluster. The default is LICENSE_INCLUDED.
        """
        return pulumi.get(self, "license_model")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        Additional information about the current lifecycle state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="maintenanceWindowDetails")
    def maintenance_window_details(self) -> Sequence['outputs.GetAutonomousVmClusterMaintenanceWindowDetailResult']:
        return pulumi.get(self, "maintenance_window_details")

    @property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> Sequence['outputs.GetAutonomousVmClusterMaintenanceWindowResult']:
        """
        The scheduling details for the quarterly maintenance window. Patching and system updates take place during the maintenance window.
        """
        return pulumi.get(self, "maintenance_windows")

    @property
    @pulumi.getter(name="memoryPerOracleComputeUnitInGbs")
    def memory_per_oracle_compute_unit_in_gbs(self) -> int:
        """
        The amount of memory (in GBs) to be enabled per OCPU or ECPU.
        """
        return pulumi.get(self, "memory_per_oracle_compute_unit_in_gbs")

    @property
    @pulumi.getter(name="memorySizeInGbs")
    def memory_size_in_gbs(self) -> int:
        """
        The memory allocated in GBs.
        """
        return pulumi.get(self, "memory_size_in_gbs")

    @property
    @pulumi.getter(name="nextMaintenanceRunId")
    def next_maintenance_run_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the next maintenance run.
        """
        return pulumi.get(self, "next_maintenance_run_id")

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> int:
        """
        The number of nodes in the Autonomous VM Cluster.
        """
        return pulumi.get(self, "node_count")

    @property
    @pulumi.getter(name="ocpusEnabled")
    def ocpus_enabled(self) -> float:
        """
        The number of enabled OCPU cores.
        """
        return pulumi.get(self, "ocpus_enabled")

    @property
    @pulumi.getter(name="reclaimableCpus")
    def reclaimable_cpus(self) -> int:
        """
        For Autonomous Databases on Dedicated Exadata Infrastructure:
        * These are the CPUs that continue to be included in the count of CPUs available to the Autonomous Container Database even after one of its Autonomous Database is terminated or scaled down. You can release them to the available CPUs at its parent Autonomous VM Cluster level by restarting the Autonomous Container Database.
        * The CPU type (OCPUs or ECPUs) is determined by the parent Autonomous Exadata VM Cluster's compute model.
        """
        return pulumi.get(self, "reclaimable_cpus")

    @property
    @pulumi.getter(name="scanListenerPortNonTls")
    def scan_listener_port_non_tls(self) -> int:
        """
        The SCAN Listener Non TLS port number. Default value is 1521.
        """
        return pulumi.get(self, "scan_listener_port_non_tls")

    @property
    @pulumi.getter(name="scanListenerPortTls")
    def scan_listener_port_tls(self) -> int:
        """
        The SCAN Listener TLS port number. Default value is 2484.
        """
        return pulumi.get(self, "scan_listener_port_tls")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the Autonomous VM cluster.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time that the Autonomous VM cluster was created.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeDatabaseSslCertificateExpires")
    def time_database_ssl_certificate_expires(self) -> str:
        """
        The date and time of Database SSL certificate expiration.
        """
        return pulumi.get(self, "time_database_ssl_certificate_expires")

    @property
    @pulumi.getter(name="timeOrdsCertificateExpires")
    def time_ords_certificate_expires(self) -> str:
        """
        The date and time of ORDS certificate expiration.
        """
        return pulumi.get(self, "time_ords_certificate_expires")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> str:
        """
        The time zone to use for the Autonomous VM cluster. For details, see [DB System Time Zones](https://docs.cloud.oracle.com/iaas/Content/Database/References/timezones.htm).
        """
        return pulumi.get(self, "time_zone")

    @property
    @pulumi.getter(name="totalContainerDatabases")
    def total_container_databases(self) -> int:
        """
        The total number of Autonomous Container Databases that can be created.
        """
        return pulumi.get(self, "total_container_databases")

    @property
    @pulumi.getter(name="vmClusterNetworkId")
    def vm_cluster_network_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VM cluster network.
        """
        return pulumi.get(self, "vm_cluster_network_id")


class AwaitableGetAutonomousVmClusterResult(GetAutonomousVmClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAutonomousVmClusterResult(
            autonomous_data_storage_size_in_tbs=self.autonomous_data_storage_size_in_tbs,
            autonomous_vm_cluster_id=self.autonomous_vm_cluster_id,
            available_autonomous_data_storage_size_in_tbs=self.available_autonomous_data_storage_size_in_tbs,
            available_container_databases=self.available_container_databases,
            available_cpus=self.available_cpus,
            available_data_storage_size_in_tbs=self.available_data_storage_size_in_tbs,
            compartment_id=self.compartment_id,
            compute_model=self.compute_model,
            cpu_core_count_per_node=self.cpu_core_count_per_node,
            cpus_enabled=self.cpus_enabled,
            data_storage_size_in_gb=self.data_storage_size_in_gb,
            data_storage_size_in_tbs=self.data_storage_size_in_tbs,
            db_node_storage_size_in_gbs=self.db_node_storage_size_in_gbs,
            db_servers=self.db_servers,
            defined_tags=self.defined_tags,
            display_name=self.display_name,
            exadata_infrastructure_id=self.exadata_infrastructure_id,
            freeform_tags=self.freeform_tags,
            id=self.id,
            is_local_backup_enabled=self.is_local_backup_enabled,
            is_mtls_enabled=self.is_mtls_enabled,
            last_maintenance_run_id=self.last_maintenance_run_id,
            license_model=self.license_model,
            lifecycle_details=self.lifecycle_details,
            maintenance_window_details=self.maintenance_window_details,
            maintenance_windows=self.maintenance_windows,
            memory_per_oracle_compute_unit_in_gbs=self.memory_per_oracle_compute_unit_in_gbs,
            memory_size_in_gbs=self.memory_size_in_gbs,
            next_maintenance_run_id=self.next_maintenance_run_id,
            node_count=self.node_count,
            ocpus_enabled=self.ocpus_enabled,
            reclaimable_cpus=self.reclaimable_cpus,
            scan_listener_port_non_tls=self.scan_listener_port_non_tls,
            scan_listener_port_tls=self.scan_listener_port_tls,
            state=self.state,
            time_created=self.time_created,
            time_database_ssl_certificate_expires=self.time_database_ssl_certificate_expires,
            time_ords_certificate_expires=self.time_ords_certificate_expires,
            time_zone=self.time_zone,
            total_container_databases=self.total_container_databases,
            vm_cluster_network_id=self.vm_cluster_network_id)


def get_autonomous_vm_cluster(autonomous_vm_cluster_id: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAutonomousVmClusterResult:
    """
    This data source provides details about a specific Autonomous Vm Cluster resource in Oracle Cloud Infrastructure Database service.

    Gets information about the specified Autonomous VM cluster for an Exadata Cloud@Customer system. To get information about an Autonomous VM Cluster in the Oracle cloud, see [GetCloudAutonomousVmCluster](https://docs.cloud.oracle.com/iaas/api/#/en/database/latest/CloudAutonomousVmCluster/GetCloudAutonomousVmCluster).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_autonomous_vm_cluster = oci.Database.get_autonomous_vm_cluster(autonomous_vm_cluster_id=oci_database_autonomous_vm_cluster["test_autonomous_vm_cluster"]["id"])
    ```


    :param str autonomous_vm_cluster_id: The autonomous VM cluster [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    """
    __args__ = dict()
    __args__['autonomousVmClusterId'] = autonomous_vm_cluster_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Database/getAutonomousVmCluster:getAutonomousVmCluster', __args__, opts=opts, typ=GetAutonomousVmClusterResult).value

    return AwaitableGetAutonomousVmClusterResult(
        autonomous_data_storage_size_in_tbs=pulumi.get(__ret__, 'autonomous_data_storage_size_in_tbs'),
        autonomous_vm_cluster_id=pulumi.get(__ret__, 'autonomous_vm_cluster_id'),
        available_autonomous_data_storage_size_in_tbs=pulumi.get(__ret__, 'available_autonomous_data_storage_size_in_tbs'),
        available_container_databases=pulumi.get(__ret__, 'available_container_databases'),
        available_cpus=pulumi.get(__ret__, 'available_cpus'),
        available_data_storage_size_in_tbs=pulumi.get(__ret__, 'available_data_storage_size_in_tbs'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        compute_model=pulumi.get(__ret__, 'compute_model'),
        cpu_core_count_per_node=pulumi.get(__ret__, 'cpu_core_count_per_node'),
        cpus_enabled=pulumi.get(__ret__, 'cpus_enabled'),
        data_storage_size_in_gb=pulumi.get(__ret__, 'data_storage_size_in_gb'),
        data_storage_size_in_tbs=pulumi.get(__ret__, 'data_storage_size_in_tbs'),
        db_node_storage_size_in_gbs=pulumi.get(__ret__, 'db_node_storage_size_in_gbs'),
        db_servers=pulumi.get(__ret__, 'db_servers'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        display_name=pulumi.get(__ret__, 'display_name'),
        exadata_infrastructure_id=pulumi.get(__ret__, 'exadata_infrastructure_id'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        is_local_backup_enabled=pulumi.get(__ret__, 'is_local_backup_enabled'),
        is_mtls_enabled=pulumi.get(__ret__, 'is_mtls_enabled'),
        last_maintenance_run_id=pulumi.get(__ret__, 'last_maintenance_run_id'),
        license_model=pulumi.get(__ret__, 'license_model'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        maintenance_window_details=pulumi.get(__ret__, 'maintenance_window_details'),
        maintenance_windows=pulumi.get(__ret__, 'maintenance_windows'),
        memory_per_oracle_compute_unit_in_gbs=pulumi.get(__ret__, 'memory_per_oracle_compute_unit_in_gbs'),
        memory_size_in_gbs=pulumi.get(__ret__, 'memory_size_in_gbs'),
        next_maintenance_run_id=pulumi.get(__ret__, 'next_maintenance_run_id'),
        node_count=pulumi.get(__ret__, 'node_count'),
        ocpus_enabled=pulumi.get(__ret__, 'ocpus_enabled'),
        reclaimable_cpus=pulumi.get(__ret__, 'reclaimable_cpus'),
        scan_listener_port_non_tls=pulumi.get(__ret__, 'scan_listener_port_non_tls'),
        scan_listener_port_tls=pulumi.get(__ret__, 'scan_listener_port_tls'),
        state=pulumi.get(__ret__, 'state'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_database_ssl_certificate_expires=pulumi.get(__ret__, 'time_database_ssl_certificate_expires'),
        time_ords_certificate_expires=pulumi.get(__ret__, 'time_ords_certificate_expires'),
        time_zone=pulumi.get(__ret__, 'time_zone'),
        total_container_databases=pulumi.get(__ret__, 'total_container_databases'),
        vm_cluster_network_id=pulumi.get(__ret__, 'vm_cluster_network_id'))


@_utilities.lift_output_func(get_autonomous_vm_cluster)
def get_autonomous_vm_cluster_output(autonomous_vm_cluster_id: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAutonomousVmClusterResult]:
    """
    This data source provides details about a specific Autonomous Vm Cluster resource in Oracle Cloud Infrastructure Database service.

    Gets information about the specified Autonomous VM cluster for an Exadata Cloud@Customer system. To get information about an Autonomous VM Cluster in the Oracle cloud, see [GetCloudAutonomousVmCluster](https://docs.cloud.oracle.com/iaas/api/#/en/database/latest/CloudAutonomousVmCluster/GetCloudAutonomousVmCluster).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_autonomous_vm_cluster = oci.Database.get_autonomous_vm_cluster(autonomous_vm_cluster_id=oci_database_autonomous_vm_cluster["test_autonomous_vm_cluster"]["id"])
    ```


    :param str autonomous_vm_cluster_id: The autonomous VM cluster [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    """
    ...
