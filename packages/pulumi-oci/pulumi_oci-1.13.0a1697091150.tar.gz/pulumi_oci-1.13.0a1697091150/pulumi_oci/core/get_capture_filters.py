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
    'GetCaptureFiltersResult',
    'AwaitableGetCaptureFiltersResult',
    'get_capture_filters',
    'get_capture_filters_output',
]

@pulumi.output_type
class GetCaptureFiltersResult:
    """
    A collection of values returned by getCaptureFilters.
    """
    def __init__(__self__, capture_filters=None, compartment_id=None, display_name=None, filters=None, id=None, state=None):
        if capture_filters and not isinstance(capture_filters, list):
            raise TypeError("Expected argument 'capture_filters' to be a list")
        pulumi.set(__self__, "capture_filters", capture_filters)
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
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="captureFilters")
    def capture_filters(self) -> Sequence['outputs.GetCaptureFiltersCaptureFilterResult']:
        """
        The list of capture_filters.
        """
        return pulumi.get(self, "capture_filters")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the capture filter.
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
    def filters(self) -> Optional[Sequence['outputs.GetCaptureFiltersFilterResult']]:
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
        The capture filter's current administrative state.
        """
        return pulumi.get(self, "state")


class AwaitableGetCaptureFiltersResult(GetCaptureFiltersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCaptureFiltersResult(
            capture_filters=self.capture_filters,
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            state=self.state)


def get_capture_filters(compartment_id: Optional[str] = None,
                        display_name: Optional[str] = None,
                        filters: Optional[Sequence[pulumi.InputType['GetCaptureFiltersFilterArgs']]] = None,
                        state: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCaptureFiltersResult:
    """
    This data source provides the list of Capture Filters in Oracle Cloud Infrastructure Core service.

    Lists the capture filters in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_capture_filters = oci.Core.get_capture_filters(compartment_id=var["compartment_id"],
        display_name=var["capture_filter_display_name"],
        state=var["capture_filter_state"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A filter to return only resources that match the given display name exactly.
    :param str state: A filter to return only resources that match the given capture filter lifecycle state. The state value is case-insensitive.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Core/getCaptureFilters:getCaptureFilters', __args__, opts=opts, typ=GetCaptureFiltersResult).value

    return AwaitableGetCaptureFiltersResult(
        capture_filters=pulumi.get(__ret__, 'capture_filters'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_capture_filters)
def get_capture_filters_output(compartment_id: Optional[pulumi.Input[str]] = None,
                               display_name: Optional[pulumi.Input[Optional[str]]] = None,
                               filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetCaptureFiltersFilterArgs']]]]] = None,
                               state: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCaptureFiltersResult]:
    """
    This data source provides the list of Capture Filters in Oracle Cloud Infrastructure Core service.

    Lists the capture filters in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_capture_filters = oci.Core.get_capture_filters(compartment_id=var["compartment_id"],
        display_name=var["capture_filter_display_name"],
        state=var["capture_filter_state"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A filter to return only resources that match the given display name exactly.
    :param str state: A filter to return only resources that match the given capture filter lifecycle state. The state value is case-insensitive.
    """
    ...
