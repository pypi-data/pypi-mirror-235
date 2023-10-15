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
    'GetInvokeRunsResult',
    'AwaitableGetInvokeRunsResult',
    'get_invoke_runs',
    'get_invoke_runs_output',
]

@pulumi.output_type
class GetInvokeRunsResult:
    """
    A collection of values returned by getInvokeRuns.
    """
    def __init__(__self__, application_id=None, compartment_id=None, display_name=None, display_name_starts_with=None, filters=None, id=None, owner_principal_id=None, pool_id=None, runs=None, state=None, time_created_greater_than=None):
        if application_id and not isinstance(application_id, str):
            raise TypeError("Expected argument 'application_id' to be a str")
        pulumi.set(__self__, "application_id", application_id)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if display_name_starts_with and not isinstance(display_name_starts_with, str):
            raise TypeError("Expected argument 'display_name_starts_with' to be a str")
        pulumi.set(__self__, "display_name_starts_with", display_name_starts_with)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if owner_principal_id and not isinstance(owner_principal_id, str):
            raise TypeError("Expected argument 'owner_principal_id' to be a str")
        pulumi.set(__self__, "owner_principal_id", owner_principal_id)
        if pool_id and not isinstance(pool_id, str):
            raise TypeError("Expected argument 'pool_id' to be a str")
        pulumi.set(__self__, "pool_id", pool_id)
        if runs and not isinstance(runs, list):
            raise TypeError("Expected argument 'runs' to be a list")
        pulumi.set(__self__, "runs", runs)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if time_created_greater_than and not isinstance(time_created_greater_than, str):
            raise TypeError("Expected argument 'time_created_greater_than' to be a str")
        pulumi.set(__self__, "time_created_greater_than", time_created_greater_than)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[str]:
        """
        The application ID.
        """
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of a compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A user-friendly name. This name is not necessarily unique.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="displayNameStartsWith")
    def display_name_starts_with(self) -> Optional[str]:
        return pulumi.get(self, "display_name_starts_with")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetInvokeRunsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ownerPrincipalId")
    def owner_principal_id(self) -> Optional[str]:
        """
        The OCID of the user who created the resource.
        """
        return pulumi.get(self, "owner_principal_id")

    @property
    @pulumi.getter(name="poolId")
    def pool_id(self) -> Optional[str]:
        """
        The OCID of a pool. Unique Id to indentify a dataflow pool resource.
        """
        return pulumi.get(self, "pool_id")

    @property
    @pulumi.getter
    def runs(self) -> Sequence['outputs.GetInvokeRunsRunResult']:
        """
        The list of runs.
        """
        return pulumi.get(self, "runs")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of this run.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreatedGreaterThan")
    def time_created_greater_than(self) -> Optional[str]:
        return pulumi.get(self, "time_created_greater_than")


