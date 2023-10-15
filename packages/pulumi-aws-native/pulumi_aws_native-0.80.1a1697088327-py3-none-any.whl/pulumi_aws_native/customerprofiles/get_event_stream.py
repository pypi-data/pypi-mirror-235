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
from ._enums import *

__all__ = [
    'GetEventStreamResult',
    'AwaitableGetEventStreamResult',
    'get_event_stream',
    'get_event_stream_output',
]

@pulumi.output_type
class GetEventStreamResult:
    def __init__(__self__, created_at=None, destination_details=None, event_stream_arn=None, state=None, tags=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if destination_details and not isinstance(destination_details, dict):
            raise TypeError("Expected argument 'destination_details' to be a dict")
        pulumi.set(__self__, "destination_details", destination_details)
        if event_stream_arn and not isinstance(event_stream_arn, str):
            raise TypeError("Expected argument 'event_stream_arn' to be a str")
        pulumi.set(__self__, "event_stream_arn", event_stream_arn)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of when the export was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="destinationDetails")
    def destination_details(self) -> Optional['outputs.DestinationDetailsProperties']:
        """
        Details regarding the Kinesis stream.
        """
        return pulumi.get(self, "destination_details")

    @property
    @pulumi.getter(name="eventStreamArn")
    def event_stream_arn(self) -> Optional[str]:
        """
        A unique identifier for the event stream.
        """
        return pulumi.get(self, "event_stream_arn")

    @property
    @pulumi.getter
    def state(self) -> Optional['EventStreamState']:
        """
        The operational state of destination stream for export.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.EventStreamTag']]:
        """
        The tags used to organize, track, or control access for this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetEventStreamResult(GetEventStreamResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEventStreamResult(
            created_at=self.created_at,
            destination_details=self.destination_details,
            event_stream_arn=self.event_stream_arn,
            state=self.state,
            tags=self.tags)


def get_event_stream(domain_name: Optional[str] = None,
                     event_stream_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEventStreamResult:
    """
    An Event Stream resource of Amazon Connect Customer Profiles


    :param str domain_name: The unique name of the domain.
    :param str event_stream_name: The name of the event stream.
    """
    __args__ = dict()
    __args__['domainName'] = domain_name
    __args__['eventStreamName'] = event_stream_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:customerprofiles:getEventStream', __args__, opts=opts, typ=GetEventStreamResult).value

    return AwaitableGetEventStreamResult(
        created_at=pulumi.get(__ret__, 'created_at'),
        destination_details=pulumi.get(__ret__, 'destination_details'),
        event_stream_arn=pulumi.get(__ret__, 'event_stream_arn'),
        state=pulumi.get(__ret__, 'state'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_event_stream)
def get_event_stream_output(domain_name: Optional[pulumi.Input[str]] = None,
                            event_stream_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEventStreamResult]:
    """
    An Event Stream resource of Amazon Connect Customer Profiles


    :param str domain_name: The unique name of the domain.
    :param str event_stream_name: The name of the event stream.
    """
    ...
