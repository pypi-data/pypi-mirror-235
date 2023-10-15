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

__all__ = ['LiveSourceArgs', 'LiveSource']

@pulumi.input_type
class LiveSourceArgs:
    def __init__(__self__, *,
                 http_package_configurations: pulumi.Input[Sequence[pulumi.Input['LiveSourceHttpPackageConfigurationArgs']]],
                 source_location_name: pulumi.Input[str],
                 live_source_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['LiveSourceTagArgs']]]] = None):
        """
        The set of arguments for constructing a LiveSource resource.
        :param pulumi.Input[Sequence[pulumi.Input['LiveSourceHttpPackageConfigurationArgs']]] http_package_configurations: <p>A list of HTTP package configuration parameters for this live source.</p>
        :param pulumi.Input[Sequence[pulumi.Input['LiveSourceTagArgs']]] tags: The tags to assign to the live source.
        """
        LiveSourceArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            http_package_configurations=http_package_configurations,
            source_location_name=source_location_name,
            live_source_name=live_source_name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             http_package_configurations: pulumi.Input[Sequence[pulumi.Input['LiveSourceHttpPackageConfigurationArgs']]],
             source_location_name: pulumi.Input[str],
             live_source_name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['LiveSourceTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("http_package_configurations", http_package_configurations)
        _setter("source_location_name", source_location_name)
        if live_source_name is not None:
            _setter("live_source_name", live_source_name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="httpPackageConfigurations")
    def http_package_configurations(self) -> pulumi.Input[Sequence[pulumi.Input['LiveSourceHttpPackageConfigurationArgs']]]:
        """
        <p>A list of HTTP package configuration parameters for this live source.</p>
        """
        return pulumi.get(self, "http_package_configurations")

    @http_package_configurations.setter
    def http_package_configurations(self, value: pulumi.Input[Sequence[pulumi.Input['LiveSourceHttpPackageConfigurationArgs']]]):
        pulumi.set(self, "http_package_configurations", value)

    @property
    @pulumi.getter(name="sourceLocationName")
    def source_location_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "source_location_name")

    @source_location_name.setter
    def source_location_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_location_name", value)

    @property
    @pulumi.getter(name="liveSourceName")
    def live_source_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "live_source_name")

    @live_source_name.setter
    def live_source_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "live_source_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LiveSourceTagArgs']]]]:
        """
        The tags to assign to the live source.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LiveSourceTagArgs']]]]):
        pulumi.set(self, "tags", value)


class LiveSource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 http_package_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LiveSourceHttpPackageConfigurationArgs']]]]] = None,
                 live_source_name: Optional[pulumi.Input[str]] = None,
                 source_location_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LiveSourceTagArgs']]]]] = None,
                 __props__=None):
        """
        Definition of AWS::MediaTailor::LiveSource Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LiveSourceHttpPackageConfigurationArgs']]]] http_package_configurations: <p>A list of HTTP package configuration parameters for this live source.</p>
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LiveSourceTagArgs']]]] tags: The tags to assign to the live source.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LiveSourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::MediaTailor::LiveSource Resource Type

        :param str resource_name: The name of the resource.
        :param LiveSourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LiveSourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            LiveSourceArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 http_package_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LiveSourceHttpPackageConfigurationArgs']]]]] = None,
                 live_source_name: Optional[pulumi.Input[str]] = None,
                 source_location_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LiveSourceTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LiveSourceArgs.__new__(LiveSourceArgs)

            if http_package_configurations is None and not opts.urn:
                raise TypeError("Missing required property 'http_package_configurations'")
            __props__.__dict__["http_package_configurations"] = http_package_configurations
            __props__.__dict__["live_source_name"] = live_source_name
            if source_location_name is None and not opts.urn:
                raise TypeError("Missing required property 'source_location_name'")
            __props__.__dict__["source_location_name"] = source_location_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["live_source_name", "source_location_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(LiveSource, __self__).__init__(
            'aws-native:mediatailor:LiveSource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LiveSource':
        """
        Get an existing LiveSource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LiveSourceArgs.__new__(LiveSourceArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["http_package_configurations"] = None
        __props__.__dict__["live_source_name"] = None
        __props__.__dict__["source_location_name"] = None
        __props__.__dict__["tags"] = None
        return LiveSource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        <p>The ARN of the live source.</p>
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="httpPackageConfigurations")
    def http_package_configurations(self) -> pulumi.Output[Sequence['outputs.LiveSourceHttpPackageConfiguration']]:
        """
        <p>A list of HTTP package configuration parameters for this live source.</p>
        """
        return pulumi.get(self, "http_package_configurations")

    @property
    @pulumi.getter(name="liveSourceName")
    def live_source_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "live_source_name")

    @property
    @pulumi.getter(name="sourceLocationName")
    def source_location_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "source_location_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.LiveSourceTag']]]:
        """
        The tags to assign to the live source.
        """
        return pulumi.get(self, "tags")

