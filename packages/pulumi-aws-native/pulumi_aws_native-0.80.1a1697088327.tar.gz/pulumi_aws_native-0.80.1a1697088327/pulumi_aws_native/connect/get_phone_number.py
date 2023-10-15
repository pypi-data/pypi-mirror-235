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
    'GetPhoneNumberResult',
    'AwaitableGetPhoneNumberResult',
    'get_phone_number',
    'get_phone_number_output',
]

@pulumi.output_type
class GetPhoneNumberResult:
    def __init__(__self__, address=None, phone_number_arn=None, tags=None, target_arn=None):
        if address and not isinstance(address, str):
            raise TypeError("Expected argument 'address' to be a str")
        pulumi.set(__self__, "address", address)
        if phone_number_arn and not isinstance(phone_number_arn, str):
            raise TypeError("Expected argument 'phone_number_arn' to be a str")
        pulumi.set(__self__, "phone_number_arn", phone_number_arn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if target_arn and not isinstance(target_arn, str):
            raise TypeError("Expected argument 'target_arn' to be a str")
        pulumi.set(__self__, "target_arn", target_arn)

    @property
    @pulumi.getter
    def address(self) -> Optional[str]:
        """
        The phone number e164 address.
        """
        return pulumi.get(self, "address")

    @property
    @pulumi.getter(name="phoneNumberArn")
    def phone_number_arn(self) -> Optional[str]:
        """
        The phone number ARN
        """
        return pulumi.get(self, "phone_number_arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.PhoneNumberTag']]:
        """
        One or more tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> Optional[str]:
        """
        The ARN of the target the phone number is claimed to.
        """
        return pulumi.get(self, "target_arn")


class AwaitableGetPhoneNumberResult(GetPhoneNumberResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPhoneNumberResult(
            address=self.address,
            phone_number_arn=self.phone_number_arn,
            tags=self.tags,
            target_arn=self.target_arn)


def get_phone_number(phone_number_arn: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPhoneNumberResult:
    """
    Resource Type definition for AWS::Connect::PhoneNumber


    :param str phone_number_arn: The phone number ARN
    """
    __args__ = dict()
    __args__['phoneNumberArn'] = phone_number_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:connect:getPhoneNumber', __args__, opts=opts, typ=GetPhoneNumberResult).value

    return AwaitableGetPhoneNumberResult(
        address=pulumi.get(__ret__, 'address'),
        phone_number_arn=pulumi.get(__ret__, 'phone_number_arn'),
        tags=pulumi.get(__ret__, 'tags'),
        target_arn=pulumi.get(__ret__, 'target_arn'))


@_utilities.lift_output_func(get_phone_number)
def get_phone_number_output(phone_number_arn: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPhoneNumberResult]:
    """
    Resource Type definition for AWS::Connect::PhoneNumber


    :param str phone_number_arn: The phone number ARN
    """
    ...
