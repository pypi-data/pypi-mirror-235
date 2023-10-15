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
    'GetSdmMaskingPolicyDifferenceResult',
    'AwaitableGetSdmMaskingPolicyDifferenceResult',
    'get_sdm_masking_policy_difference',
    'get_sdm_masking_policy_difference_output',
]

@pulumi.output_type
class GetSdmMaskingPolicyDifferenceResult:
    """
    A collection of values returned by getSdmMaskingPolicyDifference.
    """
    def __init__(__self__, compartment_id=None, defined_tags=None, difference_type=None, display_name=None, freeform_tags=None, id=None, masking_policy_id=None, sdm_masking_policy_difference_id=None, sensitive_data_model_id=None, state=None, system_tags=None, time_created=None, time_creation_started=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if difference_type and not isinstance(difference_type, str):
            raise TypeError("Expected argument 'difference_type' to be a str")
        pulumi.set(__self__, "difference_type", difference_type)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if masking_policy_id and not isinstance(masking_policy_id, str):
            raise TypeError("Expected argument 'masking_policy_id' to be a str")
        pulumi.set(__self__, "masking_policy_id", masking_policy_id)
        if sdm_masking_policy_difference_id and not isinstance(sdm_masking_policy_difference_id, str):
            raise TypeError("Expected argument 'sdm_masking_policy_difference_id' to be a str")
        pulumi.set(__self__, "sdm_masking_policy_difference_id", sdm_masking_policy_difference_id)
        if sensitive_data_model_id and not isinstance(sensitive_data_model_id, str):
            raise TypeError("Expected argument 'sensitive_data_model_id' to be a str")
        pulumi.set(__self__, "sensitive_data_model_id", sensitive_data_model_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_creation_started and not isinstance(time_creation_started, str):
            raise TypeError("Expected argument 'time_creation_started' to be a str")
        pulumi.set(__self__, "time_creation_started", time_creation_started)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment that contains the SDM masking policy difference.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="differenceType")
    def difference_type(self) -> str:
        """
        The type of the SDM masking policy difference. It defines the difference scope. NEW identifies new sensitive columns in the sensitive data model that are not in the masking policy. DELETED identifies columns that are present in the masking policy but have been deleted from the sensitive data model. MODIFIED identifies columns that are present in the sensitive data model as well as the masking policy but some of their attributes have been modified. ALL covers all the above three scenarios and reports new, deleted and modified columns.
        """
        return pulumi.get(self, "difference_type")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name of the SDM masking policy difference.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The OCID of the SDM masking policy difference.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="maskingPolicyId")
    def masking_policy_id(self) -> str:
        """
        The OCID of the masking policy associated with the SDM masking policy difference.
        """
        return pulumi.get(self, "masking_policy_id")

    @property
    @pulumi.getter(name="sdmMaskingPolicyDifferenceId")
    def sdm_masking_policy_difference_id(self) -> str:
        return pulumi.get(self, "sdm_masking_policy_difference_id")

    @property
    @pulumi.getter(name="sensitiveDataModelId")
    def sensitive_data_model_id(self) -> str:
        """
        The OCID of the sensitive data model associated with the SDM masking policy difference.
        """
        return pulumi.get(self, "sensitive_data_model_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the SDM masking policy difference.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the SDM masking policy difference was created, in the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339).
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeCreationStarted")
    def time_creation_started(self) -> str:
        """
        The date and time the SDM masking policy difference creation started, in the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339).
        """
        return pulumi.get(self, "time_creation_started")


class AwaitableGetSdmMaskingPolicyDifferenceResult(GetSdmMaskingPolicyDifferenceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSdmMaskingPolicyDifferenceResult(
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            difference_type=self.difference_type,
            display_name=self.display_name,
            freeform_tags=self.freeform_tags,
            id=self.id,
            masking_policy_id=self.masking_policy_id,
            sdm_masking_policy_difference_id=self.sdm_masking_policy_difference_id,
            sensitive_data_model_id=self.sensitive_data_model_id,
            state=self.state,
            system_tags=self.system_tags,
            time_created=self.time_created,
            time_creation_started=self.time_creation_started)


def get_sdm_masking_policy_difference(sdm_masking_policy_difference_id: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSdmMaskingPolicyDifferenceResult:
    """
    This data source provides details about a specific Sdm Masking Policy Difference resource in Oracle Cloud Infrastructure Data Safe service.

    Gets the details of the specified SDM Masking policy difference.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_sdm_masking_policy_difference = oci.DataSafe.get_sdm_masking_policy_difference(sdm_masking_policy_difference_id=oci_data_safe_sdm_masking_policy_difference["test_sdm_masking_policy_difference"]["id"])
    ```


    :param str sdm_masking_policy_difference_id: The OCID of the SDM masking policy difference.
    """
    __args__ = dict()
    __args__['sdmMaskingPolicyDifferenceId'] = sdm_masking_policy_difference_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataSafe/getSdmMaskingPolicyDifference:getSdmMaskingPolicyDifference', __args__, opts=opts, typ=GetSdmMaskingPolicyDifferenceResult).value

    return AwaitableGetSdmMaskingPolicyDifferenceResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        difference_type=pulumi.get(__ret__, 'difference_type'),
        display_name=pulumi.get(__ret__, 'display_name'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        masking_policy_id=pulumi.get(__ret__, 'masking_policy_id'),
        sdm_masking_policy_difference_id=pulumi.get(__ret__, 'sdm_masking_policy_difference_id'),
        sensitive_data_model_id=pulumi.get(__ret__, 'sensitive_data_model_id'),
        state=pulumi.get(__ret__, 'state'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_creation_started=pulumi.get(__ret__, 'time_creation_started'))


@_utilities.lift_output_func(get_sdm_masking_policy_difference)
def get_sdm_masking_policy_difference_output(sdm_masking_policy_difference_id: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSdmMaskingPolicyDifferenceResult]:
    """
    This data source provides details about a specific Sdm Masking Policy Difference resource in Oracle Cloud Infrastructure Data Safe service.

    Gets the details of the specified SDM Masking policy difference.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_sdm_masking_policy_difference = oci.DataSafe.get_sdm_masking_policy_difference(sdm_masking_policy_difference_id=oci_data_safe_sdm_masking_policy_difference["test_sdm_masking_policy_difference"]["id"])
    ```


    :param str sdm_masking_policy_difference_id: The OCID of the SDM masking policy difference.
    """
    ...
