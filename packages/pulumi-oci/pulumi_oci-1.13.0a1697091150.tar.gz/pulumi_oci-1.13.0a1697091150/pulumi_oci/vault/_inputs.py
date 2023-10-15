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
    'SecretSecretContentArgs',
    'SecretSecretRuleArgs',
    'GetSecretsFilterArgs',
]

@pulumi.input_type
class SecretSecretContentArgs:
    def __init__(__self__, *,
                 content: pulumi.Input[str],
                 content_type: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 stage: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] content: (Updatable) The base64-encoded content of the secret.
        :param pulumi.Input[str] content_type: (Updatable) content type . Example `BASE64` .
        :param pulumi.Input[str] name: (Updatable) Names should be unique within a secret. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods.
        :param pulumi.Input[str] stage: (Updatable) The rotation state of the secret content. The default is `CURRENT`, meaning that the secret is currently in use. A secret version that you mark as `PENDING` is staged and available for use, but you don't yet want to rotate it into current, active use. For example, you might create or update a secret and mark its rotation state as `PENDING` if you haven't yet updated the secret on the target system. When creating a secret, only the value `CURRENT` is applicable, although the value `LATEST` is also automatically applied. When updating  a secret, you can specify a version's rotation state as either `CURRENT` or `PENDING`.
        """
        SecretSecretContentArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            content=content,
            content_type=content_type,
            name=name,
            stage=stage,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             content: pulumi.Input[str],
             content_type: pulumi.Input[str],
             name: Optional[pulumi.Input[str]] = None,
             stage: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("content", content)
        _setter("content_type", content_type)
        if name is not None:
            _setter("name", name)
        if stage is not None:
            _setter("stage", stage)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Input[str]:
        """
        (Updatable) The base64-encoded content of the secret.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: pulumi.Input[str]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Input[str]:
        """
        (Updatable) content type . Example `BASE64` .
        """
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "content_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Names should be unique within a secret. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def stage(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The rotation state of the secret content. The default is `CURRENT`, meaning that the secret is currently in use. A secret version that you mark as `PENDING` is staged and available for use, but you don't yet want to rotate it into current, active use. For example, you might create or update a secret and mark its rotation state as `PENDING` if you haven't yet updated the secret on the target system. When creating a secret, only the value `CURRENT` is applicable, although the value `LATEST` is also automatically applied. When updating  a secret, you can specify a version's rotation state as either `CURRENT` or `PENDING`.
        """
        return pulumi.get(self, "stage")

    @stage.setter
    def stage(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stage", value)


@pulumi.input_type
class SecretSecretRuleArgs:
    def __init__(__self__, *,
                 rule_type: pulumi.Input[str],
                 is_enforced_on_deleted_secret_versions: Optional[pulumi.Input[bool]] = None,
                 is_secret_content_retrieval_blocked_on_expiry: Optional[pulumi.Input[bool]] = None,
                 secret_version_expiry_interval: Optional[pulumi.Input[str]] = None,
                 time_of_absolute_expiry: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] rule_type: (Updatable) The type of rule, which either controls when the secret contents expire or whether they can be reused.
        :param pulumi.Input[bool] is_enforced_on_deleted_secret_versions: (Updatable) A property indicating whether the rule is applied even if the secret version with the content you are trying to reuse was deleted.
        :param pulumi.Input[bool] is_secret_content_retrieval_blocked_on_expiry: (Updatable) A property indicating whether to block retrieval of the secret content, on expiry. The default is false. If the secret has already expired and you would like to retrieve the secret contents, you need to edit the secret rule to disable this property, to allow reading the secret content.
        :param pulumi.Input[str] secret_version_expiry_interval: (Updatable) A property indicating how long the secret contents will be considered valid, expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals) format. The secret needs to be updated when the secret content expires. No enforcement mechanism exists at this time, but audit logs record the expiration on the appropriate date, according to the time interval specified in the rule. The timer resets after you update the secret contents. The minimum value is 1 day and the maximum value is 90 days for this property. Currently, only intervals expressed in days are supported. For example, pass `P3D` to have the secret version expire every 3 days.
        :param pulumi.Input[str] time_of_absolute_expiry: (Updatable) An optional property indicating the absolute time when this secret will expire, expressed in [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format. The minimum number of days from current time is 1 day and the maximum number of days from current time is 365 days. Example: `2019-04-03T21:10:29.600Z`
        """
        SecretSecretRuleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            rule_type=rule_type,
            is_enforced_on_deleted_secret_versions=is_enforced_on_deleted_secret_versions,
            is_secret_content_retrieval_blocked_on_expiry=is_secret_content_retrieval_blocked_on_expiry,
            secret_version_expiry_interval=secret_version_expiry_interval,
            time_of_absolute_expiry=time_of_absolute_expiry,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             rule_type: pulumi.Input[str],
             is_enforced_on_deleted_secret_versions: Optional[pulumi.Input[bool]] = None,
             is_secret_content_retrieval_blocked_on_expiry: Optional[pulumi.Input[bool]] = None,
             secret_version_expiry_interval: Optional[pulumi.Input[str]] = None,
             time_of_absolute_expiry: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("rule_type", rule_type)
        if is_enforced_on_deleted_secret_versions is not None:
            _setter("is_enforced_on_deleted_secret_versions", is_enforced_on_deleted_secret_versions)
        if is_secret_content_retrieval_blocked_on_expiry is not None:
            _setter("is_secret_content_retrieval_blocked_on_expiry", is_secret_content_retrieval_blocked_on_expiry)
        if secret_version_expiry_interval is not None:
            _setter("secret_version_expiry_interval", secret_version_expiry_interval)
        if time_of_absolute_expiry is not None:
            _setter("time_of_absolute_expiry", time_of_absolute_expiry)

    @property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> pulumi.Input[str]:
        """
        (Updatable) The type of rule, which either controls when the secret contents expire or whether they can be reused.
        """
        return pulumi.get(self, "rule_type")

    @rule_type.setter
    def rule_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "rule_type", value)

    @property
    @pulumi.getter(name="isEnforcedOnDeletedSecretVersions")
    def is_enforced_on_deleted_secret_versions(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) A property indicating whether the rule is applied even if the secret version with the content you are trying to reuse was deleted.
        """
        return pulumi.get(self, "is_enforced_on_deleted_secret_versions")

    @is_enforced_on_deleted_secret_versions.setter
    def is_enforced_on_deleted_secret_versions(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_enforced_on_deleted_secret_versions", value)

    @property
    @pulumi.getter(name="isSecretContentRetrievalBlockedOnExpiry")
    def is_secret_content_retrieval_blocked_on_expiry(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) A property indicating whether to block retrieval of the secret content, on expiry. The default is false. If the secret has already expired and you would like to retrieve the secret contents, you need to edit the secret rule to disable this property, to allow reading the secret content.
        """
        return pulumi.get(self, "is_secret_content_retrieval_blocked_on_expiry")

    @is_secret_content_retrieval_blocked_on_expiry.setter
    def is_secret_content_retrieval_blocked_on_expiry(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_secret_content_retrieval_blocked_on_expiry", value)

    @property
    @pulumi.getter(name="secretVersionExpiryInterval")
    def secret_version_expiry_interval(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) A property indicating how long the secret contents will be considered valid, expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals) format. The secret needs to be updated when the secret content expires. No enforcement mechanism exists at this time, but audit logs record the expiration on the appropriate date, according to the time interval specified in the rule. The timer resets after you update the secret contents. The minimum value is 1 day and the maximum value is 90 days for this property. Currently, only intervals expressed in days are supported. For example, pass `P3D` to have the secret version expire every 3 days.
        """
        return pulumi.get(self, "secret_version_expiry_interval")

    @secret_version_expiry_interval.setter
    def secret_version_expiry_interval(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_version_expiry_interval", value)

    @property
    @pulumi.getter(name="timeOfAbsoluteExpiry")
    def time_of_absolute_expiry(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) An optional property indicating the absolute time when this secret will expire, expressed in [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format. The minimum number of days from current time is 1 day and the maximum number of days from current time is 365 days. Example: `2019-04-03T21:10:29.600Z`
        """
        return pulumi.get(self, "time_of_absolute_expiry")

    @time_of_absolute_expiry.setter
    def time_of_absolute_expiry(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_of_absolute_expiry", value)


@pulumi.input_type
class GetSecretsFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str],
                 regex: Optional[bool] = None):
        """
        :param str name: The secret name.
        """
        GetSecretsFilterArgs._configure(
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
        """
        The secret name.
        """
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


