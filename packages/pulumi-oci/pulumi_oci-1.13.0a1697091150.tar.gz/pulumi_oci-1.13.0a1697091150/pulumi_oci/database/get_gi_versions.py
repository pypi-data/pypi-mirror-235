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
    'GetGiVersionsResult',
    'AwaitableGetGiVersionsResult',
    'get_gi_versions',
    'get_gi_versions_output',
]

@pulumi.output_type
class GetGiVersionsResult:
    """
    A collection of values returned by getGiVersions.
    """
    def __init__(__self__, compartment_id=None, filters=None, gi_versions=None, id=None, shape=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if gi_versions and not isinstance(gi_versions, list):
            raise TypeError("Expected argument 'gi_versions' to be a list")
        pulumi.set(__self__, "gi_versions", gi_versions)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if shape and not isinstance(shape, str):
            raise TypeError("Expected argument 'shape' to be a str")
        pulumi.set(__self__, "shape", shape)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetGiVersionsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter(name="giVersions")
    def gi_versions(self) -> Sequence['outputs.GetGiVersionsGiVersionResult']:
        """
        The list of gi_versions.
        """
        return pulumi.get(self, "gi_versions")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def shape(self) -> Optional[str]:
        return pulumi.get(self, "shape")


class AwaitableGetGiVersionsResult(GetGiVersionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGiVersionsResult(
            compartment_id=self.compartment_id,
            filters=self.filters,
            gi_versions=self.gi_versions,
            id=self.id,
            shape=self.shape)


def get_gi_versions(compartment_id: Optional[str] = None,
                    filters: Optional[Sequence[pulumi.InputType['GetGiVersionsFilterArgs']]] = None,
                    shape: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGiVersionsResult:
    """
    This data source provides the list of Gi Versions in Oracle Cloud Infrastructure Database service.

    Gets a list of supported GI versions for the Exadata Cloud@Customer VM cluster.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_gi_versions = oci.Database.get_gi_versions(compartment_id=var["compartment_id"],
        shape=var["gi_version_shape"])
    ```


    :param str compartment_id: The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str shape: If provided, filters the results for the given shape.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['shape'] = shape
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Database/getGiVersions:getGiVersions', __args__, opts=opts, typ=GetGiVersionsResult).value

    return AwaitableGetGiVersionsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        gi_versions=pulumi.get(__ret__, 'gi_versions'),
        id=pulumi.get(__ret__, 'id'),
        shape=pulumi.get(__ret__, 'shape'))


@_utilities.lift_output_func(get_gi_versions)
def get_gi_versions_output(compartment_id: Optional[pulumi.Input[str]] = None,
                           filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetGiVersionsFilterArgs']]]]] = None,
                           shape: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGiVersionsResult]:
    """
    This data source provides the list of Gi Versions in Oracle Cloud Infrastructure Database service.

    Gets a list of supported GI versions for the Exadata Cloud@Customer VM cluster.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_gi_versions = oci.Database.get_gi_versions(compartment_id=var["compartment_id"],
        shape=var["gi_version_shape"])
    ```


    :param str compartment_id: The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str shape: If provided, filters the results for the given shape.
    """
    ...
