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
    'GetTsigKeysResult',
    'AwaitableGetTsigKeysResult',
    'get_tsig_keys',
    'get_tsig_keys_output',
]

@pulumi.output_type
class GetTsigKeysResult:
    """
    A collection of values returned by getTsigKeys.
    """
    def __init__(__self__, compartment_id=None, filters=None, id=None, name=None, state=None, tsig_keys=None):
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
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tsig_keys and not isinstance(tsig_keys, list):
            raise TypeError("Expected argument 'tsig_keys' to be a list")
        pulumi.set(__self__, "tsig_keys", tsig_keys)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment containing the TSIG key.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetTsigKeysFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The OCID of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        A globally unique domain name identifying the key for a given pair of hosts.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the resource.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="tsigKeys")
    def tsig_keys(self) -> Sequence['outputs.GetTsigKeysTsigKeyResult']:
        """
        The list of tsig_keys.
        """
        return pulumi.get(self, "tsig_keys")


class AwaitableGetTsigKeysResult(GetTsigKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTsigKeysResult(
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            name=self.name,
            state=self.state,
            tsig_keys=self.tsig_keys)


def get_tsig_keys(compartment_id: Optional[str] = None,
                  filters: Optional[Sequence[pulumi.InputType['GetTsigKeysFilterArgs']]] = None,
                  id: Optional[str] = None,
                  name: Optional[str] = None,
                  state: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTsigKeysResult:
    """
    This data source provides the list of Tsig Keys in Oracle Cloud Infrastructure DNS service.

    Gets a list of all TSIG keys in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_tsig_keys = oci.Dns.get_tsig_keys(compartment_id=var["compartment_id"],
        id=var["tsig_key_id"],
        name=var["tsig_key_name"],
        state=var["tsig_key_state"])
    ```


    :param str compartment_id: The OCID of the compartment the resource belongs to.
    :param str id: The OCID of a resource.
    :param str name: The name of a resource.
    :param str state: The state of a resource.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['name'] = name
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Dns/getTsigKeys:getTsigKeys', __args__, opts=opts, typ=GetTsigKeysResult).value

    return AwaitableGetTsigKeysResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        state=pulumi.get(__ret__, 'state'),
        tsig_keys=pulumi.get(__ret__, 'tsig_keys'))


@_utilities.lift_output_func(get_tsig_keys)
def get_tsig_keys_output(compartment_id: Optional[pulumi.Input[str]] = None,
                         filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetTsigKeysFilterArgs']]]]] = None,
                         id: Optional[pulumi.Input[Optional[str]]] = None,
                         name: Optional[pulumi.Input[Optional[str]]] = None,
                         state: Optional[pulumi.Input[Optional[str]]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTsigKeysResult]:
    """
    This data source provides the list of Tsig Keys in Oracle Cloud Infrastructure DNS service.

    Gets a list of all TSIG keys in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_tsig_keys = oci.Dns.get_tsig_keys(compartment_id=var["compartment_id"],
        id=var["tsig_key_id"],
        name=var["tsig_key_name"],
        state=var["tsig_key_state"])
    ```


    :param str compartment_id: The OCID of the compartment the resource belongs to.
    :param str id: The OCID of a resource.
    :param str name: The name of a resource.
    :param str state: The state of a resource.
    """
    ...
