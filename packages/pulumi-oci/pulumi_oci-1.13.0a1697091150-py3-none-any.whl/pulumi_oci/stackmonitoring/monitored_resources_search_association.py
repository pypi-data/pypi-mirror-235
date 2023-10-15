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

__all__ = ['MonitoredResourcesSearchAssociationArgs', 'MonitoredResourcesSearchAssociation']

@pulumi.input_type
class MonitoredResourcesSearchAssociationArgs:
    def __init__(__self__, *,
                 compartment_id: pulumi.Input[str],
                 association_type: Optional[pulumi.Input[str]] = None,
                 destination_resource_id: Optional[pulumi.Input[str]] = None,
                 destination_resource_name: Optional[pulumi.Input[str]] = None,
                 destination_resource_type: Optional[pulumi.Input[str]] = None,
                 source_resource_id: Optional[pulumi.Input[str]] = None,
                 source_resource_name: Optional[pulumi.Input[str]] = None,
                 source_resource_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a MonitoredResourcesSearchAssociation resource.
        :param pulumi.Input[str] compartment_id: Compartment Identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        :param pulumi.Input[str] association_type: Association type filter to search associated resources.
        :param pulumi.Input[str] destination_resource_id: Destination Monitored Resource Identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        :param pulumi.Input[str] destination_resource_name: Source Monitored Resource Name.
        :param pulumi.Input[str] destination_resource_type: Source Monitored Resource Type.
        :param pulumi.Input[str] source_resource_id: Source Monitored Resource Identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        :param pulumi.Input[str] source_resource_name: Source Monitored Resource Name.
        :param pulumi.Input[str] source_resource_type: Source Monitored Resource Type. 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        MonitoredResourcesSearchAssociationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            compartment_id=compartment_id,
            association_type=association_type,
            destination_resource_id=destination_resource_id,
            destination_resource_name=destination_resource_name,
            destination_resource_type=destination_resource_type,
            source_resource_id=source_resource_id,
            source_resource_name=source_resource_name,
            source_resource_type=source_resource_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             compartment_id: pulumi.Input[str],
             association_type: Optional[pulumi.Input[str]] = None,
             destination_resource_id: Optional[pulumi.Input[str]] = None,
             destination_resource_name: Optional[pulumi.Input[str]] = None,
             destination_resource_type: Optional[pulumi.Input[str]] = None,
             source_resource_id: Optional[pulumi.Input[str]] = None,
             source_resource_name: Optional[pulumi.Input[str]] = None,
             source_resource_type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("compartment_id", compartment_id)
        if association_type is not None:
            _setter("association_type", association_type)
        if destination_resource_id is not None:
            _setter("destination_resource_id", destination_resource_id)
        if destination_resource_name is not None:
            _setter("destination_resource_name", destination_resource_name)
        if destination_resource_type is not None:
            _setter("destination_resource_type", destination_resource_type)
        if source_resource_id is not None:
            _setter("source_resource_id", source_resource_id)
        if source_resource_name is not None:
            _setter("source_resource_name", source_resource_name)
        if source_resource_type is not None:
            _setter("source_resource_type", source_resource_type)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Input[str]:
        """
        Compartment Identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="associationType")
    def association_type(self) -> Optional[pulumi.Input[str]]:
        """
        Association type filter to search associated resources.
        """
        return pulumi.get(self, "association_type")

    @association_type.setter
    def association_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "association_type", value)

    @property
    @pulumi.getter(name="destinationResourceId")
    def destination_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        Destination Monitored Resource Identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        """
        return pulumi.get(self, "destination_resource_id")

    @destination_resource_id.setter
    def destination_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_resource_id", value)

    @property
    @pulumi.getter(name="destinationResourceName")
    def destination_resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        Source Monitored Resource Name.
        """
        return pulumi.get(self, "destination_resource_name")

    @destination_resource_name.setter
    def destination_resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_resource_name", value)

    @property
    @pulumi.getter(name="destinationResourceType")
    def destination_resource_type(self) -> Optional[pulumi.Input[str]]:
        """
        Source Monitored Resource Type.
        """
        return pulumi.get(self, "destination_resource_type")

    @destination_resource_type.setter
    def destination_resource_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_resource_type", value)

    @property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        Source Monitored Resource Identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        """
        return pulumi.get(self, "source_resource_id")

    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_resource_id", value)

    @property
    @pulumi.getter(name="sourceResourceName")
    def source_resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        Source Monitored Resource Name.
        """
        return pulumi.get(self, "source_resource_name")

    @source_resource_name.setter
    def source_resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_resource_name", value)

    @property
    @pulumi.getter(name="sourceResourceType")
    def source_resource_type(self) -> Optional[pulumi.Input[str]]:
        """
        Source Monitored Resource Type. 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "source_resource_type")

    @source_resource_type.setter
    def source_resource_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_resource_type", value)


