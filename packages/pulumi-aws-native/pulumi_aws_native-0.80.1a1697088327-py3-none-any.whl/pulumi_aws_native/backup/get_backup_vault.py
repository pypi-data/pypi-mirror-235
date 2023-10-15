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

__all__ = [
    'GetBackupVaultResult',
    'AwaitableGetBackupVaultResult',
    'get_backup_vault',
    'get_backup_vault_output',
]

@pulumi.output_type
class GetBackupVaultResult:
    def __init__(__self__, access_policy=None, backup_vault_arn=None, backup_vault_tags=None, lock_configuration=None, notifications=None):
        if access_policy and not isinstance(access_policy, dict):
            raise TypeError("Expected argument 'access_policy' to be a dict")
        pulumi.set(__self__, "access_policy", access_policy)
        if backup_vault_arn and not isinstance(backup_vault_arn, str):
            raise TypeError("Expected argument 'backup_vault_arn' to be a str")
        pulumi.set(__self__, "backup_vault_arn", backup_vault_arn)
        if backup_vault_tags and not isinstance(backup_vault_tags, dict):
            raise TypeError("Expected argument 'backup_vault_tags' to be a dict")
        pulumi.set(__self__, "backup_vault_tags", backup_vault_tags)
        if lock_configuration and not isinstance(lock_configuration, dict):
            raise TypeError("Expected argument 'lock_configuration' to be a dict")
        pulumi.set(__self__, "lock_configuration", lock_configuration)
        if notifications and not isinstance(notifications, dict):
            raise TypeError("Expected argument 'notifications' to be a dict")
        pulumi.set(__self__, "notifications", notifications)

    @property
    @pulumi.getter(name="accessPolicy")
    def access_policy(self) -> Optional[Any]:
        return pulumi.get(self, "access_policy")

    @property
    @pulumi.getter(name="backupVaultArn")
    def backup_vault_arn(self) -> Optional[str]:
        return pulumi.get(self, "backup_vault_arn")

    @property
    @pulumi.getter(name="backupVaultTags")
    def backup_vault_tags(self) -> Optional[Any]:
        return pulumi.get(self, "backup_vault_tags")

    @property
    @pulumi.getter(name="lockConfiguration")
    def lock_configuration(self) -> Optional['outputs.BackupVaultLockConfigurationType']:
        return pulumi.get(self, "lock_configuration")

    @property
    @pulumi.getter
    def notifications(self) -> Optional['outputs.BackupVaultNotificationObjectType']:
        return pulumi.get(self, "notifications")


class AwaitableGetBackupVaultResult(GetBackupVaultResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBackupVaultResult(
            access_policy=self.access_policy,
            backup_vault_arn=self.backup_vault_arn,
            backup_vault_tags=self.backup_vault_tags,
            lock_configuration=self.lock_configuration,
            notifications=self.notifications)


def get_backup_vault(backup_vault_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBackupVaultResult:
    """
    Resource Type definition for AWS::Backup::BackupVault
    """
    __args__ = dict()
    __args__['backupVaultName'] = backup_vault_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:backup:getBackupVault', __args__, opts=opts, typ=GetBackupVaultResult).value

    return AwaitableGetBackupVaultResult(
        access_policy=pulumi.get(__ret__, 'access_policy'),
        backup_vault_arn=pulumi.get(__ret__, 'backup_vault_arn'),
        backup_vault_tags=pulumi.get(__ret__, 'backup_vault_tags'),
        lock_configuration=pulumi.get(__ret__, 'lock_configuration'),
        notifications=pulumi.get(__ret__, 'notifications'))


@_utilities.lift_output_func(get_backup_vault)
def get_backup_vault_output(backup_vault_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBackupVaultResult]:
    """
    Resource Type definition for AWS::Backup::BackupVault
    """
    ...
