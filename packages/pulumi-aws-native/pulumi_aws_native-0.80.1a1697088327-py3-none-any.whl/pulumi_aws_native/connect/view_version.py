# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ViewVersionArgs', 'ViewVersion']

@pulumi.input_type
class ViewVersionArgs:
    def __init__(__self__, *,
                 view_arn: pulumi.Input[str],
                 version_description: Optional[pulumi.Input[str]] = None,
                 view_content_sha256: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ViewVersion resource.
        :param pulumi.Input[str] view_arn: The Amazon Resource Name (ARN) of the view for which a version is being created.
        :param pulumi.Input[str] version_description: The description for the view version.
        :param pulumi.Input[str] view_content_sha256: The view content hash to be checked.
        """
        ViewVersionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            view_arn=view_arn,
            version_description=version_description,
            view_content_sha256=view_content_sha256,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             view_arn: pulumi.Input[str],
             version_description: Optional[pulumi.Input[str]] = None,
             view_content_sha256: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("view_arn", view_arn)
        if version_description is not None:
            _setter("version_description", version_description)
        if view_content_sha256 is not None:
            _setter("view_content_sha256", view_content_sha256)

    @property
    @pulumi.getter(name="viewArn")
    def view_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of the view for which a version is being created.
        """
        return pulumi.get(self, "view_arn")

    @view_arn.setter
    def view_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "view_arn", value)

    @property
    @pulumi.getter(name="versionDescription")
    def version_description(self) -> Optional[pulumi.Input[str]]:
        """
        The description for the view version.
        """
        return pulumi.get(self, "version_description")

    @version_description.setter
    def version_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version_description", value)

    @property
    @pulumi.getter(name="viewContentSha256")
    def view_content_sha256(self) -> Optional[pulumi.Input[str]]:
        """
        The view content hash to be checked.
        """
        return pulumi.get(self, "view_content_sha256")

    @view_content_sha256.setter
    def view_content_sha256(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "view_content_sha256", value)


class ViewVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 version_description: Optional[pulumi.Input[str]] = None,
                 view_arn: Optional[pulumi.Input[str]] = None,
                 view_content_sha256: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Connect::ViewVersion

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] version_description: The description for the view version.
        :param pulumi.Input[str] view_arn: The Amazon Resource Name (ARN) of the view for which a version is being created.
        :param pulumi.Input[str] view_content_sha256: The view content hash to be checked.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ViewVersionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Connect::ViewVersion

        :param str resource_name: The name of the resource.
        :param ViewVersionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ViewVersionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ViewVersionArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 version_description: Optional[pulumi.Input[str]] = None,
                 view_arn: Optional[pulumi.Input[str]] = None,
                 view_content_sha256: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ViewVersionArgs.__new__(ViewVersionArgs)

            __props__.__dict__["version_description"] = version_description
            if view_arn is None and not opts.urn:
                raise TypeError("Missing required property 'view_arn'")
            __props__.__dict__["view_arn"] = view_arn
            __props__.__dict__["view_content_sha256"] = view_content_sha256
            __props__.__dict__["version"] = None
            __props__.__dict__["view_version_arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["version_description", "view_arn", "view_content_sha256"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ViewVersion, __self__).__init__(
            'aws-native:connect:ViewVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ViewVersion':
        """
        Get an existing ViewVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ViewVersionArgs.__new__(ViewVersionArgs)

        __props__.__dict__["version"] = None
        __props__.__dict__["version_description"] = None
        __props__.__dict__["view_arn"] = None
        __props__.__dict__["view_content_sha256"] = None
        __props__.__dict__["view_version_arn"] = None
        return ViewVersion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[int]:
        """
        The version of the view.
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="versionDescription")
    def version_description(self) -> pulumi.Output[Optional[str]]:
        """
        The description for the view version.
        """
        return pulumi.get(self, "version_description")

    @property
    @pulumi.getter(name="viewArn")
    def view_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the view for which a version is being created.
        """
        return pulumi.get(self, "view_arn")

    @property
    @pulumi.getter(name="viewContentSha256")
    def view_content_sha256(self) -> pulumi.Output[Optional[str]]:
        """
        The view content hash to be checked.
        """
        return pulumi.get(self, "view_content_sha256")

    @property
    @pulumi.getter(name="viewVersionArn")
    def view_version_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the created view version.
        """
        return pulumi.get(self, "view_version_arn")

