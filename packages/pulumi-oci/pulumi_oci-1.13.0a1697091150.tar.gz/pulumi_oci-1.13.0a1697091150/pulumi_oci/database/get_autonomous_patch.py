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
    'GetAutonomousPatchResult',
    'AwaitableGetAutonomousPatchResult',
    'get_autonomous_patch',
    'get_autonomous_patch_output',
]

@pulumi.output_type
class GetAutonomousPatchResult:
    """
    A collection of values returned by getAutonomousPatch.
    """
    def __init__(__self__, autonomous_patch_id=None, description=None, id=None, lifecycle_details=None, patch_model=None, quarter=None, state=None, time_released=None, type=None, version=None, year=None):
        if autonomous_patch_id and not isinstance(autonomous_patch_id, str):
            raise TypeError("Expected argument 'autonomous_patch_id' to be a str")
        pulumi.set(__self__, "autonomous_patch_id", autonomous_patch_id)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if patch_model and not isinstance(patch_model, str):
            raise TypeError("Expected argument 'patch_model' to be a str")
        pulumi.set(__self__, "patch_model", patch_model)
        if quarter and not isinstance(quarter, str):
            raise TypeError("Expected argument 'quarter' to be a str")
        pulumi.set(__self__, "quarter", quarter)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if time_released and not isinstance(time_released, str):
            raise TypeError("Expected argument 'time_released' to be a str")
        pulumi.set(__self__, "time_released", time_released)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)
        if year and not isinstance(year, str):
            raise TypeError("Expected argument 'year' to be a str")
        pulumi.set(__self__, "year", year)

    @property
    @pulumi.getter(name="autonomousPatchId")
    def autonomous_patch_id(self) -> str:
        return pulumi.get(self, "autonomous_patch_id")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The text describing this patch package.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        A descriptive text associated with the lifecycleState. Typically can contain additional displayable text.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="patchModel")
    def patch_model(self) -> str:
        """
        Database patching model preference. See [My Oracle Support note 2285040.1](https://support.oracle.com/rs?type=doc&id=2285040.1) for information on the Release Update (RU) and Release Update Revision (RUR) patching models.
        """
        return pulumi.get(self, "patch_model")

    @property
    @pulumi.getter
    def quarter(self) -> str:
        """
        First month of the quarter in which the patch was released.
        """
        return pulumi.get(self, "quarter")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the patch as a result of lastAction.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeReleased")
    def time_released(self) -> str:
        """
        The date and time that the patch was released.
        """
        return pulumi.get(self, "time_released")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of patch. BUNDLE is one example.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        The version of this patch package.
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter
    def year(self) -> str:
        """
        Year in which the patch was released.
        """
        return pulumi.get(self, "year")


class AwaitableGetAutonomousPatchResult(GetAutonomousPatchResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAutonomousPatchResult(
            autonomous_patch_id=self.autonomous_patch_id,
            description=self.description,
            id=self.id,
            lifecycle_details=self.lifecycle_details,
            patch_model=self.patch_model,
            quarter=self.quarter,
            state=self.state,
            time_released=self.time_released,
            type=self.type,
            version=self.version,
            year=self.year)


def get_autonomous_patch(autonomous_patch_id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAutonomousPatchResult:
    """
    This data source provides details about a specific Autonomous Patch resource in Oracle Cloud Infrastructure Database service.

    Gets information about a specific autonomous patch.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_autonomous_patch = oci.Database.get_autonomous_patch(autonomous_patch_id=oci_database_autonomous_patch["test_autonomous_patch"]["id"])
    ```


    :param str autonomous_patch_id: The autonomous patch [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    """
    __args__ = dict()
    __args__['autonomousPatchId'] = autonomous_patch_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Database/getAutonomousPatch:getAutonomousPatch', __args__, opts=opts, typ=GetAutonomousPatchResult).value

    return AwaitableGetAutonomousPatchResult(
        autonomous_patch_id=pulumi.get(__ret__, 'autonomous_patch_id'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        patch_model=pulumi.get(__ret__, 'patch_model'),
        quarter=pulumi.get(__ret__, 'quarter'),
        state=pulumi.get(__ret__, 'state'),
        time_released=pulumi.get(__ret__, 'time_released'),
        type=pulumi.get(__ret__, 'type'),
        version=pulumi.get(__ret__, 'version'),
        year=pulumi.get(__ret__, 'year'))


@_utilities.lift_output_func(get_autonomous_patch)
def get_autonomous_patch_output(autonomous_patch_id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAutonomousPatchResult]:
    """
    This data source provides details about a specific Autonomous Patch resource in Oracle Cloud Infrastructure Database service.

    Gets information about a specific autonomous patch.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_autonomous_patch = oci.Database.get_autonomous_patch(autonomous_patch_id=oci_database_autonomous_patch["test_autonomous_patch"]["id"])
    ```


    :param str autonomous_patch_id: The autonomous patch [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    """
    ...
