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
    'GetDomainsMyOauth2clientCredentialsResult',
    'AwaitableGetDomainsMyOauth2clientCredentialsResult',
    'get_domains_my_oauth2client_credentials',
    'get_domains_my_oauth2client_credentials_output',
]

@pulumi.output_type
class GetDomainsMyOauth2clientCredentialsResult:
    """
    A collection of values returned by getDomainsMyOauth2clientCredentials.
    """
    def __init__(__self__, authorization=None, compartment_id=None, id=None, idcs_endpoint=None, items_per_page=None, my_oauth2client_credential_count=None, my_oauth2client_credential_filter=None, my_oauth2client_credentials=None, resource_type_schema_version=None, schemas=None, sort_by=None, sort_order=None, start_index=None, total_results=None):
        if authorization and not isinstance(authorization, str):
            raise TypeError("Expected argument 'authorization' to be a str")
        pulumi.set(__self__, "authorization", authorization)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if idcs_endpoint and not isinstance(idcs_endpoint, str):
            raise TypeError("Expected argument 'idcs_endpoint' to be a str")
        pulumi.set(__self__, "idcs_endpoint", idcs_endpoint)
        if items_per_page and not isinstance(items_per_page, int):
            raise TypeError("Expected argument 'items_per_page' to be a int")
        pulumi.set(__self__, "items_per_page", items_per_page)
        if my_oauth2client_credential_count and not isinstance(my_oauth2client_credential_count, int):
            raise TypeError("Expected argument 'my_oauth2client_credential_count' to be a int")
        pulumi.set(__self__, "my_oauth2client_credential_count", my_oauth2client_credential_count)
        if my_oauth2client_credential_filter and not isinstance(my_oauth2client_credential_filter, str):
            raise TypeError("Expected argument 'my_oauth2client_credential_filter' to be a str")
        pulumi.set(__self__, "my_oauth2client_credential_filter", my_oauth2client_credential_filter)
        if my_oauth2client_credentials and not isinstance(my_oauth2client_credentials, list):
            raise TypeError("Expected argument 'my_oauth2client_credentials' to be a list")
        pulumi.set(__self__, "my_oauth2client_credentials", my_oauth2client_credentials)
        if resource_type_schema_version and not isinstance(resource_type_schema_version, str):
            raise TypeError("Expected argument 'resource_type_schema_version' to be a str")
        pulumi.set(__self__, "resource_type_schema_version", resource_type_schema_version)
        if schemas and not isinstance(schemas, list):
            raise TypeError("Expected argument 'schemas' to be a list")
        pulumi.set(__self__, "schemas", schemas)
        if sort_by and not isinstance(sort_by, str):
            raise TypeError("Expected argument 'sort_by' to be a str")
        pulumi.set(__self__, "sort_by", sort_by)
        if sort_order and not isinstance(sort_order, str):
            raise TypeError("Expected argument 'sort_order' to be a str")
        pulumi.set(__self__, "sort_order", sort_order)
        if start_index and not isinstance(start_index, int):
            raise TypeError("Expected argument 'start_index' to be a int")
        pulumi.set(__self__, "start_index", start_index)
        if total_results and not isinstance(total_results, int):
            raise TypeError("Expected argument 'total_results' to be a int")
        pulumi.set(__self__, "total_results", total_results)

    @property
    @pulumi.getter
    def authorization(self) -> Optional[str]:
        return pulumi.get(self, "authorization")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="idcsEndpoint")
    def idcs_endpoint(self) -> str:
        return pulumi.get(self, "idcs_endpoint")

    @property
    @pulumi.getter(name="itemsPerPage")
    def items_per_page(self) -> int:
        return pulumi.get(self, "items_per_page")

    @property
    @pulumi.getter(name="myOauth2clientCredentialCount")
    def my_oauth2client_credential_count(self) -> Optional[int]:
        return pulumi.get(self, "my_oauth2client_credential_count")

    @property
    @pulumi.getter(name="myOauth2clientCredentialFilter")
    def my_oauth2client_credential_filter(self) -> Optional[str]:
        return pulumi.get(self, "my_oauth2client_credential_filter")

    @property
    @pulumi.getter(name="myOauth2clientCredentials")
    def my_oauth2client_credentials(self) -> Sequence['outputs.GetDomainsMyOauth2clientCredentialsMyOauth2clientCredentialResult']:
        """
        The list of my_oauth2client_credentials.
        """
        return pulumi.get(self, "my_oauth2client_credentials")

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
    @pulumi.getter(name="sortBy")
    def sort_by(self) -> Optional[str]:
        return pulumi.get(self, "sort_by")

    @property
    @pulumi.getter(name="sortOrder")
    def sort_order(self) -> Optional[str]:
        return pulumi.get(self, "sort_order")

    @property
    @pulumi.getter(name="startIndex")
    def start_index(self) -> Optional[int]:
        return pulumi.get(self, "start_index")

    @property
    @pulumi.getter(name="totalResults")
    def total_results(self) -> int:
        return pulumi.get(self, "total_results")


