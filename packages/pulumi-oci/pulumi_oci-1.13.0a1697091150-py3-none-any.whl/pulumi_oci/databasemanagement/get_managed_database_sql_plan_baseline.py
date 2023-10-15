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
    'GetManagedDatabaseSqlPlanBaselineResult',
    'AwaitableGetManagedDatabaseSqlPlanBaselineResult',
    'get_managed_database_sql_plan_baseline',
    'get_managed_database_sql_plan_baseline_output',
]

@pulumi.output_type
class GetManagedDatabaseSqlPlanBaselineResult:
    """
    A collection of values returned by getManagedDatabaseSqlPlanBaseline.
    """
    def __init__(__self__, accepted=None, action=None, adaptive=None, auto_purge=None, enabled=None, execution_plan=None, fixed=None, id=None, managed_database_id=None, module=None, origin=None, plan_name=None, reproduced=None, sql_handle=None, sql_text=None, time_created=None, time_last_executed=None, time_last_modified=None):
        if accepted and not isinstance(accepted, str):
            raise TypeError("Expected argument 'accepted' to be a str")
        pulumi.set(__self__, "accepted", accepted)
        if action and not isinstance(action, str):
            raise TypeError("Expected argument 'action' to be a str")
        pulumi.set(__self__, "action", action)
        if adaptive and not isinstance(adaptive, str):
            raise TypeError("Expected argument 'adaptive' to be a str")
        pulumi.set(__self__, "adaptive", adaptive)
        if auto_purge and not isinstance(auto_purge, str):
            raise TypeError("Expected argument 'auto_purge' to be a str")
        pulumi.set(__self__, "auto_purge", auto_purge)
        if enabled and not isinstance(enabled, str):
            raise TypeError("Expected argument 'enabled' to be a str")
        pulumi.set(__self__, "enabled", enabled)
        if execution_plan and not isinstance(execution_plan, str):
            raise TypeError("Expected argument 'execution_plan' to be a str")
        pulumi.set(__self__, "execution_plan", execution_plan)
        if fixed and not isinstance(fixed, str):
            raise TypeError("Expected argument 'fixed' to be a str")
        pulumi.set(__self__, "fixed", fixed)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if managed_database_id and not isinstance(managed_database_id, str):
            raise TypeError("Expected argument 'managed_database_id' to be a str")
        pulumi.set(__self__, "managed_database_id", managed_database_id)
        if module and not isinstance(module, str):
            raise TypeError("Expected argument 'module' to be a str")
        pulumi.set(__self__, "module", module)
        if origin and not isinstance(origin, str):
            raise TypeError("Expected argument 'origin' to be a str")
        pulumi.set(__self__, "origin", origin)
        if plan_name and not isinstance(plan_name, str):
            raise TypeError("Expected argument 'plan_name' to be a str")
        pulumi.set(__self__, "plan_name", plan_name)
        if reproduced and not isinstance(reproduced, str):
            raise TypeError("Expected argument 'reproduced' to be a str")
        pulumi.set(__self__, "reproduced", reproduced)
        if sql_handle and not isinstance(sql_handle, str):
            raise TypeError("Expected argument 'sql_handle' to be a str")
        pulumi.set(__self__, "sql_handle", sql_handle)
        if sql_text and not isinstance(sql_text, str):
            raise TypeError("Expected argument 'sql_text' to be a str")
        pulumi.set(__self__, "sql_text", sql_text)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_last_executed and not isinstance(time_last_executed, str):
            raise TypeError("Expected argument 'time_last_executed' to be a str")
        pulumi.set(__self__, "time_last_executed", time_last_executed)
        if time_last_modified and not isinstance(time_last_modified, str):
            raise TypeError("Expected argument 'time_last_modified' to be a str")
        pulumi.set(__self__, "time_last_modified", time_last_modified)

    @property
    @pulumi.getter
    def accepted(self) -> str:
        """
        Indicates whether the plan baseline is accepted (`YES`) or not (`NO`).
        """
        return pulumi.get(self, "accepted")

    @property
    @pulumi.getter
    def action(self) -> str:
        """
        The application action.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def adaptive(self) -> str:
        """
        Indicates whether a plan that is automatically captured by SQL plan management is marked adaptive or not.
        """
        return pulumi.get(self, "adaptive")

    @property
    @pulumi.getter(name="autoPurge")
    def auto_purge(self) -> str:
        """
        Indicates whether the plan baseline is auto-purged (`YES`) or not (`NO`).
        """
        return pulumi.get(self, "auto_purge")

    @property
    @pulumi.getter
    def enabled(self) -> str:
        """
        Indicates whether the plan baseline is enabled (`YES`) or disabled (`NO`).
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="executionPlan")
    def execution_plan(self) -> str:
        """
        The execution plan for the SQL statement.
        """
        return pulumi.get(self, "execution_plan")

    @property
    @pulumi.getter
    def fixed(self) -> str:
        """
        Indicates whether the plan baseline is fixed (`YES`) or not (`NO`).
        """
        return pulumi.get(self, "fixed")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="managedDatabaseId")
    def managed_database_id(self) -> str:
        return pulumi.get(self, "managed_database_id")

    @property
    @pulumi.getter
    def module(self) -> str:
        """
        The application module name.
        """
        return pulumi.get(self, "module")

    @property
    @pulumi.getter
    def origin(self) -> str:
        """
        The origin of the SQL plan baseline.
        """
        return pulumi.get(self, "origin")

    @property
    @pulumi.getter(name="planName")
    def plan_name(self) -> str:
        """
        The unique plan identifier.
        """
        return pulumi.get(self, "plan_name")

    @property
    @pulumi.getter
    def reproduced(self) -> str:
        """
        Indicates whether the optimizer was able to reproduce the plan (`YES`) or not (`NO`). The value is set to `YES` when a plan is initially added to the plan baseline.
        """
        return pulumi.get(self, "reproduced")

    @property
    @pulumi.getter(name="sqlHandle")
    def sql_handle(self) -> str:
        """
        The unique SQL identifier.
        """
        return pulumi.get(self, "sql_handle")

    @property
    @pulumi.getter(name="sqlText")
    def sql_text(self) -> str:
        """
        The SQL text.
        """
        return pulumi.get(self, "sql_text")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time when the plan baseline was created.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeLastExecuted")
    def time_last_executed(self) -> str:
        """
        The date and time when the plan baseline was last executed.
        """
        return pulumi.get(self, "time_last_executed")

    @property
    @pulumi.getter(name="timeLastModified")
    def time_last_modified(self) -> str:
        """
        The date and time when the plan baseline was last modified.
        """
        return pulumi.get(self, "time_last_modified")


