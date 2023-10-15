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
    'ScalableTargetActionArgs',
    'ScalableTargetScheduledActionArgs',
    'ScalableTargetSuspendedStateArgs',
    'ScalingPolicyCustomizedMetricSpecificationArgs',
    'ScalingPolicyMetricDimensionArgs',
    'ScalingPolicyPredefinedMetricSpecificationArgs',
    'ScalingPolicyStepAdjustmentArgs',
    'ScalingPolicyStepScalingPolicyConfigurationArgs',
    'ScalingPolicyTargetTrackingScalingPolicyConfigurationArgs',
]

@pulumi.input_type
class ScalableTargetActionArgs:
    def __init__(__self__, *,
                 max_capacity: Optional[pulumi.Input[int]] = None,
                 min_capacity: Optional[pulumi.Input[int]] = None):
        """
        specifies the minimum and maximum capacity
        """
        ScalableTargetActionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            max_capacity=max_capacity,
            min_capacity=min_capacity,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             max_capacity: Optional[pulumi.Input[int]] = None,
             min_capacity: Optional[pulumi.Input[int]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if max_capacity is not None:
            _setter("max_capacity", max_capacity)
        if min_capacity is not None:
            _setter("min_capacity", min_capacity)

    @property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "max_capacity")

    @max_capacity.setter
    def max_capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_capacity", value)

    @property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "min_capacity")

    @min_capacity.setter
    def min_capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_capacity", value)


@pulumi.input_type
class ScalableTargetScheduledActionArgs:
    def __init__(__self__, *,
                 schedule: pulumi.Input[str],
                 scheduled_action_name: pulumi.Input[str],
                 end_time: Optional[pulumi.Input[str]] = None,
                 scalable_target_action: Optional[pulumi.Input['ScalableTargetActionArgs']] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 timezone: Optional[pulumi.Input[str]] = None):
        """
        specifies a scheduled action for a scalable target
        """
        ScalableTargetScheduledActionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            schedule=schedule,
            scheduled_action_name=scheduled_action_name,
            end_time=end_time,
            scalable_target_action=scalable_target_action,
            start_time=start_time,
            timezone=timezone,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             schedule: pulumi.Input[str],
             scheduled_action_name: pulumi.Input[str],
             end_time: Optional[pulumi.Input[str]] = None,
             scalable_target_action: Optional[pulumi.Input['ScalableTargetActionArgs']] = None,
             start_time: Optional[pulumi.Input[str]] = None,
             timezone: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("schedule", schedule)
        _setter("scheduled_action_name", scheduled_action_name)
        if end_time is not None:
            _setter("end_time", end_time)
        if scalable_target_action is not None:
            _setter("scalable_target_action", scalable_target_action)
        if start_time is not None:
            _setter("start_time", start_time)
        if timezone is not None:
            _setter("timezone", timezone)

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Input[str]:
        return pulumi.get(self, "schedule")

    @schedule.setter
    def schedule(self, value: pulumi.Input[str]):
        pulumi.set(self, "schedule", value)

    @property
    @pulumi.getter(name="scheduledActionName")
    def scheduled_action_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "scheduled_action_name")

    @scheduled_action_name.setter
    def scheduled_action_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "scheduled_action_name", value)

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "end_time")

    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_time", value)

    @property
    @pulumi.getter(name="scalableTargetAction")
    def scalable_target_action(self) -> Optional[pulumi.Input['ScalableTargetActionArgs']]:
        return pulumi.get(self, "scalable_target_action")

    @scalable_target_action.setter
    def scalable_target_action(self, value: Optional[pulumi.Input['ScalableTargetActionArgs']]):
        pulumi.set(self, "scalable_target_action", value)

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "start_time")

    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_time", value)

    @property
    @pulumi.getter
    def timezone(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "timezone")

    @timezone.setter
    def timezone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "timezone", value)


