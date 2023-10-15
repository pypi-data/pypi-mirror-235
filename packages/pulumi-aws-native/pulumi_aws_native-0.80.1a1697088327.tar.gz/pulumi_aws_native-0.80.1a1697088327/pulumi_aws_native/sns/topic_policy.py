# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['TopicPolicyArgs', 'TopicPolicy']

@pulumi.input_type
class TopicPolicyArgs:
    def __init__(__self__, *,
                 policy_document: Any,
                 topics: pulumi.Input[Sequence[pulumi.Input[str]]]):
        """
        The set of arguments for constructing a TopicPolicy resource.
        :param Any policy_document: A policy document that contains permissions to add to the specified SNS topics.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] topics: The Amazon Resource Names (ARN) of the topics to which you want to add the policy. You can use the [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html)` function to specify an [AWS::SNS::Topic](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic.html) resource.
        """
        TopicPolicyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            policy_document=policy_document,
            topics=topics,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             policy_document: Any,
             topics: pulumi.Input[Sequence[pulumi.Input[str]]],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("policy_document", policy_document)
        _setter("topics", topics)

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Any:
        """
        A policy document that contains permissions to add to the specified SNS topics.
        """
        return pulumi.get(self, "policy_document")

    @policy_document.setter
    def policy_document(self, value: Any):
        pulumi.set(self, "policy_document", value)

    @property
    @pulumi.getter
    def topics(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The Amazon Resource Names (ARN) of the topics to which you want to add the policy. You can use the [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html)` function to specify an [AWS::SNS::Topic](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic.html) resource.
        """
        return pulumi.get(self, "topics")

    @topics.setter
    def topics(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "topics", value)


class TopicPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 policy_document: Optional[Any] = None,
                 topics: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Schema for AWS::SNS::TopicPolicy

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param Any policy_document: A policy document that contains permissions to add to the specified SNS topics.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] topics: The Amazon Resource Names (ARN) of the topics to which you want to add the policy. You can use the [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html)` function to specify an [AWS::SNS::Topic](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic.html) resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TopicPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Schema for AWS::SNS::TopicPolicy

        :param str resource_name: The name of the resource.
        :param TopicPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TopicPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            TopicPolicyArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 policy_document: Optional[Any] = None,
                 topics: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TopicPolicyArgs.__new__(TopicPolicyArgs)

            if policy_document is None and not opts.urn:
                raise TypeError("Missing required property 'policy_document'")
            __props__.__dict__["policy_document"] = policy_document
            if topics is None and not opts.urn:
                raise TypeError("Missing required property 'topics'")
            __props__.__dict__["topics"] = topics
        super(TopicPolicy, __self__).__init__(
            'aws-native:sns:TopicPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TopicPolicy':
        """
        Get an existing TopicPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TopicPolicyArgs.__new__(TopicPolicyArgs)

        __props__.__dict__["policy_document"] = None
        __props__.__dict__["topics"] = None
        return TopicPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Output[Any]:
        """
        A policy document that contains permissions to add to the specified SNS topics.
        """
        return pulumi.get(self, "policy_document")

    @property
    @pulumi.getter
    def topics(self) -> pulumi.Output[Sequence[str]]:
        """
        The Amazon Resource Names (ARN) of the topics to which you want to add the policy. You can use the [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html)` function to specify an [AWS::SNS::Topic](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic.html) resource.
        """
        return pulumi.get(self, "topics")

