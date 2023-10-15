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

__all__ = ['StreamingImageArgs', 'StreamingImage']

@pulumi.input_type
class StreamingImageArgs:
    def __init__(__self__, *,
                 ec2_image_id: pulumi.Input[str],
                 studio_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input['StreamingImageTagsArgs']] = None):
        """
        The set of arguments for constructing a StreamingImage resource.
        :param pulumi.Input[str] ec2_image_id: <p>The ID of an EC2 machine image with which to create this streaming image.</p>
        :param pulumi.Input[str] studio_id: <p>The studioId. </p>
        :param pulumi.Input[str] description: <p>A human-readable description of the streaming image.</p>
        :param pulumi.Input[str] name: <p>A friendly name for a streaming image resource.</p>
        """
        StreamingImageArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            ec2_image_id=ec2_image_id,
            studio_id=studio_id,
            description=description,
            name=name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             ec2_image_id: pulumi.Input[str],
             studio_id: pulumi.Input[str],
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input['StreamingImageTagsArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("ec2_image_id", ec2_image_id)
        _setter("studio_id", studio_id)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="ec2ImageId")
    def ec2_image_id(self) -> pulumi.Input[str]:
        """
        <p>The ID of an EC2 machine image with which to create this streaming image.</p>
        """
        return pulumi.get(self, "ec2_image_id")

    @ec2_image_id.setter
    def ec2_image_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "ec2_image_id", value)

    @property
    @pulumi.getter(name="studioId")
    def studio_id(self) -> pulumi.Input[str]:
        """
        <p>The studioId. </p>
        """
        return pulumi.get(self, "studio_id")

    @studio_id.setter
    def studio_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "studio_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        <p>A human-readable description of the streaming image.</p>
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        <p>A friendly name for a streaming image resource.</p>
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input['StreamingImageTagsArgs']]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input['StreamingImageTagsArgs']]):
        pulumi.set(self, "tags", value)


class StreamingImage(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ec2_image_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 studio_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[pulumi.InputType['StreamingImageTagsArgs']]] = None,
                 __props__=None):
        """
        Represents a streaming session machine image that can be used to launch a streaming session

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: <p>A human-readable description of the streaming image.</p>
        :param pulumi.Input[str] ec2_image_id: <p>The ID of an EC2 machine image with which to create this streaming image.</p>
        :param pulumi.Input[str] name: <p>A friendly name for a streaming image resource.</p>
        :param pulumi.Input[str] studio_id: <p>The studioId. </p>
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StreamingImageArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a streaming session machine image that can be used to launch a streaming session

        :param str resource_name: The name of the resource.
        :param StreamingImageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StreamingImageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            StreamingImageArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ec2_image_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 studio_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[pulumi.InputType['StreamingImageTagsArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StreamingImageArgs.__new__(StreamingImageArgs)

            __props__.__dict__["description"] = description
            if ec2_image_id is None and not opts.urn:
                raise TypeError("Missing required property 'ec2_image_id'")
            __props__.__dict__["ec2_image_id"] = ec2_image_id
            __props__.__dict__["name"] = name
            if studio_id is None and not opts.urn:
                raise TypeError("Missing required property 'studio_id'")
            __props__.__dict__["studio_id"] = studio_id
            if tags is not None and not isinstance(tags, StreamingImageTagsArgs):
                tags = tags or {}
                def _setter(key, value):
                    tags[key] = value
                StreamingImageTagsArgs._configure(_setter, **tags)
            __props__.__dict__["tags"] = tags
            __props__.__dict__["encryption_configuration"] = None
            __props__.__dict__["eula_ids"] = None
            __props__.__dict__["owner"] = None
            __props__.__dict__["platform"] = None
            __props__.__dict__["streaming_image_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["ec2_image_id", "studio_id", "tags"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(StreamingImage, __self__).__init__(
            'aws-native:nimblestudio:StreamingImage',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StreamingImage':
        """
        Get an existing StreamingImage resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StreamingImageArgs.__new__(StreamingImageArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["ec2_image_id"] = None
        __props__.__dict__["encryption_configuration"] = None
        __props__.__dict__["eula_ids"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["owner"] = None
        __props__.__dict__["platform"] = None
        __props__.__dict__["streaming_image_id"] = None
        __props__.__dict__["studio_id"] = None
        __props__.__dict__["tags"] = None
        return StreamingImage(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        <p>A human-readable description of the streaming image.</p>
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="ec2ImageId")
    def ec2_image_id(self) -> pulumi.Output[str]:
        """
        <p>The ID of an EC2 machine image with which to create this streaming image.</p>
        """
        return pulumi.get(self, "ec2_image_id")

    @property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> pulumi.Output['outputs.StreamingImageEncryptionConfiguration']:
        return pulumi.get(self, "encryption_configuration")

    @property
    @pulumi.getter(name="eulaIds")
    def eula_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        <p>The list of EULAs that must be accepted before a Streaming Session can be started using this streaming image.</p>
        """
        return pulumi.get(self, "eula_ids")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        <p>A friendly name for a streaming image resource.</p>
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[str]:
        """
        <p>The owner of the streaming image, either the studioId that contains the streaming image, or 'amazon' for images that are provided by Amazon Nimble Studio.</p>
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter
    def platform(self) -> pulumi.Output[str]:
        """
        <p>The platform of the streaming image, either WINDOWS or LINUX.</p>
        """
        return pulumi.get(self, "platform")

    @property
    @pulumi.getter(name="streamingImageId")
    def streaming_image_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "streaming_image_id")

    @property
    @pulumi.getter(name="studioId")
    def studio_id(self) -> pulumi.Output[str]:
        """
        <p>The studioId. </p>
        """
        return pulumi.get(self, "studio_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional['outputs.StreamingImageTags']]:
        return pulumi.get(self, "tags")

