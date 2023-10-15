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
    'GetScalableTargetResult',
    'AwaitableGetScalableTargetResult',
    'get_scalable_target',
    'get_scalable_target_output',
]

@pulumi.output_type
class GetScalableTargetResult:
    def __init__(__self__, id=None, max_capacity=None, min_capacity=None, scheduled_actions=None, suspended_state=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if max_capacity and not isinstance(max_capacity, int):
            raise TypeError("Expected argument 'max_capacity' to be a int")
        pulumi.set(__self__, "max_capacity", max_capacity)
        if min_capacity and not isinstance(min_capacity, int):
            raise TypeError("Expected argument 'min_capacity' to be a int")
        pulumi.set(__self__, "min_capacity", min_capacity)
        if scheduled_actions and not isinstance(scheduled_actions, list):
            raise TypeError("Expected argument 'scheduled_actions' to be a list")
        pulumi.set(__self__, "scheduled_actions", scheduled_actions)
        if suspended_state and not isinstance(suspended_state, dict):
            raise TypeError("Expected argument 'suspended_state' to be a dict")
        pulumi.set(__self__, "suspended_state", suspended_state)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        This value can be returned by using the Ref function. Ref returns the Cloudformation generated ID of the resource in format - ResourceId|ScalableDimension|ServiceNamespace
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[int]:
        """
        The maximum value that you plan to scale in to. When a scaling policy is in effect, Application Auto Scaling can scale in (contract) as needed to the minimum capacity limit in response to changing demand
        """
        return pulumi.get(self, "max_capacity")

    @property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> Optional[int]:
        """
        The minimum value that you plan to scale in to. When a scaling policy is in effect, Application Auto Scaling can scale in (contract) as needed to the minimum capacity limit in response to changing demand
        """
        return pulumi.get(self, "min_capacity")

    @property
    @pulumi.getter(name="scheduledActions")
    def scheduled_actions(self) -> Optional[Sequence['outputs.ScalableTargetScheduledAction']]:
        """
        The scheduled actions for the scalable target. Duplicates aren't allowed.
        """
        return pulumi.get(self, "scheduled_actions")

    @property
    @pulumi.getter(name="suspendedState")
    def suspended_state(self) -> Optional['outputs.ScalableTargetSuspendedState']:
        """
        An embedded object that contains attributes and attribute values that are used to suspend and resume automatic scaling. Setting the value of an attribute to true suspends the specified scaling activities. Setting it to false (default) resumes the specified scaling activities.
        """
        return pulumi.get(self, "suspended_state")


class AwaitableGetScalableTargetResult(GetScalableTargetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScalableTargetResult(
            id=self.id,
            max_capacity=self.max_capacity,
            min_capacity=self.min_capacity,
            scheduled_actions=self.scheduled_actions,
            suspended_state=self.suspended_state)


def get_scalable_target(resource_id: Optional[str] = None,
                        scalable_dimension: Optional[str] = None,
                        service_namespace: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScalableTargetResult:
    """
    Resource Type definition for AWS::ApplicationAutoScaling::ScalableTarget


    :param str resource_id: The identifier of the resource associated with the scalable target
    :param str scalable_dimension: The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property
    :param str service_namespace: The namespace of the AWS service that provides the resource, or a custom-resource
    """
    __args__ = dict()
    __args__['resourceId'] = resource_id
    __args__['scalableDimension'] = scalable_dimension
    __args__['serviceNamespace'] = service_namespace
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:applicationautoscaling:getScalableTarget', __args__, opts=opts, typ=GetScalableTargetResult).value

    return AwaitableGetScalableTargetResult(
        id=pulumi.get(__ret__, 'id'),
        max_capacity=pulumi.get(__ret__, 'max_capacity'),
        min_capacity=pulumi.get(__ret__, 'min_capacity'),
        scheduled_actions=pulumi.get(__ret__, 'scheduled_actions'),
        suspended_state=pulumi.get(__ret__, 'suspended_state'))


@_utilities.lift_output_func(get_scalable_target)
def get_scalable_target_output(resource_id: Optional[pulumi.Input[str]] = None,
                               scalable_dimension: Optional[pulumi.Input[str]] = None,
                               service_namespace: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetScalableTargetResult]:
    """
    Resource Type definition for AWS::ApplicationAutoScaling::ScalableTarget


    :param str resource_id: The identifier of the resource associated with the scalable target
    :param str scalable_dimension: The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property
    :param str service_namespace: The namespace of the AWS service that provides the resource, or a custom-resource
    """
    ...
