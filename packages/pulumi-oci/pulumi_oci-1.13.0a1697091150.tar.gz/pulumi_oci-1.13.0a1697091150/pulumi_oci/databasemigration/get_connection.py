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
    'GetConnectionResult',
    'AwaitableGetConnectionResult',
    'get_connection',
    'get_connection_output',
]

@pulumi.output_type
class GetConnectionResult:
    """
    A collection of values returned by getConnection.
    """
    def __init__(__self__, admin_credentials=None, certificate_tdn=None, compartment_id=None, connect_descriptors=None, connection_id=None, credentials_secret_id=None, database_id=None, database_type=None, defined_tags=None, display_name=None, freeform_tags=None, id=None, lifecycle_details=None, nsg_ids=None, private_endpoints=None, replication_credentials=None, ssh_details=None, state=None, system_tags=None, time_created=None, time_updated=None, tls_keystore=None, tls_wallet=None, vault_details=None):
        if admin_credentials and not isinstance(admin_credentials, list):
            raise TypeError("Expected argument 'admin_credentials' to be a list")
        pulumi.set(__self__, "admin_credentials", admin_credentials)
        if certificate_tdn and not isinstance(certificate_tdn, str):
            raise TypeError("Expected argument 'certificate_tdn' to be a str")
        pulumi.set(__self__, "certificate_tdn", certificate_tdn)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if connect_descriptors and not isinstance(connect_descriptors, list):
            raise TypeError("Expected argument 'connect_descriptors' to be a list")
        pulumi.set(__self__, "connect_descriptors", connect_descriptors)
        if connection_id and not isinstance(connection_id, str):
            raise TypeError("Expected argument 'connection_id' to be a str")
        pulumi.set(__self__, "connection_id", connection_id)
        if credentials_secret_id and not isinstance(credentials_secret_id, str):
            raise TypeError("Expected argument 'credentials_secret_id' to be a str")
        pulumi.set(__self__, "credentials_secret_id", credentials_secret_id)
        if database_id and not isinstance(database_id, str):
            raise TypeError("Expected argument 'database_id' to be a str")
        pulumi.set(__self__, "database_id", database_id)
        if database_type and not isinstance(database_type, str):
            raise TypeError("Expected argument 'database_type' to be a str")
        pulumi.set(__self__, "database_type", database_type)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if nsg_ids and not isinstance(nsg_ids, list):
            raise TypeError("Expected argument 'nsg_ids' to be a list")
        pulumi.set(__self__, "nsg_ids", nsg_ids)
        if private_endpoints and not isinstance(private_endpoints, list):
            raise TypeError("Expected argument 'private_endpoints' to be a list")
        pulumi.set(__self__, "private_endpoints", private_endpoints)
        if replication_credentials and not isinstance(replication_credentials, list):
            raise TypeError("Expected argument 'replication_credentials' to be a list")
        pulumi.set(__self__, "replication_credentials", replication_credentials)
        if ssh_details and not isinstance(ssh_details, list):
            raise TypeError("Expected argument 'ssh_details' to be a list")
        pulumi.set(__self__, "ssh_details", ssh_details)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)
        if tls_keystore and not isinstance(tls_keystore, str):
            raise TypeError("Expected argument 'tls_keystore' to be a str")
        pulumi.set(__self__, "tls_keystore", tls_keystore)
        if tls_wallet and not isinstance(tls_wallet, str):
            raise TypeError("Expected argument 'tls_wallet' to be a str")
        pulumi.set(__self__, "tls_wallet", tls_wallet)
        if vault_details and not isinstance(vault_details, list):
            raise TypeError("Expected argument 'vault_details' to be a list")
        pulumi.set(__self__, "vault_details", vault_details)

    @property
    @pulumi.getter(name="adminCredentials")
    def admin_credentials(self) -> Sequence['outputs.GetConnectionAdminCredentialResult']:
        """
        Database Administrator Credentials details.
        """
        return pulumi.get(self, "admin_credentials")

    @property
    @pulumi.getter(name="certificateTdn")
    def certificate_tdn(self) -> str:
        """
        This name is the distinguished name used while creating the certificate on target database.
        """
        return pulumi.get(self, "certificate_tdn")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        OCID of the compartment where the secret containing the credentials will be created.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="connectDescriptors")
    def connect_descriptors(self) -> Sequence['outputs.GetConnectionConnectDescriptorResult']:
        """
        Connect Descriptor details.
        """
        return pulumi.get(self, "connect_descriptors")

    @property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> str:
        return pulumi.get(self, "connection_id")

    @property
    @pulumi.getter(name="credentialsSecretId")
    def credentials_secret_id(self) -> str:
        """
        OCID of the Secret in the Oracle Cloud Infrastructure vault containing the Database Connection credentials.
        """
        return pulumi.get(self, "credentials_secret_id")

    @property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> str:
        """
        The OCID of the cloud database.
        """
        return pulumi.get(self, "database_id")

    @property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> str:
        """
        Database connection type.
        """
        return pulumi.get(self, "database_type")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Database Connection display name identifier.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a previously created Private Endpoint.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="nsgIds")
    def nsg_ids(self) -> Sequence[str]:
        """
        An array of Network Security Group OCIDs used to define network access for Connections.
        """
        return pulumi.get(self, "nsg_ids")

    @property
    @pulumi.getter(name="privateEndpoints")
    def private_endpoints(self) -> Sequence['outputs.GetConnectionPrivateEndpointResult']:
        """
        Oracle Cloud Infrastructure Private Endpoint configuration details.
        """
        return pulumi.get(self, "private_endpoints")

    @property
    @pulumi.getter(name="replicationCredentials")
    def replication_credentials(self) -> Sequence['outputs.GetConnectionReplicationCredentialResult']:
        """
        Database Administrator Credentials details.
        """
        return pulumi.get(self, "replication_credentials")

    @property
    @pulumi.getter(name="sshDetails")
    def ssh_details(self) -> Sequence['outputs.GetConnectionSshDetailResult']:
        """
        Details of the SSH key that will be used.
        """
        return pulumi.get(self, "ssh_details")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the Connection resource.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The time the Connection resource was created. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The time of the last Connection resource details update. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_updated")

    @property
    @pulumi.getter(name="tlsKeystore")
    def tls_keystore(self) -> str:
        return pulumi.get(self, "tls_keystore")

    @property
    @pulumi.getter(name="tlsWallet")
    def tls_wallet(self) -> str:
        return pulumi.get(self, "tls_wallet")

    @property
    @pulumi.getter(name="vaultDetails")
    def vault_details(self) -> Sequence['outputs.GetConnectionVaultDetailResult']:
        """
        Oracle Cloud Infrastructure Vault details to store migration and connection credentials secrets
        """
        return pulumi.get(self, "vault_details")


