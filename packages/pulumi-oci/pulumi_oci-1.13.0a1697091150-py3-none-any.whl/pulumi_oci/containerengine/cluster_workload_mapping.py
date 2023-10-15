# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ClusterWorkloadMappingArgs', 'ClusterWorkloadMapping']

@pulumi.input_type
class ClusterWorkloadMappingArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 mapped_compartment_id: pulumi.Input[str],
                 namespace: pulumi.Input[str],
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a ClusterWorkloadMapping resource.
        :param pulumi.Input[str] cluster_id: The OCID of the cluster.
        :param pulumi.Input[str] mapped_compartment_id: (Updatable) The OCID of the mapped customer compartment.
        :param pulumi.Input[str] namespace: The namespace of the workloadMapping.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        """
        ClusterWorkloadMappingArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cluster_id=cluster_id,
            mapped_compartment_id=mapped_compartment_id,
            namespace=namespace,
            defined_tags=defined_tags,
            freeform_tags=freeform_tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cluster_id: pulumi.Input[str],
             mapped_compartment_id: pulumi.Input[str],
             namespace: pulumi.Input[str],
             defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("cluster_id", cluster_id)
        _setter("mapped_compartment_id", mapped_compartment_id)
        _setter("namespace", namespace)
        if defined_tags is not None:
            _setter("defined_tags", defined_tags)
        if freeform_tags is not None:
            _setter("freeform_tags", freeform_tags)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        The OCID of the cluster.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="mappedCompartmentId")
    def mapped_compartment_id(self) -> pulumi.Input[str]:
        """
        (Updatable) The OCID of the mapped customer compartment.
        """
        return pulumi.get(self, "mapped_compartment_id")

    @mapped_compartment_id.setter
    def mapped_compartment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "mapped_compartment_id", value)

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[str]:
        """
        The namespace of the workloadMapping.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)


@pulumi.input_type
class _ClusterWorkloadMappingState:
    def __init__(__self__, *,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 mapped_compartment_id: Optional[pulumi.Input[str]] = None,
                 mapped_tenancy_id: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 time_created: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ClusterWorkloadMapping resources.
        :param pulumi.Input[str] cluster_id: The OCID of the cluster.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        :param pulumi.Input[str] mapped_compartment_id: (Updatable) The OCID of the mapped customer compartment.
        :param pulumi.Input[str] mapped_tenancy_id: The OCID of the mapped customer tenancy.
        :param pulumi.Input[str] namespace: The namespace of the workloadMapping.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] state: The state of the workloadMapping.
        :param pulumi.Input[str] time_created: The time the cluster was created.
        """
        _ClusterWorkloadMappingState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cluster_id=cluster_id,
            defined_tags=defined_tags,
            freeform_tags=freeform_tags,
            mapped_compartment_id=mapped_compartment_id,
            mapped_tenancy_id=mapped_tenancy_id,
            namespace=namespace,
            state=state,
            time_created=time_created,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cluster_id: Optional[pulumi.Input[str]] = None,
             defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             mapped_compartment_id: Optional[pulumi.Input[str]] = None,
             mapped_tenancy_id: Optional[pulumi.Input[str]] = None,
             namespace: Optional[pulumi.Input[str]] = None,
             state: Optional[pulumi.Input[str]] = None,
             time_created: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if cluster_id is not None:
            _setter("cluster_id", cluster_id)
        if defined_tags is not None:
            _setter("defined_tags", defined_tags)
        if freeform_tags is not None:
            _setter("freeform_tags", freeform_tags)
        if mapped_compartment_id is not None:
            _setter("mapped_compartment_id", mapped_compartment_id)
        if mapped_tenancy_id is not None:
            _setter("mapped_tenancy_id", mapped_tenancy_id)
        if namespace is not None:
            _setter("namespace", namespace)
        if state is not None:
            _setter("state", state)
        if time_created is not None:
            _setter("time_created", time_created)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The OCID of the cluster.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="mappedCompartmentId")
    def mapped_compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The OCID of the mapped customer compartment.
        """
        return pulumi.get(self, "mapped_compartment_id")

    @mapped_compartment_id.setter
    def mapped_compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mapped_compartment_id", value)

    @property
    @pulumi.getter(name="mappedTenancyId")
    def mapped_tenancy_id(self) -> Optional[pulumi.Input[str]]:
        """
        The OCID of the mapped customer tenancy.
        """
        return pulumi.get(self, "mapped_tenancy_id")

    @mapped_tenancy_id.setter
    def mapped_tenancy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mapped_tenancy_id", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace of the workloadMapping.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The state of the workloadMapping.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The time the cluster was created.
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)