class AwaitableGetDomainsMyOauth2clientCredentialsResult(GetDomainsMyOauth2clientCredentialsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDomainsMyOauth2clientCredentialsResult(
            authorization=self.authorization,
            compartment_id=self.compartment_id,
            id=self.id,
            idcs_endpoint=self.idcs_endpoint,
            items_per_page=self.items_per_page,
            my_oauth2client_credential_count=self.my_oauth2client_credential_count,
            my_oauth2client_credential_filter=self.my_oauth2client_credential_filter,
            my_oauth2client_credentials=self.my_oauth2client_credentials,
            resource_type_schema_version=self.resource_type_schema_version,
            schemas=self.schemas,
            sort_by=self.sort_by,
            sort_order=self.sort_order,
            start_index=self.start_index,
            total_results=self.total_results)


def get_domains_my_oauth2client_credentials(authorization: Optional[str] = None,
                                            compartment_id: Optional[str] = None,
                                            idcs_endpoint: Optional[str] = None,
                                            my_oauth2client_credential_count: Optional[int] = None,
                                            my_oauth2client_credential_filter: Optional[str] = None,
                                            resource_type_schema_version: Optional[str] = None,
                                            sort_by: Optional[str] = None,
                                            sort_order: Optional[str] = None,
                                            start_index: Optional[int] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDomainsMyOauth2clientCredentialsResult:
    """
    This data source provides the list of My O Auth2 Client Credentials in Oracle Cloud Infrastructure Identity Domains service.

    Search for a user's own OAuth2 client credential.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_my_oauth2client_credentials = oci.Identity.get_domains_my_oauth2client_credentials(idcs_endpoint=data["oci_identity_domain"]["test_domain"]["url"],
        my_oauth2client_credential_count=var["my_oauth2client_credential_my_oauth2client_credential_count"],
        my_oauth2client_credential_filter=var["my_oauth2client_credential_my_oauth2client_credential_filter"],
        authorization=var["my_oauth2client_credential_authorization"],
        resource_type_schema_version=var["my_oauth2client_credential_resource_type_schema_version"],
        start_index=var["my_oauth2client_credential_start_index"])
    ```


    :param str authorization: The Authorization field value consists of credentials containing the authentication information of the user agent for the realm of the resource being requested.
    :param str idcs_endpoint: The basic endpoint for the identity domain
    :param int my_oauth2client_credential_count: OPTIONAL. An integer that indicates the desired maximum number of query results per page. 1000 is the largest value that you can use. See the Pagination section of the System for Cross-Domain Identity Management Protocol specification for more information. (Section 3.4.2.4).
    :param str my_oauth2client_credential_filter: OPTIONAL. The filter string that is used to request a subset of resources. The filter string MUST be a valid filter expression. See the Filtering section of the SCIM specification for more information (Section 3.4.2.2). The string should contain at least one condition that each item must match in order to be returned in the search results. Each condition specifies an attribute, an operator, and a value. Conditions within a filter can be connected by logical operators (such as AND and OR). Sets of conditions can be grouped together using parentheses.
    :param str resource_type_schema_version: An endpoint-specific schema version number to use in the Request. Allowed version values are Earliest Version or Latest Version as specified in each REST API endpoint description, or any sequential number inbetween. All schema attributes/body parameters are a part of version 1. After version 1, any attributes added or deprecated will be tagged with the version that they were added to or deprecated in. If no version is provided, the latest schema version is returned.
    :param int start_index: OPTIONAL. An integer that indicates the 1-based index of the first query result. See the Pagination section of the SCIM specification for more information. (Section 3.4.2.4). The number of results pages to return. The first page is 1. Specify 2 to access the second page of results, and so on.
    """
    __args__ = dict()
    __args__['authorization'] = authorization
    __args__['compartmentId'] = compartment_id
    __args__['idcsEndpoint'] = idcs_endpoint
    __args__['myOauth2clientCredentialCount'] = my_oauth2client_credential_count
    __args__['myOauth2clientCredentialFilter'] = my_oauth2client_credential_filter
    __args__['resourceTypeSchemaVersion'] = resource_type_schema_version
    __args__['sortBy'] = sort_by
    __args__['sortOrder'] = sort_order
    __args__['startIndex'] = start_index
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Identity/getDomainsMyOauth2clientCredentials:getDomainsMyOauth2clientCredentials', __args__, opts=opts, typ=GetDomainsMyOauth2clientCredentialsResult).value

    return AwaitableGetDomainsMyOauth2clientCredentialsResult(
        authorization=pulumi.get(__ret__, 'authorization'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        id=pulumi.get(__ret__, 'id'),
        idcs_endpoint=pulumi.get(__ret__, 'idcs_endpoint'),
        items_per_page=pulumi.get(__ret__, 'items_per_page'),
        my_oauth2client_credential_count=pulumi.get(__ret__, 'my_oauth2client_credential_count'),
        my_oauth2client_credential_filter=pulumi.get(__ret__, 'my_oauth2client_credential_filter'),
        my_oauth2client_credentials=pulumi.get(__ret__, 'my_oauth2client_credentials'),
        resource_type_schema_version=pulumi.get(__ret__, 'resource_type_schema_version'),
        schemas=pulumi.get(__ret__, 'schemas'),
        sort_by=pulumi.get(__ret__, 'sort_by'),
        sort_order=pulumi.get(__ret__, 'sort_order'),
        start_index=pulumi.get(__ret__, 'start_index'),
        total_results=pulumi.get(__ret__, 'total_results'))


@_utilities.lift_output_func(get_domains_my_oauth2client_credentials)
def get_domains_my_oauth2client_credentials_output(authorization: Optional[pulumi.Input[Optional[str]]] = None,
                                                   compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                                                   idcs_endpoint: Optional[pulumi.Input[str]] = None,
                                                   my_oauth2client_credential_count: Optional[pulumi.Input[Optional[int]]] = None,
                                                   my_oauth2client_credential_filter: Optional[pulumi.Input[Optional[str]]] = None,
                                                   resource_type_schema_version: Optional[pulumi.Input[Optional[str]]] = None,
                                                   sort_by: Optional[pulumi.Input[Optional[str]]] = None,
                                                   sort_order: Optional[pulumi.Input[Optional[str]]] = None,
                                                   start_index: Optional[pulumi.Input[Optional[int]]] = None,
                                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDomainsMyOauth2clientCredentialsResult]:
    """
    This data source provides the list of My O Auth2 Client Credentials in Oracle Cloud Infrastructure Identity Domains service.

    Search for a user's own OAuth2 client credential.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_my_oauth2client_credentials = oci.Identity.get_domains_my_oauth2client_credentials(idcs_endpoint=data["oci_identity_domain"]["test_domain"]["url"],
        my_oauth2client_credential_count=var["my_oauth2client_credential_my_oauth2client_credential_count"],
        my_oauth2client_credential_filter=var["my_oauth2client_credential_my_oauth2client_credential_filter"],
        authorization=var["my_oauth2client_credential_authorization"],
        resource_type_schema_version=var["my_oauth2client_credential_resource_type_schema_version"],
        start_index=var["my_oauth2client_credential_start_index"])
    ```


    :param str authorization: The Authorization field value consists of credentials containing the authentication information of the user agent for the realm of the resource being requested.
    :param str idcs_endpoint: The basic endpoint for the identity domain
    :param int my_oauth2client_credential_count: OPTIONAL. An integer that indicates the desired maximum number of query results per page. 1000 is the largest value that you can use. See the Pagination section of the System for Cross-Domain Identity Management Protocol specification for more information. (Section 3.4.2.4).
    :param str my_oauth2client_credential_filter: OPTIONAL. The filter string that is used to request a subset of resources. The filter string MUST be a valid filter expression. See the Filtering section of the SCIM specification for more information (Section 3.4.2.2). The string should contain at least one condition that each item must match in order to be returned in the search results. Each condition specifies an attribute, an operator, and a value. Conditions within a filter can be connected by logical operators (such as AND and OR). Sets of conditions can be grouped together using parentheses.
    :param str resource_type_schema_version: An endpoint-specific schema version number to use in the Request. Allowed version values are Earliest Version or Latest Version as specified in each REST API endpoint description, or any sequential number inbetween. All schema attributes/body parameters are a part of version 1. After version 1, any attributes added or deprecated will be tagged with the version that they were added to or deprecated in. If no version is provided, the latest schema version is returned.
    :param int start_index: OPTIONAL. An integer that indicates the 1-based index of the first query result. See the Pagination section of the SCIM specification for more information. (Section 3.4.2.4). The number of results pages to return. The first page is 1. Specify 2 to access the second page of results, and so on.
    """
    ...
