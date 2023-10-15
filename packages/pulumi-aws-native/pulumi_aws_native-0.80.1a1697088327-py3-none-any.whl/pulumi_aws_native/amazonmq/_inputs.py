# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'BrokerConfigurationIdArgs',
    'BrokerEncryptionOptionsArgs',
    'BrokerLdapServerMetadataArgs',
    'BrokerLogListArgs',
    'BrokerMaintenanceWindowArgs',
    'BrokerTagsEntryArgs',
    'BrokerUserArgs',
    'ConfigurationAssociationConfigurationIdArgs',
    'ConfigurationTagsEntryArgs',
]

@pulumi.input_type
class BrokerConfigurationIdArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 revision: pulumi.Input[int]):
        BrokerConfigurationIdArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            id=id,
            revision=revision,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             id: pulumi.Input[str],
             revision: pulumi.Input[int],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("id", id)
        _setter("revision", revision)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def revision(self) -> pulumi.Input[int]:
        return pulumi.get(self, "revision")

    @revision.setter
    def revision(self, value: pulumi.Input[int]):
        pulumi.set(self, "revision", value)


@pulumi.input_type
class BrokerEncryptionOptionsArgs:
    def __init__(__self__, *,
                 use_aws_owned_key: pulumi.Input[bool],
                 kms_key_id: Optional[pulumi.Input[str]] = None):
        BrokerEncryptionOptionsArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            use_aws_owned_key=use_aws_owned_key,
            kms_key_id=kms_key_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             use_aws_owned_key: pulumi.Input[bool],
             kms_key_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("use_aws_owned_key", use_aws_owned_key)
        if kms_key_id is not None:
            _setter("kms_key_id", kms_key_id)

    @property
    @pulumi.getter(name="useAwsOwnedKey")
    def use_aws_owned_key(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "use_aws_owned_key")

    @use_aws_owned_key.setter
    def use_aws_owned_key(self, value: pulumi.Input[bool]):
        pulumi.set(self, "use_aws_owned_key", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)


