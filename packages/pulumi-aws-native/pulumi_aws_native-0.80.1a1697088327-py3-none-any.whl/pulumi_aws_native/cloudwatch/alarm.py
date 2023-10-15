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
from ._inputs import *

__all__ = ['AlarmArgs', 'Alarm']

@pulumi.input_type
class AlarmArgs:
    def __init__(__self__, *,
                 comparison_operator: pulumi.Input[str],
                 evaluation_periods: pulumi.Input[int],
                 actions_enabled: Optional[pulumi.Input[bool]] = None,
                 alarm_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 alarm_description: Optional[pulumi.Input[str]] = None,
                 alarm_name: Optional[pulumi.Input[str]] = None,
                 datapoints_to_alarm: Optional[pulumi.Input[int]] = None,
                 dimensions: Optional[pulumi.Input[Sequence[pulumi.Input['AlarmDimensionArgs']]]] = None,
                 evaluate_low_sample_count_percentile: Optional[pulumi.Input[str]] = None,
                 extended_statistic: Optional[pulumi.Input[str]] = None,
                 insufficient_data_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 metric_name: Optional[pulumi.Input[str]] = None,
                 metrics: Optional[pulumi.Input[Sequence[pulumi.Input['AlarmMetricDataQueryArgs']]]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 ok_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 period: Optional[pulumi.Input[int]] = None,
                 statistic: Optional[pulumi.Input[str]] = None,
                 threshold: Optional[pulumi.Input[float]] = None,
                 threshold_metric_id: Optional[pulumi.Input[str]] = None,
                 treat_missing_data: Optional[pulumi.Input[str]] = None,
                 unit: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Alarm resource.
        :param pulumi.Input[str] comparison_operator: The arithmetic operation to use when comparing the specified statistic and threshold.
        :param pulumi.Input[int] evaluation_periods: The number of periods over which data is compared to the specified threshold.
        :param pulumi.Input[bool] actions_enabled: Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] alarm_actions: The list of actions to execute when this alarm transitions into an ALARM state from any other state.
        :param pulumi.Input[str] alarm_description: The description of the alarm.
        :param pulumi.Input[str] alarm_name: The name of the alarm.
        :param pulumi.Input[int] datapoints_to_alarm: The number of datapoints that must be breaching to trigger the alarm.
        :param pulumi.Input[Sequence[pulumi.Input['AlarmDimensionArgs']]] dimensions: The dimensions for the metric associated with the alarm. For an alarm based on a math expression, you can't specify Dimensions. Instead, you use Metrics.
        :param pulumi.Input[str] evaluate_low_sample_count_percentile: Used only for alarms based on percentiles.
        :param pulumi.Input[str] extended_statistic: The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] insufficient_data_actions: The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state.
        :param pulumi.Input[str] metric_name: The name of the metric associated with the alarm.
        :param pulumi.Input[Sequence[pulumi.Input['AlarmMetricDataQueryArgs']]] metrics: An array that enables you to create an alarm based on the result of a metric math expression.
        :param pulumi.Input[str] namespace: The namespace of the metric associated with the alarm.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ok_actions: The actions to execute when this alarm transitions to the OK state from any other state.
        :param pulumi.Input[int] period: The period in seconds, over which the statistic is applied.
        :param pulumi.Input[str] statistic: The statistic for the metric associated with the alarm, other than percentile.
        :param pulumi.Input[float] threshold: In an alarm based on an anomaly detection model, this is the ID of the ANOMALY_DETECTION_BAND function used as the threshold for the alarm.
        :param pulumi.Input[str] threshold_metric_id: In an alarm based on an anomaly detection model, this is the ID of the ANOMALY_DETECTION_BAND function used as the threshold for the alarm.
        :param pulumi.Input[str] treat_missing_data: Sets how this alarm is to handle missing data points. Valid values are breaching, notBreaching, ignore, and missing.
        :param pulumi.Input[str] unit: The unit of the metric associated with the alarm.
        """
        AlarmArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            comparison_operator=comparison_operator,
            evaluation_periods=evaluation_periods,
            actions_enabled=actions_enabled,
            alarm_actions=alarm_actions,
            alarm_description=alarm_description,
            alarm_name=alarm_name,
            datapoints_to_alarm=datapoints_to_alarm,
            dimensions=dimensions,
            evaluate_low_sample_count_percentile=evaluate_low_sample_count_percentile,
            extended_statistic=extended_statistic,
            insufficient_data_actions=insufficient_data_actions,
            metric_name=metric_name,
            metrics=metrics,
            namespace=namespace,
            ok_actions=ok_actions,
            period=period,
            statistic=statistic,
            threshold=threshold,
            threshold_metric_id=threshold_metric_id,
            treat_missing_data=treat_missing_data,
            unit=unit,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             comparison_operator: pulumi.Input[str],
             evaluation_periods: pulumi.Input[int],
             actions_enabled: Optional[pulumi.Input[bool]] = None,
             alarm_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             alarm_description: Optional[pulumi.Input[str]] = None,
             alarm_name: Optional[pulumi.Input[str]] = None,
             datapoints_to_alarm: Optional[pulumi.Input[int]] = None,
             dimensions: Optional[pulumi.Input[Sequence[pulumi.Input['AlarmDimensionArgs']]]] = None,
             evaluate_low_sample_count_percentile: Optional[pulumi.Input[str]] = None,
             extended_statistic: Optional[pulumi.Input[str]] = None,
             insufficient_data_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             metric_name: Optional[pulumi.Input[str]] = None,
             metrics: Optional[pulumi.Input[Sequence[pulumi.Input['AlarmMetricDataQueryArgs']]]] = None,
             namespace: Optional[pulumi.Input[str]] = None,
             ok_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             period: Optional[pulumi.Input[int]] = None,
             statistic: Optional[pulumi.Input[str]] = None,
             threshold: Optional[pulumi.Input[float]] = None,
             threshold_metric_id: Optional[pulumi.Input[str]] = None,
             treat_missing_data: Optional[pulumi.Input[str]] = None,
             unit: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("comparison_operator", comparison_operator)
        _setter("evaluation_periods", evaluation_periods)
        if actions_enabled is not None:
            _setter("actions_enabled", actions_enabled)
        if alarm_actions is not None:
            _setter("alarm_actions", alarm_actions)
        if alarm_description is not None:
            _setter("alarm_description", alarm_description)
        if alarm_name is not None:
            _setter("alarm_name", alarm_name)
        if datapoints_to_alarm is not None:
            _setter("datapoints_to_alarm", datapoints_to_alarm)
        if dimensions is not None:
            _setter("dimensions", dimensions)
        if evaluate_low_sample_count_percentile is not None:
            _setter("evaluate_low_sample_count_percentile", evaluate_low_sample_count_percentile)
        if extended_statistic is not None:
            _setter("extended_statistic", extended_statistic)
        if insufficient_data_actions is not None:
            _setter("insufficient_data_actions", insufficient_data_actions)
        if metric_name is not None:
            _setter("metric_name", metric_name)
        if metrics is not None:
            _setter("metrics", metrics)
        if namespace is not None:
            _setter("namespace", namespace)
        if ok_actions is not None:
            _setter("ok_actions", ok_actions)
        if period is not None:
            _setter("period", period)
        if statistic is not None:
            _setter("statistic", statistic)
        if threshold is not None:
            _setter("threshold", threshold)
        if threshold_metric_id is not None:
            _setter("threshold_metric_id", threshold_metric_id)
        if treat_missing_data is not None:
            _setter("treat_missing_data", treat_missing_data)
        if unit is not None:
            _setter("unit", unit)

    @property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> pulumi.Input[str]:
        """
        The arithmetic operation to use when comparing the specified statistic and threshold.
        """
        return pulumi.get(self, "comparison_operator")

    @comparison_operator.setter
    def comparison_operator(self, value: pulumi.Input[str]):
        pulumi.set(self, "comparison_operator", value)

    @property
    @pulumi.getter(name="evaluationPeriods")
    def evaluation_periods(self) -> pulumi.Input[int]:
        """
        The number of periods over which data is compared to the specified threshold.
        """
        return pulumi.get(self, "evaluation_periods")

    @evaluation_periods.setter
    def evaluation_periods(self, value: pulumi.Input[int]):
        pulumi.set(self, "evaluation_periods", value)

    @property
    @pulumi.getter(name="actionsEnabled")
    def actions_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE.
        """
        return pulumi.get(self, "actions_enabled")

    @actions_enabled.setter
    def actions_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "actions_enabled", value)

    @property
    @pulumi.getter(name="alarmActions")
    def alarm_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of actions to execute when this alarm transitions into an ALARM state from any other state.
        """
        return pulumi.get(self, "alarm_actions")

    @alarm_actions.setter
    def alarm_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "alarm_actions", value)

    @property
    @pulumi.getter(name="alarmDescription")
    def alarm_description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the alarm.
        """
        return pulumi.get(self, "alarm_description")

    @alarm_description.setter
    def alarm_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alarm_description", value)

    @property
    @pulumi.getter(name="alarmName")
    def alarm_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the alarm.
        """
        return pulumi.get(self, "alarm_name")

    @alarm_name.setter
    def alarm_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alarm_name", value)

    @property
    @pulumi.getter(name="datapointsToAlarm")
    def datapoints_to_alarm(self) -> Optional[pulumi.Input[int]]:
        """
        The number of datapoints that must be breaching to trigger the alarm.
        """
        return pulumi.get(self, "datapoints_to_alarm")

    @datapoints_to_alarm.setter
    def datapoints_to_alarm(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "datapoints_to_alarm", value)

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AlarmDimensionArgs']]]]:
        """
        The dimensions for the metric associated with the alarm. For an alarm based on a math expression, you can't specify Dimensions. Instead, you use Metrics.
        """
        return pulumi.get(self, "dimensions")

    @dimensions.setter
    def dimensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AlarmDimensionArgs']]]]):
        pulumi.set(self, "dimensions", value)

    @property
    @pulumi.getter(name="evaluateLowSampleCountPercentile")
    def evaluate_low_sample_count_percentile(self) -> Optional[pulumi.Input[str]]:
        """
        Used only for alarms based on percentiles.
        """
        return pulumi.get(self, "evaluate_low_sample_count_percentile")

    @evaluate_low_sample_count_percentile.setter
    def evaluate_low_sample_count_percentile(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "evaluate_low_sample_count_percentile", value)

    @property
    @pulumi.getter(name="extendedStatistic")
    def extended_statistic(self) -> Optional[pulumi.Input[str]]:
        """
        The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.
        """
        return pulumi.get(self, "extended_statistic")

    @extended_statistic.setter
    def extended_statistic(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "extended_statistic", value)

    @property
    @pulumi.getter(name="insufficientDataActions")
    def insufficient_data_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state.
        """
        return pulumi.get(self, "insufficient_data_actions")

    @insufficient_data_actions.setter
    def insufficient_data_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "insufficient_data_actions", value)

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the metric associated with the alarm.
        """
        return pulumi.get(self, "metric_name")

    @metric_name.setter
    def metric_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_name", value)

    @property
    @pulumi.getter
    def metrics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AlarmMetricDataQueryArgs']]]]:
        """
        An array that enables you to create an alarm based on the result of a metric math expression.
        """
        return pulumi.get(self, "metrics")

    @metrics.setter
    def metrics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AlarmMetricDataQueryArgs']]]]):
        pulumi.set(self, "metrics", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace of the metric associated with the alarm.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter(name="okActions")
    def ok_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The actions to execute when this alarm transitions to the OK state from any other state.
        """
        return pulumi.get(self, "ok_actions")

    @ok_actions.setter
    def ok_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ok_actions", value)

    @property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[int]]:
        """
        The period in seconds, over which the statistic is applied.
        """
        return pulumi.get(self, "period")

    @period.setter
    def period(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "period", value)

    @property
    @pulumi.getter
    def statistic(self) -> Optional[pulumi.Input[str]]:
        """
        The statistic for the metric associated with the alarm, other than percentile.
        """
        return pulumi.get(self, "statistic")

    @statistic.setter
    def statistic(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "statistic", value)

    @property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input[float]]:
        """
        In an alarm based on an anomaly detection model, this is the ID of the ANOMALY_DETECTION_BAND function used as the threshold for the alarm.
        """
        return pulumi.get(self, "threshold")

    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "threshold", value)

    @property
    @pulumi.getter(name="thresholdMetricId")
    def threshold_metric_id(self) -> Optional[pulumi.Input[str]]:
        """
        In an alarm based on an anomaly detection model, this is the ID of the ANOMALY_DETECTION_BAND function used as the threshold for the alarm.
        """
        return pulumi.get(self, "threshold_metric_id")

    @threshold_metric_id.setter
    def threshold_metric_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "threshold_metric_id", value)

    @property
    @pulumi.getter(name="treatMissingData")
    def treat_missing_data(self) -> Optional[pulumi.Input[str]]:
        """
        Sets how this alarm is to handle missing data points. Valid values are breaching, notBreaching, ignore, and missing.
        """
        return pulumi.get(self, "treat_missing_data")

    @treat_missing_data.setter
    def treat_missing_data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "treat_missing_data", value)

    @property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[str]]:
        """
        The unit of the metric associated with the alarm.
        """
        return pulumi.get(self, "unit")

    @unit.setter
    def unit(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "unit", value)


