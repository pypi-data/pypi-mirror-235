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

__all__ = ['AtCustomerCccUpgradeScheduleArgs', 'AtCustomerCccUpgradeSchedule']

@pulumi.input_type
class AtCustomerCccUpgradeScheduleArgs:
    def __init__(__self__, *,
                 compartment_id: pulumi.Input[str],
                 display_name: pulumi.Input[str],
                 events: pulumi.Input[Sequence[pulumi.Input['AtCustomerCccUpgradeScheduleEventArgs']]],
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a AtCustomerCccUpgradeSchedule resource.
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the Compute Cloud@Customer Upgrade Schedule.
        :param pulumi.Input[str] display_name: (Updatable) Compute Cloud@Customer upgrade schedule display name. Avoid entering confidential information.
        :param pulumi.Input[Sequence[pulumi.Input['AtCustomerCccUpgradeScheduleEventArgs']]] events: (Updatable) List of preferred times for Compute Cloud@Customer infrastructure to be upgraded.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) A description of the Compute Cloud@Customer upgrade schedule time block.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        AtCustomerCccUpgradeScheduleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            compartment_id=compartment_id,
            display_name=display_name,
            events=events,
            defined_tags=defined_tags,
            description=description,
            freeform_tags=freeform_tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             compartment_id: pulumi.Input[str],
             display_name: pulumi.Input[str],
             events: pulumi.Input[Sequence[pulumi.Input['AtCustomerCccUpgradeScheduleEventArgs']]],
             defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             description: Optional[pulumi.Input[str]] = None,
             freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("compartment_id", compartment_id)
        _setter("display_name", display_name)
        _setter("events", events)
        if defined_tags is not None:
            _setter("defined_tags", defined_tags)
        if description is not None:
            _setter("description", description)
        if freeform_tags is not None:
            _setter("freeform_tags", freeform_tags)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Input[str]:
        """
        (Updatable) Compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the Compute Cloud@Customer Upgrade Schedule.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        (Updatable) Compute Cloud@Customer upgrade schedule display name. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def events(self) -> pulumi.Input[Sequence[pulumi.Input['AtCustomerCccUpgradeScheduleEventArgs']]]:
        """
        (Updatable) List of preferred times for Compute Cloud@Customer infrastructure to be upgraded.
        """
        return pulumi.get(self, "events")

    @events.setter
    def events(self, value: pulumi.Input[Sequence[pulumi.Input['AtCustomerCccUpgradeScheduleEventArgs']]]):
        pulumi.set(self, "events", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) A description of the Compute Cloud@Customer upgrade schedule time block.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}` 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)


@pulumi.input_type
class _AtCustomerCccUpgradeScheduleState:
    def __init__(__self__, *,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 events: Optional[pulumi.Input[Sequence[pulumi.Input['AtCustomerCccUpgradeScheduleEventArgs']]]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 infrastructure_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 lifecycle_details: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 system_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 time_updated: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AtCustomerCccUpgradeSchedule resources.
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the Compute Cloud@Customer Upgrade Schedule.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) A description of the Compute Cloud@Customer upgrade schedule time block.
        :param pulumi.Input[str] display_name: (Updatable) Compute Cloud@Customer upgrade schedule display name. Avoid entering confidential information.
        :param pulumi.Input[Sequence[pulumi.Input['AtCustomerCccUpgradeScheduleEventArgs']]] events: (Updatable) List of preferred times for Compute Cloud@Customer infrastructure to be upgraded.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[Sequence[pulumi.Input[str]]] infrastructure_ids: List of Compute Cloud@Customer infrastructure [OCIDs](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that are using this upgrade schedule.
        :param pulumi.Input[str] lifecycle_details: A message describing the current state in more detail. For example, the message can be used to provide actionable information for a resource in a Failed state.
        :param pulumi.Input[str] state: Lifecycle state of the resource.
        :param pulumi.Input[Mapping[str, Any]] system_tags: System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        :param pulumi.Input[str] time_created: The time the upgrade schedule was created, using an RFC3339 formatted datetime string.
        :param pulumi.Input[str] time_updated: The time the upgrade schedule was updated, using an RFC3339 formatted datetime string.
        """
        _AtCustomerCccUpgradeScheduleState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            compartment_id=compartment_id,
            defined_tags=defined_tags,
            description=description,
            display_name=display_name,
            events=events,
            freeform_tags=freeform_tags,
            infrastructure_ids=infrastructure_ids,
            lifecycle_details=lifecycle_details,
            state=state,
            system_tags=system_tags,
            time_created=time_created,
            time_updated=time_updated,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             compartment_id: Optional[pulumi.Input[str]] = None,
             defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             description: Optional[pulumi.Input[str]] = None,
             display_name: Optional[pulumi.Input[str]] = None,
             events: Optional[pulumi.Input[Sequence[pulumi.Input['AtCustomerCccUpgradeScheduleEventArgs']]]] = None,
             freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             infrastructure_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             lifecycle_details: Optional[pulumi.Input[str]] = None,
             state: Optional[pulumi.Input[str]] = None,
             system_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             time_created: Optional[pulumi.Input[str]] = None,
             time_updated: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if compartment_id is not None:
            _setter("compartment_id", compartment_id)
        if defined_tags is not None:
            _setter("defined_tags", defined_tags)
        if description is not None:
            _setter("description", description)
        if display_name is not None:
            _setter("display_name", display_name)
        if events is not None:
            _setter("events", events)
        if freeform_tags is not None:
            _setter("freeform_tags", freeform_tags)
        if infrastructure_ids is not None:
            _setter("infrastructure_ids", infrastructure_ids)
        if lifecycle_details is not None:
            _setter("lifecycle_details", lifecycle_details)
        if state is not None:
            _setter("state", state)
        if system_tags is not None:
            _setter("system_tags", system_tags)
        if time_created is not None:
            _setter("time_created", time_created)
        if time_updated is not None:
            _setter("time_updated", time_updated)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the Compute Cloud@Customer Upgrade Schedule.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) A description of the Compute Cloud@Customer upgrade schedule time block.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Compute Cloud@Customer upgrade schedule display name. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def events(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AtCustomerCccUpgradeScheduleEventArgs']]]]:
        """
        (Updatable) List of preferred times for Compute Cloud@Customer infrastructure to be upgraded.
        """
        return pulumi.get(self, "events")

    @events.setter
    def events(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AtCustomerCccUpgradeScheduleEventArgs']]]]):
        pulumi.set(self, "events", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}` 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="infrastructureIds")
    def infrastructure_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of Compute Cloud@Customer infrastructure [OCIDs](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that are using this upgrade schedule.
        """
        return pulumi.get(self, "infrastructure_ids")

    @infrastructure_ids.setter
    def infrastructure_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "infrastructure_ids", value)

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> Optional[pulumi.Input[str]]:
        """
        A message describing the current state in more detail. For example, the message can be used to provide actionable information for a resource in a Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @lifecycle_details.setter
    def lifecycle_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_details", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        Lifecycle state of the resource.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @system_tags.setter
    def system_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "system_tags", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The time the upgrade schedule was created, using an RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> Optional[pulumi.Input[str]]:
        """
        The time the upgrade schedule was updated, using an RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_updated")

    @time_updated.setter
    def time_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_updated", value)


class AtCustomerCccUpgradeSchedule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 events: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AtCustomerCccUpgradeScheduleEventArgs']]]]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        """
        This resource provides the Ccc Upgrade Schedule resource in Oracle Cloud Infrastructure Compute Cloud At Customer service.

        Creates a new Compute Cloud@Customer upgrade schedule.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_ccc_upgrade_schedule = oci.compute_cloud.AtCustomerCccUpgradeSchedule("testCccUpgradeSchedule",
            compartment_id=var["compartment_id"],
            display_name=var["ccc_upgrade_schedule_display_name"],
            events=[oci.compute_cloud.AtCustomerCccUpgradeScheduleEventArgs(
                description=var["ccc_upgrade_schedule_events_description"],
                schedule_event_duration=var["ccc_upgrade_schedule_events_schedule_event_duration"],
                time_start=var["ccc_upgrade_schedule_events_time_start"],
                schedule_event_recurrences=var["ccc_upgrade_schedule_events_schedule_event_recurrences"],
            )],
            defined_tags={
                "foo-namespace.bar-key": "value",
            },
            description=var["ccc_upgrade_schedule_description"],
            freeform_tags={
                "bar-key": "value",
            })
        ```

        ## Import

        CccUpgradeSchedules can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:ComputeCloud/atCustomerCccUpgradeSchedule:AtCustomerCccUpgradeSchedule test_ccc_upgrade_schedule "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the Compute Cloud@Customer Upgrade Schedule.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) A description of the Compute Cloud@Customer upgrade schedule time block.
        :param pulumi.Input[str] display_name: (Updatable) Compute Cloud@Customer upgrade schedule display name. Avoid entering confidential information.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AtCustomerCccUpgradeScheduleEventArgs']]]] events: (Updatable) List of preferred times for Compute Cloud@Customer infrastructure to be upgraded.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AtCustomerCccUpgradeScheduleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Ccc Upgrade Schedule resource in Oracle Cloud Infrastructure Compute Cloud At Customer service.

        Creates a new Compute Cloud@Customer upgrade schedule.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_ccc_upgrade_schedule = oci.compute_cloud.AtCustomerCccUpgradeSchedule("testCccUpgradeSchedule",
            compartment_id=var["compartment_id"],
            display_name=var["ccc_upgrade_schedule_display_name"],
            events=[oci.compute_cloud.AtCustomerCccUpgradeScheduleEventArgs(
                description=var["ccc_upgrade_schedule_events_description"],
                schedule_event_duration=var["ccc_upgrade_schedule_events_schedule_event_duration"],
                time_start=var["ccc_upgrade_schedule_events_time_start"],
                schedule_event_recurrences=var["ccc_upgrade_schedule_events_schedule_event_recurrences"],
            )],
            defined_tags={
                "foo-namespace.bar-key": "value",
            },
            description=var["ccc_upgrade_schedule_description"],
            freeform_tags={
                "bar-key": "value",
            })
        ```

        ## Import

        CccUpgradeSchedules can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:ComputeCloud/atCustomerCccUpgradeSchedule:AtCustomerCccUpgradeSchedule test_ccc_upgrade_schedule "id"
        ```

        :param str resource_name: The name of the resource.
        :param AtCustomerCccUpgradeScheduleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AtCustomerCccUpgradeScheduleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            AtCustomerCccUpgradeScheduleArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 events: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AtCustomerCccUpgradeScheduleEventArgs']]]]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AtCustomerCccUpgradeScheduleArgs.__new__(AtCustomerCccUpgradeScheduleArgs)

            if compartment_id is None and not opts.urn:
                raise TypeError("Missing required property 'compartment_id'")
            __props__.__dict__["compartment_id"] = compartment_id
            __props__.__dict__["defined_tags"] = defined_tags
            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            if events is None and not opts.urn:
                raise TypeError("Missing required property 'events'")
            __props__.__dict__["events"] = events
            __props__.__dict__["freeform_tags"] = freeform_tags
            __props__.__dict__["infrastructure_ids"] = None
            __props__.__dict__["lifecycle_details"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["system_tags"] = None
            __props__.__dict__["time_created"] = None
            __props__.__dict__["time_updated"] = None
        super(AtCustomerCccUpgradeSchedule, __self__).__init__(
            'oci:ComputeCloud/atCustomerCccUpgradeSchedule:AtCustomerCccUpgradeSchedule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            events: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AtCustomerCccUpgradeScheduleEventArgs']]]]] = None,
            freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            infrastructure_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            lifecycle_details: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            system_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            time_updated: Optional[pulumi.Input[str]] = None) -> 'AtCustomerCccUpgradeSchedule':
        """
        Get an existing AtCustomerCccUpgradeSchedule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the Compute Cloud@Customer Upgrade Schedule.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) A description of the Compute Cloud@Customer upgrade schedule time block.
        :param pulumi.Input[str] display_name: (Updatable) Compute Cloud@Customer upgrade schedule display name. Avoid entering confidential information.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AtCustomerCccUpgradeScheduleEventArgs']]]] events: (Updatable) List of preferred times for Compute Cloud@Customer infrastructure to be upgraded.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[Sequence[pulumi.Input[str]]] infrastructure_ids: List of Compute Cloud@Customer infrastructure [OCIDs](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that are using this upgrade schedule.
        :param pulumi.Input[str] lifecycle_details: A message describing the current state in more detail. For example, the message can be used to provide actionable information for a resource in a Failed state.
        :param pulumi.Input[str] state: Lifecycle state of the resource.
        :param pulumi.Input[Mapping[str, Any]] system_tags: System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        :param pulumi.Input[str] time_created: The time the upgrade schedule was created, using an RFC3339 formatted datetime string.
        :param pulumi.Input[str] time_updated: The time the upgrade schedule was updated, using an RFC3339 formatted datetime string.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AtCustomerCccUpgradeScheduleState.__new__(_AtCustomerCccUpgradeScheduleState)

        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["defined_tags"] = defined_tags
        __props__.__dict__["description"] = description
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["events"] = events
        __props__.__dict__["freeform_tags"] = freeform_tags
        __props__.__dict__["infrastructure_ids"] = infrastructure_ids
        __props__.__dict__["lifecycle_details"] = lifecycle_details
        __props__.__dict__["state"] = state
        __props__.__dict__["system_tags"] = system_tags
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["time_updated"] = time_updated
        return AtCustomerCccUpgradeSchedule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        (Updatable) Compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the Compute Cloud@Customer Upgrade Schedule.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        (Updatable) A description of the Compute Cloud@Customer upgrade schedule time block.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        (Updatable) Compute Cloud@Customer upgrade schedule display name. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def events(self) -> pulumi.Output[Sequence['outputs.AtCustomerCccUpgradeScheduleEvent']]:
        """
        (Updatable) List of preferred times for Compute Cloud@Customer infrastructure to be upgraded.
        """
        return pulumi.get(self, "events")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}` 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="infrastructureIds")
    def infrastructure_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        List of Compute Cloud@Customer infrastructure [OCIDs](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that are using this upgrade schedule.
        """
        return pulumi.get(self, "infrastructure_ids")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> pulumi.Output[str]:
        """
        A message describing the current state in more detail. For example, the message can be used to provide actionable information for a resource in a Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        Lifecycle state of the resource.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The time the upgrade schedule was created, using an RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> pulumi.Output[str]:
        """
        The time the upgrade schedule was updated, using an RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_updated")

