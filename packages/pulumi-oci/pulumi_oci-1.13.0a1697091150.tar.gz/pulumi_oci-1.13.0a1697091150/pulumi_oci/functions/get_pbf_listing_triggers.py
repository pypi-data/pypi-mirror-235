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
    'GetPbfListingTriggersResult',
    'AwaitableGetPbfListingTriggersResult',
    'get_pbf_listing_triggers',
    'get_pbf_listing_triggers_output',
]

@pulumi.output_type
class GetPbfListingTriggersResult:
    """
    A collection of values returned by getPbfListingTriggers.
    """
    def __init__(__self__, filters=None, id=None, name=None, triggers_collections=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if triggers_collections and not isinstance(triggers_collections, list):
            raise TypeError("Expected argument 'triggers_collections' to be a list")
        pulumi.set(__self__, "triggers_collections", triggers_collections)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetPbfListingTriggersFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        A brief descriptive name for the PBF trigger.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="triggersCollections")
    def triggers_collections(self) -> Sequence['outputs.GetPbfListingTriggersTriggersCollectionResult']:
        """
        The list of triggers_collection.
        """
        return pulumi.get(self, "triggers_collections")


class AwaitableGetPbfListingTriggersResult(GetPbfListingTriggersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPbfListingTriggersResult(
            filters=self.filters,
            id=self.id,
            name=self.name,
            triggers_collections=self.triggers_collections)


def get_pbf_listing_triggers(filters: Optional[Sequence[pulumi.InputType['GetPbfListingTriggersFilterArgs']]] = None,
                             name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPbfListingTriggersResult:
    """
    This data source provides the list of Pbf Listing Triggers in Oracle Cloud Infrastructure Functions service.

    Returns a list of Triggers.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_pbf_listing_triggers = oci.Functions.get_pbf_listing_triggers(name=var["pbf_listing_trigger_name"])
    ```


    :param str name: A filter to return only resources that match the service trigger source of a PBF.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Functions/getPbfListingTriggers:getPbfListingTriggers', __args__, opts=opts, typ=GetPbfListingTriggersResult).value

    return AwaitableGetPbfListingTriggersResult(
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        triggers_collections=pulumi.get(__ret__, 'triggers_collections'))


@_utilities.lift_output_func(get_pbf_listing_triggers)
def get_pbf_listing_triggers_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetPbfListingTriggersFilterArgs']]]]] = None,
                                    name: Optional[pulumi.Input[Optional[str]]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPbfListingTriggersResult]:
    """
    This data source provides the list of Pbf Listing Triggers in Oracle Cloud Infrastructure Functions service.

    Returns a list of Triggers.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_pbf_listing_triggers = oci.Functions.get_pbf_listing_triggers(name=var["pbf_listing_trigger_name"])
    ```


    :param str name: A filter to return only resources that match the service trigger source of a PBF.
    """
    ...
