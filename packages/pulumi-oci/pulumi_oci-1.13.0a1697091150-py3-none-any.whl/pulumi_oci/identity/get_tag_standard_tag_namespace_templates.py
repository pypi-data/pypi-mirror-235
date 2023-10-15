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
    'GetTagStandardTagNamespaceTemplatesResult',
    'AwaitableGetTagStandardTagNamespaceTemplatesResult',
    'get_tag_standard_tag_namespace_templates',
    'get_tag_standard_tag_namespace_templates_output',
]

@pulumi.output_type
class GetTagStandardTagNamespaceTemplatesResult:
    """
    A collection of values returned by getTagStandardTagNamespaceTemplates.
    """
    def __init__(__self__, compartment_id=None, filters=None, id=None, standard_tag_namespace_templates=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if standard_tag_namespace_templates and not isinstance(standard_tag_namespace_templates, list):
            raise TypeError("Expected argument 'standard_tag_namespace_templates' to be a list")
        pulumi.set(__self__, "standard_tag_namespace_templates", standard_tag_namespace_templates)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetTagStandardTagNamespaceTemplatesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="standardTagNamespaceTemplates")
    def standard_tag_namespace_templates(self) -> Sequence['outputs.GetTagStandardTagNamespaceTemplatesStandardTagNamespaceTemplateResult']:
        """
        The list of standard_tag_namespace_templates.
        """
        return pulumi.get(self, "standard_tag_namespace_templates")


class AwaitableGetTagStandardTagNamespaceTemplatesResult(GetTagStandardTagNamespaceTemplatesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTagStandardTagNamespaceTemplatesResult(
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            standard_tag_namespace_templates=self.standard_tag_namespace_templates)


def get_tag_standard_tag_namespace_templates(compartment_id: Optional[str] = None,
                                             filters: Optional[Sequence[pulumi.InputType['GetTagStandardTagNamespaceTemplatesFilterArgs']]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTagStandardTagNamespaceTemplatesResult:
    """
    This data source provides the list of Tag Standard Tag Namespace Templates in Oracle Cloud Infrastructure Identity service.

    Lists available standard tag namespaces that users can create.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_tag_standard_tag_namespace_templates = oci.Identity.get_tag_standard_tag_namespace_templates(compartment_id=var["compartment_id"])
    ```


    :param str compartment_id: The OCID of the compartment (remember that the tenancy is simply the root compartment).
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Identity/getTagStandardTagNamespaceTemplates:getTagStandardTagNamespaceTemplates', __args__, opts=opts, typ=GetTagStandardTagNamespaceTemplatesResult).value

    return AwaitableGetTagStandardTagNamespaceTemplatesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        standard_tag_namespace_templates=pulumi.get(__ret__, 'standard_tag_namespace_templates'))


@_utilities.lift_output_func(get_tag_standard_tag_namespace_templates)
def get_tag_standard_tag_namespace_templates_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                                    filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetTagStandardTagNamespaceTemplatesFilterArgs']]]]] = None,
                                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTagStandardTagNamespaceTemplatesResult]:
    """
    This data source provides the list of Tag Standard Tag Namespace Templates in Oracle Cloud Infrastructure Identity service.

    Lists available standard tag namespaces that users can create.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_tag_standard_tag_namespace_templates = oci.Identity.get_tag_standard_tag_namespace_templates(compartment_id=var["compartment_id"])
    ```


    :param str compartment_id: The OCID of the compartment (remember that the tenancy is simply the root compartment).
    """
    ...
