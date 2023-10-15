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
    'GetOdaPrivateEndpointAttachmentResult',
    'AwaitableGetOdaPrivateEndpointAttachmentResult',
    'get_oda_private_endpoint_attachment',
    'get_oda_private_endpoint_attachment_output',
]

@pulumi.output_type
class GetOdaPrivateEndpointAttachmentResult:
    """
    A collection of values returned by getOdaPrivateEndpointAttachment.
    """
    def __init__(__self__, compartment_id=None, id=None, oda_instance_id=None, oda_private_endpoint_attachment_id=None, oda_private_endpoint_id=None, state=None, time_created=None, time_updated=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if oda_instance_id and not isinstance(oda_instance_id, str):
            raise TypeError("Expected argument 'oda_instance_id' to be a str")
        pulumi.set(__self__, "oda_instance_id", oda_instance_id)
        if oda_private_endpoint_attachment_id and not isinstance(oda_private_endpoint_attachment_id, str):
            raise TypeError("Expected argument 'oda_private_endpoint_attachment_id' to be a str")
        pulumi.set(__self__, "oda_private_endpoint_attachment_id", oda_private_endpoint_attachment_id)
        if oda_private_endpoint_id and not isinstance(oda_private_endpoint_id, str):
            raise TypeError("Expected argument 'oda_private_endpoint_id' to be a str")
        pulumi.set(__self__, "oda_private_endpoint_id", oda_private_endpoint_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that the ODA private endpoint attachment belongs to.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the ODA Private Endpoint Attachment.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="odaInstanceId")
    def oda_instance_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the attached ODA Instance.
        """
        return pulumi.get(self, "oda_instance_id")

    @property
    @pulumi.getter(name="odaPrivateEndpointAttachmentId")
    def oda_private_endpoint_attachment_id(self) -> str:
        return pulumi.get(self, "oda_private_endpoint_attachment_id")

    @property
    @pulumi.getter(name="odaPrivateEndpointId")
    def oda_private_endpoint_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the ODA Private Endpoint.
        """
        return pulumi.get(self, "oda_private_endpoint_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the ODA Private Endpoint attachment.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        When the resource was created. A date-time string as described in [RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        When the resource was last updated. A date-time string as described in [RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.
        """
        return pulumi.get(self, "time_updated")


class AwaitableGetOdaPrivateEndpointAttachmentResult(GetOdaPrivateEndpointAttachmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOdaPrivateEndpointAttachmentResult(
            compartment_id=self.compartment_id,
            id=self.id,
            oda_instance_id=self.oda_instance_id,
            oda_private_endpoint_attachment_id=self.oda_private_endpoint_attachment_id,
            oda_private_endpoint_id=self.oda_private_endpoint_id,
            state=self.state,
            time_created=self.time_created,
            time_updated=self.time_updated)


def get_oda_private_endpoint_attachment(oda_private_endpoint_attachment_id: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOdaPrivateEndpointAttachmentResult:
    """
    This data source provides details about a specific Oda Private Endpoint Attachment resource in Oracle Cloud Infrastructure Digital Assistant service.

    Gets the specified ODA Private Endpoint Attachment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_oda_private_endpoint_attachment = oci.Oda.get_oda_private_endpoint_attachment(oda_private_endpoint_attachment_id=oci_oda_oda_private_endpoint_attachment["test_oda_private_endpoint_attachment"]["id"])
    ```


    :param str oda_private_endpoint_attachment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of ODA Private Endpoint Attachment.
    """
    __args__ = dict()
    __args__['odaPrivateEndpointAttachmentId'] = oda_private_endpoint_attachment_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Oda/getOdaPrivateEndpointAttachment:getOdaPrivateEndpointAttachment', __args__, opts=opts, typ=GetOdaPrivateEndpointAttachmentResult).value

    return AwaitableGetOdaPrivateEndpointAttachmentResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        id=pulumi.get(__ret__, 'id'),
        oda_instance_id=pulumi.get(__ret__, 'oda_instance_id'),
        oda_private_endpoint_attachment_id=pulumi.get(__ret__, 'oda_private_endpoint_attachment_id'),
        oda_private_endpoint_id=pulumi.get(__ret__, 'oda_private_endpoint_id'),
        state=pulumi.get(__ret__, 'state'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'))


@_utilities.lift_output_func(get_oda_private_endpoint_attachment)
def get_oda_private_endpoint_attachment_output(oda_private_endpoint_attachment_id: Optional[pulumi.Input[str]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOdaPrivateEndpointAttachmentResult]:
    """
    This data source provides details about a specific Oda Private Endpoint Attachment resource in Oracle Cloud Infrastructure Digital Assistant service.

    Gets the specified ODA Private Endpoint Attachment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_oda_private_endpoint_attachment = oci.Oda.get_oda_private_endpoint_attachment(oda_private_endpoint_attachment_id=oci_oda_oda_private_endpoint_attachment["test_oda_private_endpoint_attachment"]["id"])
    ```


    :param str oda_private_endpoint_attachment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of ODA Private Endpoint Attachment.
    """
    ...
