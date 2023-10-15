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
    'GetLogGroupResult',
    'AwaitableGetLogGroupResult',
    'get_log_group',
    'get_log_group_output',
]

@pulumi.output_type
class GetLogGroupResult:
    def __init__(__self__, arn=None, data_protection_policy=None, kms_key_id=None, retention_in_days=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if data_protection_policy and not isinstance(data_protection_policy, dict):
            raise TypeError("Expected argument 'data_protection_policy' to be a dict")
        pulumi.set(__self__, "data_protection_policy", data_protection_policy)
        if kms_key_id and not isinstance(kms_key_id, str):
            raise TypeError("Expected argument 'kms_key_id' to be a str")
        pulumi.set(__self__, "kms_key_id", kms_key_id)
        if retention_in_days and not isinstance(retention_in_days, int):
            raise TypeError("Expected argument 'retention_in_days' to be a int")
        pulumi.set(__self__, "retention_in_days", retention_in_days)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The CloudWatch log group ARN.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="dataProtectionPolicy")
    def data_protection_policy(self) -> Optional[Any]:
        """
        The body of the policy document you want to use for this topic.

        You can only add one policy per topic.

        The policy must be in JSON string format.

        Length Constraints: Maximum length of 30720
        """
        return pulumi.get(self, "data_protection_policy")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> Optional[int]:
        """
        The number of days to retain the log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1096, 1827, and 3653.
        """
        return pulumi.get(self, "retention_in_days")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.LogGroupTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetLogGroupResult(GetLogGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLogGroupResult(
            arn=self.arn,
            data_protection_policy=self.data_protection_policy,
            kms_key_id=self.kms_key_id,
            retention_in_days=self.retention_in_days,
            tags=self.tags)


def get_log_group(log_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLogGroupResult:
    """
    Resource schema for AWS::Logs::LogGroup


    :param str log_group_name: The name of the log group. If you don't specify a name, AWS CloudFormation generates a unique ID for the log group.
    """
    __args__ = dict()
    __args__['logGroupName'] = log_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:logs:getLogGroup', __args__, opts=opts, typ=GetLogGroupResult).value

    return AwaitableGetLogGroupResult(
        arn=pulumi.get(__ret__, 'arn'),
        data_protection_policy=pulumi.get(__ret__, 'data_protection_policy'),
        kms_key_id=pulumi.get(__ret__, 'kms_key_id'),
        retention_in_days=pulumi.get(__ret__, 'retention_in_days'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_log_group)
def get_log_group_output(log_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLogGroupResult]:
    """
    Resource schema for AWS::Logs::LogGroup


    :param str log_group_name: The name of the log group. If you don't specify a name, AWS CloudFormation generates a unique ID for the log group.
    """
    ...
