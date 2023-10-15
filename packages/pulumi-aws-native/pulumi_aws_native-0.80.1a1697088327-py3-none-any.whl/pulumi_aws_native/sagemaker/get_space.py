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
    'GetSpaceResult',
    'AwaitableGetSpaceResult',
    'get_space',
    'get_space_output',
]

@pulumi.output_type
class GetSpaceResult:
    def __init__(__self__, space_arn=None):
        if space_arn and not isinstance(space_arn, str):
            raise TypeError("Expected argument 'space_arn' to be a str")
        pulumi.set(__self__, "space_arn", space_arn)

    @property
    @pulumi.getter(name="spaceArn")
    def space_arn(self) -> Optional[str]:
        """
        The space Amazon Resource Name (ARN).
        """
        return pulumi.get(self, "space_arn")


class AwaitableGetSpaceResult(GetSpaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSpaceResult(
            space_arn=self.space_arn)


def get_space(domain_id: Optional[str] = None,
              space_name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSpaceResult:
    """
    Resource Type definition for AWS::SageMaker::Space


    :param str domain_id: The ID of the associated Domain.
    :param str space_name: A name for the Space.
    """
    __args__ = dict()
    __args__['domainId'] = domain_id
    __args__['spaceName'] = space_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:sagemaker:getSpace', __args__, opts=opts, typ=GetSpaceResult).value

    return AwaitableGetSpaceResult(
        space_arn=pulumi.get(__ret__, 'space_arn'))


@_utilities.lift_output_func(get_space)
def get_space_output(domain_id: Optional[pulumi.Input[str]] = None,
                     space_name: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSpaceResult]:
    """
    Resource Type definition for AWS::SageMaker::Space


    :param str domain_id: The ID of the associated Domain.
    :param str space_name: A name for the Space.
    """
    ...
