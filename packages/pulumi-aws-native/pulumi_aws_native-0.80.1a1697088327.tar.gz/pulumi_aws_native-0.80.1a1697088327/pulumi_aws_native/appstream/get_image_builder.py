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
    'GetImageBuilderResult',
    'AwaitableGetImageBuilderResult',
    'get_image_builder',
    'get_image_builder_output',
]

@pulumi.output_type
class GetImageBuilderResult:
    def __init__(__self__, access_endpoints=None, appstream_agent_version=None, description=None, display_name=None, domain_join_info=None, enable_default_internet_access=None, iam_role_arn=None, image_arn=None, image_name=None, instance_type=None, name=None, streaming_url=None, tags=None, vpc_config=None):
        if access_endpoints and not isinstance(access_endpoints, list):
            raise TypeError("Expected argument 'access_endpoints' to be a list")
        pulumi.set(__self__, "access_endpoints", access_endpoints)
        if appstream_agent_version and not isinstance(appstream_agent_version, str):
            raise TypeError("Expected argument 'appstream_agent_version' to be a str")
        pulumi.set(__self__, "appstream_agent_version", appstream_agent_version)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if domain_join_info and not isinstance(domain_join_info, dict):
            raise TypeError("Expected argument 'domain_join_info' to be a dict")
        pulumi.set(__self__, "domain_join_info", domain_join_info)
        if enable_default_internet_access and not isinstance(enable_default_internet_access, bool):
            raise TypeError("Expected argument 'enable_default_internet_access' to be a bool")
        pulumi.set(__self__, "enable_default_internet_access", enable_default_internet_access)
        if iam_role_arn and not isinstance(iam_role_arn, str):
            raise TypeError("Expected argument 'iam_role_arn' to be a str")
        pulumi.set(__self__, "iam_role_arn", iam_role_arn)
        if image_arn and not isinstance(image_arn, str):
            raise TypeError("Expected argument 'image_arn' to be a str")
        pulumi.set(__self__, "image_arn", image_arn)
        if image_name and not isinstance(image_name, str):
            raise TypeError("Expected argument 'image_name' to be a str")
        pulumi.set(__self__, "image_name", image_name)
        if instance_type and not isinstance(instance_type, str):
            raise TypeError("Expected argument 'instance_type' to be a str")
        pulumi.set(__self__, "instance_type", instance_type)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if streaming_url and not isinstance(streaming_url, str):
            raise TypeError("Expected argument 'streaming_url' to be a str")
        pulumi.set(__self__, "streaming_url", streaming_url)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if vpc_config and not isinstance(vpc_config, dict):
            raise TypeError("Expected argument 'vpc_config' to be a dict")
        pulumi.set(__self__, "vpc_config", vpc_config)

    @property
    @pulumi.getter(name="accessEndpoints")
    def access_endpoints(self) -> Optional[Sequence['outputs.ImageBuilderAccessEndpoint']]:
        return pulumi.get(self, "access_endpoints")

    @property
    @pulumi.getter(name="appstreamAgentVersion")
    def appstream_agent_version(self) -> Optional[str]:
        return pulumi.get(self, "appstream_agent_version")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="domainJoinInfo")
    def domain_join_info(self) -> Optional['outputs.ImageBuilderDomainJoinInfo']:
        return pulumi.get(self, "domain_join_info")

    @property
    @pulumi.getter(name="enableDefaultInternetAccess")
    def enable_default_internet_access(self) -> Optional[bool]:
        return pulumi.get(self, "enable_default_internet_access")

    @property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> Optional[str]:
        return pulumi.get(self, "iam_role_arn")

    @property
    @pulumi.getter(name="imageArn")
    def image_arn(self) -> Optional[str]:
        return pulumi.get(self, "image_arn")

    @property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[str]:
        return pulumi.get(self, "image_name")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[str]:
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="streamingUrl")
    def streaming_url(self) -> Optional[str]:
        return pulumi.get(self, "streaming_url")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ImageBuilderTag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional['outputs.ImageBuilderVpcConfig']:
        return pulumi.get(self, "vpc_config")


class AwaitableGetImageBuilderResult(GetImageBuilderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetImageBuilderResult(
            access_endpoints=self.access_endpoints,
            appstream_agent_version=self.appstream_agent_version,
            description=self.description,
            display_name=self.display_name,
            domain_join_info=self.domain_join_info,
            enable_default_internet_access=self.enable_default_internet_access,
            iam_role_arn=self.iam_role_arn,
            image_arn=self.image_arn,
            image_name=self.image_name,
            instance_type=self.instance_type,
            name=self.name,
            streaming_url=self.streaming_url,
            tags=self.tags,
            vpc_config=self.vpc_config)


def get_image_builder(name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetImageBuilderResult:
    """
    Resource Type definition for AWS::AppStream::ImageBuilder
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:appstream:getImageBuilder', __args__, opts=opts, typ=GetImageBuilderResult).value

    return AwaitableGetImageBuilderResult(
        access_endpoints=pulumi.get(__ret__, 'access_endpoints'),
        appstream_agent_version=pulumi.get(__ret__, 'appstream_agent_version'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        domain_join_info=pulumi.get(__ret__, 'domain_join_info'),
        enable_default_internet_access=pulumi.get(__ret__, 'enable_default_internet_access'),
        iam_role_arn=pulumi.get(__ret__, 'iam_role_arn'),
        image_arn=pulumi.get(__ret__, 'image_arn'),
        image_name=pulumi.get(__ret__, 'image_name'),
        instance_type=pulumi.get(__ret__, 'instance_type'),
        name=pulumi.get(__ret__, 'name'),
        streaming_url=pulumi.get(__ret__, 'streaming_url'),
        tags=pulumi.get(__ret__, 'tags'),
        vpc_config=pulumi.get(__ret__, 'vpc_config'))


@_utilities.lift_output_func(get_image_builder)
def get_image_builder_output(name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetImageBuilderResult]:
    """
    Resource Type definition for AWS::AppStream::ImageBuilder
    """
    ...