@pulumi.input_type
class ScalableTargetSuspendedStateArgs:
    def __init__(__self__, *,
                 dynamic_scaling_in_suspended: Optional[pulumi.Input[bool]] = None,
                 dynamic_scaling_out_suspended: Optional[pulumi.Input[bool]] = None,
                 scheduled_scaling_suspended: Optional[pulumi.Input[bool]] = None):
        """
        specifies whether the scaling activities for a scalable target are in a suspended state
        """
        ScalableTargetSuspendedStateArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            dynamic_scaling_in_suspended=dynamic_scaling_in_suspended,
            dynamic_scaling_out_suspended=dynamic_scaling_out_suspended,
            scheduled_scaling_suspended=scheduled_scaling_suspended,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             dynamic_scaling_in_suspended: Optional[pulumi.Input[bool]] = None,
             dynamic_scaling_out_suspended: Optional[pulumi.Input[bool]] = None,
             scheduled_scaling_suspended: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if dynamic_scaling_in_suspended is not None:
            _setter("dynamic_scaling_in_suspended", dynamic_scaling_in_suspended)
        if dynamic_scaling_out_suspended is not None:
            _setter("dynamic_scaling_out_suspended", dynamic_scaling_out_suspended)
        if scheduled_scaling_suspended is not None:
            _setter("scheduled_scaling_suspended", scheduled_scaling_suspended)

    @property
    @pulumi.getter(name="dynamicScalingInSuspended")
    def dynamic_scaling_in_suspended(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "dynamic_scaling_in_suspended")

    @dynamic_scaling_in_suspended.setter
    def dynamic_scaling_in_suspended(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "dynamic_scaling_in_suspended", value)

    @property
    @pulumi.getter(name="dynamicScalingOutSuspended")
    def dynamic_scaling_out_suspended(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "dynamic_scaling_out_suspended")

    @dynamic_scaling_out_suspended.setter
    def dynamic_scaling_out_suspended(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "dynamic_scaling_out_suspended", value)

    @property
    @pulumi.getter(name="scheduledScalingSuspended")
    def scheduled_scaling_suspended(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "scheduled_scaling_suspended")

    @scheduled_scaling_suspended.setter
    def scheduled_scaling_suspended(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "scheduled_scaling_suspended", value)


@pulumi.input_type
class ScalingPolicyCustomizedMetricSpecificationArgs:
    def __init__(__self__, *,
                 metric_name: pulumi.Input[str],
                 namespace: pulumi.Input[str],
                 statistic: pulumi.Input[str],
                 dimensions: Optional[pulumi.Input[Sequence[pulumi.Input['ScalingPolicyMetricDimensionArgs']]]] = None,
                 unit: Optional[pulumi.Input[str]] = None):
        ScalingPolicyCustomizedMetricSpecificationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            metric_name=metric_name,
            namespace=namespace,
            statistic=statistic,
            dimensions=dimensions,
            unit=unit,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             metric_name: pulumi.Input[str],
             namespace: pulumi.Input[str],
             statistic: pulumi.Input[str],
             dimensions: Optional[pulumi.Input[Sequence[pulumi.Input['ScalingPolicyMetricDimensionArgs']]]] = None,
             unit: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("metric_name", metric_name)
        _setter("namespace", namespace)
        _setter("statistic", statistic)
        if dimensions is not None:
            _setter("dimensions", dimensions)
        if unit is not None:
            _setter("unit", unit)

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "metric_name")

    @metric_name.setter
    def metric_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "metric_name", value)

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[str]:
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter
    def statistic(self) -> pulumi.Input[str]:
        return pulumi.get(self, "statistic")

    @statistic.setter
    def statistic(self, value: pulumi.Input[str]):
        pulumi.set(self, "statistic", value)

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ScalingPolicyMetricDimensionArgs']]]]:
        return pulumi.get(self, "dimensions")

    @dimensions.setter
    def dimensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ScalingPolicyMetricDimensionArgs']]]]):
        pulumi.set(self, "dimensions", value)

    @property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "unit")

    @unit.setter
    def unit(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "unit", value)


@pulumi.input_type
class ScalingPolicyMetricDimensionArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 value: pulumi.Input[str]):
        ScalingPolicyMetricDimensionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: pulumi.Input[str],
             value: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("name", name)
        _setter("value", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ScalingPolicyPredefinedMetricSpecificationArgs:
    def __init__(__self__, *,
                 predefined_metric_type: pulumi.Input[str],
                 resource_label: Optional[pulumi.Input[str]] = None):
        ScalingPolicyPredefinedMetricSpecificationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            predefined_metric_type=predefined_metric_type,
            resource_label=resource_label,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             predefined_metric_type: pulumi.Input[str],
             resource_label: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("predefined_metric_type", predefined_metric_type)
        if resource_label is not None:
            _setter("resource_label", resource_label)

    @property
    @pulumi.getter(name="predefinedMetricType")
    def predefined_metric_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "predefined_metric_type")

    @predefined_metric_type.setter
    def predefined_metric_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "predefined_metric_type", value)

    @property
    @pulumi.getter(name="resourceLabel")
    def resource_label(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "resource_label")

    @resource_label.setter
    def resource_label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_label", value)


