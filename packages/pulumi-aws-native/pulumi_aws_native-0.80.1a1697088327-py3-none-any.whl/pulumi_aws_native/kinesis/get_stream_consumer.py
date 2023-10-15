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
    'GetStreamConsumerResult',
    'AwaitableGetStreamConsumerResult',
    'get_stream_consumer',
    'get_stream_consumer_output',
]

@pulumi.output_type
class GetStreamConsumerResult:
    def __init__(__self__, consumer_arn=None, consumer_creation_timestamp=None, consumer_status=None, id=None):
        if consumer_arn and not isinstance(consumer_arn, str):
            raise TypeError("Expected argument 'consumer_arn' to be a str")
        pulumi.set(__self__, "consumer_arn", consumer_arn)
        if consumer_creation_timestamp and not isinstance(consumer_creation_timestamp, str):
            raise TypeError("Expected argument 'consumer_creation_timestamp' to be a str")
        pulumi.set(__self__, "consumer_creation_timestamp", consumer_creation_timestamp)
        if consumer_status and not isinstance(consumer_status, str):
            raise TypeError("Expected argument 'consumer_status' to be a str")
        pulumi.set(__self__, "consumer_status", consumer_status)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="consumerArn")
    def consumer_arn(self) -> Optional[str]:
        return pulumi.get(self, "consumer_arn")

    @property
    @pulumi.getter(name="consumerCreationTimestamp")
    def consumer_creation_timestamp(self) -> Optional[str]:
        return pulumi.get(self, "consumer_creation_timestamp")

    @property
    @pulumi.getter(name="consumerStatus")
    def consumer_status(self) -> Optional[str]:
        return pulumi.get(self, "consumer_status")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetStreamConsumerResult(GetStreamConsumerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStreamConsumerResult(
            consumer_arn=self.consumer_arn,
            consumer_creation_timestamp=self.consumer_creation_timestamp,
            consumer_status=self.consumer_status,
            id=self.id)


def get_stream_consumer(id: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStreamConsumerResult:
    """
    Resource Type definition for AWS::Kinesis::StreamConsumer
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:kinesis:getStreamConsumer', __args__, opts=opts, typ=GetStreamConsumerResult).value

    return AwaitableGetStreamConsumerResult(
        consumer_arn=pulumi.get(__ret__, 'consumer_arn'),
        consumer_creation_timestamp=pulumi.get(__ret__, 'consumer_creation_timestamp'),
        consumer_status=pulumi.get(__ret__, 'consumer_status'),
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_stream_consumer)
def get_stream_consumer_output(id: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStreamConsumerResult]:
    """
    Resource Type definition for AWS::Kinesis::StreamConsumer
    """
    ...
