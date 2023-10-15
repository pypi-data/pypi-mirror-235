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
    'GetReceiptRuleResult',
    'AwaitableGetReceiptRuleResult',
    'get_receipt_rule',
    'get_receipt_rule_output',
]

@pulumi.output_type
class GetReceiptRuleResult:
    def __init__(__self__, after=None, id=None, rule=None):
        if after and not isinstance(after, str):
            raise TypeError("Expected argument 'after' to be a str")
        pulumi.set(__self__, "after", after)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if rule and not isinstance(rule, dict):
            raise TypeError("Expected argument 'rule' to be a dict")
        pulumi.set(__self__, "rule", rule)

    @property
    @pulumi.getter
    def after(self) -> Optional[str]:
        return pulumi.get(self, "after")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def rule(self) -> Optional['outputs.ReceiptRuleRule']:
        return pulumi.get(self, "rule")


class AwaitableGetReceiptRuleResult(GetReceiptRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReceiptRuleResult(
            after=self.after,
            id=self.id,
            rule=self.rule)


def get_receipt_rule(id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReceiptRuleResult:
    """
    Resource Type definition for AWS::SES::ReceiptRule
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ses:getReceiptRule', __args__, opts=opts, typ=GetReceiptRuleResult).value

    return AwaitableGetReceiptRuleResult(
        after=pulumi.get(__ret__, 'after'),
        id=pulumi.get(__ret__, 'id'),
        rule=pulumi.get(__ret__, 'rule'))


@_utilities.lift_output_func(get_receipt_rule)
def get_receipt_rule_output(id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReceiptRuleResult]:
    """
    Resource Type definition for AWS::SES::ReceiptRule
    """
    ...
