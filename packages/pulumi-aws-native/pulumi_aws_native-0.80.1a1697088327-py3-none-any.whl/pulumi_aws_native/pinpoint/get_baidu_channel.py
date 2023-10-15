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
    'GetBaiduChannelResult',
    'AwaitableGetBaiduChannelResult',
    'get_baidu_channel',
    'get_baidu_channel_output',
]

@pulumi.output_type
class GetBaiduChannelResult:
    def __init__(__self__, api_key=None, enabled=None, id=None, secret_key=None):
        if api_key and not isinstance(api_key, str):
            raise TypeError("Expected argument 'api_key' to be a str")
        pulumi.set(__self__, "api_key", api_key)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if secret_key and not isinstance(secret_key, str):
            raise TypeError("Expected argument 'secret_key' to be a str")
        pulumi.set(__self__, "secret_key", secret_key)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[str]:
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> Optional[str]:
        return pulumi.get(self, "secret_key")


class AwaitableGetBaiduChannelResult(GetBaiduChannelResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBaiduChannelResult(
            api_key=self.api_key,
            enabled=self.enabled,
            id=self.id,
            secret_key=self.secret_key)


def get_baidu_channel(id: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBaiduChannelResult:
    """
    Resource Type definition for AWS::Pinpoint::BaiduChannel
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:pinpoint:getBaiduChannel', __args__, opts=opts, typ=GetBaiduChannelResult).value

    return AwaitableGetBaiduChannelResult(
        api_key=pulumi.get(__ret__, 'api_key'),
        enabled=pulumi.get(__ret__, 'enabled'),
        id=pulumi.get(__ret__, 'id'),
        secret_key=pulumi.get(__ret__, 'secret_key'))


@_utilities.lift_output_func(get_baidu_channel)
def get_baidu_channel_output(id: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBaiduChannelResult]:
    """
    Resource Type definition for AWS::Pinpoint::BaiduChannel
    """
    ...
