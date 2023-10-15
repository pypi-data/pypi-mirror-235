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

__all__ = ['MetricStreamArgs', 'MetricStream']

@pulumi.input_type
class MetricStreamArgs:
    def __init__(__self__, *,
                 firehose_arn: pulumi.Input[str],
                 output_format: pulumi.Input[str],
                 role_arn: pulumi.Input[str],
                 exclude_filters: Optional[pulumi.Input[Sequence[pulumi.Input['MetricStreamFilterArgs']]]] = None,
                 include_filters: Optional[pulumi.Input[Sequence[pulumi.Input['MetricStreamFilterArgs']]]] = None,
                 include_linked_accounts_metrics: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 statistics_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['MetricStreamStatisticsConfigurationArgs']]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['MetricStreamTagArgs']]]] = None):
        """
        The set of arguments for constructing a MetricStream resource.
        :param pulumi.Input[str] firehose_arn: The ARN of the Kinesis Firehose where to stream the data.
        :param pulumi.Input[str] output_format: The output format of the data streamed to the Kinesis Firehose.
        :param pulumi.Input[str] role_arn: The ARN of the role that provides access to the Kinesis Firehose.
        :param pulumi.Input[Sequence[pulumi.Input['MetricStreamFilterArgs']]] exclude_filters: Define which metrics will be not streamed. Metrics matched by multiple instances of MetricStreamFilter are joined with an OR operation by default. If both IncludeFilters and ExcludeFilters are omitted, all metrics in the account will be streamed. IncludeFilters and ExcludeFilters are mutually exclusive. Default to null.
        :param pulumi.Input[Sequence[pulumi.Input['MetricStreamFilterArgs']]] include_filters: Define which metrics will be streamed. Metrics matched by multiple instances of MetricStreamFilter are joined with an OR operation by default. If both IncludeFilters and ExcludeFilters are omitted, all metrics in the account will be streamed. IncludeFilters and ExcludeFilters are mutually exclusive. Default to null.
        :param pulumi.Input[bool] include_linked_accounts_metrics: If you are creating a metric stream in a monitoring account, specify true to include metrics from source accounts that are linked to this monitoring account, in the metric stream. The default is false.
        :param pulumi.Input[str] name: Name of the metric stream.
        :param pulumi.Input[Sequence[pulumi.Input['MetricStreamStatisticsConfigurationArgs']]] statistics_configurations: By default, a metric stream always sends the MAX, MIN, SUM, and SAMPLECOUNT statistics for each metric that is streamed. You can use this parameter to have the metric stream also send additional statistics in the stream. This array can have up to 100 members.
        :param pulumi.Input[Sequence[pulumi.Input['MetricStreamTagArgs']]] tags: A set of tags to assign to the delivery stream.
        """
        MetricStreamArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            firehose_arn=firehose_arn,
            output_format=output_format,
            role_arn=role_arn,
            exclude_filters=exclude_filters,
            include_filters=include_filters,
            include_linked_accounts_metrics=include_linked_accounts_metrics,
            name=name,
            statistics_configurations=statistics_configurations,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             firehose_arn: pulumi.Input[str],
             output_format: pulumi.Input[str],
             role_arn: pulumi.Input[str],
             exclude_filters: Optional[pulumi.Input[Sequence[pulumi.Input['MetricStreamFilterArgs']]]] = None,
             include_filters: Optional[pulumi.Input[Sequence[pulumi.Input['MetricStreamFilterArgs']]]] = None,
             include_linked_accounts_metrics: Optional[pulumi.Input[bool]] = None,
             name: Optional[pulumi.Input[str]] = None,
             statistics_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['MetricStreamStatisticsConfigurationArgs']]]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['MetricStreamTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("firehose_arn", firehose_arn)
        _setter("output_format", output_format)
        _setter("role_arn", role_arn)
        if exclude_filters is not None:
            _setter("exclude_filters", exclude_filters)
        if include_filters is not None:
            _setter("include_filters", include_filters)
        if include_linked_accounts_metrics is not None:
            _setter("include_linked_accounts_metrics", include_linked_accounts_metrics)
        if name is not None:
            _setter("name", name)
        if statistics_configurations is not None:
            _setter("statistics_configurations", statistics_configurations)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="firehoseArn")
    def firehose_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the Kinesis Firehose where to stream the data.
        """
        return pulumi.get(self, "firehose_arn")

    @firehose_arn.setter
    def firehose_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "firehose_arn", value)

    @property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> pulumi.Input[str]:
        """
        The output format of the data streamed to the Kinesis Firehose.
        """
        return pulumi.get(self, "output_format")

    @output_format.setter
    def output_format(self, value: pulumi.Input[str]):
        pulumi.set(self, "output_format", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the role that provides access to the Kinesis Firehose.
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="excludeFilters")
    def exclude_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MetricStreamFilterArgs']]]]:
        """
        Define which metrics will be not streamed. Metrics matched by multiple instances of MetricStreamFilter are joined with an OR operation by default. If both IncludeFilters and ExcludeFilters are omitted, all metrics in the account will be streamed. IncludeFilters and ExcludeFilters are mutually exclusive. Default to null.
        """
        return pulumi.get(self, "exclude_filters")

    @exclude_filters.setter
    def exclude_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MetricStreamFilterArgs']]]]):
        pulumi.set(self, "exclude_filters", value)

    @property
    @pulumi.getter(name="includeFilters")
    def include_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MetricStreamFilterArgs']]]]:
        """
        Define which metrics will be streamed. Metrics matched by multiple instances of MetricStreamFilter are joined with an OR operation by default. If both IncludeFilters and ExcludeFilters are omitted, all metrics in the account will be streamed. IncludeFilters and ExcludeFilters are mutually exclusive. Default to null.
        """
        return pulumi.get(self, "include_filters")

    @include_filters.setter
    def include_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MetricStreamFilterArgs']]]]):
        pulumi.set(self, "include_filters", value)

    @property
    @pulumi.getter(name="includeLinkedAccountsMetrics")
    def include_linked_accounts_metrics(self) -> Optional[pulumi.Input[bool]]:
        """
        If you are creating a metric stream in a monitoring account, specify true to include metrics from source accounts that are linked to this monitoring account, in the metric stream. The default is false.
        """
        return pulumi.get(self, "include_linked_accounts_metrics")

    @include_linked_accounts_metrics.setter
    def include_linked_accounts_metrics(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_linked_accounts_metrics", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the metric stream.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="statisticsConfigurations")
    def statistics_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MetricStreamStatisticsConfigurationArgs']]]]:
        """
        By default, a metric stream always sends the MAX, MIN, SUM, and SAMPLECOUNT statistics for each metric that is streamed. You can use this parameter to have the metric stream also send additional statistics in the stream. This array can have up to 100 members.
        """
        return pulumi.get(self, "statistics_configurations")

    @statistics_configurations.setter
    def statistics_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MetricStreamStatisticsConfigurationArgs']]]]):
        pulumi.set(self, "statistics_configurations", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MetricStreamTagArgs']]]]:
        """
        A set of tags to assign to the delivery stream.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MetricStreamTagArgs']]]]):
        pulumi.set(self, "tags", value)


