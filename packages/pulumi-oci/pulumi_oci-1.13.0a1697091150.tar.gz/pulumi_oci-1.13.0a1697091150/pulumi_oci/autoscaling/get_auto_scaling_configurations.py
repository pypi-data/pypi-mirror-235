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
    'GetAutoScalingConfigurationsResult',
    'AwaitableGetAutoScalingConfigurationsResult',
    'get_auto_scaling_configurations',
    'get_auto_scaling_configurations_output',
]

@pulumi.output_type
class GetAutoScalingConfigurationsResult:
    """
    A collection of values returned by getAutoScalingConfigurations.
    """
    def __init__(__self__, auto_scaling_configurations=None, compartment_id=None, display_name=None, filters=None, id=None):
        if auto_scaling_configurations and not isinstance(auto_scaling_configurations, list):
            raise TypeError("Expected argument 'auto_scaling_configurations' to be a list")
        pulumi.set(__self__, "auto_scaling_configurations", auto_scaling_configurations)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="autoScalingConfigurations")
    def auto_scaling_configurations(self) -> Sequence['outputs.GetAutoScalingConfigurationsAutoScalingConfigurationResult']:
        """
        The list of auto_scaling_configurations.
        """
        return pulumi.get(self, "auto_scaling_configurations")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the autoscaling configuration.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetAutoScalingConfigurationsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetAutoScalingConfigurationsResult(GetAutoScalingConfigurationsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAutoScalingConfigurationsResult(
            auto_scaling_configurations=self.auto_scaling_configurations,
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id)


def get_auto_scaling_configurations(compartment_id: Optional[str] = None,
                                    display_name: Optional[str] = None,
                                    filters: Optional[Sequence[pulumi.InputType['GetAutoScalingConfigurationsFilterArgs']]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAutoScalingConfigurationsResult:
    """
    This data source provides the list of Auto Scaling Configurations in Oracle Cloud Infrastructure Auto Scaling service.

    Lists autoscaling configurations in the specifed compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_auto_scaling_configurations = oci.Autoscaling.get_auto_scaling_configurations(compartment_id=var["compartment_id"],
        display_name=var["auto_scaling_configuration_display_name"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the resources monitored by the metric that you are searching for. Use tenancyId to search in the root compartment.
    :param str display_name: A filter to return only resources that match the given display name exactly.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Autoscaling/getAutoScalingConfigurations:getAutoScalingConfigurations', __args__, opts=opts, typ=GetAutoScalingConfigurationsResult).value

    return AwaitableGetAutoScalingConfigurationsResult(
        auto_scaling_configurations=pulumi.get(__ret__, 'auto_scaling_configurations'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_auto_scaling_configurations)
def get_auto_scaling_configurations_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                           display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                           filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetAutoScalingConfigurationsFilterArgs']]]]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAutoScalingConfigurationsResult]:
    """
    This data source provides the list of Auto Scaling Configurations in Oracle Cloud Infrastructure Auto Scaling service.

    Lists autoscaling configurations in the specifed compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_auto_scaling_configurations = oci.Autoscaling.get_auto_scaling_configurations(compartment_id=var["compartment_id"],
        display_name=var["auto_scaling_configuration_display_name"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the resources monitored by the metric that you are searching for. Use tenancyId to search in the root compartment.
    :param str display_name: A filter to return only resources that match the given display name exactly.
    """
    ...
