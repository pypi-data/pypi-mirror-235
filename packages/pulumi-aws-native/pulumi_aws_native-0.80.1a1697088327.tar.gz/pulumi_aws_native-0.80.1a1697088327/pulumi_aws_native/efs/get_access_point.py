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
    'GetAccessPointResult',
    'AwaitableGetAccessPointResult',
    'get_access_point',
    'get_access_point_output',
]

@pulumi.output_type
class GetAccessPointResult:
    def __init__(__self__, access_point_id=None, access_point_tags=None, arn=None):
        if access_point_id and not isinstance(access_point_id, str):
            raise TypeError("Expected argument 'access_point_id' to be a str")
        pulumi.set(__self__, "access_point_id", access_point_id)
        if access_point_tags and not isinstance(access_point_tags, list):
            raise TypeError("Expected argument 'access_point_tags' to be a list")
        pulumi.set(__self__, "access_point_tags", access_point_tags)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)

    @property
    @pulumi.getter(name="accessPointId")
    def access_point_id(self) -> Optional[str]:
        return pulumi.get(self, "access_point_id")

    @property
    @pulumi.getter(name="accessPointTags")
    def access_point_tags(self) -> Optional[Sequence['outputs.AccessPointTag']]:
        return pulumi.get(self, "access_point_tags")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")


class AwaitableGetAccessPointResult(GetAccessPointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccessPointResult(
            access_point_id=self.access_point_id,
            access_point_tags=self.access_point_tags,
            arn=self.arn)


def get_access_point(access_point_id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccessPointResult:
    """
    Resource Type definition for AWS::EFS::AccessPoint
    """
    __args__ = dict()
    __args__['accessPointId'] = access_point_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:efs:getAccessPoint', __args__, opts=opts, typ=GetAccessPointResult).value

    return AwaitableGetAccessPointResult(
        access_point_id=pulumi.get(__ret__, 'access_point_id'),
        access_point_tags=pulumi.get(__ret__, 'access_point_tags'),
        arn=pulumi.get(__ret__, 'arn'))


@_utilities.lift_output_func(get_access_point)
def get_access_point_output(access_point_id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccessPointResult]:
    """
    Resource Type definition for AWS::EFS::AccessPoint
    """
    ...
