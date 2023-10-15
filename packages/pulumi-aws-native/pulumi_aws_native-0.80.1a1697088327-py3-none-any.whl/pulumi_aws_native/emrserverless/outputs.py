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

__all__ = [
    'ApplicationAutoStartConfiguration',
    'ApplicationAutoStopConfiguration',
    'ApplicationImageConfigurationInput',
    'ApplicationInitialCapacityConfig',
    'ApplicationInitialCapacityConfigKeyValuePair',
    'ApplicationMaximumAllowedResources',
    'ApplicationNetworkConfiguration',
    'ApplicationTag',
    'ApplicationWorkerConfiguration',
    'ApplicationWorkerTypeSpecificationInputMap',
]

@pulumi.output_type
class ApplicationAutoStartConfiguration(dict):
    """
    Configuration for Auto Start of Application
    """
    def __init__(__self__, *,
                 enabled: Optional[bool] = None):
        """
        Configuration for Auto Start of Application
        :param bool enabled: If set to true, the Application will automatically start. Defaults to true.
        """
        ApplicationAutoStartConfiguration._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            enabled=enabled,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             enabled: Optional[bool] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if enabled is not None:
            _setter("enabled", enabled)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        If set to true, the Application will automatically start. Defaults to true.
        """
        return pulumi.get(self, "enabled")


@pulumi.output_type
class ApplicationAutoStopConfiguration(dict):
    """
    Configuration for Auto Stop of Application
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "idleTimeoutMinutes":
            suggest = "idle_timeout_minutes"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationAutoStopConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationAutoStopConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationAutoStopConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enabled: Optional[bool] = None,
                 idle_timeout_minutes: Optional[int] = None):
        """
        Configuration for Auto Stop of Application
        :param bool enabled: If set to true, the Application will automatically stop after being idle. Defaults to true.
        :param int idle_timeout_minutes: The amount of time [in minutes] to wait before auto stopping the Application when idle. Defaults to 15 minutes.
        """
        ApplicationAutoStopConfiguration._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            enabled=enabled,
            idle_timeout_minutes=idle_timeout_minutes,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             enabled: Optional[bool] = None,
             idle_timeout_minutes: Optional[int] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if enabled is not None:
            _setter("enabled", enabled)
        if idle_timeout_minutes is not None:
            _setter("idle_timeout_minutes", idle_timeout_minutes)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        If set to true, the Application will automatically stop after being idle. Defaults to true.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="idleTimeoutMinutes")
    def idle_timeout_minutes(self) -> Optional[int]:
        """
        The amount of time [in minutes] to wait before auto stopping the Application when idle. Defaults to 15 minutes.
        """
        return pulumi.get(self, "idle_timeout_minutes")


