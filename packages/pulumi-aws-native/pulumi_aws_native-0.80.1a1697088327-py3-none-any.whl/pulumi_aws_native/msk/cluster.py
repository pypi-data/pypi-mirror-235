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

__all__ = ['ClusterArgs', 'Cluster']

@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *,
                 broker_node_group_info: pulumi.Input['ClusterBrokerNodeGroupInfoArgs'],
                 kafka_version: pulumi.Input[str],
                 number_of_broker_nodes: pulumi.Input[int],
                 client_authentication: Optional[pulumi.Input['ClusterClientAuthenticationArgs']] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 configuration_info: Optional[pulumi.Input['ClusterConfigurationInfoArgs']] = None,
                 current_version: Optional[pulumi.Input[str]] = None,
                 encryption_info: Optional[pulumi.Input['ClusterEncryptionInfoArgs']] = None,
                 enhanced_monitoring: Optional[pulumi.Input['ClusterEnhancedMonitoring']] = None,
                 logging_info: Optional[pulumi.Input['ClusterLoggingInfoArgs']] = None,
                 open_monitoring: Optional[pulumi.Input['ClusterOpenMonitoringArgs']] = None,
                 storage_mode: Optional[pulumi.Input['ClusterStorageMode']] = None,
                 tags: Optional[Any] = None):
        """
        The set of arguments for constructing a Cluster resource.
        :param pulumi.Input[str] current_version: The current version of the MSK cluster
        :param Any tags: A key-value pair to associate with a resource.
        """
        ClusterArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            broker_node_group_info=broker_node_group_info,
            kafka_version=kafka_version,
            number_of_broker_nodes=number_of_broker_nodes,
            client_authentication=client_authentication,
            cluster_name=cluster_name,
            configuration_info=configuration_info,
            current_version=current_version,
            encryption_info=encryption_info,
            enhanced_monitoring=enhanced_monitoring,
            logging_info=logging_info,
            open_monitoring=open_monitoring,
            storage_mode=storage_mode,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             broker_node_group_info: pulumi.Input['ClusterBrokerNodeGroupInfoArgs'],
             kafka_version: pulumi.Input[str],
             number_of_broker_nodes: pulumi.Input[int],
             client_authentication: Optional[pulumi.Input['ClusterClientAuthenticationArgs']] = None,
             cluster_name: Optional[pulumi.Input[str]] = None,
             configuration_info: Optional[pulumi.Input['ClusterConfigurationInfoArgs']] = None,
             current_version: Optional[pulumi.Input[str]] = None,
             encryption_info: Optional[pulumi.Input['ClusterEncryptionInfoArgs']] = None,
             enhanced_monitoring: Optional[pulumi.Input['ClusterEnhancedMonitoring']] = None,
             logging_info: Optional[pulumi.Input['ClusterLoggingInfoArgs']] = None,
             open_monitoring: Optional[pulumi.Input['ClusterOpenMonitoringArgs']] = None,
             storage_mode: Optional[pulumi.Input['ClusterStorageMode']] = None,
             tags: Optional[Any] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("broker_node_group_info", broker_node_group_info)
        _setter("kafka_version", kafka_version)
        _setter("number_of_broker_nodes", number_of_broker_nodes)
        if client_authentication is not None:
            _setter("client_authentication", client_authentication)
        if cluster_name is not None:
            _setter("cluster_name", cluster_name)
        if configuration_info is not None:
            _setter("configuration_info", configuration_info)
        if current_version is not None:
            _setter("current_version", current_version)
        if encryption_info is not None:
            _setter("encryption_info", encryption_info)
        if enhanced_monitoring is not None:
            _setter("enhanced_monitoring", enhanced_monitoring)
        if logging_info is not None:
            _setter("logging_info", logging_info)
        if open_monitoring is not None:
            _setter("open_monitoring", open_monitoring)
        if storage_mode is not None:
            _setter("storage_mode", storage_mode)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="brokerNodeGroupInfo")
    def broker_node_group_info(self) -> pulumi.Input['ClusterBrokerNodeGroupInfoArgs']:
        return pulumi.get(self, "broker_node_group_info")

    @broker_node_group_info.setter
    def broker_node_group_info(self, value: pulumi.Input['ClusterBrokerNodeGroupInfoArgs']):
        pulumi.set(self, "broker_node_group_info", value)

    @property
    @pulumi.getter(name="kafkaVersion")
    def kafka_version(self) -> pulumi.Input[str]:
        return pulumi.get(self, "kafka_version")

    @kafka_version.setter
    def kafka_version(self, value: pulumi.Input[str]):
        pulumi.set(self, "kafka_version", value)

    @property
    @pulumi.getter(name="numberOfBrokerNodes")
    def number_of_broker_nodes(self) -> pulumi.Input[int]:
        return pulumi.get(self, "number_of_broker_nodes")

    @number_of_broker_nodes.setter
    def number_of_broker_nodes(self, value: pulumi.Input[int]):
        pulumi.set(self, "number_of_broker_nodes", value)

    @property
    @pulumi.getter(name="clientAuthentication")
    def client_authentication(self) -> Optional[pulumi.Input['ClusterClientAuthenticationArgs']]:
        return pulumi.get(self, "client_authentication")

    @client_authentication.setter
    def client_authentication(self, value: Optional[pulumi.Input['ClusterClientAuthenticationArgs']]):
        pulumi.set(self, "client_authentication", value)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="configurationInfo")
    def configuration_info(self) -> Optional[pulumi.Input['ClusterConfigurationInfoArgs']]:
        return pulumi.get(self, "configuration_info")

    @configuration_info.setter
    def configuration_info(self, value: Optional[pulumi.Input['ClusterConfigurationInfoArgs']]):
        pulumi.set(self, "configuration_info", value)

    @property
    @pulumi.getter(name="currentVersion")
    def current_version(self) -> Optional[pulumi.Input[str]]:
        """
        The current version of the MSK cluster
        """
        return pulumi.get(self, "current_version")

    @current_version.setter
    def current_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "current_version", value)

    @property
    @pulumi.getter(name="encryptionInfo")
    def encryption_info(self) -> Optional[pulumi.Input['ClusterEncryptionInfoArgs']]:
        return pulumi.get(self, "encryption_info")

    @encryption_info.setter
    def encryption_info(self, value: Optional[pulumi.Input['ClusterEncryptionInfoArgs']]):
        pulumi.set(self, "encryption_info", value)

    @property
    @pulumi.getter(name="enhancedMonitoring")
    def enhanced_monitoring(self) -> Optional[pulumi.Input['ClusterEnhancedMonitoring']]:
        return pulumi.get(self, "enhanced_monitoring")

    @enhanced_monitoring.setter
    def enhanced_monitoring(self, value: Optional[pulumi.Input['ClusterEnhancedMonitoring']]):
        pulumi.set(self, "enhanced_monitoring", value)

    @property
    @pulumi.getter(name="loggingInfo")
    def logging_info(self) -> Optional[pulumi.Input['ClusterLoggingInfoArgs']]:
        return pulumi.get(self, "logging_info")

    @logging_info.setter
    def logging_info(self, value: Optional[pulumi.Input['ClusterLoggingInfoArgs']]):
        pulumi.set(self, "logging_info", value)

    @property
    @pulumi.getter(name="openMonitoring")
    def open_monitoring(self) -> Optional[pulumi.Input['ClusterOpenMonitoringArgs']]:
        return pulumi.get(self, "open_monitoring")

    @open_monitoring.setter
    def open_monitoring(self, value: Optional[pulumi.Input['ClusterOpenMonitoringArgs']]):
        pulumi.set(self, "open_monitoring", value)

    @property
    @pulumi.getter(name="storageMode")
    def storage_mode(self) -> Optional[pulumi.Input['ClusterStorageMode']]:
        return pulumi.get(self, "storage_mode")

    @storage_mode.setter
    def storage_mode(self, value: Optional[pulumi.Input['ClusterStorageMode']]):
        pulumi.set(self, "storage_mode", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        A key-value pair to associate with a resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[Any]):
        pulumi.set(self, "tags", value)


