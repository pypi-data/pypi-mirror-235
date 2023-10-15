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
    'GetObjectsResult',
    'AwaitableGetObjectsResult',
    'get_objects',
    'get_objects_output',
]

@pulumi.output_type
class GetObjectsResult:
    """
    A collection of values returned by getObjects.
    """
    def __init__(__self__, bucket=None, delimiter=None, end=None, filters=None, id=None, namespace=None, objects=None, prefix=None, prefixes=None, start=None, start_after=None):
        if bucket and not isinstance(bucket, str):
            raise TypeError("Expected argument 'bucket' to be a str")
        pulumi.set(__self__, "bucket", bucket)
        if delimiter and not isinstance(delimiter, str):
            raise TypeError("Expected argument 'delimiter' to be a str")
        pulumi.set(__self__, "delimiter", delimiter)
        if end and not isinstance(end, str):
            raise TypeError("Expected argument 'end' to be a str")
        pulumi.set(__self__, "end", end)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if objects and not isinstance(objects, list):
            raise TypeError("Expected argument 'objects' to be a list")
        pulumi.set(__self__, "objects", objects)
        if prefix and not isinstance(prefix, str):
            raise TypeError("Expected argument 'prefix' to be a str")
        pulumi.set(__self__, "prefix", prefix)
        if prefixes and not isinstance(prefixes, list):
            raise TypeError("Expected argument 'prefixes' to be a list")
        pulumi.set(__self__, "prefixes", prefixes)
        if start and not isinstance(start, str):
            raise TypeError("Expected argument 'start' to be a str")
        pulumi.set(__self__, "start", start)
        if start_after and not isinstance(start_after, str):
            raise TypeError("Expected argument 'start_after' to be a str")
        pulumi.set(__self__, "start_after", start_after)

    @property
    @pulumi.getter
    def bucket(self) -> str:
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter
    def delimiter(self) -> Optional[str]:
        return pulumi.get(self, "delimiter")

    @property
    @pulumi.getter
    def end(self) -> Optional[str]:
        return pulumi.get(self, "end")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetObjectsFilterResult']]:
        return pulumi.get(self, "filters")

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
    @pulumi.getter
    def objects(self) -> Sequence['outputs.GetObjectsObjectResult']:
        """
        The list of list_objects.
        """
        return pulumi.get(self, "objects")

    @property
    @pulumi.getter
    def prefix(self) -> Optional[str]:
        return pulumi.get(self, "prefix")

    @property
    @pulumi.getter
    def prefixes(self) -> Sequence[str]:
        return pulumi.get(self, "prefixes")

    @property
    @pulumi.getter
    def start(self) -> Optional[str]:
        return pulumi.get(self, "start")

    @property
    @pulumi.getter(name="startAfter")
    def start_after(self) -> Optional[str]:
        return pulumi.get(self, "start_after")