@pulumi.input_type
class BrokerLdapServerMetadataArgs:
    def __init__(__self__, *,
                 hosts: pulumi.Input[Sequence[pulumi.Input[str]]],
                 role_base: pulumi.Input[str],
                 role_search_matching: pulumi.Input[str],
                 service_account_password: pulumi.Input[str],
                 service_account_username: pulumi.Input[str],
                 user_base: pulumi.Input[str],
                 user_search_matching: pulumi.Input[str],
                 role_name: Optional[pulumi.Input[str]] = None,
                 role_search_subtree: Optional[pulumi.Input[bool]] = None,
                 user_role_name: Optional[pulumi.Input[str]] = None,
                 user_search_subtree: Optional[pulumi.Input[bool]] = None):
        BrokerLdapServerMetadataArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            hosts=hosts,
            role_base=role_base,
            role_search_matching=role_search_matching,
            service_account_password=service_account_password,
            service_account_username=service_account_username,
            user_base=user_base,
            user_search_matching=user_search_matching,
            role_name=role_name,
            role_search_subtree=role_search_subtree,
            user_role_name=user_role_name,
            user_search_subtree=user_search_subtree,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             hosts: pulumi.Input[Sequence[pulumi.Input[str]]],
             role_base: pulumi.Input[str],
             role_search_matching: pulumi.Input[str],
             service_account_password: pulumi.Input[str],
             service_account_username: pulumi.Input[str],
             user_base: pulumi.Input[str],
             user_search_matching: pulumi.Input[str],
             role_name: Optional[pulumi.Input[str]] = None,
             role_search_subtree: Optional[pulumi.Input[bool]] = None,
             user_role_name: Optional[pulumi.Input[str]] = None,
             user_search_subtree: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("hosts", hosts)
        _setter("role_base", role_base)
        _setter("role_search_matching", role_search_matching)
        _setter("service_account_password", service_account_password)
        _setter("service_account_username", service_account_username)
        _setter("user_base", user_base)
        _setter("user_search_matching", user_search_matching)
        if role_name is not None:
            _setter("role_name", role_name)
        if role_search_subtree is not None:
            _setter("role_search_subtree", role_search_subtree)
        if user_role_name is not None:
            _setter("user_role_name", user_role_name)
        if user_search_subtree is not None:
            _setter("user_search_subtree", user_search_subtree)

    @property
    @pulumi.getter
    def hosts(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "hosts")

    @hosts.setter
    def hosts(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "hosts", value)

    @property
    @pulumi.getter(name="roleBase")
    def role_base(self) -> pulumi.Input[str]:
        return pulumi.get(self, "role_base")

    @role_base.setter
    def role_base(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_base", value)

    @property
    @pulumi.getter(name="roleSearchMatching")
    def role_search_matching(self) -> pulumi.Input[str]:
        return pulumi.get(self, "role_search_matching")

    @role_search_matching.setter
    def role_search_matching(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_search_matching", value)

    @property
    @pulumi.getter(name="serviceAccountPassword")
    def service_account_password(self) -> pulumi.Input[str]:
        return pulumi.get(self, "service_account_password")

    @service_account_password.setter
    def service_account_password(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_account_password", value)

    @property
    @pulumi.getter(name="serviceAccountUsername")
    def service_account_username(self) -> pulumi.Input[str]:
        return pulumi.get(self, "service_account_username")

    @service_account_username.setter
    def service_account_username(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_account_username", value)

    @property
    @pulumi.getter(name="userBase")
    def user_base(self) -> pulumi.Input[str]:
        return pulumi.get(self, "user_base")

    @user_base.setter
    def user_base(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_base", value)

    @property
    @pulumi.getter(name="userSearchMatching")
    def user_search_matching(self) -> pulumi.Input[str]:
        return pulumi.get(self, "user_search_matching")

    @user_search_matching.setter
    def user_search_matching(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_search_matching", value)

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "role_name")

    @role_name.setter
    def role_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_name", value)

    @property
    @pulumi.getter(name="roleSearchSubtree")
    def role_search_subtree(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "role_search_subtree")

    @role_search_subtree.setter
    def role_search_subtree(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "role_search_subtree", value)

    @property
    @pulumi.getter(name="userRoleName")
    def user_role_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "user_role_name")

    @user_role_name.setter
    def user_role_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_role_name", value)

    @property
    @pulumi.getter(name="userSearchSubtree")
    def user_search_subtree(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "user_search_subtree")

    @user_search_subtree.setter
    def user_search_subtree(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "user_search_subtree", value)


@pulumi.input_type
class BrokerLogListArgs:
    def __init__(__self__, *,
                 audit: Optional[pulumi.Input[bool]] = None,
                 general: Optional[pulumi.Input[bool]] = None):
        BrokerLogListArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            audit=audit,
            general=general,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             audit: Optional[pulumi.Input[bool]] = None,
             general: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if audit is not None:
            _setter("audit", audit)
        if general is not None:
            _setter("general", general)

    @property
    @pulumi.getter
    def audit(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "audit")

    @audit.setter
    def audit(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "audit", value)

    @property
    @pulumi.getter
    def general(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "general")

    @general.setter
    def general(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "general", value)


@pulumi.input_type
class BrokerMaintenanceWindowArgs:
    def __init__(__self__, *,
                 day_of_week: pulumi.Input[str],
                 time_of_day: pulumi.Input[str],
                 time_zone: pulumi.Input[str]):
        BrokerMaintenanceWindowArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            day_of_week=day_of_week,
            time_of_day=time_of_day,
            time_zone=time_zone,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             day_of_week: pulumi.Input[str],
             time_of_day: pulumi.Input[str],
             time_zone: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("day_of_week", day_of_week)
        _setter("time_of_day", time_of_day)
        _setter("time_zone", time_zone)

    @property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> pulumi.Input[str]:
        return pulumi.get(self, "day_of_week")

    @day_of_week.setter
    def day_of_week(self, value: pulumi.Input[str]):
        pulumi.set(self, "day_of_week", value)

    @property
    @pulumi.getter(name="timeOfDay")
    def time_of_day(self) -> pulumi.Input[str]:
        return pulumi.get(self, "time_of_day")

    @time_of_day.setter
    def time_of_day(self, value: pulumi.Input[str]):
        pulumi.set(self, "time_of_day", value)

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Input[str]:
        return pulumi.get(self, "time_zone")

    @time_zone.setter
    def time_zone(self, value: pulumi.Input[str]):
        pulumi.set(self, "time_zone", value)


@pulumi.input_type
class BrokerTagsEntryArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        BrokerTagsEntryArgs._configure(
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
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class BrokerUserArgs:
    def __init__(__self__, *,
                 password: pulumi.Input[str],
                 username: pulumi.Input[str],
                 console_access: Optional[pulumi.Input[bool]] = None,
                 groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        BrokerUserArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            password=password,
            username=username,
            console_access=console_access,
            groups=groups,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             password: pulumi.Input[str],
             username: pulumi.Input[str],
             console_access: Optional[pulumi.Input[bool]] = None,
             groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("password", password)
        _setter("username", username)
        if console_access is not None:
            _setter("console_access", console_access)
        if groups is not None:
            _setter("groups", groups)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)

    @property
    @pulumi.getter(name="consoleAccess")
    def console_access(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "console_access")

    @console_access.setter
    def console_access(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "console_access", value)

    @property
    @pulumi.getter
    def groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "groups")

    @groups.setter
    def groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "groups", value)


@pulumi.input_type
class ConfigurationAssociationConfigurationIdArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 revision: pulumi.Input[int]):
        ConfigurationAssociationConfigurationIdArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            id=id,
            revision=revision,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             id: pulumi.Input[str],
             revision: pulumi.Input[int],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("id", id)
        _setter("revision", revision)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def revision(self) -> pulumi.Input[int]:
        return pulumi.get(self, "revision")

    @revision.setter
    def revision(self, value: pulumi.Input[int]):
        pulumi.set(self, "revision", value)


@pulumi.input_type
class ConfigurationTagsEntryArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        ConfigurationTagsEntryArgs._configure(
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
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


