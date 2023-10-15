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

__all__ = ['GlobalReplicationGroupArgs', 'GlobalReplicationGroup']

@pulumi.input_type
class GlobalReplicationGroupArgs:
    def __init__(__self__, *,
                 members: pulumi.Input[Sequence[pulumi.Input['GlobalReplicationGroupMemberArgs']]],
                 automatic_failover_enabled: Optional[pulumi.Input[bool]] = None,
                 cache_node_type: Optional[pulumi.Input[str]] = None,
                 cache_parameter_group_name: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 global_node_group_count: Optional[pulumi.Input[int]] = None,
                 global_replication_group_description: Optional[pulumi.Input[str]] = None,
                 global_replication_group_id_suffix: Optional[pulumi.Input[str]] = None,
                 regional_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['GlobalReplicationGroupRegionalConfigurationArgs']]]] = None):
        """
        The set of arguments for constructing a GlobalReplicationGroup resource.
        :param pulumi.Input[Sequence[pulumi.Input['GlobalReplicationGroupMemberArgs']]] members: The replication groups that comprise the Global Datastore.
        :param pulumi.Input[bool] automatic_failover_enabled: AutomaticFailoverEnabled
        :param pulumi.Input[str] cache_node_type: The cache node type of the Global Datastore
        :param pulumi.Input[str] cache_parameter_group_name: Cache parameter group name to use for the new engine version. This parameter cannot be modified independently.
        :param pulumi.Input[str] engine_version: The engine version of the Global Datastore.
        :param pulumi.Input[int] global_node_group_count: Indicates the number of node groups in the Global Datastore.
        :param pulumi.Input[str] global_replication_group_description: The optional description of the Global Datastore
        :param pulumi.Input[str] global_replication_group_id_suffix: The suffix name of a Global Datastore. Amazon ElastiCache automatically applies a prefix to the Global Datastore ID when it is created. Each AWS Region has its own prefix. 
        :param pulumi.Input[Sequence[pulumi.Input['GlobalReplicationGroupRegionalConfigurationArgs']]] regional_configurations: Describes the replication group IDs, the AWS regions where they are stored and the shard configuration for each that comprise the Global Datastore 
        """
        GlobalReplicationGroupArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            members=members,
            automatic_failover_enabled=automatic_failover_enabled,
            cache_node_type=cache_node_type,
            cache_parameter_group_name=cache_parameter_group_name,
            engine_version=engine_version,
            global_node_group_count=global_node_group_count,
            global_replication_group_description=global_replication_group_description,
            global_replication_group_id_suffix=global_replication_group_id_suffix,
            regional_configurations=regional_configurations,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             members: pulumi.Input[Sequence[pulumi.Input['GlobalReplicationGroupMemberArgs']]],
             automatic_failover_enabled: Optional[pulumi.Input[bool]] = None,
             cache_node_type: Optional[pulumi.Input[str]] = None,
             cache_parameter_group_name: Optional[pulumi.Input[str]] = None,
             engine_version: Optional[pulumi.Input[str]] = None,
             global_node_group_count: Optional[pulumi.Input[int]] = None,
             global_replication_group_description: Optional[pulumi.Input[str]] = None,
             global_replication_group_id_suffix: Optional[pulumi.Input[str]] = None,
             regional_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['GlobalReplicationGroupRegionalConfigurationArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("members", members)
        if automatic_failover_enabled is not None:
            _setter("automatic_failover_enabled", automatic_failover_enabled)
        if cache_node_type is not None:
            _setter("cache_node_type", cache_node_type)
        if cache_parameter_group_name is not None:
            _setter("cache_parameter_group_name", cache_parameter_group_name)
        if engine_version is not None:
            _setter("engine_version", engine_version)
        if global_node_group_count is not None:
            _setter("global_node_group_count", global_node_group_count)
        if global_replication_group_description is not None:
            _setter("global_replication_group_description", global_replication_group_description)
        if global_replication_group_id_suffix is not None:
            _setter("global_replication_group_id_suffix", global_replication_group_id_suffix)
        if regional_configurations is not None:
            _setter("regional_configurations", regional_configurations)

    @property
    @pulumi.getter
    def members(self) -> pulumi.Input[Sequence[pulumi.Input['GlobalReplicationGroupMemberArgs']]]:
        """
        The replication groups that comprise the Global Datastore.
        """
        return pulumi.get(self, "members")

    @members.setter
    def members(self, value: pulumi.Input[Sequence[pulumi.Input['GlobalReplicationGroupMemberArgs']]]):
        pulumi.set(self, "members", value)

    @property
    @pulumi.getter(name="automaticFailoverEnabled")
    def automatic_failover_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        AutomaticFailoverEnabled
        """
        return pulumi.get(self, "automatic_failover_enabled")

    @automatic_failover_enabled.setter
    def automatic_failover_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "automatic_failover_enabled", value)

    @property
    @pulumi.getter(name="cacheNodeType")
    def cache_node_type(self) -> Optional[pulumi.Input[str]]:
        """
        The cache node type of the Global Datastore
        """
        return pulumi.get(self, "cache_node_type")

    @cache_node_type.setter
    def cache_node_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cache_node_type", value)

    @property
    @pulumi.getter(name="cacheParameterGroupName")
    def cache_parameter_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Cache parameter group name to use for the new engine version. This parameter cannot be modified independently.
        """
        return pulumi.get(self, "cache_parameter_group_name")

    @cache_parameter_group_name.setter
    def cache_parameter_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cache_parameter_group_name", value)

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[str]]:
        """
        The engine version of the Global Datastore.
        """
        return pulumi.get(self, "engine_version")

    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "engine_version", value)

    @property
    @pulumi.getter(name="globalNodeGroupCount")
    def global_node_group_count(self) -> Optional[pulumi.Input[int]]:
        """
        Indicates the number of node groups in the Global Datastore.
        """
        return pulumi.get(self, "global_node_group_count")

    @global_node_group_count.setter
    def global_node_group_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "global_node_group_count", value)

    @property
    @pulumi.getter(name="globalReplicationGroupDescription")
    def global_replication_group_description(self) -> Optional[pulumi.Input[str]]:
        """
        The optional description of the Global Datastore
        """
        return pulumi.get(self, "global_replication_group_description")

    @global_replication_group_description.setter
    def global_replication_group_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "global_replication_group_description", value)

    @property
    @pulumi.getter(name="globalReplicationGroupIdSuffix")
    def global_replication_group_id_suffix(self) -> Optional[pulumi.Input[str]]:
        """
        The suffix name of a Global Datastore. Amazon ElastiCache automatically applies a prefix to the Global Datastore ID when it is created. Each AWS Region has its own prefix. 
        """
        return pulumi.get(self, "global_replication_group_id_suffix")

    @global_replication_group_id_suffix.setter
    def global_replication_group_id_suffix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "global_replication_group_id_suffix", value)

    @property
    @pulumi.getter(name="regionalConfigurations")
    def regional_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GlobalReplicationGroupRegionalConfigurationArgs']]]]:
        """
        Describes the replication group IDs, the AWS regions where they are stored and the shard configuration for each that comprise the Global Datastore 
        """
        return pulumi.get(self, "regional_configurations")

    @regional_configurations.setter
    def regional_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GlobalReplicationGroupRegionalConfigurationArgs']]]]):
        pulumi.set(self, "regional_configurations", value)


class GlobalReplicationGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automatic_failover_enabled: Optional[pulumi.Input[bool]] = None,
                 cache_node_type: Optional[pulumi.Input[str]] = None,
                 cache_parameter_group_name: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 global_node_group_count: Optional[pulumi.Input[int]] = None,
                 global_replication_group_description: Optional[pulumi.Input[str]] = None,
                 global_replication_group_id_suffix: Optional[pulumi.Input[str]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GlobalReplicationGroupMemberArgs']]]]] = None,
                 regional_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GlobalReplicationGroupRegionalConfigurationArgs']]]]] = None,
                 __props__=None):
        """
        The AWS::ElastiCache::GlobalReplicationGroup resource creates an Amazon ElastiCache Global Replication Group.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] automatic_failover_enabled: AutomaticFailoverEnabled
        :param pulumi.Input[str] cache_node_type: The cache node type of the Global Datastore
        :param pulumi.Input[str] cache_parameter_group_name: Cache parameter group name to use for the new engine version. This parameter cannot be modified independently.
        :param pulumi.Input[str] engine_version: The engine version of the Global Datastore.
        :param pulumi.Input[int] global_node_group_count: Indicates the number of node groups in the Global Datastore.
        :param pulumi.Input[str] global_replication_group_description: The optional description of the Global Datastore
        :param pulumi.Input[str] global_replication_group_id_suffix: The suffix name of a Global Datastore. Amazon ElastiCache automatically applies a prefix to the Global Datastore ID when it is created. Each AWS Region has its own prefix. 
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GlobalReplicationGroupMemberArgs']]]] members: The replication groups that comprise the Global Datastore.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GlobalReplicationGroupRegionalConfigurationArgs']]]] regional_configurations: Describes the replication group IDs, the AWS regions where they are stored and the shard configuration for each that comprise the Global Datastore 
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GlobalReplicationGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::ElastiCache::GlobalReplicationGroup resource creates an Amazon ElastiCache Global Replication Group.

        :param str resource_name: The name of the resource.
        :param GlobalReplicationGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GlobalReplicationGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            GlobalReplicationGroupArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automatic_failover_enabled: Optional[pulumi.Input[bool]] = None,
                 cache_node_type: Optional[pulumi.Input[str]] = None,
                 cache_parameter_group_name: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 global_node_group_count: Optional[pulumi.Input[int]] = None,
                 global_replication_group_description: Optional[pulumi.Input[str]] = None,
                 global_replication_group_id_suffix: Optional[pulumi.Input[str]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GlobalReplicationGroupMemberArgs']]]]] = None,
                 regional_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GlobalReplicationGroupRegionalConfigurationArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GlobalReplicationGroupArgs.__new__(GlobalReplicationGroupArgs)

            __props__.__dict__["automatic_failover_enabled"] = automatic_failover_enabled
            __props__.__dict__["cache_node_type"] = cache_node_type
            __props__.__dict__["cache_parameter_group_name"] = cache_parameter_group_name
            __props__.__dict__["engine_version"] = engine_version
            __props__.__dict__["global_node_group_count"] = global_node_group_count
            __props__.__dict__["global_replication_group_description"] = global_replication_group_description
            __props__.__dict__["global_replication_group_id_suffix"] = global_replication_group_id_suffix
            if members is None and not opts.urn:
                raise TypeError("Missing required property 'members'")
            __props__.__dict__["members"] = members
            __props__.__dict__["regional_configurations"] = regional_configurations
            __props__.__dict__["global_replication_group_id"] = None
            __props__.__dict__["status"] = None
        super(GlobalReplicationGroup, __self__).__init__(
            'aws-native:elasticache:GlobalReplicationGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GlobalReplicationGroup':
        """
        Get an existing GlobalReplicationGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GlobalReplicationGroupArgs.__new__(GlobalReplicationGroupArgs)

        __props__.__dict__["automatic_failover_enabled"] = None
        __props__.__dict__["cache_node_type"] = None
        __props__.__dict__["cache_parameter_group_name"] = None
        __props__.__dict__["engine_version"] = None
        __props__.__dict__["global_node_group_count"] = None
        __props__.__dict__["global_replication_group_description"] = None
        __props__.__dict__["global_replication_group_id"] = None
        __props__.__dict__["global_replication_group_id_suffix"] = None
        __props__.__dict__["members"] = None
        __props__.__dict__["regional_configurations"] = None
        __props__.__dict__["status"] = None
        return GlobalReplicationGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="automaticFailoverEnabled")
    def automatic_failover_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        AutomaticFailoverEnabled
        """
        return pulumi.get(self, "automatic_failover_enabled")

    @property
    @pulumi.getter(name="cacheNodeType")
    def cache_node_type(self) -> pulumi.Output[Optional[str]]:
        """
        The cache node type of the Global Datastore
        """
        return pulumi.get(self, "cache_node_type")

    @property
    @pulumi.getter(name="cacheParameterGroupName")
    def cache_parameter_group_name(self) -> pulumi.Output[Optional[str]]:
        """
        Cache parameter group name to use for the new engine version. This parameter cannot be modified independently.
        """
        return pulumi.get(self, "cache_parameter_group_name")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[Optional[str]]:
        """
        The engine version of the Global Datastore.
        """
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter(name="globalNodeGroupCount")
    def global_node_group_count(self) -> pulumi.Output[Optional[int]]:
        """
        Indicates the number of node groups in the Global Datastore.
        """
        return pulumi.get(self, "global_node_group_count")

    @property
    @pulumi.getter(name="globalReplicationGroupDescription")
    def global_replication_group_description(self) -> pulumi.Output[Optional[str]]:
        """
        The optional description of the Global Datastore
        """
        return pulumi.get(self, "global_replication_group_description")

    @property
    @pulumi.getter(name="globalReplicationGroupId")
    def global_replication_group_id(self) -> pulumi.Output[str]:
        """
        The name of the Global Datastore, it is generated by ElastiCache adding a prefix to GlobalReplicationGroupIdSuffix.
        """
        return pulumi.get(self, "global_replication_group_id")

    @property
    @pulumi.getter(name="globalReplicationGroupIdSuffix")
    def global_replication_group_id_suffix(self) -> pulumi.Output[Optional[str]]:
        """
        The suffix name of a Global Datastore. Amazon ElastiCache automatically applies a prefix to the Global Datastore ID when it is created. Each AWS Region has its own prefix. 
        """
        return pulumi.get(self, "global_replication_group_id_suffix")

    @property
    @pulumi.getter
    def members(self) -> pulumi.Output[Sequence['outputs.GlobalReplicationGroupMember']]:
        """
        The replication groups that comprise the Global Datastore.
        """
        return pulumi.get(self, "members")

    @property
    @pulumi.getter(name="regionalConfigurations")
    def regional_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.GlobalReplicationGroupRegionalConfiguration']]]:
        """
        Describes the replication group IDs, the AWS regions where they are stored and the shard configuration for each that comprise the Global Datastore 
        """
        return pulumi.get(self, "regional_configurations")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the Global Datastore
        """
        return pulumi.get(self, "status")

