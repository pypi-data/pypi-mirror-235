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

__all__ = [
    'GetViewResult',
    'AwaitableGetViewResult',
    'get_view',
    'get_view_output',
]

@pulumi.output_type
class GetViewResult:
    def __init__(__self__, actions=None, description=None, instance_arn=None, name=None, tags=None, template=None, view_arn=None, view_content_sha256=None, view_id=None):
        if actions and not isinstance(actions, list):
            raise TypeError("Expected argument 'actions' to be a list")
        pulumi.set(__self__, "actions", actions)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if instance_arn and not isinstance(instance_arn, str):
            raise TypeError("Expected argument 'instance_arn' to be a str")
        pulumi.set(__self__, "instance_arn", instance_arn)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if template and not isinstance(template, dict):
            raise TypeError("Expected argument 'template' to be a dict")
        pulumi.set(__self__, "template", template)
        if view_arn and not isinstance(view_arn, str):
            raise TypeError("Expected argument 'view_arn' to be a str")
        pulumi.set(__self__, "view_arn", view_arn)
        if view_content_sha256 and not isinstance(view_content_sha256, str):
            raise TypeError("Expected argument 'view_content_sha256' to be a str")
        pulumi.set(__self__, "view_content_sha256", view_content_sha256)
        if view_id and not isinstance(view_id, str):
            raise TypeError("Expected argument 'view_id' to be a str")
        pulumi.set(__self__, "view_id", view_id)

    @property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[str]]:
        """
        The actions of the view in an array.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the view.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the instance.
        """
        return pulumi.get(self, "instance_arn")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the view.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ViewTag']]:
        """
        One or more tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def template(self) -> Optional[Any]:
        """
        The template of the view as JSON.
        """
        return pulumi.get(self, "template")

    @property
    @pulumi.getter(name="viewArn")
    def view_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the view.
        """
        return pulumi.get(self, "view_arn")

    @property
    @pulumi.getter(name="viewContentSha256")
    def view_content_sha256(self) -> Optional[str]:
        """
        The view content hash.
        """
        return pulumi.get(self, "view_content_sha256")

    @property
    @pulumi.getter(name="viewId")
    def view_id(self) -> Optional[str]:
        """
        The view id of the view.
        """
        return pulumi.get(self, "view_id")


class AwaitableGetViewResult(GetViewResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetViewResult(
            actions=self.actions,
            description=self.description,
            instance_arn=self.instance_arn,
            name=self.name,
            tags=self.tags,
            template=self.template,
            view_arn=self.view_arn,
            view_content_sha256=self.view_content_sha256,
            view_id=self.view_id)


def get_view(view_arn: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetViewResult:
    """
    Resource Type definition for AWS::Connect::View


    :param str view_arn: The Amazon Resource Name (ARN) of the view.
    """
    __args__ = dict()
    __args__['viewArn'] = view_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:connect:getView', __args__, opts=opts, typ=GetViewResult).value

    return AwaitableGetViewResult(
        actions=pulumi.get(__ret__, 'actions'),
        description=pulumi.get(__ret__, 'description'),
        instance_arn=pulumi.get(__ret__, 'instance_arn'),
        name=pulumi.get(__ret__, 'name'),
        tags=pulumi.get(__ret__, 'tags'),
        template=pulumi.get(__ret__, 'template'),
        view_arn=pulumi.get(__ret__, 'view_arn'),
        view_content_sha256=pulumi.get(__ret__, 'view_content_sha256'),
        view_id=pulumi.get(__ret__, 'view_id'))


@_utilities.lift_output_func(get_view)
def get_view_output(view_arn: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetViewResult]:
    """
    Resource Type definition for AWS::Connect::View


    :param str view_arn: The Amazon Resource Name (ARN) of the view.
    """
    ...
