# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetApiKeyResult',
    'AwaitableGetApiKeyResult',
    'get_api_key',
    'get_api_key_output',
]

@pulumi.output_type
class GetApiKeyResult:
    def __init__(__self__, api_key=None, api_key_id=None, arn=None, description=None, expires=None):
        if api_key and not isinstance(api_key, str):
            raise TypeError("Expected argument 'api_key' to be a str")
        pulumi.set(__self__, "api_key", api_key)
        if api_key_id and not isinstance(api_key_id, str):
            raise TypeError("Expected argument 'api_key_id' to be a str")
        pulumi.set(__self__, "api_key_id", api_key_id)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if expires and not isinstance(expires, float):
            raise TypeError("Expected argument 'expires' to be a float")
        pulumi.set(__self__, "expires", expires)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[str]:
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter(name="apiKeyId")
    def api_key_id(self) -> Optional[str]:
        return pulumi.get(self, "api_key_id")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def expires(self) -> Optional[float]:
        return pulumi.get(self, "expires")


class AwaitableGetApiKeyResult(GetApiKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApiKeyResult(
            api_key=self.api_key,
            api_key_id=self.api_key_id,
            arn=self.arn,
            description=self.description,
            expires=self.expires)


def get_api_key(api_key_id: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApiKeyResult:
    """
    Resource Type definition for AWS::AppSync::ApiKey
    """
    __args__ = dict()
    __args__['apiKeyId'] = api_key_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:appsync:getApiKey', __args__, opts=opts, typ=GetApiKeyResult).value

    return AwaitableGetApiKeyResult(
        api_key=pulumi.get(__ret__, 'api_key'),
        api_key_id=pulumi.get(__ret__, 'api_key_id'),
        arn=pulumi.get(__ret__, 'arn'),
        description=pulumi.get(__ret__, 'description'),
        expires=pulumi.get(__ret__, 'expires'))


@_utilities.lift_output_func(get_api_key)
def get_api_key_output(api_key_id: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApiKeyResult]:
    """
    Resource Type definition for AWS::AppSync::ApiKey
    """
    ...
