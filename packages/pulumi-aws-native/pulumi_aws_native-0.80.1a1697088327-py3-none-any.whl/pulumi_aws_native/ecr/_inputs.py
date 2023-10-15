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
    'PublicRepositoryTagArgs',
    'ReplicationConfigurationReplicationDestinationArgs',
    'ReplicationConfigurationReplicationRuleArgs',
    'ReplicationConfigurationRepositoryFilterArgs',
    'ReplicationConfigurationArgs',
    'RepositoryCatalogDataPropertiesArgs',
    'RepositoryEncryptionConfigurationArgs',
    'RepositoryImageScanningConfigurationArgs',
    'RepositoryLifecyclePolicyArgs',
    'RepositoryTagArgs',
]

@pulumi.input_type
class PublicRepositoryTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        PublicRepositoryTagArgs._configure(
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
        The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ReplicationConfigurationReplicationDestinationArgs:
    def __init__(__self__, *,
                 region: pulumi.Input[str],
                 registry_id: pulumi.Input[str]):
        """
        An array of objects representing the details of a replication destination.
        """
        ReplicationConfigurationReplicationDestinationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            region=region,
            registry_id=registry_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             region: pulumi.Input[str],
             registry_id: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("region", region)
        _setter("registry_id", registry_id)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "registry_id")

    @registry_id.setter
    def registry_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "registry_id", value)


