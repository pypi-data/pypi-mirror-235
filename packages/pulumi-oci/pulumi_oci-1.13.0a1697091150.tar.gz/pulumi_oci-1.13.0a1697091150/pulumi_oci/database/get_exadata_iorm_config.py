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
    'GetExadataIormConfigResult',
    'AwaitableGetExadataIormConfigResult',
    'get_exadata_iorm_config',
    'get_exadata_iorm_config_output',
]

@pulumi.output_type
class GetExadataIormConfigResult:
    """
    A collection of values returned by getExadataIormConfig.
    """
    def __init__(__self__, db_plans=None, db_system_id=None, id=None, lifecycle_details=None, objective=None, state=None):
        if db_plans and not isinstance(db_plans, list):
            raise TypeError("Expected argument 'db_plans' to be a list")
        pulumi.set(__self__, "db_plans", db_plans)
        if db_system_id and not isinstance(db_system_id, str):
            raise TypeError("Expected argument 'db_system_id' to be a str")
        pulumi.set(__self__, "db_system_id", db_system_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if objective and not isinstance(objective, str):
            raise TypeError("Expected argument 'objective' to be a str")
        pulumi.set(__self__, "objective", objective)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="dbPlans")
    def db_plans(self) -> Sequence['outputs.GetExadataIormConfigDbPlanResult']:
        """
        An array of IORM settings for all the database in the Exadata DB system.
        """
        return pulumi.get(self, "db_plans")

    @property
    @pulumi.getter(name="dbSystemId")
    def db_system_id(self) -> str:
        return pulumi.get(self, "db_system_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        Additional information about the current `lifecycleState`.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter
    def objective(self) -> str:
        """
        The current value for the IORM objective. The default is `AUTO`.
        """
        return pulumi.get(self, "objective")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of IORM configuration for the Exadata DB system.
        """
        return pulumi.get(self, "state")


class AwaitableGetExadataIormConfigResult(GetExadataIormConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExadataIormConfigResult(
            db_plans=self.db_plans,
            db_system_id=self.db_system_id,
            id=self.id,
            lifecycle_details=self.lifecycle_details,
            objective=self.objective,
            state=self.state)


def get_exadata_iorm_config(db_system_id: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExadataIormConfigResult:
    """
    This data source provides details about a specific Exadata Iorm Config resource in Oracle Cloud Infrastructure Database service.

    Gets the IORM configuration settings for the specified cloud Exadata DB system.
    All Exadata service instances have default IORM settings.

    **Note:** Deprecated for Exadata Cloud Service systems. Use the [new resource model APIs](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/exaflexsystem.htm#exaflexsystem_topic-resource_model) instead.

    For Exadata Cloud Service instances, support for this API will end on May 15th, 2021. See [Switching an Exadata DB System to the New Resource Model and APIs](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/exaflexsystem_topic-resource_model_conversion.htm) for details on converting existing Exadata DB systems to the new resource model.

    The [GetCloudVmClusterIormConfig](https://docs.cloud.oracle.com/iaas/api/#/en/database/latest/CloudVmCluster/GetCloudVmClusterIormConfig/) API is used for this operation with Exadata systems using the
    new resource model.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_exadata_iorm_config = oci.Database.get_exadata_iorm_config(db_system_id=oci_database_db_system["test_db_system"]["id"])
    ```


    :param str db_system_id: The DB system [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    """
    __args__ = dict()
    __args__['dbSystemId'] = db_system_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Database/getExadataIormConfig:getExadataIormConfig', __args__, opts=opts, typ=GetExadataIormConfigResult).value

    return AwaitableGetExadataIormConfigResult(
        db_plans=pulumi.get(__ret__, 'db_plans'),
        db_system_id=pulumi.get(__ret__, 'db_system_id'),
        id=pulumi.get(__ret__, 'id'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        objective=pulumi.get(__ret__, 'objective'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_exadata_iorm_config)
def get_exadata_iorm_config_output(db_system_id: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExadataIormConfigResult]:
    """
    This data source provides details about a specific Exadata Iorm Config resource in Oracle Cloud Infrastructure Database service.

    Gets the IORM configuration settings for the specified cloud Exadata DB system.
    All Exadata service instances have default IORM settings.

    **Note:** Deprecated for Exadata Cloud Service systems. Use the [new resource model APIs](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/exaflexsystem.htm#exaflexsystem_topic-resource_model) instead.

    For Exadata Cloud Service instances, support for this API will end on May 15th, 2021. See [Switching an Exadata DB System to the New Resource Model and APIs](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/exaflexsystem_topic-resource_model_conversion.htm) for details on converting existing Exadata DB systems to the new resource model.

    The [GetCloudVmClusterIormConfig](https://docs.cloud.oracle.com/iaas/api/#/en/database/latest/CloudVmCluster/GetCloudVmClusterIormConfig/) API is used for this operation with Exadata systems using the
    new resource model.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_exadata_iorm_config = oci.Database.get_exadata_iorm_config(db_system_id=oci_database_db_system["test_db_system"]["id"])
    ```


    :param str db_system_id: The DB system [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    """
    ...
