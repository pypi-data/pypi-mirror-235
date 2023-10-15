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
    'GetInternetGatewayResult',
    'AwaitableGetInternetGatewayResult',
    'get_internet_gateway',
    'get_internet_gateway_output',
]

@pulumi.output_type
class GetInternetGatewayResult:
    def __init__(__self__, internet_gateway_id=None, tags=None):
        if internet_gateway_id and not isinstance(internet_gateway_id, str):
            raise TypeError("Expected argument 'internet_gateway_id' to be a str")
        pulumi.set(__self__, "internet_gateway_id", internet_gateway_id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="internetGatewayId")
    def internet_gateway_id(self) -> Optional[str]:
        """
        ID of internet gateway.
        """
        return pulumi.get(self, "internet_gateway_id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.InternetGatewayTag']]:
        """
        Any tags to assign to the internet gateway.
        """
        return pulumi.get(self, "tags")


class AwaitableGetInternetGatewayResult(GetInternetGatewayResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInternetGatewayResult(
            internet_gateway_id=self.internet_gateway_id,
            tags=self.tags)


def get_internet_gateway(internet_gateway_id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInternetGatewayResult:
    """
    Resource Type definition for AWS::EC2::InternetGateway


    :param str internet_gateway_id: ID of internet gateway.
    """
    __args__ = dict()
    __args__['internetGatewayId'] = internet_gateway_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getInternetGateway', __args__, opts=opts, typ=GetInternetGatewayResult).value

    return AwaitableGetInternetGatewayResult(
        internet_gateway_id=pulumi.get(__ret__, 'internet_gateway_id'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_internet_gateway)
def get_internet_gateway_output(internet_gateway_id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInternetGatewayResult]:
    """
    Resource Type definition for AWS::EC2::InternetGateway


    :param str internet_gateway_id: ID of internet gateway.
    """
    ...
