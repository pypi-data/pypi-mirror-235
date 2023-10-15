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

__all__ = ['ReportPlanArgs', 'ReportPlan']

@pulumi.input_type
class ReportPlanArgs:
    def __init__(__self__, *,
                 report_delivery_channel: pulumi.Input['ReportDeliveryChannelPropertiesArgs'],
                 report_setting: pulumi.Input['ReportSettingPropertiesArgs'],
                 report_plan_description: Optional[pulumi.Input[str]] = None,
                 report_plan_name: Optional[pulumi.Input[str]] = None,
                 report_plan_tags: Optional[pulumi.Input[Sequence[pulumi.Input['ReportPlanTagArgs']]]] = None):
        """
        The set of arguments for constructing a ReportPlan resource.
        :param pulumi.Input['ReportDeliveryChannelPropertiesArgs'] report_delivery_channel: A structure that contains information about where and how to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.
        :param pulumi.Input['ReportSettingPropertiesArgs'] report_setting: Identifies the report template for the report. Reports are built using a report template.
        :param pulumi.Input[str] report_plan_description: An optional description of the report plan with a maximum of 1,024 characters.
        :param pulumi.Input[str] report_plan_name: The unique name of the report plan. The name must be between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).
        :param pulumi.Input[Sequence[pulumi.Input['ReportPlanTagArgs']]] report_plan_tags: Metadata that you can assign to help organize the report plans that you create. Each tag is a key-value pair.
        """
        ReportPlanArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            report_delivery_channel=report_delivery_channel,
            report_setting=report_setting,
            report_plan_description=report_plan_description,
            report_plan_name=report_plan_name,
            report_plan_tags=report_plan_tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             report_delivery_channel: pulumi.Input['ReportDeliveryChannelPropertiesArgs'],
             report_setting: pulumi.Input['ReportSettingPropertiesArgs'],
             report_plan_description: Optional[pulumi.Input[str]] = None,
             report_plan_name: Optional[pulumi.Input[str]] = None,
             report_plan_tags: Optional[pulumi.Input[Sequence[pulumi.Input['ReportPlanTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("report_delivery_channel", report_delivery_channel)
        _setter("report_setting", report_setting)
        if report_plan_description is not None:
            _setter("report_plan_description", report_plan_description)
        if report_plan_name is not None:
            _setter("report_plan_name", report_plan_name)
        if report_plan_tags is not None:
            _setter("report_plan_tags", report_plan_tags)

    @property
    @pulumi.getter(name="reportDeliveryChannel")
    def report_delivery_channel(self) -> pulumi.Input['ReportDeliveryChannelPropertiesArgs']:
        """
        A structure that contains information about where and how to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.
        """
        return pulumi.get(self, "report_delivery_channel")

    @report_delivery_channel.setter
    def report_delivery_channel(self, value: pulumi.Input['ReportDeliveryChannelPropertiesArgs']):
        pulumi.set(self, "report_delivery_channel", value)

    @property
    @pulumi.getter(name="reportSetting")
    def report_setting(self) -> pulumi.Input['ReportSettingPropertiesArgs']:
        """
        Identifies the report template for the report. Reports are built using a report template.
        """
        return pulumi.get(self, "report_setting")

    @report_setting.setter
    def report_setting(self, value: pulumi.Input['ReportSettingPropertiesArgs']):
        pulumi.set(self, "report_setting", value)

    @property
    @pulumi.getter(name="reportPlanDescription")
    def report_plan_description(self) -> Optional[pulumi.Input[str]]:
        """
        An optional description of the report plan with a maximum of 1,024 characters.
        """
        return pulumi.get(self, "report_plan_description")

    @report_plan_description.setter
    def report_plan_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "report_plan_description", value)

    @property
    @pulumi.getter(name="reportPlanName")
    def report_plan_name(self) -> Optional[pulumi.Input[str]]:
        """
        The unique name of the report plan. The name must be between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).
        """
        return pulumi.get(self, "report_plan_name")

    @report_plan_name.setter
    def report_plan_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "report_plan_name", value)

    @property
    @pulumi.getter(name="reportPlanTags")
    def report_plan_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ReportPlanTagArgs']]]]:
        """
        Metadata that you can assign to help organize the report plans that you create. Each tag is a key-value pair.
        """
        return pulumi.get(self, "report_plan_tags")

    @report_plan_tags.setter
    def report_plan_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ReportPlanTagArgs']]]]):
        pulumi.set(self, "report_plan_tags", value)


class ReportPlan(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 report_delivery_channel: Optional[pulumi.Input[pulumi.InputType['ReportDeliveryChannelPropertiesArgs']]] = None,
                 report_plan_description: Optional[pulumi.Input[str]] = None,
                 report_plan_name: Optional[pulumi.Input[str]] = None,
                 report_plan_tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReportPlanTagArgs']]]]] = None,
                 report_setting: Optional[pulumi.Input[pulumi.InputType['ReportSettingPropertiesArgs']]] = None,
                 __props__=None):
        """
        Contains detailed information about a report plan in AWS Backup Audit Manager.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ReportDeliveryChannelPropertiesArgs']] report_delivery_channel: A structure that contains information about where and how to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.
        :param pulumi.Input[str] report_plan_description: An optional description of the report plan with a maximum of 1,024 characters.
        :param pulumi.Input[str] report_plan_name: The unique name of the report plan. The name must be between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReportPlanTagArgs']]]] report_plan_tags: Metadata that you can assign to help organize the report plans that you create. Each tag is a key-value pair.
        :param pulumi.Input[pulumi.InputType['ReportSettingPropertiesArgs']] report_setting: Identifies the report template for the report. Reports are built using a report template.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ReportPlanArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Contains detailed information about a report plan in AWS Backup Audit Manager.

        :param str resource_name: The name of the resource.
        :param ReportPlanArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ReportPlanArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ReportPlanArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 report_delivery_channel: Optional[pulumi.Input[pulumi.InputType['ReportDeliveryChannelPropertiesArgs']]] = None,
                 report_plan_description: Optional[pulumi.Input[str]] = None,
                 report_plan_name: Optional[pulumi.Input[str]] = None,
                 report_plan_tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReportPlanTagArgs']]]]] = None,
                 report_setting: Optional[pulumi.Input[pulumi.InputType['ReportSettingPropertiesArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ReportPlanArgs.__new__(ReportPlanArgs)

            if report_delivery_channel is not None and not isinstance(report_delivery_channel, ReportDeliveryChannelPropertiesArgs):
                report_delivery_channel = report_delivery_channel or {}
                def _setter(key, value):
                    report_delivery_channel[key] = value
                ReportDeliveryChannelPropertiesArgs._configure(_setter, **report_delivery_channel)
            if report_delivery_channel is None and not opts.urn:
                raise TypeError("Missing required property 'report_delivery_channel'")
            __props__.__dict__["report_delivery_channel"] = report_delivery_channel
            __props__.__dict__["report_plan_description"] = report_plan_description
            __props__.__dict__["report_plan_name"] = report_plan_name
            __props__.__dict__["report_plan_tags"] = report_plan_tags
            if report_setting is not None and not isinstance(report_setting, ReportSettingPropertiesArgs):
                report_setting = report_setting or {}
                def _setter(key, value):
                    report_setting[key] = value
                ReportSettingPropertiesArgs._configure(_setter, **report_setting)
            if report_setting is None and not opts.urn:
                raise TypeError("Missing required property 'report_setting'")
            __props__.__dict__["report_setting"] = report_setting
            __props__.__dict__["report_plan_arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["report_plan_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ReportPlan, __self__).__init__(
            'aws-native:backup:ReportPlan',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ReportPlan':
        """
        Get an existing ReportPlan resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ReportPlanArgs.__new__(ReportPlanArgs)

        __props__.__dict__["report_delivery_channel"] = None
        __props__.__dict__["report_plan_arn"] = None
        __props__.__dict__["report_plan_description"] = None
        __props__.__dict__["report_plan_name"] = None
        __props__.__dict__["report_plan_tags"] = None
        __props__.__dict__["report_setting"] = None
        return ReportPlan(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="reportDeliveryChannel")
    def report_delivery_channel(self) -> pulumi.Output['outputs.ReportDeliveryChannelProperties']:
        """
        A structure that contains information about where and how to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.
        """
        return pulumi.get(self, "report_delivery_channel")

    @property
    @pulumi.getter(name="reportPlanArn")
    def report_plan_arn(self) -> pulumi.Output[str]:
        """
        An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.
        """
        return pulumi.get(self, "report_plan_arn")

    @property
    @pulumi.getter(name="reportPlanDescription")
    def report_plan_description(self) -> pulumi.Output[Optional[str]]:
        """
        An optional description of the report plan with a maximum of 1,024 characters.
        """
        return pulumi.get(self, "report_plan_description")

    @property
    @pulumi.getter(name="reportPlanName")
    def report_plan_name(self) -> pulumi.Output[Optional[str]]:
        """
        The unique name of the report plan. The name must be between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).
        """
        return pulumi.get(self, "report_plan_name")

    @property
    @pulumi.getter(name="reportPlanTags")
    def report_plan_tags(self) -> pulumi.Output[Optional[Sequence['outputs.ReportPlanTag']]]:
        """
        Metadata that you can assign to help organize the report plans that you create. Each tag is a key-value pair.
        """
        return pulumi.get(self, "report_plan_tags")

    @property
    @pulumi.getter(name="reportSetting")
    def report_setting(self) -> pulumi.Output['outputs.ReportSettingProperties']:
        """
        Identifies the report template for the report. Reports are built using a report template.
        """
        return pulumi.get(self, "report_setting")

