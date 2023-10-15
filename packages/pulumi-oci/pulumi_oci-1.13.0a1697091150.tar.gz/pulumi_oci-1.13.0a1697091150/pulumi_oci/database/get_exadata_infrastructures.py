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
    'GetExadataInfrastructuresResult',
    'AwaitableGetExadataInfrastructuresResult',
    'get_exadata_infrastructures',
    'get_exadata_infrastructures_output',
]

@pulumi.output_type
class GetExadataInfrastructuresResult:
    """
    A collection of values returned by getExadataInfrastructures.
    """
    def __init__(__self__, compartment_id=None, display_name=None, exadata_infrastructures=None, filters=None, id=None, state=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if exadata_infrastructures and not isinstance(exadata_infrastructures, list):
            raise TypeError("Expected argument 'exadata_infrastructures' to be a list")
        pulumi.set(__self__, "exadata_infrastructures", exadata_infrastructures)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The user-friendly name for the Exadata Cloud@Customer infrastructure. The name does not need to be unique.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="exadataInfrastructures")
    def exadata_infrastructures(self) -> Sequence['outputs.GetExadataInfrastructuresExadataInfrastructureResult']:
        """
        The list of exadata_infrastructures.
        """
        return pulumi.get(self, "exadata_infrastructures")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetExadataInfrastructuresFilterResult']]:
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
    def state(self) -> Optional[str]:
        """
        The current lifecycle state of the Exadata infrastructure.
        """
        return pulumi.get(self, "state")


class AwaitableGetExadataInfrastructuresResult(GetExadataInfrastructuresResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExadataInfrastructuresResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            exadata_infrastructures=self.exadata_infrastructures,
            filters=self.filters,
            id=self.id,
            state=self.state)


def get_exadata_infrastructures(compartment_id: Optional[str] = None,
                                display_name: Optional[str] = None,
                                filters: Optional[Sequence[pulumi.InputType['GetExadataInfrastructuresFilterArgs']]] = None,
                                state: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExadataInfrastructuresResult:
    """
    This data source provides the list of Exadata Infrastructures in Oracle Cloud Infrastructure Database service.

    Lists the Exadata infrastructure resources in the specified compartment. Applies to Exadata Cloud@Customer instances only.
    To list the Exadata Cloud Service infrastructure resources in a compartment, use the  [ListCloudExadataInfrastructures](https://docs.cloud.oracle.com/iaas/api/#/en/database/latest/CloudExadataInfrastructure/ListCloudExadataInfrastructures) operation.


    :param str compartment_id: The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str display_name: A filter to return only resources that match the entire display name given. The match is not case sensitive.
    :param str state: A filter to return only resources that match the given lifecycle state exactly.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Database/getExadataInfrastructures:getExadataInfrastructures', __args__, opts=opts, typ=GetExadataInfrastructuresResult).value

    return AwaitableGetExadataInfrastructuresResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        exadata_infrastructures=pulumi.get(__ret__, 'exadata_infrastructures'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_exadata_infrastructures)
def get_exadata_infrastructures_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                       display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                       filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetExadataInfrastructuresFilterArgs']]]]] = None,
                                       state: Optional[pulumi.Input[Optional[str]]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExadataInfrastructuresResult]:
    """
    This data source provides the list of Exadata Infrastructures in Oracle Cloud Infrastructure Database service.

    Lists the Exadata infrastructure resources in the specified compartment. Applies to Exadata Cloud@Customer instances only.
    To list the Exadata Cloud Service infrastructure resources in a compartment, use the  [ListCloudExadataInfrastructures](https://docs.cloud.oracle.com/iaas/api/#/en/database/latest/CloudExadataInfrastructure/ListCloudExadataInfrastructures) operation.


    :param str compartment_id: The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str display_name: A filter to return only resources that match the entire display name given. The match is not case sensitive.
    :param str state: A filter to return only resources that match the given lifecycle state exactly.
    """
    ...