class AwaitableGetManagedDatabaseSqlPlanBaselineResult(GetManagedDatabaseSqlPlanBaselineResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedDatabaseSqlPlanBaselineResult(
            accepted=self.accepted,
            action=self.action,
            adaptive=self.adaptive,
            auto_purge=self.auto_purge,
            enabled=self.enabled,
            execution_plan=self.execution_plan,
            fixed=self.fixed,
            id=self.id,
            managed_database_id=self.managed_database_id,
            module=self.module,
            origin=self.origin,
            plan_name=self.plan_name,
            reproduced=self.reproduced,
            sql_handle=self.sql_handle,
            sql_text=self.sql_text,
            time_created=self.time_created,
            time_last_executed=self.time_last_executed,
            time_last_modified=self.time_last_modified)


def get_managed_database_sql_plan_baseline(managed_database_id: Optional[str] = None,
                                           plan_name: Optional[str] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedDatabaseSqlPlanBaselineResult:
    """
    This data source provides details about a specific Managed Database Sql Plan Baseline resource in Oracle Cloud Infrastructure Database Management service.

    Gets the SQL plan baseline details for the specified planName.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_database_sql_plan_baseline = oci.DatabaseManagement.get_managed_database_sql_plan_baseline(managed_database_id=oci_database_management_managed_database["test_managed_database"]["id"],
        plan_name=var["managed_database_sql_plan_baseline_plan_name"])
    ```


    :param str managed_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
    :param str plan_name: The plan name of the SQL plan baseline.
    """
    __args__ = dict()
    __args__['managedDatabaseId'] = managed_database_id
    __args__['planName'] = plan_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseManagement/getManagedDatabaseSqlPlanBaseline:getManagedDatabaseSqlPlanBaseline', __args__, opts=opts, typ=GetManagedDatabaseSqlPlanBaselineResult).value

    return AwaitableGetManagedDatabaseSqlPlanBaselineResult(
        accepted=pulumi.get(__ret__, 'accepted'),
        action=pulumi.get(__ret__, 'action'),
        adaptive=pulumi.get(__ret__, 'adaptive'),
        auto_purge=pulumi.get(__ret__, 'auto_purge'),
        enabled=pulumi.get(__ret__, 'enabled'),
        execution_plan=pulumi.get(__ret__, 'execution_plan'),
        fixed=pulumi.get(__ret__, 'fixed'),
        id=pulumi.get(__ret__, 'id'),
        managed_database_id=pulumi.get(__ret__, 'managed_database_id'),
        module=pulumi.get(__ret__, 'module'),
        origin=pulumi.get(__ret__, 'origin'),
        plan_name=pulumi.get(__ret__, 'plan_name'),
        reproduced=pulumi.get(__ret__, 'reproduced'),
        sql_handle=pulumi.get(__ret__, 'sql_handle'),
        sql_text=pulumi.get(__ret__, 'sql_text'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_last_executed=pulumi.get(__ret__, 'time_last_executed'),
        time_last_modified=pulumi.get(__ret__, 'time_last_modified'))


@_utilities.lift_output_func(get_managed_database_sql_plan_baseline)
def get_managed_database_sql_plan_baseline_output(managed_database_id: Optional[pulumi.Input[str]] = None,
                                                  plan_name: Optional[pulumi.Input[str]] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedDatabaseSqlPlanBaselineResult]:
    """
    This data source provides details about a specific Managed Database Sql Plan Baseline resource in Oracle Cloud Infrastructure Database Management service.

    Gets the SQL plan baseline details for the specified planName.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_database_sql_plan_baseline = oci.DatabaseManagement.get_managed_database_sql_plan_baseline(managed_database_id=oci_database_management_managed_database["test_managed_database"]["id"],
        plan_name=var["managed_database_sql_plan_baseline_plan_name"])
    ```


    :param str managed_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
    :param str plan_name: The plan name of the SQL plan baseline.
    """
    ...
