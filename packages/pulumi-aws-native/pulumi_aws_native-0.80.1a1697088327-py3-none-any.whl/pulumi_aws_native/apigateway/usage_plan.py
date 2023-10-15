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

__all__ = ['UsagePlanArgs', 'UsagePlan']

@pulumi.input_type
class UsagePlanArgs:
    def __init__(__self__, *,
                 api_stages: Optional[pulumi.Input[Sequence[pulumi.Input['UsagePlanApiStageArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 quota: Optional[pulumi.Input['UsagePlanQuotaSettingsArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['UsagePlanTagArgs']]]] = None,
                 throttle: Optional[pulumi.Input['UsagePlanThrottleSettingsArgs']] = None,
                 usage_plan_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a UsagePlan resource.
        :param pulumi.Input[Sequence[pulumi.Input['UsagePlanApiStageArgs']]] api_stages: The API stages to associate with this usage plan.
        :param pulumi.Input[str] description: A description of the usage plan.
        :param pulumi.Input['UsagePlanQuotaSettingsArgs'] quota: Configures the number of requests that users can make within a given interval.
        :param pulumi.Input[Sequence[pulumi.Input['UsagePlanTagArgs']]] tags: An array of arbitrary tags (key-value pairs) to associate with the usage plan.
        :param pulumi.Input['UsagePlanThrottleSettingsArgs'] throttle: Configures the overall request rate (average requests per second) and burst capacity.
        :param pulumi.Input[str] usage_plan_name: A name for the usage plan.
        """
        UsagePlanArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            api_stages=api_stages,
            description=description,
            quota=quota,
            tags=tags,
            throttle=throttle,
            usage_plan_name=usage_plan_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             api_stages: Optional[pulumi.Input[Sequence[pulumi.Input['UsagePlanApiStageArgs']]]] = None,
             description: Optional[pulumi.Input[str]] = None,
             quota: Optional[pulumi.Input['UsagePlanQuotaSettingsArgs']] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['UsagePlanTagArgs']]]] = None,
             throttle: Optional[pulumi.Input['UsagePlanThrottleSettingsArgs']] = None,
             usage_plan_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if api_stages is not None:
            _setter("api_stages", api_stages)
        if description is not None:
            _setter("description", description)
        if quota is not None:
            _setter("quota", quota)
        if tags is not None:
            _setter("tags", tags)
        if throttle is not None:
            _setter("throttle", throttle)
        if usage_plan_name is not None:
            _setter("usage_plan_name", usage_plan_name)

    @property
    @pulumi.getter(name="apiStages")
    def api_stages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['UsagePlanApiStageArgs']]]]:
        """
        The API stages to associate with this usage plan.
        """
        return pulumi.get(self, "api_stages")

    @api_stages.setter
    def api_stages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['UsagePlanApiStageArgs']]]]):
        pulumi.set(self, "api_stages", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the usage plan.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def quota(self) -> Optional[pulumi.Input['UsagePlanQuotaSettingsArgs']]:
        """
        Configures the number of requests that users can make within a given interval.
        """
        return pulumi.get(self, "quota")

    @quota.setter
    def quota(self, value: Optional[pulumi.Input['UsagePlanQuotaSettingsArgs']]):
        pulumi.set(self, "quota", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['UsagePlanTagArgs']]]]:
        """
        An array of arbitrary tags (key-value pairs) to associate with the usage plan.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['UsagePlanTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def throttle(self) -> Optional[pulumi.Input['UsagePlanThrottleSettingsArgs']]:
        """
        Configures the overall request rate (average requests per second) and burst capacity.
        """
        return pulumi.get(self, "throttle")

    @throttle.setter
    def throttle(self, value: Optional[pulumi.Input['UsagePlanThrottleSettingsArgs']]):
        pulumi.set(self, "throttle", value)

    @property
    @pulumi.getter(name="usagePlanName")
    def usage_plan_name(self) -> Optional[pulumi.Input[str]]:
        """
        A name for the usage plan.
        """
        return pulumi.get(self, "usage_plan_name")

    @usage_plan_name.setter
    def usage_plan_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "usage_plan_name", value)


class UsagePlan(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_stages: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UsagePlanApiStageArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 quota: Optional[pulumi.Input[pulumi.InputType['UsagePlanQuotaSettingsArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UsagePlanTagArgs']]]]] = None,
                 throttle: Optional[pulumi.Input[pulumi.InputType['UsagePlanThrottleSettingsArgs']]] = None,
                 usage_plan_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::ApiGateway::UsagePlan

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UsagePlanApiStageArgs']]]] api_stages: The API stages to associate with this usage plan.
        :param pulumi.Input[str] description: A description of the usage plan.
        :param pulumi.Input[pulumi.InputType['UsagePlanQuotaSettingsArgs']] quota: Configures the number of requests that users can make within a given interval.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UsagePlanTagArgs']]]] tags: An array of arbitrary tags (key-value pairs) to associate with the usage plan.
        :param pulumi.Input[pulumi.InputType['UsagePlanThrottleSettingsArgs']] throttle: Configures the overall request rate (average requests per second) and burst capacity.
        :param pulumi.Input[str] usage_plan_name: A name for the usage plan.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[UsagePlanArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::ApiGateway::UsagePlan

        :param str resource_name: The name of the resource.
        :param UsagePlanArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UsagePlanArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            UsagePlanArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_stages: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UsagePlanApiStageArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 quota: Optional[pulumi.Input[pulumi.InputType['UsagePlanQuotaSettingsArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UsagePlanTagArgs']]]]] = None,
                 throttle: Optional[pulumi.Input[pulumi.InputType['UsagePlanThrottleSettingsArgs']]] = None,
                 usage_plan_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UsagePlanArgs.__new__(UsagePlanArgs)

            __props__.__dict__["api_stages"] = api_stages
            __props__.__dict__["description"] = description
            if quota is not None and not isinstance(quota, UsagePlanQuotaSettingsArgs):
                quota = quota or {}
                def _setter(key, value):
                    quota[key] = value
                UsagePlanQuotaSettingsArgs._configure(_setter, **quota)
            __props__.__dict__["quota"] = quota
            __props__.__dict__["tags"] = tags
            if throttle is not None and not isinstance(throttle, UsagePlanThrottleSettingsArgs):
                throttle = throttle or {}
                def _setter(key, value):
                    throttle[key] = value
                UsagePlanThrottleSettingsArgs._configure(_setter, **throttle)
            __props__.__dict__["throttle"] = throttle
            __props__.__dict__["usage_plan_name"] = usage_plan_name
        super(UsagePlan, __self__).__init__(
            'aws-native:apigateway:UsagePlan',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'UsagePlan':
        """
        Get an existing UsagePlan resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = UsagePlanArgs.__new__(UsagePlanArgs)

        __props__.__dict__["api_stages"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["quota"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["throttle"] = None
        __props__.__dict__["usage_plan_name"] = None
        return UsagePlan(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiStages")
    def api_stages(self) -> pulumi.Output[Optional[Sequence['outputs.UsagePlanApiStage']]]:
        """
        The API stages to associate with this usage plan.
        """
        return pulumi.get(self, "api_stages")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the usage plan.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def quota(self) -> pulumi.Output[Optional['outputs.UsagePlanQuotaSettings']]:
        """
        Configures the number of requests that users can make within a given interval.
        """
        return pulumi.get(self, "quota")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.UsagePlanTag']]]:
        """
        An array of arbitrary tags (key-value pairs) to associate with the usage plan.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def throttle(self) -> pulumi.Output[Optional['outputs.UsagePlanThrottleSettings']]:
        """
        Configures the overall request rate (average requests per second) and burst capacity.
        """
        return pulumi.get(self, "throttle")

    @property
    @pulumi.getter(name="usagePlanName")
    def usage_plan_name(self) -> pulumi.Output[Optional[str]]:
        """
        A name for the usage plan.
        """
        return pulumi.get(self, "usage_plan_name")

