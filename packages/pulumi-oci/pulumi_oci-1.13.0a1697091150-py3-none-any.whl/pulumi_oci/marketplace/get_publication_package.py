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
    'GetPublicationPackageResult',
    'AwaitableGetPublicationPackageResult',
    'get_publication_package',
    'get_publication_package_output',
]

@pulumi.output_type
class GetPublicationPackageResult:
    """
    A collection of values returned by getPublicationPackage.
    """
    def __init__(__self__, app_catalog_listing_id=None, app_catalog_listing_resource_version=None, description=None, id=None, image_id=None, listing_id=None, operating_systems=None, package_type=None, package_version=None, publication_id=None, resource_id=None, resource_link=None, time_created=None, variables=None, version=None):
        if app_catalog_listing_id and not isinstance(app_catalog_listing_id, str):
            raise TypeError("Expected argument 'app_catalog_listing_id' to be a str")
        pulumi.set(__self__, "app_catalog_listing_id", app_catalog_listing_id)
        if app_catalog_listing_resource_version and not isinstance(app_catalog_listing_resource_version, str):
            raise TypeError("Expected argument 'app_catalog_listing_resource_version' to be a str")
        pulumi.set(__self__, "app_catalog_listing_resource_version", app_catalog_listing_resource_version)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_id and not isinstance(image_id, str):
            raise TypeError("Expected argument 'image_id' to be a str")
        pulumi.set(__self__, "image_id", image_id)
        if listing_id and not isinstance(listing_id, str):
            raise TypeError("Expected argument 'listing_id' to be a str")
        pulumi.set(__self__, "listing_id", listing_id)
        if operating_systems and not isinstance(operating_systems, list):
            raise TypeError("Expected argument 'operating_systems' to be a list")
        pulumi.set(__self__, "operating_systems", operating_systems)
        if package_type and not isinstance(package_type, str):
            raise TypeError("Expected argument 'package_type' to be a str")
        pulumi.set(__self__, "package_type", package_type)
        if package_version and not isinstance(package_version, str):
            raise TypeError("Expected argument 'package_version' to be a str")
        pulumi.set(__self__, "package_version", package_version)
        if publication_id and not isinstance(publication_id, str):
            raise TypeError("Expected argument 'publication_id' to be a str")
        pulumi.set(__self__, "publication_id", publication_id)
        if resource_id and not isinstance(resource_id, str):
            raise TypeError("Expected argument 'resource_id' to be a str")
        pulumi.set(__self__, "resource_id", resource_id)
        if resource_link and not isinstance(resource_link, str):
            raise TypeError("Expected argument 'resource_link' to be a str")
        pulumi.set(__self__, "resource_link", resource_link)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if variables and not isinstance(variables, list):
            raise TypeError("Expected argument 'variables' to be a list")
        pulumi.set(__self__, "variables", variables)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="appCatalogListingId")
    def app_catalog_listing_id(self) -> str:
        """
        The ID of the listing resource associated with this publication package. For more information, see [AppCatalogListing](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogListing/) in the Core Services API.
        """
        return pulumi.get(self, "app_catalog_listing_id")

    @property
    @pulumi.getter(name="appCatalogListingResourceVersion")
    def app_catalog_listing_resource_version(self) -> str:
        """
        The resource version of the listing resource associated with this publication package.
        """
        return pulumi.get(self, "app_catalog_listing_resource_version")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A description of the variable.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> str:
        """
        The ID of the image that corresponds to the package.
        """
        return pulumi.get(self, "image_id")

    @property
    @pulumi.getter(name="listingId")
    def listing_id(self) -> str:
        """
        The ID of the listing that the specified package belongs to.
        """
        return pulumi.get(self, "listing_id")

    @property
    @pulumi.getter(name="operatingSystems")
    def operating_systems(self) -> Sequence['outputs.GetPublicationPackageOperatingSystemResult']:
        """
        The operating system used by the listing.
        """
        return pulumi.get(self, "operating_systems")

    @property
    @pulumi.getter(name="packageType")
    def package_type(self) -> str:
        """
        The specified package's type.
        """
        return pulumi.get(self, "package_type")

    @property
    @pulumi.getter(name="packageVersion")
    def package_version(self) -> str:
        return pulumi.get(self, "package_version")

    @property
    @pulumi.getter(name="publicationId")
    def publication_id(self) -> str:
        return pulumi.get(self, "publication_id")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> str:
        """
        The unique identifier for the package resource.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="resourceLink")
    def resource_link(self) -> str:
        """
        A link to the stack resource.
        """
        return pulumi.get(self, "resource_link")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the publication package was created, expressed in [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format.  Example: `2016-08-25T21:10:29.600Z`
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter
    def variables(self) -> Sequence['outputs.GetPublicationPackageVariableResult']:
        """
        A list of variables for the stack resource.
        """
        return pulumi.get(self, "variables")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        The package version.
        """
        return pulumi.get(self, "version")


