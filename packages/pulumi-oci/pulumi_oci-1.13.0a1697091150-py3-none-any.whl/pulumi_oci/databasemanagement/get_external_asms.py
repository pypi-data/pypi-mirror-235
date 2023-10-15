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
    'GetExternalAsmsResult',
    'AwaitableGetExternalAsmsResult',
    'get_external_asms',
    'get_external_asms_output',
]

@pulumi.output_type
class GetExternalAsmsResult:
    """
    A collection of values returned by getExternalAsms.
    """
    def __init__(__self__, compartment_id=None, display_name=None, external_asm_collections=None, external_db_system_id=None, filters=None, id=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if external_asm_collections and not isinstance(external_asm_collections, list):
            raise TypeError("Expected argument 'external_asm_collections' to be a list")
        pulumi.set(__self__, "external_asm_collections", external_asm_collections)
        if external_db_system_id and not isinstance(external_db_system_id, str):
            raise TypeError("Expected argument 'external_db_system_id' to be a str")
        pulumi.set(__self__, "external_db_system_id", external_db_system_id)
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
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which the external database resides.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The user-friendly name for the database. The name does not have to be unique.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="externalAsmCollections")
    def external_asm_collections(self) -> Sequence['outputs.GetExternalAsmsExternalAsmCollectionResult']:
        """
        The list of external_asm_collection.
        """
        return pulumi.get(self, "external_asm_collections")

    @property
    @pulumi.getter(name="externalDbSystemId")
    def external_db_system_id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system that the ASM is a part of.
        """
        return pulumi.get(self, "external_db_system_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetExternalAsmsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetExternalAsmsResult(GetExternalAsmsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExternalAsmsResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            external_asm_collections=self.external_asm_collections,
            external_db_system_id=self.external_db_system_id,
            filters=self.filters,
            id=self.id)


def get_external_asms(compartment_id: Optional[str] = None,
                      display_name: Optional[str] = None,
                      external_db_system_id: Optional[str] = None,
                      filters: Optional[Sequence[pulumi.InputType['GetExternalAsmsFilterArgs']]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExternalAsmsResult:
    """
    This data source provides the list of External Asms in Oracle Cloud Infrastructure Database Management service.

    Lists the ASMs in the specified external DB system.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_external_asms = oci.DatabaseManagement.get_external_asms(compartment_id=var["compartment_id"],
        display_name=var["external_asm_display_name"],
        external_db_system_id=oci_database_management_external_db_system["test_external_db_system"]["id"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A filter to only return the resources that match the entire display name.
    :param str external_db_system_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['externalDbSystemId'] = external_db_system_id
    __args__['filters'] = filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseManagement/getExternalAsms:getExternalAsms', __args__, opts=opts, typ=GetExternalAsmsResult).value

    return AwaitableGetExternalAsmsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        external_asm_collections=pulumi.get(__ret__, 'external_asm_collections'),
        external_db_system_id=pulumi.get(__ret__, 'external_db_system_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_external_asms)
def get_external_asms_output(compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                             display_name: Optional[pulumi.Input[Optional[str]]] = None,
                             external_db_system_id: Optional[pulumi.Input[Optional[str]]] = None,
                             filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetExternalAsmsFilterArgs']]]]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExternalAsmsResult]:
    """
    This data source provides the list of External Asms in Oracle Cloud Infrastructure Database Management service.

    Lists the ASMs in the specified external DB system.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_external_asms = oci.DatabaseManagement.get_external_asms(compartment_id=var["compartment_id"],
        display_name=var["external_asm_display_name"],
        external_db_system_id=oci_database_management_external_db_system["test_external_db_system"]["id"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A filter to only return the resources that match the entire display name.
    :param str external_db_system_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system.
    """
    ...
