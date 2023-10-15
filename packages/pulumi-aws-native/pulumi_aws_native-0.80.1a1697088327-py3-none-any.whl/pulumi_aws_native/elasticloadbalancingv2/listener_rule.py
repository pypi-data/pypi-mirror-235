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

__all__ = ['ListenerRuleArgs', 'ListenerRule']

@pulumi.input_type
class ListenerRuleArgs:
    def __init__(__self__, *,
                 actions: pulumi.Input[Sequence[pulumi.Input['ListenerRuleActionArgs']]],
                 conditions: pulumi.Input[Sequence[pulumi.Input['ListenerRuleRuleConditionArgs']]],
                 priority: pulumi.Input[int],
                 listener_arn: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ListenerRule resource.
        """
        ListenerRuleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            actions=actions,
            conditions=conditions,
            priority=priority,
            listener_arn=listener_arn,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             actions: pulumi.Input[Sequence[pulumi.Input['ListenerRuleActionArgs']]],
             conditions: pulumi.Input[Sequence[pulumi.Input['ListenerRuleRuleConditionArgs']]],
             priority: pulumi.Input[int],
             listener_arn: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("actions", actions)
        _setter("conditions", conditions)
        _setter("priority", priority)
        if listener_arn is not None:
            _setter("listener_arn", listener_arn)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input['ListenerRuleActionArgs']]]:
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input['ListenerRuleActionArgs']]]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter
    def conditions(self) -> pulumi.Input[Sequence[pulumi.Input['ListenerRuleRuleConditionArgs']]]:
        return pulumi.get(self, "conditions")

    @conditions.setter
    def conditions(self, value: pulumi.Input[Sequence[pulumi.Input['ListenerRuleRuleConditionArgs']]]):
        pulumi.set(self, "conditions", value)

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Input[int]:
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: pulumi.Input[int]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="listenerArn")
    def listener_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "listener_arn")

    @listener_arn.setter
    def listener_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "listener_arn", value)


class ListenerRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ListenerRuleActionArgs']]]]] = None,
                 conditions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ListenerRuleRuleConditionArgs']]]]] = None,
                 listener_arn: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::ElasticLoadBalancingV2::ListenerRule

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ListenerRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::ElasticLoadBalancingV2::ListenerRule

        :param str resource_name: The name of the resource.
        :param ListenerRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ListenerRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ListenerRuleArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ListenerRuleActionArgs']]]]] = None,
                 conditions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ListenerRuleRuleConditionArgs']]]]] = None,
                 listener_arn: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ListenerRuleArgs.__new__(ListenerRuleArgs)

            if actions is None and not opts.urn:
                raise TypeError("Missing required property 'actions'")
            __props__.__dict__["actions"] = actions
            if conditions is None and not opts.urn:
                raise TypeError("Missing required property 'conditions'")
            __props__.__dict__["conditions"] = conditions
            __props__.__dict__["listener_arn"] = listener_arn
            if priority is None and not opts.urn:
                raise TypeError("Missing required property 'priority'")
            __props__.__dict__["priority"] = priority
            __props__.__dict__["is_default"] = None
            __props__.__dict__["rule_arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["listener_arn"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ListenerRule, __self__).__init__(
            'aws-native:elasticloadbalancingv2:ListenerRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ListenerRule':
        """
        Get an existing ListenerRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ListenerRuleArgs.__new__(ListenerRuleArgs)

        __props__.__dict__["actions"] = None
        __props__.__dict__["conditions"] = None
        __props__.__dict__["is_default"] = None
        __props__.__dict__["listener_arn"] = None
        __props__.__dict__["priority"] = None
        __props__.__dict__["rule_arn"] = None
        return ListenerRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Sequence['outputs.ListenerRuleAction']]:
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def conditions(self) -> pulumi.Output[Sequence['outputs.ListenerRuleRuleCondition']]:
        return pulumi.get(self, "conditions")

    @property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "is_default")

    @property
    @pulumi.getter(name="listenerArn")
    def listener_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "listener_arn")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="ruleArn")
    def rule_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "rule_arn")