@pulumi.input_type
class ScalingPolicyStepAdjustmentArgs:
    def __init__(__self__, *,
                 scaling_adjustment: pulumi.Input[int],
                 metric_interval_lower_bound: Optional[pulumi.Input[float]] = None,
                 metric_interval_upper_bound: Optional[pulumi.Input[float]] = None):
        ScalingPolicyStepAdjustmentArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            scaling_adjustment=scaling_adjustment,
            metric_interval_lower_bound=metric_interval_lower_bound,
            metric_interval_upper_bound=metric_interval_upper_bound,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             scaling_adjustment: pulumi.Input[int],
             metric_interval_lower_bound: Optional[pulumi.Input[float]] = None,
             metric_interval_upper_bound: Optional[pulumi.Input[float]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("scaling_adjustment", scaling_adjustment)
        if metric_interval_lower_bound is not None:
            _setter("metric_interval_lower_bound", metric_interval_lower_bound)
        if metric_interval_upper_bound is not None:
            _setter("metric_interval_upper_bound", metric_interval_upper_bound)

    @property
    @pulumi.getter(name="scalingAdjustment")
    def scaling_adjustment(self) -> pulumi.Input[int]:
        return pulumi.get(self, "scaling_adjustment")

    @scaling_adjustment.setter
    def scaling_adjustment(self, value: pulumi.Input[int]):
        pulumi.set(self, "scaling_adjustment", value)

    @property
    @pulumi.getter(name="metricIntervalLowerBound")
    def metric_interval_lower_bound(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "metric_interval_lower_bound")

    @metric_interval_lower_bound.setter
    def metric_interval_lower_bound(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "metric_interval_lower_bound", value)

    @property
    @pulumi.getter(name="metricIntervalUpperBound")
    def metric_interval_upper_bound(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "metric_interval_upper_bound")

    @metric_interval_upper_bound.setter
    def metric_interval_upper_bound(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "metric_interval_upper_bound", value)


@pulumi.input_type
class ScalingPolicyStepScalingPolicyConfigurationArgs:
    def __init__(__self__, *,
                 adjustment_type: Optional[pulumi.Input[str]] = None,
                 cooldown: Optional[pulumi.Input[int]] = None,
                 metric_aggregation_type: Optional[pulumi.Input[str]] = None,
                 min_adjustment_magnitude: Optional[pulumi.Input[int]] = None,
                 step_adjustments: Optional[pulumi.Input[Sequence[pulumi.Input['ScalingPolicyStepAdjustmentArgs']]]] = None):
        ScalingPolicyStepScalingPolicyConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            adjustment_type=adjustment_type,
            cooldown=cooldown,
            metric_aggregation_type=metric_aggregation_type,
            min_adjustment_magnitude=min_adjustment_magnitude,
            step_adjustments=step_adjustments,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             adjustment_type: Optional[pulumi.Input[str]] = None,
             cooldown: Optional[pulumi.Input[int]] = None,
             metric_aggregation_type: Optional[pulumi.Input[str]] = None,
             min_adjustment_magnitude: Optional[pulumi.Input[int]] = None,
             step_adjustments: Optional[pulumi.Input[Sequence[pulumi.Input['ScalingPolicyStepAdjustmentArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if adjustment_type is not None:
            _setter("adjustment_type", adjustment_type)
        if cooldown is not None:
            _setter("cooldown", cooldown)
        if metric_aggregation_type is not None:
            _setter("metric_aggregation_type", metric_aggregation_type)
        if min_adjustment_magnitude is not None:
            _setter("min_adjustment_magnitude", min_adjustment_magnitude)
        if step_adjustments is not None:
            _setter("step_adjustments", step_adjustments)

    @property
    @pulumi.getter(name="adjustmentType")
    def adjustment_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "adjustment_type")

    @adjustment_type.setter
    def adjustment_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "adjustment_type", value)

    @property
    @pulumi.getter
    def cooldown(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "cooldown")

    @cooldown.setter
    def cooldown(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cooldown", value)

    @property
    @pulumi.getter(name="metricAggregationType")
    def metric_aggregation_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "metric_aggregation_type")

    @metric_aggregation_type.setter
    def metric_aggregation_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_aggregation_type", value)

    @property
    @pulumi.getter(name="minAdjustmentMagnitude")
    def min_adjustment_magnitude(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "min_adjustment_magnitude")

    @min_adjustment_magnitude.setter
    def min_adjustment_magnitude(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_adjustment_magnitude", value)

    @property
    @pulumi.getter(name="stepAdjustments")
    def step_adjustments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ScalingPolicyStepAdjustmentArgs']]]]:
        return pulumi.get(self, "step_adjustments")

    @step_adjustments.setter
    def step_adjustments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ScalingPolicyStepAdjustmentArgs']]]]):
        pulumi.set(self, "step_adjustments", value)


@pulumi.input_type
class ScalingPolicyTargetTrackingScalingPolicyConfigurationArgs:
    def __init__(__self__, *,
                 target_value: pulumi.Input[float],
                 customized_metric_specification: Optional[pulumi.Input['ScalingPolicyCustomizedMetricSpecificationArgs']] = None,
                 disable_scale_in: Optional[pulumi.Input[bool]] = None,
                 predefined_metric_specification: Optional[pulumi.Input['ScalingPolicyPredefinedMetricSpecificationArgs']] = None,
                 scale_in_cooldown: Optional[pulumi.Input[int]] = None,
                 scale_out_cooldown: Optional[pulumi.Input[int]] = None):
        ScalingPolicyTargetTrackingScalingPolicyConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            target_value=target_value,
            customized_metric_specification=customized_metric_specification,
            disable_scale_in=disable_scale_in,
            predefined_metric_specification=predefined_metric_specification,
            scale_in_cooldown=scale_in_cooldown,
            scale_out_cooldown=scale_out_cooldown,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             target_value: pulumi.Input[float],
             customized_metric_specification: Optional[pulumi.Input['ScalingPolicyCustomizedMetricSpecificationArgs']] = None,
             disable_scale_in: Optional[pulumi.Input[bool]] = None,
             predefined_metric_specification: Optional[pulumi.Input['ScalingPolicyPredefinedMetricSpecificationArgs']] = None,
             scale_in_cooldown: Optional[pulumi.Input[int]] = None,
             scale_out_cooldown: Optional[pulumi.Input[int]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("target_value", target_value)
        if customized_metric_specification is not None:
            _setter("customized_metric_specification", customized_metric_specification)
        if disable_scale_in is not None:
            _setter("disable_scale_in", disable_scale_in)
        if predefined_metric_specification is not None:
            _setter("predefined_metric_specification", predefined_metric_specification)
        if scale_in_cooldown is not None:
            _setter("scale_in_cooldown", scale_in_cooldown)
        if scale_out_cooldown is not None:
            _setter("scale_out_cooldown", scale_out_cooldown)

    @property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> pulumi.Input[float]:
        return pulumi.get(self, "target_value")

    @target_value.setter
    def target_value(self, value: pulumi.Input[float]):
        pulumi.set(self, "target_value", value)

    @property
    @pulumi.getter(name="customizedMetricSpecification")
    def customized_metric_specification(self) -> Optional[pulumi.Input['ScalingPolicyCustomizedMetricSpecificationArgs']]:
        return pulumi.get(self, "customized_metric_specification")

    @customized_metric_specification.setter
    def customized_metric_specification(self, value: Optional[pulumi.Input['ScalingPolicyCustomizedMetricSpecificationArgs']]):
        pulumi.set(self, "customized_metric_specification", value)

    @property
    @pulumi.getter(name="disableScaleIn")
    def disable_scale_in(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "disable_scale_in")

    @disable_scale_in.setter
    def disable_scale_in(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_scale_in", value)

    @property
    @pulumi.getter(name="predefinedMetricSpecification")
    def predefined_metric_specification(self) -> Optional[pulumi.Input['ScalingPolicyPredefinedMetricSpecificationArgs']]:
        return pulumi.get(self, "predefined_metric_specification")

    @predefined_metric_specification.setter
    def predefined_metric_specification(self, value: Optional[pulumi.Input['ScalingPolicyPredefinedMetricSpecificationArgs']]):
        pulumi.set(self, "predefined_metric_specification", value)

    @property
    @pulumi.getter(name="scaleInCooldown")
    def scale_in_cooldown(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "scale_in_cooldown")

    @scale_in_cooldown.setter
    def scale_in_cooldown(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "scale_in_cooldown", value)

    @property
    @pulumi.getter(name="scaleOutCooldown")
    def scale_out_cooldown(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "scale_out_cooldown")

    @scale_out_cooldown.setter
    def scale_out_cooldown(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "scale_out_cooldown", value)


