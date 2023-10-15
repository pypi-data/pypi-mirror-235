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
    'GetReportsResult',
    'AwaitableGetReportsResult',
    'get_reports',
    'get_reports_output',
]

@pulumi.output_type
class GetReportsResult:
    """
    A collection of values returned by getReports.
    """
    def __init__(__self__, access_level=None, compartment_id=None, compartment_id_in_subtree=None, display_name=None, filters=None, id=None, report_collections=None, report_definition_id=None, state=None, type=None):
        if access_level and not isinstance(access_level, str):
            raise TypeError("Expected argument 'access_level' to be a str")
        pulumi.set(__self__, "access_level", access_level)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if compartment_id_in_subtree and not isinstance(compartment_id_in_subtree, bool):
            raise TypeError("Expected argument 'compartment_id_in_subtree' to be a bool")
        pulumi.set(__self__, "compartment_id_in_subtree", compartment_id_in_subtree)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if report_collections and not isinstance(report_collections, list):
            raise TypeError("Expected argument 'report_collections' to be a list")
        pulumi.set(__self__, "report_collections", report_collections)
        if report_definition_id and not isinstance(report_definition_id, str):
            raise TypeError("Expected argument 'report_definition_id' to be a str")
        pulumi.set(__self__, "report_definition_id", report_definition_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[str]:
        return pulumi.get(self, "access_level")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment containing the report.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="compartmentIdInSubtree")
    def compartment_id_in_subtree(self) -> Optional[bool]:
        return pulumi.get(self, "compartment_id_in_subtree")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        Name of the report.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetReportsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="reportCollections")
    def report_collections(self) -> Sequence['outputs.GetReportsReportCollectionResult']:
        """
        The list of report_collection.
        """
        return pulumi.get(self, "report_collections")

    @property
    @pulumi.getter(name="reportDefinitionId")
    def report_definition_id(self) -> Optional[str]:
        """
        The OCID of the report definition.
        """
        return pulumi.get(self, "report_definition_id")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the audit report.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type of the audit report.
        """
        return pulumi.get(self, "type")


class AwaitableGetReportsResult(GetReportsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReportsResult(
            access_level=self.access_level,
            compartment_id=self.compartment_id,
            compartment_id_in_subtree=self.compartment_id_in_subtree,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            report_collections=self.report_collections,
            report_definition_id=self.report_definition_id,
            state=self.state,
            type=self.type)


def get_reports(access_level: Optional[str] = None,
                compartment_id: Optional[str] = None,
                compartment_id_in_subtree: Optional[bool] = None,
                display_name: Optional[str] = None,
                filters: Optional[Sequence[pulumi.InputType['GetReportsFilterArgs']]] = None,
                report_definition_id: Optional[str] = None,
                state: Optional[str] = None,
                type: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReportsResult:
    """
    This data source provides the list of Reports in Oracle Cloud Infrastructure Data Safe service.

    Gets a list of all the reports in the compartment. It contains information such as report generation time.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_reports = oci.DataSafe.get_reports(compartment_id=var["compartment_id"],
        access_level=var["report_access_level"],
        compartment_id_in_subtree=var["report_compartment_id_in_subtree"],
        display_name=var["report_display_name"],
        report_definition_id=oci_data_safe_report_definition["test_report_definition"]["id"],
        state=var["report_state"],
        type=var["report_type"])
    ```


    :param str access_level: Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.
    :param str compartment_id: A filter to return only resources that match the specified compartment OCID.
    :param bool compartment_id_in_subtree: Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.
    :param str display_name: The name of the report definition to query.
    :param str report_definition_id: The ID of the report definition to filter the list of reports
    :param str state: An optional filter to return only resources that match the specified lifecycle state.
    :param str type: An optional filter to return only resources that match the specified type.
    """
    __args__ = dict()
    __args__['accessLevel'] = access_level
    __args__['compartmentId'] = compartment_id
    __args__['compartmentIdInSubtree'] = compartment_id_in_subtree
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['reportDefinitionId'] = report_definition_id
    __args__['state'] = state
    __args__['type'] = type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataSafe/getReports:getReports', __args__, opts=opts, typ=GetReportsResult).value

    return AwaitableGetReportsResult(
        access_level=pulumi.get(__ret__, 'access_level'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        compartment_id_in_subtree=pulumi.get(__ret__, 'compartment_id_in_subtree'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        report_collections=pulumi.get(__ret__, 'report_collections'),
        report_definition_id=pulumi.get(__ret__, 'report_definition_id'),
        state=pulumi.get(__ret__, 'state'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_reports)
def get_reports_output(access_level: Optional[pulumi.Input[Optional[str]]] = None,
                       compartment_id: Optional[pulumi.Input[str]] = None,
                       compartment_id_in_subtree: Optional[pulumi.Input[Optional[bool]]] = None,
                       display_name: Optional[pulumi.Input[Optional[str]]] = None,
                       filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetReportsFilterArgs']]]]] = None,
                       report_definition_id: Optional[pulumi.Input[Optional[str]]] = None,
                       state: Optional[pulumi.Input[Optional[str]]] = None,
                       type: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReportsResult]:
    """
    This data source provides the list of Reports in Oracle Cloud Infrastructure Data Safe service.

    Gets a list of all the reports in the compartment. It contains information such as report generation time.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_reports = oci.DataSafe.get_reports(compartment_id=var["compartment_id"],
        access_level=var["report_access_level"],
        compartment_id_in_subtree=var["report_compartment_id_in_subtree"],
        display_name=var["report_display_name"],
        report_definition_id=oci_data_safe_report_definition["test_report_definition"]["id"],
        state=var["report_state"],
        type=var["report_type"])
    ```


    :param str access_level: Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.
    :param str compartment_id: A filter to return only resources that match the specified compartment OCID.
    :param bool compartment_id_in_subtree: Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.
    :param str display_name: The name of the report definition to query.
    :param str report_definition_id: The ID of the report definition to filter the list of reports
    :param str state: An optional filter to return only resources that match the specified lifecycle state.
    :param str type: An optional filter to return only resources that match the specified type.
    """
    ...
