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
    'GetFunctionsResult',
    'AwaitableGetFunctionsResult',
    'get_functions',
    'get_functions_output',
]

@pulumi.output_type
class GetFunctionsResult:
    """
    A collection of values returned by getFunctions.
    """
    def __init__(__self__, application_id=None, display_name=None, filters=None, functions=None, id=None, state=None):
        if application_id and not isinstance(application_id, str):
            raise TypeError("Expected argument 'application_id' to be a str")
        pulumi.set(__self__, "application_id", application_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if functions and not isinstance(functions, list):
            raise TypeError("Expected argument 'functions' to be a list")
        pulumi.set(__self__, "functions", functions)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> str:
        """
        The OCID of the application the function belongs to.
        """
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The display name of the function. The display name is unique within the application containing the function.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetFunctionsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def functions(self) -> Sequence['outputs.GetFunctionsFunctionResult']:
        """
        The list of functions.
        """
        return pulumi.get(self, "functions")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the function.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the function.
        """
        return pulumi.get(self, "state")


class AwaitableGetFunctionsResult(GetFunctionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFunctionsResult(
            application_id=self.application_id,
            display_name=self.display_name,
            filters=self.filters,
            functions=self.functions,
            id=self.id,
            state=self.state)


def get_functions(application_id: Optional[str] = None,
                  display_name: Optional[str] = None,
                  filters: Optional[Sequence[pulumi.InputType['GetFunctionsFilterArgs']]] = None,
                  id: Optional[str] = None,
                  state: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFunctionsResult:
    """
    This data source provides the list of Functions in Oracle Cloud Infrastructure Functions service.

    Lists functions for an application.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_functions = oci.Functions.get_functions(application_id=oci_functions_application["test_application"]["id"],
        display_name=var["function_display_name"],
        id=var["function_id"],
        state=var["function_state"])
    ```


    :param str application_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the application to which this function belongs.
    :param str display_name: A filter to return only functions with display names that match the display name string. Matching is exact.
    :param str id: A filter to return only functions with the specified OCID.
    :param str state: A filter to return only functions that match the lifecycle state in this parameter. Example: `Creating`
    """
    __args__ = dict()
    __args__['applicationId'] = application_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Functions/getFunctions:getFunctions', __args__, opts=opts, typ=GetFunctionsResult).value

    return AwaitableGetFunctionsResult(
        application_id=pulumi.get(__ret__, 'application_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        functions=pulumi.get(__ret__, 'functions'),
        id=pulumi.get(__ret__, 'id'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_functions)
def get_functions_output(application_id: Optional[pulumi.Input[str]] = None,
                         display_name: Optional[pulumi.Input[Optional[str]]] = None,
                         filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetFunctionsFilterArgs']]]]] = None,
                         id: Optional[pulumi.Input[Optional[str]]] = None,
                         state: Optional[pulumi.Input[Optional[str]]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFunctionsResult]:
    """
    This data source provides the list of Functions in Oracle Cloud Infrastructure Functions service.

    Lists functions for an application.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_functions = oci.Functions.get_functions(application_id=oci_functions_application["test_application"]["id"],
        display_name=var["function_display_name"],
        id=var["function_id"],
        state=var["function_state"])
    ```


    :param str application_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the application to which this function belongs.
    :param str display_name: A filter to return only functions with display names that match the display name string. Matching is exact.
    :param str id: A filter to return only functions with the specified OCID.
    :param str state: A filter to return only functions that match the lifecycle state in this parameter. Example: `Creating`
    """
    ...
