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
    'GetPbfListingVersionsResult',
    'AwaitableGetPbfListingVersionsResult',
    'get_pbf_listing_versions',
    'get_pbf_listing_versions_output',
]

@pulumi.output_type
class GetPbfListingVersionsResult:
    """
    A collection of values returned by getPbfListingVersions.
    """
    def __init__(__self__, filters=None, id=None, is_current_version=None, name=None, pbf_listing_id=None, pbf_listing_version_id=None, pbf_listing_versions_collections=None, state=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_current_version and not isinstance(is_current_version, bool):
            raise TypeError("Expected argument 'is_current_version' to be a bool")
        pulumi.set(__self__, "is_current_version", is_current_version)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if pbf_listing_id and not isinstance(pbf_listing_id, str):
            raise TypeError("Expected argument 'pbf_listing_id' to be a str")
        pulumi.set(__self__, "pbf_listing_id", pbf_listing_id)
        if pbf_listing_version_id and not isinstance(pbf_listing_version_id, str):
            raise TypeError("Expected argument 'pbf_listing_version_id' to be a str")
        pulumi.set(__self__, "pbf_listing_version_id", pbf_listing_version_id)
        if pbf_listing_versions_collections and not isinstance(pbf_listing_versions_collections, list):
            raise TypeError("Expected argument 'pbf_listing_versions_collections' to be a list")
        pulumi.set(__self__, "pbf_listing_versions_collections", pbf_listing_versions_collections)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetPbfListingVersionsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isCurrentVersion")
    def is_current_version(self) -> Optional[bool]:
        return pulumi.get(self, "is_current_version")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        A brief descriptive name for the PBF trigger.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pbfListingId")
    def pbf_listing_id(self) -> str:
        """
        The OCID of the PbfListing this resource version belongs to.
        """
        return pulumi.get(self, "pbf_listing_id")

    @property
    @pulumi.getter(name="pbfListingVersionId")
    def pbf_listing_version_id(self) -> Optional[str]:
        return pulumi.get(self, "pbf_listing_version_id")

    @property
    @pulumi.getter(name="pbfListingVersionsCollections")
    def pbf_listing_versions_collections(self) -> Sequence['outputs.GetPbfListingVersionsPbfListingVersionsCollectionResult']:
        """
        The list of pbf_listing_versions_collection.
        """
        return pulumi.get(self, "pbf_listing_versions_collections")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the PBF resource.
        """
        return pulumi.get(self, "state")


class AwaitableGetPbfListingVersionsResult(GetPbfListingVersionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPbfListingVersionsResult(
            filters=self.filters,
            id=self.id,
            is_current_version=self.is_current_version,
            name=self.name,
            pbf_listing_id=self.pbf_listing_id,
            pbf_listing_version_id=self.pbf_listing_version_id,
            pbf_listing_versions_collections=self.pbf_listing_versions_collections,
            state=self.state)


def get_pbf_listing_versions(filters: Optional[Sequence[pulumi.InputType['GetPbfListingVersionsFilterArgs']]] = None,
                             is_current_version: Optional[bool] = None,
                             name: Optional[str] = None,
                             pbf_listing_id: Optional[str] = None,
                             pbf_listing_version_id: Optional[str] = None,
                             state: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPbfListingVersionsResult:
    """
    This data source provides the list of Pbf Listing Versions in Oracle Cloud Infrastructure Functions service.

    Fetches a wrapped list of all Pre-built Function(PBF) Listing versions. Returns a PbfListingVersionCollection
    containing an array of PbfListingVersionSummary response models.

    Note that the PbfListingIdentifier must be provided as a query parameter, otherwise an exception shall
    be thrown.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_pbf_listing_versions = oci.Functions.get_pbf_listing_versions(pbf_listing_id=oci_functions_pbf_listing["test_pbf_listing"]["id"],
        is_current_version=var["pbf_listing_version_is_current_version"],
        name=var["pbf_listing_version_name"],
        pbf_listing_version_id=oci_functions_pbf_listing_version["test_pbf_listing_version"]["id"],
        state=var["pbf_listing_version_state"])
    ```


    :param bool is_current_version: Matches the current version (the most recently added version with an Active  lifecycleState) associated with a PbfListing.
    :param str name: Matches a PbfListingVersion based on a provided semantic version name for a PbfListingVersion.  Each PbfListingVersion name is unique with respect to its associated PbfListing.
    :param str pbf_listing_id: unique PbfListing identifier
    :param str pbf_listing_version_id: unique PbfListingVersion identifier
    :param str state: A filter to return only resources their lifecycleState matches the given lifecycleState.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['isCurrentVersion'] = is_current_version
    __args__['name'] = name
    __args__['pbfListingId'] = pbf_listing_id
    __args__['pbfListingVersionId'] = pbf_listing_version_id
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Functions/getPbfListingVersions:getPbfListingVersions', __args__, opts=opts, typ=GetPbfListingVersionsResult).value

    return AwaitableGetPbfListingVersionsResult(
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        is_current_version=pulumi.get(__ret__, 'is_current_version'),
        name=pulumi.get(__ret__, 'name'),
        pbf_listing_id=pulumi.get(__ret__, 'pbf_listing_id'),
        pbf_listing_version_id=pulumi.get(__ret__, 'pbf_listing_version_id'),
        pbf_listing_versions_collections=pulumi.get(__ret__, 'pbf_listing_versions_collections'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_pbf_listing_versions)
def get_pbf_listing_versions_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetPbfListingVersionsFilterArgs']]]]] = None,
                                    is_current_version: Optional[pulumi.Input[Optional[bool]]] = None,
                                    name: Optional[pulumi.Input[Optional[str]]] = None,
                                    pbf_listing_id: Optional[pulumi.Input[str]] = None,
                                    pbf_listing_version_id: Optional[pulumi.Input[Optional[str]]] = None,
                                    state: Optional[pulumi.Input[Optional[str]]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPbfListingVersionsResult]:
    """
    This data source provides the list of Pbf Listing Versions in Oracle Cloud Infrastructure Functions service.

    Fetches a wrapped list of all Pre-built Function(PBF) Listing versions. Returns a PbfListingVersionCollection
    containing an array of PbfListingVersionSummary response models.

    Note that the PbfListingIdentifier must be provided as a query parameter, otherwise an exception shall
    be thrown.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_pbf_listing_versions = oci.Functions.get_pbf_listing_versions(pbf_listing_id=oci_functions_pbf_listing["test_pbf_listing"]["id"],
        is_current_version=var["pbf_listing_version_is_current_version"],
        name=var["pbf_listing_version_name"],
        pbf_listing_version_id=oci_functions_pbf_listing_version["test_pbf_listing_version"]["id"],
        state=var["pbf_listing_version_state"])
    ```


    :param bool is_current_version: Matches the current version (the most recently added version with an Active  lifecycleState) associated with a PbfListing.
    :param str name: Matches a PbfListingVersion based on a provided semantic version name for a PbfListingVersion.  Each PbfListingVersion name is unique with respect to its associated PbfListing.
    :param str pbf_listing_id: unique PbfListing identifier
    :param str pbf_listing_version_id: unique PbfListingVersion identifier
    :param str state: A filter to return only resources their lifecycleState matches the given lifecycleState.
    """
    ...
