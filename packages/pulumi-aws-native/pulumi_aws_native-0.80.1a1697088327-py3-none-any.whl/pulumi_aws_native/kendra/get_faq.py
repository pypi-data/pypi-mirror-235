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
    'GetFaqResult',
    'AwaitableGetFaqResult',
    'get_faq',
    'get_faq_output',
]

@pulumi.output_type
class GetFaqResult:
    def __init__(__self__, arn=None, id=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.FaqTag']]:
        """
        Tags for labeling the FAQ
        """
        return pulumi.get(self, "tags")


class AwaitableGetFaqResult(GetFaqResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFaqResult(
            arn=self.arn,
            id=self.id,
            tags=self.tags)


def get_faq(id: Optional[str] = None,
            index_id: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFaqResult:
    """
    A Kendra FAQ resource


    :param str index_id: Index ID
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['indexId'] = index_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:kendra:getFaq', __args__, opts=opts, typ=GetFaqResult).value

    return AwaitableGetFaqResult(
        arn=pulumi.get(__ret__, 'arn'),
        id=pulumi.get(__ret__, 'id'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_faq)
def get_faq_output(id: Optional[pulumi.Input[str]] = None,
                   index_id: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFaqResult]:
    """
    A Kendra FAQ resource


    :param str index_id: Index ID
    """
    ...
