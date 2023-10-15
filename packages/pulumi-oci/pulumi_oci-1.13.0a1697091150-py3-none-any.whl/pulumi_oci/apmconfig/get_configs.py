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
    'GetConfigsResult',
    'AwaitableGetConfigsResult',
    'get_configs',
    'get_configs_output',
]

@pulumi.output_type
class GetConfigsResult:
    """
    A collection of values returned by getConfigs.
    """
    def __init__(__self__, apm_domain_id=None, config_collections=None, config_type=None, defined_tag_equals=None, defined_tag_exists=None, display_name=None, filters=None, freeform_tag_equals=None, freeform_tag_exists=None, id=None, options_group=None):
        if apm_domain_id and not isinstance(apm_domain_id, str):
            raise TypeError("Expected argument 'apm_domain_id' to be a str")
        pulumi.set(__self__, "apm_domain_id", apm_domain_id)
        if config_collections and not isinstance(config_collections, list):
            raise TypeError("Expected argument 'config_collections' to be a list")
        pulumi.set(__self__, "config_collections", config_collections)
        if config_type and not isinstance(config_type, str):
            raise TypeError("Expected argument 'config_type' to be a str")
        pulumi.set(__self__, "config_type", config_type)
        if defined_tag_equals and not isinstance(defined_tag_equals, list):
            raise TypeError("Expected argument 'defined_tag_equals' to be a list")
        pulumi.set(__self__, "defined_tag_equals", defined_tag_equals)
        if defined_tag_exists and not isinstance(defined_tag_exists, list):
            raise TypeError("Expected argument 'defined_tag_exists' to be a list")
        pulumi.set(__self__, "defined_tag_exists", defined_tag_exists)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if freeform_tag_equals and not isinstance(freeform_tag_equals, list):
            raise TypeError("Expected argument 'freeform_tag_equals' to be a list")
        pulumi.set(__self__, "freeform_tag_equals", freeform_tag_equals)
        if freeform_tag_exists and not isinstance(freeform_tag_exists, list):
            raise TypeError("Expected argument 'freeform_tag_exists' to be a list")
        pulumi.set(__self__, "freeform_tag_exists", freeform_tag_exists)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if options_group and not isinstance(options_group, str):
            raise TypeError("Expected argument 'options_group' to be a str")
        pulumi.set(__self__, "options_group", options_group)

    @property
    @pulumi.getter(name="apmDomainId")
    def apm_domain_id(self) -> str:
        return pulumi.get(self, "apm_domain_id")

    @property
    @pulumi.getter(name="configCollections")
    def config_collections(self) -> Sequence['outputs.GetConfigsConfigCollectionResult']:
        """
        The list of config_collection.
        """
        return pulumi.get(self, "config_collections")

    @property
    @pulumi.getter(name="configType")
    def config_type(self) -> Optional[str]:
        """
        The type of configuration item.
        """
        return pulumi.get(self, "config_type")

    @property
    @pulumi.getter(name="definedTagEquals")
    def defined_tag_equals(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "defined_tag_equals")

    @property
    @pulumi.getter(name="definedTagExists")
    def defined_tag_exists(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "defined_tag_exists")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The name by which a configuration entity is displayed to the end user.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetConfigsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter(name="freeformTagEquals")
    def freeform_tag_equals(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "freeform_tag_equals")

    @property
    @pulumi.getter(name="freeformTagExists")
    def freeform_tag_exists(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "freeform_tag_exists")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="optionsGroup")
    def options_group(self) -> Optional[str]:
        """
        A string that specifies the group that an OPTIONS item belongs to.
        """
        return pulumi.get(self, "options_group")


