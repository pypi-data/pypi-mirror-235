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

__all__ = ['DiscovererArgs', 'Discoverer']

@pulumi.input_type
class DiscovererArgs:
    def __init__(__self__, *,
                 source_arn: pulumi.Input[str],
                 cross_account: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DiscovererTagsEntryArgs']]]] = None):
        """
        The set of arguments for constructing a Discoverer resource.
        """
        DiscovererArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            source_arn=source_arn,
            cross_account=cross_account,
            description=description,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             source_arn: pulumi.Input[str],
             cross_account: Optional[pulumi.Input[bool]] = None,
             description: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['DiscovererTagsEntryArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("source_arn", source_arn)
        if cross_account is not None:
            _setter("cross_account", cross_account)
        if description is not None:
            _setter("description", description)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "source_arn")

    @source_arn.setter
    def source_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_arn", value)

    @property
    @pulumi.getter(name="crossAccount")
    def cross_account(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "cross_account")

    @cross_account.setter
    def cross_account(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "cross_account", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DiscovererTagsEntryArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DiscovererTagsEntryArgs']]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""Discoverer is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Discoverer(pulumi.CustomResource):
    warnings.warn("""Discoverer is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cross_account: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 source_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DiscovererTagsEntryArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EventSchemas::Discoverer

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DiscovererArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EventSchemas::Discoverer

        :param str resource_name: The name of the resource.
        :param DiscovererArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DiscovererArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DiscovererArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cross_account: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 source_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DiscovererTagsEntryArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""Discoverer is deprecated: Discoverer is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DiscovererArgs.__new__(DiscovererArgs)

            __props__.__dict__["cross_account"] = cross_account
            __props__.__dict__["description"] = description
            if source_arn is None and not opts.urn:
                raise TypeError("Missing required property 'source_arn'")
            __props__.__dict__["source_arn"] = source_arn
            __props__.__dict__["tags"] = tags
            __props__.__dict__["discoverer_arn"] = None
            __props__.__dict__["discoverer_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["source_arn"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Discoverer, __self__).__init__(
            'aws-native:eventschemas:Discoverer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Discoverer':
        """
        Get an existing Discoverer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DiscovererArgs.__new__(DiscovererArgs)

        __props__.__dict__["cross_account"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["discoverer_arn"] = None
        __props__.__dict__["discoverer_id"] = None
        __props__.__dict__["source_arn"] = None
        __props__.__dict__["tags"] = None
        return Discoverer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="crossAccount")
    def cross_account(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "cross_account")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="discovererArn")
    def discoverer_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "discoverer_arn")

    @property
    @pulumi.getter(name="discovererId")
    def discoverer_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "discoverer_id")

    @property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "source_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DiscovererTagsEntry']]]:
        return pulumi.get(self, "tags")

