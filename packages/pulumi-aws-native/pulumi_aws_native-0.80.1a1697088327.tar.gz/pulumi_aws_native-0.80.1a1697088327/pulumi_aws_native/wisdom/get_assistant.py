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
    'GetAssistantResult',
    'AwaitableGetAssistantResult',
    'get_assistant',
    'get_assistant_output',
]

@pulumi.output_type
class GetAssistantResult:
    def __init__(__self__, assistant_arn=None, assistant_id=None):
        if assistant_arn and not isinstance(assistant_arn, str):
            raise TypeError("Expected argument 'assistant_arn' to be a str")
        pulumi.set(__self__, "assistant_arn", assistant_arn)
        if assistant_id and not isinstance(assistant_id, str):
            raise TypeError("Expected argument 'assistant_id' to be a str")
        pulumi.set(__self__, "assistant_id", assistant_id)

    @property
    @pulumi.getter(name="assistantArn")
    def assistant_arn(self) -> Optional[str]:
        return pulumi.get(self, "assistant_arn")

    @property
    @pulumi.getter(name="assistantId")
    def assistant_id(self) -> Optional[str]:
        return pulumi.get(self, "assistant_id")


class AwaitableGetAssistantResult(GetAssistantResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAssistantResult(
            assistant_arn=self.assistant_arn,
            assistant_id=self.assistant_id)


def get_assistant(assistant_id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAssistantResult:
    """
    Definition of AWS::Wisdom::Assistant Resource Type
    """
    __args__ = dict()
    __args__['assistantId'] = assistant_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:wisdom:getAssistant', __args__, opts=opts, typ=GetAssistantResult).value

    return AwaitableGetAssistantResult(
        assistant_arn=pulumi.get(__ret__, 'assistant_arn'),
        assistant_id=pulumi.get(__ret__, 'assistant_id'))


@_utilities.lift_output_func(get_assistant)
def get_assistant_output(assistant_id: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAssistantResult]:
    """
    Definition of AWS::Wisdom::Assistant Resource Type
    """
    ...