@pulumi.input_type
class _MonitoredResourcesSearchAssociationState:
    def __init__(__self__, *,
                 association_type: Optional[pulumi.Input[str]] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 destination_resource_id: Optional[pulumi.Input[str]] = None,
                 destination_resource_name: Optional[pulumi.Input[str]] = None,
                 destination_resource_type: Optional[pulumi.Input[str]] = None,
                 items: Optional[pulumi.Input[Sequence[pulumi.Input['MonitoredResourcesSearchAssociationItemArgs']]]] = None,
                 source_resource_id: Optional[pulumi.Input[str]] = None,
                 source_resource_name: Optional[pulumi.Input[str]] = None,
                 source_resource_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering MonitoredResourcesSearchAssociation resources.
        :param pulumi.Input[str] association_type: Association type filter to search associated resources.
        :param pulumi.Input[str] compartment_id: Compartment Identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        :param pulumi.Input[str] destination_resource_id: Destination Monitored Resource Identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        :param pulumi.Input[str] destination_resource_name: Source Monitored Resource Name.
        :param pulumi.Input[str] destination_resource_type: Source Monitored Resource Type.
        :param pulumi.Input[Sequence[pulumi.Input['MonitoredResourcesSearchAssociationItemArgs']]] items: List of Monitored Resource Associations.
        :param pulumi.Input[str] source_resource_id: Source Monitored Resource Identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        :param pulumi.Input[str] source_resource_name: Source Monitored Resource Name.
        :param pulumi.Input[str] source_resource_type: Source Monitored Resource Type. 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        _MonitoredResourcesSearchAssociationState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            association_type=association_type,
            compartment_id=compartment_id,
            destination_resource_id=destination_resource_id,
            destination_resource_name=destination_resource_name,
            destination_resource_type=destination_resource_type,
            items=items,
            source_resource_id=source_resource_id,
            source_resource_name=source_resource_name,
            source_resource_type=source_resource_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             association_type: Optional[pulumi.Input[str]] = None,
             compartment_id: Optional[pulumi.Input[str]] = None,
             destination_resource_id: Optional[pulumi.Input[str]] = None,
             destination_resource_name: Optional[pulumi.Input[str]] = None,
             destination_resource_type: Optional[pulumi.Input[str]] = None,
             items: Optional[pulumi.Input[Sequence[pulumi.Input['MonitoredResourcesSearchAssociationItemArgs']]]] = None,
             source_resource_id: Optional[pulumi.Input[str]] = None,
             source_resource_name: Optional[pulumi.Input[str]] = None,
             source_resource_type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if association_type is not None:
            _setter("association_type", association_type)
        if compartment_id is not None:
            _setter("compartment_id", compartment_id)
        if destination_resource_id is not None:
            _setter("destination_resource_id", destination_resource_id)
        if destination_resource_name is not None:
            _setter("destination_resource_name", destination_resource_name)
        if destination_resource_type is not None:
            _setter("destination_resource_type", destination_resource_type)
        if items is not None:
            _setter("items", items)
        if source_resource_id is not None:
            _setter("source_resource_id", source_resource_id)
        if source_resource_name is not None:
            _setter("source_resource_name", source_resource_name)
        if source_resource_type is not None:
            _setter("source_resource_type", source_resource_type)

    @property
    @pulumi.getter(name="associationType")
    def association_type(self) -> Optional[pulumi.Input[str]]:
        """
        Association type filter to search associated resources.
        """
        return pulumi.get(self, "association_type")

    @association_type.setter
    def association_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "association_type", value)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        Compartment Identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="destinationResourceId")
    def destination_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        Destination Monitored Resource Identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        """
        return pulumi.get(self, "destination_resource_id")

    @destination_resource_id.setter
    def destination_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_resource_id", value)

    @property
    @pulumi.getter(name="destinationResourceName")
    def destination_resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        Source Monitored Resource Name.
        """
        return pulumi.get(self, "destination_resource_name")

    @destination_resource_name.setter
    def destination_resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_resource_name", value)

    @property
    @pulumi.getter(name="destinationResourceType")
    def destination_resource_type(self) -> Optional[pulumi.Input[str]]:
        """
        Source Monitored Resource Type.
        """
        return pulumi.get(self, "destination_resource_type")

    @destination_resource_type.setter
    def destination_resource_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_resource_type", value)

    @property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MonitoredResourcesSearchAssociationItemArgs']]]]:
        """
        List of Monitored Resource Associations.
        """
        return pulumi.get(self, "items")

    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MonitoredResourcesSearchAssociationItemArgs']]]]):
        pulumi.set(self, "items", value)

    @property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        Source Monitored Resource Identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        """
        return pulumi.get(self, "source_resource_id")

    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_resource_id", value)

    @property
    @pulumi.getter(name="sourceResourceName")
    def source_resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        Source Monitored Resource Name.
        """
        return pulumi.get(self, "source_resource_name")

    @source_resource_name.setter
    def source_resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_resource_name", value)

    @property
    @pulumi.getter(name="sourceResourceType")
    def source_resource_type(self) -> Optional[pulumi.Input[str]]:
        """
        Source Monitored Resource Type. 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "source_resource_type")

    @source_resource_type.setter
    def source_resource_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_resource_type", value)


class MonitoredResourcesSearchAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 association_type: Optional[pulumi.Input[str]] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 destination_resource_id: Optional[pulumi.Input[str]] = None,
                 destination_resource_name: Optional[pulumi.Input[str]] = None,
                 destination_resource_type: Optional[pulumi.Input[str]] = None,
                 source_resource_id: Optional[pulumi.Input[str]] = None,
                 source_resource_name: Optional[pulumi.Input[str]] = None,
                 source_resource_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Monitored Resources Search Association resource in Oracle Cloud Infrastructure Stack Monitoring service.

        Search associations in the given compartment based on the search criteria.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_monitored_resources_search_association = oci.stack_monitoring.MonitoredResourcesSearchAssociation("testMonitoredResourcesSearchAssociation",
            compartment_id=var["compartment_id"],
            association_type=var["monitored_resources_search_association_association_type"],
            destination_resource_id=oci_stack_monitoring_destination_resource["test_destination_resource"]["id"],
            destination_resource_name=var["monitored_resources_search_association_destination_resource_name"],
            destination_resource_type=var["monitored_resources_search_association_destination_resource_type"],
            source_resource_id=oci_stack_monitoring_source_resource["test_source_resource"]["id"],
            source_resource_name=var["monitored_resources_search_association_source_resource_name"],
            source_resource_type=var["monitored_resources_search_association_source_resource_type"])
        ```

        ## Import

        MonitoredResourcesSearchAssociations can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:StackMonitoring/monitoredResourcesSearchAssociation:MonitoredResourcesSearchAssociation test_monitored_resources_search_association "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] association_type: Association type filter to search associated resources.
        :param pulumi.Input[str] compartment_id: Compartment Identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        :param pulumi.Input[str] destination_resource_id: Destination Monitored Resource Identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        :param pulumi.Input[str] destination_resource_name: Source Monitored Resource Name.
        :param pulumi.Input[str] destination_resource_type: Source Monitored Resource Type.
        :param pulumi.Input[str] source_resource_id: Source Monitored Resource Identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        :param pulumi.Input[str] source_resource_name: Source Monitored Resource Name.
        :param pulumi.Input[str] source_resource_type: Source Monitored Resource Type. 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MonitoredResourcesSearchAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Monitored Resources Search Association resource in Oracle Cloud Infrastructure Stack Monitoring service.

        Search associations in the given compartment based on the search criteria.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_monitored_resources_search_association = oci.stack_monitoring.MonitoredResourcesSearchAssociation("testMonitoredResourcesSearchAssociation",
            compartment_id=var["compartment_id"],
            association_type=var["monitored_resources_search_association_association_type"],
            destination_resource_id=oci_stack_monitoring_destination_resource["test_destination_resource"]["id"],
            destination_resource_name=var["monitored_resources_search_association_destination_resource_name"],
            destination_resource_type=var["monitored_resources_search_association_destination_resource_type"],
            source_resource_id=oci_stack_monitoring_source_resource["test_source_resource"]["id"],
            source_resource_name=var["monitored_resources_search_association_source_resource_name"],
            source_resource_type=var["monitored_resources_search_association_source_resource_type"])
        ```

        ## Import

        MonitoredResourcesSearchAssociations can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:StackMonitoring/monitoredResourcesSearchAssociation:MonitoredResourcesSearchAssociation test_monitored_resources_search_association "id"
        ```

        :param str resource_name: The name of the resource.
        :param MonitoredResourcesSearchAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MonitoredResourcesSearchAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            MonitoredResourcesSearchAssociationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 association_type: Optional[pulumi.Input[str]] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 destination_resource_id: Optional[pulumi.Input[str]] = None,
                 destination_resource_name: Optional[pulumi.Input[str]] = None,
                 destination_resource_type: Optional[pulumi.Input[str]] = None,
                 source_resource_id: Optional[pulumi.Input[str]] = None,
                 source_resource_name: Optional[pulumi.Input[str]] = None,
                 source_resource_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MonitoredResourcesSearchAssociationArgs.__new__(MonitoredResourcesSearchAssociationArgs)

            __props__.__dict__["association_type"] = association_type
            if compartment_id is None and not opts.urn:
                raise TypeError("Missing required property 'compartment_id'")
            __props__.__dict__["compartment_id"] = compartment_id
            __props__.__dict__["destination_resource_id"] = destination_resource_id
            __props__.__dict__["destination_resource_name"] = destination_resource_name
            __props__.__dict__["destination_resource_type"] = destination_resource_type
            __props__.__dict__["source_resource_id"] = source_resource_id
            __props__.__dict__["source_resource_name"] = source_resource_name
            __props__.__dict__["source_resource_type"] = source_resource_type
            __props__.__dict__["items"] = None
        super(MonitoredResourcesSearchAssociation, __self__).__init__(
            'oci:StackMonitoring/monitoredResourcesSearchAssociation:MonitoredResourcesSearchAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            association_type: Optional[pulumi.Input[str]] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            destination_resource_id: Optional[pulumi.Input[str]] = None,
            destination_resource_name: Optional[pulumi.Input[str]] = None,
            destination_resource_type: Optional[pulumi.Input[str]] = None,
            items: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MonitoredResourcesSearchAssociationItemArgs']]]]] = None,
            source_resource_id: Optional[pulumi.Input[str]] = None,
            source_resource_name: Optional[pulumi.Input[str]] = None,
            source_resource_type: Optional[pulumi.Input[str]] = None) -> 'MonitoredResourcesSearchAssociation':
        """
        Get an existing MonitoredResourcesSearchAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] association_type: Association type filter to search associated resources.
        :param pulumi.Input[str] compartment_id: Compartment Identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        :param pulumi.Input[str] destination_resource_id: Destination Monitored Resource Identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        :param pulumi.Input[str] destination_resource_name: Source Monitored Resource Name.
        :param pulumi.Input[str] destination_resource_type: Source Monitored Resource Type.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MonitoredResourcesSearchAssociationItemArgs']]]] items: List of Monitored Resource Associations.
        :param pulumi.Input[str] source_resource_id: Source Monitored Resource Identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        :param pulumi.Input[str] source_resource_name: Source Monitored Resource Name.
        :param pulumi.Input[str] source_resource_type: Source Monitored Resource Type. 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MonitoredResourcesSearchAssociationState.__new__(_MonitoredResourcesSearchAssociationState)

        __props__.__dict__["association_type"] = association_type
        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["destination_resource_id"] = destination_resource_id
        __props__.__dict__["destination_resource_name"] = destination_resource_name
        __props__.__dict__["destination_resource_type"] = destination_resource_type
        __props__.__dict__["items"] = items
        __props__.__dict__["source_resource_id"] = source_resource_id
        __props__.__dict__["source_resource_name"] = source_resource_name
        __props__.__dict__["source_resource_type"] = source_resource_type
        return MonitoredResourcesSearchAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="associationType")
    def association_type(self) -> pulumi.Output[Optional[str]]:
        """
        Association type filter to search associated resources.
        """
        return pulumi.get(self, "association_type")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        Compartment Identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="destinationResourceId")
    def destination_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        Destination Monitored Resource Identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        """
        return pulumi.get(self, "destination_resource_id")

    @property
    @pulumi.getter(name="destinationResourceName")
    def destination_resource_name(self) -> pulumi.Output[Optional[str]]:
        """
        Source Monitored Resource Name.
        """
        return pulumi.get(self, "destination_resource_name")

    @property
    @pulumi.getter(name="destinationResourceType")
    def destination_resource_type(self) -> pulumi.Output[Optional[str]]:
        """
        Source Monitored Resource Type.
        """
        return pulumi.get(self, "destination_resource_type")

    @property
    @pulumi.getter
    def items(self) -> pulumi.Output[Sequence['outputs.MonitoredResourcesSearchAssociationItem']]:
        """
        List of Monitored Resource Associations.
        """
        return pulumi.get(self, "items")

    @property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        Source Monitored Resource Identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        """
        return pulumi.get(self, "source_resource_id")

    @property
    @pulumi.getter(name="sourceResourceName")
    def source_resource_name(self) -> pulumi.Output[Optional[str]]:
        """
        Source Monitored Resource Name.
        """
        return pulumi.get(self, "source_resource_name")

    @property
    @pulumi.getter(name="sourceResourceType")
    def source_resource_type(self) -> pulumi.Output[Optional[str]]:
        """
        Source Monitored Resource Type. 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "source_resource_type")

