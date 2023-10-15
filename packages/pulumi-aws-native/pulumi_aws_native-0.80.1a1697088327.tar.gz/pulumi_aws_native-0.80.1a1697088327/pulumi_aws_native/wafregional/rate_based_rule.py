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

__all__ = ['RateBasedRuleArgs', 'RateBasedRule']

@pulumi.input_type
class RateBasedRuleArgs:
    def __init__(__self__, *,
                 metric_name: pulumi.Input[str],
                 rate_key: pulumi.Input[str],
                 rate_limit: pulumi.Input[int],
                 match_predicates: Optional[pulumi.Input[Sequence[pulumi.Input['RateBasedRulePredicateArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RateBasedRule resource.
        """
        RateBasedRuleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            metric_name=metric_name,
            rate_key=rate_key,
            rate_limit=rate_limit,
            match_predicates=match_predicates,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             metric_name: pulumi.Input[str],
             rate_key: pulumi.Input[str],
             rate_limit: pulumi.Input[int],
             match_predicates: Optional[pulumi.Input[Sequence[pulumi.Input['RateBasedRulePredicateArgs']]]] = None,
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("metric_name", metric_name)
        _setter("rate_key", rate_key)
        _setter("rate_limit", rate_limit)
        if match_predicates is not None:
            _setter("match_predicates", match_predicates)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "metric_name")

    @metric_name.setter
    def metric_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "metric_name", value)

    @property
    @pulumi.getter(name="rateKey")
    def rate_key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "rate_key")

    @rate_key.setter
    def rate_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "rate_key", value)

    @property
    @pulumi.getter(name="rateLimit")
    def rate_limit(self) -> pulumi.Input[int]:
        return pulumi.get(self, "rate_limit")

    @rate_limit.setter
    def rate_limit(self, value: pulumi.Input[int]):
        pulumi.set(self, "rate_limit", value)

    @property
    @pulumi.getter(name="matchPredicates")
    def match_predicates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RateBasedRulePredicateArgs']]]]:
        return pulumi.get(self, "match_predicates")

    @match_predicates.setter
    def match_predicates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RateBasedRulePredicateArgs']]]]):
        pulumi.set(self, "match_predicates", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


warnings.warn("""RateBasedRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class RateBasedRule(pulumi.CustomResource):
    warnings.warn("""RateBasedRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 match_predicates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RateBasedRulePredicateArgs']]]]] = None,
                 metric_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rate_key: Optional[pulumi.Input[str]] = None,
                 rate_limit: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::WAFRegional::RateBasedRule

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RateBasedRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::WAFRegional::RateBasedRule

        :param str resource_name: The name of the resource.
        :param RateBasedRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RateBasedRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            RateBasedRuleArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 match_predicates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RateBasedRulePredicateArgs']]]]] = None,
                 metric_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rate_key: Optional[pulumi.Input[str]] = None,
                 rate_limit: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        pulumi.log.warn("""RateBasedRule is deprecated: RateBasedRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RateBasedRuleArgs.__new__(RateBasedRuleArgs)

            __props__.__dict__["match_predicates"] = match_predicates
            if metric_name is None and not opts.urn:
                raise TypeError("Missing required property 'metric_name'")
            __props__.__dict__["metric_name"] = metric_name
            __props__.__dict__["name"] = name
            if rate_key is None and not opts.urn:
                raise TypeError("Missing required property 'rate_key'")
            __props__.__dict__["rate_key"] = rate_key
            if rate_limit is None and not opts.urn:
                raise TypeError("Missing required property 'rate_limit'")
            __props__.__dict__["rate_limit"] = rate_limit
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["metric_name", "name", "rate_key"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(RateBasedRule, __self__).__init__(
            'aws-native:wafregional:RateBasedRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RateBasedRule':
        """
        Get an existing RateBasedRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RateBasedRuleArgs.__new__(RateBasedRuleArgs)

        __props__.__dict__["match_predicates"] = None
        __props__.__dict__["metric_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["rate_key"] = None
        __props__.__dict__["rate_limit"] = None
        return RateBasedRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="matchPredicates")
    def match_predicates(self) -> pulumi.Output[Optional[Sequence['outputs.RateBasedRulePredicate']]]:
        return pulumi.get(self, "match_predicates")

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "metric_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="rateKey")
    def rate_key(self) -> pulumi.Output[str]:
        return pulumi.get(self, "rate_key")

    @property
    @pulumi.getter(name="rateLimit")
    def rate_limit(self) -> pulumi.Output[int]:
        return pulumi.get(self, "rate_limit")