class ClusterWorkloadMapping(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 mapped_compartment_id: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Cluster Workload Mapping resource in Oracle Cloud Infrastructure Container Engine service.

        Create the specified workloadMapping for a cluster.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_cluster_workload_mapping = oci.container_engine.ClusterWorkloadMapping("testClusterWorkloadMapping",
            cluster_id=oci_containerengine_cluster["test_cluster"]["id"],
            mapped_compartment_id=oci_identity_compartment["test_compartment"]["id"],
            namespace=var["cluster_workload_mapping_namespace"],
            defined_tags={
                "Operations.CostCenter": "42",
            },
            freeform_tags={
                "Department": "Finance",
            })
        ```

        ## Import

        ClusterWorkloadMappings can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:ContainerEngine/clusterWorkloadMapping:ClusterWorkloadMapping test_cluster_workload_mapping "clusters/{clusterId}/workloadMappings/{workloadMappingId}"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The OCID of the cluster.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        :param pulumi.Input[str] mapped_compartment_id: (Updatable) The OCID of the mapped customer compartment.
        :param pulumi.Input[str] namespace: The namespace of the workloadMapping.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterWorkloadMappingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Cluster Workload Mapping resource in Oracle Cloud Infrastructure Container Engine service.

        Create the specified workloadMapping for a cluster.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_cluster_workload_mapping = oci.container_engine.ClusterWorkloadMapping("testClusterWorkloadMapping",
            cluster_id=oci_containerengine_cluster["test_cluster"]["id"],
            mapped_compartment_id=oci_identity_compartment["test_compartment"]["id"],
            namespace=var["cluster_workload_mapping_namespace"],
            defined_tags={
                "Operations.CostCenter": "42",
            },
            freeform_tags={
                "Department": "Finance",
            })
        ```

        ## Import

        ClusterWorkloadMappings can be imported using the `id`, e.g.

        ```sh
         $ pulumi import oci:ContainerEngine/clusterWorkloadMapping:ClusterWorkloadMapping test_cluster_workload_mapping "clusters/{clusterId}/workloadMappings/{workloadMappingId}"
        ```

        :param str resource_name: The name of the resource.
        :param ClusterWorkloadMappingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterWorkloadMappingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ClusterWorkloadMappingArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 mapped_compartment_id: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterWorkloadMappingArgs.__new__(ClusterWorkloadMappingArgs)

            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            __props__.__dict__["defined_tags"] = defined_tags
            __props__.__dict__["freeform_tags"] = freeform_tags
            if mapped_compartment_id is None and not opts.urn:
                raise TypeError("Missing required property 'mapped_compartment_id'")
            __props__.__dict__["mapped_compartment_id"] = mapped_compartment_id
            if namespace is None and not opts.urn:
                raise TypeError("Missing required property 'namespace'")
            __props__.__dict__["namespace"] = namespace
            __props__.__dict__["mapped_tenancy_id"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["time_created"] = None
        super(ClusterWorkloadMapping, __self__).__init__(
            'oci:ContainerEngine/clusterWorkloadMapping:ClusterWorkloadMapping',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            mapped_compartment_id: Optional[pulumi.Input[str]] = None,
            mapped_tenancy_id: Optional[pulumi.Input[str]] = None,
            namespace: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            time_created: Optional[pulumi.Input[str]] = None) -> 'ClusterWorkloadMapping':
        """
        Get an existing ClusterWorkloadMapping resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The OCID of the cluster.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        :param pulumi.Input[str] mapped_compartment_id: (Updatable) The OCID of the mapped customer compartment.
        :param pulumi.Input[str] mapped_tenancy_id: The OCID of the mapped customer tenancy.
        :param pulumi.Input[str] namespace: The namespace of the workloadMapping.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] state: The state of the workloadMapping.
        :param pulumi.Input[str] time_created: The time the cluster was created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ClusterWorkloadMappingState.__new__(_ClusterWorkloadMappingState)

        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["defined_tags"] = defined_tags
        __props__.__dict__["freeform_tags"] = freeform_tags
        __props__.__dict__["mapped_compartment_id"] = mapped_compartment_id
        __props__.__dict__["mapped_tenancy_id"] = mapped_tenancy_id
        __props__.__dict__["namespace"] = namespace
        __props__.__dict__["state"] = state
        __props__.__dict__["time_created"] = time_created
        return ClusterWorkloadMapping(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        The OCID of the cluster.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="mappedCompartmentId")
    def mapped_compartment_id(self) -> pulumi.Output[str]:
        """
        (Updatable) The OCID of the mapped customer compartment.
        """
        return pulumi.get(self, "mapped_compartment_id")

    @property
    @pulumi.getter(name="mappedTenancyId")
    def mapped_tenancy_id(self) -> pulumi.Output[str]:
        """
        The OCID of the mapped customer tenancy.
        """
        return pulumi.get(self, "mapped_tenancy_id")

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[str]:
        """
        The namespace of the workloadMapping.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the workloadMapping.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The time the cluster was created.
        """
        return pulumi.get(self, "time_created")

