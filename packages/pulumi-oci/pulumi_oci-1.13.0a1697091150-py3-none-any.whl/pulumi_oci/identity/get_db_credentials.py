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
    'GetDbCredentialsResult',
    'AwaitableGetDbCredentialsResult',
    'get_db_credentials',
    'get_db_credentials_output',
]

@pulumi.output_type
class GetDbCredentialsResult:
    """
    A collection of values returned by getDbCredentials.
    """
    def __init__(__self__, db_credentials=None, filters=None, id=None, name=None, state=None, user_id=None):
        if db_credentials and not isinstance(db_credentials, list):
            raise TypeError("Expected argument 'db_credentials' to be a list")
        pulumi.set(__self__, "db_credentials", db_credentials)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if user_id and not isinstance(user_id, str):
            raise TypeError("Expected argument 'user_id' to be a str")
        pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter(name="dbCredentials")
    def db_credentials(self) -> Sequence['outputs.GetDbCredentialsDbCredentialResult']:
        """
        The list of db_credentials.
        """
        return pulumi.get(self, "db_credentials")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetDbCredentialsFilterResult']]:
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
    def state(self) -> Optional[str]:
        """
        The credential's current state. After creating a DB credential, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> str:
        """
        The OCID of the user the DB credential belongs to.
        """
        return pulumi.get(self, "user_id")


class AwaitableGetDbCredentialsResult(GetDbCredentialsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDbCredentialsResult(
            db_credentials=self.db_credentials,
            filters=self.filters,
            id=self.id,
            name=self.name,
            state=self.state,
            user_id=self.user_id)


def get_db_credentials(filters: Optional[Sequence[pulumi.InputType['GetDbCredentialsFilterArgs']]] = None,
                       name: Optional[str] = None,
                       state: Optional[str] = None,
                       user_id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDbCredentialsResult:
    """
    This data source provides the list of Db Credentials in Oracle Cloud Infrastructure Identity service.

    Lists the DB credentials for the specified user. The returned object contains the credential's OCID

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_db_credentials = oci.Identity.get_db_credentials(user_id=oci_identity_user["test_user"]["id"],
        name=var["db_credential_name"],
        state=var["db_credential_state"])
    ```


    :param str name: A filter to only return resources that match the given name exactly.
    :param str state: A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.
    :param str user_id: The OCID of the user.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['name'] = name
    __args__['state'] = state
    __args__['userId'] = user_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Identity/getDbCredentials:getDbCredentials', __args__, opts=opts, typ=GetDbCredentialsResult).value

    return AwaitableGetDbCredentialsResult(
        db_credentials=pulumi.get(__ret__, 'db_credentials'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        state=pulumi.get(__ret__, 'state'),
        user_id=pulumi.get(__ret__, 'user_id'))


@_utilities.lift_output_func(get_db_credentials)
def get_db_credentials_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDbCredentialsFilterArgs']]]]] = None,
                              name: Optional[pulumi.Input[Optional[str]]] = None,
                              state: Optional[pulumi.Input[Optional[str]]] = None,
                              user_id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDbCredentialsResult]:
    """
    This data source provides the list of Db Credentials in Oracle Cloud Infrastructure Identity service.

    Lists the DB credentials for the specified user. The returned object contains the credential's OCID

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_db_credentials = oci.Identity.get_db_credentials(user_id=oci_identity_user["test_user"]["id"],
        name=var["db_credential_name"],
        state=var["db_credential_state"])
    ```


    :param str name: A filter to only return resources that match the given name exactly.
    :param str state: A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.
    :param str user_id: The OCID of the user.
    """
    ...
