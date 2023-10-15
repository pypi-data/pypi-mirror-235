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
    'ApplicationApiGatewayProxyInputArgs',
    'ApplicationTagArgs',
    'EnvironmentTagArgs',
    'RouteDefaultRouteInputArgs',
    'RouteTagArgs',
    'RouteUriPathRouteInputArgs',
    'ServiceLambdaEndpointInputArgs',
    'ServiceTagArgs',
    'ServiceUrlEndpointInputArgs',
]

@pulumi.input_type
class ApplicationApiGatewayProxyInputArgs:
    def __init__(__self__, *,
                 endpoint_type: Optional[pulumi.Input['ApplicationApiGatewayEndpointType']] = None,
                 stage_name: Optional[pulumi.Input[str]] = None):
        ApplicationApiGatewayProxyInputArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            endpoint_type=endpoint_type,
            stage_name=stage_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             endpoint_type: Optional[pulumi.Input['ApplicationApiGatewayEndpointType']] = None,
             stage_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if endpoint_type is not None:
            _setter("endpoint_type", endpoint_type)
        if stage_name is not None:
            _setter("stage_name", stage_name)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[pulumi.Input['ApplicationApiGatewayEndpointType']]:
        return pulumi.get(self, "endpoint_type")

    @endpoint_type.setter
    def endpoint_type(self, value: Optional[pulumi.Input['ApplicationApiGatewayEndpointType']]):
        pulumi.set(self, "endpoint_type", value)

    @property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "stage_name")

    @stage_name.setter
    def stage_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stage_name", value)


@pulumi.input_type
class ApplicationTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A label for tagging Environment resource
        :param pulumi.Input[str] key: A string used to identify this tag
        :param pulumi.Input[str] value: A string containing the value for the tag
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
        A string used to identify this tag
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        A string containing the value for the tag
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class EnvironmentTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A label for tagging Environment resource
        :param pulumi.Input[str] key: A string used to identify this tag
        :param pulumi.Input[str] value: A string containing the value for the tag
        """
        EnvironmentTagArgs._configure(
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
        A string used to identify this tag
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        A string containing the value for the tag
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class RouteDefaultRouteInputArgs:
    def __init__(__self__, *,
                 activation_state: pulumi.Input['RouteActivationState']):
        RouteDefaultRouteInputArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            activation_state=activation_state,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             activation_state: pulumi.Input['RouteActivationState'],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("activation_state", activation_state)

    @property
    @pulumi.getter(name="activationState")
    def activation_state(self) -> pulumi.Input['RouteActivationState']:
        return pulumi.get(self, "activation_state")

    @activation_state.setter
    def activation_state(self, value: pulumi.Input['RouteActivationState']):
        pulumi.set(self, "activation_state", value)


@pulumi.input_type
class RouteTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A label for tagging Environment resource
        :param pulumi.Input[str] key: A string used to identify this tag
        :param pulumi.Input[str] value: A string containing the value for the tag
        """
        RouteTagArgs._configure(
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
        A string used to identify this tag
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        A string containing the value for the tag
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class RouteUriPathRouteInputArgs:
    def __init__(__self__, *,
                 activation_state: pulumi.Input['RouteActivationState'],
                 append_source_path: Optional[pulumi.Input[bool]] = None,
                 include_child_paths: Optional[pulumi.Input[bool]] = None,
                 methods: Optional[pulumi.Input[Sequence[pulumi.Input['RouteMethod']]]] = None,
                 source_path: Optional[pulumi.Input[str]] = None):
        RouteUriPathRouteInputArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            activation_state=activation_state,
            append_source_path=append_source_path,
            include_child_paths=include_child_paths,
            methods=methods,
            source_path=source_path,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             activation_state: pulumi.Input['RouteActivationState'],
             append_source_path: Optional[pulumi.Input[bool]] = None,
             include_child_paths: Optional[pulumi.Input[bool]] = None,
             methods: Optional[pulumi.Input[Sequence[pulumi.Input['RouteMethod']]]] = None,
             source_path: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("activation_state", activation_state)
        if append_source_path is not None:
            _setter("append_source_path", append_source_path)
        if include_child_paths is not None:
            _setter("include_child_paths", include_child_paths)
        if methods is not None:
            _setter("methods", methods)
        if source_path is not None:
            _setter("source_path", source_path)

    @property
    @pulumi.getter(name="activationState")
    def activation_state(self) -> pulumi.Input['RouteActivationState']:
        return pulumi.get(self, "activation_state")

    @activation_state.setter
    def activation_state(self, value: pulumi.Input['RouteActivationState']):
        pulumi.set(self, "activation_state", value)

    @property
    @pulumi.getter(name="appendSourcePath")
    def append_source_path(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "append_source_path")

    @append_source_path.setter
    def append_source_path(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "append_source_path", value)

    @property
    @pulumi.getter(name="includeChildPaths")
    def include_child_paths(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "include_child_paths")

    @include_child_paths.setter
    def include_child_paths(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_child_paths", value)

    @property
    @pulumi.getter
    def methods(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RouteMethod']]]]:
        return pulumi.get(self, "methods")

    @methods.setter
    def methods(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RouteMethod']]]]):
        pulumi.set(self, "methods", value)

    @property
    @pulumi.getter(name="sourcePath")
    def source_path(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source_path")

    @source_path.setter
    def source_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_path", value)


@pulumi.input_type
class ServiceLambdaEndpointInputArgs:
    def __init__(__self__, *,
                 arn: pulumi.Input[str]):
        ServiceLambdaEndpointInputArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            arn=arn,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             arn: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("arn", arn)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "arn", value)


@pulumi.input_type
class ServiceTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A label for tagging Environment resource
        :param pulumi.Input[str] key: A string used to identify this tag
        :param pulumi.Input[str] value: A string containing the value for the tag
        """
        ServiceTagArgs._configure(
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
        A string used to identify this tag
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        A string containing the value for the tag
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ServiceUrlEndpointInputArgs:
    def __init__(__self__, *,
                 url: pulumi.Input[str],
                 health_url: Optional[pulumi.Input[str]] = None):
        ServiceUrlEndpointInputArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            url=url,
            health_url=health_url,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             url: pulumi.Input[str],
             health_url: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("url", url)
        if health_url is not None:
            _setter("health_url", health_url)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter(name="healthUrl")
    def health_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "health_url")

    @health_url.setter
    def health_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "health_url", value)


