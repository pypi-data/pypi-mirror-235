# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetOperationsInsightsWarehouseResourceUsageSummaryResult',
    'AwaitableGetOperationsInsightsWarehouseResourceUsageSummaryResult',
    'get_operations_insights_warehouse_resource_usage_summary',
    'get_operations_insights_warehouse_resource_usage_summary_output',
]

@pulumi.output_type
class GetOperationsInsightsWarehouseResourceUsageSummaryResult:
    """
    A collection of values returned by getOperationsInsightsWarehouseResourceUsageSummary.
    """
    def __init__(__self__, cpu_used=None, id=None, operations_insights_warehouse_id=None, state=None, storage_used_in_gbs=None):
        if cpu_used and not isinstance(cpu_used, float):
            raise TypeError("Expected argument 'cpu_used' to be a float")
        pulumi.set(__self__, "cpu_used", cpu_used)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if operations_insights_warehouse_id and not isinstance(operations_insights_warehouse_id, str):
            raise TypeError("Expected argument 'operations_insights_warehouse_id' to be a str")
        pulumi.set(__self__, "operations_insights_warehouse_id", operations_insights_warehouse_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if storage_used_in_gbs and not isinstance(storage_used_in_gbs, float):
            raise TypeError("Expected argument 'storage_used_in_gbs' to be a float")
        pulumi.set(__self__, "storage_used_in_gbs", storage_used_in_gbs)

    @property
    @pulumi.getter(name="cpuUsed")
    def cpu_used(self) -> float:
        """
        Number of OCPUs used by OPSI Warehouse ADW. Can be fractional.
        """
        return pulumi.get(self, "cpu_used")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="operationsInsightsWarehouseId")
    def operations_insights_warehouse_id(self) -> str:
        return pulumi.get(self, "operations_insights_warehouse_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        Possible lifecycle states
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="storageUsedInGbs")
    def storage_used_in_gbs(self) -> float:
        """
        Storage by OPSI Warehouse ADW in GB.
        """
        return pulumi.get(self, "storage_used_in_gbs")


class AwaitableGetOperationsInsightsWarehouseResourceUsageSummaryResult(GetOperationsInsightsWarehouseResourceUsageSummaryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOperationsInsightsWarehouseResourceUsageSummaryResult(
            cpu_used=self.cpu_used,
            id=self.id,
            operations_insights_warehouse_id=self.operations_insights_warehouse_id,
            state=self.state,
            storage_used_in_gbs=self.storage_used_in_gbs)


def get_operations_insights_warehouse_resource_usage_summary(operations_insights_warehouse_id: Optional[str] = None,
                                                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOperationsInsightsWarehouseResourceUsageSummaryResult:
    """
    This data source provides details about a specific Operations Insights Warehouse Resource Usage Summary resource in Oracle Cloud Infrastructure Opsi service.

    Gets the details of resources used by an Operations Insights Warehouse.
    There is only expected to be 1 warehouse per tenant. The warehouse is expected to be in the root compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_operations_insights_warehouse_resource_usage_summary = oci.Opsi.get_operations_insights_warehouse_resource_usage_summary(operations_insights_warehouse_id=oci_opsi_operations_insights_warehouse["test_operations_insights_warehouse"]["id"])
    ```


    :param str operations_insights_warehouse_id: Unique Operations Insights Warehouse identifier
    """
    __args__ = dict()
    __args__['operationsInsightsWarehouseId'] = operations_insights_warehouse_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Opsi/getOperationsInsightsWarehouseResourceUsageSummary:getOperationsInsightsWarehouseResourceUsageSummary', __args__, opts=opts, typ=GetOperationsInsightsWarehouseResourceUsageSummaryResult).value

    return AwaitableGetOperationsInsightsWarehouseResourceUsageSummaryResult(
        cpu_used=pulumi.get(__ret__, 'cpu_used'),
        id=pulumi.get(__ret__, 'id'),
        operations_insights_warehouse_id=pulumi.get(__ret__, 'operations_insights_warehouse_id'),
        state=pulumi.get(__ret__, 'state'),
        storage_used_in_gbs=pulumi.get(__ret__, 'storage_used_in_gbs'))


@_utilities.lift_output_func(get_operations_insights_warehouse_resource_usage_summary)
def get_operations_insights_warehouse_resource_usage_summary_output(operations_insights_warehouse_id: Optional[pulumi.Input[str]] = None,
                                                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOperationsInsightsWarehouseResourceUsageSummaryResult]:
    """
    This data source provides details about a specific Operations Insights Warehouse Resource Usage Summary resource in Oracle Cloud Infrastructure Opsi service.

    Gets the details of resources used by an Operations Insights Warehouse.
    There is only expected to be 1 warehouse per tenant. The warehouse is expected to be in the root compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_operations_insights_warehouse_resource_usage_summary = oci.Opsi.get_operations_insights_warehouse_resource_usage_summary(operations_insights_warehouse_id=oci_opsi_operations_insights_warehouse["test_operations_insights_warehouse"]["id"])
    ```


    :param str operations_insights_warehouse_id: Unique Operations Insights Warehouse identifier
    """
    ...
