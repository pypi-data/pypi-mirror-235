# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DatastoreClusterVmAntiAffinityRuleArgs', 'DatastoreClusterVmAntiAffinityRule']

@pulumi.input_type
class DatastoreClusterVmAntiAffinityRuleArgs:
    def __init__(__self__, *,
                 datastore_cluster_id: pulumi.Input[str],
                 virtual_machine_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 enabled: Optional[pulumi.Input[bool]] = None,
                 mandatory: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DatastoreClusterVmAntiAffinityRule resource.
        :param pulumi.Input[str] datastore_cluster_id: The managed object reference
               ID of the datastore cluster to put the group in.  Forces
               a new resource if changed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] virtual_machine_ids: The UUIDs of the virtual machines to run
               on different datastores from each other.
               
               > **NOTE:** The minimum length of `virtual_machine_ids` is 2.
        :param pulumi.Input[bool] enabled: Enable this rule in the cluster. Default: `true`.
        :param pulumi.Input[bool] mandatory: When this value is `true`, prevents any virtual
               machine operations that may violate this rule. Default: `false`.
        :param pulumi.Input[str] name: The name of the rule. This must be unique in the cluster.
        """
        DatastoreClusterVmAntiAffinityRuleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            datastore_cluster_id=datastore_cluster_id,
            virtual_machine_ids=virtual_machine_ids,
            enabled=enabled,
            mandatory=mandatory,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             datastore_cluster_id: pulumi.Input[str],
             virtual_machine_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
             enabled: Optional[pulumi.Input[bool]] = None,
             mandatory: Optional[pulumi.Input[bool]] = None,
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("datastore_cluster_id", datastore_cluster_id)
        _setter("virtual_machine_ids", virtual_machine_ids)
        if enabled is not None:
            _setter("enabled", enabled)
        if mandatory is not None:
            _setter("mandatory", mandatory)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="datastoreClusterId")
    def datastore_cluster_id(self) -> pulumi.Input[str]:
        """
        The managed object reference
        ID of the datastore cluster to put the group in.  Forces
        a new resource if changed.
        """
        return pulumi.get(self, "datastore_cluster_id")

    @datastore_cluster_id.setter
    def datastore_cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "datastore_cluster_id", value)

    @property
    @pulumi.getter(name="virtualMachineIds")
    def virtual_machine_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The UUIDs of the virtual machines to run
        on different datastores from each other.

        > **NOTE:** The minimum length of `virtual_machine_ids` is 2.
        """
        return pulumi.get(self, "virtual_machine_ids")

    @virtual_machine_ids.setter
    def virtual_machine_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "virtual_machine_ids", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable this rule in the cluster. Default: `true`.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def mandatory(self) -> Optional[pulumi.Input[bool]]:
        """
        When this value is `true`, prevents any virtual
        machine operations that may violate this rule. Default: `false`.
        """
        return pulumi.get(self, "mandatory")

    @mandatory.setter
    def mandatory(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "mandatory", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the rule. This must be unique in the cluster.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _DatastoreClusterVmAntiAffinityRuleState:
    def __init__(__self__, *,
                 datastore_cluster_id: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 mandatory: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 virtual_machine_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering DatastoreClusterVmAntiAffinityRule resources.
        :param pulumi.Input[str] datastore_cluster_id: The managed object reference
               ID of the datastore cluster to put the group in.  Forces
               a new resource if changed.
        :param pulumi.Input[bool] enabled: Enable this rule in the cluster. Default: `true`.
        :param pulumi.Input[bool] mandatory: When this value is `true`, prevents any virtual
               machine operations that may violate this rule. Default: `false`.
        :param pulumi.Input[str] name: The name of the rule. This must be unique in the cluster.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] virtual_machine_ids: The UUIDs of the virtual machines to run
               on different datastores from each other.
               
               > **NOTE:** The minimum length of `virtual_machine_ids` is 2.
        """
        _DatastoreClusterVmAntiAffinityRuleState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            datastore_cluster_id=datastore_cluster_id,
            enabled=enabled,
            mandatory=mandatory,
            name=name,
            virtual_machine_ids=virtual_machine_ids,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             datastore_cluster_id: Optional[pulumi.Input[str]] = None,
             enabled: Optional[pulumi.Input[bool]] = None,
             mandatory: Optional[pulumi.Input[bool]] = None,
             name: Optional[pulumi.Input[str]] = None,
             virtual_machine_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if datastore_cluster_id is not None:
            _setter("datastore_cluster_id", datastore_cluster_id)
        if enabled is not None:
            _setter("enabled", enabled)
        if mandatory is not None:
            _setter("mandatory", mandatory)
        if name is not None:
            _setter("name", name)
        if virtual_machine_ids is not None:
            _setter("virtual_machine_ids", virtual_machine_ids)

    @property
    @pulumi.getter(name="datastoreClusterId")
    def datastore_cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The managed object reference
        ID of the datastore cluster to put the group in.  Forces
        a new resource if changed.
        """
        return pulumi.get(self, "datastore_cluster_id")

    @datastore_cluster_id.setter
    def datastore_cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datastore_cluster_id", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable this rule in the cluster. Default: `true`.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def mandatory(self) -> Optional[pulumi.Input[bool]]:
        """
        When this value is `true`, prevents any virtual
        machine operations that may violate this rule. Default: `false`.
        """
        return pulumi.get(self, "mandatory")

    @mandatory.setter
    def mandatory(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "mandatory", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the rule. This must be unique in the cluster.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="virtualMachineIds")
    def virtual_machine_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The UUIDs of the virtual machines to run
        on different datastores from each other.

        > **NOTE:** The minimum length of `virtual_machine_ids` is 2.
        """
        return pulumi.get(self, "virtual_machine_ids")

    @virtual_machine_ids.setter
    def virtual_machine_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "virtual_machine_ids", value)


class DatastoreClusterVmAntiAffinityRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datastore_cluster_id: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 mandatory: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 virtual_machine_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a DatastoreClusterVmAntiAffinityRule resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datastore_cluster_id: The managed object reference
               ID of the datastore cluster to put the group in.  Forces
               a new resource if changed.
        :param pulumi.Input[bool] enabled: Enable this rule in the cluster. Default: `true`.
        :param pulumi.Input[bool] mandatory: When this value is `true`, prevents any virtual
               machine operations that may violate this rule. Default: `false`.
        :param pulumi.Input[str] name: The name of the rule. This must be unique in the cluster.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] virtual_machine_ids: The UUIDs of the virtual machines to run
               on different datastores from each other.
               
               > **NOTE:** The minimum length of `virtual_machine_ids` is 2.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatastoreClusterVmAntiAffinityRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a DatastoreClusterVmAntiAffinityRule resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param DatastoreClusterVmAntiAffinityRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatastoreClusterVmAntiAffinityRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DatastoreClusterVmAntiAffinityRuleArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datastore_cluster_id: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 mandatory: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 virtual_machine_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DatastoreClusterVmAntiAffinityRuleArgs.__new__(DatastoreClusterVmAntiAffinityRuleArgs)

            if datastore_cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'datastore_cluster_id'")
            __props__.__dict__["datastore_cluster_id"] = datastore_cluster_id
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["mandatory"] = mandatory
            __props__.__dict__["name"] = name
            if virtual_machine_ids is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_machine_ids'")
            __props__.__dict__["virtual_machine_ids"] = virtual_machine_ids
        super(DatastoreClusterVmAntiAffinityRule, __self__).__init__(
            'vsphere:index/datastoreClusterVmAntiAffinityRule:DatastoreClusterVmAntiAffinityRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            datastore_cluster_id: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            mandatory: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            virtual_machine_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'DatastoreClusterVmAntiAffinityRule':
        """
        Get an existing DatastoreClusterVmAntiAffinityRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datastore_cluster_id: The managed object reference
               ID of the datastore cluster to put the group in.  Forces
               a new resource if changed.
        :param pulumi.Input[bool] enabled: Enable this rule in the cluster. Default: `true`.
        :param pulumi.Input[bool] mandatory: When this value is `true`, prevents any virtual
               machine operations that may violate this rule. Default: `false`.
        :param pulumi.Input[str] name: The name of the rule. This must be unique in the cluster.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] virtual_machine_ids: The UUIDs of the virtual machines to run
               on different datastores from each other.
               
               > **NOTE:** The minimum length of `virtual_machine_ids` is 2.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DatastoreClusterVmAntiAffinityRuleState.__new__(_DatastoreClusterVmAntiAffinityRuleState)

        __props__.__dict__["datastore_cluster_id"] = datastore_cluster_id
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["mandatory"] = mandatory
        __props__.__dict__["name"] = name
        __props__.__dict__["virtual_machine_ids"] = virtual_machine_ids
        return DatastoreClusterVmAntiAffinityRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="datastoreClusterId")
    def datastore_cluster_id(self) -> pulumi.Output[str]:
        """
        The managed object reference
        ID of the datastore cluster to put the group in.  Forces
        a new resource if changed.
        """
        return pulumi.get(self, "datastore_cluster_id")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable this rule in the cluster. Default: `true`.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def mandatory(self) -> pulumi.Output[Optional[bool]]:
        """
        When this value is `true`, prevents any virtual
        machine operations that may violate this rule. Default: `false`.
        """
        return pulumi.get(self, "mandatory")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the rule. This must be unique in the cluster.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="virtualMachineIds")
    def virtual_machine_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The UUIDs of the virtual machines to run
        on different datastores from each other.

        > **NOTE:** The minimum length of `virtual_machine_ids` is 2.
        """
        return pulumi.get(self, "virtual_machine_ids")

