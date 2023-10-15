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
    'GetBootVolumeAttachmentsResult',
    'AwaitableGetBootVolumeAttachmentsResult',
    'get_boot_volume_attachments',
    'get_boot_volume_attachments_output',
]

@pulumi.output_type
class GetBootVolumeAttachmentsResult:
    """
    A collection of values returned by getBootVolumeAttachments.
    """
    def __init__(__self__, availability_domain=None, boot_volume_attachments=None, boot_volume_id=None, compartment_id=None, filters=None, id=None, instance_id=None):
        if availability_domain and not isinstance(availability_domain, str):
            raise TypeError("Expected argument 'availability_domain' to be a str")
        pulumi.set(__self__, "availability_domain", availability_domain)
        if boot_volume_attachments and not isinstance(boot_volume_attachments, list):
            raise TypeError("Expected argument 'boot_volume_attachments' to be a list")
        pulumi.set(__self__, "boot_volume_attachments", boot_volume_attachments)
        if boot_volume_id and not isinstance(boot_volume_id, str):
            raise TypeError("Expected argument 'boot_volume_id' to be a str")
        pulumi.set(__self__, "boot_volume_id", boot_volume_id)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_id and not isinstance(instance_id, str):
            raise TypeError("Expected argument 'instance_id' to be a str")
        pulumi.set(__self__, "instance_id", instance_id)

    @property
    @pulumi.getter(name="availabilityDomain")
    def availability_domain(self) -> str:
        """
        The availability domain of an instance.  Example: `Uocm:PHX-AD-1`
        """
        return pulumi.get(self, "availability_domain")

    @property
    @pulumi.getter(name="bootVolumeAttachments")
    def boot_volume_attachments(self) -> Sequence['outputs.GetBootVolumeAttachmentsBootVolumeAttachmentResult']:
        """
        The list of boot_volume_attachments.
        """
        return pulumi.get(self, "boot_volume_attachments")

    @property
    @pulumi.getter(name="bootVolumeId")
    def boot_volume_id(self) -> Optional[str]:
        """
        The OCID of the boot volume.
        """
        return pulumi.get(self, "boot_volume_id")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetBootVolumeAttachmentsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[str]:
        """
        The OCID of the instance the boot volume is attached to.
        """
        return pulumi.get(self, "instance_id")


class AwaitableGetBootVolumeAttachmentsResult(GetBootVolumeAttachmentsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBootVolumeAttachmentsResult(
            availability_domain=self.availability_domain,
            boot_volume_attachments=self.boot_volume_attachments,
            boot_volume_id=self.boot_volume_id,
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            instance_id=self.instance_id)


def get_boot_volume_attachments(availability_domain: Optional[str] = None,
                                boot_volume_id: Optional[str] = None,
                                compartment_id: Optional[str] = None,
                                filters: Optional[Sequence[pulumi.InputType['GetBootVolumeAttachmentsFilterArgs']]] = None,
                                instance_id: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBootVolumeAttachmentsResult:
    """
    Use this data source to access information about an existing resource.

    :param str availability_domain: The name of the availability domain.  Example: `Uocm:PHX-AD-1`
    :param str boot_volume_id: The OCID of the boot volume.
    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str instance_id: The OCID of the instance.
    """
    __args__ = dict()
    __args__['availabilityDomain'] = availability_domain
    __args__['bootVolumeId'] = boot_volume_id
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['instanceId'] = instance_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Core/getBootVolumeAttachments:getBootVolumeAttachments', __args__, opts=opts, typ=GetBootVolumeAttachmentsResult).value

    return AwaitableGetBootVolumeAttachmentsResult(
        availability_domain=pulumi.get(__ret__, 'availability_domain'),
        boot_volume_attachments=pulumi.get(__ret__, 'boot_volume_attachments'),
        boot_volume_id=pulumi.get(__ret__, 'boot_volume_id'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        instance_id=pulumi.get(__ret__, 'instance_id'))


@_utilities.lift_output_func(get_boot_volume_attachments)
def get_boot_volume_attachments_output(availability_domain: Optional[pulumi.Input[str]] = None,
                                       boot_volume_id: Optional[pulumi.Input[Optional[str]]] = None,
                                       compartment_id: Optional[pulumi.Input[str]] = None,
                                       filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetBootVolumeAttachmentsFilterArgs']]]]] = None,
                                       instance_id: Optional[pulumi.Input[Optional[str]]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBootVolumeAttachmentsResult]:
    """
    Use this data source to access information about an existing resource.

    :param str availability_domain: The name of the availability domain.  Example: `Uocm:PHX-AD-1`
    :param str boot_volume_id: The OCID of the boot volume.
    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str instance_id: The OCID of the instance.
    """
    ...
