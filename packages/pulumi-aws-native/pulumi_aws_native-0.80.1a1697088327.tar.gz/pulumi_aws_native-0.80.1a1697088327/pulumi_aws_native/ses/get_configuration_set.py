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
    'GetConfigurationSetResult',
    'AwaitableGetConfigurationSetResult',
    'get_configuration_set',
    'get_configuration_set_output',
]

@pulumi.output_type
class GetConfigurationSetResult:
    def __init__(__self__, delivery_options=None, reputation_options=None, sending_options=None, suppression_options=None, tracking_options=None, vdm_options=None):
        if delivery_options and not isinstance(delivery_options, dict):
            raise TypeError("Expected argument 'delivery_options' to be a dict")
        pulumi.set(__self__, "delivery_options", delivery_options)
        if reputation_options and not isinstance(reputation_options, dict):
            raise TypeError("Expected argument 'reputation_options' to be a dict")
        pulumi.set(__self__, "reputation_options", reputation_options)
        if sending_options and not isinstance(sending_options, dict):
            raise TypeError("Expected argument 'sending_options' to be a dict")
        pulumi.set(__self__, "sending_options", sending_options)
        if suppression_options and not isinstance(suppression_options, dict):
            raise TypeError("Expected argument 'suppression_options' to be a dict")
        pulumi.set(__self__, "suppression_options", suppression_options)
        if tracking_options and not isinstance(tracking_options, dict):
            raise TypeError("Expected argument 'tracking_options' to be a dict")
        pulumi.set(__self__, "tracking_options", tracking_options)
        if vdm_options and not isinstance(vdm_options, dict):
            raise TypeError("Expected argument 'vdm_options' to be a dict")
        pulumi.set(__self__, "vdm_options", vdm_options)

    @property
    @pulumi.getter(name="deliveryOptions")
    def delivery_options(self) -> Optional['outputs.ConfigurationSetDeliveryOptions']:
        return pulumi.get(self, "delivery_options")

    @property
    @pulumi.getter(name="reputationOptions")
    def reputation_options(self) -> Optional['outputs.ConfigurationSetReputationOptions']:
        return pulumi.get(self, "reputation_options")

    @property
    @pulumi.getter(name="sendingOptions")
    def sending_options(self) -> Optional['outputs.ConfigurationSetSendingOptions']:
        return pulumi.get(self, "sending_options")

    @property
    @pulumi.getter(name="suppressionOptions")
    def suppression_options(self) -> Optional['outputs.ConfigurationSetSuppressionOptions']:
        return pulumi.get(self, "suppression_options")

    @property
    @pulumi.getter(name="trackingOptions")
    def tracking_options(self) -> Optional['outputs.ConfigurationSetTrackingOptions']:
        return pulumi.get(self, "tracking_options")

    @property
    @pulumi.getter(name="vdmOptions")
    def vdm_options(self) -> Optional['outputs.ConfigurationSetVdmOptions']:
        return pulumi.get(self, "vdm_options")


class AwaitableGetConfigurationSetResult(GetConfigurationSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConfigurationSetResult(
            delivery_options=self.delivery_options,
            reputation_options=self.reputation_options,
            sending_options=self.sending_options,
            suppression_options=self.suppression_options,
            tracking_options=self.tracking_options,
            vdm_options=self.vdm_options)


def get_configuration_set(name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConfigurationSetResult:
    """
    Resource schema for AWS::SES::ConfigurationSet.


    :param str name: The name of the configuration set.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ses:getConfigurationSet', __args__, opts=opts, typ=GetConfigurationSetResult).value

    return AwaitableGetConfigurationSetResult(
        delivery_options=pulumi.get(__ret__, 'delivery_options'),
        reputation_options=pulumi.get(__ret__, 'reputation_options'),
        sending_options=pulumi.get(__ret__, 'sending_options'),
        suppression_options=pulumi.get(__ret__, 'suppression_options'),
        tracking_options=pulumi.get(__ret__, 'tracking_options'),
        vdm_options=pulumi.get(__ret__, 'vdm_options'))


@_utilities.lift_output_func(get_configuration_set)
def get_configuration_set_output(name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConfigurationSetResult]:
    """
    Resource schema for AWS::SES::ConfigurationSet.


    :param str name: The name of the configuration set.
    """
    ...
