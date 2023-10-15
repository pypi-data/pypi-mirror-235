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

__all__ = ['PermissionsArgs', 'Permissions']

@pulumi.input_type
class PermissionsArgs:
    def __init__(__self__, *,
                 data_lake_principal: pulumi.Input['PermissionsDataLakePrincipalArgs'],
                 resource: pulumi.Input['PermissionsResourceArgs'],
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 permissions_with_grant_option: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Permissions resource.
        """
        PermissionsArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            data_lake_principal=data_lake_principal,
            resource=resource,
            permissions=permissions,
            permissions_with_grant_option=permissions_with_grant_option,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             data_lake_principal: pulumi.Input['PermissionsDataLakePrincipalArgs'],
             resource: pulumi.Input['PermissionsResourceArgs'],
             permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             permissions_with_grant_option: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("data_lake_principal", data_lake_principal)
        _setter("resource", resource)
        if permissions is not None:
            _setter("permissions", permissions)
        if permissions_with_grant_option is not None:
            _setter("permissions_with_grant_option", permissions_with_grant_option)

    @property
    @pulumi.getter(name="dataLakePrincipal")
    def data_lake_principal(self) -> pulumi.Input['PermissionsDataLakePrincipalArgs']:
        return pulumi.get(self, "data_lake_principal")

    @data_lake_principal.setter
    def data_lake_principal(self, value: pulumi.Input['PermissionsDataLakePrincipalArgs']):
        pulumi.set(self, "data_lake_principal", value)

    @property
    @pulumi.getter
    def resource(self) -> pulumi.Input['PermissionsResourceArgs']:
        return pulumi.get(self, "resource")

    @resource.setter
    def resource(self, value: pulumi.Input['PermissionsResourceArgs']):
        pulumi.set(self, "resource", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter(name="permissionsWithGrantOption")
    def permissions_with_grant_option(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "permissions_with_grant_option")

    @permissions_with_grant_option.setter
    def permissions_with_grant_option(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "permissions_with_grant_option", value)


warnings.warn("""Permissions is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Permissions(pulumi.CustomResource):
    warnings.warn("""Permissions is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_lake_principal: Optional[pulumi.Input[pulumi.InputType['PermissionsDataLakePrincipalArgs']]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 permissions_with_grant_option: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource: Optional[pulumi.Input[pulumi.InputType['PermissionsResourceArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::LakeFormation::Permissions

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PermissionsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::LakeFormation::Permissions

        :param str resource_name: The name of the resource.
        :param PermissionsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PermissionsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            PermissionsArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_lake_principal: Optional[pulumi.Input[pulumi.InputType['PermissionsDataLakePrincipalArgs']]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 permissions_with_grant_option: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource: Optional[pulumi.Input[pulumi.InputType['PermissionsResourceArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""Permissions is deprecated: Permissions is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PermissionsArgs.__new__(PermissionsArgs)

            if data_lake_principal is not None and not isinstance(data_lake_principal, PermissionsDataLakePrincipalArgs):
                data_lake_principal = data_lake_principal or {}
                def _setter(key, value):
                    data_lake_principal[key] = value
                PermissionsDataLakePrincipalArgs._configure(_setter, **data_lake_principal)
            if data_lake_principal is None and not opts.urn:
                raise TypeError("Missing required property 'data_lake_principal'")
            __props__.__dict__["data_lake_principal"] = data_lake_principal
            __props__.__dict__["permissions"] = permissions
            __props__.__dict__["permissions_with_grant_option"] = permissions_with_grant_option
            if resource is not None and not isinstance(resource, PermissionsResourceArgs):
                resource = resource or {}
                def _setter(key, value):
                    resource[key] = value
                PermissionsResourceArgs._configure(_setter, **resource)
            if resource is None and not opts.urn:
                raise TypeError("Missing required property 'resource'")
            __props__.__dict__["resource"] = resource
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["data_lake_principal", "resource"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Permissions, __self__).__init__(
            'aws-native:lakeformation:Permissions',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Permissions':
        """
        Get an existing Permissions resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PermissionsArgs.__new__(PermissionsArgs)

        __props__.__dict__["data_lake_principal"] = None
        __props__.__dict__["permissions"] = None
        __props__.__dict__["permissions_with_grant_option"] = None
        __props__.__dict__["resource"] = None
        return Permissions(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dataLakePrincipal")
    def data_lake_principal(self) -> pulumi.Output['outputs.PermissionsDataLakePrincipal']:
        return pulumi.get(self, "data_lake_principal")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter(name="permissionsWithGrantOption")
    def permissions_with_grant_option(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "permissions_with_grant_option")

    @property
    @pulumi.getter
    def resource(self) -> pulumi.Output['outputs.PermissionsResource']:
        return pulumi.get(self, "resource")

