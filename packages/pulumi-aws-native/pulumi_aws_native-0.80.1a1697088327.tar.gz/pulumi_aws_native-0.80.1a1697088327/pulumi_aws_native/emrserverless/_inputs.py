# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'ApplicationAutoStartConfigurationArgs',
    'ApplicationAutoStopConfigurationArgs',
    'ApplicationImageConfigurationInputArgs',
    'ApplicationInitialCapacityConfigKeyValuePairArgs',
    'ApplicationInitialCapacityConfigArgs',
    'ApplicationMaximumAllowedResourcesArgs',
    'ApplicationNetworkConfigurationArgs',
    'ApplicationTagArgs',
    'ApplicationWorkerConfigurationArgs',
    'ApplicationWorkerTypeSpecificationInputMapArgs',
]

@pulumi.input_type
class ApplicationAutoStartConfigurationArgs:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None):
        """
        Configuration for Auto Start of Application
        :param pulumi.Input[bool] enabled: If set to true, the Application will automatically start. Defaults to true.
        """
        ApplicationAutoStartConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            enabled=enabled,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             enabled: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if enabled is not None:
            _setter("enabled", enabled)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to true, the Application will automatically start. Defaults to true.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)


@pulumi.input_type
class ApplicationAutoStopConfigurationArgs:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 idle_timeout_minutes: Optional[pulumi.Input[int]] = None):
        """
        Configuration for Auto Stop of Application
        :param pulumi.Input[bool] enabled: If set to true, the Application will automatically stop after being idle. Defaults to true.
        :param pulumi.Input[int] idle_timeout_minutes: The amount of time [in minutes] to wait before auto stopping the Application when idle. Defaults to 15 minutes.
        """
        ApplicationAutoStopConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            enabled=enabled,
            idle_timeout_minutes=idle_timeout_minutes,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             enabled: Optional[pulumi.Input[bool]] = None,
             idle_timeout_minutes: Optional[pulumi.Input[int]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if enabled is not None:
            _setter("enabled", enabled)
        if idle_timeout_minutes is not None:
            _setter("idle_timeout_minutes", idle_timeout_minutes)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to true, the Application will automatically stop after being idle. Defaults to true.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="idleTimeoutMinutes")
    def idle_timeout_minutes(self) -> Optional[pulumi.Input[int]]:
        """
        The amount of time [in minutes] to wait before auto stopping the Application when idle. Defaults to 15 minutes.
        """
        return pulumi.get(self, "idle_timeout_minutes")

    @idle_timeout_minutes.setter
    def idle_timeout_minutes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "idle_timeout_minutes", value)


