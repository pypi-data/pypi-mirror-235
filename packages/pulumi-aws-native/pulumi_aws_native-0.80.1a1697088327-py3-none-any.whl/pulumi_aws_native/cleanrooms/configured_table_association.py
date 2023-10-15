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

__all__ = ['ConfiguredTableAssociationArgs', 'ConfiguredTableAssociation']

@pulumi.input_type
class ConfiguredTableAssociationArgs:
    def __init__(__self__, *,
                 configured_table_identifier: pulumi.Input[str],
                 membership_identifier: pulumi.Input[str],
                 role_arn: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ConfiguredTableAssociationTagArgs']]]] = None):
        """
        The set of arguments for constructing a ConfiguredTableAssociation resource.
        :param pulumi.Input[Sequence[pulumi.Input['ConfiguredTableAssociationTagArgs']]] tags: An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.
        """
        ConfiguredTableAssociationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            configured_table_identifier=configured_table_identifier,
            membership_identifier=membership_identifier,
            role_arn=role_arn,
            description=description,
            name=name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             configured_table_identifier: pulumi.Input[str],
             membership_identifier: pulumi.Input[str],
             role_arn: pulumi.Input[str],
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['ConfiguredTableAssociationTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("configured_table_identifier", configured_table_identifier)
        _setter("membership_identifier", membership_identifier)
        _setter("role_arn", role_arn)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="configuredTableIdentifier")
    def configured_table_identifier(self) -> pulumi.Input[str]:
        return pulumi.get(self, "configured_table_identifier")

    @configured_table_identifier.setter
    def configured_table_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "configured_table_identifier", value)

    @property
    @pulumi.getter(name="membershipIdentifier")
    def membership_identifier(self) -> pulumi.Input[str]:
        return pulumi.get(self, "membership_identifier")

    @membership_identifier.setter
    def membership_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "membership_identifier", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConfiguredTableAssociationTagArgs']]]]:
        """
        An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConfiguredTableAssociationTagArgs']]]]):
        pulumi.set(self, "tags", value)


class ConfiguredTableAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configured_table_identifier: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 membership_identifier: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfiguredTableAssociationTagArgs']]]]] = None,
                 __props__=None):
        """
        Represents a table that can be queried within a collaboration

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfiguredTableAssociationTagArgs']]]] tags: An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConfiguredTableAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a table that can be queried within a collaboration

        :param str resource_name: The name of the resource.
        :param ConfiguredTableAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConfiguredTableAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ConfiguredTableAssociationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configured_table_identifier: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 membership_identifier: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfiguredTableAssociationTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConfiguredTableAssociationArgs.__new__(ConfiguredTableAssociationArgs)

            if configured_table_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'configured_table_identifier'")
            __props__.__dict__["configured_table_identifier"] = configured_table_identifier
            __props__.__dict__["description"] = description
            if membership_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'membership_identifier'")
            __props__.__dict__["membership_identifier"] = membership_identifier
            __props__.__dict__["name"] = name
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["configured_table_association_identifier"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["configured_table_identifier", "membership_identifier", "name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ConfiguredTableAssociation, __self__).__init__(
            'aws-native:cleanrooms:ConfiguredTableAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConfiguredTableAssociation':
        """
        Get an existing ConfiguredTableAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConfiguredTableAssociationArgs.__new__(ConfiguredTableAssociationArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["configured_table_association_identifier"] = None
        __props__.__dict__["configured_table_identifier"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["membership_identifier"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["role_arn"] = None
        __props__.__dict__["tags"] = None
        return ConfiguredTableAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="configuredTableAssociationIdentifier")
    def configured_table_association_identifier(self) -> pulumi.Output[str]:
        return pulumi.get(self, "configured_table_association_identifier")

    @property
    @pulumi.getter(name="configuredTableIdentifier")
    def configured_table_identifier(self) -> pulumi.Output[str]:
        return pulumi.get(self, "configured_table_identifier")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="membershipIdentifier")
    def membership_identifier(self) -> pulumi.Output[str]:
        return pulumi.get(self, "membership_identifier")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ConfiguredTableAssociationTag']]]:
        """
        An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.
        """
        return pulumi.get(self, "tags")

