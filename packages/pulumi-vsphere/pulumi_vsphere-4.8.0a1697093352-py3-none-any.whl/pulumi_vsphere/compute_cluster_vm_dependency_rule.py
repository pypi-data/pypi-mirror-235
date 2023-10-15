# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ComputeClusterVmDependencyRuleArgs', 'ComputeClusterVmDependencyRule']

@pulumi.input_type
class ComputeClusterVmDependencyRuleArgs:
    def __init__(__self__, *,
                 compute_cluster_id: pulumi.Input[str],
                 dependency_vm_group_name: pulumi.Input[str],
                 vm_group_name: pulumi.Input[str],
                 enabled: Optional[pulumi.Input[bool]] = None,
                 mandatory: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ComputeClusterVmDependencyRule resource.
        :param pulumi.Input[str] compute_cluster_id: The managed object reference
               ID of the cluster to put the group in.  Forces a new
               resource if changed.
        :param pulumi.Input[str] dependency_vm_group_name: The name of the VM group that this
               rule depends on. The VMs defined in the group specified by
               `vm_group_name` will not be started until the VMs in this
               group are started.
        :param pulumi.Input[str] vm_group_name: The name of the VM group that is the subject of
               this rule. The VMs defined in this group will not be started until the VMs in
               the group specified by
               `dependency_vm_group_name` are started.
        :param pulumi.Input[bool] enabled: Enable this rule in the cluster. Default: `true`.
        :param pulumi.Input[bool] mandatory: When this value is `true`, prevents any virtual
               machine operations that may violate this rule. Default: `false`.
               
               > **NOTE:** The namespace for rule names on this resource (defined by the
               `name` argument) is shared with all rules in the cluster - consider
               this when naming your rules.
        :param pulumi.Input[str] name: The name of the rule. This must be unique in the
               cluster.
        """
        ComputeClusterVmDependencyRuleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            compute_cluster_id=compute_cluster_id,
            dependency_vm_group_name=dependency_vm_group_name,
            vm_group_name=vm_group_name,
            enabled=enabled,
            mandatory=mandatory,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             compute_cluster_id: pulumi.Input[str],
             dependency_vm_group_name: pulumi.Input[str],
             vm_group_name: pulumi.Input[str],
             enabled: Optional[pulumi.Input[bool]] = None,
             mandatory: Optional[pulumi.Input[bool]] = None,
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("compute_cluster_id", compute_cluster_id)
        _setter("dependency_vm_group_name", dependency_vm_group_name)
        _setter("vm_group_name", vm_group_name)
        if enabled is not None:
            _setter("enabled", enabled)
        if mandatory is not None:
            _setter("mandatory", mandatory)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="computeClusterId")
    def compute_cluster_id(self) -> pulumi.Input[str]:
        """
        The managed object reference
        ID of the cluster to put the group in.  Forces a new
        resource if changed.
        """
        return pulumi.get(self, "compute_cluster_id")

    @compute_cluster_id.setter
    def compute_cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "compute_cluster_id", value)

    @property
    @pulumi.getter(name="dependencyVmGroupName")
    def dependency_vm_group_name(self) -> pulumi.Input[str]:
        """
        The name of the VM group that this
        rule depends on. The VMs defined in the group specified by
        `vm_group_name` will not be started until the VMs in this
        group are started.
        """
        return pulumi.get(self, "dependency_vm_group_name")

    @dependency_vm_group_name.setter
    def dependency_vm_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "dependency_vm_group_name", value)

    @property
    @pulumi.getter(name="vmGroupName")
    def vm_group_name(self) -> pulumi.Input[str]:
        """
        The name of the VM group that is the subject of
        this rule. The VMs defined in this group will not be started until the VMs in
        the group specified by
        `dependency_vm_group_name` are started.
        """
        return pulumi.get(self, "vm_group_name")

    @vm_group_name.setter
    def vm_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "vm_group_name", value)

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

        > **NOTE:** The namespace for rule names on this resource (defined by the
        `name` argument) is shared with all rules in the cluster - consider
        this when naming your rules.
        """
        return pulumi.get(self, "mandatory")

    @mandatory.setter
    def mandatory(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "mandatory", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the rule. This must be unique in the
        cluster.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ComputeClusterVmDependencyRuleState:
    def __init__(__self__, *,
                 compute_cluster_id: Optional[pulumi.Input[str]] = None,
                 dependency_vm_group_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 mandatory: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 vm_group_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ComputeClusterVmDependencyRule resources.
        :param pulumi.Input[str] compute_cluster_id: The managed object reference
               ID of the cluster to put the group in.  Forces a new
               resource if changed.
        :param pulumi.Input[str] dependency_vm_group_name: The name of the VM group that this
               rule depends on. The VMs defined in the group specified by
               `vm_group_name` will not be started until the VMs in this
               group are started.
        :param pulumi.Input[bool] enabled: Enable this rule in the cluster. Default: `true`.
        :param pulumi.Input[bool] mandatory: When this value is `true`, prevents any virtual
               machine operations that may violate this rule. Default: `false`.
               
               > **NOTE:** The namespace for rule names on this resource (defined by the
               `name` argument) is shared with all rules in the cluster - consider
               this when naming your rules.
        :param pulumi.Input[str] name: The name of the rule. This must be unique in the
               cluster.
        :param pulumi.Input[str] vm_group_name: The name of the VM group that is the subject of
               this rule. The VMs defined in this group will not be started until the VMs in
               the group specified by
               `dependency_vm_group_name` are started.
        """
        _ComputeClusterVmDependencyRuleState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            compute_cluster_id=compute_cluster_id,
            dependency_vm_group_name=dependency_vm_group_name,
            enabled=enabled,
            mandatory=mandatory,
            name=name,
            vm_group_name=vm_group_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             compute_cluster_id: Optional[pulumi.Input[str]] = None,
             dependency_vm_group_name: Optional[pulumi.Input[str]] = None,
             enabled: Optional[pulumi.Input[bool]] = None,
             mandatory: Optional[pulumi.Input[bool]] = None,
             name: Optional[pulumi.Input[str]] = None,
             vm_group_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if compute_cluster_id is not None:
            _setter("compute_cluster_id", compute_cluster_id)
        if dependency_vm_group_name is not None:
            _setter("dependency_vm_group_name", dependency_vm_group_name)
        if enabled is not None:
            _setter("enabled", enabled)
        if mandatory is not None:
            _setter("mandatory", mandatory)
        if name is not None:
            _setter("name", name)
        if vm_group_name is not None:
            _setter("vm_group_name", vm_group_name)

    @property
    @pulumi.getter(name="computeClusterId")
    def compute_cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The managed object reference
        ID of the cluster to put the group in.  Forces a new
        resource if changed.
        """
        return pulumi.get(self, "compute_cluster_id")

    @compute_cluster_id.setter
    def compute_cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compute_cluster_id", value)

    @property
    @pulumi.getter(name="dependencyVmGroupName")
    def dependency_vm_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the VM group that this
        rule depends on. The VMs defined in the group specified by
        `vm_group_name` will not be started until the VMs in this
        group are started.
        """
        return pulumi.get(self, "dependency_vm_group_name")

    @dependency_vm_group_name.setter
    def dependency_vm_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dependency_vm_group_name", value)

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

        > **NOTE:** The namespace for rule names on this resource (defined by the
        `name` argument) is shared with all rules in the cluster - consider
        this when naming your rules.
        """
        return pulumi.get(self, "mandatory")

    @mandatory.setter
    def mandatory(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "mandatory", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the rule. This must be unique in the
        cluster.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="vmGroupName")
    def vm_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the VM group that is the subject of
        this rule. The VMs defined in this group will not be started until the VMs in
        the group specified by
        `dependency_vm_group_name` are started.
        """
        return pulumi.get(self, "vm_group_name")

    @vm_group_name.setter
    def vm_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vm_group_name", value)


class ComputeClusterVmDependencyRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compute_cluster_id: Optional[pulumi.Input[str]] = None,
                 dependency_vm_group_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 mandatory: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 vm_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a ComputeClusterVmDependencyRule resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compute_cluster_id: The managed object reference
               ID of the cluster to put the group in.  Forces a new
               resource if changed.
        :param pulumi.Input[str] dependency_vm_group_name: The name of the VM group that this
               rule depends on. The VMs defined in the group specified by
               `vm_group_name` will not be started until the VMs in this
               group are started.
        :param pulumi.Input[bool] enabled: Enable this rule in the cluster. Default: `true`.
        :param pulumi.Input[bool] mandatory: When this value is `true`, prevents any virtual
               machine operations that may violate this rule. Default: `false`.
               
               > **NOTE:** The namespace for rule names on this resource (defined by the
               `name` argument) is shared with all rules in the cluster - consider
               this when naming your rules.
        :param pulumi.Input[str] name: The name of the rule. This must be unique in the
               cluster.
        :param pulumi.Input[str] vm_group_name: The name of the VM group that is the subject of
               this rule. The VMs defined in this group will not be started until the VMs in
               the group specified by
               `dependency_vm_group_name` are started.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ComputeClusterVmDependencyRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ComputeClusterVmDependencyRule resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ComputeClusterVmDependencyRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ComputeClusterVmDependencyRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ComputeClusterVmDependencyRuleArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compute_cluster_id: Optional[pulumi.Input[str]] = None,
                 dependency_vm_group_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 mandatory: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 vm_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ComputeClusterVmDependencyRuleArgs.__new__(ComputeClusterVmDependencyRuleArgs)

            if compute_cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'compute_cluster_id'")
            __props__.__dict__["compute_cluster_id"] = compute_cluster_id
            if dependency_vm_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'dependency_vm_group_name'")
            __props__.__dict__["dependency_vm_group_name"] = dependency_vm_group_name
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["mandatory"] = mandatory
            __props__.__dict__["name"] = name
            if vm_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'vm_group_name'")
            __props__.__dict__["vm_group_name"] = vm_group_name
        super(ComputeClusterVmDependencyRule, __self__).__init__(
            'vsphere:index/computeClusterVmDependencyRule:ComputeClusterVmDependencyRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            compute_cluster_id: Optional[pulumi.Input[str]] = None,
            dependency_vm_group_name: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            mandatory: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            vm_group_name: Optional[pulumi.Input[str]] = None) -> 'ComputeClusterVmDependencyRule':
        """
        Get an existing ComputeClusterVmDependencyRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compute_cluster_id: The managed object reference
               ID of the cluster to put the group in.  Forces a new
               resource if changed.
        :param pulumi.Input[str] dependency_vm_group_name: The name of the VM group that this
               rule depends on. The VMs defined in the group specified by
               `vm_group_name` will not be started until the VMs in this
               group are started.
        :param pulumi.Input[bool] enabled: Enable this rule in the cluster. Default: `true`.
        :param pulumi.Input[bool] mandatory: When this value is `true`, prevents any virtual
               machine operations that may violate this rule. Default: `false`.
               
               > **NOTE:** The namespace for rule names on this resource (defined by the
               `name` argument) is shared with all rules in the cluster - consider
               this when naming your rules.
        :param pulumi.Input[str] name: The name of the rule. This must be unique in the
               cluster.
        :param pulumi.Input[str] vm_group_name: The name of the VM group that is the subject of
               this rule. The VMs defined in this group will not be started until the VMs in
               the group specified by
               `dependency_vm_group_name` are started.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ComputeClusterVmDependencyRuleState.__new__(_ComputeClusterVmDependencyRuleState)

        __props__.__dict__["compute_cluster_id"] = compute_cluster_id
        __props__.__dict__["dependency_vm_group_name"] = dependency_vm_group_name
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["mandatory"] = mandatory
        __props__.__dict__["name"] = name
        __props__.__dict__["vm_group_name"] = vm_group_name
        return ComputeClusterVmDependencyRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="computeClusterId")
    def compute_cluster_id(self) -> pulumi.Output[str]:
        """
        The managed object reference
        ID of the cluster to put the group in.  Forces a new
        resource if changed.
        """
        return pulumi.get(self, "compute_cluster_id")

    @property
    @pulumi.getter(name="dependencyVmGroupName")
    def dependency_vm_group_name(self) -> pulumi.Output[str]:
        """
        The name of the VM group that this
        rule depends on. The VMs defined in the group specified by
        `vm_group_name` will not be started until the VMs in this
        group are started.
        """
        return pulumi.get(self, "dependency_vm_group_name")

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

        > **NOTE:** The namespace for rule names on this resource (defined by the
        `name` argument) is shared with all rules in the cluster - consider
        this when naming your rules.
        """
        return pulumi.get(self, "mandatory")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the rule. This must be unique in the
        cluster.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="vmGroupName")
    def vm_group_name(self) -> pulumi.Output[str]:
        """
        The name of the VM group that is the subject of
        this rule. The VMs defined in this group will not be started until the VMs in
        the group specified by
        `dependency_vm_group_name` are started.
        """
        return pulumi.get(self, "vm_group_name")

