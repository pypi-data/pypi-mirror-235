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

__all__ = ['FlywheelArgs', 'Flywheel']

@pulumi.input_type
class FlywheelArgs:
    def __init__(__self__, *,
                 data_access_role_arn: pulumi.Input[str],
                 data_lake_s3_uri: pulumi.Input[str],
                 active_model_arn: Optional[pulumi.Input[str]] = None,
                 data_security_config: Optional[pulumi.Input['FlywheelDataSecurityConfigArgs']] = None,
                 flywheel_name: Optional[pulumi.Input[str]] = None,
                 model_type: Optional[pulumi.Input['FlywheelModelType']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['FlywheelTagArgs']]]] = None,
                 task_config: Optional[pulumi.Input['FlywheelTaskConfigArgs']] = None):
        """
        The set of arguments for constructing a Flywheel resource.
        """
        FlywheelArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            data_access_role_arn=data_access_role_arn,
            data_lake_s3_uri=data_lake_s3_uri,
            active_model_arn=active_model_arn,
            data_security_config=data_security_config,
            flywheel_name=flywheel_name,
            model_type=model_type,
            tags=tags,
            task_config=task_config,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             data_access_role_arn: pulumi.Input[str],
             data_lake_s3_uri: pulumi.Input[str],
             active_model_arn: Optional[pulumi.Input[str]] = None,
             data_security_config: Optional[pulumi.Input['FlywheelDataSecurityConfigArgs']] = None,
             flywheel_name: Optional[pulumi.Input[str]] = None,
             model_type: Optional[pulumi.Input['FlywheelModelType']] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['FlywheelTagArgs']]]] = None,
             task_config: Optional[pulumi.Input['FlywheelTaskConfigArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("data_access_role_arn", data_access_role_arn)
        _setter("data_lake_s3_uri", data_lake_s3_uri)
        if active_model_arn is not None:
            _setter("active_model_arn", active_model_arn)
        if data_security_config is not None:
            _setter("data_security_config", data_security_config)
        if flywheel_name is not None:
            _setter("flywheel_name", flywheel_name)
        if model_type is not None:
            _setter("model_type", model_type)
        if tags is not None:
            _setter("tags", tags)
        if task_config is not None:
            _setter("task_config", task_config)

    @property
    @pulumi.getter(name="dataAccessRoleArn")
    def data_access_role_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "data_access_role_arn")

    @data_access_role_arn.setter
    def data_access_role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_access_role_arn", value)

    @property
    @pulumi.getter(name="dataLakeS3Uri")
    def data_lake_s3_uri(self) -> pulumi.Input[str]:
        return pulumi.get(self, "data_lake_s3_uri")

    @data_lake_s3_uri.setter
    def data_lake_s3_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_lake_s3_uri", value)

    @property
    @pulumi.getter(name="activeModelArn")
    def active_model_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "active_model_arn")

    @active_model_arn.setter
    def active_model_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "active_model_arn", value)

    @property
    @pulumi.getter(name="dataSecurityConfig")
    def data_security_config(self) -> Optional[pulumi.Input['FlywheelDataSecurityConfigArgs']]:
        return pulumi.get(self, "data_security_config")

    @data_security_config.setter
    def data_security_config(self, value: Optional[pulumi.Input['FlywheelDataSecurityConfigArgs']]):
        pulumi.set(self, "data_security_config", value)

    @property
    @pulumi.getter(name="flywheelName")
    def flywheel_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "flywheel_name")

    @flywheel_name.setter
    def flywheel_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "flywheel_name", value)

    @property
    @pulumi.getter(name="modelType")
    def model_type(self) -> Optional[pulumi.Input['FlywheelModelType']]:
        return pulumi.get(self, "model_type")

    @model_type.setter
    def model_type(self, value: Optional[pulumi.Input['FlywheelModelType']]):
        pulumi.set(self, "model_type", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FlywheelTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FlywheelTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="taskConfig")
    def task_config(self) -> Optional[pulumi.Input['FlywheelTaskConfigArgs']]:
        return pulumi.get(self, "task_config")

    @task_config.setter
    def task_config(self, value: Optional[pulumi.Input['FlywheelTaskConfigArgs']]):
        pulumi.set(self, "task_config", value)