class AwaitableGetConnectionResult(GetConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConnectionResult(
            admin_credentials=self.admin_credentials,
            certificate_tdn=self.certificate_tdn,
            compartment_id=self.compartment_id,
            connect_descriptors=self.connect_descriptors,
            connection_id=self.connection_id,
            credentials_secret_id=self.credentials_secret_id,
            database_id=self.database_id,
            database_type=self.database_type,
            defined_tags=self.defined_tags,
            display_name=self.display_name,
            freeform_tags=self.freeform_tags,
            id=self.id,
            lifecycle_details=self.lifecycle_details,
            nsg_ids=self.nsg_ids,
            private_endpoints=self.private_endpoints,
            replication_credentials=self.replication_credentials,
            ssh_details=self.ssh_details,
            state=self.state,
            system_tags=self.system_tags,
            time_created=self.time_created,
            time_updated=self.time_updated,
            tls_keystore=self.tls_keystore,
            tls_wallet=self.tls_wallet,
            vault_details=self.vault_details)


def get_connection(connection_id: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConnectionResult:
    """
    This data source provides details about a specific Connection resource in Oracle Cloud Infrastructure Database Migration service.

    Display Database Connection details.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_connection = oci.DatabaseMigration.get_connection(connection_id=oci_database_migration_connection["test_connection"]["id"])
    ```


    :param str connection_id: The OCID of the database connection
    """
    __args__ = dict()
    __args__['connectionId'] = connection_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseMigration/getConnection:getConnection', __args__, opts=opts, typ=GetConnectionResult).value

    return AwaitableGetConnectionResult(
        admin_credentials=pulumi.get(__ret__, 'admin_credentials'),
        certificate_tdn=pulumi.get(__ret__, 'certificate_tdn'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        connect_descriptors=pulumi.get(__ret__, 'connect_descriptors'),
        connection_id=pulumi.get(__ret__, 'connection_id'),
        credentials_secret_id=pulumi.get(__ret__, 'credentials_secret_id'),
        database_id=pulumi.get(__ret__, 'database_id'),
        database_type=pulumi.get(__ret__, 'database_type'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        display_name=pulumi.get(__ret__, 'display_name'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        nsg_ids=pulumi.get(__ret__, 'nsg_ids'),
        private_endpoints=pulumi.get(__ret__, 'private_endpoints'),
        replication_credentials=pulumi.get(__ret__, 'replication_credentials'),
        ssh_details=pulumi.get(__ret__, 'ssh_details'),
        state=pulumi.get(__ret__, 'state'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'),
        tls_keystore=pulumi.get(__ret__, 'tls_keystore'),
        tls_wallet=pulumi.get(__ret__, 'tls_wallet'),
        vault_details=pulumi.get(__ret__, 'vault_details'))


@_utilities.lift_output_func(get_connection)
def get_connection_output(connection_id: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConnectionResult]:
    """
    This data source provides details about a specific Connection resource in Oracle Cloud Infrastructure Database Migration service.

    Display Database Connection details.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_connection = oci.DatabaseMigration.get_connection(connection_id=oci_database_migration_connection["test_connection"]["id"])
    ```


    :param str connection_id: The OCID of the database connection
    """
    ...
