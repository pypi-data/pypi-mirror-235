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
    'GetTrailSequencesResult',
    'AwaitableGetTrailSequencesResult',
    'get_trail_sequences',
    'get_trail_sequences_output',
]

@pulumi.output_type
class GetTrailSequencesResult:
    """
    A collection of values returned by getTrailSequences.
    """
    def __init__(__self__, deployment_id=None, display_name=None, filters=None, id=None, trail_file_id=None, trail_sequence_collections=None, trail_sequence_id=None):
        if deployment_id and not isinstance(deployment_id, str):
            raise TypeError("Expected argument 'deployment_id' to be a str")
        pulumi.set(__self__, "deployment_id", deployment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if trail_file_id and not isinstance(trail_file_id, str):
            raise TypeError("Expected argument 'trail_file_id' to be a str")
        pulumi.set(__self__, "trail_file_id", trail_file_id)
        if trail_sequence_collections and not isinstance(trail_sequence_collections, list):
            raise TypeError("Expected argument 'trail_sequence_collections' to be a list")
        pulumi.set(__self__, "trail_sequence_collections", trail_sequence_collections)
        if trail_sequence_id and not isinstance(trail_sequence_id, str):
            raise TypeError("Expected argument 'trail_sequence_id' to be a str")
        pulumi.set(__self__, "trail_sequence_id", trail_sequence_id)

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> str:
        return pulumi.get(self, "deployment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        An object's Display Name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetTrailSequencesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="trailFileId")
    def trail_file_id(self) -> str:
        return pulumi.get(self, "trail_file_id")

    @property
    @pulumi.getter(name="trailSequenceCollections")
    def trail_sequence_collections(self) -> Sequence['outputs.GetTrailSequencesTrailSequenceCollectionResult']:
        """
        The list of trail_sequence_collection.
        """
        return pulumi.get(self, "trail_sequence_collections")

    @property
    @pulumi.getter(name="trailSequenceId")
    def trail_sequence_id(self) -> str:
        return pulumi.get(self, "trail_sequence_id")


class AwaitableGetTrailSequencesResult(GetTrailSequencesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTrailSequencesResult(
            deployment_id=self.deployment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            trail_file_id=self.trail_file_id,
            trail_sequence_collections=self.trail_sequence_collections,
            trail_sequence_id=self.trail_sequence_id)


def get_trail_sequences(deployment_id: Optional[str] = None,
                        display_name: Optional[str] = None,
                        filters: Optional[Sequence[pulumi.InputType['GetTrailSequencesFilterArgs']]] = None,
                        trail_file_id: Optional[str] = None,
                        trail_sequence_id: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTrailSequencesResult:
    """
    This data source provides the list of Trail Sequences in Oracle Cloud Infrastructure Golden Gate service.

    Lists the Trail Sequences for a TrailFile in a given deployment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_trail_sequences = oci.GoldenGate.get_trail_sequences(deployment_id=oci_golden_gate_deployment["test_deployment"]["id"],
        trail_file_id=oci_golden_gate_trail_file["test_trail_file"]["id"],
        display_name=var["trail_sequence_display_name"],
        trail_sequence_id=oci_golden_gate_trail_sequence["test_trail_sequence"]["id"])
    ```


    :param str deployment_id: A unique Deployment identifier.
    :param str display_name: A filter to return only the resources that match the entire 'displayName' given.
    :param str trail_file_id: A Trail File identifier
    :param str trail_sequence_id: A Trail Sequence identifier
    """
    __args__ = dict()
    __args__['deploymentId'] = deployment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['trailFileId'] = trail_file_id
    __args__['trailSequenceId'] = trail_sequence_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:GoldenGate/getTrailSequences:getTrailSequences', __args__, opts=opts, typ=GetTrailSequencesResult).value

    return AwaitableGetTrailSequencesResult(
        deployment_id=pulumi.get(__ret__, 'deployment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        trail_file_id=pulumi.get(__ret__, 'trail_file_id'),
        trail_sequence_collections=pulumi.get(__ret__, 'trail_sequence_collections'),
        trail_sequence_id=pulumi.get(__ret__, 'trail_sequence_id'))


@_utilities.lift_output_func(get_trail_sequences)
def get_trail_sequences_output(deployment_id: Optional[pulumi.Input[str]] = None,
                               display_name: Optional[pulumi.Input[str]] = None,
                               filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetTrailSequencesFilterArgs']]]]] = None,
                               trail_file_id: Optional[pulumi.Input[str]] = None,
                               trail_sequence_id: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTrailSequencesResult]:
    """
    This data source provides the list of Trail Sequences in Oracle Cloud Infrastructure Golden Gate service.

    Lists the Trail Sequences for a TrailFile in a given deployment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_trail_sequences = oci.GoldenGate.get_trail_sequences(deployment_id=oci_golden_gate_deployment["test_deployment"]["id"],
        trail_file_id=oci_golden_gate_trail_file["test_trail_file"]["id"],
        display_name=var["trail_sequence_display_name"],
        trail_sequence_id=oci_golden_gate_trail_sequence["test_trail_sequence"]["id"])
    ```


    :param str deployment_id: A unique Deployment identifier.
    :param str display_name: A filter to return only the resources that match the entire 'displayName' given.
    :param str trail_file_id: A Trail File identifier
    :param str trail_sequence_id: A Trail Sequence identifier
    """
    ...