class Flywheel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active_model_arn: Optional[pulumi.Input[str]] = None,
                 data_access_role_arn: Optional[pulumi.Input[str]] = None,
                 data_lake_s3_uri: Optional[pulumi.Input[str]] = None,
                 data_security_config: Optional[pulumi.Input[pulumi.InputType['FlywheelDataSecurityConfigArgs']]] = None,
                 flywheel_name: Optional[pulumi.Input[str]] = None,
                 model_type: Optional[pulumi.Input['FlywheelModelType']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlywheelTagArgs']]]]] = None,
                 task_config: Optional[pulumi.Input[pulumi.InputType['FlywheelTaskConfigArgs']]] = None,
                 __props__=None):
        """
        The AWS::Comprehend::Flywheel resource creates an Amazon Comprehend Flywheel that enables customer to train their model.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FlywheelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::Comprehend::Flywheel resource creates an Amazon Comprehend Flywheel that enables customer to train their model.

        :param str resource_name: The name of the resource.
        :param FlywheelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FlywheelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            FlywheelArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active_model_arn: Optional[pulumi.Input[str]] = None,
                 data_access_role_arn: Optional[pulumi.Input[str]] = None,
                 data_lake_s3_uri: Optional[pulumi.Input[str]] = None,
                 data_security_config: Optional[pulumi.Input[pulumi.InputType['FlywheelDataSecurityConfigArgs']]] = None,
                 flywheel_name: Optional[pulumi.Input[str]] = None,
                 model_type: Optional[pulumi.Input['FlywheelModelType']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlywheelTagArgs']]]]] = None,
                 task_config: Optional[pulumi.Input[pulumi.InputType['FlywheelTaskConfigArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FlywheelArgs.__new__(FlywheelArgs)

            __props__.__dict__["active_model_arn"] = active_model_arn
            if data_access_role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'data_access_role_arn'")
            __props__.__dict__["data_access_role_arn"] = data_access_role_arn
            if data_lake_s3_uri is None and not opts.urn:
                raise TypeError("Missing required property 'data_lake_s3_uri'")
            __props__.__dict__["data_lake_s3_uri"] = data_lake_s3_uri
            if data_security_config is not None and not isinstance(data_security_config, FlywheelDataSecurityConfigArgs):
                data_security_config = data_security_config or {}
                def _setter(key, value):
                    data_security_config[key] = value
                FlywheelDataSecurityConfigArgs._configure(_setter, **data_security_config)
            __props__.__dict__["data_security_config"] = data_security_config
            __props__.__dict__["flywheel_name"] = flywheel_name
            __props__.__dict__["model_type"] = model_type
            __props__.__dict__["tags"] = tags
            if task_config is not None and not isinstance(task_config, FlywheelTaskConfigArgs):
                task_config = task_config or {}
                def _setter(key, value):
                    task_config[key] = value
                FlywheelTaskConfigArgs._configure(_setter, **task_config)
            __props__.__dict__["task_config"] = task_config
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["data_lake_s3_uri", "flywheel_name", "model_type", "task_config"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Flywheel, __self__).__init__(
            'aws-native:comprehend:Flywheel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Flywheel':
        """
        Get an existing Flywheel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FlywheelArgs.__new__(FlywheelArgs)

        __props__.__dict__["active_model_arn"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["data_access_role_arn"] = None
        __props__.__dict__["data_lake_s3_uri"] = None
        __props__.__dict__["data_security_config"] = None
        __props__.__dict__["flywheel_name"] = None
        __props__.__dict__["model_type"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["task_config"] = None
        return Flywheel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="activeModelArn")
    def active_model_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "active_model_arn")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="dataAccessRoleArn")
    def data_access_role_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "data_access_role_arn")

    @property
    @pulumi.getter(name="dataLakeS3Uri")
    def data_lake_s3_uri(self) -> pulumi.Output[str]:
        return pulumi.get(self, "data_lake_s3_uri")

    @property
    @pulumi.getter(name="dataSecurityConfig")
    def data_security_config(self) -> pulumi.Output[Optional['outputs.FlywheelDataSecurityConfig']]:
        return pulumi.get(self, "data_security_config")

    @property
    @pulumi.getter(name="flywheelName")
    def flywheel_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "flywheel_name")

    @property
    @pulumi.getter(name="modelType")
    def model_type(self) -> pulumi.Output[Optional['FlywheelModelType']]:
        return pulumi.get(self, "model_type")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.FlywheelTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="taskConfig")
    def task_config(self) -> pulumi.Output[Optional['outputs.FlywheelTaskConfig']]:
        return pulumi.get(self, "task_config")