class Alarm(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions_enabled: Optional[pulumi.Input[bool]] = None,
                 alarm_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 alarm_description: Optional[pulumi.Input[str]] = None,
                 alarm_name: Optional[pulumi.Input[str]] = None,
                 comparison_operator: Optional[pulumi.Input[str]] = None,
                 datapoints_to_alarm: Optional[pulumi.Input[int]] = None,
                 dimensions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AlarmDimensionArgs']]]]] = None,
                 evaluate_low_sample_count_percentile: Optional[pulumi.Input[str]] = None,
                 evaluation_periods: Optional[pulumi.Input[int]] = None,
                 extended_statistic: Optional[pulumi.Input[str]] = None,
                 insufficient_data_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 metric_name: Optional[pulumi.Input[str]] = None,
                 metrics: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AlarmMetricDataQueryArgs']]]]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 ok_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 period: Optional[pulumi.Input[int]] = None,
                 statistic: Optional[pulumi.Input[str]] = None,
                 threshold: Optional[pulumi.Input[float]] = None,
                 threshold_metric_id: Optional[pulumi.Input[str]] = None,
                 treat_missing_data: Optional[pulumi.Input[str]] = None,
                 unit: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::CloudWatch::Alarm

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] actions_enabled: Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] alarm_actions: The list of actions to execute when this alarm transitions into an ALARM state from any other state.
        :param pulumi.Input[str] alarm_description: The description of the alarm.
        :param pulumi.Input[str] alarm_name: The name of the alarm.
        :param pulumi.Input[str] comparison_operator: The arithmetic operation to use when comparing the specified statistic and threshold.
        :param pulumi.Input[int] datapoints_to_alarm: The number of datapoints that must be breaching to trigger the alarm.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AlarmDimensionArgs']]]] dimensions: The dimensions for the metric associated with the alarm. For an alarm based on a math expression, you can't specify Dimensions. Instead, you use Metrics.
        :param pulumi.Input[str] evaluate_low_sample_count_percentile: Used only for alarms based on percentiles.
        :param pulumi.Input[int] evaluation_periods: The number of periods over which data is compared to the specified threshold.
        :param pulumi.Input[str] extended_statistic: The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] insufficient_data_actions: The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state.
        :param pulumi.Input[str] metric_name: The name of the metric associated with the alarm.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AlarmMetricDataQueryArgs']]]] metrics: An array that enables you to create an alarm based on the result of a metric math expression.
        :param pulumi.Input[str] namespace: The namespace of the metric associated with the alarm.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ok_actions: The actions to execute when this alarm transitions to the OK state from any other state.
        :param pulumi.Input[int] period: The period in seconds, over which the statistic is applied.
        :param pulumi.Input[str] statistic: The statistic for the metric associated with the alarm, other than percentile.
        :param pulumi.Input[float] threshold: In an alarm based on an anomaly detection model, this is the ID of the ANOMALY_DETECTION_BAND function used as the threshold for the alarm.
        :param pulumi.Input[str] threshold_metric_id: In an alarm based on an anomaly detection model, this is the ID of the ANOMALY_DETECTION_BAND function used as the threshold for the alarm.
        :param pulumi.Input[str] treat_missing_data: Sets how this alarm is to handle missing data points. Valid values are breaching, notBreaching, ignore, and missing.
        :param pulumi.Input[str] unit: The unit of the metric associated with the alarm.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AlarmArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::CloudWatch::Alarm

        :param str resource_name: The name of the resource.
        :param AlarmArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AlarmArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            AlarmArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions_enabled: Optional[pulumi.Input[bool]] = None,
                 alarm_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 alarm_description: Optional[pulumi.Input[str]] = None,
                 alarm_name: Optional[pulumi.Input[str]] = None,
                 comparison_operator: Optional[pulumi.Input[str]] = None,
                 datapoints_to_alarm: Optional[pulumi.Input[int]] = None,
                 dimensions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AlarmDimensionArgs']]]]] = None,
                 evaluate_low_sample_count_percentile: Optional[pulumi.Input[str]] = None,
                 evaluation_periods: Optional[pulumi.Input[int]] = None,
                 extended_statistic: Optional[pulumi.Input[str]] = None,
                 insufficient_data_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 metric_name: Optional[pulumi.Input[str]] = None,
                 metrics: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AlarmMetricDataQueryArgs']]]]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 ok_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 period: Optional[pulumi.Input[int]] = None,
                 statistic: Optional[pulumi.Input[str]] = None,
                 threshold: Optional[pulumi.Input[float]] = None,
                 threshold_metric_id: Optional[pulumi.Input[str]] = None,
                 treat_missing_data: Optional[pulumi.Input[str]] = None,
                 unit: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AlarmArgs.__new__(AlarmArgs)

            __props__.__dict__["actions_enabled"] = actions_enabled
            __props__.__dict__["alarm_actions"] = alarm_actions
            __props__.__dict__["alarm_description"] = alarm_description
            __props__.__dict__["alarm_name"] = alarm_name
            if comparison_operator is None and not opts.urn:
                raise TypeError("Missing required property 'comparison_operator'")
            __props__.__dict__["comparison_operator"] = comparison_operator
            __props__.__dict__["datapoints_to_alarm"] = datapoints_to_alarm
            __props__.__dict__["dimensions"] = dimensions
            __props__.__dict__["evaluate_low_sample_count_percentile"] = evaluate_low_sample_count_percentile
            if evaluation_periods is None and not opts.urn:
                raise TypeError("Missing required property 'evaluation_periods'")
            __props__.__dict__["evaluation_periods"] = evaluation_periods
            __props__.__dict__["extended_statistic"] = extended_statistic
            __props__.__dict__["insufficient_data_actions"] = insufficient_data_actions
            __props__.__dict__["metric_name"] = metric_name
            __props__.__dict__["metrics"] = metrics
            __props__.__dict__["namespace"] = namespace
            __props__.__dict__["ok_actions"] = ok_actions
            __props__.__dict__["period"] = period
            __props__.__dict__["statistic"] = statistic
            __props__.__dict__["threshold"] = threshold
            __props__.__dict__["threshold_metric_id"] = threshold_metric_id
            __props__.__dict__["treat_missing_data"] = treat_missing_data
            __props__.__dict__["unit"] = unit
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["alarm_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Alarm, __self__).__init__(
            'aws-native:cloudwatch:Alarm',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Alarm':
        """
        Get an existing Alarm resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AlarmArgs.__new__(AlarmArgs)

        __props__.__dict__["actions_enabled"] = None
        __props__.__dict__["alarm_actions"] = None
        __props__.__dict__["alarm_description"] = None
        __props__.__dict__["alarm_name"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["comparison_operator"] = None
        __props__.__dict__["datapoints_to_alarm"] = None
        __props__.__dict__["dimensions"] = None
        __props__.__dict__["evaluate_low_sample_count_percentile"] = None
        __props__.__dict__["evaluation_periods"] = None
        __props__.__dict__["extended_statistic"] = None
        __props__.__dict__["insufficient_data_actions"] = None
        __props__.__dict__["metric_name"] = None
        __props__.__dict__["metrics"] = None
        __props__.__dict__["namespace"] = None
        __props__.__dict__["ok_actions"] = None
        __props__.__dict__["period"] = None
        __props__.__dict__["statistic"] = None
        __props__.__dict__["threshold"] = None
        __props__.__dict__["threshold_metric_id"] = None
        __props__.__dict__["treat_missing_data"] = None
        __props__.__dict__["unit"] = None
        return Alarm(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="actionsEnabled")
    def actions_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE.
        """
        return pulumi.get(self, "actions_enabled")

    @property
    @pulumi.getter(name="alarmActions")
    def alarm_actions(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The list of actions to execute when this alarm transitions into an ALARM state from any other state.
        """
        return pulumi.get(self, "alarm_actions")

    @property
    @pulumi.getter(name="alarmDescription")
    def alarm_description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the alarm.
        """
        return pulumi.get(self, "alarm_description")

    @property
    @pulumi.getter(name="alarmName")
    def alarm_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the alarm.
        """
        return pulumi.get(self, "alarm_name")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name is a unique name for each resource.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> pulumi.Output[str]:
        """
        The arithmetic operation to use when comparing the specified statistic and threshold.
        """
        return pulumi.get(self, "comparison_operator")

    @property
    @pulumi.getter(name="datapointsToAlarm")
    def datapoints_to_alarm(self) -> pulumi.Output[Optional[int]]:
        """
        The number of datapoints that must be breaching to trigger the alarm.
        """
        return pulumi.get(self, "datapoints_to_alarm")

    @property
    @pulumi.getter
    def dimensions(self) -> pulumi.Output[Optional[Sequence['outputs.AlarmDimension']]]:
        """
        The dimensions for the metric associated with the alarm. For an alarm based on a math expression, you can't specify Dimensions. Instead, you use Metrics.
        """
        return pulumi.get(self, "dimensions")

    @property
    @pulumi.getter(name="evaluateLowSampleCountPercentile")
    def evaluate_low_sample_count_percentile(self) -> pulumi.Output[Optional[str]]:
        """
        Used only for alarms based on percentiles.
        """
        return pulumi.get(self, "evaluate_low_sample_count_percentile")

    @property
    @pulumi.getter(name="evaluationPeriods")
    def evaluation_periods(self) -> pulumi.Output[int]:
        """
        The number of periods over which data is compared to the specified threshold.
        """
        return pulumi.get(self, "evaluation_periods")

    @property
    @pulumi.getter(name="extendedStatistic")
    def extended_statistic(self) -> pulumi.Output[Optional[str]]:
        """
        The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.
        """
        return pulumi.get(self, "extended_statistic")

    @property
    @pulumi.getter(name="insufficientDataActions")
    def insufficient_data_actions(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state.
        """
        return pulumi.get(self, "insufficient_data_actions")

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the metric associated with the alarm.
        """
        return pulumi.get(self, "metric_name")

    @property
    @pulumi.getter
    def metrics(self) -> pulumi.Output[Optional[Sequence['outputs.AlarmMetricDataQuery']]]:
        """
        An array that enables you to create an alarm based on the result of a metric math expression.
        """
        return pulumi.get(self, "metrics")

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[Optional[str]]:
        """
        The namespace of the metric associated with the alarm.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="okActions")
    def ok_actions(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The actions to execute when this alarm transitions to the OK state from any other state.
        """
        return pulumi.get(self, "ok_actions")

    @property
    @pulumi.getter
    def period(self) -> pulumi.Output[Optional[int]]:
        """
        The period in seconds, over which the statistic is applied.
        """
        return pulumi.get(self, "period")

    @property
    @pulumi.getter
    def statistic(self) -> pulumi.Output[Optional[str]]:
        """
        The statistic for the metric associated with the alarm, other than percentile.
        """
        return pulumi.get(self, "statistic")

    @property
    @pulumi.getter
    def threshold(self) -> pulumi.Output[Optional[float]]:
        """
        In an alarm based on an anomaly detection model, this is the ID of the ANOMALY_DETECTION_BAND function used as the threshold for the alarm.
        """
        return pulumi.get(self, "threshold")

    @property
    @pulumi.getter(name="thresholdMetricId")
    def threshold_metric_id(self) -> pulumi.Output[Optional[str]]:
        """
        In an alarm based on an anomaly detection model, this is the ID of the ANOMALY_DETECTION_BAND function used as the threshold for the alarm.
        """
        return pulumi.get(self, "threshold_metric_id")

    @property
    @pulumi.getter(name="treatMissingData")
    def treat_missing_data(self) -> pulumi.Output[Optional[str]]:
        """
        Sets how this alarm is to handle missing data points. Valid values are breaching, notBreaching, ignore, and missing.
        """
        return pulumi.get(self, "treat_missing_data")

    @property
    @pulumi.getter
    def unit(self) -> pulumi.Output[Optional[str]]:
        """
        The unit of the metric associated with the alarm.
        """
        return pulumi.get(self, "unit")

