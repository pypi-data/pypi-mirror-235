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
    'GetWaasPolicyResult',
    'AwaitableGetWaasPolicyResult',
    'get_waas_policy',
    'get_waas_policy_output',
]

@pulumi.output_type
class GetWaasPolicyResult:
    """
    A collection of values returned by getWaasPolicy.
    """
    def __init__(__self__, additional_domains=None, cname=None, compartment_id=None, defined_tags=None, display_name=None, domain=None, freeform_tags=None, id=None, origin_groups=None, origins=None, policy_configs=None, state=None, time_created=None, waas_policy_id=None, waf_configs=None):
        if additional_domains and not isinstance(additional_domains, list):
            raise TypeError("Expected argument 'additional_domains' to be a list")
        pulumi.set(__self__, "additional_domains", additional_domains)
        if cname and not isinstance(cname, str):
            raise TypeError("Expected argument 'cname' to be a str")
        pulumi.set(__self__, "cname", cname)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if domain and not isinstance(domain, str):
            raise TypeError("Expected argument 'domain' to be a str")
        pulumi.set(__self__, "domain", domain)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if origin_groups and not isinstance(origin_groups, list):
            raise TypeError("Expected argument 'origin_groups' to be a list")
        pulumi.set(__self__, "origin_groups", origin_groups)
        if origins and not isinstance(origins, list):
            raise TypeError("Expected argument 'origins' to be a list")
        pulumi.set(__self__, "origins", origins)
        if policy_configs and not isinstance(policy_configs, list):
            raise TypeError("Expected argument 'policy_configs' to be a list")
        pulumi.set(__self__, "policy_configs", policy_configs)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if waas_policy_id and not isinstance(waas_policy_id, str):
            raise TypeError("Expected argument 'waas_policy_id' to be a str")
        pulumi.set(__self__, "waas_policy_id", waas_policy_id)
        if waf_configs and not isinstance(waf_configs, list):
            raise TypeError("Expected argument 'waf_configs' to be a list")
        pulumi.set(__self__, "waf_configs", waf_configs)

    @property
    @pulumi.getter(name="additionalDomains")
    def additional_domains(self) -> Sequence[str]:
        """
        An array of additional domains for this web application.
        """
        return pulumi.get(self, "additional_domains")

    @property
    @pulumi.getter
    def cname(self) -> str:
        """
        The CNAME record to add to your DNS configuration to route traffic for the domain, and all additional domains, through the WAF.
        """
        return pulumi.get(self, "cname")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the WAAS policy's compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The user-friendly name of the WAAS policy. The name can be changed and does not need to be unique.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def domain(self) -> str:
        """
        The domain for which the cookie is set, defaults to WAAS policy domain.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="originGroups")
    def origin_groups(self) -> Sequence['outputs.GetWaasPolicyOriginGroupResult']:
        """
        The map of origin groups and their keys used to associate origins to the `wafConfig`. Origin groups allow you to apply weights to groups of origins for load balancing purposes. Origins with higher weights will receive larger proportions of client requests. To add additional origins to your WAAS policy, update the `origins` field of a `UpdateWaasPolicy` request.
        """
        return pulumi.get(self, "origin_groups")

    @property
    @pulumi.getter
    def origins(self) -> Sequence['outputs.GetWaasPolicyOriginResult']:
        """
        A map of host servers (origins) and their keys for the web application. Origin keys are used to associate origins to specific protection rules. The key should be a user-friendly name for the host. **Examples:** `primary` or `secondary`.
        """
        return pulumi.get(self, "origins")

    @property
    @pulumi.getter(name="policyConfigs")
    def policy_configs(self) -> Sequence['outputs.GetWaasPolicyPolicyConfigResult']:
        """
        The configuration details for the WAAS policy.
        """
        return pulumi.get(self, "policy_configs")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current lifecycle state of the WAAS policy.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the policy was created, expressed in RFC 3339 timestamp format.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="waasPolicyId")
    def waas_policy_id(self) -> str:
        return pulumi.get(self, "waas_policy_id")

    @property
    @pulumi.getter(name="wafConfigs")
    def waf_configs(self) -> Sequence['outputs.GetWaasPolicyWafConfigResult']:
        """
        The Web Application Firewall configuration for the WAAS policy.
        """
        return pulumi.get(self, "waf_configs")


class AwaitableGetWaasPolicyResult(GetWaasPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWaasPolicyResult(
            additional_domains=self.additional_domains,
            cname=self.cname,
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            display_name=self.display_name,
            domain=self.domain,
            freeform_tags=self.freeform_tags,
            id=self.id,
            origin_groups=self.origin_groups,
            origins=self.origins,
            policy_configs=self.policy_configs,
            state=self.state,
            time_created=self.time_created,
            waas_policy_id=self.waas_policy_id,
            waf_configs=self.waf_configs)


def get_waas_policy(waas_policy_id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWaasPolicyResult:
    """
    This data source provides details about a specific Waas Policy resource in Oracle Cloud Infrastructure Web Application Acceleration and Security service.

    Gets the details of a WAAS policy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_waas_policy = oci.Waas.get_waas_policy(waas_policy_id=oci_waas_waas_policy["test_waas_policy"]["id"])
    ```


    :param str waas_policy_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the WAAS policy.
    """
    __args__ = dict()
    __args__['waasPolicyId'] = waas_policy_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Waas/getWaasPolicy:getWaasPolicy', __args__, opts=opts, typ=GetWaasPolicyResult).value

    return AwaitableGetWaasPolicyResult(
        additional_domains=pulumi.get(__ret__, 'additional_domains'),
        cname=pulumi.get(__ret__, 'cname'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        display_name=pulumi.get(__ret__, 'display_name'),
        domain=pulumi.get(__ret__, 'domain'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        origin_groups=pulumi.get(__ret__, 'origin_groups'),
        origins=pulumi.get(__ret__, 'origins'),
        policy_configs=pulumi.get(__ret__, 'policy_configs'),
        state=pulumi.get(__ret__, 'state'),
        time_created=pulumi.get(__ret__, 'time_created'),
        waas_policy_id=pulumi.get(__ret__, 'waas_policy_id'),
        waf_configs=pulumi.get(__ret__, 'waf_configs'))


@_utilities.lift_output_func(get_waas_policy)
def get_waas_policy_output(waas_policy_id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWaasPolicyResult]:
    """
    This data source provides details about a specific Waas Policy resource in Oracle Cloud Infrastructure Web Application Acceleration and Security service.

    Gets the details of a WAAS policy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_waas_policy = oci.Waas.get_waas_policy(waas_policy_id=oci_waas_waas_policy["test_waas_policy"]["id"])
    ```


    :param str waas_policy_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the WAAS policy.
    """
    ...
