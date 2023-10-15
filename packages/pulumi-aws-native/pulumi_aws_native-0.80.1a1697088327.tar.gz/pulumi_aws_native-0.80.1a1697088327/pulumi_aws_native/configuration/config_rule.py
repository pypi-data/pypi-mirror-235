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

__all__ = ['ConfigRuleArgs', 'ConfigRule']

@pulumi.input_type
class ConfigRuleArgs:
    def __init__(__self__, *,
                 source: pulumi.Input['ConfigRuleSourceArgs'],
                 compliance: Optional[pulumi.Input['CompliancePropertiesArgs']] = None,
                 config_rule_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 evaluation_modes: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigRuleEvaluationModeConfigurationArgs']]]] = None,
                 input_parameters: Optional[pulumi.Input[str]] = None,
                 maximum_execution_frequency: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input['ConfigRuleScopeArgs']] = None):
        """
        The set of arguments for constructing a ConfigRule resource.
        :param pulumi.Input['ConfigRuleSourceArgs'] source: Source of events for the AWS Config rule
        :param pulumi.Input['CompliancePropertiesArgs'] compliance: Compliance details of the Config rule
        :param pulumi.Input[str] config_rule_name: Name for the AWS Config rule
        :param pulumi.Input[str] description: Description provided for the AWS Config rule
        :param pulumi.Input[Sequence[pulumi.Input['ConfigRuleEvaluationModeConfigurationArgs']]] evaluation_modes: List of EvaluationModeConfiguration objects
        :param pulumi.Input[str] input_parameters: JSON string passed the Lambda function
        :param pulumi.Input[str] maximum_execution_frequency: Maximum frequency at which the rule has to be evaluated
        :param pulumi.Input['ConfigRuleScopeArgs'] scope: Scope to constrain which resources can trigger the AWS Config rule
        """
        ConfigRuleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            source=source,
            compliance=compliance,
            config_rule_name=config_rule_name,
            description=description,
            evaluation_modes=evaluation_modes,
            input_parameters=input_parameters,
            maximum_execution_frequency=maximum_execution_frequency,
            scope=scope,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             source: pulumi.Input['ConfigRuleSourceArgs'],
             compliance: Optional[pulumi.Input['CompliancePropertiesArgs']] = None,
             config_rule_name: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             evaluation_modes: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigRuleEvaluationModeConfigurationArgs']]]] = None,
             input_parameters: Optional[pulumi.Input[str]] = None,
             maximum_execution_frequency: Optional[pulumi.Input[str]] = None,
             scope: Optional[pulumi.Input['ConfigRuleScopeArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("source", source)
        if compliance is not None:
            _setter("compliance", compliance)
        if config_rule_name is not None:
            _setter("config_rule_name", config_rule_name)
        if description is not None:
            _setter("description", description)
        if evaluation_modes is not None:
            _setter("evaluation_modes", evaluation_modes)
        if input_parameters is not None:
            _setter("input_parameters", input_parameters)
        if maximum_execution_frequency is not None:
            _setter("maximum_execution_frequency", maximum_execution_frequency)
        if scope is not None:
            _setter("scope", scope)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input['ConfigRuleSourceArgs']:
        """
        Source of events for the AWS Config rule
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input['ConfigRuleSourceArgs']):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def compliance(self) -> Optional[pulumi.Input['CompliancePropertiesArgs']]:
        """
        Compliance details of the Config rule
        """
        return pulumi.get(self, "compliance")

    @compliance.setter
    def compliance(self, value: Optional[pulumi.Input['CompliancePropertiesArgs']]):
        pulumi.set(self, "compliance", value)

    @property
    @pulumi.getter(name="configRuleName")
    def config_rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name for the AWS Config rule
        """
        return pulumi.get(self, "config_rule_name")

    @config_rule_name.setter
    def config_rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config_rule_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description provided for the AWS Config rule
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="evaluationModes")
    def evaluation_modes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConfigRuleEvaluationModeConfigurationArgs']]]]:
        """
        List of EvaluationModeConfiguration objects
        """
        return pulumi.get(self, "evaluation_modes")

    @evaluation_modes.setter
    def evaluation_modes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigRuleEvaluationModeConfigurationArgs']]]]):
        pulumi.set(self, "evaluation_modes", value)

    @property
    @pulumi.getter(name="inputParameters")
    def input_parameters(self) -> Optional[pulumi.Input[str]]:
        """
        JSON string passed the Lambda function
        """
        return pulumi.get(self, "input_parameters")

    @input_parameters.setter
    def input_parameters(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "input_parameters", value)

    @property
    @pulumi.getter(name="maximumExecutionFrequency")
    def maximum_execution_frequency(self) -> Optional[pulumi.Input[str]]:
        """
        Maximum frequency at which the rule has to be evaluated
        """
        return pulumi.get(self, "maximum_execution_frequency")

    @maximum_execution_frequency.setter
    def maximum_execution_frequency(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "maximum_execution_frequency", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input['ConfigRuleScopeArgs']]:
        """
        Scope to constrain which resources can trigger the AWS Config rule
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input['ConfigRuleScopeArgs']]):
        pulumi.set(self, "scope", value)


class ConfigRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compliance: Optional[pulumi.Input[pulumi.InputType['CompliancePropertiesArgs']]] = None,
                 config_rule_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 evaluation_modes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigRuleEvaluationModeConfigurationArgs']]]]] = None,
                 input_parameters: Optional[pulumi.Input[str]] = None,
                 maximum_execution_frequency: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[pulumi.InputType['ConfigRuleScopeArgs']]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['ConfigRuleSourceArgs']]] = None,
                 __props__=None):
        """
        Schema for AWS Config ConfigRule

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['CompliancePropertiesArgs']] compliance: Compliance details of the Config rule
        :param pulumi.Input[str] config_rule_name: Name for the AWS Config rule
        :param pulumi.Input[str] description: Description provided for the AWS Config rule
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigRuleEvaluationModeConfigurationArgs']]]] evaluation_modes: List of EvaluationModeConfiguration objects
        :param pulumi.Input[str] input_parameters: JSON string passed the Lambda function
        :param pulumi.Input[str] maximum_execution_frequency: Maximum frequency at which the rule has to be evaluated
        :param pulumi.Input[pulumi.InputType['ConfigRuleScopeArgs']] scope: Scope to constrain which resources can trigger the AWS Config rule
        :param pulumi.Input[pulumi.InputType['ConfigRuleSourceArgs']] source: Source of events for the AWS Config rule
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConfigRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Schema for AWS Config ConfigRule

        :param str resource_name: The name of the resource.
        :param ConfigRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConfigRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ConfigRuleArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compliance: Optional[pulumi.Input[pulumi.InputType['CompliancePropertiesArgs']]] = None,
                 config_rule_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 evaluation_modes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigRuleEvaluationModeConfigurationArgs']]]]] = None,
                 input_parameters: Optional[pulumi.Input[str]] = None,
                 maximum_execution_frequency: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[pulumi.InputType['ConfigRuleScopeArgs']]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['ConfigRuleSourceArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConfigRuleArgs.__new__(ConfigRuleArgs)

            if compliance is not None and not isinstance(compliance, CompliancePropertiesArgs):
                compliance = compliance or {}
                def _setter(key, value):
                    compliance[key] = value
                CompliancePropertiesArgs._configure(_setter, **compliance)
            __props__.__dict__["compliance"] = compliance
            __props__.__dict__["config_rule_name"] = config_rule_name
            __props__.__dict__["description"] = description
            __props__.__dict__["evaluation_modes"] = evaluation_modes
            __props__.__dict__["input_parameters"] = input_parameters
            __props__.__dict__["maximum_execution_frequency"] = maximum_execution_frequency
            if scope is not None and not isinstance(scope, ConfigRuleScopeArgs):
                scope = scope or {}
                def _setter(key, value):
                    scope[key] = value
                ConfigRuleScopeArgs._configure(_setter, **scope)
            __props__.__dict__["scope"] = scope
            if source is not None and not isinstance(source, ConfigRuleSourceArgs):
                source = source or {}
                def _setter(key, value):
                    source[key] = value
                ConfigRuleSourceArgs._configure(_setter, **source)
            if source is None and not opts.urn:
                raise TypeError("Missing required property 'source'")
            __props__.__dict__["source"] = source
            __props__.__dict__["arn"] = None
            __props__.__dict__["config_rule_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["config_rule_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ConfigRule, __self__).__init__(
            'aws-native:configuration:ConfigRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConfigRule':
        """
        Get an existing ConfigRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConfigRuleArgs.__new__(ConfigRuleArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["compliance"] = None
        __props__.__dict__["config_rule_id"] = None
        __props__.__dict__["config_rule_name"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["evaluation_modes"] = None
        __props__.__dict__["input_parameters"] = None
        __props__.__dict__["maximum_execution_frequency"] = None
        __props__.__dict__["scope"] = None
        __props__.__dict__["source"] = None
        return ConfigRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        ARN generated for the AWS Config rule 
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def compliance(self) -> pulumi.Output[Optional['outputs.ComplianceProperties']]:
        """
        Compliance details of the Config rule
        """
        return pulumi.get(self, "compliance")

    @property
    @pulumi.getter(name="configRuleId")
    def config_rule_id(self) -> pulumi.Output[str]:
        """
        ID of the config rule
        """
        return pulumi.get(self, "config_rule_id")

    @property
    @pulumi.getter(name="configRuleName")
    def config_rule_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name for the AWS Config rule
        """
        return pulumi.get(self, "config_rule_name")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description provided for the AWS Config rule
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="evaluationModes")
    def evaluation_modes(self) -> pulumi.Output[Optional[Sequence['outputs.ConfigRuleEvaluationModeConfiguration']]]:
        """
        List of EvaluationModeConfiguration objects
        """
        return pulumi.get(self, "evaluation_modes")

    @property
    @pulumi.getter(name="inputParameters")
    def input_parameters(self) -> pulumi.Output[Optional[str]]:
        """
        JSON string passed the Lambda function
        """
        return pulumi.get(self, "input_parameters")

    @property
    @pulumi.getter(name="maximumExecutionFrequency")
    def maximum_execution_frequency(self) -> pulumi.Output[Optional[str]]:
        """
        Maximum frequency at which the rule has to be evaluated
        """
        return pulumi.get(self, "maximum_execution_frequency")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional['outputs.ConfigRuleScope']]:
        """
        Scope to constrain which resources can trigger the AWS Config rule
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output['outputs.ConfigRuleSource']:
        """
        Source of events for the AWS Config rule
        """
        return pulumi.get(self, "source")

