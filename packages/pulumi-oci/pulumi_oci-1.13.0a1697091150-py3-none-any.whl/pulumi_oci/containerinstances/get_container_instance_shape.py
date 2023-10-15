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

__all__ = [
    'GetContainerInstanceShapeResult',
    'AwaitableGetContainerInstanceShapeResult',
    'get_container_instance_shape',
    'get_container_instance_shape_output',
]

@pulumi.output_type
class GetContainerInstanceShapeResult:
    """
    A collection of values returned by getContainerInstanceShape.
    """
    def __init__(__self__, availability_domain=None, compartment_id=None, id=None, items=None):
        if availability_domain and not isinstance(availability_domain, str):
            raise TypeError("Expected argument 'availability_domain' to be a str")
        pulumi.set(__self__, "availability_domain", availability_domain)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if items and not isinstance(items, list):
            raise TypeError("Expected argument 'items' to be a list")
        pulumi.set(__self__, "items", items)

    @property
    @pulumi.getter(name="availabilityDomain")
    def availability_domain(self) -> Optional[str]:
        return pulumi.get(self, "availability_domain")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.GetContainerInstanceShapeItemResult']:
        """
        List of shapes.
        """
        return pulumi.get(self, "items")


class AwaitableGetContainerInstanceShapeResult(GetContainerInstanceShapeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContainerInstanceShapeResult(
            availability_domain=self.availability_domain,
            compartment_id=self.compartment_id,
            id=self.id,
            items=self.items)


def get_container_instance_shape(availability_domain: Optional[str] = None,
                                 compartment_id: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContainerInstanceShapeResult:
    """
    This data source provides details about a specific Container Instance Shape resource in Oracle Cloud Infrastructure Container Instances service.

    Get a list of shapes for creating Container Instances and their details.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_container_instance_shape = oci.ContainerInstances.get_container_instance_shape(compartment_id=var["compartment_id"],
        availability_domain=var["container_instance_shape_availability_domain"])
    ```


    :param str availability_domain: The name of the availability domain.  Example: `Uocm:PHX-AD-1`
    :param str compartment_id: The ID of the compartment in which to list resources.
    """
    __args__ = dict()
    __args__['availabilityDomain'] = availability_domain
    __args__['compartmentId'] = compartment_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:ContainerInstances/getContainerInstanceShape:getContainerInstanceShape', __args__, opts=opts, typ=GetContainerInstanceShapeResult).value

    return AwaitableGetContainerInstanceShapeResult(
        availability_domain=pulumi.get(__ret__, 'availability_domain'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        id=pulumi.get(__ret__, 'id'),
        items=pulumi.get(__ret__, 'items'))


@_utilities.lift_output_func(get_container_instance_shape)
def get_container_instance_shape_output(availability_domain: Optional[pulumi.Input[Optional[str]]] = None,
                                        compartment_id: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetContainerInstanceShapeResult]:
    """
    This data source provides details about a specific Container Instance Shape resource in Oracle Cloud Infrastructure Container Instances service.

    Get a list of shapes for creating Container Instances and their details.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_container_instance_shape = oci.ContainerInstances.get_container_instance_shape(compartment_id=var["compartment_id"],
        availability_domain=var["container_instance_shape_availability_domain"])
    ```


    :param str availability_domain: The name of the availability domain.  Example: `Uocm:PHX-AD-1`
    :param str compartment_id: The ID of the compartment in which to list resources.
    """
    ...
