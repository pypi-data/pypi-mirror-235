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
    'GetFusionEnvironmentTimeAvailableForRefreshResult',
    'AwaitableGetFusionEnvironmentTimeAvailableForRefreshResult',
    'get_fusion_environment_time_available_for_refresh',
    'get_fusion_environment_time_available_for_refresh_output',
]

@pulumi.output_type
class GetFusionEnvironmentTimeAvailableForRefreshResult:
    """
    A collection of values returned by getFusionEnvironmentTimeAvailableForRefresh.
    """
    def __init__(__self__, fusion_environment_id=None, id=None, items=None):
        if fusion_environment_id and not isinstance(fusion_environment_id, str):
            raise TypeError("Expected argument 'fusion_environment_id' to be a str")
        pulumi.set(__self__, "fusion_environment_id", fusion_environment_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if items and not isinstance(items, list):
            raise TypeError("Expected argument 'items' to be a list")
        pulumi.set(__self__, "items", items)

    @property
    @pulumi.getter(name="fusionEnvironmentId")
    def fusion_environment_id(self) -> str:
        return pulumi.get(self, "fusion_environment_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.GetFusionEnvironmentTimeAvailableForRefreshItemResult']:
        """
        A list of available refresh time objects.
        """
        return pulumi.get(self, "items")


class AwaitableGetFusionEnvironmentTimeAvailableForRefreshResult(GetFusionEnvironmentTimeAvailableForRefreshResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFusionEnvironmentTimeAvailableForRefreshResult(
            fusion_environment_id=self.fusion_environment_id,
            id=self.id,
            items=self.items)


def get_fusion_environment_time_available_for_refresh(fusion_environment_id: Optional[str] = None,
                                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFusionEnvironmentTimeAvailableForRefreshResult:
    """
    This data source provides details about a specific Fusion Environment Time Available For Refresh resource in Oracle Cloud Infrastructure Fusion Apps service.

    Gets available refresh time for this fusion environment

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_fusion_environment_time_available_for_refresh = oci.Functions.get_fusion_environment_time_available_for_refresh(fusion_environment_id=oci_fusion_apps_fusion_environment["test_fusion_environment"]["id"])
    ```


    :param str fusion_environment_id: unique FusionEnvironment identifier
    """
    __args__ = dict()
    __args__['fusionEnvironmentId'] = fusion_environment_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Functions/getFusionEnvironmentTimeAvailableForRefresh:getFusionEnvironmentTimeAvailableForRefresh', __args__, opts=opts, typ=GetFusionEnvironmentTimeAvailableForRefreshResult).value

    return AwaitableGetFusionEnvironmentTimeAvailableForRefreshResult(
        fusion_environment_id=pulumi.get(__ret__, 'fusion_environment_id'),
        id=pulumi.get(__ret__, 'id'),
        items=pulumi.get(__ret__, 'items'))


@_utilities.lift_output_func(get_fusion_environment_time_available_for_refresh)
def get_fusion_environment_time_available_for_refresh_output(fusion_environment_id: Optional[pulumi.Input[str]] = None,
                                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFusionEnvironmentTimeAvailableForRefreshResult]:
    """
    This data source provides details about a specific Fusion Environment Time Available For Refresh resource in Oracle Cloud Infrastructure Fusion Apps service.

    Gets available refresh time for this fusion environment

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_fusion_environment_time_available_for_refresh = oci.Functions.get_fusion_environment_time_available_for_refresh(fusion_environment_id=oci_fusion_apps_fusion_environment["test_fusion_environment"]["id"])
    ```


    :param str fusion_environment_id: unique FusionEnvironment identifier
    """
    ...
