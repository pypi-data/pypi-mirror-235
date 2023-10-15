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
    'GetNamespaceStorageRecalledDataSizeResult',
    'AwaitableGetNamespaceStorageRecalledDataSizeResult',
    'get_namespace_storage_recalled_data_size',
    'get_namespace_storage_recalled_data_size_output',
]

@pulumi.output_type
class GetNamespaceStorageRecalledDataSizeResult:
    """
    A collection of values returned by getNamespaceStorageRecalledDataSize.
    """
    def __init__(__self__, id=None, namespace=None, not_recalled_data_in_bytes=None, recalled_data_in_bytes=None, time_data_ended=None, time_data_started=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if not_recalled_data_in_bytes and not isinstance(not_recalled_data_in_bytes, str):
            raise TypeError("Expected argument 'not_recalled_data_in_bytes' to be a str")
        pulumi.set(__self__, "not_recalled_data_in_bytes", not_recalled_data_in_bytes)
        if recalled_data_in_bytes and not isinstance(recalled_data_in_bytes, str):
            raise TypeError("Expected argument 'recalled_data_in_bytes' to be a str")
        pulumi.set(__self__, "recalled_data_in_bytes", recalled_data_in_bytes)
        if time_data_ended and not isinstance(time_data_ended, str):
            raise TypeError("Expected argument 'time_data_ended' to be a str")
        pulumi.set(__self__, "time_data_ended", time_data_ended)
        if time_data_started and not isinstance(time_data_started, str):
            raise TypeError("Expected argument 'time_data_started' to be a str")
        pulumi.set(__self__, "time_data_started", time_data_started)

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
    @pulumi.getter(name="notRecalledDataInBytes")
    def not_recalled_data_in_bytes(self) -> str:
        """
        This is the size of the archival data not recalled yet
        """
        return pulumi.get(self, "not_recalled_data_in_bytes")

    @property
    @pulumi.getter(name="recalledDataInBytes")
    def recalled_data_in_bytes(self) -> str:
        """
        This is the size of the recalled data
        """
        return pulumi.get(self, "recalled_data_in_bytes")

    @property
    @pulumi.getter(name="timeDataEnded")
    def time_data_ended(self) -> str:
        """
        This is the end of the time range of the archival data
        """
        return pulumi.get(self, "time_data_ended")

    @property
    @pulumi.getter(name="timeDataStarted")
    def time_data_started(self) -> str:
        """
        This is the start of the time range of the archival data
        """
        return pulumi.get(self, "time_data_started")


class AwaitableGetNamespaceStorageRecalledDataSizeResult(GetNamespaceStorageRecalledDataSizeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNamespaceStorageRecalledDataSizeResult(
            id=self.id,
            namespace=self.namespace,
            not_recalled_data_in_bytes=self.not_recalled_data_in_bytes,
            recalled_data_in_bytes=self.recalled_data_in_bytes,
            time_data_ended=self.time_data_ended,
            time_data_started=self.time_data_started)


def get_namespace_storage_recalled_data_size(namespace: Optional[str] = None,
                                             time_data_ended: Optional[str] = None,
                                             time_data_started: Optional[str] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNamespaceStorageRecalledDataSizeResult:
    """
    This data source provides details about a specific Namespace Storage Recalled Data Size resource in Oracle Cloud Infrastructure Log Analytics service.

    This API gets the datasize of recalls for a given timeframe

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_namespace_storage_recalled_data_size = oci.LogAnalytics.get_namespace_storage_recalled_data_size(namespace=var["namespace_storage_recalled_data_size_namespace"],
        time_data_ended=var["namespace_storage_recalled_data_size_time_data_ended"],
        time_data_started=var["namespace_storage_recalled_data_size_time_data_started"])
    ```


    :param str namespace: The Logging Analytics namespace used for the request.
    :param str time_data_ended: This is the end of the time range for recalled data
    :param str time_data_started: This is the start of the time range for recalled data
    """
    __args__ = dict()
    __args__['namespace'] = namespace
    __args__['timeDataEnded'] = time_data_ended
    __args__['timeDataStarted'] = time_data_started
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:LogAnalytics/getNamespaceStorageRecalledDataSize:getNamespaceStorageRecalledDataSize', __args__, opts=opts, typ=GetNamespaceStorageRecalledDataSizeResult).value

    return AwaitableGetNamespaceStorageRecalledDataSizeResult(
        id=pulumi.get(__ret__, 'id'),
        namespace=pulumi.get(__ret__, 'namespace'),
        not_recalled_data_in_bytes=pulumi.get(__ret__, 'not_recalled_data_in_bytes'),
        recalled_data_in_bytes=pulumi.get(__ret__, 'recalled_data_in_bytes'),
        time_data_ended=pulumi.get(__ret__, 'time_data_ended'),
        time_data_started=pulumi.get(__ret__, 'time_data_started'))


@_utilities.lift_output_func(get_namespace_storage_recalled_data_size)
def get_namespace_storage_recalled_data_size_output(namespace: Optional[pulumi.Input[str]] = None,
                                                    time_data_ended: Optional[pulumi.Input[Optional[str]]] = None,
                                                    time_data_started: Optional[pulumi.Input[Optional[str]]] = None,
                                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNamespaceStorageRecalledDataSizeResult]:
    """
    This data source provides details about a specific Namespace Storage Recalled Data Size resource in Oracle Cloud Infrastructure Log Analytics service.

    This API gets the datasize of recalls for a given timeframe

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_namespace_storage_recalled_data_size = oci.LogAnalytics.get_namespace_storage_recalled_data_size(namespace=var["namespace_storage_recalled_data_size_namespace"],
        time_data_ended=var["namespace_storage_recalled_data_size_time_data_ended"],
        time_data_started=var["namespace_storage_recalled_data_size_time_data_started"])
    ```


    :param str namespace: The Logging Analytics namespace used for the request.
    :param str time_data_ended: This is the end of the time range for recalled data
    :param str time_data_started: This is the start of the time range for recalled data
    """
    ...
