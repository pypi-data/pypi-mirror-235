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
    'GetSuppressionResult',
    'AwaitableGetSuppressionResult',
    'get_suppression',
    'get_suppression_output',
]

@pulumi.output_type
class GetSuppressionResult:
    """
    A collection of values returned by getSuppression.
    """
    def __init__(__self__, compartment_id=None, email_address=None, error_detail=None, error_source=None, id=None, message_id=None, reason=None, suppression_id=None, time_created=None, time_last_suppressed=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if email_address and not isinstance(email_address, str):
            raise TypeError("Expected argument 'email_address' to be a str")
        pulumi.set(__self__, "email_address", email_address)
        if error_detail and not isinstance(error_detail, str):
            raise TypeError("Expected argument 'error_detail' to be a str")
        pulumi.set(__self__, "error_detail", error_detail)
        if error_source and not isinstance(error_source, str):
            raise TypeError("Expected argument 'error_source' to be a str")
        pulumi.set(__self__, "error_source", error_source)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if message_id and not isinstance(message_id, str):
            raise TypeError("Expected argument 'message_id' to be a str")
        pulumi.set(__self__, "message_id", message_id)
        if reason and not isinstance(reason, str):
            raise TypeError("Expected argument 'reason' to be a str")
        pulumi.set(__self__, "reason", reason)
        if suppression_id and not isinstance(suppression_id, str):
            raise TypeError("Expected argument 'suppression_id' to be a str")
        pulumi.set(__self__, "suppression_id", suppression_id)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_last_suppressed and not isinstance(time_last_suppressed, str):
            raise TypeError("Expected argument 'time_last_suppressed' to be a str")
        pulumi.set(__self__, "time_last_suppressed", time_last_suppressed)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment to contain the suppression. Since suppressions are at the customer level, this must be the tenancy OCID.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> str:
        """
        The email address of the suppression.
        """
        return pulumi.get(self, "email_address")

    @property
    @pulumi.getter(name="errorDetail")
    def error_detail(self) -> str:
        """
        The specific error message returned by a system that resulted in the suppression. This message is usually an SMTP error code with additional descriptive text. Not provided for all types of suppressions.
        """
        return pulumi.get(self, "error_detail")

    @property
    @pulumi.getter(name="errorSource")
    def error_source(self) -> str:
        """
        DNS name of the source of the error that caused the suppression. Will be set to either the remote-mta or reporting-mta field from a delivery status notification (RFC 3464) when available. Not provided for all types of suppressions, and not always known.
        """
        return pulumi.get(self, "error_source")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The unique OCID of the suppression.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="messageId")
    def message_id(self) -> str:
        """
        The value of the Message-ID header from the email that triggered a suppression. This value is as defined in RFC 5322 section 3.6.4, excluding angle-brackets. Not provided for all types of suppressions.
        """
        return pulumi.get(self, "message_id")

    @property
    @pulumi.getter
    def reason(self) -> str:
        """
        The reason that the email address was suppressed. For more information on the types of bounces, see [Suppression List](https://docs.cloud.oracle.com/iaas/Content/Email/Concepts/overview.htm#components).
        """
        return pulumi.get(self, "reason")

    @property
    @pulumi.getter(name="suppressionId")
    def suppression_id(self) -> str:
        return pulumi.get(self, "suppression_id")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time a recipient's email address was added to the suppression list, in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeLastSuppressed")
    def time_last_suppressed(self) -> str:
        """
        The last date and time the suppression prevented submission in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.
        """
        return pulumi.get(self, "time_last_suppressed")


class AwaitableGetSuppressionResult(GetSuppressionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSuppressionResult(
            compartment_id=self.compartment_id,
            email_address=self.email_address,
            error_detail=self.error_detail,
            error_source=self.error_source,
            id=self.id,
            message_id=self.message_id,
            reason=self.reason,
            suppression_id=self.suppression_id,
            time_created=self.time_created,
            time_last_suppressed=self.time_last_suppressed)


def get_suppression(suppression_id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSuppressionResult:
    """
    This data source provides details about a specific Suppression resource in Oracle Cloud Infrastructure Email service.

    Gets the details of a suppressed recipient email address for a given
    `suppressionId`. Each suppression is given a unique OCID.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_suppression = oci.Email.get_suppression(suppression_id=oci_email_suppression["test_suppression"]["id"])
    ```


    :param str suppression_id: The unique OCID of the suppression.
    """
    __args__ = dict()
    __args__['suppressionId'] = suppression_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Email/getSuppression:getSuppression', __args__, opts=opts, typ=GetSuppressionResult).value

    return AwaitableGetSuppressionResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        email_address=pulumi.get(__ret__, 'email_address'),
        error_detail=pulumi.get(__ret__, 'error_detail'),
        error_source=pulumi.get(__ret__, 'error_source'),
        id=pulumi.get(__ret__, 'id'),
        message_id=pulumi.get(__ret__, 'message_id'),
        reason=pulumi.get(__ret__, 'reason'),
        suppression_id=pulumi.get(__ret__, 'suppression_id'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_last_suppressed=pulumi.get(__ret__, 'time_last_suppressed'))


@_utilities.lift_output_func(get_suppression)
def get_suppression_output(suppression_id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSuppressionResult]:
    """
    This data source provides details about a specific Suppression resource in Oracle Cloud Infrastructure Email service.

    Gets the details of a suppressed recipient email address for a given
    `suppressionId`. Each suppression is given a unique OCID.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_suppression = oci.Email.get_suppression(suppression_id=oci_email_suppression["test_suppression"]["id"])
    ```


    :param str suppression_id: The unique OCID of the suppression.
    """
    ...
