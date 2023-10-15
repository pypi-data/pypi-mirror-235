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
from ._inputs import *

__all__ = ['ScheduleArgs', 'Schedule']

@pulumi.input_type
class ScheduleArgs:
    def __init__(__self__, *,
                 flexible_time_window: pulumi.Input['ScheduleFlexibleTimeWindowArgs'],
                 schedule_expression: pulumi.Input[str],
                 target: pulumi.Input['ScheduleTargetArgs'],
                 description: Optional[pulumi.Input[str]] = None,
                 end_date: Optional[pulumi.Input[str]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 kms_key_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 schedule_expression_timezone: Optional[pulumi.Input[str]] = None,
                 start_date: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input['ScheduleState']] = None):
        """
        The set of arguments for constructing a Schedule resource.
        :param pulumi.Input[str] schedule_expression: The scheduling expression.
        :param pulumi.Input[str] description: The description of the schedule.
        :param pulumi.Input[str] end_date: The date, in UTC, before which the schedule can invoke its target. Depending on the schedule's recurrence expression, invocations might stop on, or before, the EndDate you specify.
        :param pulumi.Input[str] group_name: The name of the schedule group to associate with this schedule. If you omit this, the default schedule group is used.
        :param pulumi.Input[str] kms_key_arn: The ARN for a KMS Key that will be used to encrypt customer data.
        :param pulumi.Input[str] schedule_expression_timezone: The timezone in which the scheduling expression is evaluated.
        :param pulumi.Input[str] start_date: The date, in UTC, after which the schedule can begin invoking its target. Depending on the schedule's recurrence expression, invocations might occur on, or after, the StartDate you specify.
        """
        ScheduleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            flexible_time_window=flexible_time_window,
            schedule_expression=schedule_expression,
            target=target,
            description=description,
            end_date=end_date,
            group_name=group_name,
            kms_key_arn=kms_key_arn,
            name=name,
            schedule_expression_timezone=schedule_expression_timezone,
            start_date=start_date,
            state=state,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             flexible_time_window: pulumi.Input['ScheduleFlexibleTimeWindowArgs'],
             schedule_expression: pulumi.Input[str],
             target: pulumi.Input['ScheduleTargetArgs'],
             description: Optional[pulumi.Input[str]] = None,
             end_date: Optional[pulumi.Input[str]] = None,
             group_name: Optional[pulumi.Input[str]] = None,
             kms_key_arn: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             schedule_expression_timezone: Optional[pulumi.Input[str]] = None,
             start_date: Optional[pulumi.Input[str]] = None,
             state: Optional[pulumi.Input['ScheduleState']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("flexible_time_window", flexible_time_window)
        _setter("schedule_expression", schedule_expression)
        _setter("target", target)
        if description is not None:
            _setter("description", description)
        if end_date is not None:
            _setter("end_date", end_date)
        if group_name is not None:
            _setter("group_name", group_name)
        if kms_key_arn is not None:
            _setter("kms_key_arn", kms_key_arn)
        if name is not None:
            _setter("name", name)
        if schedule_expression_timezone is not None:
            _setter("schedule_expression_timezone", schedule_expression_timezone)
        if start_date is not None:
            _setter("start_date", start_date)
        if state is not None:
            _setter("state", state)

    @property
    @pulumi.getter(name="flexibleTimeWindow")
    def flexible_time_window(self) -> pulumi.Input['ScheduleFlexibleTimeWindowArgs']:
        return pulumi.get(self, "flexible_time_window")

    @flexible_time_window.setter
    def flexible_time_window(self, value: pulumi.Input['ScheduleFlexibleTimeWindowArgs']):
        pulumi.set(self, "flexible_time_window", value)

    @property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> pulumi.Input[str]:
        """
        The scheduling expression.
        """
        return pulumi.get(self, "schedule_expression")

    @schedule_expression.setter
    def schedule_expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "schedule_expression", value)

    @property
    @pulumi.getter
    def target(self) -> pulumi.Input['ScheduleTargetArgs']:
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: pulumi.Input['ScheduleTargetArgs']):
        pulumi.set(self, "target", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the schedule.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[pulumi.Input[str]]:
        """
        The date, in UTC, before which the schedule can invoke its target. Depending on the schedule's recurrence expression, invocations might stop on, or before, the EndDate you specify.
        """
        return pulumi.get(self, "end_date")

    @end_date.setter
    def end_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_date", value)

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the schedule group to associate with this schedule. If you omit this, the default schedule group is used.
        """
        return pulumi.get(self, "group_name")

    @group_name.setter
    def group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_name", value)

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN for a KMS Key that will be used to encrypt customer data.
        """
        return pulumi.get(self, "kms_key_arn")

    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_arn", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="scheduleExpressionTimezone")
    def schedule_expression_timezone(self) -> Optional[pulumi.Input[str]]:
        """
        The timezone in which the scheduling expression is evaluated.
        """
        return pulumi.get(self, "schedule_expression_timezone")

    @schedule_expression_timezone.setter
    def schedule_expression_timezone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schedule_expression_timezone", value)

    @property
    @pulumi.getter(name="startDate")
    def start_date(self) -> Optional[pulumi.Input[str]]:
        """
        The date, in UTC, after which the schedule can begin invoking its target. Depending on the schedule's recurrence expression, invocations might occur on, or after, the StartDate you specify.
        """
        return pulumi.get(self, "start_date")

    @start_date.setter
    def start_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_date", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input['ScheduleState']]:
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input['ScheduleState']]):
        pulumi.set(self, "state", value)


