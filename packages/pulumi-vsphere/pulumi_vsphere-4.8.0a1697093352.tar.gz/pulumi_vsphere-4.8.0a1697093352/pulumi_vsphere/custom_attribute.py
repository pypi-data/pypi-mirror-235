# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['CustomAttributeArgs', 'CustomAttribute']

@pulumi.input_type
class CustomAttributeArgs:
    def __init__(__self__, *,
                 managed_object_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CustomAttribute resource.
        :param pulumi.Input[str] managed_object_type: The object type that this attribute may be
               applied to. If not set, the custom attribute may be applied to any object
               type. For a full list, review the Managed Object Types. Forces a new resource if changed.
        :param pulumi.Input[str] name: The name of the custom attribute.
        """
        CustomAttributeArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            managed_object_type=managed_object_type,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             managed_object_type: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if managed_object_type is not None:
            _setter("managed_object_type", managed_object_type)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="managedObjectType")
    def managed_object_type(self) -> Optional[pulumi.Input[str]]:
        """
        The object type that this attribute may be
        applied to. If not set, the custom attribute may be applied to any object
        type. For a full list, review the Managed Object Types. Forces a new resource if changed.
        """
        return pulumi.get(self, "managed_object_type")

    @managed_object_type.setter
    def managed_object_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "managed_object_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the custom attribute.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _CustomAttributeState:
    def __init__(__self__, *,
                 managed_object_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CustomAttribute resources.
        :param pulumi.Input[str] managed_object_type: The object type that this attribute may be
               applied to. If not set, the custom attribute may be applied to any object
               type. For a full list, review the Managed Object Types. Forces a new resource if changed.
        :param pulumi.Input[str] name: The name of the custom attribute.
        """
        _CustomAttributeState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            managed_object_type=managed_object_type,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             managed_object_type: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if managed_object_type is not None:
            _setter("managed_object_type", managed_object_type)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="managedObjectType")
    def managed_object_type(self) -> Optional[pulumi.Input[str]]:
        """
        The object type that this attribute may be
        applied to. If not set, the custom attribute may be applied to any object
        type. For a full list, review the Managed Object Types. Forces a new resource if changed.
        """
        return pulumi.get(self, "managed_object_type")

    @managed_object_type.setter
    def managed_object_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "managed_object_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the custom attribute.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class CustomAttribute(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 managed_object_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a CustomAttribute resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] managed_object_type: The object type that this attribute may be
               applied to. If not set, the custom attribute may be applied to any object
               type. For a full list, review the Managed Object Types. Forces a new resource if changed.
        :param pulumi.Input[str] name: The name of the custom attribute.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[CustomAttributeArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a CustomAttribute resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param CustomAttributeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomAttributeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            CustomAttributeArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 managed_object_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CustomAttributeArgs.__new__(CustomAttributeArgs)

            __props__.__dict__["managed_object_type"] = managed_object_type
            __props__.__dict__["name"] = name
        super(CustomAttribute, __self__).__init__(
            'vsphere:index/customAttribute:CustomAttribute',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            managed_object_type: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'CustomAttribute':
        """
        Get an existing CustomAttribute resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] managed_object_type: The object type that this attribute may be
               applied to. If not set, the custom attribute may be applied to any object
               type. For a full list, review the Managed Object Types. Forces a new resource if changed.
        :param pulumi.Input[str] name: The name of the custom attribute.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CustomAttributeState.__new__(_CustomAttributeState)

        __props__.__dict__["managed_object_type"] = managed_object_type
        __props__.__dict__["name"] = name
        return CustomAttribute(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="managedObjectType")
    def managed_object_type(self) -> pulumi.Output[Optional[str]]:
        """
        The object type that this attribute may be
        applied to. If not set, the custom attribute may be applied to any object
        type. For a full list, review the Managed Object Types. Forces a new resource if changed.
        """
        return pulumi.get(self, "managed_object_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the custom attribute.
        """
        return pulumi.get(self, "name")

