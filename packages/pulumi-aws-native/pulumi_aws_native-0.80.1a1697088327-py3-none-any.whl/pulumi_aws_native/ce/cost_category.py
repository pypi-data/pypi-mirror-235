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

__all__ = ['CostCategoryArgs', 'CostCategory']

@pulumi.input_type
class CostCategoryArgs:
    def __init__(__self__, *,
                 rule_version: pulumi.Input['CostCategoryRuleVersion'],
                 rules: pulumi.Input[str],
                 default_value: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 split_charge_rules: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CostCategory resource.
        :param pulumi.Input[str] rules: JSON array format of Expression in Billing and Cost Management API
        :param pulumi.Input[str] default_value: The default value for the cost category
        :param pulumi.Input[str] split_charge_rules: Json array format of CostCategorySplitChargeRule in Billing and Cost Management API
        """
        CostCategoryArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            rule_version=rule_version,
            rules=rules,
            default_value=default_value,
            name=name,
            split_charge_rules=split_charge_rules,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             rule_version: pulumi.Input['CostCategoryRuleVersion'],
             rules: pulumi.Input[str],
             default_value: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             split_charge_rules: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("rule_version", rule_version)
        _setter("rules", rules)
        if default_value is not None:
            _setter("default_value", default_value)
        if name is not None:
            _setter("name", name)
        if split_charge_rules is not None:
            _setter("split_charge_rules", split_charge_rules)

    @property
    @pulumi.getter(name="ruleVersion")
    def rule_version(self) -> pulumi.Input['CostCategoryRuleVersion']:
        return pulumi.get(self, "rule_version")

    @rule_version.setter
    def rule_version(self, value: pulumi.Input['CostCategoryRuleVersion']):
        pulumi.set(self, "rule_version", value)

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Input[str]:
        """
        JSON array format of Expression in Billing and Cost Management API
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: pulumi.Input[str]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[pulumi.Input[str]]:
        """
        The default value for the cost category
        """
        return pulumi.get(self, "default_value")

    @default_value.setter
    def default_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_value", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="splitChargeRules")
    def split_charge_rules(self) -> Optional[pulumi.Input[str]]:
        """
        Json array format of CostCategorySplitChargeRule in Billing and Cost Management API
        """
        return pulumi.get(self, "split_charge_rules")

    @split_charge_rules.setter
    def split_charge_rules(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "split_charge_rules", value)


class CostCategory(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_value: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rule_version: Optional[pulumi.Input['CostCategoryRuleVersion']] = None,
                 rules: Optional[pulumi.Input[str]] = None,
                 split_charge_rules: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Cost Category enables you to map your cost and usage into meaningful categories. You can use Cost Category to organize your costs using a rule-based engine.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_value: The default value for the cost category
        :param pulumi.Input[str] rules: JSON array format of Expression in Billing and Cost Management API
        :param pulumi.Input[str] split_charge_rules: Json array format of CostCategorySplitChargeRule in Billing and Cost Management API
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CostCategoryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Cost Category enables you to map your cost and usage into meaningful categories. You can use Cost Category to organize your costs using a rule-based engine.

        :param str resource_name: The name of the resource.
        :param CostCategoryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CostCategoryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            CostCategoryArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_value: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rule_version: Optional[pulumi.Input['CostCategoryRuleVersion']] = None,
                 rules: Optional[pulumi.Input[str]] = None,
                 split_charge_rules: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CostCategoryArgs.__new__(CostCategoryArgs)

            __props__.__dict__["default_value"] = default_value
            __props__.__dict__["name"] = name
            if rule_version is None and not opts.urn:
                raise TypeError("Missing required property 'rule_version'")
            __props__.__dict__["rule_version"] = rule_version
            if rules is None and not opts.urn:
                raise TypeError("Missing required property 'rules'")
            __props__.__dict__["rules"] = rules
            __props__.__dict__["split_charge_rules"] = split_charge_rules
            __props__.__dict__["arn"] = None
            __props__.__dict__["effective_start"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(CostCategory, __self__).__init__(
            'aws-native:ce:CostCategory',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CostCategory':
        """
        Get an existing CostCategory resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CostCategoryArgs.__new__(CostCategoryArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["default_value"] = None
        __props__.__dict__["effective_start"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["rule_version"] = None
        __props__.__dict__["rules"] = None
        __props__.__dict__["split_charge_rules"] = None
        return CostCategory(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Cost category ARN
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> pulumi.Output[Optional[str]]:
        """
        The default value for the cost category
        """
        return pulumi.get(self, "default_value")

    @property
    @pulumi.getter(name="effectiveStart")
    def effective_start(self) -> pulumi.Output[str]:
        return pulumi.get(self, "effective_start")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ruleVersion")
    def rule_version(self) -> pulumi.Output['CostCategoryRuleVersion']:
        return pulumi.get(self, "rule_version")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[str]:
        """
        JSON array format of Expression in Billing and Cost Management API
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter(name="splitChargeRules")
    def split_charge_rules(self) -> pulumi.Output[Optional[str]]:
        """
        Json array format of CostCategorySplitChargeRule in Billing and Cost Management API
        """
        return pulumi.get(self, "split_charge_rules")

