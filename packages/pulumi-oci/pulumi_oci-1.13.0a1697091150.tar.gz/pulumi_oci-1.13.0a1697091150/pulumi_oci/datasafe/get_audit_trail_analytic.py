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
    'GetAuditTrailAnalyticResult',
    'AwaitableGetAuditTrailAnalyticResult',
    'get_audit_trail_analytic',
    'get_audit_trail_analytic_output',
]

@pulumi.output_type
class GetAuditTrailAnalyticResult:
    """
    A collection of values returned by getAuditTrailAnalytic.
    """
    def __init__(__self__, access_level=None, compartment_id=None, compartment_id_in_subtree=None, group_bies=None, id=None, items=None, target_id=None):
        if access_level and not isinstance(access_level, str):
            raise TypeError("Expected argument 'access_level' to be a str")
        pulumi.set(__self__, "access_level", access_level)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if compartment_id_in_subtree and not isinstance(compartment_id_in_subtree, bool):
            raise TypeError("Expected argument 'compartment_id_in_subtree' to be a bool")
        pulumi.set(__self__, "compartment_id_in_subtree", compartment_id_in_subtree)
        if group_bies and not isinstance(group_bies, list):
            raise TypeError("Expected argument 'group_bies' to be a list")
        pulumi.set(__self__, "group_bies", group_bies)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if items and not isinstance(items, list):
            raise TypeError("Expected argument 'items' to be a list")
        pulumi.set(__self__, "items", items)
        if target_id and not isinstance(target_id, str):
            raise TypeError("Expected argument 'target_id' to be a str")
        pulumi.set(__self__, "target_id", target_id)

    @property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[str]:
        return pulumi.get(self, "access_level")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="compartmentIdInSubtree")
    def compartment_id_in_subtree(self) -> Optional[bool]:
        return pulumi.get(self, "compartment_id_in_subtree")

    @property
    @pulumi.getter(name="groupBies")
    def group_bies(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "group_bies")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.GetAuditTrailAnalyticItemResult']:
        """
        Array of audit trail aggregration data.
        """
        return pulumi.get(self, "items")

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[str]:
        """
        The OCID of the Data Safe target for which the audit trail is created.
        """
        return pulumi.get(self, "target_id")


class AwaitableGetAuditTrailAnalyticResult(GetAuditTrailAnalyticResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAuditTrailAnalyticResult(
            access_level=self.access_level,
            compartment_id=self.compartment_id,
            compartment_id_in_subtree=self.compartment_id_in_subtree,
            group_bies=self.group_bies,
            id=self.id,
            items=self.items,
            target_id=self.target_id)


def get_audit_trail_analytic(access_level: Optional[str] = None,
                             compartment_id: Optional[str] = None,
                             compartment_id_in_subtree: Optional[bool] = None,
                             group_bies: Optional[Sequence[str]] = None,
                             target_id: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAuditTrailAnalyticResult:
    """
    This data source provides details about a specific Audit Trail Analytic resource in Oracle Cloud Infrastructure Data Safe service.

    Gets a list of audit trail aggregated details . A audit trail aggregation helps understand the overall  state of trails.
    As an example, it helps understand how many trails are running or stopped. It is especially useful to create dashboards or to support analytics.

    The parameter `accessLevel` specifies whether to return only those compartments for which the
    requestor has INSPECT permissions on at least one resource directly
    or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if
    Principal doesn't have access to even one of the child compartments. This is valid only when
    `compartmentIdInSubtree` is set to `true`.

    The parameter `compartmentIdInSubtree` applies when you perform AuditTrailAnalytics on the
    `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned.
    To get a full list of all compartments and subcompartments in the tenancy (root compartment),
    set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_audit_trail_analytic = oci.DataSafe.get_audit_trail_analytic(compartment_id=var["compartment_id"],
        access_level=var["audit_trail_analytic_access_level"],
        compartment_id_in_subtree=var["audit_trail_analytic_compartment_id_in_subtree"],
        group_bies=var["audit_trail_analytic_group_by"],
        target_id=oci_cloud_guard_target["test_target"]["id"])
    ```


    :param str access_level: Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.
    :param str compartment_id: A filter to return only resources that match the specified compartment OCID.
    :param bool compartment_id_in_subtree: Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.
    :param Sequence[str] group_bies: The group by parameter for summarize operation on audit trail.
    :param str target_id: A filter to return only items related to a specific target OCID.
    """
    __args__ = dict()
    __args__['accessLevel'] = access_level
    __args__['compartmentId'] = compartment_id
    __args__['compartmentIdInSubtree'] = compartment_id_in_subtree
    __args__['groupBies'] = group_bies
    __args__['targetId'] = target_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataSafe/getAuditTrailAnalytic:getAuditTrailAnalytic', __args__, opts=opts, typ=GetAuditTrailAnalyticResult).value

    return AwaitableGetAuditTrailAnalyticResult(
        access_level=pulumi.get(__ret__, 'access_level'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        compartment_id_in_subtree=pulumi.get(__ret__, 'compartment_id_in_subtree'),
        group_bies=pulumi.get(__ret__, 'group_bies'),
        id=pulumi.get(__ret__, 'id'),
        items=pulumi.get(__ret__, 'items'),
        target_id=pulumi.get(__ret__, 'target_id'))


@_utilities.lift_output_func(get_audit_trail_analytic)
def get_audit_trail_analytic_output(access_level: Optional[pulumi.Input[Optional[str]]] = None,
                                    compartment_id: Optional[pulumi.Input[str]] = None,
                                    compartment_id_in_subtree: Optional[pulumi.Input[Optional[bool]]] = None,
                                    group_bies: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                    target_id: Optional[pulumi.Input[Optional[str]]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAuditTrailAnalyticResult]:
    """
    This data source provides details about a specific Audit Trail Analytic resource in Oracle Cloud Infrastructure Data Safe service.

    Gets a list of audit trail aggregated details . A audit trail aggregation helps understand the overall  state of trails.
    As an example, it helps understand how many trails are running or stopped. It is especially useful to create dashboards or to support analytics.

    The parameter `accessLevel` specifies whether to return only those compartments for which the
    requestor has INSPECT permissions on at least one resource directly
    or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if
    Principal doesn't have access to even one of the child compartments. This is valid only when
    `compartmentIdInSubtree` is set to `true`.

    The parameter `compartmentIdInSubtree` applies when you perform AuditTrailAnalytics on the
    `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned.
    To get a full list of all compartments and subcompartments in the tenancy (root compartment),
    set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_audit_trail_analytic = oci.DataSafe.get_audit_trail_analytic(compartment_id=var["compartment_id"],
        access_level=var["audit_trail_analytic_access_level"],
        compartment_id_in_subtree=var["audit_trail_analytic_compartment_id_in_subtree"],
        group_bies=var["audit_trail_analytic_group_by"],
        target_id=oci_cloud_guard_target["test_target"]["id"])
    ```


    :param str access_level: Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.
    :param str compartment_id: A filter to return only resources that match the specified compartment OCID.
    :param bool compartment_id_in_subtree: Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.
    :param Sequence[str] group_bies: The group by parameter for summarize operation on audit trail.
    :param str target_id: A filter to return only items related to a specific target OCID.
    """
    ...
