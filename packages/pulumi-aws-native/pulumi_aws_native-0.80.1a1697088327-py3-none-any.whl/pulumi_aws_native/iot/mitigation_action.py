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

__all__ = ['MitigationActionArgs', 'MitigationAction']

@pulumi.input_type
class MitigationActionArgs:
    def __init__(__self__, *,
                 action_params: pulumi.Input['MitigationActionActionParamsArgs'],
                 role_arn: pulumi.Input[str],
                 action_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['MitigationActionTagArgs']]]] = None):
        """
        The set of arguments for constructing a MitigationAction resource.
        :param pulumi.Input[str] action_name: A unique identifier for the mitigation action.
        :param pulumi.Input[Sequence[pulumi.Input['MitigationActionTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        MitigationActionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            action_params=action_params,
            role_arn=role_arn,
            action_name=action_name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             action_params: pulumi.Input['MitigationActionActionParamsArgs'],
             role_arn: pulumi.Input[str],
             action_name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['MitigationActionTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("action_params", action_params)
        _setter("role_arn", role_arn)
        if action_name is not None:
            _setter("action_name", action_name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="actionParams")
    def action_params(self) -> pulumi.Input['MitigationActionActionParamsArgs']:
        return pulumi.get(self, "action_params")

    @action_params.setter
    def action_params(self, value: pulumi.Input['MitigationActionActionParamsArgs']):
        pulumi.set(self, "action_params", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="actionName")
    def action_name(self) -> Optional[pulumi.Input[str]]:
        """
        A unique identifier for the mitigation action.
        """
        return pulumi.get(self, "action_name")

    @action_name.setter
    def action_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MitigationActionTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MitigationActionTagArgs']]]]):
        pulumi.set(self, "tags", value)


class MitigationAction(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_name: Optional[pulumi.Input[str]] = None,
                 action_params: Optional[pulumi.Input[pulumi.InputType['MitigationActionActionParamsArgs']]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MitigationActionTagArgs']]]]] = None,
                 __props__=None):
        """
        Mitigation actions can be used to take actions to mitigate issues that were found in an Audit finding or Detect violation.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action_name: A unique identifier for the mitigation action.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MitigationActionTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MitigationActionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Mitigation actions can be used to take actions to mitigate issues that were found in an Audit finding or Detect violation.

        :param str resource_name: The name of the resource.
        :param MitigationActionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MitigationActionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            MitigationActionArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_name: Optional[pulumi.Input[str]] = None,
                 action_params: Optional[pulumi.Input[pulumi.InputType['MitigationActionActionParamsArgs']]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MitigationActionTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MitigationActionArgs.__new__(MitigationActionArgs)

            __props__.__dict__["action_name"] = action_name
            if action_params is not None and not isinstance(action_params, MitigationActionActionParamsArgs):
                action_params = action_params or {}
                def _setter(key, value):
                    action_params[key] = value
                MitigationActionActionParamsArgs._configure(_setter, **action_params)
            if action_params is None and not opts.urn:
                raise TypeError("Missing required property 'action_params'")
            __props__.__dict__["action_params"] = action_params
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
            __props__.__dict__["tags"] = tags
            __props__.__dict__["mitigation_action_arn"] = None
            __props__.__dict__["mitigation_action_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["action_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(MitigationAction, __self__).__init__(
            'aws-native:iot:MitigationAction',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'MitigationAction':
        """
        Get an existing MitigationAction resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MitigationActionArgs.__new__(MitigationActionArgs)

        __props__.__dict__["action_name"] = None
        __props__.__dict__["action_params"] = None
        __props__.__dict__["mitigation_action_arn"] = None
        __props__.__dict__["mitigation_action_id"] = None
        __props__.__dict__["role_arn"] = None
        __props__.__dict__["tags"] = None
        return MitigationAction(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="actionName")
    def action_name(self) -> pulumi.Output[Optional[str]]:
        """
        A unique identifier for the mitigation action.
        """
        return pulumi.get(self, "action_name")

    @property
    @pulumi.getter(name="actionParams")
    def action_params(self) -> pulumi.Output['outputs.MitigationActionActionParams']:
        return pulumi.get(self, "action_params")

    @property
    @pulumi.getter(name="mitigationActionArn")
    def mitigation_action_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "mitigation_action_arn")

    @property
    @pulumi.getter(name="mitigationActionId")
    def mitigation_action_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "mitigation_action_id")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.MitigationActionTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

