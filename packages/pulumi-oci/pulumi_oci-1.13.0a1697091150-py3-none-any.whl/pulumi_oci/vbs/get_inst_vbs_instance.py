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
    'GetInstVbsInstanceResult',
    'AwaitableGetInstVbsInstanceResult',
    'get_inst_vbs_instance',
    'get_inst_vbs_instance_output',
]

@pulumi.output_type
class GetInstVbsInstanceResult:
    """
    A collection of values returned by getInstVbsInstance.
    """
    def __init__(__self__, compartment_id=None, defined_tags=None, display_name=None, freeform_tags=None, id=None, idcs_access_token=None, is_resource_usage_agreement_granted=None, lifecyle_details=None, name=None, resource_compartment_id=None, state=None, system_tags=None, time_created=None, time_updated=None, vbs_access_url=None, vbs_instance_id=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if idcs_access_token and not isinstance(idcs_access_token, str):
            raise TypeError("Expected argument 'idcs_access_token' to be a str")
        pulumi.set(__self__, "idcs_access_token", idcs_access_token)
        if is_resource_usage_agreement_granted and not isinstance(is_resource_usage_agreement_granted, bool):
            raise TypeError("Expected argument 'is_resource_usage_agreement_granted' to be a bool")
        pulumi.set(__self__, "is_resource_usage_agreement_granted", is_resource_usage_agreement_granted)
        if lifecyle_details and not isinstance(lifecyle_details, str):
            raise TypeError("Expected argument 'lifecyle_details' to be a str")
        pulumi.set(__self__, "lifecyle_details", lifecyle_details)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_compartment_id and not isinstance(resource_compartment_id, str):
            raise TypeError("Expected argument 'resource_compartment_id' to be a str")
        pulumi.set(__self__, "resource_compartment_id", resource_compartment_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)
        if vbs_access_url and not isinstance(vbs_access_url, str):
            raise TypeError("Expected argument 'vbs_access_url' to be a str")
        pulumi.set(__self__, "vbs_access_url", vbs_access_url)
        if vbs_instance_id and not isinstance(vbs_instance_id, str):
            raise TypeError("Expected argument 'vbs_instance_id' to be a str")
        pulumi.set(__self__, "vbs_instance_id", vbs_instance_id)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        Compartment of the service instance
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Service instance display name
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Unique identifier that is immutable on creation
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="idcsAccessToken")
    def idcs_access_token(self) -> str:
        return pulumi.get(self, "idcs_access_token")

    @property
    @pulumi.getter(name="isResourceUsageAgreementGranted")
    def is_resource_usage_agreement_granted(self) -> bool:
        """
        Whether the VBS service instance owner explicitly approved VBS to create and use resources in the customer tenancy
        """
        return pulumi.get(self, "is_resource_usage_agreement_granted")

    @property
    @pulumi.getter(name="lifecyleDetails")
    def lifecyle_details(self) -> str:
        """
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        """
        return pulumi.get(self, "lifecyle_details")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Service instance name (unique identifier)
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceCompartmentId")
    def resource_compartment_id(self) -> str:
        """
        Compartment where VBS may create additional resources for the service instance
        """
        return pulumi.get(self, "resource_compartment_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the VbsInstance.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The time the the VbsInstance was created. An RFC3339 formatted datetime string
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The time the VbsInstance was updated. An RFC3339 formatted datetime string
        """
        return pulumi.get(self, "time_updated")

    @property
    @pulumi.getter(name="vbsAccessUrl")
    def vbs_access_url(self) -> str:
        """
        Public web URL for accessing the VBS service instance
        """
        return pulumi.get(self, "vbs_access_url")

    @property
    @pulumi.getter(name="vbsInstanceId")
    def vbs_instance_id(self) -> str:
        return pulumi.get(self, "vbs_instance_id")


class AwaitableGetInstVbsInstanceResult(GetInstVbsInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstVbsInstanceResult(
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            display_name=self.display_name,
            freeform_tags=self.freeform_tags,
            id=self.id,
            idcs_access_token=self.idcs_access_token,
            is_resource_usage_agreement_granted=self.is_resource_usage_agreement_granted,
            lifecyle_details=self.lifecyle_details,
            name=self.name,
            resource_compartment_id=self.resource_compartment_id,
            state=self.state,
            system_tags=self.system_tags,
            time_created=self.time_created,
            time_updated=self.time_updated,
            vbs_access_url=self.vbs_access_url,
            vbs_instance_id=self.vbs_instance_id)


def get_inst_vbs_instance(vbs_instance_id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstVbsInstanceResult:
    """
    This data source provides details about a specific Vbs Instance resource in Oracle Cloud Infrastructure Vbs Inst service.

    Gets a VbsInstance by identifier

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_vbs_instance = oci.Vbs.get_inst_vbs_instance(vbs_instance_id=oci_vbs_inst_vbs_instance["test_vbs_instance"]["id"])
    ```


    :param str vbs_instance_id: unique VbsInstance identifier
    """
    __args__ = dict()
    __args__['vbsInstanceId'] = vbs_instance_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Vbs/getInstVbsInstance:getInstVbsInstance', __args__, opts=opts, typ=GetInstVbsInstanceResult).value

    return AwaitableGetInstVbsInstanceResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        display_name=pulumi.get(__ret__, 'display_name'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        idcs_access_token=pulumi.get(__ret__, 'idcs_access_token'),
        is_resource_usage_agreement_granted=pulumi.get(__ret__, 'is_resource_usage_agreement_granted'),
        lifecyle_details=pulumi.get(__ret__, 'lifecyle_details'),
        name=pulumi.get(__ret__, 'name'),
        resource_compartment_id=pulumi.get(__ret__, 'resource_compartment_id'),
        state=pulumi.get(__ret__, 'state'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'),
        vbs_access_url=pulumi.get(__ret__, 'vbs_access_url'),
        vbs_instance_id=pulumi.get(__ret__, 'vbs_instance_id'))


@_utilities.lift_output_func(get_inst_vbs_instance)
def get_inst_vbs_instance_output(vbs_instance_id: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstVbsInstanceResult]:
    """
    This data source provides details about a specific Vbs Instance resource in Oracle Cloud Infrastructure Vbs Inst service.

    Gets a VbsInstance by identifier

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_vbs_instance = oci.Vbs.get_inst_vbs_instance(vbs_instance_id=oci_vbs_inst_vbs_instance["test_vbs_instance"]["id"])
    ```


    :param str vbs_instance_id: unique VbsInstance identifier
    """
    ...
