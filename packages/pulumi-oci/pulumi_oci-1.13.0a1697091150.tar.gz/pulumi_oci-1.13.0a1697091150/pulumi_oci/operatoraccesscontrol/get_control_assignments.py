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
    'GetControlAssignmentsResult',
    'AwaitableGetControlAssignmentsResult',
    'get_control_assignments',
    'get_control_assignments_output',
]

@pulumi.output_type
class GetControlAssignmentsResult:
    """
    A collection of values returned by getControlAssignments.
    """
    def __init__(__self__, compartment_id=None, filters=None, id=None, operator_control_assignment_collections=None, operator_control_name=None, resource_name=None, resource_type=None, state=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if operator_control_assignment_collections and not isinstance(operator_control_assignment_collections, list):
            raise TypeError("Expected argument 'operator_control_assignment_collections' to be a list")
        pulumi.set(__self__, "operator_control_assignment_collections", operator_control_assignment_collections)
        if operator_control_name and not isinstance(operator_control_name, str):
            raise TypeError("Expected argument 'operator_control_name' to be a str")
        pulumi.set(__self__, "operator_control_name", operator_control_name)
        if resource_name and not isinstance(resource_name, str):
            raise TypeError("Expected argument 'resource_name' to be a str")
        pulumi.set(__self__, "resource_name", resource_name)
        if resource_type and not isinstance(resource_type, str):
            raise TypeError("Expected argument 'resource_type' to be a str")
        pulumi.set(__self__, "resource_type", resource_type)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the comparment that contains the operator control assignment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetControlAssignmentsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="operatorControlAssignmentCollections")
    def operator_control_assignment_collections(self) -> Sequence['outputs.GetControlAssignmentsOperatorControlAssignmentCollectionResult']:
        """
        The list of operator_control_assignment_collection.
        """
        return pulumi.get(self, "operator_control_assignment_collections")

    @property
    @pulumi.getter(name="operatorControlName")
    def operator_control_name(self) -> Optional[str]:
        return pulumi.get(self, "operator_control_name")

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[str]:
        """
        Name of the target resource.
        """
        return pulumi.get(self, "resource_name")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[str]:
        """
        resourceType for which the OperatorControlAssignment is applicable
        """
        return pulumi.get(self, "resource_type")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current lifcycle state of the OperatorControl.
        """
        return pulumi.get(self, "state")


class AwaitableGetControlAssignmentsResult(GetControlAssignmentsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetControlAssignmentsResult(
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            operator_control_assignment_collections=self.operator_control_assignment_collections,
            operator_control_name=self.operator_control_name,
            resource_name=self.resource_name,
            resource_type=self.resource_type,
            state=self.state)


def get_control_assignments(compartment_id: Optional[str] = None,
                            filters: Optional[Sequence[pulumi.InputType['GetControlAssignmentsFilterArgs']]] = None,
                            operator_control_name: Optional[str] = None,
                            resource_name: Optional[str] = None,
                            resource_type: Optional[str] = None,
                            state: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetControlAssignmentsResult:
    """
    This data source provides the list of Operator Control Assignments in Oracle Cloud Infrastructure Operator Access Control service.

    Lists all Operator Control Assignments.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_operator_control_assignments = oci.OperatorAccessControl.get_control_assignments(compartment_id=var["compartment_id"],
        operator_control_name=oci_operator_access_control_operator_control["test_operator_control"]["name"],
        resource_name=var["operator_control_assignment_resource_name"],
        resource_type=var["operator_control_assignment_resource_type"],
        state=var["operator_control_assignment_state"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str operator_control_name: A filter to return OperatorControl that match the given operatorControlName.
    :param str resource_name: A filter to return only resources that match the given ResourceName.
    :param str resource_type: A filter to return only lists of resources that match the entire given service type.
    :param str state: A filter to return only resources whose lifecycleState matches the given OperatorControlAssignment lifecycleState.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['operatorControlName'] = operator_control_name
    __args__['resourceName'] = resource_name
    __args__['resourceType'] = resource_type
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:OperatorAccessControl/getControlAssignments:getControlAssignments', __args__, opts=opts, typ=GetControlAssignmentsResult).value

    return AwaitableGetControlAssignmentsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        operator_control_assignment_collections=pulumi.get(__ret__, 'operator_control_assignment_collections'),
        operator_control_name=pulumi.get(__ret__, 'operator_control_name'),
        resource_name=pulumi.get(__ret__, 'resource_name'),
        resource_type=pulumi.get(__ret__, 'resource_type'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_control_assignments)
def get_control_assignments_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                   filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetControlAssignmentsFilterArgs']]]]] = None,
                                   operator_control_name: Optional[pulumi.Input[Optional[str]]] = None,
                                   resource_name: Optional[pulumi.Input[Optional[str]]] = None,
                                   resource_type: Optional[pulumi.Input[Optional[str]]] = None,
                                   state: Optional[pulumi.Input[Optional[str]]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetControlAssignmentsResult]:
    """
    This data source provides the list of Operator Control Assignments in Oracle Cloud Infrastructure Operator Access Control service.

    Lists all Operator Control Assignments.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_operator_control_assignments = oci.OperatorAccessControl.get_control_assignments(compartment_id=var["compartment_id"],
        operator_control_name=oci_operator_access_control_operator_control["test_operator_control"]["name"],
        resource_name=var["operator_control_assignment_resource_name"],
        resource_type=var["operator_control_assignment_resource_type"],
        state=var["operator_control_assignment_state"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str operator_control_name: A filter to return OperatorControl that match the given operatorControlName.
    :param str resource_name: A filter to return only resources that match the given ResourceName.
    :param str resource_type: A filter to return only lists of resources that match the entire given service type.
    :param str state: A filter to return only resources whose lifecycleState matches the given OperatorControlAssignment lifecycleState.
    """
    ...