class AwaitableGetObjectsResult(GetObjectsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetObjectsResult(
            bucket=self.bucket,
            delimiter=self.delimiter,
            end=self.end,
            filters=self.filters,
            id=self.id,
            namespace=self.namespace,
            objects=self.objects,
            prefix=self.prefix,
            prefixes=self.prefixes,
            start=self.start,
            start_after=self.start_after)


def get_objects(bucket: Optional[str] = None,
                delimiter: Optional[str] = None,
                end: Optional[str] = None,
                filters: Optional[Sequence[pulumi.InputType['GetObjectsFilterArgs']]] = None,
                namespace: Optional[str] = None,
                prefix: Optional[str] = None,
                start: Optional[str] = None,
                start_after: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetObjectsResult:
    """
    This data source provides the list of Objects in Oracle Cloud Infrastructure Object Storage service.

    Lists the objects in a bucket. By default, ListObjects returns object names only. See the `fields`
    parameter for other fields that you can optionally include in ListObjects response.

    ListObjects returns at most 1000 objects. To paginate through more objects, use the returned 'nextStartWith'
    value with the 'start' parameter. To filter which objects ListObjects returns, use the 'start' and 'end'
    parameters.

    To use this and other API operations, you must be authorized in an IAM policy. If you are not authorized,
    talk to an administrator. If you are an administrator who needs to write policies to give users access, see
    [Getting Started with Policies](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).


    :param str bucket: The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`
    :param str delimiter: When this parameter is set, only objects whose names do not contain the delimiter character (after an optionally specified prefix) are returned in the objects key of the response body. Scanned objects whose names contain the delimiter have the part of their name up to the first occurrence of the delimiter (including the optional prefix) returned as a set of prefixes. Note that only '/' is a supported delimiter character at this time.
    :param str end: Object names returned by a list query must be strictly less than this parameter.
    :param str namespace: The Object Storage namespace used for the request.
    :param str prefix: The string to use for matching against the start of object names in a list query.
    :param str start: Object names returned by a list query must be greater or equal to this parameter.
    :param str start_after: Object names returned by a list query must be greater than this parameter.
    """
    __args__ = dict()
    __args__['bucket'] = bucket
    __args__['delimiter'] = delimiter
    __args__['end'] = end
    __args__['filters'] = filters
    __args__['namespace'] = namespace
    __args__['prefix'] = prefix
    __args__['start'] = start
    __args__['startAfter'] = start_after
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:ObjectStorage/getObjects:getObjects', __args__, opts=opts, typ=GetObjectsResult).value

    return AwaitableGetObjectsResult(
        bucket=pulumi.get(__ret__, 'bucket'),
        delimiter=pulumi.get(__ret__, 'delimiter'),
        end=pulumi.get(__ret__, 'end'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        namespace=pulumi.get(__ret__, 'namespace'),
        objects=pulumi.get(__ret__, 'objects'),
        prefix=pulumi.get(__ret__, 'prefix'),
        prefixes=pulumi.get(__ret__, 'prefixes'),
        start=pulumi.get(__ret__, 'start'),
        start_after=pulumi.get(__ret__, 'start_after'))


@_utilities.lift_output_func(get_objects)
def get_objects_output(bucket: Optional[pulumi.Input[str]] = None,
                       delimiter: Optional[pulumi.Input[Optional[str]]] = None,
                       end: Optional[pulumi.Input[Optional[str]]] = None,
                       filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetObjectsFilterArgs']]]]] = None,
                       namespace: Optional[pulumi.Input[str]] = None,
                       prefix: Optional[pulumi.Input[Optional[str]]] = None,
                       start: Optional[pulumi.Input[Optional[str]]] = None,
                       start_after: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetObjectsResult]:
    """
    This data source provides the list of Objects in Oracle Cloud Infrastructure Object Storage service.

    Lists the objects in a bucket. By default, ListObjects returns object names only. See the `fields`
    parameter for other fields that you can optionally include in ListObjects response.

    ListObjects returns at most 1000 objects. To paginate through more objects, use the returned 'nextStartWith'
    value with the 'start' parameter. To filter which objects ListObjects returns, use the 'start' and 'end'
    parameters.

    To use this and other API operations, you must be authorized in an IAM policy. If you are not authorized,
    talk to an administrator. If you are an administrator who needs to write policies to give users access, see
    [Getting Started with Policies](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).


    :param str bucket: The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`
    :param str delimiter: When this parameter is set, only objects whose names do not contain the delimiter character (after an optionally specified prefix) are returned in the objects key of the response body. Scanned objects whose names contain the delimiter have the part of their name up to the first occurrence of the delimiter (including the optional prefix) returned as a set of prefixes. Note that only '/' is a supported delimiter character at this time.
    :param str end: Object names returned by a list query must be strictly less than this parameter.
    :param str namespace: The Object Storage namespace used for the request.
    :param str prefix: The string to use for matching against the start of object names in a list query.
    :param str start: Object names returned by a list query must be greater or equal to this parameter.
    :param str start_after: Object names returned by a list query must be greater than this parameter.
    """
    ...
