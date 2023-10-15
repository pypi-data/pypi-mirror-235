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
    'GetOdaPrivateEndpointAttachmentsResult',
    'AwaitableGetOdaPrivateEndpointAttachmentsResult',
    'get_oda_private_endpoint_attachments',
    'get_oda_private_endpoint_attachments_output',
]

@pulumi.output_type
class GetOdaPrivateEndpointAttachmentsResult:
    """
    A collection of values returned by getOdaPrivateEndpointAttachments.
    """
    def __init__(__self__, compartment_id=None, filters=None, id=None, oda_private_endpoint_attachment_collections=None, oda_private_endpoint_id=None, state=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if oda_private_endpoint_attachment_collections and not isinstance(oda_private_endpoint_attachment_collections, list):
            raise TypeError("Expected argument 'oda_private_endpoint_attachment_collections' to be a list")
        pulumi.set(__self__, "oda_private_endpoint_attachment_collections", oda_private_endpoint_attachment_collections)
        if oda_private_endpoint_id and not isinstance(oda_private_endpoint_id, str):
            raise TypeError("Expected argument 'oda_private_endpoint_id' to be a str")
        pulumi.set(__self__, "oda_private_endpoint_id", oda_private_endpoint_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that the ODA private endpoint attachment belongs to.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetOdaPrivateEndpointAttachmentsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="odaPrivateEndpointAttachmentCollections")
    def oda_private_endpoint_attachment_collections(self) -> Sequence['outputs.GetOdaPrivateEndpointAttachmentsOdaPrivateEndpointAttachmentCollectionResult']:
        """
        The list of oda_private_endpoint_attachment_collection.
        """
        return pulumi.get(self, "oda_private_endpoint_attachment_collections")

    @property
    @pulumi.getter(name="odaPrivateEndpointId")
    def oda_private_endpoint_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the ODA Private Endpoint.
        """
        return pulumi.get(self, "oda_private_endpoint_id")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the ODA Private Endpoint attachment.
        """
        return pulumi.get(self, "state")


class AwaitableGetOdaPrivateEndpointAttachmentsResult(GetOdaPrivateEndpointAttachmentsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOdaPrivateEndpointAttachmentsResult(
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            oda_private_endpoint_attachment_collections=self.oda_private_endpoint_attachment_collections,
            oda_private_endpoint_id=self.oda_private_endpoint_id,
            state=self.state)


def get_oda_private_endpoint_attachments(compartment_id: Optional[str] = None,
                                         filters: Optional[Sequence[pulumi.InputType['GetOdaPrivateEndpointAttachmentsFilterArgs']]] = None,
                                         oda_private_endpoint_id: Optional[str] = None,
                                         state: Optional[str] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOdaPrivateEndpointAttachmentsResult:
    """
    This data source provides the list of Oda Private Endpoint Attachments in Oracle Cloud Infrastructure Digital Assistant service.

    Returns a page of ODA Instances attached to this ODA Private Endpoint.

    If the `opc-next-page` header appears in the response, then
    there are more items to retrieve. To get the next page in the subsequent
    GET request, include the header's value as the `page` query parameter.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_oda_private_endpoint_attachments = oci.Oda.get_oda_private_endpoint_attachments(compartment_id=var["compartment_id"],
        oda_private_endpoint_id=oci_oda_oda_private_endpoint["test_oda_private_endpoint"]["id"],
        state=var["oda_private_endpoint_attachment_state"])
    ```


    :param str compartment_id: List the ODA Private Endpoint Attachments that belong to this compartment.
    :param str oda_private_endpoint_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of ODA Private Endpoint.
    :param str state: List only the ODA Private Endpoint Attachments that are in this lifecycle state.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['odaPrivateEndpointId'] = oda_private_endpoint_id
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Oda/getOdaPrivateEndpointAttachments:getOdaPrivateEndpointAttachments', __args__, opts=opts, typ=GetOdaPrivateEndpointAttachmentsResult).value

    return AwaitableGetOdaPrivateEndpointAttachmentsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        oda_private_endpoint_attachment_collections=pulumi.get(__ret__, 'oda_private_endpoint_attachment_collections'),
        oda_private_endpoint_id=pulumi.get(__ret__, 'oda_private_endpoint_id'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_oda_private_endpoint_attachments)
def get_oda_private_endpoint_attachments_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                                filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetOdaPrivateEndpointAttachmentsFilterArgs']]]]] = None,
                                                oda_private_endpoint_id: Optional[pulumi.Input[str]] = None,
                                                state: Optional[pulumi.Input[Optional[str]]] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOdaPrivateEndpointAttachmentsResult]:
    """
    This data source provides the list of Oda Private Endpoint Attachments in Oracle Cloud Infrastructure Digital Assistant service.

    Returns a page of ODA Instances attached to this ODA Private Endpoint.

    If the `opc-next-page` header appears in the response, then
    there are more items to retrieve. To get the next page in the subsequent
    GET request, include the header's value as the `page` query parameter.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_oda_private_endpoint_attachments = oci.Oda.get_oda_private_endpoint_attachments(compartment_id=var["compartment_id"],
        oda_private_endpoint_id=oci_oda_oda_private_endpoint["test_oda_private_endpoint"]["id"],
        state=var["oda_private_endpoint_attachment_state"])
    ```


    :param str compartment_id: List the ODA Private Endpoint Attachments that belong to this compartment.
    :param str oda_private_endpoint_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of ODA Private Endpoint.
    :param str state: List only the ODA Private Endpoint Attachments that are in this lifecycle state.
    """
    ...