class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 broker_node_group_info: Optional[pulumi.Input[pulumi.InputType['ClusterBrokerNodeGroupInfoArgs']]] = None,
                 client_authentication: Optional[pulumi.Input[pulumi.InputType['ClusterClientAuthenticationArgs']]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 configuration_info: Optional[pulumi.Input[pulumi.InputType['ClusterConfigurationInfoArgs']]] = None,
                 current_version: Optional[pulumi.Input[str]] = None,
                 encryption_info: Optional[pulumi.Input[pulumi.InputType['ClusterEncryptionInfoArgs']]] = None,
                 enhanced_monitoring: Optional[pulumi.Input['ClusterEnhancedMonitoring']] = None,
                 kafka_version: Optional[pulumi.Input[str]] = None,
                 logging_info: Optional[pulumi.Input[pulumi.InputType['ClusterLoggingInfoArgs']]] = None,
                 number_of_broker_nodes: Optional[pulumi.Input[int]] = None,
                 open_monitoring: Optional[pulumi.Input[pulumi.InputType['ClusterOpenMonitoringArgs']]] = None,
                 storage_mode: Optional[pulumi.Input['ClusterStorageMode']] = None,
                 tags: Optional[Any] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::MSK::Cluster

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] current_version: The current version of the MSK cluster
        :param Any tags: A key-value pair to associate with a resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::MSK::Cluster

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
                 broker_node_group_info: Optional[pulumi.Input[pulumi.InputType['ClusterBrokerNodeGroupInfoArgs']]] = None,
                 client_authentication: Optional[pulumi.Input[pulumi.InputType['ClusterClientAuthenticationArgs']]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 configuration_info: Optional[pulumi.Input[pulumi.InputType['ClusterConfigurationInfoArgs']]] = None,
                 current_version: Optional[pulumi.Input[str]] = None,
                 encryption_info: Optional[pulumi.Input[pulumi.InputType['ClusterEncryptionInfoArgs']]] = None,
                 enhanced_monitoring: Optional[pulumi.Input['ClusterEnhancedMonitoring']] = None,
                 kafka_version: Optional[pulumi.Input[str]] = None,
                 logging_info: Optional[pulumi.Input[pulumi.InputType['ClusterLoggingInfoArgs']]] = None,
                 number_of_broker_nodes: Optional[pulumi.Input[int]] = None,
                 open_monitoring: Optional[pulumi.Input[pulumi.InputType['ClusterOpenMonitoringArgs']]] = None,
                 storage_mode: Optional[pulumi.Input['ClusterStorageMode']] = None,
                 tags: Optional[Any] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterArgs.__new__(ClusterArgs)

            if broker_node_group_info is not None and not isinstance(broker_node_group_info, ClusterBrokerNodeGroupInfoArgs):
                broker_node_group_info = broker_node_group_info or {}
                def _setter(key, value):
                    broker_node_group_info[key] = value
                ClusterBrokerNodeGroupInfoArgs._configure(_setter, **broker_node_group_info)
            if broker_node_group_info is None and not opts.urn:
                raise TypeError("Missing required property 'broker_node_group_info'")
            __props__.__dict__["broker_node_group_info"] = broker_node_group_info
            if client_authentication is not None and not isinstance(client_authentication, ClusterClientAuthenticationArgs):
                client_authentication = client_authentication or {}
                def _setter(key, value):
                    client_authentication[key] = value
                ClusterClientAuthenticationArgs._configure(_setter, **client_authentication)
            __props__.__dict__["client_authentication"] = client_authentication
            __props__.__dict__["cluster_name"] = cluster_name
            if configuration_info is not None and not isinstance(configuration_info, ClusterConfigurationInfoArgs):
                configuration_info = configuration_info or {}
                def _setter(key, value):
                    configuration_info[key] = value
                ClusterConfigurationInfoArgs._configure(_setter, **configuration_info)
            __props__.__dict__["configuration_info"] = configuration_info
            __props__.__dict__["current_version"] = current_version
            if encryption_info is not None and not isinstance(encryption_info, ClusterEncryptionInfoArgs):
                encryption_info = encryption_info or {}
                def _setter(key, value):
                    encryption_info[key] = value
                ClusterEncryptionInfoArgs._configure(_setter, **encryption_info)
            __props__.__dict__["encryption_info"] = encryption_info
            __props__.__dict__["enhanced_monitoring"] = enhanced_monitoring
            if kafka_version is None and not opts.urn:
                raise TypeError("Missing required property 'kafka_version'")
            __props__.__dict__["kafka_version"] = kafka_version
            if logging_info is not None and not isinstance(logging_info, ClusterLoggingInfoArgs):
                logging_info = logging_info or {}
                def _setter(key, value):
                    logging_info[key] = value
                ClusterLoggingInfoArgs._configure(_setter, **logging_info)
            __props__.__dict__["logging_info"] = logging_info
            if number_of_broker_nodes is None and not opts.urn:
                raise TypeError("Missing required property 'number_of_broker_nodes'")
            __props__.__dict__["number_of_broker_nodes"] = number_of_broker_nodes
            if open_monitoring is not None and not isinstance(open_monitoring, ClusterOpenMonitoringArgs):
                open_monitoring = open_monitoring or {}
                def _setter(key, value):
                    open_monitoring[key] = value
                ClusterOpenMonitoringArgs._configure(_setter, **open_monitoring)
            __props__.__dict__["open_monitoring"] = open_monitoring
            __props__.__dict__["storage_mode"] = storage_mode
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["broker_node_group_info.broker_az_distribution", "broker_node_group_info.client_subnets[*]", "broker_node_group_info.security_groups[*]", "cluster_name", "encryption_info.encryption_at_rest", "encryption_info.encryption_in_transit.in_cluster"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Cluster, __self__).__init__(
            'aws-native:msk:Cluster',
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
        __props__.__dict__["broker_node_group_info"] = None
        __props__.__dict__["client_authentication"] = None
        __props__.__dict__["cluster_name"] = None
        __props__.__dict__["configuration_info"] = None
        __props__.__dict__["current_version"] = None
        __props__.__dict__["encryption_info"] = None
        __props__.__dict__["enhanced_monitoring"] = None
        __props__.__dict__["kafka_version"] = None
        __props__.__dict__["logging_info"] = None
        __props__.__dict__["number_of_broker_nodes"] = None
        __props__.__dict__["open_monitoring"] = None
        __props__.__dict__["storage_mode"] = None
        __props__.__dict__["tags"] = None
        return Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="brokerNodeGroupInfo")
    def broker_node_group_info(self) -> pulumi.Output['outputs.ClusterBrokerNodeGroupInfo']:
        return pulumi.get(self, "broker_node_group_info")

    @property
    @pulumi.getter(name="clientAuthentication")
    def client_authentication(self) -> pulumi.Output[Optional['outputs.ClusterClientAuthentication']]:
        return pulumi.get(self, "client_authentication")

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="configurationInfo")
    def configuration_info(self) -> pulumi.Output[Optional['outputs.ClusterConfigurationInfo']]:
        return pulumi.get(self, "configuration_info")

    @property
    @pulumi.getter(name="currentVersion")
    def current_version(self) -> pulumi.Output[Optional[str]]:
        """
        The current version of the MSK cluster
        """
        return pulumi.get(self, "current_version")

    @property
    @pulumi.getter(name="encryptionInfo")
    def encryption_info(self) -> pulumi.Output[Optional['outputs.ClusterEncryptionInfo']]:
        return pulumi.get(self, "encryption_info")

    @property
    @pulumi.getter(name="enhancedMonitoring")
    def enhanced_monitoring(self) -> pulumi.Output[Optional['ClusterEnhancedMonitoring']]:
        return pulumi.get(self, "enhanced_monitoring")

    @property
    @pulumi.getter(name="kafkaVersion")
    def kafka_version(self) -> pulumi.Output[str]:
        return pulumi.get(self, "kafka_version")

    @property
    @pulumi.getter(name="loggingInfo")
    def logging_info(self) -> pulumi.Output[Optional['outputs.ClusterLoggingInfo']]:
        return pulumi.get(self, "logging_info")

    @property
    @pulumi.getter(name="numberOfBrokerNodes")
    def number_of_broker_nodes(self) -> pulumi.Output[int]:
        return pulumi.get(self, "number_of_broker_nodes")

    @property
    @pulumi.getter(name="openMonitoring")
    def open_monitoring(self) -> pulumi.Output[Optional['outputs.ClusterOpenMonitoring']]:
        return pulumi.get(self, "open_monitoring")

    @property
    @pulumi.getter(name="storageMode")
    def storage_mode(self) -> pulumi.Output[Optional['ClusterStorageMode']]:
        return pulumi.get(self, "storage_mode")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Any]]:
        """
        A key-value pair to associate with a resource.
        """
        return pulumi.get(self, "tags")

