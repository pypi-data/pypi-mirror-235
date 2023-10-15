# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['SubnetGroupArgs', 'SubnetGroup']

@pulumi.input_type
class SubnetGroupArgs:
    def __init__(__self__, *,
                 subnet_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 description: Optional[pulumi.Input[str]] = None,
                 subnet_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['SubnetGroupTagArgs']]]] = None):
        """
        The set of arguments for constructing a SubnetGroup resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: A list of VPC subnet IDs for the subnet group.
        :param pulumi.Input[str] description: An optional description of the subnet group.
        :param pulumi.Input[str] subnet_group_name: The name of the subnet group. This value must be unique as it also serves as the subnet group identifier.
        :param pulumi.Input[Sequence[pulumi.Input['SubnetGroupTagArgs']]] tags: An array of key-value pairs to apply to this subnet group.
        """
        SubnetGroupArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            subnet_ids=subnet_ids,
            description=description,
            subnet_group_name=subnet_group_name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             subnet_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
             description: Optional[pulumi.Input[str]] = None,
             subnet_group_name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['SubnetGroupTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("subnet_ids", subnet_ids)
        if description is not None:
            _setter("description", description)
        if subnet_group_name is not None:
            _setter("subnet_group_name", subnet_group_name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of VPC subnet IDs for the subnet group.
        """
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        An optional description of the subnet group.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="subnetGroupName")
    def subnet_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the subnet group. This value must be unique as it also serves as the subnet group identifier.
        """
        return pulumi.get(self, "subnet_group_name")

    @subnet_group_name.setter
    def subnet_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_group_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SubnetGroupTagArgs']]]]:
        """
        An array of key-value pairs to apply to this subnet group.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SubnetGroupTagArgs']]]]):
        pulumi.set(self, "tags", value)


class SubnetGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 subnet_group_name: Optional[pulumi.Input[str]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetGroupTagArgs']]]]] = None,
                 __props__=None):
        """
        The AWS::MemoryDB::SubnetGroup resource creates an Amazon MemoryDB Subnet Group.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: An optional description of the subnet group.
        :param pulumi.Input[str] subnet_group_name: The name of the subnet group. This value must be unique as it also serves as the subnet group identifier.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: A list of VPC subnet IDs for the subnet group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetGroupTagArgs']]]] tags: An array of key-value pairs to apply to this subnet group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SubnetGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::MemoryDB::SubnetGroup resource creates an Amazon MemoryDB Subnet Group.

        :param str resource_name: The name of the resource.
        :param SubnetGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SubnetGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            SubnetGroupArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 subnet_group_name: Optional[pulumi.Input[str]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetGroupTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SubnetGroupArgs.__new__(SubnetGroupArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["subnet_group_name"] = subnet_group_name
            if subnet_ids is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_ids'")
            __props__.__dict__["subnet_ids"] = subnet_ids
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["subnet_group_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(SubnetGroup, __self__).__init__(
            'aws-native:memorydb:SubnetGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SubnetGroup':
        """
        Get an existing SubnetGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SubnetGroupArgs.__new__(SubnetGroupArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["subnet_group_name"] = None
        __props__.__dict__["subnet_ids"] = None
        __props__.__dict__["tags"] = None
        return SubnetGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the subnet group.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        An optional description of the subnet group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="subnetGroupName")
    def subnet_group_name(self) -> pulumi.Output[str]:
        """
        The name of the subnet group. This value must be unique as it also serves as the subnet group identifier.
        """
        return pulumi.get(self, "subnet_group_name")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of VPC subnet IDs for the subnet group.
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.SubnetGroupTag']]]:
        """
        An array of key-value pairs to apply to this subnet group.
        """
        return pulumi.get(self, "tags")