class AwaitableGetPublicationPackageResult(GetPublicationPackageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPublicationPackageResult(
            app_catalog_listing_id=self.app_catalog_listing_id,
            app_catalog_listing_resource_version=self.app_catalog_listing_resource_version,
            description=self.description,
            id=self.id,
            image_id=self.image_id,
            listing_id=self.listing_id,
            operating_systems=self.operating_systems,
            package_type=self.package_type,
            package_version=self.package_version,
            publication_id=self.publication_id,
            resource_id=self.resource_id,
            resource_link=self.resource_link,
            time_created=self.time_created,
            variables=self.variables,
            version=self.version)


def get_publication_package(package_version: Optional[str] = None,
                            publication_id: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPublicationPackageResult:
    """
    This data source provides details about a specific Publication Package resource in Oracle Cloud Infrastructure Marketplace service.

    Gets the details of a specific package version within a given publication.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_publication_package = oci.Marketplace.get_publication_package(package_version=var["publication_package_package_version"],
        publication_id=oci_marketplace_publication["test_publication"]["id"])
    ```


    :param str package_version: The version of the package. Package versions are unique within a listing.
    :param str publication_id: The unique identifier for the publication.
    """
    __args__ = dict()
    __args__['packageVersion'] = package_version
    __args__['publicationId'] = publication_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Marketplace/getPublicationPackage:getPublicationPackage', __args__, opts=opts, typ=GetPublicationPackageResult).value

    return AwaitableGetPublicationPackageResult(
        app_catalog_listing_id=pulumi.get(__ret__, 'app_catalog_listing_id'),
        app_catalog_listing_resource_version=pulumi.get(__ret__, 'app_catalog_listing_resource_version'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        image_id=pulumi.get(__ret__, 'image_id'),
        listing_id=pulumi.get(__ret__, 'listing_id'),
        operating_systems=pulumi.get(__ret__, 'operating_systems'),
        package_type=pulumi.get(__ret__, 'package_type'),
        package_version=pulumi.get(__ret__, 'package_version'),
        publication_id=pulumi.get(__ret__, 'publication_id'),
        resource_id=pulumi.get(__ret__, 'resource_id'),
        resource_link=pulumi.get(__ret__, 'resource_link'),
        time_created=pulumi.get(__ret__, 'time_created'),
        variables=pulumi.get(__ret__, 'variables'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_publication_package)
def get_publication_package_output(package_version: Optional[pulumi.Input[str]] = None,
                                   publication_id: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPublicationPackageResult]:
    """
    This data source provides details about a specific Publication Package resource in Oracle Cloud Infrastructure Marketplace service.

    Gets the details of a specific package version within a given publication.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_publication_package = oci.Marketplace.get_publication_package(package_version=var["publication_package_package_version"],
        publication_id=oci_marketplace_publication["test_publication"]["id"])
    ```


    :param str package_version: The version of the package. Package versions are unique within a listing.
    :param str publication_id: The unique identifier for the publication.
    """
    ...
