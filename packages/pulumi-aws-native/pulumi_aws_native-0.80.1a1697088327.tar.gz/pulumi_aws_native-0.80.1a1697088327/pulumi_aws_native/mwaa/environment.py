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

__all__ = ['EnvironmentArgs', 'Environment']

@pulumi.input_type
class EnvironmentArgs:
    def __init__(__self__, *,
                 airflow_configuration_options: Optional[Any] = None,
                 airflow_version: Optional[pulumi.Input[str]] = None,
                 dag_s3_path: Optional[pulumi.Input[str]] = None,
                 environment_class: Optional[pulumi.Input[str]] = None,
                 execution_role_arn: Optional[pulumi.Input[str]] = None,
                 kms_key: Optional[pulumi.Input[str]] = None,
                 logging_configuration: Optional[pulumi.Input['EnvironmentLoggingConfigurationArgs']] = None,
                 max_workers: Optional[pulumi.Input[int]] = None,
                 min_workers: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_configuration: Optional[pulumi.Input['EnvironmentNetworkConfigurationArgs']] = None,
                 plugins_s3_object_version: Optional[pulumi.Input[str]] = None,
                 plugins_s3_path: Optional[pulumi.Input[str]] = None,
                 requirements_s3_object_version: Optional[pulumi.Input[str]] = None,
                 requirements_s3_path: Optional[pulumi.Input[str]] = None,
                 schedulers: Optional[pulumi.Input[int]] = None,
                 source_bucket_arn: Optional[pulumi.Input[str]] = None,
                 startup_script_s3_object_version: Optional[pulumi.Input[str]] = None,
                 startup_script_s3_path: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None,
                 webserver_access_mode: Optional[pulumi.Input['EnvironmentWebserverAccessMode']] = None,
                 weekly_maintenance_window_start: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Environment resource.
        :param Any airflow_configuration_options: Key/value pairs representing Airflow configuration variables.
                   Keys are prefixed by their section:
               
                   [core]
                   dags_folder={AIRFLOW_HOME}/dags
               
                   Would be represented as
               
                   "core.dags_folder": "{AIRFLOW_HOME}/dags"
        :param Any tags: A map of tags for the environment.
        """
        EnvironmentArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            airflow_configuration_options=airflow_configuration_options,
            airflow_version=airflow_version,
            dag_s3_path=dag_s3_path,
            environment_class=environment_class,
            execution_role_arn=execution_role_arn,
            kms_key=kms_key,
            logging_configuration=logging_configuration,
            max_workers=max_workers,
            min_workers=min_workers,
            name=name,
            network_configuration=network_configuration,
            plugins_s3_object_version=plugins_s3_object_version,
            plugins_s3_path=plugins_s3_path,
            requirements_s3_object_version=requirements_s3_object_version,
            requirements_s3_path=requirements_s3_path,
            schedulers=schedulers,
            source_bucket_arn=source_bucket_arn,
            startup_script_s3_object_version=startup_script_s3_object_version,
            startup_script_s3_path=startup_script_s3_path,
            tags=tags,
            webserver_access_mode=webserver_access_mode,
            weekly_maintenance_window_start=weekly_maintenance_window_start,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             airflow_configuration_options: Optional[Any] = None,
             airflow_version: Optional[pulumi.Input[str]] = None,
             dag_s3_path: Optional[pulumi.Input[str]] = None,
             environment_class: Optional[pulumi.Input[str]] = None,
             execution_role_arn: Optional[pulumi.Input[str]] = None,
             kms_key: Optional[pulumi.Input[str]] = None,
             logging_configuration: Optional[pulumi.Input['EnvironmentLoggingConfigurationArgs']] = None,
             max_workers: Optional[pulumi.Input[int]] = None,
             min_workers: Optional[pulumi.Input[int]] = None,
             name: Optional[pulumi.Input[str]] = None,
             network_configuration: Optional[pulumi.Input['EnvironmentNetworkConfigurationArgs']] = None,
             plugins_s3_object_version: Optional[pulumi.Input[str]] = None,
             plugins_s3_path: Optional[pulumi.Input[str]] = None,
             requirements_s3_object_version: Optional[pulumi.Input[str]] = None,
             requirements_s3_path: Optional[pulumi.Input[str]] = None,
             schedulers: Optional[pulumi.Input[int]] = None,
             source_bucket_arn: Optional[pulumi.Input[str]] = None,
             startup_script_s3_object_version: Optional[pulumi.Input[str]] = None,
             startup_script_s3_path: Optional[pulumi.Input[str]] = None,
             tags: Optional[Any] = None,
             webserver_access_mode: Optional[pulumi.Input['EnvironmentWebserverAccessMode']] = None,
             weekly_maintenance_window_start: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if airflow_configuration_options is not None:
            _setter("airflow_configuration_options", airflow_configuration_options)
        if airflow_version is not None:
            _setter("airflow_version", airflow_version)
        if dag_s3_path is not None:
            _setter("dag_s3_path", dag_s3_path)
        if environment_class is not None:
            _setter("environment_class", environment_class)
        if execution_role_arn is not None:
            _setter("execution_role_arn", execution_role_arn)
        if kms_key is not None:
            _setter("kms_key", kms_key)
        if logging_configuration is not None:
            _setter("logging_configuration", logging_configuration)
        if max_workers is not None:
            _setter("max_workers", max_workers)
        if min_workers is not None:
            _setter("min_workers", min_workers)
        if name is not None:
            _setter("name", name)
        if network_configuration is not None:
            _setter("network_configuration", network_configuration)
        if plugins_s3_object_version is not None:
            _setter("plugins_s3_object_version", plugins_s3_object_version)
        if plugins_s3_path is not None:
            _setter("plugins_s3_path", plugins_s3_path)
        if requirements_s3_object_version is not None:
            _setter("requirements_s3_object_version", requirements_s3_object_version)
        if requirements_s3_path is not None:
            _setter("requirements_s3_path", requirements_s3_path)
        if schedulers is not None:
            _setter("schedulers", schedulers)
        if source_bucket_arn is not None:
            _setter("source_bucket_arn", source_bucket_arn)
        if startup_script_s3_object_version is not None:
            _setter("startup_script_s3_object_version", startup_script_s3_object_version)
        if startup_script_s3_path is not None:
            _setter("startup_script_s3_path", startup_script_s3_path)
        if tags is not None:
            _setter("tags", tags)
        if webserver_access_mode is not None:
            _setter("webserver_access_mode", webserver_access_mode)
        if weekly_maintenance_window_start is not None:
            _setter("weekly_maintenance_window_start", weekly_maintenance_window_start)

    @property
    @pulumi.getter(name="airflowConfigurationOptions")
    def airflow_configuration_options(self) -> Optional[Any]:
        """
        Key/value pairs representing Airflow configuration variables.
            Keys are prefixed by their section:

            [core]
            dags_folder={AIRFLOW_HOME}/dags

            Would be represented as

            "core.dags_folder": "{AIRFLOW_HOME}/dags"
        """
        return pulumi.get(self, "airflow_configuration_options")

    @airflow_configuration_options.setter
    def airflow_configuration_options(self, value: Optional[Any]):
        pulumi.set(self, "airflow_configuration_options", value)

    @property
    @pulumi.getter(name="airflowVersion")
    def airflow_version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "airflow_version")

    @airflow_version.setter
    def airflow_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "airflow_version", value)

    @property
    @pulumi.getter(name="dagS3Path")
    def dag_s3_path(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "dag_s3_path")

    @dag_s3_path.setter
    def dag_s3_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dag_s3_path", value)

    @property
    @pulumi.getter(name="environmentClass")
    def environment_class(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "environment_class")

    @environment_class.setter
    def environment_class(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment_class", value)

    @property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "execution_role_arn")

    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "execution_role_arn", value)

    @property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "kms_key")

    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key", value)

    @property
    @pulumi.getter(name="loggingConfiguration")
    def logging_configuration(self) -> Optional[pulumi.Input['EnvironmentLoggingConfigurationArgs']]:
        return pulumi.get(self, "logging_configuration")

    @logging_configuration.setter
    def logging_configuration(self, value: Optional[pulumi.Input['EnvironmentLoggingConfigurationArgs']]):
        pulumi.set(self, "logging_configuration", value)

    @property
    @pulumi.getter(name="maxWorkers")
    def max_workers(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "max_workers")

    @max_workers.setter
    def max_workers(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_workers", value)

    @property
    @pulumi.getter(name="minWorkers")
    def min_workers(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "min_workers")

    @min_workers.setter
    def min_workers(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_workers", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> Optional[pulumi.Input['EnvironmentNetworkConfigurationArgs']]:
        return pulumi.get(self, "network_configuration")

    @network_configuration.setter
    def network_configuration(self, value: Optional[pulumi.Input['EnvironmentNetworkConfigurationArgs']]):
        pulumi.set(self, "network_configuration", value)

    @property
    @pulumi.getter(name="pluginsS3ObjectVersion")
    def plugins_s3_object_version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "plugins_s3_object_version")

    @plugins_s3_object_version.setter
    def plugins_s3_object_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "plugins_s3_object_version", value)

    @property
    @pulumi.getter(name="pluginsS3Path")
    def plugins_s3_path(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "plugins_s3_path")

    @plugins_s3_path.setter
    def plugins_s3_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "plugins_s3_path", value)

    @property
    @pulumi.getter(name="requirementsS3ObjectVersion")
    def requirements_s3_object_version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "requirements_s3_object_version")

    @requirements_s3_object_version.setter
    def requirements_s3_object_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "requirements_s3_object_version", value)

    @property
    @pulumi.getter(name="requirementsS3Path")
    def requirements_s3_path(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "requirements_s3_path")

    @requirements_s3_path.setter
    def requirements_s3_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "requirements_s3_path", value)

    @property
    @pulumi.getter
    def schedulers(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "schedulers")

    @schedulers.setter
    def schedulers(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "schedulers", value)

    @property
    @pulumi.getter(name="sourceBucketArn")
    def source_bucket_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source_bucket_arn")

    @source_bucket_arn.setter
    def source_bucket_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_bucket_arn", value)

    @property
    @pulumi.getter(name="startupScriptS3ObjectVersion")
    def startup_script_s3_object_version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "startup_script_s3_object_version")

    @startup_script_s3_object_version.setter
    def startup_script_s3_object_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "startup_script_s3_object_version", value)

    @property
    @pulumi.getter(name="startupScriptS3Path")
    def startup_script_s3_path(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "startup_script_s3_path")

    @startup_script_s3_path.setter
    def startup_script_s3_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "startup_script_s3_path", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        A map of tags for the environment.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[Any]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="webserverAccessMode")
    def webserver_access_mode(self) -> Optional[pulumi.Input['EnvironmentWebserverAccessMode']]:
        return pulumi.get(self, "webserver_access_mode")

    @webserver_access_mode.setter
    def webserver_access_mode(self, value: Optional[pulumi.Input['EnvironmentWebserverAccessMode']]):
        pulumi.set(self, "webserver_access_mode", value)

    @property
    @pulumi.getter(name="weeklyMaintenanceWindowStart")
    def weekly_maintenance_window_start(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "weekly_maintenance_window_start")

    @weekly_maintenance_window_start.setter
    def weekly_maintenance_window_start(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "weekly_maintenance_window_start", value)


class Environment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 airflow_configuration_options: Optional[Any] = None,
                 airflow_version: Optional[pulumi.Input[str]] = None,
                 dag_s3_path: Optional[pulumi.Input[str]] = None,
                 environment_class: Optional[pulumi.Input[str]] = None,
                 execution_role_arn: Optional[pulumi.Input[str]] = None,
                 kms_key: Optional[pulumi.Input[str]] = None,
                 logging_configuration: Optional[pulumi.Input[pulumi.InputType['EnvironmentLoggingConfigurationArgs']]] = None,
                 max_workers: Optional[pulumi.Input[int]] = None,
                 min_workers: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_configuration: Optional[pulumi.Input[pulumi.InputType['EnvironmentNetworkConfigurationArgs']]] = None,
                 plugins_s3_object_version: Optional[pulumi.Input[str]] = None,
                 plugins_s3_path: Optional[pulumi.Input[str]] = None,
                 requirements_s3_object_version: Optional[pulumi.Input[str]] = None,
                 requirements_s3_path: Optional[pulumi.Input[str]] = None,
                 schedulers: Optional[pulumi.Input[int]] = None,
                 source_bucket_arn: Optional[pulumi.Input[str]] = None,
                 startup_script_s3_object_version: Optional[pulumi.Input[str]] = None,
                 startup_script_s3_path: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None,
                 webserver_access_mode: Optional[pulumi.Input['EnvironmentWebserverAccessMode']] = None,
                 weekly_maintenance_window_start: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource schema for AWS::MWAA::Environment

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param Any airflow_configuration_options: Key/value pairs representing Airflow configuration variables.
                   Keys are prefixed by their section:
               
                   [core]
                   dags_folder={AIRFLOW_HOME}/dags
               
                   Would be represented as
               
                   "core.dags_folder": "{AIRFLOW_HOME}/dags"
        :param Any tags: A map of tags for the environment.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[EnvironmentArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::MWAA::Environment

        :param str resource_name: The name of the resource.
        :param EnvironmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EnvironmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            EnvironmentArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 airflow_configuration_options: Optional[Any] = None,
                 airflow_version: Optional[pulumi.Input[str]] = None,
                 dag_s3_path: Optional[pulumi.Input[str]] = None,
                 environment_class: Optional[pulumi.Input[str]] = None,
                 execution_role_arn: Optional[pulumi.Input[str]] = None,
                 kms_key: Optional[pulumi.Input[str]] = None,
                 logging_configuration: Optional[pulumi.Input[pulumi.InputType['EnvironmentLoggingConfigurationArgs']]] = None,
                 max_workers: Optional[pulumi.Input[int]] = None,
                 min_workers: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_configuration: Optional[pulumi.Input[pulumi.InputType['EnvironmentNetworkConfigurationArgs']]] = None,
                 plugins_s3_object_version: Optional[pulumi.Input[str]] = None,
                 plugins_s3_path: Optional[pulumi.Input[str]] = None,
                 requirements_s3_object_version: Optional[pulumi.Input[str]] = None,
                 requirements_s3_path: Optional[pulumi.Input[str]] = None,
                 schedulers: Optional[pulumi.Input[int]] = None,
                 source_bucket_arn: Optional[pulumi.Input[str]] = None,
                 startup_script_s3_object_version: Optional[pulumi.Input[str]] = None,
                 startup_script_s3_path: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None,
                 webserver_access_mode: Optional[pulumi.Input['EnvironmentWebserverAccessMode']] = None,
                 weekly_maintenance_window_start: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EnvironmentArgs.__new__(EnvironmentArgs)

            __props__.__dict__["airflow_configuration_options"] = airflow_configuration_options
            __props__.__dict__["airflow_version"] = airflow_version
            __props__.__dict__["dag_s3_path"] = dag_s3_path
            __props__.__dict__["environment_class"] = environment_class
            __props__.__dict__["execution_role_arn"] = execution_role_arn
            __props__.__dict__["kms_key"] = kms_key
            if logging_configuration is not None and not isinstance(logging_configuration, EnvironmentLoggingConfigurationArgs):
                logging_configuration = logging_configuration or {}
                def _setter(key, value):
                    logging_configuration[key] = value
                EnvironmentLoggingConfigurationArgs._configure(_setter, **logging_configuration)
            __props__.__dict__["logging_configuration"] = logging_configuration
            __props__.__dict__["max_workers"] = max_workers
            __props__.__dict__["min_workers"] = min_workers
            __props__.__dict__["name"] = name
            if network_configuration is not None and not isinstance(network_configuration, EnvironmentNetworkConfigurationArgs):
                network_configuration = network_configuration or {}
                def _setter(key, value):
                    network_configuration[key] = value
                EnvironmentNetworkConfigurationArgs._configure(_setter, **network_configuration)
            __props__.__dict__["network_configuration"] = network_configuration
            __props__.__dict__["plugins_s3_object_version"] = plugins_s3_object_version
            __props__.__dict__["plugins_s3_path"] = plugins_s3_path
            __props__.__dict__["requirements_s3_object_version"] = requirements_s3_object_version
            __props__.__dict__["requirements_s3_path"] = requirements_s3_path
            __props__.__dict__["schedulers"] = schedulers
            __props__.__dict__["source_bucket_arn"] = source_bucket_arn
            __props__.__dict__["startup_script_s3_object_version"] = startup_script_s3_object_version
            __props__.__dict__["startup_script_s3_path"] = startup_script_s3_path
            __props__.__dict__["tags"] = tags
            __props__.__dict__["webserver_access_mode"] = webserver_access_mode
            __props__.__dict__["weekly_maintenance_window_start"] = weekly_maintenance_window_start
            __props__.__dict__["arn"] = None
            __props__.__dict__["webserver_url"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["kms_key", "name", "network_configuration.subnet_ids[*]"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Environment, __self__).__init__(
            'aws-native:mwaa:Environment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Environment':
        """
        Get an existing Environment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EnvironmentArgs.__new__(EnvironmentArgs)

        __props__.__dict__["airflow_configuration_options"] = None
        __props__.__dict__["airflow_version"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["dag_s3_path"] = None
        __props__.__dict__["environment_class"] = None
        __props__.__dict__["execution_role_arn"] = None
        __props__.__dict__["kms_key"] = None
        __props__.__dict__["logging_configuration"] = None
        __props__.__dict__["max_workers"] = None
        __props__.__dict__["min_workers"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_configuration"] = None
        __props__.__dict__["plugins_s3_object_version"] = None
        __props__.__dict__["plugins_s3_path"] = None
        __props__.__dict__["requirements_s3_object_version"] = None
        __props__.__dict__["requirements_s3_path"] = None
        __props__.__dict__["schedulers"] = None
        __props__.__dict__["source_bucket_arn"] = None
        __props__.__dict__["startup_script_s3_object_version"] = None
        __props__.__dict__["startup_script_s3_path"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["webserver_access_mode"] = None
        __props__.__dict__["webserver_url"] = None
        __props__.__dict__["weekly_maintenance_window_start"] = None
        return Environment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="airflowConfigurationOptions")
    def airflow_configuration_options(self) -> pulumi.Output[Optional[Any]]:
        """
        Key/value pairs representing Airflow configuration variables.
            Keys are prefixed by their section:

            [core]
            dags_folder={AIRFLOW_HOME}/dags

            Would be represented as

            "core.dags_folder": "{AIRFLOW_HOME}/dags"
        """
        return pulumi.get(self, "airflow_configuration_options")

    @property
    @pulumi.getter(name="airflowVersion")
    def airflow_version(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "airflow_version")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="dagS3Path")
    def dag_s3_path(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "dag_s3_path")

    @property
    @pulumi.getter(name="environmentClass")
    def environment_class(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "environment_class")

    @property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "execution_role_arn")

    @property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "kms_key")

    @property
    @pulumi.getter(name="loggingConfiguration")
    def logging_configuration(self) -> pulumi.Output[Optional['outputs.EnvironmentLoggingConfiguration']]:
        return pulumi.get(self, "logging_configuration")

    @property
    @pulumi.getter(name="maxWorkers")
    def max_workers(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "max_workers")

    @property
    @pulumi.getter(name="minWorkers")
    def min_workers(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "min_workers")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> pulumi.Output[Optional['outputs.EnvironmentNetworkConfiguration']]:
        return pulumi.get(self, "network_configuration")

    @property
    @pulumi.getter(name="pluginsS3ObjectVersion")
    def plugins_s3_object_version(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "plugins_s3_object_version")

    @property
    @pulumi.getter(name="pluginsS3Path")
    def plugins_s3_path(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "plugins_s3_path")

    @property
    @pulumi.getter(name="requirementsS3ObjectVersion")
    def requirements_s3_object_version(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "requirements_s3_object_version")

    @property
    @pulumi.getter(name="requirementsS3Path")
    def requirements_s3_path(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "requirements_s3_path")

    @property
    @pulumi.getter
    def schedulers(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "schedulers")

    @property
    @pulumi.getter(name="sourceBucketArn")
    def source_bucket_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "source_bucket_arn")

    @property
    @pulumi.getter(name="startupScriptS3ObjectVersion")
    def startup_script_s3_object_version(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "startup_script_s3_object_version")

    @property
    @pulumi.getter(name="startupScriptS3Path")
    def startup_script_s3_path(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "startup_script_s3_path")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Any]]:
        """
        A map of tags for the environment.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="webserverAccessMode")
    def webserver_access_mode(self) -> pulumi.Output[Optional['EnvironmentWebserverAccessMode']]:
        return pulumi.get(self, "webserver_access_mode")

    @property
    @pulumi.getter(name="webserverUrl")
    def webserver_url(self) -> pulumi.Output[str]:
        return pulumi.get(self, "webserver_url")

    @property
    @pulumi.getter(name="weeklyMaintenanceWindowStart")
    def weekly_maintenance_window_start(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "weekly_maintenance_window_start")

