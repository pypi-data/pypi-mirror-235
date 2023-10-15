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

__all__ = ['DatabaseArgs', 'Database']

@pulumi.input_type
class DatabaseArgs:
    def __init__(__self__, *,
                 master_database_name: pulumi.Input[str],
                 master_username: pulumi.Input[str],
                 relational_database_blueprint_id: pulumi.Input[str],
                 relational_database_bundle_id: pulumi.Input[str],
                 relational_database_name: pulumi.Input[str],
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 backup_retention: Optional[pulumi.Input[bool]] = None,
                 ca_certificate_identifier: Optional[pulumi.Input[str]] = None,
                 master_user_password: Optional[pulumi.Input[str]] = None,
                 preferred_backup_window: Optional[pulumi.Input[str]] = None,
                 preferred_maintenance_window: Optional[pulumi.Input[str]] = None,
                 publicly_accessible: Optional[pulumi.Input[bool]] = None,
                 relational_database_parameters: Optional[pulumi.Input[Sequence[pulumi.Input['DatabaseRelationalDatabaseParameterArgs']]]] = None,
                 rotate_master_user_password: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DatabaseTagArgs']]]] = None):
        """
        The set of arguments for constructing a Database resource.
        :param pulumi.Input[str] master_database_name: The name of the database to create when the Lightsail database resource is created. For MySQL, if this parameter isn't specified, no database is created in the database resource. For PostgreSQL, if this parameter isn't specified, a database named postgres is created in the database resource.
        :param pulumi.Input[str] master_username: The name for the master user.
        :param pulumi.Input[str] relational_database_blueprint_id: The blueprint ID for your new database. A blueprint describes the major engine version of a database.
        :param pulumi.Input[str] relational_database_bundle_id: The bundle ID for your new database. A bundle describes the performance specifications for your database.
        :param pulumi.Input[str] relational_database_name: The name to use for your new Lightsail database resource.
        :param pulumi.Input[str] availability_zone: The Availability Zone in which to create your new database. Use the us-east-2a case-sensitive format.
        :param pulumi.Input[bool] backup_retention: When true, enables automated backup retention for your database. Updates are applied during the next maintenance window because this can result in an outage.
        :param pulumi.Input[str] ca_certificate_identifier: Indicates the certificate that needs to be associated with the database.
        :param pulumi.Input[str] master_user_password: The password for the master user. The password can include any printable ASCII character except "/", \"\"\", or "@". It cannot contain spaces.
        :param pulumi.Input[str] preferred_backup_window: The daily time range during which automated backups are created for your new database if automated backups are enabled.
        :param pulumi.Input[str] preferred_maintenance_window: The weekly time range during which system maintenance can occur on your new database.
        :param pulumi.Input[bool] publicly_accessible: Specifies the accessibility options for your new database. A value of true specifies a database that is available to resources outside of your Lightsail account. A value of false specifies a database that is available only to your Lightsail resources in the same region as your database.
        :param pulumi.Input[Sequence[pulumi.Input['DatabaseRelationalDatabaseParameterArgs']]] relational_database_parameters: Update one or more parameters of the relational database.
        :param pulumi.Input[bool] rotate_master_user_password: When true, the master user password is changed to a new strong password generated by Lightsail. Use the get relational database master user password operation to get the new password.
        :param pulumi.Input[Sequence[pulumi.Input['DatabaseTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        DatabaseArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            master_database_name=master_database_name,
            master_username=master_username,
            relational_database_blueprint_id=relational_database_blueprint_id,
            relational_database_bundle_id=relational_database_bundle_id,
            relational_database_name=relational_database_name,
            availability_zone=availability_zone,
            backup_retention=backup_retention,
            ca_certificate_identifier=ca_certificate_identifier,
            master_user_password=master_user_password,
            preferred_backup_window=preferred_backup_window,
            preferred_maintenance_window=preferred_maintenance_window,
            publicly_accessible=publicly_accessible,
            relational_database_parameters=relational_database_parameters,
            rotate_master_user_password=rotate_master_user_password,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             master_database_name: pulumi.Input[str],
             master_username: pulumi.Input[str],
             relational_database_blueprint_id: pulumi.Input[str],
             relational_database_bundle_id: pulumi.Input[str],
             relational_database_name: pulumi.Input[str],
             availability_zone: Optional[pulumi.Input[str]] = None,
             backup_retention: Optional[pulumi.Input[bool]] = None,
             ca_certificate_identifier: Optional[pulumi.Input[str]] = None,
             master_user_password: Optional[pulumi.Input[str]] = None,
             preferred_backup_window: Optional[pulumi.Input[str]] = None,
             preferred_maintenance_window: Optional[pulumi.Input[str]] = None,
             publicly_accessible: Optional[pulumi.Input[bool]] = None,
             relational_database_parameters: Optional[pulumi.Input[Sequence[pulumi.Input['DatabaseRelationalDatabaseParameterArgs']]]] = None,
             rotate_master_user_password: Optional[pulumi.Input[bool]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['DatabaseTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("master_database_name", master_database_name)
        _setter("master_username", master_username)
        _setter("relational_database_blueprint_id", relational_database_blueprint_id)
        _setter("relational_database_bundle_id", relational_database_bundle_id)
        _setter("relational_database_name", relational_database_name)
        if availability_zone is not None:
            _setter("availability_zone", availability_zone)
        if backup_retention is not None:
            _setter("backup_retention", backup_retention)
        if ca_certificate_identifier is not None:
            _setter("ca_certificate_identifier", ca_certificate_identifier)
        if master_user_password is not None:
            _setter("master_user_password", master_user_password)
        if preferred_backup_window is not None:
            _setter("preferred_backup_window", preferred_backup_window)
        if preferred_maintenance_window is not None:
            _setter("preferred_maintenance_window", preferred_maintenance_window)
        if publicly_accessible is not None:
            _setter("publicly_accessible", publicly_accessible)
        if relational_database_parameters is not None:
            _setter("relational_database_parameters", relational_database_parameters)
        if rotate_master_user_password is not None:
            _setter("rotate_master_user_password", rotate_master_user_password)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="masterDatabaseName")
    def master_database_name(self) -> pulumi.Input[str]:
        """
        The name of the database to create when the Lightsail database resource is created. For MySQL, if this parameter isn't specified, no database is created in the database resource. For PostgreSQL, if this parameter isn't specified, a database named postgres is created in the database resource.
        """
        return pulumi.get(self, "master_database_name")

    @master_database_name.setter
    def master_database_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "master_database_name", value)

    @property
    @pulumi.getter(name="masterUsername")
    def master_username(self) -> pulumi.Input[str]:
        """
        The name for the master user.
        """
        return pulumi.get(self, "master_username")

    @master_username.setter
    def master_username(self, value: pulumi.Input[str]):
        pulumi.set(self, "master_username", value)

    @property
    @pulumi.getter(name="relationalDatabaseBlueprintId")
    def relational_database_blueprint_id(self) -> pulumi.Input[str]:
        """
        The blueprint ID for your new database. A blueprint describes the major engine version of a database.
        """
        return pulumi.get(self, "relational_database_blueprint_id")

    @relational_database_blueprint_id.setter
    def relational_database_blueprint_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "relational_database_blueprint_id", value)

    @property
    @pulumi.getter(name="relationalDatabaseBundleId")
    def relational_database_bundle_id(self) -> pulumi.Input[str]:
        """
        The bundle ID for your new database. A bundle describes the performance specifications for your database.
        """
        return pulumi.get(self, "relational_database_bundle_id")

    @relational_database_bundle_id.setter
    def relational_database_bundle_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "relational_database_bundle_id", value)

    @property
    @pulumi.getter(name="relationalDatabaseName")
    def relational_database_name(self) -> pulumi.Input[str]:
        """
        The name to use for your new Lightsail database resource.
        """
        return pulumi.get(self, "relational_database_name")

    @relational_database_name.setter
    def relational_database_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "relational_database_name", value)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[str]]:
        """
        The Availability Zone in which to create your new database. Use the us-east-2a case-sensitive format.
        """
        return pulumi.get(self, "availability_zone")

    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability_zone", value)

    @property
    @pulumi.getter(name="backupRetention")
    def backup_retention(self) -> Optional[pulumi.Input[bool]]:
        """
        When true, enables automated backup retention for your database. Updates are applied during the next maintenance window because this can result in an outage.
        """
        return pulumi.get(self, "backup_retention")

    @backup_retention.setter
    def backup_retention(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "backup_retention", value)

    @property
    @pulumi.getter(name="caCertificateIdentifier")
    def ca_certificate_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates the certificate that needs to be associated with the database.
        """
        return pulumi.get(self, "ca_certificate_identifier")

    @ca_certificate_identifier.setter
    def ca_certificate_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ca_certificate_identifier", value)

    @property
    @pulumi.getter(name="masterUserPassword")
    def master_user_password(self) -> Optional[pulumi.Input[str]]:
        """
        The password for the master user. The password can include any printable ASCII character except "/", \"\"\", or "@". It cannot contain spaces.
        """
        return pulumi.get(self, "master_user_password")

    @master_user_password.setter
    def master_user_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "master_user_password", value)

    @property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> Optional[pulumi.Input[str]]:
        """
        The daily time range during which automated backups are created for your new database if automated backups are enabled.
        """
        return pulumi.get(self, "preferred_backup_window")

    @preferred_backup_window.setter
    def preferred_backup_window(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "preferred_backup_window", value)

    @property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[pulumi.Input[str]]:
        """
        The weekly time range during which system maintenance can occur on your new database.
        """
        return pulumi.get(self, "preferred_maintenance_window")

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "preferred_maintenance_window", value)

    @property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies the accessibility options for your new database. A value of true specifies a database that is available to resources outside of your Lightsail account. A value of false specifies a database that is available only to your Lightsail resources in the same region as your database.
        """
        return pulumi.get(self, "publicly_accessible")

    @publicly_accessible.setter
    def publicly_accessible(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "publicly_accessible", value)

    @property
    @pulumi.getter(name="relationalDatabaseParameters")
    def relational_database_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DatabaseRelationalDatabaseParameterArgs']]]]:
        """
        Update one or more parameters of the relational database.
        """
        return pulumi.get(self, "relational_database_parameters")

    @relational_database_parameters.setter
    def relational_database_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DatabaseRelationalDatabaseParameterArgs']]]]):
        pulumi.set(self, "relational_database_parameters", value)

    @property
    @pulumi.getter(name="rotateMasterUserPassword")
    def rotate_master_user_password(self) -> Optional[pulumi.Input[bool]]:
        """
        When true, the master user password is changed to a new strong password generated by Lightsail. Use the get relational database master user password operation to get the new password.
        """
        return pulumi.get(self, "rotate_master_user_password")

    @rotate_master_user_password.setter
    def rotate_master_user_password(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "rotate_master_user_password", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DatabaseTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DatabaseTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Database(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 backup_retention: Optional[pulumi.Input[bool]] = None,
                 ca_certificate_identifier: Optional[pulumi.Input[str]] = None,
                 master_database_name: Optional[pulumi.Input[str]] = None,
                 master_user_password: Optional[pulumi.Input[str]] = None,
                 master_username: Optional[pulumi.Input[str]] = None,
                 preferred_backup_window: Optional[pulumi.Input[str]] = None,
                 preferred_maintenance_window: Optional[pulumi.Input[str]] = None,
                 publicly_accessible: Optional[pulumi.Input[bool]] = None,
                 relational_database_blueprint_id: Optional[pulumi.Input[str]] = None,
                 relational_database_bundle_id: Optional[pulumi.Input[str]] = None,
                 relational_database_name: Optional[pulumi.Input[str]] = None,
                 relational_database_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DatabaseRelationalDatabaseParameterArgs']]]]] = None,
                 rotate_master_user_password: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DatabaseTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Lightsail::Database

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] availability_zone: The Availability Zone in which to create your new database. Use the us-east-2a case-sensitive format.
        :param pulumi.Input[bool] backup_retention: When true, enables automated backup retention for your database. Updates are applied during the next maintenance window because this can result in an outage.
        :param pulumi.Input[str] ca_certificate_identifier: Indicates the certificate that needs to be associated with the database.
        :param pulumi.Input[str] master_database_name: The name of the database to create when the Lightsail database resource is created. For MySQL, if this parameter isn't specified, no database is created in the database resource. For PostgreSQL, if this parameter isn't specified, a database named postgres is created in the database resource.
        :param pulumi.Input[str] master_user_password: The password for the master user. The password can include any printable ASCII character except "/", \"\"\", or "@". It cannot contain spaces.
        :param pulumi.Input[str] master_username: The name for the master user.
        :param pulumi.Input[str] preferred_backup_window: The daily time range during which automated backups are created for your new database if automated backups are enabled.
        :param pulumi.Input[str] preferred_maintenance_window: The weekly time range during which system maintenance can occur on your new database.
        :param pulumi.Input[bool] publicly_accessible: Specifies the accessibility options for your new database. A value of true specifies a database that is available to resources outside of your Lightsail account. A value of false specifies a database that is available only to your Lightsail resources in the same region as your database.
        :param pulumi.Input[str] relational_database_blueprint_id: The blueprint ID for your new database. A blueprint describes the major engine version of a database.
        :param pulumi.Input[str] relational_database_bundle_id: The bundle ID for your new database. A bundle describes the performance specifications for your database.
        :param pulumi.Input[str] relational_database_name: The name to use for your new Lightsail database resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DatabaseRelationalDatabaseParameterArgs']]]] relational_database_parameters: Update one or more parameters of the relational database.
        :param pulumi.Input[bool] rotate_master_user_password: When true, the master user password is changed to a new strong password generated by Lightsail. Use the get relational database master user password operation to get the new password.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DatabaseTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatabaseArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Lightsail::Database

        :param str resource_name: The name of the resource.
        :param DatabaseArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatabaseArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DatabaseArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 backup_retention: Optional[pulumi.Input[bool]] = None,
                 ca_certificate_identifier: Optional[pulumi.Input[str]] = None,
                 master_database_name: Optional[pulumi.Input[str]] = None,
                 master_user_password: Optional[pulumi.Input[str]] = None,
                 master_username: Optional[pulumi.Input[str]] = None,
                 preferred_backup_window: Optional[pulumi.Input[str]] = None,
                 preferred_maintenance_window: Optional[pulumi.Input[str]] = None,
                 publicly_accessible: Optional[pulumi.Input[bool]] = None,
                 relational_database_blueprint_id: Optional[pulumi.Input[str]] = None,
                 relational_database_bundle_id: Optional[pulumi.Input[str]] = None,
                 relational_database_name: Optional[pulumi.Input[str]] = None,
                 relational_database_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DatabaseRelationalDatabaseParameterArgs']]]]] = None,
                 rotate_master_user_password: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DatabaseTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DatabaseArgs.__new__(DatabaseArgs)

            __props__.__dict__["availability_zone"] = availability_zone
            __props__.__dict__["backup_retention"] = backup_retention
            __props__.__dict__["ca_certificate_identifier"] = ca_certificate_identifier
            if master_database_name is None and not opts.urn:
                raise TypeError("Missing required property 'master_database_name'")
            __props__.__dict__["master_database_name"] = master_database_name
            __props__.__dict__["master_user_password"] = master_user_password
            if master_username is None and not opts.urn:
                raise TypeError("Missing required property 'master_username'")
            __props__.__dict__["master_username"] = master_username
            __props__.__dict__["preferred_backup_window"] = preferred_backup_window
            __props__.__dict__["preferred_maintenance_window"] = preferred_maintenance_window
            __props__.__dict__["publicly_accessible"] = publicly_accessible
            if relational_database_blueprint_id is None and not opts.urn:
                raise TypeError("Missing required property 'relational_database_blueprint_id'")
            __props__.__dict__["relational_database_blueprint_id"] = relational_database_blueprint_id
            if relational_database_bundle_id is None and not opts.urn:
                raise TypeError("Missing required property 'relational_database_bundle_id'")
            __props__.__dict__["relational_database_bundle_id"] = relational_database_bundle_id
            if relational_database_name is None and not opts.urn:
                raise TypeError("Missing required property 'relational_database_name'")
            __props__.__dict__["relational_database_name"] = relational_database_name
            __props__.__dict__["relational_database_parameters"] = relational_database_parameters
            __props__.__dict__["rotate_master_user_password"] = rotate_master_user_password
            __props__.__dict__["tags"] = tags
            __props__.__dict__["database_arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["availability_zone", "master_database_name", "master_username", "relational_database_blueprint_id", "relational_database_bundle_id", "relational_database_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Database, __self__).__init__(
            'aws-native:lightsail:Database',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Database':
        """
        Get an existing Database resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DatabaseArgs.__new__(DatabaseArgs)

        __props__.__dict__["availability_zone"] = None
        __props__.__dict__["backup_retention"] = None
        __props__.__dict__["ca_certificate_identifier"] = None
        __props__.__dict__["database_arn"] = None
        __props__.__dict__["master_database_name"] = None
        __props__.__dict__["master_user_password"] = None
        __props__.__dict__["master_username"] = None
        __props__.__dict__["preferred_backup_window"] = None
        __props__.__dict__["preferred_maintenance_window"] = None
        __props__.__dict__["publicly_accessible"] = None
        __props__.__dict__["relational_database_blueprint_id"] = None
        __props__.__dict__["relational_database_bundle_id"] = None
        __props__.__dict__["relational_database_name"] = None
        __props__.__dict__["relational_database_parameters"] = None
        __props__.__dict__["rotate_master_user_password"] = None
        __props__.__dict__["tags"] = None
        return Database(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[Optional[str]]:
        """
        The Availability Zone in which to create your new database. Use the us-east-2a case-sensitive format.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="backupRetention")
    def backup_retention(self) -> pulumi.Output[Optional[bool]]:
        """
        When true, enables automated backup retention for your database. Updates are applied during the next maintenance window because this can result in an outage.
        """
        return pulumi.get(self, "backup_retention")

    @property
    @pulumi.getter(name="caCertificateIdentifier")
    def ca_certificate_identifier(self) -> pulumi.Output[Optional[str]]:
        """
        Indicates the certificate that needs to be associated with the database.
        """
        return pulumi.get(self, "ca_certificate_identifier")

    @property
    @pulumi.getter(name="databaseArn")
    def database_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "database_arn")

    @property
    @pulumi.getter(name="masterDatabaseName")
    def master_database_name(self) -> pulumi.Output[str]:
        """
        The name of the database to create when the Lightsail database resource is created. For MySQL, if this parameter isn't specified, no database is created in the database resource. For PostgreSQL, if this parameter isn't specified, a database named postgres is created in the database resource.
        """
        return pulumi.get(self, "master_database_name")

    @property
    @pulumi.getter(name="masterUserPassword")
    def master_user_password(self) -> pulumi.Output[Optional[str]]:
        """
        The password for the master user. The password can include any printable ASCII character except "/", \"\"\", or "@". It cannot contain spaces.
        """
        return pulumi.get(self, "master_user_password")

    @property
    @pulumi.getter(name="masterUsername")
    def master_username(self) -> pulumi.Output[str]:
        """
        The name for the master user.
        """
        return pulumi.get(self, "master_username")

    @property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> pulumi.Output[Optional[str]]:
        """
        The daily time range during which automated backups are created for your new database if automated backups are enabled.
        """
        return pulumi.get(self, "preferred_backup_window")

    @property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> pulumi.Output[Optional[str]]:
        """
        The weekly time range during which system maintenance can occur on your new database.
        """
        return pulumi.get(self, "preferred_maintenance_window")

    @property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies the accessibility options for your new database. A value of true specifies a database that is available to resources outside of your Lightsail account. A value of false specifies a database that is available only to your Lightsail resources in the same region as your database.
        """
        return pulumi.get(self, "publicly_accessible")

    @property
    @pulumi.getter(name="relationalDatabaseBlueprintId")
    def relational_database_blueprint_id(self) -> pulumi.Output[str]:
        """
        The blueprint ID for your new database. A blueprint describes the major engine version of a database.
        """
        return pulumi.get(self, "relational_database_blueprint_id")

    @property
    @pulumi.getter(name="relationalDatabaseBundleId")
    def relational_database_bundle_id(self) -> pulumi.Output[str]:
        """
        The bundle ID for your new database. A bundle describes the performance specifications for your database.
        """
        return pulumi.get(self, "relational_database_bundle_id")

    @property
    @pulumi.getter(name="relationalDatabaseName")
    def relational_database_name(self) -> pulumi.Output[str]:
        """
        The name to use for your new Lightsail database resource.
        """
        return pulumi.get(self, "relational_database_name")

    @property
    @pulumi.getter(name="relationalDatabaseParameters")
    def relational_database_parameters(self) -> pulumi.Output[Optional[Sequence['outputs.DatabaseRelationalDatabaseParameter']]]:
        """
        Update one or more parameters of the relational database.
        """
        return pulumi.get(self, "relational_database_parameters")

    @property
    @pulumi.getter(name="rotateMasterUserPassword")
    def rotate_master_user_password(self) -> pulumi.Output[Optional[bool]]:
        """
        When true, the master user password is changed to a new strong password generated by Lightsail. Use the get relational database master user password operation to get the new password.
        """
        return pulumi.get(self, "rotate_master_user_password")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DatabaseTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

