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
    'GetUrlResult',
    'AwaitableGetUrlResult',
    'get_url',
    'get_url_output',
]

@pulumi.output_type
class GetUrlResult:
    def __init__(__self__, auth_type=None, cors=None, function_arn=None, function_url=None, invoke_mode=None):
        if auth_type and not isinstance(auth_type, str):
            raise TypeError("Expected argument 'auth_type' to be a str")
        pulumi.set(__self__, "auth_type", auth_type)
        if cors and not isinstance(cors, dict):
            raise TypeError("Expected argument 'cors' to be a dict")
        pulumi.set(__self__, "cors", cors)
        if function_arn and not isinstance(function_arn, str):
            raise TypeError("Expected argument 'function_arn' to be a str")
        pulumi.set(__self__, "function_arn", function_arn)
        if function_url and not isinstance(function_url, str):
            raise TypeError("Expected argument 'function_url' to be a str")
        pulumi.set(__self__, "function_url", function_url)
        if invoke_mode and not isinstance(invoke_mode, str):
            raise TypeError("Expected argument 'invoke_mode' to be a str")
        pulumi.set(__self__, "invoke_mode", invoke_mode)

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional['UrlAuthType']:
        """
        Can be either AWS_IAM if the requests are authorized via IAM, or NONE if no authorization is configured on the Function URL.
        """
        return pulumi.get(self, "auth_type")

    @property
    @pulumi.getter
    def cors(self) -> Optional['outputs.UrlCors']:
        return pulumi.get(self, "cors")

    @property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> Optional[str]:
        """
        The full Amazon Resource Name (ARN) of the function associated with the Function URL.
        """
        return pulumi.get(self, "function_arn")

    @property
    @pulumi.getter(name="functionUrl")
    def function_url(self) -> Optional[str]:
        """
        The generated url for this resource.
        """
        return pulumi.get(self, "function_url")

    @property
    @pulumi.getter(name="invokeMode")
    def invoke_mode(self) -> Optional['UrlInvokeMode']:
        """
        The invocation mode for the function’s URL. Set to BUFFERED if you want to buffer responses before returning them to the client. Set to RESPONSE_STREAM if you want to stream responses, allowing faster time to first byte and larger response payload sizes. If not set, defaults to BUFFERED.
        """
        return pulumi.get(self, "invoke_mode")


class AwaitableGetUrlResult(GetUrlResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUrlResult(
            auth_type=self.auth_type,
            cors=self.cors,
            function_arn=self.function_arn,
            function_url=self.function_url,
            invoke_mode=self.invoke_mode)


def get_url(function_arn: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUrlResult:
    """
    Resource Type definition for AWS::Lambda::Url


    :param str function_arn: The full Amazon Resource Name (ARN) of the function associated with the Function URL.
    """
    __args__ = dict()
    __args__['functionArn'] = function_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:lambda:getUrl', __args__, opts=opts, typ=GetUrlResult).value

    return AwaitableGetUrlResult(
        auth_type=pulumi.get(__ret__, 'auth_type'),
        cors=pulumi.get(__ret__, 'cors'),
        function_arn=pulumi.get(__ret__, 'function_arn'),
        function_url=pulumi.get(__ret__, 'function_url'),
        invoke_mode=pulumi.get(__ret__, 'invoke_mode'))


@_utilities.lift_output_func(get_url)
def get_url_output(function_arn: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUrlResult]:
    """
    Resource Type definition for AWS::Lambda::Url


    :param str function_arn: The full Amazon Resource Name (ARN) of the function associated with the Function URL.
    """
    ...
