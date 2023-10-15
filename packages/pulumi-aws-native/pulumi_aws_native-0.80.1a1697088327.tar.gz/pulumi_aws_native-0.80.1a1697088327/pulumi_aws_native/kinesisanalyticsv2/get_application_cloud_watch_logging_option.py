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
    'GetApplicationCloudWatchLoggingOptionResult',
    'AwaitableGetApplicationCloudWatchLoggingOptionResult',
    'get_application_cloud_watch_logging_option',
    'get_application_cloud_watch_logging_option_output',
]

@pulumi.output_type
class GetApplicationCloudWatchLoggingOptionResult:
    def __init__(__self__, cloud_watch_logging_option=None, id=None):
        if cloud_watch_logging_option and not isinstance(cloud_watch_logging_option, dict):
            raise TypeError("Expected argument 'cloud_watch_logging_option' to be a dict")
        pulumi.set(__self__, "cloud_watch_logging_option", cloud_watch_logging_option)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="cloudWatchLoggingOption")
    def cloud_watch_logging_option(self) -> Optional['outputs.ApplicationCloudWatchLoggingOptionCloudWatchLoggingOption']:
        return pulumi.get(self, "cloud_watch_logging_option")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetApplicationCloudWatchLoggingOptionResult(GetApplicationCloudWatchLoggingOptionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplicationCloudWatchLoggingOptionResult(
            cloud_watch_logging_option=self.cloud_watch_logging_option,
            id=self.id)


def get_application_cloud_watch_logging_option(id: Optional[str] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplicationCloudWatchLoggingOptionResult:
    """
    Resource Type definition for AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:kinesisanalyticsv2:getApplicationCloudWatchLoggingOption', __args__, opts=opts, typ=GetApplicationCloudWatchLoggingOptionResult).value

    return AwaitableGetApplicationCloudWatchLoggingOptionResult(
        cloud_watch_logging_option=pulumi.get(__ret__, 'cloud_watch_logging_option'),
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_application_cloud_watch_logging_option)
def get_application_cloud_watch_logging_option_output(id: Optional[pulumi.Input[str]] = None,
                                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApplicationCloudWatchLoggingOptionResult]:
    """
    Resource Type definition for AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption
    """
    ...
