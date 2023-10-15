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

__all__ = ['ClusterArgs', 'Cluster']

@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *,
                 capacity_providers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 cluster_settings: Optional[pulumi.Input[Sequence[pulumi.Input['ClusterSettingsArgs']]]] = None,
                 configuration: Optional[pulumi.Input['ClusterConfigurationArgs']] = None,
                 default_capacity_provider_strategy: Optional[pulumi.Input[Sequence[pulumi.Input['ClusterCapacityProviderStrategyItemArgs']]]] = None,
                 service_connect_defaults: Optional[pulumi.Input['ClusterServiceConnectDefaultsArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ClusterTagArgs']]]] = None):
        """
        The set of arguments for constructing a Cluster resource.
        :param pulumi.Input[str] cluster_name: A user-generated string that you use to identify your cluster. If you don't specify a name, AWS CloudFormation generates a unique physical ID for the name.
        """
        ClusterArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            capacity_providers=capacity_providers,
            cluster_name=cluster_name,
            cluster_settings=cluster_settings,
            configuration=configuration,
            default_capacity_provider_strategy=default_capacity_provider_strategy,
            service_connect_defaults=service_connect_defaults,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             capacity_providers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             cluster_name: Optional[pulumi.Input[str]] = None,
             cluster_settings: Optional[pulumi.Input[Sequence[pulumi.Input['ClusterSettingsArgs']]]] = None,
             configuration: Optional[pulumi.Input['ClusterConfigurationArgs']] = None,
             default_capacity_provider_strategy: Optional[pulumi.Input[Sequence[pulumi.Input['ClusterCapacityProviderStrategyItemArgs']]]] = None,
             service_connect_defaults: Optional[pulumi.Input['ClusterServiceConnectDefaultsArgs']] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['ClusterTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if capacity_providers is not None:
            _setter("capacity_providers", capacity_providers)
        if cluster_name is not None:
            _setter("cluster_name", cluster_name)
        if cluster_settings is not None:
            _setter("cluster_settings", cluster_settings)
        if configuration is not None:
            _setter("configuration", configuration)
        if default_capacity_provider_strategy is not None:
            _setter("default_capacity_provider_strategy", default_capacity_provider_strategy)
        if service_connect_defaults is not None:
            _setter("service_connect_defaults", service_connect_defaults)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="capacityProviders")
    def capacity_providers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "capacity_providers")

    @capacity_providers.setter
    def capacity_providers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "capacity_providers", value)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[str]]:
        """
        A user-generated string that you use to identify your cluster. If you don't specify a name, AWS CloudFormation generates a unique physical ID for the name.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="clusterSettings")
    def cluster_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ClusterSettingsArgs']]]]:
        return pulumi.get(self, "cluster_settings")

    @cluster_settings.setter
    def cluster_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ClusterSettingsArgs']]]]):
        pulumi.set(self, "cluster_settings", value)

    @property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input['ClusterConfigurationArgs']]:
        return pulumi.get(self, "configuration")

    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input['ClusterConfigurationArgs']]):
        pulumi.set(self, "configuration", value)

    @property
    @pulumi.getter(name="defaultCapacityProviderStrategy")
    def default_capacity_provider_strategy(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ClusterCapacityProviderStrategyItemArgs']]]]:
        return pulumi.get(self, "default_capacity_provider_strategy")

    @default_capacity_provider_strategy.setter
    def default_capacity_provider_strategy(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ClusterCapacityProviderStrategyItemArgs']]]]):
        pulumi.set(self, "default_capacity_provider_strategy", value)

    @property
    @pulumi.getter(name="serviceConnectDefaults")
    def service_connect_defaults(self) -> Optional[pulumi.Input['ClusterServiceConnectDefaultsArgs']]:
        return pulumi.get(self, "service_connect_defaults")

    @service_connect_defaults.setter
    def service_connect_defaults(self, value: Optional[pulumi.Input['ClusterServiceConnectDefaultsArgs']]):
        pulumi.set(self, "service_connect_defaults", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ClusterTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ClusterTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capacity_providers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 cluster_settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterSettingsArgs']]]]] = None,
                 configuration: Optional[pulumi.Input[pulumi.InputType['ClusterConfigurationArgs']]] = None,
                 default_capacity_provider_strategy: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterCapacityProviderStrategyItemArgs']]]]] = None,
                 service_connect_defaults: Optional[pulumi.Input[pulumi.InputType['ClusterServiceConnectDefaultsArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterTagArgs']]]]] = None,
                 __props__=None):
        """
        Create an Elastic Container Service (ECS) cluster.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: A user-generated string that you use to identify your cluster. If you don't specify a name, AWS CloudFormation generates a unique physical ID for the name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ClusterArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create an Elastic Container Service (ECS) cluster.

        :param str resource_name: The name of the resource.
        :param ClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ClusterArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capacity_providers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 cluster_settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterSettingsArgs']]]]] = None,
                 configuration: Optional[pulumi.Input[pulumi.InputType['ClusterConfigurationArgs']]] = None,
                 default_capacity_provider_strategy: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterCapacityProviderStrategyItemArgs']]]]] = None,
                 service_connect_defaults: Optional[pulumi.Input[pulumi.InputType['ClusterServiceConnectDefaultsArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterArgs.__new__(ClusterArgs)

            __props__.__dict__["capacity_providers"] = capacity_providers
            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["cluster_settings"] = cluster_settings
            if configuration is not None and not isinstance(configuration, ClusterConfigurationArgs):
                configuration = configuration or {}
                def _setter(key, value):
                    configuration[key] = value
                ClusterConfigurationArgs._configure(_setter, **configuration)
            __props__.__dict__["configuration"] = configuration
            __props__.__dict__["default_capacity_provider_strategy"] = default_capacity_provider_strategy
            if service_connect_defaults is not None and not isinstance(service_connect_defaults, ClusterServiceConnectDefaultsArgs):
                service_connect_defaults = service_connect_defaults or {}
                def _setter(key, value):
                    service_connect_defaults[key] = value
                ClusterServiceConnectDefaultsArgs._configure(_setter, **service_connect_defaults)
            __props__.__dict__["service_connect_defaults"] = service_connect_defaults
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["cluster_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Cluster, __self__).__init__(
            'aws-native:ecs:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Cluster':
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ClusterArgs.__new__(ClusterArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["capacity_providers"] = None
        __props__.__dict__["cluster_name"] = None
        __props__.__dict__["cluster_settings"] = None
        __props__.__dict__["configuration"] = None
        __props__.__dict__["default_capacity_provider_strategy"] = None
        __props__.__dict__["service_connect_defaults"] = None
        __props__.__dict__["tags"] = None
        return Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the Amazon ECS cluster, such as arn:aws:ecs:us-east-2:123456789012:cluster/MyECSCluster.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="capacityProviders")
    def capacity_providers(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "capacity_providers")

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[Optional[str]]:
        """
        A user-generated string that you use to identify your cluster. If you don't specify a name, AWS CloudFormation generates a unique physical ID for the name.
        """
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="clusterSettings")
    def cluster_settings(self) -> pulumi.Output[Optional[Sequence['outputs.ClusterSettings']]]:
        return pulumi.get(self, "cluster_settings")

    @property
    @pulumi.getter
    def configuration(self) -> pulumi.Output[Optional['outputs.ClusterConfiguration']]:
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter(name="defaultCapacityProviderStrategy")
    def default_capacity_provider_strategy(self) -> pulumi.Output[Optional[Sequence['outputs.ClusterCapacityProviderStrategyItem']]]:
        return pulumi.get(self, "default_capacity_provider_strategy")

    @property
    @pulumi.getter(name="serviceConnectDefaults")
    def service_connect_defaults(self) -> pulumi.Output[Optional['outputs.ClusterServiceConnectDefaults']]:
        return pulumi.get(self, "service_connect_defaults")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ClusterTag']]]:
        return pulumi.get(self, "tags")