class AwaitableGetInvokeRunsResult(GetInvokeRunsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInvokeRunsResult(
            application_id=self.application_id,
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            display_name_starts_with=self.display_name_starts_with,
            filters=self.filters,
            id=self.id,
            owner_principal_id=self.owner_principal_id,
            pool_id=self.pool_id,
            runs=self.runs,
            state=self.state,
            time_created_greater_than=self.time_created_greater_than)


def get_invoke_runs(application_id: Optional[str] = None,
                    compartment_id: Optional[str] = None,
                    display_name: Optional[str] = None,
                    display_name_starts_with: Optional[str] = None,
                    filters: Optional[Sequence[pulumi.InputType['GetInvokeRunsFilterArgs']]] = None,
                    owner_principal_id: Optional[str] = None,
                    pool_id: Optional[str] = None,
                    state: Optional[str] = None,
                    time_created_greater_than: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInvokeRunsResult:
    """
    This data source provides the list of Invoke Runs in Oracle Cloud Infrastructure Data Flow service.

    Lists all runs of an application in the specified compartment.  Only one parameter other than compartmentId may also be included in a query. The query must include compartmentId. If the query does not include compartmentId, or includes compartmentId but two or more other parameters an error is returned.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_invoke_runs = oci.DataFlow.get_invoke_runs(compartment_id=var["compartment_id"],
        application_id=oci_dataflow_application["test_application"]["id"],
        display_name=var["invoke_run_display_name"],
        display_name_starts_with=var["invoke_run_display_name_starts_with"],
        owner_principal_id=oci_dataflow_owner_principal["test_owner_principal"]["id"],
        pool_id=oci_dataflow_pool["test_pool"]["id"],
        state=var["invoke_run_state"],
        time_created_greater_than=var["invoke_run_time_created_greater_than"])
    ```


    :param str application_id: The ID of the application.
    :param str compartment_id: The OCID of the compartment.
    :param str display_name: The query parameter for the Spark application name.
    :param str display_name_starts_with: The displayName prefix.
    :param str owner_principal_id: The OCID of the user who created the resource.
    :param str pool_id: The ID of the pool.
    :param str state: The LifecycleState of the run.
    :param str time_created_greater_than: The epoch time that the resource was created.
    """
    __args__ = dict()
    __args__['applicationId'] = application_id
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['displayNameStartsWith'] = display_name_starts_with
    __args__['filters'] = filters
    __args__['ownerPrincipalId'] = owner_principal_id
    __args__['poolId'] = pool_id
    __args__['state'] = state
    __args__['timeCreatedGreaterThan'] = time_created_greater_than
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataFlow/getInvokeRuns:getInvokeRuns', __args__, opts=opts, typ=GetInvokeRunsResult).value

    return AwaitableGetInvokeRunsResult(
        application_id=pulumi.get(__ret__, 'application_id'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        display_name_starts_with=pulumi.get(__ret__, 'display_name_starts_with'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        owner_principal_id=pulumi.get(__ret__, 'owner_principal_id'),
        pool_id=pulumi.get(__ret__, 'pool_id'),
        runs=pulumi.get(__ret__, 'runs'),
        state=pulumi.get(__ret__, 'state'),
        time_created_greater_than=pulumi.get(__ret__, 'time_created_greater_than'))


@_utilities.lift_output_func(get_invoke_runs)
def get_invoke_runs_output(application_id: Optional[pulumi.Input[Optional[str]]] = None,
                           compartment_id: Optional[pulumi.Input[str]] = None,
                           display_name: Optional[pulumi.Input[Optional[str]]] = None,
                           display_name_starts_with: Optional[pulumi.Input[Optional[str]]] = None,
                           filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetInvokeRunsFilterArgs']]]]] = None,
                           owner_principal_id: Optional[pulumi.Input[Optional[str]]] = None,
                           pool_id: Optional[pulumi.Input[Optional[str]]] = None,
                           state: Optional[pulumi.Input[Optional[str]]] = None,
                           time_created_greater_than: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInvokeRunsResult]:
    """
    This data source provides the list of Invoke Runs in Oracle Cloud Infrastructure Data Flow service.

    Lists all runs of an application in the specified compartment.  Only one parameter other than compartmentId may also be included in a query. The query must include compartmentId. If the query does not include compartmentId, or includes compartmentId but two or more other parameters an error is returned.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_invoke_runs = oci.DataFlow.get_invoke_runs(compartment_id=var["compartment_id"],
        application_id=oci_dataflow_application["test_application"]["id"],
        display_name=var["invoke_run_display_name"],
        display_name_starts_with=var["invoke_run_display_name_starts_with"],
        owner_principal_id=oci_dataflow_owner_principal["test_owner_principal"]["id"],
        pool_id=oci_dataflow_pool["test_pool"]["id"],
        state=var["invoke_run_state"],
        time_created_greater_than=var["invoke_run_time_created_greater_than"])
    ```


    :param str application_id: The ID of the application.
    :param str compartment_id: The OCID of the compartment.
    :param str display_name: The query parameter for the Spark application name.
    :param str display_name_starts_with: The displayName prefix.
    :param str owner_principal_id: The OCID of the user who created the resource.
    :param str pool_id: The ID of the pool.
    :param str state: The LifecycleState of the run.
    :param str time_created_greater_than: The epoch time that the resource was created.
    """
    ...
