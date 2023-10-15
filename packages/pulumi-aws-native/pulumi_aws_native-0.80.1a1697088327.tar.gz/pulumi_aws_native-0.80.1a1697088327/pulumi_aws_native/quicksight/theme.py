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
from ._enums import *
from ._inputs import *

__all__ = ['ThemeArgs', 'Theme']

@pulumi.input_type
class ThemeArgs:
    def __init__(__self__, *,
                 aws_account_id: pulumi.Input[str],
                 base_theme_id: pulumi.Input[str],
                 configuration: pulumi.Input['ThemeConfigurationArgs'],
                 theme_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input['ThemeResourcePermissionArgs']]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ThemeTagArgs']]]] = None,
                 version_description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Theme resource.
        """
        ThemeArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            aws_account_id=aws_account_id,
            base_theme_id=base_theme_id,
            configuration=configuration,
            theme_id=theme_id,
            name=name,
            permissions=permissions,
            tags=tags,
            version_description=version_description,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             aws_account_id: pulumi.Input[str],
             base_theme_id: pulumi.Input[str],
             configuration: pulumi.Input['ThemeConfigurationArgs'],
             theme_id: pulumi.Input[str],
             name: Optional[pulumi.Input[str]] = None,
             permissions: Optional[pulumi.Input[Sequence[pulumi.Input['ThemeResourcePermissionArgs']]]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['ThemeTagArgs']]]] = None,
             version_description: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("aws_account_id", aws_account_id)
        _setter("base_theme_id", base_theme_id)
        _setter("configuration", configuration)
        _setter("theme_id", theme_id)
        if name is not None:
            _setter("name", name)
        if permissions is not None:
            _setter("permissions", permissions)
        if tags is not None:
            _setter("tags", tags)
        if version_description is not None:
            _setter("version_description", version_description)

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "aws_account_id")

    @aws_account_id.setter
    def aws_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "aws_account_id", value)

    @property
    @pulumi.getter(name="baseThemeId")
    def base_theme_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "base_theme_id")

    @base_theme_id.setter
    def base_theme_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "base_theme_id", value)

    @property
    @pulumi.getter
    def configuration(self) -> pulumi.Input['ThemeConfigurationArgs']:
        return pulumi.get(self, "configuration")

    @configuration.setter
    def configuration(self, value: pulumi.Input['ThemeConfigurationArgs']):
        pulumi.set(self, "configuration", value)

    @property
    @pulumi.getter(name="themeId")
    def theme_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "theme_id")

    @theme_id.setter
    def theme_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "theme_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ThemeResourcePermissionArgs']]]]:
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ThemeResourcePermissionArgs']]]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ThemeTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ThemeTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="versionDescription")
    def version_description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "version_description")

    @version_description.setter
    def version_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version_description", value)


class Theme(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_account_id: Optional[pulumi.Input[str]] = None,
                 base_theme_id: Optional[pulumi.Input[str]] = None,
                 configuration: Optional[pulumi.Input[pulumi.InputType['ThemeConfigurationArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThemeResourcePermissionArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThemeTagArgs']]]]] = None,
                 theme_id: Optional[pulumi.Input[str]] = None,
                 version_description: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Definition of the AWS::QuickSight::Theme Resource Type.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ThemeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of the AWS::QuickSight::Theme Resource Type.

        :param str resource_name: The name of the resource.
        :param ThemeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ThemeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ThemeArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_account_id: Optional[pulumi.Input[str]] = None,
                 base_theme_id: Optional[pulumi.Input[str]] = None,
                 configuration: Optional[pulumi.Input[pulumi.InputType['ThemeConfigurationArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThemeResourcePermissionArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThemeTagArgs']]]]] = None,
                 theme_id: Optional[pulumi.Input[str]] = None,
                 version_description: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ThemeArgs.__new__(ThemeArgs)

            if aws_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'aws_account_id'")
            __props__.__dict__["aws_account_id"] = aws_account_id
            if base_theme_id is None and not opts.urn:
                raise TypeError("Missing required property 'base_theme_id'")
            __props__.__dict__["base_theme_id"] = base_theme_id
            if configuration is not None and not isinstance(configuration, ThemeConfigurationArgs):
                configuration = configuration or {}
                def _setter(key, value):
                    configuration[key] = value
                ThemeConfigurationArgs._configure(_setter, **configuration)
            if configuration is None and not opts.urn:
                raise TypeError("Missing required property 'configuration'")
            __props__.__dict__["configuration"] = configuration
            __props__.__dict__["name"] = name
            __props__.__dict__["permissions"] = permissions
            __props__.__dict__["tags"] = tags
            if theme_id is None and not opts.urn:
                raise TypeError("Missing required property 'theme_id'")
            __props__.__dict__["theme_id"] = theme_id
            __props__.__dict__["version_description"] = version_description
            __props__.__dict__["arn"] = None
            __props__.__dict__["created_time"] = None
            __props__.__dict__["last_updated_time"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["version"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["aws_account_id", "theme_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Theme, __self__).__init__(
            'aws-native:quicksight:Theme',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Theme':
        """
        Get an existing Theme resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ThemeArgs.__new__(ThemeArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["aws_account_id"] = None
        __props__.__dict__["base_theme_id"] = None
        __props__.__dict__["configuration"] = None
        __props__.__dict__["created_time"] = None
        __props__.__dict__["last_updated_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["permissions"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["theme_id"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version"] = None
        __props__.__dict__["version_description"] = None
        return Theme(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "aws_account_id")

    @property
    @pulumi.getter(name="baseThemeId")
    def base_theme_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "base_theme_id")

    @property
    @pulumi.getter
    def configuration(self) -> pulumi.Output['outputs.ThemeConfiguration']:
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Optional[Sequence['outputs.ThemeResourcePermission']]]:
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ThemeTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="themeId")
    def theme_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "theme_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output['ThemeType']:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output['outputs.ThemeVersion']:
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="versionDescription")
    def version_description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "version_description")

