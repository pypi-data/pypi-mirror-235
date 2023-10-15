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
    'GetFusionEnvironmentDataMaskingActivityResult',
    'AwaitableGetFusionEnvironmentDataMaskingActivityResult',
    'get_fusion_environment_data_masking_activity',
    'get_fusion_environment_data_masking_activity_output',
]

@pulumi.output_type
class GetFusionEnvironmentDataMaskingActivityResult:
    """
    A collection of values returned by getFusionEnvironmentDataMaskingActivity.
    """
    def __init__(__self__, data_masking_activity_id=None, fusion_environment_id=None, id=None, is_resume_data_masking=None, state=None, time_masking_finish=None, time_masking_start=None):
        if data_masking_activity_id and not isinstance(data_masking_activity_id, str):
            raise TypeError("Expected argument 'data_masking_activity_id' to be a str")
        pulumi.set(__self__, "data_masking_activity_id", data_masking_activity_id)
        if fusion_environment_id and not isinstance(fusion_environment_id, str):
            raise TypeError("Expected argument 'fusion_environment_id' to be a str")
        pulumi.set(__self__, "fusion_environment_id", fusion_environment_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_resume_data_masking and not isinstance(is_resume_data_masking, bool):
            raise TypeError("Expected argument 'is_resume_data_masking' to be a bool")
        pulumi.set(__self__, "is_resume_data_masking", is_resume_data_masking)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if time_masking_finish and not isinstance(time_masking_finish, str):
            raise TypeError("Expected argument 'time_masking_finish' to be a str")
        pulumi.set(__self__, "time_masking_finish", time_masking_finish)
        if time_masking_start and not isinstance(time_masking_start, str):
            raise TypeError("Expected argument 'time_masking_start' to be a str")
        pulumi.set(__self__, "time_masking_start", time_masking_start)

    @property
    @pulumi.getter(name="dataMaskingActivityId")
    def data_masking_activity_id(self) -> str:
        return pulumi.get(self, "data_masking_activity_id")

    @property
    @pulumi.getter(name="fusionEnvironmentId")
    def fusion_environment_id(self) -> str:
        """
        Fusion Environment Identifier.
        """
        return pulumi.get(self, "fusion_environment_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Unique identifier that is immutable on creation.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isResumeDataMasking")
    def is_resume_data_masking(self) -> bool:
        return pulumi.get(self, "is_resume_data_masking")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the DataMaskingActivity.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeMaskingFinish")
    def time_masking_finish(self) -> str:
        """
        The time the data masking activity ended. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_masking_finish")

    @property
    @pulumi.getter(name="timeMaskingStart")
    def time_masking_start(self) -> str:
        """
        The time the data masking activity started. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_masking_start")


class AwaitableGetFusionEnvironmentDataMaskingActivityResult(GetFusionEnvironmentDataMaskingActivityResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFusionEnvironmentDataMaskingActivityResult(
            data_masking_activity_id=self.data_masking_activity_id,
            fusion_environment_id=self.fusion_environment_id,
            id=self.id,
            is_resume_data_masking=self.is_resume_data_masking,
            state=self.state,
            time_masking_finish=self.time_masking_finish,
            time_masking_start=self.time_masking_start)


def get_fusion_environment_data_masking_activity(data_masking_activity_id: Optional[str] = None,
                                                 fusion_environment_id: Optional[str] = None,
                                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFusionEnvironmentDataMaskingActivityResult:
    """
    This data source provides details about a specific Fusion Environment Data Masking Activity resource in Oracle Cloud Infrastructure Fusion Apps service.

    Gets a DataMaskingActivity by identifier

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_fusion_environment_data_masking_activity = oci.Functions.get_fusion_environment_data_masking_activity(data_masking_activity_id=oci_fusion_apps_data_masking_activity["test_data_masking_activity"]["id"],
        fusion_environment_id=oci_fusion_apps_fusion_environment["test_fusion_environment"]["id"])
    ```


    :param str data_masking_activity_id: Unique DataMasking run identifier.
    :param str fusion_environment_id: unique FusionEnvironment identifier
    """
    __args__ = dict()
    __args__['dataMaskingActivityId'] = data_masking_activity_id
    __args__['fusionEnvironmentId'] = fusion_environment_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Functions/getFusionEnvironmentDataMaskingActivity:getFusionEnvironmentDataMaskingActivity', __args__, opts=opts, typ=GetFusionEnvironmentDataMaskingActivityResult).value

    return AwaitableGetFusionEnvironmentDataMaskingActivityResult(
        data_masking_activity_id=pulumi.get(__ret__, 'data_masking_activity_id'),
        fusion_environment_id=pulumi.get(__ret__, 'fusion_environment_id'),
        id=pulumi.get(__ret__, 'id'),
        is_resume_data_masking=pulumi.get(__ret__, 'is_resume_data_masking'),
        state=pulumi.get(__ret__, 'state'),
        time_masking_finish=pulumi.get(__ret__, 'time_masking_finish'),
        time_masking_start=pulumi.get(__ret__, 'time_masking_start'))


@_utilities.lift_output_func(get_fusion_environment_data_masking_activity)
def get_fusion_environment_data_masking_activity_output(data_masking_activity_id: Optional[pulumi.Input[str]] = None,
                                                        fusion_environment_id: Optional[pulumi.Input[str]] = None,
                                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFusionEnvironmentDataMaskingActivityResult]:
    """
    This data source provides details about a specific Fusion Environment Data Masking Activity resource in Oracle Cloud Infrastructure Fusion Apps service.

    Gets a DataMaskingActivity by identifier

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_fusion_environment_data_masking_activity = oci.Functions.get_fusion_environment_data_masking_activity(data_masking_activity_id=oci_fusion_apps_data_masking_activity["test_data_masking_activity"]["id"],
        fusion_environment_id=oci_fusion_apps_fusion_environment["test_fusion_environment"]["id"])
    ```


    :param str data_masking_activity_id: Unique DataMasking run identifier.
    :param str fusion_environment_id: unique FusionEnvironment identifier
    """
    ...
