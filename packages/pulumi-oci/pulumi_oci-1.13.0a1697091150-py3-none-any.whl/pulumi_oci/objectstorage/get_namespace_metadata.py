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
    'GetNamespaceMetadataResult',
    'AwaitableGetNamespaceMetadataResult',
    'get_namespace_metadata',
    'get_namespace_metadata_output',
]

@pulumi.output_type
class GetNamespaceMetadataResult:
    """
    A collection of values returned by getNamespaceMetadata.
    """
    def __init__(__self__, default_s3compartment_id=None, default_swift_compartment_id=None, id=None, namespace=None):
        if default_s3compartment_id and not isinstance(default_s3compartment_id, str):
            raise TypeError("Expected argument 'default_s3compartment_id' to be a str")
        pulumi.set(__self__, "default_s3compartment_id", default_s3compartment_id)
        if default_swift_compartment_id and not isinstance(default_swift_compartment_id, str):
            raise TypeError("Expected argument 'default_swift_compartment_id' to be a str")
        pulumi.set(__self__, "default_swift_compartment_id", default_swift_compartment_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter(name="defaultS3compartmentId")
    def default_s3compartment_id(self) -> str:
        return pulumi.get(self, "default_s3compartment_id")

    @property
    @pulumi.getter(name="defaultSwiftCompartmentId")
    def default_swift_compartment_id(self) -> str:
        return pulumi.get(self, "default_swift_compartment_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        return pulumi.get(self, "namespace")


class AwaitableGetNamespaceMetadataResult(GetNamespaceMetadataResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNamespaceMetadataResult(
            default_s3compartment_id=self.default_s3compartment_id,
            default_swift_compartment_id=self.default_swift_compartment_id,
            id=self.id,
            namespace=self.namespace)


def get_namespace_metadata(namespace: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNamespaceMetadataResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['namespace'] = namespace
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:ObjectStorage/getNamespaceMetadata:getNamespaceMetadata', __args__, opts=opts, typ=GetNamespaceMetadataResult).value

    return AwaitableGetNamespaceMetadataResult(
        default_s3compartment_id=pulumi.get(__ret__, 'default_s3compartment_id'),
        default_swift_compartment_id=pulumi.get(__ret__, 'default_swift_compartment_id'),
        id=pulumi.get(__ret__, 'id'),
        namespace=pulumi.get(__ret__, 'namespace'))


@_utilities.lift_output_func(get_namespace_metadata)
def get_namespace_metadata_output(namespace: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNamespaceMetadataResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
