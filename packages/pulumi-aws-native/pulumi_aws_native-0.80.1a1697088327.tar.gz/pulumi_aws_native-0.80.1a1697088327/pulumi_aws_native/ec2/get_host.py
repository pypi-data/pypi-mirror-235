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
    'GetHostResult',
    'AwaitableGetHostResult',
    'get_host',
    'get_host_output',
]

@pulumi.output_type
class GetHostResult:
    def __init__(__self__, auto_placement=None, host_id=None, host_maintenance=None, host_recovery=None):
        if auto_placement and not isinstance(auto_placement, str):
            raise TypeError("Expected argument 'auto_placement' to be a str")
        pulumi.set(__self__, "auto_placement", auto_placement)
        if host_id and not isinstance(host_id, str):
            raise TypeError("Expected argument 'host_id' to be a str")
        pulumi.set(__self__, "host_id", host_id)
        if host_maintenance and not isinstance(host_maintenance, str):
            raise TypeError("Expected argument 'host_maintenance' to be a str")
        pulumi.set(__self__, "host_maintenance", host_maintenance)
        if host_recovery and not isinstance(host_recovery, str):
            raise TypeError("Expected argument 'host_recovery' to be a str")
        pulumi.set(__self__, "host_recovery", host_recovery)

    @property
    @pulumi.getter(name="autoPlacement")
    def auto_placement(self) -> Optional[str]:
        """
        Indicates whether the host accepts any untargeted instance launches that match its instance type configuration, or if it only accepts Host tenancy instance launches that specify its unique host ID.
        """
        return pulumi.get(self, "auto_placement")

    @property
    @pulumi.getter(name="hostId")
    def host_id(self) -> Optional[str]:
        """
        ID of the host created.
        """
        return pulumi.get(self, "host_id")

    @property
    @pulumi.getter(name="hostMaintenance")
    def host_maintenance(self) -> Optional[str]:
        """
        Automatically allocates a new dedicated host and moves your instances on to it if a degradation is detected on your current host.
        """
        return pulumi.get(self, "host_maintenance")

    @property
    @pulumi.getter(name="hostRecovery")
    def host_recovery(self) -> Optional[str]:
        """
        Indicates whether to enable or disable host recovery for the Dedicated Host. Host recovery is disabled by default.
        """
        return pulumi.get(self, "host_recovery")


class AwaitableGetHostResult(GetHostResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHostResult(
            auto_placement=self.auto_placement,
            host_id=self.host_id,
            host_maintenance=self.host_maintenance,
            host_recovery=self.host_recovery)


def get_host(host_id: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHostResult:
    """
    Resource Type definition for AWS::EC2::Host


    :param str host_id: ID of the host created.
    """
    __args__ = dict()
    __args__['hostId'] = host_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getHost', __args__, opts=opts, typ=GetHostResult).value

    return AwaitableGetHostResult(
        auto_placement=pulumi.get(__ret__, 'auto_placement'),
        host_id=pulumi.get(__ret__, 'host_id'),
        host_maintenance=pulumi.get(__ret__, 'host_maintenance'),
        host_recovery=pulumi.get(__ret__, 'host_recovery'))


@_utilities.lift_output_func(get_host)
def get_host_output(host_id: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetHostResult]:
    """
    Resource Type definition for AWS::EC2::Host


    :param str host_id: ID of the host created.
    """
    ...
