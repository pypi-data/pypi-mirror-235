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

__all__ = ['DomainArgs', 'Domain']

@pulumi.input_type
class DomainArgs:
    def __init__(__self__, *,
                 access_policies: Optional[Any] = None,
                 advanced_options: Optional[Any] = None,
                 advanced_security_options: Optional[pulumi.Input['DomainAdvancedSecurityOptionsInputArgs']] = None,
                 cluster_config: Optional[pulumi.Input['DomainClusterConfigArgs']] = None,
                 cognito_options: Optional[pulumi.Input['DomainCognitoOptionsArgs']] = None,
                 domain_endpoint_options: Optional[pulumi.Input['DomainEndpointOptionsArgs']] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 ebs_options: Optional[pulumi.Input['DomainEbsOptionsArgs']] = None,
                 encryption_at_rest_options: Optional[pulumi.Input['DomainEncryptionAtRestOptionsArgs']] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 log_publishing_options: Optional[Any] = None,
                 node_to_node_encryption_options: Optional[pulumi.Input['DomainNodeToNodeEncryptionOptionsArgs']] = None,
                 off_peak_window_options: Optional[pulumi.Input['DomainOffPeakWindowOptionsArgs']] = None,
                 snapshot_options: Optional[pulumi.Input['DomainSnapshotOptionsArgs']] = None,
                 software_update_options: Optional[pulumi.Input['DomainSoftwareUpdateOptionsArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DomainTagArgs']]]] = None,
                 vpc_options: Optional[pulumi.Input['DomainVpcOptionsArgs']] = None):
        """
        The set of arguments for constructing a Domain resource.
        :param pulumi.Input[Sequence[pulumi.Input['DomainTagArgs']]] tags: An arbitrary set of tags (key-value pairs) for this Domain.
        """
        DomainArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            access_policies=access_policies,
            advanced_options=advanced_options,
            advanced_security_options=advanced_security_options,
            cluster_config=cluster_config,
            cognito_options=cognito_options,
            domain_endpoint_options=domain_endpoint_options,
            domain_name=domain_name,
            ebs_options=ebs_options,
            encryption_at_rest_options=encryption_at_rest_options,
            engine_version=engine_version,
            log_publishing_options=log_publishing_options,
            node_to_node_encryption_options=node_to_node_encryption_options,
            off_peak_window_options=off_peak_window_options,
            snapshot_options=snapshot_options,
            software_update_options=software_update_options,
            tags=tags,
            vpc_options=vpc_options,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             access_policies: Optional[Any] = None,
             advanced_options: Optional[Any] = None,
             advanced_security_options: Optional[pulumi.Input['DomainAdvancedSecurityOptionsInputArgs']] = None,
             cluster_config: Optional[pulumi.Input['DomainClusterConfigArgs']] = None,
             cognito_options: Optional[pulumi.Input['DomainCognitoOptionsArgs']] = None,
             domain_endpoint_options: Optional[pulumi.Input['DomainEndpointOptionsArgs']] = None,
             domain_name: Optional[pulumi.Input[str]] = None,
             ebs_options: Optional[pulumi.Input['DomainEbsOptionsArgs']] = None,
             encryption_at_rest_options: Optional[pulumi.Input['DomainEncryptionAtRestOptionsArgs']] = None,
             engine_version: Optional[pulumi.Input[str]] = None,
             log_publishing_options: Optional[Any] = None,
             node_to_node_encryption_options: Optional[pulumi.Input['DomainNodeToNodeEncryptionOptionsArgs']] = None,
             off_peak_window_options: Optional[pulumi.Input['DomainOffPeakWindowOptionsArgs']] = None,
             snapshot_options: Optional[pulumi.Input['DomainSnapshotOptionsArgs']] = None,
             software_update_options: Optional[pulumi.Input['DomainSoftwareUpdateOptionsArgs']] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['DomainTagArgs']]]] = None,
             vpc_options: Optional[pulumi.Input['DomainVpcOptionsArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if access_policies is not None:
            _setter("access_policies", access_policies)
        if advanced_options is not None:
            _setter("advanced_options", advanced_options)
        if advanced_security_options is not None:
            _setter("advanced_security_options", advanced_security_options)
        if cluster_config is not None:
            _setter("cluster_config", cluster_config)
        if cognito_options is not None:
            _setter("cognito_options", cognito_options)
        if domain_endpoint_options is not None:
            _setter("domain_endpoint_options", domain_endpoint_options)
        if domain_name is not None:
            _setter("domain_name", domain_name)
        if ebs_options is not None:
            _setter("ebs_options", ebs_options)
        if encryption_at_rest_options is not None:
            _setter("encryption_at_rest_options", encryption_at_rest_options)
        if engine_version is not None:
            _setter("engine_version", engine_version)
        if log_publishing_options is not None:
            _setter("log_publishing_options", log_publishing_options)
        if node_to_node_encryption_options is not None:
            _setter("node_to_node_encryption_options", node_to_node_encryption_options)
        if off_peak_window_options is not None:
            _setter("off_peak_window_options", off_peak_window_options)
        if snapshot_options is not None:
            _setter("snapshot_options", snapshot_options)
        if software_update_options is not None:
            _setter("software_update_options", software_update_options)
        if tags is not None:
            _setter("tags", tags)
        if vpc_options is not None:
            _setter("vpc_options", vpc_options)

    @property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> Optional[Any]:
        return pulumi.get(self, "access_policies")

    @access_policies.setter
    def access_policies(self, value: Optional[Any]):
        pulumi.set(self, "access_policies", value)

    @property
    @pulumi.getter(name="advancedOptions")
    def advanced_options(self) -> Optional[Any]:
        return pulumi.get(self, "advanced_options")

    @advanced_options.setter
    def advanced_options(self, value: Optional[Any]):
        pulumi.set(self, "advanced_options", value)

    @property
    @pulumi.getter(name="advancedSecurityOptions")
    def advanced_security_options(self) -> Optional[pulumi.Input['DomainAdvancedSecurityOptionsInputArgs']]:
        return pulumi.get(self, "advanced_security_options")

    @advanced_security_options.setter
    def advanced_security_options(self, value: Optional[pulumi.Input['DomainAdvancedSecurityOptionsInputArgs']]):
        pulumi.set(self, "advanced_security_options", value)

    @property
    @pulumi.getter(name="clusterConfig")
    def cluster_config(self) -> Optional[pulumi.Input['DomainClusterConfigArgs']]:
        return pulumi.get(self, "cluster_config")

    @cluster_config.setter
    def cluster_config(self, value: Optional[pulumi.Input['DomainClusterConfigArgs']]):
        pulumi.set(self, "cluster_config", value)

    @property
    @pulumi.getter(name="cognitoOptions")
    def cognito_options(self) -> Optional[pulumi.Input['DomainCognitoOptionsArgs']]:
        return pulumi.get(self, "cognito_options")

    @cognito_options.setter
    def cognito_options(self, value: Optional[pulumi.Input['DomainCognitoOptionsArgs']]):
        pulumi.set(self, "cognito_options", value)

    @property
    @pulumi.getter(name="domainEndpointOptions")
    def domain_endpoint_options(self) -> Optional[pulumi.Input['DomainEndpointOptionsArgs']]:
        return pulumi.get(self, "domain_endpoint_options")

    @domain_endpoint_options.setter
    def domain_endpoint_options(self, value: Optional[pulumi.Input['DomainEndpointOptionsArgs']]):
        pulumi.set(self, "domain_endpoint_options", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="ebsOptions")
    def ebs_options(self) -> Optional[pulumi.Input['DomainEbsOptionsArgs']]:
        return pulumi.get(self, "ebs_options")

    @ebs_options.setter
    def ebs_options(self, value: Optional[pulumi.Input['DomainEbsOptionsArgs']]):
        pulumi.set(self, "ebs_options", value)

    @property
    @pulumi.getter(name="encryptionAtRestOptions")
    def encryption_at_rest_options(self) -> Optional[pulumi.Input['DomainEncryptionAtRestOptionsArgs']]:
        return pulumi.get(self, "encryption_at_rest_options")

    @encryption_at_rest_options.setter
    def encryption_at_rest_options(self, value: Optional[pulumi.Input['DomainEncryptionAtRestOptionsArgs']]):
        pulumi.set(self, "encryption_at_rest_options", value)

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "engine_version")

    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "engine_version", value)

    @property
    @pulumi.getter(name="logPublishingOptions")
    def log_publishing_options(self) -> Optional[Any]:
        return pulumi.get(self, "log_publishing_options")

    @log_publishing_options.setter
    def log_publishing_options(self, value: Optional[Any]):
        pulumi.set(self, "log_publishing_options", value)

    @property
    @pulumi.getter(name="nodeToNodeEncryptionOptions")
    def node_to_node_encryption_options(self) -> Optional[pulumi.Input['DomainNodeToNodeEncryptionOptionsArgs']]:
        return pulumi.get(self, "node_to_node_encryption_options")

    @node_to_node_encryption_options.setter
    def node_to_node_encryption_options(self, value: Optional[pulumi.Input['DomainNodeToNodeEncryptionOptionsArgs']]):
        pulumi.set(self, "node_to_node_encryption_options", value)

    @property
    @pulumi.getter(name="offPeakWindowOptions")
    def off_peak_window_options(self) -> Optional[pulumi.Input['DomainOffPeakWindowOptionsArgs']]:
        return pulumi.get(self, "off_peak_window_options")

    @off_peak_window_options.setter
    def off_peak_window_options(self, value: Optional[pulumi.Input['DomainOffPeakWindowOptionsArgs']]):
        pulumi.set(self, "off_peak_window_options", value)

    @property
    @pulumi.getter(name="snapshotOptions")
    def snapshot_options(self) -> Optional[pulumi.Input['DomainSnapshotOptionsArgs']]:
        return pulumi.get(self, "snapshot_options")

    @snapshot_options.setter
    def snapshot_options(self, value: Optional[pulumi.Input['DomainSnapshotOptionsArgs']]):
        pulumi.set(self, "snapshot_options", value)

    @property
    @pulumi.getter(name="softwareUpdateOptions")
    def software_update_options(self) -> Optional[pulumi.Input['DomainSoftwareUpdateOptionsArgs']]:
        return pulumi.get(self, "software_update_options")

    @software_update_options.setter
    def software_update_options(self, value: Optional[pulumi.Input['DomainSoftwareUpdateOptionsArgs']]):
        pulumi.set(self, "software_update_options", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DomainTagArgs']]]]:
        """
        An arbitrary set of tags (key-value pairs) for this Domain.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DomainTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="vpcOptions")
    def vpc_options(self) -> Optional[pulumi.Input['DomainVpcOptionsArgs']]:
        return pulumi.get(self, "vpc_options")

    @vpc_options.setter
    def vpc_options(self, value: Optional[pulumi.Input['DomainVpcOptionsArgs']]):
        pulumi.set(self, "vpc_options", value)


class Domain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_policies: Optional[Any] = None,
                 advanced_options: Optional[Any] = None,
                 advanced_security_options: Optional[pulumi.Input[pulumi.InputType['DomainAdvancedSecurityOptionsInputArgs']]] = None,
                 cluster_config: Optional[pulumi.Input[pulumi.InputType['DomainClusterConfigArgs']]] = None,
                 cognito_options: Optional[pulumi.Input[pulumi.InputType['DomainCognitoOptionsArgs']]] = None,
                 domain_endpoint_options: Optional[pulumi.Input[pulumi.InputType['DomainEndpointOptionsArgs']]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 ebs_options: Optional[pulumi.Input[pulumi.InputType['DomainEbsOptionsArgs']]] = None,
                 encryption_at_rest_options: Optional[pulumi.Input[pulumi.InputType['DomainEncryptionAtRestOptionsArgs']]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 log_publishing_options: Optional[Any] = None,
                 node_to_node_encryption_options: Optional[pulumi.Input[pulumi.InputType['DomainNodeToNodeEncryptionOptionsArgs']]] = None,
                 off_peak_window_options: Optional[pulumi.Input[pulumi.InputType['DomainOffPeakWindowOptionsArgs']]] = None,
                 snapshot_options: Optional[pulumi.Input[pulumi.InputType['DomainSnapshotOptionsArgs']]] = None,
                 software_update_options: Optional[pulumi.Input[pulumi.InputType['DomainSoftwareUpdateOptionsArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainTagArgs']]]]] = None,
                 vpc_options: Optional[pulumi.Input[pulumi.InputType['DomainVpcOptionsArgs']]] = None,
                 __props__=None):
        """
        An example resource schema demonstrating some basic constructs and validation rules.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainTagArgs']]]] tags: An arbitrary set of tags (key-value pairs) for this Domain.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DomainArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An example resource schema demonstrating some basic constructs and validation rules.

        :param str resource_name: The name of the resource.
        :param DomainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DomainArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_policies: Optional[Any] = None,
                 advanced_options: Optional[Any] = None,
                 advanced_security_options: Optional[pulumi.Input[pulumi.InputType['DomainAdvancedSecurityOptionsInputArgs']]] = None,
                 cluster_config: Optional[pulumi.Input[pulumi.InputType['DomainClusterConfigArgs']]] = None,
                 cognito_options: Optional[pulumi.Input[pulumi.InputType['DomainCognitoOptionsArgs']]] = None,
                 domain_endpoint_options: Optional[pulumi.Input[pulumi.InputType['DomainEndpointOptionsArgs']]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 ebs_options: Optional[pulumi.Input[pulumi.InputType['DomainEbsOptionsArgs']]] = None,
                 encryption_at_rest_options: Optional[pulumi.Input[pulumi.InputType['DomainEncryptionAtRestOptionsArgs']]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 log_publishing_options: Optional[Any] = None,
                 node_to_node_encryption_options: Optional[pulumi.Input[pulumi.InputType['DomainNodeToNodeEncryptionOptionsArgs']]] = None,
                 off_peak_window_options: Optional[pulumi.Input[pulumi.InputType['DomainOffPeakWindowOptionsArgs']]] = None,
                 snapshot_options: Optional[pulumi.Input[pulumi.InputType['DomainSnapshotOptionsArgs']]] = None,
                 software_update_options: Optional[pulumi.Input[pulumi.InputType['DomainSoftwareUpdateOptionsArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainTagArgs']]]]] = None,
                 vpc_options: Optional[pulumi.Input[pulumi.InputType['DomainVpcOptionsArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DomainArgs.__new__(DomainArgs)

            __props__.__dict__["access_policies"] = access_policies
            __props__.__dict__["advanced_options"] = advanced_options
            if advanced_security_options is not None and not isinstance(advanced_security_options, DomainAdvancedSecurityOptionsInputArgs):
                advanced_security_options = advanced_security_options or {}
                def _setter(key, value):
                    advanced_security_options[key] = value
                DomainAdvancedSecurityOptionsInputArgs._configure(_setter, **advanced_security_options)
            __props__.__dict__["advanced_security_options"] = advanced_security_options
            if cluster_config is not None and not isinstance(cluster_config, DomainClusterConfigArgs):
                cluster_config = cluster_config or {}
                def _setter(key, value):
                    cluster_config[key] = value
                DomainClusterConfigArgs._configure(_setter, **cluster_config)
            __props__.__dict__["cluster_config"] = cluster_config
            if cognito_options is not None and not isinstance(cognito_options, DomainCognitoOptionsArgs):
                cognito_options = cognito_options or {}
                def _setter(key, value):
                    cognito_options[key] = value
                DomainCognitoOptionsArgs._configure(_setter, **cognito_options)
            __props__.__dict__["cognito_options"] = cognito_options
            if domain_endpoint_options is not None and not isinstance(domain_endpoint_options, DomainEndpointOptionsArgs):
                domain_endpoint_options = domain_endpoint_options or {}
                def _setter(key, value):
                    domain_endpoint_options[key] = value
                DomainEndpointOptionsArgs._configure(_setter, **domain_endpoint_options)
            __props__.__dict__["domain_endpoint_options"] = domain_endpoint_options
            __props__.__dict__["domain_name"] = domain_name
            if ebs_options is not None and not isinstance(ebs_options, DomainEbsOptionsArgs):
                ebs_options = ebs_options or {}
                def _setter(key, value):
                    ebs_options[key] = value
                DomainEbsOptionsArgs._configure(_setter, **ebs_options)
            __props__.__dict__["ebs_options"] = ebs_options
            if encryption_at_rest_options is not None and not isinstance(encryption_at_rest_options, DomainEncryptionAtRestOptionsArgs):
                encryption_at_rest_options = encryption_at_rest_options or {}
                def _setter(key, value):
                    encryption_at_rest_options[key] = value
                DomainEncryptionAtRestOptionsArgs._configure(_setter, **encryption_at_rest_options)
            __props__.__dict__["encryption_at_rest_options"] = encryption_at_rest_options
            __props__.__dict__["engine_version"] = engine_version
            __props__.__dict__["log_publishing_options"] = log_publishing_options
            if node_to_node_encryption_options is not None and not isinstance(node_to_node_encryption_options, DomainNodeToNodeEncryptionOptionsArgs):
                node_to_node_encryption_options = node_to_node_encryption_options or {}
                def _setter(key, value):
                    node_to_node_encryption_options[key] = value
                DomainNodeToNodeEncryptionOptionsArgs._configure(_setter, **node_to_node_encryption_options)
            __props__.__dict__["node_to_node_encryption_options"] = node_to_node_encryption_options
            if off_peak_window_options is not None and not isinstance(off_peak_window_options, DomainOffPeakWindowOptionsArgs):
                off_peak_window_options = off_peak_window_options or {}
                def _setter(key, value):
                    off_peak_window_options[key] = value
                DomainOffPeakWindowOptionsArgs._configure(_setter, **off_peak_window_options)
            __props__.__dict__["off_peak_window_options"] = off_peak_window_options
            if snapshot_options is not None and not isinstance(snapshot_options, DomainSnapshotOptionsArgs):
                snapshot_options = snapshot_options or {}
                def _setter(key, value):
                    snapshot_options[key] = value
                DomainSnapshotOptionsArgs._configure(_setter, **snapshot_options)
            __props__.__dict__["snapshot_options"] = snapshot_options
            if software_update_options is not None and not isinstance(software_update_options, DomainSoftwareUpdateOptionsArgs):
                software_update_options = software_update_options or {}
                def _setter(key, value):
                    software_update_options[key] = value
                DomainSoftwareUpdateOptionsArgs._configure(_setter, **software_update_options)
            __props__.__dict__["software_update_options"] = software_update_options
            __props__.__dict__["tags"] = tags
            if vpc_options is not None and not isinstance(vpc_options, DomainVpcOptionsArgs):
                vpc_options = vpc_options or {}
                def _setter(key, value):
                    vpc_options[key] = value
                DomainVpcOptionsArgs._configure(_setter, **vpc_options)
            __props__.__dict__["vpc_options"] = vpc_options
            __props__.__dict__["arn"] = None
            __props__.__dict__["domain_arn"] = None
            __props__.__dict__["domain_endpoint"] = None
            __props__.__dict__["domain_endpoints"] = None
            __props__.__dict__["service_software_options"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["domain_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Domain, __self__).__init__(
            'aws-native:opensearchservice:Domain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Domain':
        """
        Get an existing Domain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DomainArgs.__new__(DomainArgs)

        __props__.__dict__["access_policies"] = None
        __props__.__dict__["advanced_options"] = None
        __props__.__dict__["advanced_security_options"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["cluster_config"] = None
        __props__.__dict__["cognito_options"] = None
        __props__.__dict__["domain_arn"] = None
        __props__.__dict__["domain_endpoint"] = None
        __props__.__dict__["domain_endpoint_options"] = None
        __props__.__dict__["domain_endpoints"] = None
        __props__.__dict__["domain_name"] = None
        __props__.__dict__["ebs_options"] = None
        __props__.__dict__["encryption_at_rest_options"] = None
        __props__.__dict__["engine_version"] = None
        __props__.__dict__["log_publishing_options"] = None
        __props__.__dict__["node_to_node_encryption_options"] = None
        __props__.__dict__["off_peak_window_options"] = None
        __props__.__dict__["service_software_options"] = None
        __props__.__dict__["snapshot_options"] = None
        __props__.__dict__["software_update_options"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["vpc_options"] = None
        return Domain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "access_policies")

    @property
    @pulumi.getter(name="advancedOptions")
    def advanced_options(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "advanced_options")

    @property
    @pulumi.getter(name="advancedSecurityOptions")
    def advanced_security_options(self) -> pulumi.Output[Optional['outputs.DomainAdvancedSecurityOptionsInput']]:
        return pulumi.get(self, "advanced_security_options")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="clusterConfig")
    def cluster_config(self) -> pulumi.Output[Optional['outputs.DomainClusterConfig']]:
        return pulumi.get(self, "cluster_config")

    @property
    @pulumi.getter(name="cognitoOptions")
    def cognito_options(self) -> pulumi.Output[Optional['outputs.DomainCognitoOptions']]:
        return pulumi.get(self, "cognito_options")

    @property
    @pulumi.getter(name="domainArn")
    def domain_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "domain_arn")

    @property
    @pulumi.getter(name="domainEndpoint")
    def domain_endpoint(self) -> pulumi.Output[str]:
        return pulumi.get(self, "domain_endpoint")

    @property
    @pulumi.getter(name="domainEndpointOptions")
    def domain_endpoint_options(self) -> pulumi.Output[Optional['outputs.DomainEndpointOptions']]:
        return pulumi.get(self, "domain_endpoint_options")

    @property
    @pulumi.getter(name="domainEndpoints")
    def domain_endpoints(self) -> pulumi.Output[Any]:
        return pulumi.get(self, "domain_endpoints")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="ebsOptions")
    def ebs_options(self) -> pulumi.Output[Optional['outputs.DomainEbsOptions']]:
        return pulumi.get(self, "ebs_options")

    @property
    @pulumi.getter(name="encryptionAtRestOptions")
    def encryption_at_rest_options(self) -> pulumi.Output[Optional['outputs.DomainEncryptionAtRestOptions']]:
        return pulumi.get(self, "encryption_at_rest_options")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter(name="logPublishingOptions")
    def log_publishing_options(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "log_publishing_options")

    @property
    @pulumi.getter(name="nodeToNodeEncryptionOptions")
    def node_to_node_encryption_options(self) -> pulumi.Output[Optional['outputs.DomainNodeToNodeEncryptionOptions']]:
        return pulumi.get(self, "node_to_node_encryption_options")

    @property
    @pulumi.getter(name="offPeakWindowOptions")
    def off_peak_window_options(self) -> pulumi.Output[Optional['outputs.DomainOffPeakWindowOptions']]:
        return pulumi.get(self, "off_peak_window_options")

    @property
    @pulumi.getter(name="serviceSoftwareOptions")
    def service_software_options(self) -> pulumi.Output['outputs.DomainServiceSoftwareOptions']:
        return pulumi.get(self, "service_software_options")

    @property
    @pulumi.getter(name="snapshotOptions")
    def snapshot_options(self) -> pulumi.Output[Optional['outputs.DomainSnapshotOptions']]:
        return pulumi.get(self, "snapshot_options")

    @property
    @pulumi.getter(name="softwareUpdateOptions")
    def software_update_options(self) -> pulumi.Output[Optional['outputs.DomainSoftwareUpdateOptions']]:
        return pulumi.get(self, "software_update_options")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DomainTag']]]:
        """
        An arbitrary set of tags (key-value pairs) for this Domain.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcOptions")
    def vpc_options(self) -> pulumi.Output[Optional['outputs.DomainVpcOptions']]:
        return pulumi.get(self, "vpc_options")

