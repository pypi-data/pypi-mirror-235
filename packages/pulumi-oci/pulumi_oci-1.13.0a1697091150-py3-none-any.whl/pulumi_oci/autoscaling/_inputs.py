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
    'AutoScalingConfigurationAutoScalingResourcesArgs',
    'AutoScalingConfigurationPolicyArgs',
    'AutoScalingConfigurationPolicyCapacityArgs',
    'AutoScalingConfigurationPolicyExecutionScheduleArgs',
    'AutoScalingConfigurationPolicyResourceActionArgs',
    'AutoScalingConfigurationPolicyRuleArgs',
    'AutoScalingConfigurationPolicyRuleActionArgs',
    'AutoScalingConfigurationPolicyRuleMetricArgs',
    'AutoScalingConfigurationPolicyRuleMetricThresholdArgs',
    'GetAutoScalingConfigurationsFilterArgs',
]

@pulumi.input_type
class AutoScalingConfigurationAutoScalingResourcesArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 type: pulumi.Input[str]):
        """
        :param pulumi.Input[str] id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that is managed by the autoscaling configuration.
        :param pulumi.Input[str] type: The type of action to take.
        """
        AutoScalingConfigurationAutoScalingResourcesArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            id=id,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             id: pulumi.Input[str],
             type: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("id", id)
        _setter("type", type)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that is managed by the autoscaling configuration.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of action to take.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class AutoScalingConfigurationPolicyArgs:
    def __init__(__self__, *,
                 policy_type: pulumi.Input[str],
                 capacity: Optional[pulumi.Input['AutoScalingConfigurationPolicyCapacityArgs']] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 execution_schedule: Optional[pulumi.Input['AutoScalingConfigurationPolicyExecutionScheduleArgs']] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 resource_action: Optional[pulumi.Input['AutoScalingConfigurationPolicyResourceActionArgs']] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['AutoScalingConfigurationPolicyRuleArgs']]]] = None,
                 time_created: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] policy_type: The type of autoscaling policy.
        :param pulumi.Input['AutoScalingConfigurationPolicyCapacityArgs'] capacity: The capacity requirements of the autoscaling policy.
        :param pulumi.Input['AutoScalingConfigurationPolicyExecutionScheduleArgs'] execution_schedule: An execution schedule for an autoscaling policy.
        :param pulumi.Input[str] id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that is managed by the autoscaling configuration.
        :param pulumi.Input[bool] is_enabled: Whether the autoscaling policy is enabled.
        :param pulumi.Input['AutoScalingConfigurationPolicyResourceActionArgs'] resource_action: An action that can be executed against a resource.
        :param pulumi.Input[str] time_created: The date and time the autoscaling configuration was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`
        """
        AutoScalingConfigurationPolicyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            policy_type=policy_type,
            capacity=capacity,
            display_name=display_name,
            execution_schedule=execution_schedule,
            id=id,
            is_enabled=is_enabled,
            resource_action=resource_action,
            rules=rules,
            time_created=time_created,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             policy_type: pulumi.Input[str],
             capacity: Optional[pulumi.Input['AutoScalingConfigurationPolicyCapacityArgs']] = None,
             display_name: Optional[pulumi.Input[str]] = None,
             execution_schedule: Optional[pulumi.Input['AutoScalingConfigurationPolicyExecutionScheduleArgs']] = None,
             id: Optional[pulumi.Input[str]] = None,
             is_enabled: Optional[pulumi.Input[bool]] = None,
             resource_action: Optional[pulumi.Input['AutoScalingConfigurationPolicyResourceActionArgs']] = None,
             rules: Optional[pulumi.Input[Sequence[pulumi.Input['AutoScalingConfigurationPolicyRuleArgs']]]] = None,
             time_created: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("policy_type", policy_type)
        if capacity is not None:
            _setter("capacity", capacity)
        if display_name is not None:
            _setter("display_name", display_name)
        if execution_schedule is not None:
            _setter("execution_schedule", execution_schedule)
        if id is not None:
            _setter("id", id)
        if is_enabled is not None:
            _setter("is_enabled", is_enabled)
        if resource_action is not None:
            _setter("resource_action", resource_action)
        if rules is not None:
            _setter("rules", rules)
        if time_created is not None:
            _setter("time_created", time_created)

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Input[str]:
        """
        The type of autoscaling policy.
        """
        return pulumi.get(self, "policy_type")

    @policy_type.setter
    def policy_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_type", value)

    @property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input['AutoScalingConfigurationPolicyCapacityArgs']]:
        """
        The capacity requirements of the autoscaling policy.
        """
        return pulumi.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input['AutoScalingConfigurationPolicyCapacityArgs']]):
        pulumi.set(self, "capacity", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="executionSchedule")
    def execution_schedule(self) -> Optional[pulumi.Input['AutoScalingConfigurationPolicyExecutionScheduleArgs']]:
        """
        An execution schedule for an autoscaling policy.
        """
        return pulumi.get(self, "execution_schedule")

    @execution_schedule.setter
    def execution_schedule(self, value: Optional[pulumi.Input['AutoScalingConfigurationPolicyExecutionScheduleArgs']]):
        pulumi.set(self, "execution_schedule", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that is managed by the autoscaling configuration.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the autoscaling policy is enabled.
        """
        return pulumi.get(self, "is_enabled")

    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_enabled", value)

    @property
    @pulumi.getter(name="resourceAction")
    def resource_action(self) -> Optional[pulumi.Input['AutoScalingConfigurationPolicyResourceActionArgs']]:
        """
        An action that can be executed against a resource.
        """
        return pulumi.get(self, "resource_action")

    @resource_action.setter
    def resource_action(self, value: Optional[pulumi.Input['AutoScalingConfigurationPolicyResourceActionArgs']]):
        pulumi.set(self, "resource_action", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AutoScalingConfigurationPolicyRuleArgs']]]]:
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AutoScalingConfigurationPolicyRuleArgs']]]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time the autoscaling configuration was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)


@pulumi.input_type
class AutoScalingConfigurationPolicyCapacityArgs:
    def __init__(__self__, *,
                 initial: Optional[pulumi.Input[int]] = None,
                 max: Optional[pulumi.Input[int]] = None,
                 min: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[int] initial: For a threshold-based autoscaling policy, this value is the initial number of instances to launch in the instance pool immediately after autoscaling is enabled. After autoscaling retrieves performance metrics, the number of instances is automatically adjusted from this initial number to a number that is based on the limits that you set.
               
               For a schedule-based autoscaling policy, this value is the target pool size to scale to when executing the schedule that's defined in the autoscaling policy.
        :param pulumi.Input[int] max: For a threshold-based autoscaling policy, this value is the maximum number of instances the instance pool is allowed to increase to (scale out).
               
               For a schedule-based autoscaling policy, this value is not used.
        :param pulumi.Input[int] min: For a threshold-based autoscaling policy, this value is the minimum number of instances the instance pool is allowed to decrease to (scale in).
               
               For a schedule-based autoscaling policy, this value is not used.
        """
        AutoScalingConfigurationPolicyCapacityArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            initial=initial,
            max=max,
            min=min,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             initial: Optional[pulumi.Input[int]] = None,
             max: Optional[pulumi.Input[int]] = None,
             min: Optional[pulumi.Input[int]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if initial is not None:
            _setter("initial", initial)
        if max is not None:
            _setter("max", max)
        if min is not None:
            _setter("min", min)

    @property
    @pulumi.getter
    def initial(self) -> Optional[pulumi.Input[int]]:
        """
        For a threshold-based autoscaling policy, this value is the initial number of instances to launch in the instance pool immediately after autoscaling is enabled. After autoscaling retrieves performance metrics, the number of instances is automatically adjusted from this initial number to a number that is based on the limits that you set.

        For a schedule-based autoscaling policy, this value is the target pool size to scale to when executing the schedule that's defined in the autoscaling policy.
        """
        return pulumi.get(self, "initial")

    @initial.setter
    def initial(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "initial", value)

    @property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[int]]:
        """
        For a threshold-based autoscaling policy, this value is the maximum number of instances the instance pool is allowed to increase to (scale out).

        For a schedule-based autoscaling policy, this value is not used.
        """
        return pulumi.get(self, "max")

    @max.setter
    def max(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max", value)

    @property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[int]]:
        """
        For a threshold-based autoscaling policy, this value is the minimum number of instances the instance pool is allowed to decrease to (scale in).

        For a schedule-based autoscaling policy, this value is not used.
        """
        return pulumi.get(self, "min")

    @min.setter
    def min(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min", value)


@pulumi.input_type
class AutoScalingConfigurationPolicyExecutionScheduleArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 timezone: pulumi.Input[str],
                 type: pulumi.Input[str]):
        """
        :param pulumi.Input[str] expression: A cron expression that represents the time at which to execute the autoscaling policy.
               
               Cron expressions have this format: `<second> <minute> <hour> <day of month> <month> <day of week> <year>`
               
               You can use special characters that are supported with the Quartz cron implementation.
               
               You must specify `0` as the value for seconds.
               
               Example: `0 15 10 ? * *`
        :param pulumi.Input[str] timezone: The time zone for the execution schedule.
        :param pulumi.Input[str] type: The type of action to take.
        """
        AutoScalingConfigurationPolicyExecutionScheduleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            expression=expression,
            timezone=timezone,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             expression: pulumi.Input[str],
             timezone: pulumi.Input[str],
             type: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("expression", expression)
        _setter("timezone", timezone)
        _setter("type", type)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        """
        A cron expression that represents the time at which to execute the autoscaling policy.

        Cron expressions have this format: `<second> <minute> <hour> <day of month> <month> <day of week> <year>`

        You can use special characters that are supported with the Quartz cron implementation.

        You must specify `0` as the value for seconds.

        Example: `0 15 10 ? * *`
        """
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def timezone(self) -> pulumi.Input[str]:
        """
        The time zone for the execution schedule.
        """
        return pulumi.get(self, "timezone")

    @timezone.setter
    def timezone(self, value: pulumi.Input[str]):
        pulumi.set(self, "timezone", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of action to take.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class AutoScalingConfigurationPolicyResourceActionArgs:
    def __init__(__self__, *,
                 action: pulumi.Input[str],
                 action_type: pulumi.Input[str]):
        """
        :param pulumi.Input[str] action: The action to take when autoscaling is triggered.
        :param pulumi.Input[str] action_type: The type of resource action.
        """
        AutoScalingConfigurationPolicyResourceActionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            action=action,
            action_type=action_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             action: pulumi.Input[str],
             action_type: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("action", action)
        _setter("action_type", action_type)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input[str]:
        """
        The action to take when autoscaling is triggered.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input[str]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter(name="actionType")
    def action_type(self) -> pulumi.Input[str]:
        """
        The type of resource action.
        """
        return pulumi.get(self, "action_type")

    @action_type.setter
    def action_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "action_type", value)


@pulumi.input_type
class AutoScalingConfigurationPolicyRuleArgs:
    def __init__(__self__, *,
                 display_name: pulumi.Input[str],
                 action: Optional[pulumi.Input['AutoScalingConfigurationPolicyRuleActionArgs']] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 metric: Optional[pulumi.Input['AutoScalingConfigurationPolicyRuleMetricArgs']] = None):
        """
        :param pulumi.Input['AutoScalingConfigurationPolicyRuleActionArgs'] action: The action to take when autoscaling is triggered.
        :param pulumi.Input[str] id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that is managed by the autoscaling configuration.
        :param pulumi.Input['AutoScalingConfigurationPolicyRuleMetricArgs'] metric: Metric and threshold details for triggering an autoscaling action.
        """
        AutoScalingConfigurationPolicyRuleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            display_name=display_name,
            action=action,
            id=id,
            metric=metric,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             display_name: pulumi.Input[str],
             action: Optional[pulumi.Input['AutoScalingConfigurationPolicyRuleActionArgs']] = None,
             id: Optional[pulumi.Input[str]] = None,
             metric: Optional[pulumi.Input['AutoScalingConfigurationPolicyRuleMetricArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("display_name", display_name)
        if action is not None:
            _setter("action", action)
        if id is not None:
            _setter("id", id)
        if metric is not None:
            _setter("metric", metric)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input['AutoScalingConfigurationPolicyRuleActionArgs']]:
        """
        The action to take when autoscaling is triggered.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input['AutoScalingConfigurationPolicyRuleActionArgs']]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that is managed by the autoscaling configuration.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def metric(self) -> Optional[pulumi.Input['AutoScalingConfigurationPolicyRuleMetricArgs']]:
        """
        Metric and threshold details for triggering an autoscaling action.
        """
        return pulumi.get(self, "metric")

    @metric.setter
    def metric(self, value: Optional[pulumi.Input['AutoScalingConfigurationPolicyRuleMetricArgs']]):
        pulumi.set(self, "metric", value)


@pulumi.input_type
class AutoScalingConfigurationPolicyRuleActionArgs:
    def __init__(__self__, *,
                 type: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[str] type: The type of action to take.
        :param pulumi.Input[int] value: ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        AutoScalingConfigurationPolicyRuleActionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            type=type,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             type: Optional[pulumi.Input[str]] = None,
             value: Optional[pulumi.Input[int]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if type is not None:
            _setter("type", type)
        if value is not None:
            _setter("value", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of action to take.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[int]]:
        """
        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class AutoScalingConfigurationPolicyRuleMetricArgs:
    def __init__(__self__, *,
                 metric_type: Optional[pulumi.Input[str]] = None,
                 threshold: Optional[pulumi.Input['AutoScalingConfigurationPolicyRuleMetricThresholdArgs']] = None):
        AutoScalingConfigurationPolicyRuleMetricArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            metric_type=metric_type,
            threshold=threshold,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             metric_type: Optional[pulumi.Input[str]] = None,
             threshold: Optional[pulumi.Input['AutoScalingConfigurationPolicyRuleMetricThresholdArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if metric_type is not None:
            _setter("metric_type", metric_type)
        if threshold is not None:
            _setter("threshold", threshold)

    @property
    @pulumi.getter(name="metricType")
    def metric_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "metric_type")

    @metric_type.setter
    def metric_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_type", value)

    @property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input['AutoScalingConfigurationPolicyRuleMetricThresholdArgs']]:
        return pulumi.get(self, "threshold")

    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input['AutoScalingConfigurationPolicyRuleMetricThresholdArgs']]):
        pulumi.set(self, "threshold", value)


@pulumi.input_type
class AutoScalingConfigurationPolicyRuleMetricThresholdArgs:
    def __init__(__self__, *,
                 operator: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[str] operator: The comparison operator to use. Options are greater than (`GT`), greater than or equal to (`GTE`), less than (`LT`), and less than or equal to (`LTE`).
        :param pulumi.Input[int] value: ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        AutoScalingConfigurationPolicyRuleMetricThresholdArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            operator=operator,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             operator: Optional[pulumi.Input[str]] = None,
             value: Optional[pulumi.Input[int]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if operator is not None:
            _setter("operator", operator)
        if value is not None:
            _setter("value", value)

    @property
    @pulumi.getter
    def operator(self) -> Optional[pulumi.Input[str]]:
        """
        The comparison operator to use. Options are greater than (`GT`), greater than or equal to (`GTE`), less than (`LT`), and less than or equal to (`LTE`).
        """
        return pulumi.get(self, "operator")

    @operator.setter
    def operator(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "operator", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[int]]:
        """
        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class GetAutoScalingConfigurationsFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str],
                 regex: Optional[bool] = None):
        GetAutoScalingConfigurationsFilterArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            values=values,
            regex=regex,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: str,
             values: Sequence[str],
             regex: Optional[bool] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("name", name)
        _setter("values", values)
        if regex is not None:
            _setter("regex", regex)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def regex(self) -> Optional[bool]:
        return pulumi.get(self, "regex")

    @regex.setter
    def regex(self, value: Optional[bool]):
        pulumi.set(self, "regex", value)