@pulumi.input_type
class ReplicationConfigurationReplicationRuleArgs:
    def __init__(__self__, *,
                 destinations: pulumi.Input[Sequence[pulumi.Input['ReplicationConfigurationReplicationDestinationArgs']]],
                 repository_filters: Optional[pulumi.Input[Sequence[pulumi.Input['ReplicationConfigurationRepositoryFilterArgs']]]] = None):
        """
        An array of objects representing the details of a replication destination.
        :param pulumi.Input[Sequence[pulumi.Input['ReplicationConfigurationReplicationDestinationArgs']]] destinations: An array of objects representing the details of a replication destination.
        :param pulumi.Input[Sequence[pulumi.Input['ReplicationConfigurationRepositoryFilterArgs']]] repository_filters: An array of objects representing the details of a repository filter.
        """
        ReplicationConfigurationReplicationRuleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            destinations=destinations,
            repository_filters=repository_filters,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             destinations: pulumi.Input[Sequence[pulumi.Input['ReplicationConfigurationReplicationDestinationArgs']]],
             repository_filters: Optional[pulumi.Input[Sequence[pulumi.Input['ReplicationConfigurationRepositoryFilterArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("destinations", destinations)
        if repository_filters is not None:
            _setter("repository_filters", repository_filters)

    @property
    @pulumi.getter
    def destinations(self) -> pulumi.Input[Sequence[pulumi.Input['ReplicationConfigurationReplicationDestinationArgs']]]:
        """
        An array of objects representing the details of a replication destination.
        """
        return pulumi.get(self, "destinations")

    @destinations.setter
    def destinations(self, value: pulumi.Input[Sequence[pulumi.Input['ReplicationConfigurationReplicationDestinationArgs']]]):
        pulumi.set(self, "destinations", value)

    @property
    @pulumi.getter(name="repositoryFilters")
    def repository_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ReplicationConfigurationRepositoryFilterArgs']]]]:
        """
        An array of objects representing the details of a repository filter.
        """
        return pulumi.get(self, "repository_filters")

    @repository_filters.setter
    def repository_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ReplicationConfigurationRepositoryFilterArgs']]]]):
        pulumi.set(self, "repository_filters", value)


@pulumi.input_type
class ReplicationConfigurationRepositoryFilterArgs:
    def __init__(__self__, *,
                 filter: pulumi.Input[str],
                 filter_type: pulumi.Input['ReplicationConfigurationFilterType']):
        """
        An array of objects representing the details of a repository filter.
        """
        ReplicationConfigurationRepositoryFilterArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            filter=filter,
            filter_type=filter_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             filter: pulumi.Input[str],
             filter_type: pulumi.Input['ReplicationConfigurationFilterType'],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("filter", filter)
        _setter("filter_type", filter_type)

    @property
    @pulumi.getter
    def filter(self) -> pulumi.Input[str]:
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: pulumi.Input[str]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> pulumi.Input['ReplicationConfigurationFilterType']:
        return pulumi.get(self, "filter_type")

    @filter_type.setter
    def filter_type(self, value: pulumi.Input['ReplicationConfigurationFilterType']):
        pulumi.set(self, "filter_type", value)


@pulumi.input_type
class ReplicationConfigurationArgs:
    def __init__(__self__, *,
                 rules: pulumi.Input[Sequence[pulumi.Input['ReplicationConfigurationReplicationRuleArgs']]]):
        """
        An object representing the replication configuration for a registry.
        :param pulumi.Input[Sequence[pulumi.Input['ReplicationConfigurationReplicationRuleArgs']]] rules: An array of objects representing the replication rules for a replication configuration. A replication configuration may contain a maximum of 10 rules.
        """
        ReplicationConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            rules=rules,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             rules: pulumi.Input[Sequence[pulumi.Input['ReplicationConfigurationReplicationRuleArgs']]],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("rules", rules)

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input['ReplicationConfigurationReplicationRuleArgs']]]:
        """
        An array of objects representing the replication rules for a replication configuration. A replication configuration may contain a maximum of 10 rules.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input['ReplicationConfigurationReplicationRuleArgs']]]):
        pulumi.set(self, "rules", value)


@pulumi.input_type
class RepositoryCatalogDataPropertiesArgs:
    def __init__(__self__, *,
                 about_text: Optional[pulumi.Input[str]] = None,
                 architectures: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 operating_systems: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 repository_description: Optional[pulumi.Input[str]] = None,
                 usage_text: Optional[pulumi.Input[str]] = None):
        """
        The CatalogData property type specifies Catalog data for ECR Public Repository. For information about Catalog Data, see <link>
        """
        RepositoryCatalogDataPropertiesArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            about_text=about_text,
            architectures=architectures,
            operating_systems=operating_systems,
            repository_description=repository_description,
            usage_text=usage_text,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             about_text: Optional[pulumi.Input[str]] = None,
             architectures: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             operating_systems: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             repository_description: Optional[pulumi.Input[str]] = None,
             usage_text: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if about_text is not None:
            _setter("about_text", about_text)
        if architectures is not None:
            _setter("architectures", architectures)
        if operating_systems is not None:
            _setter("operating_systems", operating_systems)
        if repository_description is not None:
            _setter("repository_description", repository_description)
        if usage_text is not None:
            _setter("usage_text", usage_text)

    @property
    @pulumi.getter(name="aboutText")
    def about_text(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "about_text")

    @about_text.setter
    def about_text(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "about_text", value)

    @property
    @pulumi.getter
    def architectures(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "architectures")

    @architectures.setter
    def architectures(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "architectures", value)

    @property
    @pulumi.getter(name="operatingSystems")
    def operating_systems(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "operating_systems")

    @operating_systems.setter
    def operating_systems(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "operating_systems", value)

    @property
    @pulumi.getter(name="repositoryDescription")
    def repository_description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "repository_description")

    @repository_description.setter
    def repository_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repository_description", value)

    @property
    @pulumi.getter(name="usageText")
    def usage_text(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "usage_text")

    @usage_text.setter
    def usage_text(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "usage_text", value)


@pulumi.input_type
class RepositoryEncryptionConfigurationArgs:
    def __init__(__self__, *,
                 encryption_type: pulumi.Input['RepositoryEncryptionType'],
                 kms_key: Optional[pulumi.Input[str]] = None):
        """
        The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest.

        By default, when no encryption configuration is set or the AES256 encryption type is used, Amazon ECR uses server-side encryption with Amazon S3-managed encryption keys which encrypts your data at rest using an AES-256 encryption algorithm. This does not require any action on your part.

        For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html
        """
        RepositoryEncryptionConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            encryption_type=encryption_type,
            kms_key=kms_key,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             encryption_type: pulumi.Input['RepositoryEncryptionType'],
             kms_key: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("encryption_type", encryption_type)
        if kms_key is not None:
            _setter("kms_key", kms_key)

    @property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> pulumi.Input['RepositoryEncryptionType']:
        return pulumi.get(self, "encryption_type")

    @encryption_type.setter
    def encryption_type(self, value: pulumi.Input['RepositoryEncryptionType']):
        pulumi.set(self, "encryption_type", value)

    @property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "kms_key")

    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key", value)


@pulumi.input_type
class RepositoryImageScanningConfigurationArgs:
    def __init__(__self__, *,
                 scan_on_push: Optional[pulumi.Input[bool]] = None):
        """
        The image scanning configuration for the repository. This setting determines whether images are scanned for known vulnerabilities after being pushed to the repository.
        """
        RepositoryImageScanningConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            scan_on_push=scan_on_push,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             scan_on_push: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if scan_on_push is not None:
            _setter("scan_on_push", scan_on_push)

    @property
    @pulumi.getter(name="scanOnPush")
    def scan_on_push(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "scan_on_push")

    @scan_on_push.setter
    def scan_on_push(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "scan_on_push", value)


@pulumi.input_type
class RepositoryLifecyclePolicyArgs:
    def __init__(__self__, *,
                 lifecycle_policy_text: Optional[pulumi.Input[str]] = None,
                 registry_id: Optional[pulumi.Input[str]] = None):
        """
        The LifecyclePolicy property type specifies a lifecycle policy. For information about lifecycle policy syntax, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html
        """
        RepositoryLifecyclePolicyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            lifecycle_policy_text=lifecycle_policy_text,
            registry_id=registry_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             lifecycle_policy_text: Optional[pulumi.Input[str]] = None,
             registry_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if lifecycle_policy_text is not None:
            _setter("lifecycle_policy_text", lifecycle_policy_text)
        if registry_id is not None:
            _setter("registry_id", registry_id)

    @property
    @pulumi.getter(name="lifecyclePolicyText")
    def lifecycle_policy_text(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "lifecycle_policy_text")

    @lifecycle_policy_text.setter
    def lifecycle_policy_text(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_policy_text", value)

    @property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "registry_id")

    @registry_id.setter
    def registry_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "registry_id", value)


@pulumi.input_type
class RepositoryTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        RepositoryTagArgs._configure(
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
        The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


