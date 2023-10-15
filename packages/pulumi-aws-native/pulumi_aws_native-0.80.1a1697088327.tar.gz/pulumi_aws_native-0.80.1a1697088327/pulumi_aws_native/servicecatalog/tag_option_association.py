# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['TagOptionAssociationArgs', 'TagOptionAssociation']

@pulumi.input_type
class TagOptionAssociationArgs:
    def __init__(__self__, *,
                 resource_id: pulumi.Input[str],
                 tag_option_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a TagOptionAssociation resource.
        """
        TagOptionAssociationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            resource_id=resource_id,
            tag_option_id=tag_option_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             resource_id: pulumi.Input[str],
             tag_option_id: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("resource_id", resource_id)
        _setter("tag_option_id", tag_option_id)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="tagOptionId")
    def tag_option_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "tag_option_id")

    @tag_option_id.setter
    def tag_option_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "tag_option_id", value)


warnings.warn("""TagOptionAssociation is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class TagOptionAssociation(pulumi.CustomResource):
    warnings.warn("""TagOptionAssociation is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 tag_option_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::ServiceCatalog::TagOptionAssociation

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TagOptionAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::ServiceCatalog::TagOptionAssociation

        :param str resource_name: The name of the resource.
        :param TagOptionAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TagOptionAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            TagOptionAssociationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 tag_option_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""TagOptionAssociation is deprecated: TagOptionAssociation is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TagOptionAssociationArgs.__new__(TagOptionAssociationArgs)

            if resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'resource_id'")
            __props__.__dict__["resource_id"] = resource_id
            if tag_option_id is None and not opts.urn:
                raise TypeError("Missing required property 'tag_option_id'")
            __props__.__dict__["tag_option_id"] = tag_option_id
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["resource_id", "tag_option_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(TagOptionAssociation, __self__).__init__(
            'aws-native:servicecatalog:TagOptionAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TagOptionAssociation':
        """
        Get an existing TagOptionAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TagOptionAssociationArgs.__new__(TagOptionAssociationArgs)

        __props__.__dict__["resource_id"] = None
        __props__.__dict__["tag_option_id"] = None
        return TagOptionAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="tagOptionId")
    def tag_option_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "tag_option_id")

