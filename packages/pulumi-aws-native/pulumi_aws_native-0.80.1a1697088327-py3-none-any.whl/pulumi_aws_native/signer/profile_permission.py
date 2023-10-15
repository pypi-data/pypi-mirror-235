# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ProfilePermissionArgs', 'ProfilePermission']

@pulumi.input_type
class ProfilePermissionArgs:
    def __init__(__self__, *,
                 action: pulumi.Input[str],
                 principal: pulumi.Input[str],
                 profile_name: pulumi.Input[str],
                 statement_id: pulumi.Input[str],
                 profile_version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ProfilePermission resource.
        """
        ProfilePermissionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            action=action,
            principal=principal,
            profile_name=profile_name,
            statement_id=statement_id,
            profile_version=profile_version,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             action: pulumi.Input[str],
             principal: pulumi.Input[str],
             profile_name: pulumi.Input[str],
             statement_id: pulumi.Input[str],
             profile_version: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("action", action)
        _setter("principal", principal)
        _setter("profile_name", profile_name)
        _setter("statement_id", statement_id)
        if profile_version is not None:
            _setter("profile_version", profile_version)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input[str]:
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input[str]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def principal(self) -> pulumi.Input[str]:
        return pulumi.get(self, "principal")

    @principal.setter
    def principal(self, value: pulumi.Input[str]):
        pulumi.set(self, "principal", value)

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "profile_name")

    @profile_name.setter
    def profile_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "profile_name", value)

    @property
    @pulumi.getter(name="statementId")
    def statement_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "statement_id")

    @statement_id.setter
    def statement_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "statement_id", value)

    @property
    @pulumi.getter(name="profileVersion")
    def profile_version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "profile_version")

    @profile_version.setter
    def profile_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "profile_version", value)


class ProfilePermission(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 principal: Optional[pulumi.Input[str]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 profile_version: Optional[pulumi.Input[str]] = None,
                 statement_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An example resource schema demonstrating some basic constructs and validation rules.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProfilePermissionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An example resource schema demonstrating some basic constructs and validation rules.

        :param str resource_name: The name of the resource.
        :param ProfilePermissionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProfilePermissionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ProfilePermissionArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 principal: Optional[pulumi.Input[str]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 profile_version: Optional[pulumi.Input[str]] = None,
                 statement_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProfilePermissionArgs.__new__(ProfilePermissionArgs)

            if action is None and not opts.urn:
                raise TypeError("Missing required property 'action'")
            __props__.__dict__["action"] = action
            if principal is None and not opts.urn:
                raise TypeError("Missing required property 'principal'")
            __props__.__dict__["principal"] = principal
            if profile_name is None and not opts.urn:
                raise TypeError("Missing required property 'profile_name'")
            __props__.__dict__["profile_name"] = profile_name
            __props__.__dict__["profile_version"] = profile_version
            if statement_id is None and not opts.urn:
                raise TypeError("Missing required property 'statement_id'")
            __props__.__dict__["statement_id"] = statement_id
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["action", "principal", "profile_name", "profile_version", "statement_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ProfilePermission, __self__).__init__(
            'aws-native:signer:ProfilePermission',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ProfilePermission':
        """
        Get an existing ProfilePermission resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProfilePermissionArgs.__new__(ProfilePermissionArgs)

        __props__.__dict__["action"] = None
        __props__.__dict__["principal"] = None
        __props__.__dict__["profile_name"] = None
        __props__.__dict__["profile_version"] = None
        __props__.__dict__["statement_id"] = None
        return ProfilePermission(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Output[str]:
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def principal(self) -> pulumi.Output[str]:
        return pulumi.get(self, "principal")

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "profile_name")

    @property
    @pulumi.getter(name="profileVersion")
    def profile_version(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "profile_version")

    @property
    @pulumi.getter(name="statementId")
    def statement_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "statement_id")

