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
    'GetProfileResult',
    'AwaitableGetProfileResult',
    'get_profile',
    'get_profile_output',
]

@pulumi.output_type
class GetProfileResult:
    """
    A collection of values returned by getProfile.
    """
    def __init__(__self__, aggregation_interval_in_days=None, compartment_id=None, defined_tags=None, description=None, freeform_tags=None, id=None, levels_configurations=None, name=None, profile_id=None, state=None, target_compartments=None, target_tags=None, time_created=None, time_updated=None):
        if aggregation_interval_in_days and not isinstance(aggregation_interval_in_days, int):
            raise TypeError("Expected argument 'aggregation_interval_in_days' to be a int")
        pulumi.set(__self__, "aggregation_interval_in_days", aggregation_interval_in_days)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if levels_configurations and not isinstance(levels_configurations, list):
            raise TypeError("Expected argument 'levels_configurations' to be a list")
        pulumi.set(__self__, "levels_configurations", levels_configurations)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if profile_id and not isinstance(profile_id, str):
            raise TypeError("Expected argument 'profile_id' to be a str")
        pulumi.set(__self__, "profile_id", profile_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if target_compartments and not isinstance(target_compartments, list):
            raise TypeError("Expected argument 'target_compartments' to be a list")
        pulumi.set(__self__, "target_compartments", target_compartments)
        if target_tags and not isinstance(target_tags, list):
            raise TypeError("Expected argument 'target_tags' to be a list")
        pulumi.set(__self__, "target_tags", target_tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)

    @property
    @pulumi.getter(name="aggregationIntervalInDays")
    def aggregation_interval_in_days(self) -> int:
        """
        The time period over which to collect data for the recommendations, measured in number of days.
        """
        return pulumi.get(self, "aggregation_interval_in_days")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the tenancy. The tenancy is the root compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Text describing the profile. Avoid entering confidential information.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Simple key-value pair applied without any predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Exists for cross-compatibility only.  Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The unique OCID of the profile.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="levelsConfigurations")
    def levels_configurations(self) -> Sequence['outputs.GetProfileLevelsConfigurationResult']:
        """
        A list of configuration levels for each recommendation.
        """
        return pulumi.get(self, "levels_configurations")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name assigned to the profile. Avoid entering confidential information.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="profileId")
    def profile_id(self) -> str:
        return pulumi.get(self, "profile_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The profile's current state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="targetCompartments")
    def target_compartments(self) -> Sequence['outputs.GetProfileTargetCompartmentResult']:
        """
        Optional. The compartments specified in the profile override for a recommendation.
        """
        return pulumi.get(self, "target_compartments")

    @property
    @pulumi.getter(name="targetTags")
    def target_tags(self) -> Sequence['outputs.GetProfileTargetTagResult']:
        """
        Optional. The tags specified in the profile override for a recommendation.
        """
        return pulumi.get(self, "target_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the profile was created, in the format defined by RFC3339.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The date and time the profile was last updated, in the format defined by RFC3339.
        """
        return pulumi.get(self, "time_updated")


class AwaitableGetProfileResult(GetProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProfileResult(
            aggregation_interval_in_days=self.aggregation_interval_in_days,
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            description=self.description,
            freeform_tags=self.freeform_tags,
            id=self.id,
            levels_configurations=self.levels_configurations,
            name=self.name,
            profile_id=self.profile_id,
            state=self.state,
            target_compartments=self.target_compartments,
            target_tags=self.target_tags,
            time_created=self.time_created,
            time_updated=self.time_updated)


def get_profile(profile_id: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProfileResult:
    """
    This data source provides details about a specific Profile resource in Oracle Cloud Infrastructure Optimizer service.

    Gets the specified profile's information. Uses the profile's OCID to determine which profile to retrieve.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_profile = oci.Optimizer.get_profile(profile_id=oci_optimizer_profile["test_profile"]["id"])
    ```


    :param str profile_id: The unique OCID of the profile.
    """
    __args__ = dict()
    __args__['profileId'] = profile_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Optimizer/getProfile:getProfile', __args__, opts=opts, typ=GetProfileResult).value

    return AwaitableGetProfileResult(
        aggregation_interval_in_days=pulumi.get(__ret__, 'aggregation_interval_in_days'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        description=pulumi.get(__ret__, 'description'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        levels_configurations=pulumi.get(__ret__, 'levels_configurations'),
        name=pulumi.get(__ret__, 'name'),
        profile_id=pulumi.get(__ret__, 'profile_id'),
        state=pulumi.get(__ret__, 'state'),
        target_compartments=pulumi.get(__ret__, 'target_compartments'),
        target_tags=pulumi.get(__ret__, 'target_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'))


@_utilities.lift_output_func(get_profile)
def get_profile_output(profile_id: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProfileResult]:
    """
    This data source provides details about a specific Profile resource in Oracle Cloud Infrastructure Optimizer service.

    Gets the specified profile's information. Uses the profile's OCID to determine which profile to retrieve.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_profile = oci.Optimizer.get_profile(profile_id=oci_optimizer_profile["test_profile"]["id"])
    ```


    :param str profile_id: The unique OCID of the profile.
    """
    ...
