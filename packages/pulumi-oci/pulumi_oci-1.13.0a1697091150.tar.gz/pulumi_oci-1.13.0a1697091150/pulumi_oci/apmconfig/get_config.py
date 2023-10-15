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
    'GetConfigResult',
    'AwaitableGetConfigResult',
    'get_config',
    'get_config_output',
]

@pulumi.output_type
class GetConfigResult:
    """
    A collection of values returned by getConfig.
    """
    def __init__(__self__, apm_domain_id=None, config_id=None, config_type=None, created_by=None, defined_tags=None, description=None, dimensions=None, display_name=None, etag=None, filter_id=None, filter_text=None, freeform_tags=None, group=None, id=None, in_use_bies=None, metrics=None, namespace=None, opc_dry_run=None, options=None, rules=None, time_created=None, time_updated=None, updated_by=None):
        if apm_domain_id and not isinstance(apm_domain_id, str):
            raise TypeError("Expected argument 'apm_domain_id' to be a str")
        pulumi.set(__self__, "apm_domain_id", apm_domain_id)
        if config_id and not isinstance(config_id, str):
            raise TypeError("Expected argument 'config_id' to be a str")
        pulumi.set(__self__, "config_id", config_id)
        if config_type and not isinstance(config_type, str):
            raise TypeError("Expected argument 'config_type' to be a str")
        pulumi.set(__self__, "config_type", config_type)
        if created_by and not isinstance(created_by, str):
            raise TypeError("Expected argument 'created_by' to be a str")
        pulumi.set(__self__, "created_by", created_by)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if dimensions and not isinstance(dimensions, list):
            raise TypeError("Expected argument 'dimensions' to be a list")
        pulumi.set(__self__, "dimensions", dimensions)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if filter_id and not isinstance(filter_id, str):
            raise TypeError("Expected argument 'filter_id' to be a str")
        pulumi.set(__self__, "filter_id", filter_id)
        if filter_text and not isinstance(filter_text, str):
            raise TypeError("Expected argument 'filter_text' to be a str")
        pulumi.set(__self__, "filter_text", filter_text)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if group and not isinstance(group, str):
            raise TypeError("Expected argument 'group' to be a str")
        pulumi.set(__self__, "group", group)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if in_use_bies and not isinstance(in_use_bies, list):
            raise TypeError("Expected argument 'in_use_bies' to be a list")
        pulumi.set(__self__, "in_use_bies", in_use_bies)
        if metrics and not isinstance(metrics, list):
            raise TypeError("Expected argument 'metrics' to be a list")
        pulumi.set(__self__, "metrics", metrics)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if opc_dry_run and not isinstance(opc_dry_run, str):
            raise TypeError("Expected argument 'opc_dry_run' to be a str")
        pulumi.set(__self__, "opc_dry_run", opc_dry_run)
        if options and not isinstance(options, str):
            raise TypeError("Expected argument 'options' to be a str")
        pulumi.set(__self__, "options", options)
        if rules and not isinstance(rules, list):
            raise TypeError("Expected argument 'rules' to be a list")
        pulumi.set(__self__, "rules", rules)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)
        if updated_by and not isinstance(updated_by, str):
            raise TypeError("Expected argument 'updated_by' to be a str")
        pulumi.set(__self__, "updated_by", updated_by)

    @property
    @pulumi.getter(name="apmDomainId")
    def apm_domain_id(self) -> str:
        return pulumi.get(self, "apm_domain_id")

    @property
    @pulumi.getter(name="configId")
    def config_id(self) -> str:
        return pulumi.get(self, "config_id")

    @property
    @pulumi.getter(name="configType")
    def config_type(self) -> str:
        """
        The type of configuration item.
        """
        return pulumi.get(self, "config_type")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a user.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A description of the metric.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def dimensions(self) -> Sequence['outputs.GetConfigDimensionResult']:
        """
        A list of dimensions for the metric. This variable should not be used.
        """
        return pulumi.get(self, "dimensions")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The name by which a configuration entity is displayed to the end user.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        For optimistic concurrency control. See `if-match`.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="filterId")
    def filter_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a Span Filter. The filterId is mandatory for the creation of MetricGroups. A filterId is generated when a Span Filter is created.
        """
        return pulumi.get(self, "filter_id")

    @property
    @pulumi.getter(name="filterText")
    def filter_text(self) -> str:
        """
        The string that defines the Span Filter expression.
        """
        return pulumi.get(self, "filter_text")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def group(self) -> str:
        """
        A string that specifies the group that an OPTIONS item belongs to.
        """
        return pulumi.get(self, "group")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the configuration item. An OCID is generated when the item is created.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="inUseBies")
    def in_use_bies(self) -> Sequence['outputs.GetConfigInUseByResult']:
        """
        The list of configuration items that reference the span filter.
        """
        return pulumi.get(self, "in_use_bies")

    @property
    @pulumi.getter
    def metrics(self) -> Sequence['outputs.GetConfigMetricResult']:
        """
        The list of metrics in this group.
        """
        return pulumi.get(self, "metrics")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        """
        The namespace to which the metrics are published. It must be one of several predefined namespaces.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="opcDryRun")
    def opc_dry_run(self) -> str:
        return pulumi.get(self, "opc_dry_run")

    @property
    @pulumi.getter
    def options(self) -> str:
        """
        The options are stored here as JSON.
        """
        return pulumi.get(self, "options")

    @property
    @pulumi.getter
    def rules(self) -> Sequence['outputs.GetConfigRuleResult']:
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The time the resource was created, expressed in [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format. Example: `2020-02-12T22:47:12.613Z`
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The time the resource was updated, expressed in [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format. Example: `2020-02-13T22:47:12.613Z`
        """
        return pulumi.get(self, "time_updated")

    @property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a user.
        """
        return pulumi.get(self, "updated_by")


class AwaitableGetConfigResult(GetConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConfigResult(
            apm_domain_id=self.apm_domain_id,
            config_id=self.config_id,
            config_type=self.config_type,
            created_by=self.created_by,
            defined_tags=self.defined_tags,
            description=self.description,
            dimensions=self.dimensions,
            display_name=self.display_name,
            etag=self.etag,
            filter_id=self.filter_id,
            filter_text=self.filter_text,
            freeform_tags=self.freeform_tags,
            group=self.group,
            id=self.id,
            in_use_bies=self.in_use_bies,
            metrics=self.metrics,
            namespace=self.namespace,
            opc_dry_run=self.opc_dry_run,
            options=self.options,
            rules=self.rules,
            time_created=self.time_created,
            time_updated=self.time_updated,
            updated_by=self.updated_by)


def get_config(apm_domain_id: Optional[str] = None,
               config_id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConfigResult:
    """
    This data source provides details about a specific Config resource in Oracle Cloud Infrastructure Apm Config service.

    Gets the configuration item identified by the OCID.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_config = oci.ApmConfig.get_config(apm_domain_id=oci_apm_apm_domain["test_apm_domain"]["id"],
        config_id=oci_apm_config_config["test_config"]["id"])
    ```


    :param str apm_domain_id: The APM Domain ID the request is intended for.
    :param str config_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the configuration item.
    """
    __args__ = dict()
    __args__['apmDomainId'] = apm_domain_id
    __args__['configId'] = config_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:ApmConfig/getConfig:getConfig', __args__, opts=opts, typ=GetConfigResult).value

    return AwaitableGetConfigResult(
        apm_domain_id=pulumi.get(__ret__, 'apm_domain_id'),
        config_id=pulumi.get(__ret__, 'config_id'),
        config_type=pulumi.get(__ret__, 'config_type'),
        created_by=pulumi.get(__ret__, 'created_by'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        description=pulumi.get(__ret__, 'description'),
        dimensions=pulumi.get(__ret__, 'dimensions'),
        display_name=pulumi.get(__ret__, 'display_name'),
        etag=pulumi.get(__ret__, 'etag'),
        filter_id=pulumi.get(__ret__, 'filter_id'),
        filter_text=pulumi.get(__ret__, 'filter_text'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        group=pulumi.get(__ret__, 'group'),
        id=pulumi.get(__ret__, 'id'),
        in_use_bies=pulumi.get(__ret__, 'in_use_bies'),
        metrics=pulumi.get(__ret__, 'metrics'),
        namespace=pulumi.get(__ret__, 'namespace'),
        opc_dry_run=pulumi.get(__ret__, 'opc_dry_run'),
        options=pulumi.get(__ret__, 'options'),
        rules=pulumi.get(__ret__, 'rules'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'),
        updated_by=pulumi.get(__ret__, 'updated_by'))


@_utilities.lift_output_func(get_config)
def get_config_output(apm_domain_id: Optional[pulumi.Input[str]] = None,
                      config_id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConfigResult]:
    """
    This data source provides details about a specific Config resource in Oracle Cloud Infrastructure Apm Config service.

    Gets the configuration item identified by the OCID.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_config = oci.ApmConfig.get_config(apm_domain_id=oci_apm_apm_domain["test_apm_domain"]["id"],
        config_id=oci_apm_config_config["test_config"]["id"])
    ```


    :param str apm_domain_id: The APM Domain ID the request is intended for.
    :param str config_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the configuration item.
    """
    ...