class MetricStream(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 exclude_filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MetricStreamFilterArgs']]]]] = None,
                 firehose_arn: Optional[pulumi.Input[str]] = None,
                 include_filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MetricStreamFilterArgs']]]]] = None,
                 include_linked_accounts_metrics: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 output_format: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 statistics_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MetricStreamStatisticsConfigurationArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MetricStreamTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for Metric Stream

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MetricStreamFilterArgs']]]] exclude_filters: Define which metrics will be not streamed. Metrics matched by multiple instances of MetricStreamFilter are joined with an OR operation by default. If both IncludeFilters and ExcludeFilters are omitted, all metrics in the account will be streamed. IncludeFilters and ExcludeFilters are mutually exclusive. Default to null.
        :param pulumi.Input[str] firehose_arn: The ARN of the Kinesis Firehose where to stream the data.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MetricStreamFilterArgs']]]] include_filters: Define which metrics will be streamed. Metrics matched by multiple instances of MetricStreamFilter are joined with an OR operation by default. If both IncludeFilters and ExcludeFilters are omitted, all metrics in the account will be streamed. IncludeFilters and ExcludeFilters are mutually exclusive. Default to null.
        :param pulumi.Input[bool] include_linked_accounts_metrics: If you are creating a metric stream in a monitoring account, specify true to include metrics from source accounts that are linked to this monitoring account, in the metric stream. The default is false.
        :param pulumi.Input[str] name: Name of the metric stream.
        :param pulumi.Input[str] output_format: The output format of the data streamed to the Kinesis Firehose.
        :param pulumi.Input[str] role_arn: The ARN of the role that provides access to the Kinesis Firehose.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MetricStreamStatisticsConfigurationArgs']]]] statistics_configurations: By default, a metric stream always sends the MAX, MIN, SUM, and SAMPLECOUNT statistics for each metric that is streamed. You can use this parameter to have the metric stream also send additional statistics in the stream. This array can have up to 100 members.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MetricStreamTagArgs']]]] tags: A set of tags to assign to the delivery stream.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MetricStreamArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for Metric Stream

        :param str resource_name: The name of the resource.
        :param MetricStreamArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MetricStreamArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            MetricStreamArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 exclude_filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MetricStreamFilterArgs']]]]] = None,
                 firehose_arn: Optional[pulumi.Input[str]] = None,
                 include_filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MetricStreamFilterArgs']]]]] = None,
                 include_linked_accounts_metrics: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 output_format: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 statistics_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MetricStreamStatisticsConfigurationArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MetricStreamTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MetricStreamArgs.__new__(MetricStreamArgs)

            __props__.__dict__["exclude_filters"] = exclude_filters
            if firehose_arn is None and not opts.urn:
                raise TypeError("Missing required property 'firehose_arn'")
            __props__.__dict__["firehose_arn"] = firehose_arn
            __props__.__dict__["include_filters"] = include_filters
            __props__.__dict__["include_linked_accounts_metrics"] = include_linked_accounts_metrics
            __props__.__dict__["name"] = name
            if output_format is None and not opts.urn:
                raise TypeError("Missing required property 'output_format'")
            __props__.__dict__["output_format"] = output_format
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
            __props__.__dict__["statistics_configurations"] = statistics_configurations
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["creation_date"] = None
            __props__.__dict__["last_update_date"] = None
            __props__.__dict__["state"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(MetricStream, __self__).__init__(
            'aws-native:cloudwatch:MetricStream',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'MetricStream':
        """
        Get an existing MetricStream resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MetricStreamArgs.__new__(MetricStreamArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["creation_date"] = None
        __props__.__dict__["exclude_filters"] = None
        __props__.__dict__["firehose_arn"] = None
        __props__.__dict__["include_filters"] = None
        __props__.__dict__["include_linked_accounts_metrics"] = None
        __props__.__dict__["last_update_date"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["output_format"] = None
        __props__.__dict__["role_arn"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["statistics_configurations"] = None
        __props__.__dict__["tags"] = None
        return MetricStream(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name of the metric stream.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[str]:
        """
        The date of creation of the metric stream.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter(name="excludeFilters")
    def exclude_filters(self) -> pulumi.Output[Optional[Sequence['outputs.MetricStreamFilter']]]:
        """
        Define which metrics will be not streamed. Metrics matched by multiple instances of MetricStreamFilter are joined with an OR operation by default. If both IncludeFilters and ExcludeFilters are omitted, all metrics in the account will be streamed. IncludeFilters and ExcludeFilters are mutually exclusive. Default to null.
        """
        return pulumi.get(self, "exclude_filters")

    @property
    @pulumi.getter(name="firehoseArn")
    def firehose_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the Kinesis Firehose where to stream the data.
        """
        return pulumi.get(self, "firehose_arn")

    @property
    @pulumi.getter(name="includeFilters")
    def include_filters(self) -> pulumi.Output[Optional[Sequence['outputs.MetricStreamFilter']]]:
        """
        Define which metrics will be streamed. Metrics matched by multiple instances of MetricStreamFilter are joined with an OR operation by default. If both IncludeFilters and ExcludeFilters are omitted, all metrics in the account will be streamed. IncludeFilters and ExcludeFilters are mutually exclusive. Default to null.
        """
        return pulumi.get(self, "include_filters")

    @property
    @pulumi.getter(name="includeLinkedAccountsMetrics")
    def include_linked_accounts_metrics(self) -> pulumi.Output[Optional[bool]]:
        """
        If you are creating a metric stream in a monitoring account, specify true to include metrics from source accounts that are linked to this monitoring account, in the metric stream. The default is false.
        """
        return pulumi.get(self, "include_linked_accounts_metrics")

    @property
    @pulumi.getter(name="lastUpdateDate")
    def last_update_date(self) -> pulumi.Output[str]:
        """
        The date of the last update of the metric stream.
        """
        return pulumi.get(self, "last_update_date")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the metric stream.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> pulumi.Output[str]:
        """
        The output format of the data streamed to the Kinesis Firehose.
        """
        return pulumi.get(self, "output_format")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the role that provides access to the Kinesis Firehose.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        Displays the state of the Metric Stream.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="statisticsConfigurations")
    def statistics_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.MetricStreamStatisticsConfiguration']]]:
        """
        By default, a metric stream always sends the MAX, MIN, SUM, and SAMPLECOUNT statistics for each metric that is streamed. You can use this parameter to have the metric stream also send additional statistics in the stream. This array can have up to 100 members.
        """
        return pulumi.get(self, "statistics_configurations")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.MetricStreamTag']]]:
        """
        A set of tags to assign to the delivery stream.
        """
        return pulumi.get(self, "tags")

