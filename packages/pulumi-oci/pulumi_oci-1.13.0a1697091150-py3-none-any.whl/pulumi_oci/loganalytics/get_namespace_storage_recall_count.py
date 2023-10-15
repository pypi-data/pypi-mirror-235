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
    'GetNamespaceStorageRecallCountResult',
    'AwaitableGetNamespaceStorageRecallCountResult',
    'get_namespace_storage_recall_count',
    'get_namespace_storage_recall_count_output',
]

@pulumi.output_type
class GetNamespaceStorageRecallCountResult:
    """
    A collection of values returned by getNamespaceStorageRecallCount.
    """
    def __init__(__self__, id=None, namespace=None, recall_count=None, recall_failed=None, recall_limit=None, recall_pending=None, recall_succeeded=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if recall_count and not isinstance(recall_count, int):
            raise TypeError("Expected argument 'recall_count' to be a int")
        pulumi.set(__self__, "recall_count", recall_count)
        if recall_failed and not isinstance(recall_failed, int):
            raise TypeError("Expected argument 'recall_failed' to be a int")
        pulumi.set(__self__, "recall_failed", recall_failed)
        if recall_limit and not isinstance(recall_limit, int):
            raise TypeError("Expected argument 'recall_limit' to be a int")
        pulumi.set(__self__, "recall_limit", recall_limit)
        if recall_pending and not isinstance(recall_pending, int):
            raise TypeError("Expected argument 'recall_pending' to be a int")
        pulumi.set(__self__, "recall_pending", recall_pending)
        if recall_succeeded and not isinstance(recall_succeeded, int):
            raise TypeError("Expected argument 'recall_succeeded' to be a int")
        pulumi.set(__self__, "recall_succeeded", recall_succeeded)

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

    @property
    @pulumi.getter(name="recallCount")
    def recall_count(self) -> int:
        """
        This is the total number of recalls made so far
        """
        return pulumi.get(self, "recall_count")

    @property
    @pulumi.getter(name="recallFailed")
    def recall_failed(self) -> int:
        """
        This is the number of recalls that failed
        """
        return pulumi.get(self, "recall_failed")

    @property
    @pulumi.getter(name="recallLimit")
    def recall_limit(self) -> int:
        """
        This is the maximum number of recalls (including successful and pending recalls) allowed
        """
        return pulumi.get(self, "recall_limit")

    @property
    @pulumi.getter(name="recallPending")
    def recall_pending(self) -> int:
        """
        This is the number of recalls in pending state
        """
        return pulumi.get(self, "recall_pending")

    @property
    @pulumi.getter(name="recallSucceeded")
    def recall_succeeded(self) -> int:
        """
        This is the number of recalls that succeeded
        """
        return pulumi.get(self, "recall_succeeded")


class AwaitableGetNamespaceStorageRecallCountResult(GetNamespaceStorageRecallCountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNamespaceStorageRecallCountResult(
            id=self.id,
            namespace=self.namespace,
            recall_count=self.recall_count,
            recall_failed=self.recall_failed,
            recall_limit=self.recall_limit,
            recall_pending=self.recall_pending,
            recall_succeeded=self.recall_succeeded)


def get_namespace_storage_recall_count(namespace: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNamespaceStorageRecallCountResult:
    """
    This data source provides details about a specific Namespace Storage Recall Count resource in Oracle Cloud Infrastructure Log Analytics service.

    This API gets the number of recalls made and the maximum recalls that can be made

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_namespace_storage_recall_count = oci.LogAnalytics.get_namespace_storage_recall_count(namespace=var["namespace_storage_recall_count_namespace"])
    ```


    :param str namespace: The Logging Analytics namespace used for the request.
    """
    __args__ = dict()
    __args__['namespace'] = namespace
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:LogAnalytics/getNamespaceStorageRecallCount:getNamespaceStorageRecallCount', __args__, opts=opts, typ=GetNamespaceStorageRecallCountResult).value

    return AwaitableGetNamespaceStorageRecallCountResult(
        id=pulumi.get(__ret__, 'id'),
        namespace=pulumi.get(__ret__, 'namespace'),
        recall_count=pulumi.get(__ret__, 'recall_count'),
        recall_failed=pulumi.get(__ret__, 'recall_failed'),
        recall_limit=pulumi.get(__ret__, 'recall_limit'),
        recall_pending=pulumi.get(__ret__, 'recall_pending'),
        recall_succeeded=pulumi.get(__ret__, 'recall_succeeded'))


@_utilities.lift_output_func(get_namespace_storage_recall_count)
def get_namespace_storage_recall_count_output(namespace: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNamespaceStorageRecallCountResult]:
    """
    This data source provides details about a specific Namespace Storage Recall Count resource in Oracle Cloud Infrastructure Log Analytics service.

    This API gets the number of recalls made and the maximum recalls that can be made

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_namespace_storage_recall_count = oci.LogAnalytics.get_namespace_storage_recall_count(namespace=var["namespace_storage_recall_count_namespace"])
    ```


    :param str namespace: The Logging Analytics namespace used for the request.
    """
    ...
