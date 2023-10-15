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
    'GetDbClusterResult',
    'AwaitableGetDbClusterResult',
    'get_db_cluster',
    'get_db_cluster_output',
]

@pulumi.output_type
class GetDbClusterResult:
    def __init__(__self__, allocated_storage=None, associated_roles=None, auto_minor_version_upgrade=None, backtrack_window=None, backup_retention_period=None, copy_tags_to_snapshot=None, db_cluster_arn=None, db_cluster_instance_class=None, db_cluster_parameter_group_name=None, db_cluster_resource_id=None, deletion_protection=None, domain=None, domain_iam_role_name=None, enable_cloudwatch_logs_exports=None, enable_http_endpoint=None, enable_iam_database_authentication=None, endpoint=None, engine=None, engine_version=None, global_cluster_identifier=None, iops=None, manage_master_user_password=None, master_user_secret=None, master_username=None, monitoring_interval=None, monitoring_role_arn=None, network_type=None, performance_insights_enabled=None, performance_insights_kms_key_id=None, performance_insights_retention_period=None, port=None, preferred_backup_window=None, preferred_maintenance_window=None, read_endpoint=None, replication_source_identifier=None, scaling_configuration=None, serverless_v2_scaling_configuration=None, storage_type=None, tags=None, vpc_security_group_ids=None):
        if allocated_storage and not isinstance(allocated_storage, int):
            raise TypeError("Expected argument 'allocated_storage' to be a int")
        pulumi.set(__self__, "allocated_storage", allocated_storage)
        if associated_roles and not isinstance(associated_roles, list):
            raise TypeError("Expected argument 'associated_roles' to be a list")
        pulumi.set(__self__, "associated_roles", associated_roles)
        if auto_minor_version_upgrade and not isinstance(auto_minor_version_upgrade, bool):
            raise TypeError("Expected argument 'auto_minor_version_upgrade' to be a bool")
        pulumi.set(__self__, "auto_minor_version_upgrade", auto_minor_version_upgrade)
        if backtrack_window and not isinstance(backtrack_window, int):
            raise TypeError("Expected argument 'backtrack_window' to be a int")
        pulumi.set(__self__, "backtrack_window", backtrack_window)
        if backup_retention_period and not isinstance(backup_retention_period, int):
            raise TypeError("Expected argument 'backup_retention_period' to be a int")
        pulumi.set(__self__, "backup_retention_period", backup_retention_period)
        if copy_tags_to_snapshot and not isinstance(copy_tags_to_snapshot, bool):
            raise TypeError("Expected argument 'copy_tags_to_snapshot' to be a bool")
        pulumi.set(__self__, "copy_tags_to_snapshot", copy_tags_to_snapshot)
        if db_cluster_arn and not isinstance(db_cluster_arn, str):
            raise TypeError("Expected argument 'db_cluster_arn' to be a str")
        pulumi.set(__self__, "db_cluster_arn", db_cluster_arn)
        if db_cluster_instance_class and not isinstance(db_cluster_instance_class, str):
            raise TypeError("Expected argument 'db_cluster_instance_class' to be a str")
        pulumi.set(__self__, "db_cluster_instance_class", db_cluster_instance_class)
        if db_cluster_parameter_group_name and not isinstance(db_cluster_parameter_group_name, str):
            raise TypeError("Expected argument 'db_cluster_parameter_group_name' to be a str")
        pulumi.set(__self__, "db_cluster_parameter_group_name", db_cluster_parameter_group_name)
        if db_cluster_resource_id and not isinstance(db_cluster_resource_id, str):
            raise TypeError("Expected argument 'db_cluster_resource_id' to be a str")
        pulumi.set(__self__, "db_cluster_resource_id", db_cluster_resource_id)
        if deletion_protection and not isinstance(deletion_protection, bool):
            raise TypeError("Expected argument 'deletion_protection' to be a bool")
        pulumi.set(__self__, "deletion_protection", deletion_protection)
        if domain and not isinstance(domain, str):
            raise TypeError("Expected argument 'domain' to be a str")
        pulumi.set(__self__, "domain", domain)
        if domain_iam_role_name and not isinstance(domain_iam_role_name, str):
            raise TypeError("Expected argument 'domain_iam_role_name' to be a str")
        pulumi.set(__self__, "domain_iam_role_name", domain_iam_role_name)
        if enable_cloudwatch_logs_exports and not isinstance(enable_cloudwatch_logs_exports, list):
            raise TypeError("Expected argument 'enable_cloudwatch_logs_exports' to be a list")
        pulumi.set(__self__, "enable_cloudwatch_logs_exports", enable_cloudwatch_logs_exports)
        if enable_http_endpoint and not isinstance(enable_http_endpoint, bool):
            raise TypeError("Expected argument 'enable_http_endpoint' to be a bool")
        pulumi.set(__self__, "enable_http_endpoint", enable_http_endpoint)
        if enable_iam_database_authentication and not isinstance(enable_iam_database_authentication, bool):
            raise TypeError("Expected argument 'enable_iam_database_authentication' to be a bool")
        pulumi.set(__self__, "enable_iam_database_authentication", enable_iam_database_authentication)
        if endpoint and not isinstance(endpoint, dict):
            raise TypeError("Expected argument 'endpoint' to be a dict")
        pulumi.set(__self__, "endpoint", endpoint)
        if engine and not isinstance(engine, str):
            raise TypeError("Expected argument 'engine' to be a str")
        pulumi.set(__self__, "engine", engine)
        if engine_version and not isinstance(engine_version, str):
            raise TypeError("Expected argument 'engine_version' to be a str")
        pulumi.set(__self__, "engine_version", engine_version)
        if global_cluster_identifier and not isinstance(global_cluster_identifier, str):
            raise TypeError("Expected argument 'global_cluster_identifier' to be a str")
        pulumi.set(__self__, "global_cluster_identifier", global_cluster_identifier)
        if iops and not isinstance(iops, int):
            raise TypeError("Expected argument 'iops' to be a int")
        pulumi.set(__self__, "iops", iops)
        if manage_master_user_password and not isinstance(manage_master_user_password, bool):
            raise TypeError("Expected argument 'manage_master_user_password' to be a bool")
        pulumi.set(__self__, "manage_master_user_password", manage_master_user_password)
        if master_user_secret and not isinstance(master_user_secret, dict):
            raise TypeError("Expected argument 'master_user_secret' to be a dict")
        pulumi.set(__self__, "master_user_secret", master_user_secret)
        if master_username and not isinstance(master_username, str):
            raise TypeError("Expected argument 'master_username' to be a str")
        pulumi.set(__self__, "master_username", master_username)
        if monitoring_interval and not isinstance(monitoring_interval, int):
            raise TypeError("Expected argument 'monitoring_interval' to be a int")
        pulumi.set(__self__, "monitoring_interval", monitoring_interval)
        if monitoring_role_arn and not isinstance(monitoring_role_arn, str):
            raise TypeError("Expected argument 'monitoring_role_arn' to be a str")
        pulumi.set(__self__, "monitoring_role_arn", monitoring_role_arn)
        if network_type and not isinstance(network_type, str):
            raise TypeError("Expected argument 'network_type' to be a str")
        pulumi.set(__self__, "network_type", network_type)
        if performance_insights_enabled and not isinstance(performance_insights_enabled, bool):
            raise TypeError("Expected argument 'performance_insights_enabled' to be a bool")
        pulumi.set(__self__, "performance_insights_enabled", performance_insights_enabled)
        if performance_insights_kms_key_id and not isinstance(performance_insights_kms_key_id, str):
            raise TypeError("Expected argument 'performance_insights_kms_key_id' to be a str")
        pulumi.set(__self__, "performance_insights_kms_key_id", performance_insights_kms_key_id)
        if performance_insights_retention_period and not isinstance(performance_insights_retention_period, int):
            raise TypeError("Expected argument 'performance_insights_retention_period' to be a int")
        pulumi.set(__self__, "performance_insights_retention_period", performance_insights_retention_period)
        if port and not isinstance(port, int):
            raise TypeError("Expected argument 'port' to be a int")
        pulumi.set(__self__, "port", port)
        if preferred_backup_window and not isinstance(preferred_backup_window, str):
            raise TypeError("Expected argument 'preferred_backup_window' to be a str")
        pulumi.set(__self__, "preferred_backup_window", preferred_backup_window)
        if preferred_maintenance_window and not isinstance(preferred_maintenance_window, str):
            raise TypeError("Expected argument 'preferred_maintenance_window' to be a str")
        pulumi.set(__self__, "preferred_maintenance_window", preferred_maintenance_window)
        if read_endpoint and not isinstance(read_endpoint, dict):
            raise TypeError("Expected argument 'read_endpoint' to be a dict")
        pulumi.set(__self__, "read_endpoint", read_endpoint)
        if replication_source_identifier and not isinstance(replication_source_identifier, str):
            raise TypeError("Expected argument 'replication_source_identifier' to be a str")
        pulumi.set(__self__, "replication_source_identifier", replication_source_identifier)
        if scaling_configuration and not isinstance(scaling_configuration, dict):
            raise TypeError("Expected argument 'scaling_configuration' to be a dict")
        pulumi.set(__self__, "scaling_configuration", scaling_configuration)
        if serverless_v2_scaling_configuration and not isinstance(serverless_v2_scaling_configuration, dict):
            raise TypeError("Expected argument 'serverless_v2_scaling_configuration' to be a dict")
        pulumi.set(__self__, "serverless_v2_scaling_configuration", serverless_v2_scaling_configuration)
        if storage_type and not isinstance(storage_type, str):
            raise TypeError("Expected argument 'storage_type' to be a str")
        pulumi.set(__self__, "storage_type", storage_type)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if vpc_security_group_ids and not isinstance(vpc_security_group_ids, list):
            raise TypeError("Expected argument 'vpc_security_group_ids' to be a list")
        pulumi.set(__self__, "vpc_security_group_ids", vpc_security_group_ids)

    @property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> Optional[int]:
        """
        The amount of storage in gibibytes (GiB) to allocate to each DB instance in the Multi-AZ DB cluster.
        """
        return pulumi.get(self, "allocated_storage")

    @property
    @pulumi.getter(name="associatedRoles")
    def associated_roles(self) -> Optional[Sequence['outputs.DbClusterDbClusterRole']]:
        """
        Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other AWS services on your behalf.
        """
        return pulumi.get(self, "associated_roles")

    @property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> Optional[bool]:
        """
        A value that indicates whether minor engine upgrades are applied automatically to the DB cluster during the maintenance window. By default, minor engine upgrades are applied automatically.
        """
        return pulumi.get(self, "auto_minor_version_upgrade")

    @property
    @pulumi.getter(name="backtrackWindow")
    def backtrack_window(self) -> Optional[int]:
        """
        The target backtrack window, in seconds. To disable backtracking, set this value to 0.
        """
        return pulumi.get(self, "backtrack_window")

    @property
    @pulumi.getter(name="backupRetentionPeriod")
    def backup_retention_period(self) -> Optional[int]:
        """
        The number of days for which automated backups are retained.
        """
        return pulumi.get(self, "backup_retention_period")

    @property
    @pulumi.getter(name="copyTagsToSnapshot")
    def copy_tags_to_snapshot(self) -> Optional[bool]:
        """
        A value that indicates whether to copy all tags from the DB cluster to snapshots of the DB cluster. The default is not to copy them.
        """
        return pulumi.get(self, "copy_tags_to_snapshot")

    @property
    @pulumi.getter(name="dbClusterArn")
    def db_cluster_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) for the DB cluster.
        """
        return pulumi.get(self, "db_cluster_arn")

    @property
    @pulumi.getter(name="dbClusterInstanceClass")
    def db_cluster_instance_class(self) -> Optional[str]:
        """
        The compute and memory capacity of each DB instance in the Multi-AZ DB cluster, for example db.m6g.xlarge.
        """
        return pulumi.get(self, "db_cluster_instance_class")

    @property
    @pulumi.getter(name="dbClusterParameterGroupName")
    def db_cluster_parameter_group_name(self) -> Optional[str]:
        """
        The name of the DB cluster parameter group to associate with this DB cluster.
        """
        return pulumi.get(self, "db_cluster_parameter_group_name")

    @property
    @pulumi.getter(name="dbClusterResourceId")
    def db_cluster_resource_id(self) -> Optional[str]:
        """
        The AWS Region-unique, immutable identifier for the DB cluster.
        """
        return pulumi.get(self, "db_cluster_resource_id")

    @property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[bool]:
        """
        A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
        """
        return pulumi.get(self, "deletion_protection")

    @property
    @pulumi.getter
    def domain(self) -> Optional[str]:
        """
        The Active Directory directory ID to create the DB cluster in.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="domainIamRoleName")
    def domain_iam_role_name(self) -> Optional[str]:
        """
        Specify the name of the IAM role to be used when making API calls to the Directory Service.
        """
        return pulumi.get(self, "domain_iam_role_name")

    @property
    @pulumi.getter(name="enableCloudwatchLogsExports")
    def enable_cloudwatch_logs_exports(self) -> Optional[Sequence[str]]:
        """
        The list of log types that need to be enabled for exporting to CloudWatch Logs. The values in the list depend on the DB engine being used. For more information, see Publishing Database Logs to Amazon CloudWatch Logs in the Amazon Aurora User Guide.
        """
        return pulumi.get(self, "enable_cloudwatch_logs_exports")

    @property
    @pulumi.getter(name="enableHttpEndpoint")
    def enable_http_endpoint(self) -> Optional[bool]:
        """
        A value that indicates whether to enable the HTTP endpoint for an Aurora Serverless DB cluster. By default, the HTTP endpoint is disabled.
        """
        return pulumi.get(self, "enable_http_endpoint")

    @property
    @pulumi.getter(name="enableIamDatabaseAuthentication")
    def enable_iam_database_authentication(self) -> Optional[bool]:
        """
        A value that indicates whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping is disabled.
        """
        return pulumi.get(self, "enable_iam_database_authentication")

    @property
    @pulumi.getter
    def endpoint(self) -> Optional['outputs.DbClusterEndpoint']:
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def engine(self) -> Optional[str]:
        """
        The name of the database engine to be used for this DB cluster. Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora), and aurora-postgresql
        """
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[str]:
        """
        The version number of the database engine to use.
        """
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter(name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> Optional[str]:
        """
        If you are configuring an Aurora global database cluster and want your Aurora DB cluster to be a secondary member in the global database cluster, specify the global cluster ID of the global database cluster. To define the primary database cluster of the global cluster, use the AWS::RDS::GlobalCluster resource.

        If you aren't configuring a global database cluster, don't specify this property.
        """
        return pulumi.get(self, "global_cluster_identifier")

    @property
    @pulumi.getter
    def iops(self) -> Optional[int]:
        """
        The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for each DB instance in the Multi-AZ DB cluster.
        """
        return pulumi.get(self, "iops")

    @property
    @pulumi.getter(name="manageMasterUserPassword")
    def manage_master_user_password(self) -> Optional[bool]:
        """
        A value that indicates whether to manage the master user password with AWS Secrets Manager.
        """
        return pulumi.get(self, "manage_master_user_password")

    @property
    @pulumi.getter(name="masterUserSecret")
    def master_user_secret(self) -> Optional['outputs.DbClusterMasterUserSecret']:
        """
        Contains the secret managed by RDS in AWS Secrets Manager for the master user password.
        """
        return pulumi.get(self, "master_user_secret")

    @property
    @pulumi.getter(name="masterUsername")
    def master_username(self) -> Optional[str]:
        """
        The name of the master user for the DB cluster. You must specify MasterUsername, unless you specify SnapshotIdentifier. In that case, don't specify MasterUsername.
        """
        return pulumi.get(self, "master_username")

    @property
    @pulumi.getter(name="monitoringInterval")
    def monitoring_interval(self) -> Optional[int]:
        """
        The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB cluster. To turn off collecting Enhanced Monitoring metrics, specify 0. The default is 0.
        """
        return pulumi.get(self, "monitoring_interval")

    @property
    @pulumi.getter(name="monitoringRoleArn")
    def monitoring_role_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.
        """
        return pulumi.get(self, "monitoring_role_arn")

    @property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[str]:
        """
        The network type of the DB cluster.
        """
        return pulumi.get(self, "network_type")

    @property
    @pulumi.getter(name="performanceInsightsEnabled")
    def performance_insights_enabled(self) -> Optional[bool]:
        """
        A value that indicates whether to turn on Performance Insights for the DB cluster.
        """
        return pulumi.get(self, "performance_insights_enabled")

    @property
    @pulumi.getter(name="performanceInsightsKmsKeyId")
    def performance_insights_kms_key_id(self) -> Optional[str]:
        """
        The Amazon Web Services KMS key identifier for encryption of Performance Insights data.
        """
        return pulumi.get(self, "performance_insights_kms_key_id")

    @property
    @pulumi.getter(name="performanceInsightsRetentionPeriod")
    def performance_insights_retention_period(self) -> Optional[int]:
        """
        The amount of time, in days, to retain Performance Insights data.
        """
        return pulumi.get(self, "performance_insights_retention_period")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        """
        The port number on which the instances in the DB cluster accept connections. Default: 3306 if engine is set as aurora or 5432 if set to aurora-postgresql.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> Optional[str]:
        """
        The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter. The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. To see the time blocks available, see Adjusting the Preferred DB Cluster Maintenance Window in the Amazon Aurora User Guide.
        """
        return pulumi.get(self, "preferred_backup_window")

    @property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[str]:
        """
        The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC). The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week. To see the time blocks available, see Adjusting the Preferred DB Cluster Maintenance Window in the Amazon Aurora User Guide.
        """
        return pulumi.get(self, "preferred_maintenance_window")

    @property
    @pulumi.getter(name="readEndpoint")
    def read_endpoint(self) -> Optional['outputs.DbClusterReadEndpoint']:
        return pulumi.get(self, "read_endpoint")

    @property
    @pulumi.getter(name="replicationSourceIdentifier")
    def replication_source_identifier(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the source DB instance or DB cluster if this DB cluster is created as a Read Replica.
        """
        return pulumi.get(self, "replication_source_identifier")

    @property
    @pulumi.getter(name="scalingConfiguration")
    def scaling_configuration(self) -> Optional['outputs.DbClusterScalingConfiguration']:
        """
        The ScalingConfiguration property type specifies the scaling configuration of an Aurora Serverless DB cluster.
        """
        return pulumi.get(self, "scaling_configuration")

    @property
    @pulumi.getter(name="serverlessV2ScalingConfiguration")
    def serverless_v2_scaling_configuration(self) -> Optional['outputs.DbClusterServerlessV2ScalingConfiguration']:
        """
        Contains the scaling configuration of an Aurora Serverless v2 DB cluster.
        """
        return pulumi.get(self, "serverless_v2_scaling_configuration")

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[str]:
        """
        Specifies the storage type to be associated with the DB cluster.
        """
        return pulumi.get(self, "storage_type")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.DbClusterTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[Sequence[str]]:
        """
        A list of EC2 VPC security groups to associate with this DB cluster.
        """
        return pulumi.get(self, "vpc_security_group_ids")


class AwaitableGetDbClusterResult(GetDbClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDbClusterResult(
            allocated_storage=self.allocated_storage,
            associated_roles=self.associated_roles,
            auto_minor_version_upgrade=self.auto_minor_version_upgrade,
            backtrack_window=self.backtrack_window,
            backup_retention_period=self.backup_retention_period,
            copy_tags_to_snapshot=self.copy_tags_to_snapshot,
            db_cluster_arn=self.db_cluster_arn,
            db_cluster_instance_class=self.db_cluster_instance_class,
            db_cluster_parameter_group_name=self.db_cluster_parameter_group_name,
            db_cluster_resource_id=self.db_cluster_resource_id,
            deletion_protection=self.deletion_protection,
            domain=self.domain,
            domain_iam_role_name=self.domain_iam_role_name,
            enable_cloudwatch_logs_exports=self.enable_cloudwatch_logs_exports,
            enable_http_endpoint=self.enable_http_endpoint,
            enable_iam_database_authentication=self.enable_iam_database_authentication,
            endpoint=self.endpoint,
            engine=self.engine,
            engine_version=self.engine_version,
            global_cluster_identifier=self.global_cluster_identifier,
            iops=self.iops,
            manage_master_user_password=self.manage_master_user_password,
            master_user_secret=self.master_user_secret,
            master_username=self.master_username,
            monitoring_interval=self.monitoring_interval,
            monitoring_role_arn=self.monitoring_role_arn,
            network_type=self.network_type,
            performance_insights_enabled=self.performance_insights_enabled,
            performance_insights_kms_key_id=self.performance_insights_kms_key_id,
            performance_insights_retention_period=self.performance_insights_retention_period,
            port=self.port,
            preferred_backup_window=self.preferred_backup_window,
            preferred_maintenance_window=self.preferred_maintenance_window,
            read_endpoint=self.read_endpoint,
            replication_source_identifier=self.replication_source_identifier,
            scaling_configuration=self.scaling_configuration,
            serverless_v2_scaling_configuration=self.serverless_v2_scaling_configuration,
            storage_type=self.storage_type,
            tags=self.tags,
            vpc_security_group_ids=self.vpc_security_group_ids)


def get_db_cluster(db_cluster_identifier: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDbClusterResult:
    """
    The AWS::RDS::DBCluster resource creates an Amazon Aurora DB cluster.


    :param str db_cluster_identifier: The DB cluster identifier. This parameter is stored as a lowercase string.
    """
    __args__ = dict()
    __args__['dbClusterIdentifier'] = db_cluster_identifier
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:rds:getDbCluster', __args__, opts=opts, typ=GetDbClusterResult).value

    return AwaitableGetDbClusterResult(
        allocated_storage=pulumi.get(__ret__, 'allocated_storage'),
        associated_roles=pulumi.get(__ret__, 'associated_roles'),
        auto_minor_version_upgrade=pulumi.get(__ret__, 'auto_minor_version_upgrade'),
        backtrack_window=pulumi.get(__ret__, 'backtrack_window'),
        backup_retention_period=pulumi.get(__ret__, 'backup_retention_period'),
        copy_tags_to_snapshot=pulumi.get(__ret__, 'copy_tags_to_snapshot'),
        db_cluster_arn=pulumi.get(__ret__, 'db_cluster_arn'),
        db_cluster_instance_class=pulumi.get(__ret__, 'db_cluster_instance_class'),
        db_cluster_parameter_group_name=pulumi.get(__ret__, 'db_cluster_parameter_group_name'),
        db_cluster_resource_id=pulumi.get(__ret__, 'db_cluster_resource_id'),
        deletion_protection=pulumi.get(__ret__, 'deletion_protection'),
        domain=pulumi.get(__ret__, 'domain'),
        domain_iam_role_name=pulumi.get(__ret__, 'domain_iam_role_name'),
        enable_cloudwatch_logs_exports=pulumi.get(__ret__, 'enable_cloudwatch_logs_exports'),
        enable_http_endpoint=pulumi.get(__ret__, 'enable_http_endpoint'),
        enable_iam_database_authentication=pulumi.get(__ret__, 'enable_iam_database_authentication'),
        endpoint=pulumi.get(__ret__, 'endpoint'),
        engine=pulumi.get(__ret__, 'engine'),
        engine_version=pulumi.get(__ret__, 'engine_version'),
        global_cluster_identifier=pulumi.get(__ret__, 'global_cluster_identifier'),
        iops=pulumi.get(__ret__, 'iops'),
        manage_master_user_password=pulumi.get(__ret__, 'manage_master_user_password'),
        master_user_secret=pulumi.get(__ret__, 'master_user_secret'),
        master_username=pulumi.get(__ret__, 'master_username'),
        monitoring_interval=pulumi.get(__ret__, 'monitoring_interval'),
        monitoring_role_arn=pulumi.get(__ret__, 'monitoring_role_arn'),
        network_type=pulumi.get(__ret__, 'network_type'),
        performance_insights_enabled=pulumi.get(__ret__, 'performance_insights_enabled'),
        performance_insights_kms_key_id=pulumi.get(__ret__, 'performance_insights_kms_key_id'),
        performance_insights_retention_period=pulumi.get(__ret__, 'performance_insights_retention_period'),
        port=pulumi.get(__ret__, 'port'),
        preferred_backup_window=pulumi.get(__ret__, 'preferred_backup_window'),
        preferred_maintenance_window=pulumi.get(__ret__, 'preferred_maintenance_window'),
        read_endpoint=pulumi.get(__ret__, 'read_endpoint'),
        replication_source_identifier=pulumi.get(__ret__, 'replication_source_identifier'),
        scaling_configuration=pulumi.get(__ret__, 'scaling_configuration'),
        serverless_v2_scaling_configuration=pulumi.get(__ret__, 'serverless_v2_scaling_configuration'),
        storage_type=pulumi.get(__ret__, 'storage_type'),
        tags=pulumi.get(__ret__, 'tags'),
        vpc_security_group_ids=pulumi.get(__ret__, 'vpc_security_group_ids'))


@_utilities.lift_output_func(get_db_cluster)
def get_db_cluster_output(db_cluster_identifier: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDbClusterResult]:
    """
    The AWS::RDS::DBCluster resource creates an Amazon Aurora DB cluster.


    :param str db_cluster_identifier: The DB cluster identifier. This parameter is stored as a lowercase string.
    """
    ...
