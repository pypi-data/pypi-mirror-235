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
    'GetAppCatalogListingResourceVersionResult',
    'AwaitableGetAppCatalogListingResourceVersionResult',
    'get_app_catalog_listing_resource_version',
    'get_app_catalog_listing_resource_version_output',
]

@pulumi.output_type
class GetAppCatalogListingResourceVersionResult:
    """
    A collection of values returned by getAppCatalogListingResourceVersion.
    """
    def __init__(__self__, accessible_ports=None, allowed_actions=None, available_regions=None, compatible_shapes=None, id=None, listing_id=None, listing_resource_id=None, listing_resource_version=None, resource_version=None, time_published=None):
        if accessible_ports and not isinstance(accessible_ports, list):
            raise TypeError("Expected argument 'accessible_ports' to be a list")
        pulumi.set(__self__, "accessible_ports", accessible_ports)
        if allowed_actions and not isinstance(allowed_actions, list):
            raise TypeError("Expected argument 'allowed_actions' to be a list")
        pulumi.set(__self__, "allowed_actions", allowed_actions)
        if available_regions and not isinstance(available_regions, list):
            raise TypeError("Expected argument 'available_regions' to be a list")
        pulumi.set(__self__, "available_regions", available_regions)
        if compatible_shapes and not isinstance(compatible_shapes, list):
            raise TypeError("Expected argument 'compatible_shapes' to be a list")
        pulumi.set(__self__, "compatible_shapes", compatible_shapes)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if listing_id and not isinstance(listing_id, str):
            raise TypeError("Expected argument 'listing_id' to be a str")
        pulumi.set(__self__, "listing_id", listing_id)
        if listing_resource_id and not isinstance(listing_resource_id, str):
            raise TypeError("Expected argument 'listing_resource_id' to be a str")
        pulumi.set(__self__, "listing_resource_id", listing_resource_id)
        if listing_resource_version and not isinstance(listing_resource_version, str):
            raise TypeError("Expected argument 'listing_resource_version' to be a str")
        pulumi.set(__self__, "listing_resource_version", listing_resource_version)
        if resource_version and not isinstance(resource_version, str):
            raise TypeError("Expected argument 'resource_version' to be a str")
        pulumi.set(__self__, "resource_version", resource_version)
        if time_published and not isinstance(time_published, str):
            raise TypeError("Expected argument 'time_published' to be a str")
        pulumi.set(__self__, "time_published", time_published)

    @property
    @pulumi.getter(name="accessiblePorts")
    def accessible_ports(self) -> Sequence[int]:
        """
        List of accessible ports for instances launched with this listing resource version.
        """
        return pulumi.get(self, "accessible_ports")

    @property
    @pulumi.getter(name="allowedActions")
    def allowed_actions(self) -> Sequence[str]:
        """
        Allowed actions for the listing resource.
        """
        return pulumi.get(self, "allowed_actions")

    @property
    @pulumi.getter(name="availableRegions")
    def available_regions(self) -> Sequence[str]:
        """
        List of regions that this listing resource version is available.
        """
        return pulumi.get(self, "available_regions")

    @property
    @pulumi.getter(name="compatibleShapes")
    def compatible_shapes(self) -> Sequence[str]:
        """
        Array of shapes compatible with this resource.
        """
        return pulumi.get(self, "compatible_shapes")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="listingId")
    def listing_id(self) -> str:
        """
        The OCID of the listing this resource version belongs to.
        """
        return pulumi.get(self, "listing_id")

    @property
    @pulumi.getter(name="listingResourceId")
    def listing_resource_id(self) -> str:
        """
        OCID of the listing resource.
        """
        return pulumi.get(self, "listing_resource_id")

    @property
    @pulumi.getter(name="listingResourceVersion")
    def listing_resource_version(self) -> str:
        """
        Resource Version.
        """
        return pulumi.get(self, "listing_resource_version")

    @property
    @pulumi.getter(name="resourceVersion")
    def resource_version(self) -> str:
        return pulumi.get(self, "resource_version")

    @property
    @pulumi.getter(name="timePublished")
    def time_published(self) -> str:
        """
        Date and time the listing resource version was published, in [RFC3339](https://tools.ietf.org/html/rfc3339) format. Example: `2018-03-20T12:32:53.532Z`
        """
        return pulumi.get(self, "time_published")


class AwaitableGetAppCatalogListingResourceVersionResult(GetAppCatalogListingResourceVersionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAppCatalogListingResourceVersionResult(
            accessible_ports=self.accessible_ports,
            allowed_actions=self.allowed_actions,
            available_regions=self.available_regions,
            compatible_shapes=self.compatible_shapes,
            id=self.id,
            listing_id=self.listing_id,
            listing_resource_id=self.listing_resource_id,
            listing_resource_version=self.listing_resource_version,
            resource_version=self.resource_version,
            time_published=self.time_published)


def get_app_catalog_listing_resource_version(listing_id: Optional[str] = None,
                                             resource_version: Optional[str] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAppCatalogListingResourceVersionResult:
    """
    This data source provides details about a specific App Catalog Listing Resource Version resource in Oracle Cloud Infrastructure Core service.

    Gets the specified listing resource version.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_app_catalog_listing_resource_version = oci.Core.get_app_catalog_listing_resource_version(listing_id=data["oci_core_app_catalog_listing"]["test_listing"]["id"],
        resource_version=var["app_catalog_listing_resource_version_resource_version"])
    ```


    :param str listing_id: The OCID of the listing.
    :param str resource_version: Listing Resource Version.
    """
    __args__ = dict()
    __args__['listingId'] = listing_id
    __args__['resourceVersion'] = resource_version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Core/getAppCatalogListingResourceVersion:getAppCatalogListingResourceVersion', __args__, opts=opts, typ=GetAppCatalogListingResourceVersionResult).value

    return AwaitableGetAppCatalogListingResourceVersionResult(
        accessible_ports=pulumi.get(__ret__, 'accessible_ports'),
        allowed_actions=pulumi.get(__ret__, 'allowed_actions'),
        available_regions=pulumi.get(__ret__, 'available_regions'),
        compatible_shapes=pulumi.get(__ret__, 'compatible_shapes'),
        id=pulumi.get(__ret__, 'id'),
        listing_id=pulumi.get(__ret__, 'listing_id'),
        listing_resource_id=pulumi.get(__ret__, 'listing_resource_id'),
        listing_resource_version=pulumi.get(__ret__, 'listing_resource_version'),
        resource_version=pulumi.get(__ret__, 'resource_version'),
        time_published=pulumi.get(__ret__, 'time_published'))


@_utilities.lift_output_func(get_app_catalog_listing_resource_version)
def get_app_catalog_listing_resource_version_output(listing_id: Optional[pulumi.Input[str]] = None,
                                                    resource_version: Optional[pulumi.Input[str]] = None,
                                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAppCatalogListingResourceVersionResult]:
    """
    This data source provides details about a specific App Catalog Listing Resource Version resource in Oracle Cloud Infrastructure Core service.

    Gets the specified listing resource version.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_app_catalog_listing_resource_version = oci.Core.get_app_catalog_listing_resource_version(listing_id=data["oci_core_app_catalog_listing"]["test_listing"]["id"],
        resource_version=var["app_catalog_listing_resource_version_resource_version"])
    ```


    :param str listing_id: The OCID of the listing.
    :param str resource_version: Listing Resource Version.
    """
    ...
