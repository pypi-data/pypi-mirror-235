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

__all__ = [
    'GetAuthorizerResult',
    'AwaitableGetAuthorizerResult',
    'get_authorizer',
    'get_authorizer_output',
]

@pulumi.output_type
class GetAuthorizerResult:
    def __init__(__self__, arn=None, authorizer_function_arn=None, enable_caching_for_http=None, status=None, tags=None, token_key_name=None, token_signing_public_keys=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if authorizer_function_arn and not isinstance(authorizer_function_arn, str):
            raise TypeError("Expected argument 'authorizer_function_arn' to be a str")
        pulumi.set(__self__, "authorizer_function_arn", authorizer_function_arn)
        if enable_caching_for_http and not isinstance(enable_caching_for_http, bool):
            raise TypeError("Expected argument 'enable_caching_for_http' to be a bool")
        pulumi.set(__self__, "enable_caching_for_http", enable_caching_for_http)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if token_key_name and not isinstance(token_key_name, str):
            raise TypeError("Expected argument 'token_key_name' to be a str")
        pulumi.set(__self__, "token_key_name", token_key_name)
        if token_signing_public_keys and not isinstance(token_signing_public_keys, dict):
            raise TypeError("Expected argument 'token_signing_public_keys' to be a dict")
        pulumi.set(__self__, "token_signing_public_keys", token_signing_public_keys)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="authorizerFunctionArn")
    def authorizer_function_arn(self) -> Optional[str]:
        return pulumi.get(self, "authorizer_function_arn")

    @property
    @pulumi.getter(name="enableCachingForHttp")
    def enable_caching_for_http(self) -> Optional[bool]:
        return pulumi.get(self, "enable_caching_for_http")

    @property
    @pulumi.getter
    def status(self) -> Optional['AuthorizerStatus']:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.AuthorizerTag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tokenKeyName")
    def token_key_name(self) -> Optional[str]:
        return pulumi.get(self, "token_key_name")

    @property
    @pulumi.getter(name="tokenSigningPublicKeys")
    def token_signing_public_keys(self) -> Optional[Any]:
        return pulumi.get(self, "token_signing_public_keys")


class AwaitableGetAuthorizerResult(GetAuthorizerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAuthorizerResult(
            arn=self.arn,
            authorizer_function_arn=self.authorizer_function_arn,
            enable_caching_for_http=self.enable_caching_for_http,
            status=self.status,
            tags=self.tags,
            token_key_name=self.token_key_name,
            token_signing_public_keys=self.token_signing_public_keys)


def get_authorizer(authorizer_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAuthorizerResult:
    """
    Creates an authorizer.
    """
    __args__ = dict()
    __args__['authorizerName'] = authorizer_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:iot:getAuthorizer', __args__, opts=opts, typ=GetAuthorizerResult).value

    return AwaitableGetAuthorizerResult(
        arn=pulumi.get(__ret__, 'arn'),
        authorizer_function_arn=pulumi.get(__ret__, 'authorizer_function_arn'),
        enable_caching_for_http=pulumi.get(__ret__, 'enable_caching_for_http'),
        status=pulumi.get(__ret__, 'status'),
        tags=pulumi.get(__ret__, 'tags'),
        token_key_name=pulumi.get(__ret__, 'token_key_name'),
        token_signing_public_keys=pulumi.get(__ret__, 'token_signing_public_keys'))


@_utilities.lift_output_func(get_authorizer)
def get_authorizer_output(authorizer_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAuthorizerResult]:
    """
    Creates an authorizer.
    """
    ...
