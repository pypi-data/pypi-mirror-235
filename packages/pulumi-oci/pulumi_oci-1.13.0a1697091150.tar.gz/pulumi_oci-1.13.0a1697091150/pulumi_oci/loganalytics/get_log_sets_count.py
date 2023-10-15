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
    'GetLogSetsCountResult',
    'AwaitableGetLogSetsCountResult',
    'get_log_sets_count',
    'get_log_sets_count_output',
]

@pulumi.output_type
class GetLogSetsCountResult:
    """
    A collection of values returned by getLogSetsCount.
    """
    def __init__(__self__, id=None, log_sets_count=None, namespace=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if log_sets_count and not isinstance(log_sets_count, str):
            raise TypeError("Expected argument 'log_sets_count' to be a str")
        pulumi.set(__self__, "log_sets_count", log_sets_count)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="logSetsCount")
    def log_sets_count(self) -> str:
        """
        This is the total number of log sets the tenancy has configured.
        """
        return pulumi.get(self, "log_sets_count")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        return pulumi.get(self, "namespace")


class AwaitableGetLogSetsCountResult(GetLogSetsCountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLogSetsCountResult(
            id=self.id,
            log_sets_count=self.log_sets_count,
            namespace=self.namespace)


def get_log_sets_count(namespace: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLogSetsCountResult:
    """
    This data source provides details about a specific Log Sets Count resource in Oracle Cloud Infrastructure Log Analytics service.

    This API returns the count of distinct log sets.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_log_sets_count = oci.LogAnalytics.get_log_sets_count(namespace=var["log_sets_count_namespace"])
    ```


    :param str namespace: The Logging Analytics namespace used for the request.
    """
    __args__ = dict()
    __args__['namespace'] = namespace
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:LogAnalytics/getLogSetsCount:getLogSetsCount', __args__, opts=opts, typ=GetLogSetsCountResult).value

    return AwaitableGetLogSetsCountResult(
        id=pulumi.get(__ret__, 'id'),
        log_sets_count=pulumi.get(__ret__, 'log_sets_count'),
        namespace=pulumi.get(__ret__, 'namespace'))


@_utilities.lift_output_func(get_log_sets_count)
def get_log_sets_count_output(namespace: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLogSetsCountResult]:
    """
    This data source provides details about a specific Log Sets Count resource in Oracle Cloud Infrastructure Log Analytics service.

    This API returns the count of distinct log sets.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_log_sets_count = oci.LogAnalytics.get_log_sets_count(namespace=var["log_sets_count_namespace"])
    ```


    :param str namespace: The Logging Analytics namespace used for the request.
    """
    ...