class AwaitableGetConfigsResult(GetConfigsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConfigsResult(
            apm_domain_id=self.apm_domain_id,
            config_collections=self.config_collections,
            config_type=self.config_type,
            defined_tag_equals=self.defined_tag_equals,
            defined_tag_exists=self.defined_tag_exists,
            display_name=self.display_name,
            filters=self.filters,
            freeform_tag_equals=self.freeform_tag_equals,
            freeform_tag_exists=self.freeform_tag_exists,
            id=self.id,
            options_group=self.options_group)


def get_configs(apm_domain_id: Optional[str] = None,
                config_type: Optional[str] = None,
                defined_tag_equals: Optional[Sequence[str]] = None,
                defined_tag_exists: Optional[Sequence[str]] = None,
                display_name: Optional[str] = None,
                filters: Optional[Sequence[pulumi.InputType['GetConfigsFilterArgs']]] = None,
                freeform_tag_equals: Optional[Sequence[str]] = None,
                freeform_tag_exists: Optional[Sequence[str]] = None,
                options_group: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConfigsResult:
    """
    This data source provides the list of Configs in Oracle Cloud Infrastructure Apm Config service.

    Returns all configuration items, which can optionally be filtered by configuration type.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_configs = oci.ApmConfig.get_configs(apm_domain_id=oci_apm_apm_domain["test_apm_domain"]["id"],
        config_type=var["config_config_type"],
        defined_tag_equals=var["config_defined_tag_equals"],
        defined_tag_exists=var["config_defined_tag_exists"],
        display_name=var["config_display_name"],
        freeform_tag_equals=var["config_freeform_tag_equals"],
        freeform_tag_exists=var["config_freeform_tag_exists"],
        options_group=var["config_options_group"])
    ```


    :param str apm_domain_id: The APM Domain ID the request is intended for.
    :param str config_type: A filter to match configuration items of a given type. Supported values are SPAN_FILTER, METRIC_GROUP, and APDEX.
    :param Sequence[str] defined_tag_equals: A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format "{namespace}.{tagName}.{value}".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as "OR". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as "AND".
    :param Sequence[str] defined_tag_exists: A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format "{namespace}.{tagName}.true" (for checking existence of a defined tag) or "{namespace}.true".  All inputs are case-insensitive. Currently, only existence ("true" at the end) is supported. Absence ("false" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as "OR". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as "AND".
    :param str display_name: A filter to return resources that match the given display name.
    :param Sequence[str] freeform_tag_equals: A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is "{tagName}.{value}".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as "OR".  Values for different tag names are interpreted as "AND".
    :param Sequence[str] freeform_tag_exists: A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is "{tagName}.true".  All inputs are case-insensitive. Currently, only existence ("true" at the end) is supported. Absence ("false" at the end) is not supported. Multiple values for different tag names are interpreted as "AND".
    :param str options_group: A filter to return OPTIONS resources that match the given group.
    """
    __args__ = dict()
    __args__['apmDomainId'] = apm_domain_id
    __args__['configType'] = config_type
    __args__['definedTagEquals'] = defined_tag_equals
    __args__['definedTagExists'] = defined_tag_exists
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['freeformTagEquals'] = freeform_tag_equals
    __args__['freeformTagExists'] = freeform_tag_exists
    __args__['optionsGroup'] = options_group
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:ApmConfig/getConfigs:getConfigs', __args__, opts=opts, typ=GetConfigsResult).value

    return AwaitableGetConfigsResult(
        apm_domain_id=pulumi.get(__ret__, 'apm_domain_id'),
        config_collections=pulumi.get(__ret__, 'config_collections'),
        config_type=pulumi.get(__ret__, 'config_type'),
        defined_tag_equals=pulumi.get(__ret__, 'defined_tag_equals'),
        defined_tag_exists=pulumi.get(__ret__, 'defined_tag_exists'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        freeform_tag_equals=pulumi.get(__ret__, 'freeform_tag_equals'),
        freeform_tag_exists=pulumi.get(__ret__, 'freeform_tag_exists'),
        id=pulumi.get(__ret__, 'id'),
        options_group=pulumi.get(__ret__, 'options_group'))


@_utilities.lift_output_func(get_configs)
def get_configs_output(apm_domain_id: Optional[pulumi.Input[str]] = None,
                       config_type: Optional[pulumi.Input[Optional[str]]] = None,
                       defined_tag_equals: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                       defined_tag_exists: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                       display_name: Optional[pulumi.Input[Optional[str]]] = None,
                       filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetConfigsFilterArgs']]]]] = None,
                       freeform_tag_equals: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                       freeform_tag_exists: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                       options_group: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConfigsResult]:
    """
    This data source provides the list of Configs in Oracle Cloud Infrastructure Apm Config service.

    Returns all configuration items, which can optionally be filtered by configuration type.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_configs = oci.ApmConfig.get_configs(apm_domain_id=oci_apm_apm_domain["test_apm_domain"]["id"],
        config_type=var["config_config_type"],
        defined_tag_equals=var["config_defined_tag_equals"],
        defined_tag_exists=var["config_defined_tag_exists"],
        display_name=var["config_display_name"],
        freeform_tag_equals=var["config_freeform_tag_equals"],
        freeform_tag_exists=var["config_freeform_tag_exists"],
        options_group=var["config_options_group"])
    ```


    :param str apm_domain_id: The APM Domain ID the request is intended for.
    :param str config_type: A filter to match configuration items of a given type. Supported values are SPAN_FILTER, METRIC_GROUP, and APDEX.
    :param Sequence[str] defined_tag_equals: A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format "{namespace}.{tagName}.{value}".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as "OR". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as "AND".
    :param Sequence[str] defined_tag_exists: A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format "{namespace}.{tagName}.true" (for checking existence of a defined tag) or "{namespace}.true".  All inputs are case-insensitive. Currently, only existence ("true" at the end) is supported. Absence ("false" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as "OR". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as "AND".
    :param str display_name: A filter to return resources that match the given display name.
    :param Sequence[str] freeform_tag_equals: A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is "{tagName}.{value}".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as "OR".  Values for different tag names are interpreted as "AND".
    :param Sequence[str] freeform_tag_exists: A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is "{tagName}.true".  All inputs are case-insensitive. Currently, only existence ("true" at the end) is supported. Absence ("false" at the end) is not supported. Multiple values for different tag names are interpreted as "AND".
    :param str options_group: A filter to return OPTIONS resources that match the given group.
    """
    ...
