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
    'GetReceiptRuleSetResult',
    'AwaitableGetReceiptRuleSetResult',
    'get_receipt_rule_set',
    'get_receipt_rule_set_output',
]

@pulumi.output_type
class GetReceiptRuleSetResult:
    def __init__(__self__, id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetReceiptRuleSetResult(GetReceiptRuleSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReceiptRuleSetResult(
            id=self.id)


def get_receipt_rule_set(id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReceiptRuleSetResult:
    """
    Resource Type definition for AWS::SES::ReceiptRuleSet
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ses:getReceiptRuleSet', __args__, opts=opts, typ=GetReceiptRuleSetResult).value

    return AwaitableGetReceiptRuleSetResult(
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_receipt_rule_set)
def get_receipt_rule_set_output(id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReceiptRuleSetResult]:
    """
    Resource Type definition for AWS::SES::ReceiptRuleSet
    """
    ...
