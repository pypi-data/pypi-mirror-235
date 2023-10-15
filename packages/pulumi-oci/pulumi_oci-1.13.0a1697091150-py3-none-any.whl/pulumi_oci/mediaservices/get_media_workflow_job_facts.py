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
    'GetMediaWorkflowJobFactsResult',
    'AwaitableGetMediaWorkflowJobFactsResult',
    'get_media_workflow_job_facts',
    'get_media_workflow_job_facts_output',
]

@pulumi.output_type
class GetMediaWorkflowJobFactsResult:
    """
    A collection of values returned by getMediaWorkflowJobFacts.
    """
    def __init__(__self__, filters=None, id=None, key=None, media_workflow_job_fact_collections=None, media_workflow_job_id=None, type=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key and not isinstance(key, str):
            raise TypeError("Expected argument 'key' to be a str")
        pulumi.set(__self__, "key", key)
        if media_workflow_job_fact_collections and not isinstance(media_workflow_job_fact_collections, list):
            raise TypeError("Expected argument 'media_workflow_job_fact_collections' to be a list")
        pulumi.set(__self__, "media_workflow_job_fact_collections", media_workflow_job_fact_collections)
        if media_workflow_job_id and not isinstance(media_workflow_job_id, str):
            raise TypeError("Expected argument 'media_workflow_job_id' to be a str")
        pulumi.set(__self__, "media_workflow_job_id", media_workflow_job_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetMediaWorkflowJobFactsFilterResult']]:
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
    def key(self) -> Optional[str]:
        """
        System generated serial number to uniquely identify a detail in order within a MediaWorkflowJob.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="mediaWorkflowJobFactCollections")
    def media_workflow_job_fact_collections(self) -> Sequence['outputs.GetMediaWorkflowJobFactsMediaWorkflowJobFactCollectionResult']:
        """
        The list of media_workflow_job_fact_collection.
        """
        return pulumi.get(self, "media_workflow_job_fact_collections")

    @property
    @pulumi.getter(name="mediaWorkflowJobId")
    def media_workflow_job_id(self) -> str:
        """
        Reference to the parent job.
        """
        return pulumi.get(self, "media_workflow_job_id")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type of information contained in this detail.
        """
        return pulumi.get(self, "type")


class AwaitableGetMediaWorkflowJobFactsResult(GetMediaWorkflowJobFactsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMediaWorkflowJobFactsResult(
            filters=self.filters,
            id=self.id,
            key=self.key,
            media_workflow_job_fact_collections=self.media_workflow_job_fact_collections,
            media_workflow_job_id=self.media_workflow_job_id,
            type=self.type)


def get_media_workflow_job_facts(filters: Optional[Sequence[pulumi.InputType['GetMediaWorkflowJobFactsFilterArgs']]] = None,
                                 key: Optional[str] = None,
                                 media_workflow_job_id: Optional[str] = None,
                                 type: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMediaWorkflowJobFactsResult:
    """
    This data source provides the list of Media Workflow Job Facts in Oracle Cloud Infrastructure Media Services service.

    Internal API to get a point-in-time snapshot of a MediaWorkflowJob.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_media_workflow_job_facts = oci.MediaServices.get_media_workflow_job_facts(media_workflow_job_id=oci_media_services_media_workflow_job["test_media_workflow_job"]["id"],
        key=var["media_workflow_job_fact_key"],
        type=var["media_workflow_job_fact_type"])
    ```


    :param str key: Filter by MediaWorkflowJob ID and MediaWorkflowJobFact key.
    :param str media_workflow_job_id: Unique MediaWorkflowJob identifier.
    :param str type: Types of details to include.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['key'] = key
    __args__['mediaWorkflowJobId'] = media_workflow_job_id
    __args__['type'] = type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:MediaServices/getMediaWorkflowJobFacts:getMediaWorkflowJobFacts', __args__, opts=opts, typ=GetMediaWorkflowJobFactsResult).value

    return AwaitableGetMediaWorkflowJobFactsResult(
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        key=pulumi.get(__ret__, 'key'),
        media_workflow_job_fact_collections=pulumi.get(__ret__, 'media_workflow_job_fact_collections'),
        media_workflow_job_id=pulumi.get(__ret__, 'media_workflow_job_id'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_media_workflow_job_facts)
def get_media_workflow_job_facts_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetMediaWorkflowJobFactsFilterArgs']]]]] = None,
                                        key: Optional[pulumi.Input[Optional[str]]] = None,
                                        media_workflow_job_id: Optional[pulumi.Input[str]] = None,
                                        type: Optional[pulumi.Input[Optional[str]]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMediaWorkflowJobFactsResult]:
    """
    This data source provides the list of Media Workflow Job Facts in Oracle Cloud Infrastructure Media Services service.

    Internal API to get a point-in-time snapshot of a MediaWorkflowJob.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_media_workflow_job_facts = oci.MediaServices.get_media_workflow_job_facts(media_workflow_job_id=oci_media_services_media_workflow_job["test_media_workflow_job"]["id"],
        key=var["media_workflow_job_fact_key"],
        type=var["media_workflow_job_fact_type"])
    ```


    :param str key: Filter by MediaWorkflowJob ID and MediaWorkflowJobFact key.
    :param str media_workflow_job_id: Unique MediaWorkflowJob identifier.
    :param str type: Types of details to include.
    """
    ...
