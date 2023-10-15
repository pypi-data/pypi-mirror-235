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
    'GetOriginAccessControlResult',
    'AwaitableGetOriginAccessControlResult',
    'get_origin_access_control',
    'get_origin_access_control_output',
]

@pulumi.output_type
class GetOriginAccessControlResult:
    def __init__(__self__, id=None, origin_access_control_config=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if origin_access_control_config and not isinstance(origin_access_control_config, dict):
            raise TypeError("Expected argument 'origin_access_control_config' to be a dict")
        pulumi.set(__self__, "origin_access_control_config", origin_access_control_config)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="originAccessControlConfig")
    def origin_access_control_config(self) -> Optional['outputs.OriginAccessControlConfig']:
        return pulumi.get(self, "origin_access_control_config")


class AwaitableGetOriginAccessControlResult(GetOriginAccessControlResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOriginAccessControlResult(
            id=self.id,
            origin_access_control_config=self.origin_access_control_config)


def get_origin_access_control(id: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOriginAccessControlResult:
    """
    Resource Type definition for AWS::CloudFront::OriginAccessControl
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:cloudfront:getOriginAccessControl', __args__, opts=opts, typ=GetOriginAccessControlResult).value

    return AwaitableGetOriginAccessControlResult(
        id=pulumi.get(__ret__, 'id'),
        origin_access_control_config=pulumi.get(__ret__, 'origin_access_control_config'))


@_utilities.lift_output_func(get_origin_access_control)
def get_origin_access_control_output(id: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOriginAccessControlResult]:
    """
    Resource Type definition for AWS::CloudFront::OriginAccessControl
    """
    ...
