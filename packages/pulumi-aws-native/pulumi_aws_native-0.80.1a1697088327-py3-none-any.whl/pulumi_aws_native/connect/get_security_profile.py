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
    'GetSecurityProfileResult',
    'AwaitableGetSecurityProfileResult',
    'get_security_profile',
    'get_security_profile_output',
]

@pulumi.output_type
class GetSecurityProfileResult:
    def __init__(__self__, allowed_access_control_tags=None, description=None, permissions=None, security_profile_arn=None, tag_restricted_resources=None, tags=None):
        if allowed_access_control_tags and not isinstance(allowed_access_control_tags, list):
            raise TypeError("Expected argument 'allowed_access_control_tags' to be a list")
        pulumi.set(__self__, "allowed_access_control_tags", allowed_access_control_tags)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if permissions and not isinstance(permissions, list):
            raise TypeError("Expected argument 'permissions' to be a list")
        pulumi.set(__self__, "permissions", permissions)
        if security_profile_arn and not isinstance(security_profile_arn, str):
            raise TypeError("Expected argument 'security_profile_arn' to be a str")
        pulumi.set(__self__, "security_profile_arn", security_profile_arn)
        if tag_restricted_resources and not isinstance(tag_restricted_resources, list):
            raise TypeError("Expected argument 'tag_restricted_resources' to be a list")
        pulumi.set(__self__, "tag_restricted_resources", tag_restricted_resources)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="allowedAccessControlTags")
    def allowed_access_control_tags(self) -> Optional[Sequence['outputs.SecurityProfileTag']]:
        """
        The list of tags that a security profile uses to restrict access to resources in Amazon Connect.
        """
        return pulumi.get(self, "allowed_access_control_tags")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the security profile.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def permissions(self) -> Optional[Sequence[str]]:
        """
        Permissions assigned to the security profile.
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter(name="securityProfileArn")
    def security_profile_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) for the security profile.
        """
        return pulumi.get(self, "security_profile_arn")

    @property
    @pulumi.getter(name="tagRestrictedResources")
    def tag_restricted_resources(self) -> Optional[Sequence[str]]:
        """
        The list of resources that a security profile applies tag restrictions to in Amazon Connect.
        """
        return pulumi.get(self, "tag_restricted_resources")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.SecurityProfileTag']]:
        """
        The tags used to organize, track, or control access for this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetSecurityProfileResult(GetSecurityProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecurityProfileResult(
            allowed_access_control_tags=self.allowed_access_control_tags,
            description=self.description,
            permissions=self.permissions,
            security_profile_arn=self.security_profile_arn,
            tag_restricted_resources=self.tag_restricted_resources,
            tags=self.tags)


def get_security_profile(security_profile_arn: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecurityProfileResult:
    """
    Resource Type definition for AWS::Connect::SecurityProfile


    :param str security_profile_arn: The Amazon Resource Name (ARN) for the security profile.
    """
    __args__ = dict()
    __args__['securityProfileArn'] = security_profile_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:connect:getSecurityProfile', __args__, opts=opts, typ=GetSecurityProfileResult).value

    return AwaitableGetSecurityProfileResult(
        allowed_access_control_tags=pulumi.get(__ret__, 'allowed_access_control_tags'),
        description=pulumi.get(__ret__, 'description'),
        permissions=pulumi.get(__ret__, 'permissions'),
        security_profile_arn=pulumi.get(__ret__, 'security_profile_arn'),
        tag_restricted_resources=pulumi.get(__ret__, 'tag_restricted_resources'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_security_profile)
def get_security_profile_output(security_profile_arn: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecurityProfileResult]:
    """
    Resource Type definition for AWS::Connect::SecurityProfile


    :param str security_profile_arn: The Amazon Resource Name (ARN) for the security profile.
    """
    ...
