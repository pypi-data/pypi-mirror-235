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
    'GetSuppressionsResult',
    'AwaitableGetSuppressionsResult',
    'get_suppressions',
    'get_suppressions_output',
]

@pulumi.output_type
class GetSuppressionsResult:
    """
    A collection of values returned by getSuppressions.
    """
    def __init__(__self__, compartment_id=None, email_address=None, filters=None, id=None, suppressions=None, time_created_greater_than_or_equal_to=None, time_created_less_than=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if email_address and not isinstance(email_address, str):
            raise TypeError("Expected argument 'email_address' to be a str")
        pulumi.set(__self__, "email_address", email_address)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if suppressions and not isinstance(suppressions, list):
            raise TypeError("Expected argument 'suppressions' to be a list")
        pulumi.set(__self__, "suppressions", suppressions)
        if time_created_greater_than_or_equal_to and not isinstance(time_created_greater_than_or_equal_to, str):
            raise TypeError("Expected argument 'time_created_greater_than_or_equal_to' to be a str")
        pulumi.set(__self__, "time_created_greater_than_or_equal_to", time_created_greater_than_or_equal_to)
        if time_created_less_than and not isinstance(time_created_less_than, str):
            raise TypeError("Expected argument 'time_created_less_than' to be a str")
        pulumi.set(__self__, "time_created_less_than", time_created_less_than)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment to contain the suppression. Since suppressions are at the customer level, this must be the tenancy OCID.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[str]:
        """
        The email address of the suppression.
        """
        return pulumi.get(self, "email_address")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetSuppressionsFilterResult']]:
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
    def suppressions(self) -> Sequence['outputs.GetSuppressionsSuppressionResult']:
        """
        The list of suppressions.
        """
        return pulumi.get(self, "suppressions")

    @property
    @pulumi.getter(name="timeCreatedGreaterThanOrEqualTo")
    def time_created_greater_than_or_equal_to(self) -> Optional[str]:
        return pulumi.get(self, "time_created_greater_than_or_equal_to")

    @property
    @pulumi.getter(name="timeCreatedLessThan")
    def time_created_less_than(self) -> Optional[str]:
        return pulumi.get(self, "time_created_less_than")


class AwaitableGetSuppressionsResult(GetSuppressionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSuppressionsResult(
            compartment_id=self.compartment_id,
            email_address=self.email_address,
            filters=self.filters,
            id=self.id,
            suppressions=self.suppressions,
            time_created_greater_than_or_equal_to=self.time_created_greater_than_or_equal_to,
            time_created_less_than=self.time_created_less_than)


def get_suppressions(compartment_id: Optional[str] = None,
                     email_address: Optional[str] = None,
                     filters: Optional[Sequence[pulumi.InputType['GetSuppressionsFilterArgs']]] = None,
                     time_created_greater_than_or_equal_to: Optional[str] = None,
                     time_created_less_than: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSuppressionsResult:
    """
    This data source provides the list of Suppressions in Oracle Cloud Infrastructure Email service.

    Gets a list of suppressed recipient email addresses for a user. The
    `compartmentId` for suppressions must be a tenancy OCID. The returned list
    is sorted by creation time in descending order.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_suppressions = oci.Email.get_suppressions(compartment_id=var["tenancy_ocid"],
        email_address=var["suppression_email_address"],
        time_created_greater_than_or_equal_to=var["suppression_time_created_greater_than_or_equal_to"],
        time_created_less_than=var["suppression_time_created_less_than"])
    ```


    :param str compartment_id: The OCID for the compartment.
    :param str email_address: The email address of the suppression.
    :param str time_created_greater_than_or_equal_to: Search for suppressions that were created within a specific date range, using this parameter to specify the earliest creation date for the returned list (inclusive). Specifying this parameter without the corresponding `timeCreatedLessThan` parameter will retrieve suppressions created from the given `timeCreatedGreaterThanOrEqualTo` to the current time, in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.
           
           **Example:** 2016-12-19T16:39:57.600Z
    :param str time_created_less_than: Search for suppressions that were created within a specific date range, using this parameter to specify the latest creation date for the returned list (exclusive). Specifying this parameter without the corresponding `timeCreatedGreaterThanOrEqualTo` parameter will retrieve all suppressions created before the specified end date, in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.
           
           **Example:** 2016-12-19T16:39:57.600Z
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['emailAddress'] = email_address
    __args__['filters'] = filters
    __args__['timeCreatedGreaterThanOrEqualTo'] = time_created_greater_than_or_equal_to
    __args__['timeCreatedLessThan'] = time_created_less_than
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Email/getSuppressions:getSuppressions', __args__, opts=opts, typ=GetSuppressionsResult).value

    return AwaitableGetSuppressionsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        email_address=pulumi.get(__ret__, 'email_address'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        suppressions=pulumi.get(__ret__, 'suppressions'),
        time_created_greater_than_or_equal_to=pulumi.get(__ret__, 'time_created_greater_than_or_equal_to'),
        time_created_less_than=pulumi.get(__ret__, 'time_created_less_than'))


@_utilities.lift_output_func(get_suppressions)
def get_suppressions_output(compartment_id: Optional[pulumi.Input[str]] = None,
                            email_address: Optional[pulumi.Input[Optional[str]]] = None,
                            filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetSuppressionsFilterArgs']]]]] = None,
                            time_created_greater_than_or_equal_to: Optional[pulumi.Input[Optional[str]]] = None,
                            time_created_less_than: Optional[pulumi.Input[Optional[str]]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSuppressionsResult]:
    """
    This data source provides the list of Suppressions in Oracle Cloud Infrastructure Email service.

    Gets a list of suppressed recipient email addresses for a user. The
    `compartmentId` for suppressions must be a tenancy OCID. The returned list
    is sorted by creation time in descending order.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_suppressions = oci.Email.get_suppressions(compartment_id=var["tenancy_ocid"],
        email_address=var["suppression_email_address"],
        time_created_greater_than_or_equal_to=var["suppression_time_created_greater_than_or_equal_to"],
        time_created_less_than=var["suppression_time_created_less_than"])
    ```


    :param str compartment_id: The OCID for the compartment.
    :param str email_address: The email address of the suppression.
    :param str time_created_greater_than_or_equal_to: Search for suppressions that were created within a specific date range, using this parameter to specify the earliest creation date for the returned list (inclusive). Specifying this parameter without the corresponding `timeCreatedLessThan` parameter will retrieve suppressions created from the given `timeCreatedGreaterThanOrEqualTo` to the current time, in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.
           
           **Example:** 2016-12-19T16:39:57.600Z
    :param str time_created_less_than: Search for suppressions that were created within a specific date range, using this parameter to specify the latest creation date for the returned list (exclusive). Specifying this parameter without the corresponding `timeCreatedGreaterThanOrEqualTo` parameter will retrieve all suppressions created before the specified end date, in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.
           
           **Example:** 2016-12-19T16:39:57.600Z
    """
    ...