@pulumi.input_type
class ApplicationImageConfigurationInputArgs:
    def __init__(__self__, *,
                 image_uri: Optional[pulumi.Input[str]] = None):
        """
        The image configuration.
        :param pulumi.Input[str] image_uri: The URI of an image in the Amazon ECR registry. This field is required when you create a new application. If you leave this field blank in an update, Amazon EMR will remove the image configuration.
        """
        ApplicationImageConfigurationInputArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            image_uri=image_uri,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             image_uri: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if image_uri is not None:
            _setter("image_uri", image_uri)

    @property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The URI of an image in the Amazon ECR registry. This field is required when you create a new application. If you leave this field blank in an update, Amazon EMR will remove the image configuration.
        """
        return pulumi.get(self, "image_uri")

    @image_uri.setter
    def image_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_uri", value)


@pulumi.input_type
class ApplicationInitialCapacityConfigKeyValuePairArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input['ApplicationInitialCapacityConfigArgs']):
        """
        :param pulumi.Input[str] key: Worker type for an analytics framework.
        """
        ApplicationInitialCapacityConfigKeyValuePairArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: pulumi.Input[str],
             value: pulumi.Input['ApplicationInitialCapacityConfigArgs'],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        Worker type for an analytics framework.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input['ApplicationInitialCapacityConfigArgs']:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input['ApplicationInitialCapacityConfigArgs']):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ApplicationInitialCapacityConfigArgs:
    def __init__(__self__, *,
                 worker_configuration: pulumi.Input['ApplicationWorkerConfigurationArgs'],
                 worker_count: pulumi.Input[int]):
        """
        :param pulumi.Input[int] worker_count: Initial count of workers to be initialized when an Application is started. This count will be continued to be maintained until the Application is stopped
        """
        ApplicationInitialCapacityConfigArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            worker_configuration=worker_configuration,
            worker_count=worker_count,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             worker_configuration: pulumi.Input['ApplicationWorkerConfigurationArgs'],
             worker_count: pulumi.Input[int],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("worker_configuration", worker_configuration)
        _setter("worker_count", worker_count)

    @property
    @pulumi.getter(name="workerConfiguration")
    def worker_configuration(self) -> pulumi.Input['ApplicationWorkerConfigurationArgs']:
        return pulumi.get(self, "worker_configuration")

    @worker_configuration.setter
    def worker_configuration(self, value: pulumi.Input['ApplicationWorkerConfigurationArgs']):
        pulumi.set(self, "worker_configuration", value)

    @property
    @pulumi.getter(name="workerCount")
    def worker_count(self) -> pulumi.Input[int]:
        """
        Initial count of workers to be initialized when an Application is started. This count will be continued to be maintained until the Application is stopped
        """
        return pulumi.get(self, "worker_count")

    @worker_count.setter
    def worker_count(self, value: pulumi.Input[int]):
        pulumi.set(self, "worker_count", value)


@pulumi.input_type
class ApplicationMaximumAllowedResourcesArgs:
    def __init__(__self__, *,
                 cpu: pulumi.Input[str],
                 memory: pulumi.Input[str],
                 disk: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] cpu: Per worker CPU resource. vCPU is the only supported unit and specifying vCPU is optional.
        :param pulumi.Input[str] memory: Per worker memory resource. GB is the only supported unit and specifying GB is optional.
        :param pulumi.Input[str] disk: Per worker Disk resource. GB is the only supported unit and specifying GB is optional
        """
        ApplicationMaximumAllowedResourcesArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cpu=cpu,
            memory=memory,
            disk=disk,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cpu: pulumi.Input[str],
             memory: pulumi.Input[str],
             disk: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("cpu", cpu)
        _setter("memory", memory)
        if disk is not None:
            _setter("disk", disk)

    @property
    @pulumi.getter
    def cpu(self) -> pulumi.Input[str]:
        """
        Per worker CPU resource. vCPU is the only supported unit and specifying vCPU is optional.
        """
        return pulumi.get(self, "cpu")

    @cpu.setter
    def cpu(self, value: pulumi.Input[str]):
        pulumi.set(self, "cpu", value)

    @property
    @pulumi.getter
    def memory(self) -> pulumi.Input[str]:
        """
        Per worker memory resource. GB is the only supported unit and specifying GB is optional.
        """
        return pulumi.get(self, "memory")

    @memory.setter
    def memory(self, value: pulumi.Input[str]):
        pulumi.set(self, "memory", value)

    @property
    @pulumi.getter
    def disk(self) -> Optional[pulumi.Input[str]]:
        """
        Per worker Disk resource. GB is the only supported unit and specifying GB is optional
        """
        return pulumi.get(self, "disk")

    @disk.setter
    def disk(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disk", value)


@pulumi.input_type
class ApplicationNetworkConfigurationArgs:
    def __init__(__self__, *,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: The ID of the security groups in the VPC to which you want to connect your job or application.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: The ID of the subnets in the VPC to which you want to connect your job or application.
        """
        ApplicationNetworkConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            security_group_ids=security_group_ids,
            subnet_ids=subnet_ids,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if security_group_ids is not None:
            _setter("security_group_ids", security_group_ids)
        if subnet_ids is not None:
            _setter("subnet_ids", subnet_ids)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The ID of the security groups in the VPC to which you want to connect your job or application.
        """
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The ID of the subnets in the VPC to which you want to connect your job or application.
        """
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subnet_ids", value)


@pulumi.input_type
class ApplicationTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The value for the tag. You can specify a value that is 1 to 128 Unicode characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        ApplicationTagArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: pulumi.Input[str],
             value: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 1 to 128 Unicode characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ApplicationWorkerConfigurationArgs:
    def __init__(__self__, *,
                 cpu: pulumi.Input[str],
                 memory: pulumi.Input[str],
                 disk: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] cpu: Per worker CPU resource. vCPU is the only supported unit and specifying vCPU is optional.
        :param pulumi.Input[str] memory: Per worker memory resource. GB is the only supported unit and specifying GB is optional.
        :param pulumi.Input[str] disk: Per worker Disk resource. GB is the only supported unit and specifying GB is optional
        """
        ApplicationWorkerConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cpu=cpu,
            memory=memory,
            disk=disk,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cpu: pulumi.Input[str],
             memory: pulumi.Input[str],
             disk: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("cpu", cpu)
        _setter("memory", memory)
        if disk is not None:
            _setter("disk", disk)

    @property
    @pulumi.getter
    def cpu(self) -> pulumi.Input[str]:
        """
        Per worker CPU resource. vCPU is the only supported unit and specifying vCPU is optional.
        """
        return pulumi.get(self, "cpu")

    @cpu.setter
    def cpu(self, value: pulumi.Input[str]):
        pulumi.set(self, "cpu", value)

    @property
    @pulumi.getter
    def memory(self) -> pulumi.Input[str]:
        """
        Per worker memory resource. GB is the only supported unit and specifying GB is optional.
        """
        return pulumi.get(self, "memory")

    @memory.setter
    def memory(self, value: pulumi.Input[str]):
        pulumi.set(self, "memory", value)

    @property
    @pulumi.getter
    def disk(self) -> Optional[pulumi.Input[str]]:
        """
        Per worker Disk resource. GB is the only supported unit and specifying GB is optional
        """
        return pulumi.get(self, "disk")

    @disk.setter
    def disk(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disk", value)


@pulumi.input_type
class ApplicationWorkerTypeSpecificationInputMapArgs:
    def __init__(__self__):
        pass
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             opts: Optional[pulumi.ResourceOptions]=None):
        pass


