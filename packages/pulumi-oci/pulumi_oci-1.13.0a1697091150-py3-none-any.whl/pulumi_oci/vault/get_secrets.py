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
    'GetSecretsResult',
    'AwaitableGetSecretsResult',
    'get_secrets',
    'get_secrets_output',
]

@pulumi.output_type
class GetSecretsResult:
    """
    A collection of values returned by getSecrets.
    """
    def __init__(__self__, compartment_id=None, filters=None, id=None, name=None, secrets=None, state=None, vault_id=None):
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
        if secrets and not isinstance(secrets, list):
            raise TypeError("Expected argument 'secrets' to be a list")
        pulumi.set(__self__, "secrets", secrets)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if vault_id and not isinstance(vault_id, str):
            raise TypeError("Expected argument 'vault_id' to be a str")
        pulumi.set(__self__, "vault_id", vault_id)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment where you want to create the secret.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetSecretsFilterResult']]:
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
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def secrets(self) -> Sequence['outputs.GetSecretsSecretResult']:
        """
        The list of secrets.
        """
        return pulumi.get(self, "secrets")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current lifecycle state of the secret.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="vaultId")
    def vault_id(self) -> Optional[str]:
        """
        The OCID of the Vault in which the secret exists
        """
        return pulumi.get(self, "vault_id")


class AwaitableGetSecretsResult(GetSecretsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecretsResult(
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            name=self.name,
            secrets=self.secrets,
            state=self.state,
            vault_id=self.vault_id)


def get_secrets(compartment_id: Optional[str] = None,
                filters: Optional[Sequence[pulumi.InputType['GetSecretsFilterArgs']]] = None,
                name: Optional[str] = None,
                state: Optional[str] = None,
                vault_id: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecretsResult:
    """
    This data source provides the list of Secrets in Oracle Cloud Infrastructure Vault service.

    Lists all secrets in the specified vault and compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_secrets = oci.Vault.get_secrets(compartment_id=var["compartment_id"],
        name=var["secret_name"],
        state=var["secret_state"],
        vault_id=oci_kms_vault["test_vault"]["id"])
    ```


    :param str compartment_id: The OCID of the compartment.
    :param str name: The secret name.
    :param str state: A filter that returns only resources that match the specified lifecycle state. The state value is case-insensitive.
    :param str vault_id: The OCID of the vault.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['name'] = name
    __args__['state'] = state
    __args__['vaultId'] = vault_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Vault/getSecrets:getSecrets', __args__, opts=opts, typ=GetSecretsResult).value

    return AwaitableGetSecretsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        secrets=pulumi.get(__ret__, 'secrets'),
        state=pulumi.get(__ret__, 'state'),
        vault_id=pulumi.get(__ret__, 'vault_id'))


@_utilities.lift_output_func(get_secrets)
def get_secrets_output(compartment_id: Optional[pulumi.Input[str]] = None,
                       filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetSecretsFilterArgs']]]]] = None,
                       name: Optional[pulumi.Input[Optional[str]]] = None,
                       state: Optional[pulumi.Input[Optional[str]]] = None,
                       vault_id: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecretsResult]:
    """
    This data source provides the list of Secrets in Oracle Cloud Infrastructure Vault service.

    Lists all secrets in the specified vault and compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_secrets = oci.Vault.get_secrets(compartment_id=var["compartment_id"],
        name=var["secret_name"],
        state=var["secret_state"],
        vault_id=oci_kms_vault["test_vault"]["id"])
    ```


    :param str compartment_id: The OCID of the compartment.
    :param str name: The secret name.
    :param str state: A filter that returns only resources that match the specified lifecycle state. The state value is case-insensitive.
    :param str vault_id: The OCID of the vault.
    """
    ...
