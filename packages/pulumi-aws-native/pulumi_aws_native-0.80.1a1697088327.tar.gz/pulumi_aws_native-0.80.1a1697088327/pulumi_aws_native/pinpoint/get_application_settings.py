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
    'GetApplicationSettingsResult',
    'AwaitableGetApplicationSettingsResult',
    'get_application_settings',
    'get_application_settings_output',
]

@pulumi.output_type
class GetApplicationSettingsResult:
    def __init__(__self__, campaign_hook=None, cloud_watch_metrics_enabled=None, id=None, limits=None, quiet_time=None):
        if campaign_hook and not isinstance(campaign_hook, dict):
            raise TypeError("Expected argument 'campaign_hook' to be a dict")
        pulumi.set(__self__, "campaign_hook", campaign_hook)
        if cloud_watch_metrics_enabled and not isinstance(cloud_watch_metrics_enabled, bool):
            raise TypeError("Expected argument 'cloud_watch_metrics_enabled' to be a bool")
        pulumi.set(__self__, "cloud_watch_metrics_enabled", cloud_watch_metrics_enabled)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if limits and not isinstance(limits, dict):
            raise TypeError("Expected argument 'limits' to be a dict")
        pulumi.set(__self__, "limits", limits)
        if quiet_time and not isinstance(quiet_time, dict):
            raise TypeError("Expected argument 'quiet_time' to be a dict")
        pulumi.set(__self__, "quiet_time", quiet_time)

    @property
    @pulumi.getter(name="campaignHook")
    def campaign_hook(self) -> Optional['outputs.ApplicationSettingsCampaignHook']:
        return pulumi.get(self, "campaign_hook")

    @property
    @pulumi.getter(name="cloudWatchMetricsEnabled")
    def cloud_watch_metrics_enabled(self) -> Optional[bool]:
        return pulumi.get(self, "cloud_watch_metrics_enabled")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def limits(self) -> Optional['outputs.ApplicationSettingsLimits']:
        return pulumi.get(self, "limits")

    @property
    @pulumi.getter(name="quietTime")
    def quiet_time(self) -> Optional['outputs.ApplicationSettingsQuietTime']:
        return pulumi.get(self, "quiet_time")


class AwaitableGetApplicationSettingsResult(GetApplicationSettingsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplicationSettingsResult(
            campaign_hook=self.campaign_hook,
            cloud_watch_metrics_enabled=self.cloud_watch_metrics_enabled,
            id=self.id,
            limits=self.limits,
            quiet_time=self.quiet_time)


def get_application_settings(id: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplicationSettingsResult:
    """
    Resource Type definition for AWS::Pinpoint::ApplicationSettings
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:pinpoint:getApplicationSettings', __args__, opts=opts, typ=GetApplicationSettingsResult).value

    return AwaitableGetApplicationSettingsResult(
        campaign_hook=pulumi.get(__ret__, 'campaign_hook'),
        cloud_watch_metrics_enabled=pulumi.get(__ret__, 'cloud_watch_metrics_enabled'),
        id=pulumi.get(__ret__, 'id'),
        limits=pulumi.get(__ret__, 'limits'),
        quiet_time=pulumi.get(__ret__, 'quiet_time'))


@_utilities.lift_output_func(get_application_settings)
def get_application_settings_output(id: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApplicationSettingsResult]:
    """
    Resource Type definition for AWS::Pinpoint::ApplicationSettings
    """
    ...
