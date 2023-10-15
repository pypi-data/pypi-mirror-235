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
    'GetDomainsAppRoleResult',
    'AwaitableGetDomainsAppRoleResult',
    'get_domains_app_role',
    'get_domains_app_role_output',
]

@pulumi.output_type
class GetDomainsAppRoleResult:
    """
    A collection of values returned by getDomainsAppRole.
    """
    def __init__(__self__, admin_role=None, app_role_id=None, apps=None, attribute_sets=None, attributes=None, authorization=None, available_to_clients=None, available_to_groups=None, available_to_users=None, compartment_ocid=None, delete_in_progress=None, description=None, display_name=None, domain_ocid=None, id=None, idcs_created_bies=None, idcs_endpoint=None, idcs_last_modified_bies=None, idcs_last_upgraded_in_release=None, idcs_prevented_operations=None, legacy_group_name=None, limited_to_one_or_more_groups=None, localized_display_name=None, members=None, metas=None, ocid=None, public=None, resource_type_schema_version=None, schemas=None, tags=None, tenancy_ocid=None, unique_name=None):
        if admin_role and not isinstance(admin_role, bool):
            raise TypeError("Expected argument 'admin_role' to be a bool")
        pulumi.set(__self__, "admin_role", admin_role)
        if app_role_id and not isinstance(app_role_id, str):
            raise TypeError("Expected argument 'app_role_id' to be a str")
        pulumi.set(__self__, "app_role_id", app_role_id)
        if apps and not isinstance(apps, list):
            raise TypeError("Expected argument 'apps' to be a list")
        pulumi.set(__self__, "apps", apps)
        if attribute_sets and not isinstance(attribute_sets, list):
            raise TypeError("Expected argument 'attribute_sets' to be a list")
        pulumi.set(__self__, "attribute_sets", attribute_sets)
        if attributes and not isinstance(attributes, str):
            raise TypeError("Expected argument 'attributes' to be a str")
        pulumi.set(__self__, "attributes", attributes)
        if authorization and not isinstance(authorization, str):
            raise TypeError("Expected argument 'authorization' to be a str")
        pulumi.set(__self__, "authorization", authorization)
        if available_to_clients and not isinstance(available_to_clients, bool):
            raise TypeError("Expected argument 'available_to_clients' to be a bool")
        pulumi.set(__self__, "available_to_clients", available_to_clients)
        if available_to_groups and not isinstance(available_to_groups, bool):
            raise TypeError("Expected argument 'available_to_groups' to be a bool")
        pulumi.set(__self__, "available_to_groups", available_to_groups)
        if available_to_users and not isinstance(available_to_users, bool):
            raise TypeError("Expected argument 'available_to_users' to be a bool")
        pulumi.set(__self__, "available_to_users", available_to_users)
        if compartment_ocid and not isinstance(compartment_ocid, str):
            raise TypeError("Expected argument 'compartment_ocid' to be a str")
        pulumi.set(__self__, "compartment_ocid", compartment_ocid)
        if delete_in_progress and not isinstance(delete_in_progress, bool):
            raise TypeError("Expected argument 'delete_in_progress' to be a bool")
        pulumi.set(__self__, "delete_in_progress", delete_in_progress)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if domain_ocid and not isinstance(domain_ocid, str):
            raise TypeError("Expected argument 'domain_ocid' to be a str")
        pulumi.set(__self__, "domain_ocid", domain_ocid)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if idcs_created_bies and not isinstance(idcs_created_bies, list):
            raise TypeError("Expected argument 'idcs_created_bies' to be a list")
        pulumi.set(__self__, "idcs_created_bies", idcs_created_bies)
        if idcs_endpoint and not isinstance(idcs_endpoint, str):
            raise TypeError("Expected argument 'idcs_endpoint' to be a str")
        pulumi.set(__self__, "idcs_endpoint", idcs_endpoint)
        if idcs_last_modified_bies and not isinstance(idcs_last_modified_bies, list):
            raise TypeError("Expected argument 'idcs_last_modified_bies' to be a list")
        pulumi.set(__self__, "idcs_last_modified_bies", idcs_last_modified_bies)
        if idcs_last_upgraded_in_release and not isinstance(idcs_last_upgraded_in_release, str):
            raise TypeError("Expected argument 'idcs_last_upgraded_in_release' to be a str")
        pulumi.set(__self__, "idcs_last_upgraded_in_release", idcs_last_upgraded_in_release)
        if idcs_prevented_operations and not isinstance(idcs_prevented_operations, list):
            raise TypeError("Expected argument 'idcs_prevented_operations' to be a list")
        pulumi.set(__self__, "idcs_prevented_operations", idcs_prevented_operations)
        if legacy_group_name and not isinstance(legacy_group_name, str):
            raise TypeError("Expected argument 'legacy_group_name' to be a str")
        pulumi.set(__self__, "legacy_group_name", legacy_group_name)
        if limited_to_one_or_more_groups and not isinstance(limited_to_one_or_more_groups, bool):
            raise TypeError("Expected argument 'limited_to_one_or_more_groups' to be a bool")
        pulumi.set(__self__, "limited_to_one_or_more_groups", limited_to_one_or_more_groups)
        if localized_display_name and not isinstance(localized_display_name, str):
            raise TypeError("Expected argument 'localized_display_name' to be a str")
        pulumi.set(__self__, "localized_display_name", localized_display_name)
        if members and not isinstance(members, list):
            raise TypeError("Expected argument 'members' to be a list")
        pulumi.set(__self__, "members", members)
        if metas and not isinstance(metas, list):
            raise TypeError("Expected argument 'metas' to be a list")
        pulumi.set(__self__, "metas", metas)
        if ocid and not isinstance(ocid, str):
            raise TypeError("Expected argument 'ocid' to be a str")
        pulumi.set(__self__, "ocid", ocid)
        if public and not isinstance(public, bool):
            raise TypeError("Expected argument 'public' to be a bool")
        pulumi.set(__self__, "public", public)
        if resource_type_schema_version and not isinstance(resource_type_schema_version, str):
            raise TypeError("Expected argument 'resource_type_schema_version' to be a str")
        pulumi.set(__self__, "resource_type_schema_version", resource_type_schema_version)
        if schemas and not isinstance(schemas, list):
            raise TypeError("Expected argument 'schemas' to be a list")
        pulumi.set(__self__, "schemas", schemas)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if tenancy_ocid and not isinstance(tenancy_ocid, str):
            raise TypeError("Expected argument 'tenancy_ocid' to be a str")
        pulumi.set(__self__, "tenancy_ocid", tenancy_ocid)
        if unique_name and not isinstance(unique_name, str):
            raise TypeError("Expected argument 'unique_name' to be a str")
        pulumi.set(__self__, "unique_name", unique_name)

    @property
    @pulumi.getter(name="adminRole")
    def admin_role(self) -> bool:
        """
        If true, the role provides administrative access privileges.
        """
        return pulumi.get(self, "admin_role")

    @property
    @pulumi.getter(name="appRoleId")
    def app_role_id(self) -> str:
        return pulumi.get(self, "app_role_id")

    @property
    @pulumi.getter
    def apps(self) -> Sequence['outputs.GetDomainsAppRoleAppResult']:
        """
        A unique identifier for the application that references this role.
        """
        return pulumi.get(self, "apps")

    @property
    @pulumi.getter(name="attributeSets")
    def attribute_sets(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "attribute_sets")

    @property
    @pulumi.getter
    def attributes(self) -> Optional[str]:
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter
    def authorization(self) -> Optional[str]:
        return pulumi.get(self, "authorization")

    @property
    @pulumi.getter(name="availableToClients")
    def available_to_clients(self) -> bool:
        """
        If true, this AppRole can be granted to Apps.
        """
        return pulumi.get(self, "available_to_clients")

    @property
    @pulumi.getter(name="availableToGroups")
    def available_to_groups(self) -> bool:
        """
        If true, this AppRole can be granted to Groups.
        """
        return pulumi.get(self, "available_to_groups")

    @property
    @pulumi.getter(name="availableToUsers")
    def available_to_users(self) -> bool:
        """
        If true, this AppRole can be granted to Users.
        """
        return pulumi.get(self, "available_to_users")

    @property
    @pulumi.getter(name="compartmentOcid")
    def compartment_ocid(self) -> str:
        """
        Oracle Cloud Infrastructure Compartment Id (ocid) in which the resource lives.
        """
        return pulumi.get(self, "compartment_ocid")

    @property
    @pulumi.getter(name="deleteInProgress")
    def delete_in_progress(self) -> bool:
        """
        A boolean flag indicating this resource in the process of being deleted. Usually set to true when synchronous deletion of the resource would take too long.
        """
        return pulumi.get(self, "delete_in_progress")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        AppRole description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        AppRole name
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="domainOcid")
    def domain_ocid(self) -> str:
        """
        Oracle Cloud Infrastructure Domain Id (ocid) in which the resource lives.
        """
        return pulumi.get(self, "domain_ocid")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Unique identifier for the SCIM Resource as defined by the Service Provider. Each representation of the Resource MUST include a non-empty id value. This identifier MUST be unique across the Service Provider's entire set of Resources. It MUST be a stable, non-reassignable identifier that does not change when the same Resource is returned in subsequent requests. The value of the id attribute is always issued by the Service Provider and MUST never be specified by the Service Consumer. bulkId: is a reserved keyword and MUST NOT be used in the unique identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="idcsCreatedBies")
    def idcs_created_bies(self) -> Sequence['outputs.GetDomainsAppRoleIdcsCreatedByResult']:
        """
        The User or App who created the Resource
        """
        return pulumi.get(self, "idcs_created_bies")

    @property
    @pulumi.getter(name="idcsEndpoint")
    def idcs_endpoint(self) -> str:
        return pulumi.get(self, "idcs_endpoint")

    @property
    @pulumi.getter(name="idcsLastModifiedBies")
    def idcs_last_modified_bies(self) -> Sequence['outputs.GetDomainsAppRoleIdcsLastModifiedByResult']:
        """
        The User or App who modified the Resource
        """
        return pulumi.get(self, "idcs_last_modified_bies")

    @property
    @pulumi.getter(name="idcsLastUpgradedInRelease")
    def idcs_last_upgraded_in_release(self) -> str:
        """
        The release number when the resource was upgraded.
        """
        return pulumi.get(self, "idcs_last_upgraded_in_release")

    @property
    @pulumi.getter(name="idcsPreventedOperations")
    def idcs_prevented_operations(self) -> Sequence[str]:
        """
        Each value of this attribute specifies an operation that only an internal client may perform on this particular resource.
        """
        return pulumi.get(self, "idcs_prevented_operations")

    @property
    @pulumi.getter(name="legacyGroupName")
    def legacy_group_name(self) -> str:
        """
        The name of the legacy group associated with this AppRole.
        """
        return pulumi.get(self, "legacy_group_name")

    @property
    @pulumi.getter(name="limitedToOneOrMoreGroups")
    def limited_to_one_or_more_groups(self) -> bool:
        """
        If true, indicates that this Oracle Identity Cloud Service AppRole can be granted to a delegated administrator whose scope is limited to users that are members of one or more groups.
        """
        return pulumi.get(self, "limited_to_one_or_more_groups")

    @property
    @pulumi.getter(name="localizedDisplayName")
    def localized_display_name(self) -> str:
        """
        AppRole localization name
        """
        return pulumi.get(self, "localized_display_name")

    @property
    @pulumi.getter
    def members(self) -> Sequence['outputs.GetDomainsAppRoleMemberResult']:
        """
        AppRole members - when requesting members attribute, it is recommended to use startIndex and count to return members in pages instead of in a single response, eg : #attributes=members[startIndex=1%26count=10]
        """
        return pulumi.get(self, "members")

    @property
    @pulumi.getter
    def metas(self) -> Sequence['outputs.GetDomainsAppRoleMetaResult']:
        """
        A complex attribute that contains resource metadata. All sub-attributes are OPTIONAL.
        """
        return pulumi.get(self, "metas")

    @property
    @pulumi.getter
    def ocid(self) -> str:
        """
        Unique Oracle Cloud Infrastructure identifier for the SCIM Resource.
        """
        return pulumi.get(self, "ocid")

    @property
    @pulumi.getter
    def public(self) -> bool:
        """
        If true, this AppRole is available automatically to every Oracle Identity Cloud Service User in this tenancy. There is no need to grant it to individual Users or Groups.
        """
        return pulumi.get(self, "public")

    @property
    @pulumi.getter(name="resourceTypeSchemaVersion")
    def resource_type_schema_version(self) -> Optional[str]:
        return pulumi.get(self, "resource_type_schema_version")

    @property
    @pulumi.getter
    def schemas(self) -> Sequence[str]:
        """
        REQUIRED. The schemas attribute is an array of Strings which allows introspection of the supported schema version for a SCIM representation as well any schema extensions supported by that representation. Each String value must be a unique URI. This specification defines URIs for User, Group, and a standard \\"enterprise\\" extension. All representations of SCIM schema MUST include a non-zero value array with value(s) of the URIs supported by that representation. Duplicate values MUST NOT be included. Value order is not specified and MUST not impact behavior.
        """
        return pulumi.get(self, "schemas")

    @property
    @pulumi.getter
    def tags(self) -> Sequence['outputs.GetDomainsAppRoleTagResult']:
        """
        A list of tags on this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tenancyOcid")
    def tenancy_ocid(self) -> str:
        """
        Oracle Cloud Infrastructure Tenant Id (ocid) in which the resource lives.
        """
        return pulumi.get(self, "tenancy_ocid")

    @property
    @pulumi.getter(name="uniqueName")
    def unique_name(self) -> str:
        """
        AppRole unique name
        """
        return pulumi.get(self, "unique_name")


class AwaitableGetDomainsAppRoleResult(GetDomainsAppRoleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDomainsAppRoleResult(
            admin_role=self.admin_role,
            app_role_id=self.app_role_id,
            apps=self.apps,
            attribute_sets=self.attribute_sets,
            attributes=self.attributes,
            authorization=self.authorization,
            available_to_clients=self.available_to_clients,
            available_to_groups=self.available_to_groups,
            available_to_users=self.available_to_users,
            compartment_ocid=self.compartment_ocid,
            delete_in_progress=self.delete_in_progress,
            description=self.description,
            display_name=self.display_name,
            domain_ocid=self.domain_ocid,
            id=self.id,
            idcs_created_bies=self.idcs_created_bies,
            idcs_endpoint=self.idcs_endpoint,
            idcs_last_modified_bies=self.idcs_last_modified_bies,
            idcs_last_upgraded_in_release=self.idcs_last_upgraded_in_release,
            idcs_prevented_operations=self.idcs_prevented_operations,
            legacy_group_name=self.legacy_group_name,
            limited_to_one_or_more_groups=self.limited_to_one_or_more_groups,
            localized_display_name=self.localized_display_name,
            members=self.members,
            metas=self.metas,
            ocid=self.ocid,
            public=self.public,
            resource_type_schema_version=self.resource_type_schema_version,
            schemas=self.schemas,
            tags=self.tags,
            tenancy_ocid=self.tenancy_ocid,
            unique_name=self.unique_name)


def get_domains_app_role(app_role_id: Optional[str] = None,
                         attribute_sets: Optional[Sequence[str]] = None,
                         attributes: Optional[str] = None,
                         authorization: Optional[str] = None,
                         idcs_endpoint: Optional[str] = None,
                         resource_type_schema_version: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDomainsAppRoleResult:
    """
    This data source provides details about a specific App Role resource in Oracle Cloud Infrastructure Identity Domains service.

    Get an AppRole

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_app_role = oci.Identity.get_domains_app_role(app_role_id=oci_identity_domains_app_role["test_app_role"]["id"],
        idcs_endpoint=data["oci_identity_domain"]["test_domain"]["url"],
        attribute_sets=["all"],
        attributes="",
        authorization=var["app_role_authorization"],
        resource_type_schema_version=var["app_role_resource_type_schema_version"])
    ```


    :param str app_role_id: ID of the resource
    :param Sequence[str] attribute_sets: A multi-valued list of strings indicating the return type of attribute definition. The specified set of attributes can be fetched by the return type of the attribute. One or more values can be given together to fetch more than one group of attributes. If 'attributes' query parameter is also available, union of the two is fetched. Valid values - all, always, never, request, default. Values are case-insensitive.
    :param str attributes: A comma-delimited string that specifies the names of resource attributes that should be returned in the response. By default, a response that contains resource attributes contains only attributes that are defined in the schema for that resource type as returned=always or returned=default. An attribute that is defined as returned=request is returned in a response only if the request specifies its name in the value of this query parameter. If a request specifies this query parameter, the response contains the attributes that this query parameter specifies, as well as any attribute that is defined as returned=always.
    :param str authorization: The Authorization field value consists of credentials containing the authentication information of the user agent for the realm of the resource being requested.
    :param str idcs_endpoint: The basic endpoint for the identity domain
    :param str resource_type_schema_version: An endpoint-specific schema version number to use in the Request. Allowed version values are Earliest Version or Latest Version as specified in each REST API endpoint description, or any sequential number inbetween. All schema attributes/body parameters are a part of version 1. After version 1, any attributes added or deprecated will be tagged with the version that they were added to or deprecated in. If no version is provided, the latest schema version is returned.
    """
    __args__ = dict()
    __args__['appRoleId'] = app_role_id
    __args__['attributeSets'] = attribute_sets
    __args__['attributes'] = attributes
    __args__['authorization'] = authorization
    __args__['idcsEndpoint'] = idcs_endpoint
    __args__['resourceTypeSchemaVersion'] = resource_type_schema_version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Identity/getDomainsAppRole:getDomainsAppRole', __args__, opts=opts, typ=GetDomainsAppRoleResult).value

    return AwaitableGetDomainsAppRoleResult(
        admin_role=pulumi.get(__ret__, 'admin_role'),
        app_role_id=pulumi.get(__ret__, 'app_role_id'),
        apps=pulumi.get(__ret__, 'apps'),
        attribute_sets=pulumi.get(__ret__, 'attribute_sets'),
        attributes=pulumi.get(__ret__, 'attributes'),
        authorization=pulumi.get(__ret__, 'authorization'),
        available_to_clients=pulumi.get(__ret__, 'available_to_clients'),
        available_to_groups=pulumi.get(__ret__, 'available_to_groups'),
        available_to_users=pulumi.get(__ret__, 'available_to_users'),
        compartment_ocid=pulumi.get(__ret__, 'compartment_ocid'),
        delete_in_progress=pulumi.get(__ret__, 'delete_in_progress'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        domain_ocid=pulumi.get(__ret__, 'domain_ocid'),
        id=pulumi.get(__ret__, 'id'),
        idcs_created_bies=pulumi.get(__ret__, 'idcs_created_bies'),
        idcs_endpoint=pulumi.get(__ret__, 'idcs_endpoint'),
        idcs_last_modified_bies=pulumi.get(__ret__, 'idcs_last_modified_bies'),
        idcs_last_upgraded_in_release=pulumi.get(__ret__, 'idcs_last_upgraded_in_release'),
        idcs_prevented_operations=pulumi.get(__ret__, 'idcs_prevented_operations'),
        legacy_group_name=pulumi.get(__ret__, 'legacy_group_name'),
        limited_to_one_or_more_groups=pulumi.get(__ret__, 'limited_to_one_or_more_groups'),
        localized_display_name=pulumi.get(__ret__, 'localized_display_name'),
        members=pulumi.get(__ret__, 'members'),
        metas=pulumi.get(__ret__, 'metas'),
        ocid=pulumi.get(__ret__, 'ocid'),
        public=pulumi.get(__ret__, 'public'),
        resource_type_schema_version=pulumi.get(__ret__, 'resource_type_schema_version'),
        schemas=pulumi.get(__ret__, 'schemas'),
        tags=pulumi.get(__ret__, 'tags'),
        tenancy_ocid=pulumi.get(__ret__, 'tenancy_ocid'),
        unique_name=pulumi.get(__ret__, 'unique_name'))


@_utilities.lift_output_func(get_domains_app_role)
def get_domains_app_role_output(app_role_id: Optional[pulumi.Input[str]] = None,
                                attribute_sets: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                attributes: Optional[pulumi.Input[Optional[str]]] = None,
                                authorization: Optional[pulumi.Input[Optional[str]]] = None,
                                idcs_endpoint: Optional[pulumi.Input[str]] = None,
                                resource_type_schema_version: Optional[pulumi.Input[Optional[str]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDomainsAppRoleResult]:
    """
    This data source provides details about a specific App Role resource in Oracle Cloud Infrastructure Identity Domains service.

    Get an AppRole

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_app_role = oci.Identity.get_domains_app_role(app_role_id=oci_identity_domains_app_role["test_app_role"]["id"],
        idcs_endpoint=data["oci_identity_domain"]["test_domain"]["url"],
        attribute_sets=["all"],
        attributes="",
        authorization=var["app_role_authorization"],
        resource_type_schema_version=var["app_role_resource_type_schema_version"])
    ```


    :param str app_role_id: ID of the resource
    :param Sequence[str] attribute_sets: A multi-valued list of strings indicating the return type of attribute definition. The specified set of attributes can be fetched by the return type of the attribute. One or more values can be given together to fetch more than one group of attributes. If 'attributes' query parameter is also available, union of the two is fetched. Valid values - all, always, never, request, default. Values are case-insensitive.
    :param str attributes: A comma-delimited string that specifies the names of resource attributes that should be returned in the response. By default, a response that contains resource attributes contains only attributes that are defined in the schema for that resource type as returned=always or returned=default. An attribute that is defined as returned=request is returned in a response only if the request specifies its name in the value of this query parameter. If a request specifies this query parameter, the response contains the attributes that this query parameter specifies, as well as any attribute that is defined as returned=always.
    :param str authorization: The Authorization field value consists of credentials containing the authentication information of the user agent for the realm of the resource being requested.
    :param str idcs_endpoint: The basic endpoint for the identity domain
    :param str resource_type_schema_version: An endpoint-specific schema version number to use in the Request. Allowed version values are Earliest Version or Latest Version as specified in each REST API endpoint description, or any sequential number inbetween. All schema attributes/body parameters are a part of version 1. After version 1, any attributes added or deprecated will be tagged with the version that they were added to or deprecated in. If no version is provided, the latest schema version is returned.
    """
    ...
