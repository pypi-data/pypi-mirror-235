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
    'ExperimentTemplateActionMapArgs',
    'ExperimentTemplateLogConfigurationCloudWatchLogsConfigurationPropertiesArgs',
    'ExperimentTemplateLogConfigurationS3ConfigurationPropertiesArgs',
    'ExperimentTemplateLogConfigurationArgs',
    'ExperimentTemplateStopConditionArgs',
    'ExperimentTemplateTargetMapArgs',
]

@pulumi.input_type
class ExperimentTemplateActionMapArgs:
    def __init__(__self__):
        """
        The actions for the experiment.
        """
        pass
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             opts: Optional[pulumi.ResourceOptions]=None):
        pass


@pulumi.input_type
class ExperimentTemplateLogConfigurationCloudWatchLogsConfigurationPropertiesArgs:
    def __init__(__self__, *,
                 log_group_arn: pulumi.Input[str]):
        ExperimentTemplateLogConfigurationCloudWatchLogsConfigurationPropertiesArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            log_group_arn=log_group_arn,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             log_group_arn: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("log_group_arn", log_group_arn)

    @property
    @pulumi.getter(name="logGroupArn")
    def log_group_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "log_group_arn")

    @log_group_arn.setter
    def log_group_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "log_group_arn", value)


@pulumi.input_type
class ExperimentTemplateLogConfigurationS3ConfigurationPropertiesArgs:
    def __init__(__self__, *,
                 bucket_name: pulumi.Input[str],
                 prefix: Optional[pulumi.Input[str]] = None):
        ExperimentTemplateLogConfigurationS3ConfigurationPropertiesArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            bucket_name=bucket_name,
            prefix=prefix,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             bucket_name: pulumi.Input[str],
             prefix: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("bucket_name", bucket_name)
        if prefix is not None:
            _setter("prefix", prefix)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "bucket_name")

    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket_name", value)

    @property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "prefix")

    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prefix", value)


@pulumi.input_type
class ExperimentTemplateLogConfigurationArgs:
    def __init__(__self__, *,
                 log_schema_version: pulumi.Input[int],
                 cloud_watch_logs_configuration: Optional[pulumi.Input['ExperimentTemplateLogConfigurationCloudWatchLogsConfigurationPropertiesArgs']] = None,
                 s3_configuration: Optional[pulumi.Input['ExperimentTemplateLogConfigurationS3ConfigurationPropertiesArgs']] = None):
        ExperimentTemplateLogConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            log_schema_version=log_schema_version,
            cloud_watch_logs_configuration=cloud_watch_logs_configuration,
            s3_configuration=s3_configuration,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             log_schema_version: pulumi.Input[int],
             cloud_watch_logs_configuration: Optional[pulumi.Input['ExperimentTemplateLogConfigurationCloudWatchLogsConfigurationPropertiesArgs']] = None,
             s3_configuration: Optional[pulumi.Input['ExperimentTemplateLogConfigurationS3ConfigurationPropertiesArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("log_schema_version", log_schema_version)
        if cloud_watch_logs_configuration is not None:
            _setter("cloud_watch_logs_configuration", cloud_watch_logs_configuration)
        if s3_configuration is not None:
            _setter("s3_configuration", s3_configuration)

    @property
    @pulumi.getter(name="logSchemaVersion")
    def log_schema_version(self) -> pulumi.Input[int]:
        return pulumi.get(self, "log_schema_version")

    @log_schema_version.setter
    def log_schema_version(self, value: pulumi.Input[int]):
        pulumi.set(self, "log_schema_version", value)

    @property
    @pulumi.getter(name="cloudWatchLogsConfiguration")
    def cloud_watch_logs_configuration(self) -> Optional[pulumi.Input['ExperimentTemplateLogConfigurationCloudWatchLogsConfigurationPropertiesArgs']]:
        return pulumi.get(self, "cloud_watch_logs_configuration")

    @cloud_watch_logs_configuration.setter
    def cloud_watch_logs_configuration(self, value: Optional[pulumi.Input['ExperimentTemplateLogConfigurationCloudWatchLogsConfigurationPropertiesArgs']]):
        pulumi.set(self, "cloud_watch_logs_configuration", value)

    @property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(self) -> Optional[pulumi.Input['ExperimentTemplateLogConfigurationS3ConfigurationPropertiesArgs']]:
        return pulumi.get(self, "s3_configuration")

    @s3_configuration.setter
    def s3_configuration(self, value: Optional[pulumi.Input['ExperimentTemplateLogConfigurationS3ConfigurationPropertiesArgs']]):
        pulumi.set(self, "s3_configuration", value)


@pulumi.input_type
class ExperimentTemplateStopConditionArgs:
    def __init__(__self__, *,
                 source: pulumi.Input[str],
                 value: Optional[pulumi.Input[str]] = None):
        ExperimentTemplateStopConditionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            source=source,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             source: pulumi.Input[str],
             value: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("source", source)
        if value is not None:
            _setter("value", value)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input[str]:
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input[str]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ExperimentTemplateTargetMapArgs:
    def __init__(__self__):
        """
        The targets for the experiment.
        """
        pass
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             opts: Optional[pulumi.ResourceOptions]=None):
        pass