@pulumi.output_type
class ApplicationImageConfigurationInput(dict):
    """
    The image configuration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "imageUri":
            suggest = "image_uri"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationImageConfigurationInput. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationImageConfigurationInput.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationImageConfigurationInput.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 image_uri: Optional[str] = None):
        """
        The image configuration.
        :param str image_uri: The URI of an image in the Amazon ECR registry. This field is required when you create a new application. If you leave this field blank in an update, Amazon EMR will remove the image configuration.
        """
        ApplicationImageConfigurationInput._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            image_uri=image_uri,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             image_uri: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if image_uri is not None:
            _setter("image_uri", image_uri)

    @property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> Optional[str]:
        """
        The URI of an image in the Amazon ECR registry. This field is required when you create a new application. If you leave this field blank in an update, Amazon EMR will remove the image configuration.
        """
        return pulumi.get(self, "image_uri")


@pulumi.output_type
class ApplicationInitialCapacityConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "workerConfiguration":
            suggest = "worker_configuration"
        elif key == "workerCount":
            suggest = "worker_count"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationInitialCapacityConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationInitialCapacityConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationInitialCapacityConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 worker_configuration: 'outputs.ApplicationWorkerConfiguration',
                 worker_count: int):
        """
        :param int worker_count: Initial count of workers to be initialized when an Application is started. This count will be continued to be maintained until the Application is stopped
        """
        ApplicationInitialCapacityConfig._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            worker_configuration=worker_configuration,
            worker_count=worker_count,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             worker_configuration: 'outputs.ApplicationWorkerConfiguration',
             worker_count: int,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("worker_configuration", worker_configuration)
        _setter("worker_count", worker_count)

    @property
    @pulumi.getter(name="workerConfiguration")
    def worker_configuration(self) -> 'outputs.ApplicationWorkerConfiguration':
        return pulumi.get(self, "worker_configuration")

    @property
    @pulumi.getter(name="workerCount")
    def worker_count(self) -> int:
        """
        Initial count of workers to be initialized when an Application is started. This count will be continued to be maintained until the Application is stopped
        """
        return pulumi.get(self, "worker_count")


@pulumi.output_type
class ApplicationInitialCapacityConfigKeyValuePair(dict):
    def __init__(__self__, *,
                 key: str,
                 value: 'outputs.ApplicationInitialCapacityConfig'):
        """
        :param str key: Worker type for an analytics framework.
        """
        ApplicationInitialCapacityConfigKeyValuePair._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: 'outputs.ApplicationInitialCapacityConfig',
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Worker type for an analytics framework.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> 'outputs.ApplicationInitialCapacityConfig':
        return pulumi.get(self, "value")


@pulumi.output_type
class ApplicationMaximumAllowedResources(dict):
    def __init__(__self__, *,
                 cpu: str,
                 memory: str,
                 disk: Optional[str] = None):
        """
        :param str cpu: Per worker CPU resource. vCPU is the only supported unit and specifying vCPU is optional.
        :param str memory: Per worker memory resource. GB is the only supported unit and specifying GB is optional.
        :param str disk: Per worker Disk resource. GB is the only supported unit and specifying GB is optional
        """
        ApplicationMaximumAllowedResources._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cpu=cpu,
            memory=memory,
            disk=disk,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cpu: str,
             memory: str,
             disk: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("cpu", cpu)
        _setter("memory", memory)
        if disk is not None:
            _setter("disk", disk)

    @property
    @pulumi.getter
    def cpu(self) -> str:
        """
        Per worker CPU resource. vCPU is the only supported unit and specifying vCPU is optional.
        """
        return pulumi.get(self, "cpu")

    @property
    @pulumi.getter
    def memory(self) -> str:
        """
        Per worker memory resource. GB is the only supported unit and specifying GB is optional.
        """
        return pulumi.get(self, "memory")

    @property
    @pulumi.getter
    def disk(self) -> Optional[str]:
        """
        Per worker Disk resource. GB is the only supported unit and specifying GB is optional
        """
        return pulumi.get(self, "disk")


@pulumi.output_type
class ApplicationNetworkConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "securityGroupIds":
            suggest = "security_group_ids"
        elif key == "subnetIds":
            suggest = "subnet_ids"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationNetworkConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationNetworkConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationNetworkConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 security_group_ids: Optional[Sequence[str]] = None,
                 subnet_ids: Optional[Sequence[str]] = None):
        """
        :param Sequence[str] security_group_ids: The ID of the security groups in the VPC to which you want to connect your job or application.
        :param Sequence[str] subnet_ids: The ID of the subnets in the VPC to which you want to connect your job or application.
        """
        ApplicationNetworkConfiguration._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            security_group_ids=security_group_ids,
            subnet_ids=subnet_ids,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             security_group_ids: Optional[Sequence[str]] = None,
             subnet_ids: Optional[Sequence[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if security_group_ids is not None:
            _setter("security_group_ids", security_group_ids)
        if subnet_ids is not None:
            _setter("subnet_ids", subnet_ids)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[str]]:
        """
        The ID of the security groups in the VPC to which you want to connect your job or application.
        """
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[Sequence[str]]:
        """
        The ID of the subnets in the VPC to which you want to connect your job or application.
        """
        return pulumi.get(self, "subnet_ids")


@pulumi.output_type
class ApplicationTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The value for the tag. You can specify a value that is 1 to 128 Unicode characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        :param str value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        ApplicationTag._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The value for the tag. You can specify a value that is 1 to 128 Unicode characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class ApplicationWorkerConfiguration(dict):
    def __init__(__self__, *,
                 cpu: str,
                 memory: str,
                 disk: Optional[str] = None):
        """
        :param str cpu: Per worker CPU resource. vCPU is the only supported unit and specifying vCPU is optional.
        :param str memory: Per worker memory resource. GB is the only supported unit and specifying GB is optional.
        :param str disk: Per worker Disk resource. GB is the only supported unit and specifying GB is optional
        """
        ApplicationWorkerConfiguration._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cpu=cpu,
            memory=memory,
            disk=disk,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cpu: str,
             memory: str,
             disk: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("cpu", cpu)
        _setter("memory", memory)
        if disk is not None:
            _setter("disk", disk)

    @property
    @pulumi.getter
    def cpu(self) -> str:
        """
        Per worker CPU resource. vCPU is the only supported unit and specifying vCPU is optional.
        """
        return pulumi.get(self, "cpu")

    @property
    @pulumi.getter
    def memory(self) -> str:
        """
        Per worker memory resource. GB is the only supported unit and specifying GB is optional.
        """
        return pulumi.get(self, "memory")

    @property
    @pulumi.getter
    def disk(self) -> Optional[str]:
        """
        Per worker Disk resource. GB is the only supported unit and specifying GB is optional
        """
        return pulumi.get(self, "disk")


@pulumi.output_type
class ApplicationWorkerTypeSpecificationInputMap(dict):
    def __init__(__self__):
        pass
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             opts: Optional[pulumi.ResourceOptions]=None):
        pass


