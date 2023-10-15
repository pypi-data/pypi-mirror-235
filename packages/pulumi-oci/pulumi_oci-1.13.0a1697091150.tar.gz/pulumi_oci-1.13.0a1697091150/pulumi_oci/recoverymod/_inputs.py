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
    'ProtectedDatabaseMetricArgs',
    'ProtectedDatabaseRecoveryServiceSubnetArgs',
    'GetProtectedDatabasesFilterArgs',
    'GetProtectionPoliciesFilterArgs',
    'GetRecoveryServiceSubnetsFilterArgs',
]

@pulumi.input_type
class ProtectedDatabaseMetricArgs:
    def __init__(__self__, *,
                 backup_space_estimate_in_gbs: Optional[pulumi.Input[float]] = None,
                 backup_space_used_in_gbs: Optional[pulumi.Input[float]] = None,
                 current_retention_period_in_seconds: Optional[pulumi.Input[float]] = None,
                 db_size_in_gbs: Optional[pulumi.Input[float]] = None,
                 is_redo_logs_enabled: Optional[pulumi.Input[bool]] = None,
                 retention_period_in_days: Optional[pulumi.Input[float]] = None,
                 unprotected_window_in_seconds: Optional[pulumi.Input[float]] = None):
        """
        :param pulumi.Input[float] backup_space_estimate_in_gbs: The estimated backup storage space, in gigabytes, required to meet the recovery window goal, including foot print and backups for the protected database.
        :param pulumi.Input[float] backup_space_used_in_gbs: Backup storage space, in gigabytes, utilized by the protected database. Oracle charges for the total storage used.
        :param pulumi.Input[float] current_retention_period_in_seconds: Number of seconds backups are currently retained for this database.
        :param pulumi.Input[float] db_size_in_gbs: The estimated space, in gigabytes, consumed by the protected database. The database size is based on the size of the data files in the catalog, and does not include archive logs.
        :param pulumi.Input[bool] is_redo_logs_enabled: The value TRUE indicates that the protected database is configured to use Real-time data protection, and redo-data is sent from the protected database to Recovery Service. Real-time data protection substantially reduces the window of potential data loss that exists between successive archived redo log backups.
        :param pulumi.Input[float] retention_period_in_days: The maximum number of days to retain backups for a protected database.
        :param pulumi.Input[float] unprotected_window_in_seconds: This is the time window when there is data loss exposure. The point after which recovery is impossible unless additional redo is available.  This is the time we received the last backup or last redo-log shipped.
        """
        ProtectedDatabaseMetricArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            backup_space_estimate_in_gbs=backup_space_estimate_in_gbs,
            backup_space_used_in_gbs=backup_space_used_in_gbs,
            current_retention_period_in_seconds=current_retention_period_in_seconds,
            db_size_in_gbs=db_size_in_gbs,
            is_redo_logs_enabled=is_redo_logs_enabled,
            retention_period_in_days=retention_period_in_days,
            unprotected_window_in_seconds=unprotected_window_in_seconds,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             backup_space_estimate_in_gbs: Optional[pulumi.Input[float]] = None,
             backup_space_used_in_gbs: Optional[pulumi.Input[float]] = None,
             current_retention_period_in_seconds: Optional[pulumi.Input[float]] = None,
             db_size_in_gbs: Optional[pulumi.Input[float]] = None,
             is_redo_logs_enabled: Optional[pulumi.Input[bool]] = None,
             retention_period_in_days: Optional[pulumi.Input[float]] = None,
             unprotected_window_in_seconds: Optional[pulumi.Input[float]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if backup_space_estimate_in_gbs is not None:
            _setter("backup_space_estimate_in_gbs", backup_space_estimate_in_gbs)
        if backup_space_used_in_gbs is not None:
            _setter("backup_space_used_in_gbs", backup_space_used_in_gbs)
        if current_retention_period_in_seconds is not None:
            _setter("current_retention_period_in_seconds", current_retention_period_in_seconds)
        if db_size_in_gbs is not None:
            _setter("db_size_in_gbs", db_size_in_gbs)
        if is_redo_logs_enabled is not None:
            _setter("is_redo_logs_enabled", is_redo_logs_enabled)
        if retention_period_in_days is not None:
            _setter("retention_period_in_days", retention_period_in_days)
        if unprotected_window_in_seconds is not None:
            _setter("unprotected_window_in_seconds", unprotected_window_in_seconds)

    @property
    @pulumi.getter(name="backupSpaceEstimateInGbs")
    def backup_space_estimate_in_gbs(self) -> Optional[pulumi.Input[float]]:
        """
        The estimated backup storage space, in gigabytes, required to meet the recovery window goal, including foot print and backups for the protected database.
        """
        return pulumi.get(self, "backup_space_estimate_in_gbs")

    @backup_space_estimate_in_gbs.setter
    def backup_space_estimate_in_gbs(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "backup_space_estimate_in_gbs", value)

    @property
    @pulumi.getter(name="backupSpaceUsedInGbs")
    def backup_space_used_in_gbs(self) -> Optional[pulumi.Input[float]]:
        """
        Backup storage space, in gigabytes, utilized by the protected database. Oracle charges for the total storage used.
        """
        return pulumi.get(self, "backup_space_used_in_gbs")

    @backup_space_used_in_gbs.setter
    def backup_space_used_in_gbs(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "backup_space_used_in_gbs", value)

    @property
    @pulumi.getter(name="currentRetentionPeriodInSeconds")
    def current_retention_period_in_seconds(self) -> Optional[pulumi.Input[float]]:
        """
        Number of seconds backups are currently retained for this database.
        """
        return pulumi.get(self, "current_retention_period_in_seconds")

    @current_retention_period_in_seconds.setter
    def current_retention_period_in_seconds(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "current_retention_period_in_seconds", value)

    @property
    @pulumi.getter(name="dbSizeInGbs")
    def db_size_in_gbs(self) -> Optional[pulumi.Input[float]]:
        """
        The estimated space, in gigabytes, consumed by the protected database. The database size is based on the size of the data files in the catalog, and does not include archive logs.
        """
        return pulumi.get(self, "db_size_in_gbs")

    @db_size_in_gbs.setter
    def db_size_in_gbs(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "db_size_in_gbs", value)

    @property
    @pulumi.getter(name="isRedoLogsEnabled")
    def is_redo_logs_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        The value TRUE indicates that the protected database is configured to use Real-time data protection, and redo-data is sent from the protected database to Recovery Service. Real-time data protection substantially reduces the window of potential data loss that exists between successive archived redo log backups.
        """
        return pulumi.get(self, "is_redo_logs_enabled")

    @is_redo_logs_enabled.setter
    def is_redo_logs_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_redo_logs_enabled", value)

    @property
    @pulumi.getter(name="retentionPeriodInDays")
    def retention_period_in_days(self) -> Optional[pulumi.Input[float]]:
        """
        The maximum number of days to retain backups for a protected database.
        """
        return pulumi.get(self, "retention_period_in_days")

    @retention_period_in_days.setter
    def retention_period_in_days(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "retention_period_in_days", value)

    @property
    @pulumi.getter(name="unprotectedWindowInSeconds")
    def unprotected_window_in_seconds(self) -> Optional[pulumi.Input[float]]:
        """
        This is the time window when there is data loss exposure. The point after which recovery is impossible unless additional redo is available.  This is the time we received the last backup or last redo-log shipped.
        """
        return pulumi.get(self, "unprotected_window_in_seconds")

    @unprotected_window_in_seconds.setter
    def unprotected_window_in_seconds(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "unprotected_window_in_seconds", value)


@pulumi.input_type
class ProtectedDatabaseRecoveryServiceSubnetArgs:
    def __init__(__self__, *,
                 recovery_service_subnet_id: pulumi.Input[str],
                 state: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] recovery_service_subnet_id: (Updatable) The recovery service subnet OCID.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] state: The current state of the Protected Database.
        """
        ProtectedDatabaseRecoveryServiceSubnetArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            recovery_service_subnet_id=recovery_service_subnet_id,
            state=state,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             recovery_service_subnet_id: pulumi.Input[str],
             state: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("recovery_service_subnet_id", recovery_service_subnet_id)
        if state is not None:
            _setter("state", state)

    @property
    @pulumi.getter(name="recoveryServiceSubnetId")
    def recovery_service_subnet_id(self) -> pulumi.Input[str]:
        """
        (Updatable) The recovery service subnet OCID.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "recovery_service_subnet_id")

    @recovery_service_subnet_id.setter
    def recovery_service_subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "recovery_service_subnet_id", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current state of the Protected Database.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)


@pulumi.input_type
class GetProtectedDatabasesFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str],
                 regex: Optional[bool] = None):
        GetProtectedDatabasesFilterArgs._configure(
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


@pulumi.input_type
class GetProtectionPoliciesFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str],
                 regex: Optional[bool] = None):
        GetProtectionPoliciesFilterArgs._configure(
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


@pulumi.input_type
class GetRecoveryServiceSubnetsFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str],
                 regex: Optional[bool] = None):
        GetRecoveryServiceSubnetsFilterArgs._configure(
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