class Schedule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 end_date: Optional[pulumi.Input[str]] = None,
                 flexible_time_window: Optional[pulumi.Input[pulumi.InputType['ScheduleFlexibleTimeWindowArgs']]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 kms_key_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 schedule_expression: Optional[pulumi.Input[str]] = None,
                 schedule_expression_timezone: Optional[pulumi.Input[str]] = None,
                 start_date: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input['ScheduleState']] = None,
                 target: Optional[pulumi.Input[pulumi.InputType['ScheduleTargetArgs']]] = None,
                 __props__=None):
        """
        Definition of AWS::Scheduler::Schedule Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the schedule.
        :param pulumi.Input[str] end_date: The date, in UTC, before which the schedule can invoke its target. Depending on the schedule's recurrence expression, invocations might stop on, or before, the EndDate you specify.
        :param pulumi.Input[str] group_name: The name of the schedule group to associate with this schedule. If you omit this, the default schedule group is used.
        :param pulumi.Input[str] kms_key_arn: The ARN for a KMS Key that will be used to encrypt customer data.
        :param pulumi.Input[str] schedule_expression: The scheduling expression.
        :param pulumi.Input[str] schedule_expression_timezone: The timezone in which the scheduling expression is evaluated.
        :param pulumi.Input[str] start_date: The date, in UTC, after which the schedule can begin invoking its target. Depending on the schedule's recurrence expression, invocations might occur on, or after, the StartDate you specify.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScheduleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::Scheduler::Schedule Resource Type

        :param str resource_name: The name of the resource.
        :param ScheduleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScheduleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ScheduleArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 end_date: Optional[pulumi.Input[str]] = None,
                 flexible_time_window: Optional[pulumi.Input[pulumi.InputType['ScheduleFlexibleTimeWindowArgs']]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 kms_key_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 schedule_expression: Optional[pulumi.Input[str]] = None,
                 schedule_expression_timezone: Optional[pulumi.Input[str]] = None,
                 start_date: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input['ScheduleState']] = None,
                 target: Optional[pulumi.Input[pulumi.InputType['ScheduleTargetArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ScheduleArgs.__new__(ScheduleArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["end_date"] = end_date
            if flexible_time_window is not None and not isinstance(flexible_time_window, ScheduleFlexibleTimeWindowArgs):
                flexible_time_window = flexible_time_window or {}
                def _setter(key, value):
                    flexible_time_window[key] = value
                ScheduleFlexibleTimeWindowArgs._configure(_setter, **flexible_time_window)
            if flexible_time_window is None and not opts.urn:
                raise TypeError("Missing required property 'flexible_time_window'")
            __props__.__dict__["flexible_time_window"] = flexible_time_window
            __props__.__dict__["group_name"] = group_name
            __props__.__dict__["kms_key_arn"] = kms_key_arn
            __props__.__dict__["name"] = name
            if schedule_expression is None and not opts.urn:
                raise TypeError("Missing required property 'schedule_expression'")
            __props__.__dict__["schedule_expression"] = schedule_expression
            __props__.__dict__["schedule_expression_timezone"] = schedule_expression_timezone
            __props__.__dict__["start_date"] = start_date
            __props__.__dict__["state"] = state
            if target is not None and not isinstance(target, ScheduleTargetArgs):
                target = target or {}
                def _setter(key, value):
                    target[key] = value
                ScheduleTargetArgs._configure(_setter, **target)
            if target is None and not opts.urn:
                raise TypeError("Missing required property 'target'")
            __props__.__dict__["target"] = target
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Schedule, __self__).__init__(
            'aws-native:scheduler:Schedule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Schedule':
        """
        Get an existing Schedule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ScheduleArgs.__new__(ScheduleArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["end_date"] = None
        __props__.__dict__["flexible_time_window"] = None
        __props__.__dict__["group_name"] = None
        __props__.__dict__["kms_key_arn"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["schedule_expression"] = None
        __props__.__dict__["schedule_expression_timezone"] = None
        __props__.__dict__["start_date"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["target"] = None
        return Schedule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the schedule.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the schedule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="endDate")
    def end_date(self) -> pulumi.Output[Optional[str]]:
        """
        The date, in UTC, before which the schedule can invoke its target. Depending on the schedule's recurrence expression, invocations might stop on, or before, the EndDate you specify.
        """
        return pulumi.get(self, "end_date")

    @property
    @pulumi.getter(name="flexibleTimeWindow")
    def flexible_time_window(self) -> pulumi.Output['outputs.ScheduleFlexibleTimeWindow']:
        return pulumi.get(self, "flexible_time_window")

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the schedule group to associate with this schedule. If you omit this, the default schedule group is used.
        """
        return pulumi.get(self, "group_name")

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The ARN for a KMS Key that will be used to encrypt customer data.
        """
        return pulumi.get(self, "kms_key_arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> pulumi.Output[str]:
        """
        The scheduling expression.
        """
        return pulumi.get(self, "schedule_expression")

    @property
    @pulumi.getter(name="scheduleExpressionTimezone")
    def schedule_expression_timezone(self) -> pulumi.Output[Optional[str]]:
        """
        The timezone in which the scheduling expression is evaluated.
        """
        return pulumi.get(self, "schedule_expression_timezone")

    @property
    @pulumi.getter(name="startDate")
    def start_date(self) -> pulumi.Output[Optional[str]]:
        """
        The date, in UTC, after which the schedule can begin invoking its target. Depending on the schedule's recurrence expression, invocations might occur on, or after, the StartDate you specify.
        """
        return pulumi.get(self, "start_date")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional['ScheduleState']]:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def target(self) -> pulumi.Output['outputs.ScheduleTarget']:
        return pulumi.get(self, "target")

