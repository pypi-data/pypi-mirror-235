# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DestinationArgs', 'Destination']

@pulumi.input_type
class DestinationArgs:
    def __init__(__self__, *,
                 role_arn: pulumi.Input[str],
                 target_arn: pulumi.Input[str],
                 destination_name: Optional[pulumi.Input[str]] = None,
                 destination_policy: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Destination resource.
        :param pulumi.Input[str] role_arn: The ARN of an IAM role that permits CloudWatch Logs to send data to the specified AWS resource
        :param pulumi.Input[str] target_arn: The ARN of the physical target where the log events are delivered (for example, a Kinesis stream)
        :param pulumi.Input[str] destination_name: The name of the destination resource
        :param pulumi.Input[str] destination_policy: An IAM policy document that governs which AWS accounts can create subscription filters against this destination.
        """
        DestinationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            role_arn=role_arn,
            target_arn=target_arn,
            destination_name=destination_name,
            destination_policy=destination_policy,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             role_arn: pulumi.Input[str],
             target_arn: pulumi.Input[str],
             destination_name: Optional[pulumi.Input[str]] = None,
             destination_policy: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("role_arn", role_arn)
        _setter("target_arn", target_arn)
        if destination_name is not None:
            _setter("destination_name", destination_name)
        if destination_policy is not None:
            _setter("destination_policy", destination_policy)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        """
        The ARN of an IAM role that permits CloudWatch Logs to send data to the specified AWS resource
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the physical target where the log events are delivered (for example, a Kinesis stream)
        """
        return pulumi.get(self, "target_arn")

    @target_arn.setter
    def target_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_arn", value)

    @property
    @pulumi.getter(name="destinationName")
    def destination_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the destination resource
        """
        return pulumi.get(self, "destination_name")

    @destination_name.setter
    def destination_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_name", value)

    @property
    @pulumi.getter(name="destinationPolicy")
    def destination_policy(self) -> Optional[pulumi.Input[str]]:
        """
        An IAM policy document that governs which AWS accounts can create subscription filters against this destination.
        """
        return pulumi.get(self, "destination_policy")

    @destination_policy.setter
    def destination_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_policy", value)


class Destination(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination_name: Optional[pulumi.Input[str]] = None,
                 destination_policy: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 target_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The AWS::Logs::Destination resource specifies a CloudWatch Logs destination. A destination encapsulates a physical resource (such as an Amazon Kinesis data stream) and enables you to subscribe that resource to a stream of log events.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] destination_name: The name of the destination resource
        :param pulumi.Input[str] destination_policy: An IAM policy document that governs which AWS accounts can create subscription filters against this destination.
        :param pulumi.Input[str] role_arn: The ARN of an IAM role that permits CloudWatch Logs to send data to the specified AWS resource
        :param pulumi.Input[str] target_arn: The ARN of the physical target where the log events are delivered (for example, a Kinesis stream)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DestinationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::Logs::Destination resource specifies a CloudWatch Logs destination. A destination encapsulates a physical resource (such as an Amazon Kinesis data stream) and enables you to subscribe that resource to a stream of log events.

        :param str resource_name: The name of the resource.
        :param DestinationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DestinationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DestinationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination_name: Optional[pulumi.Input[str]] = None,
                 destination_policy: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 target_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DestinationArgs.__new__(DestinationArgs)

            __props__.__dict__["destination_name"] = destination_name
            __props__.__dict__["destination_policy"] = destination_policy
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
            if target_arn is None and not opts.urn:
                raise TypeError("Missing required property 'target_arn'")
            __props__.__dict__["target_arn"] = target_arn
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["destination_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Destination, __self__).__init__(
            'aws-native:logs:Destination',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Destination':
        """
        Get an existing Destination resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DestinationArgs.__new__(DestinationArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["destination_name"] = None
        __props__.__dict__["destination_policy"] = None
        __props__.__dict__["role_arn"] = None
        __props__.__dict__["target_arn"] = None
        return Destination(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="destinationName")
    def destination_name(self) -> pulumi.Output[str]:
        """
        The name of the destination resource
        """
        return pulumi.get(self, "destination_name")

    @property
    @pulumi.getter(name="destinationPolicy")
    def destination_policy(self) -> pulumi.Output[Optional[str]]:
        """
        An IAM policy document that governs which AWS accounts can create subscription filters against this destination.
        """
        return pulumi.get(self, "destination_policy")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        """
        The ARN of an IAM role that permits CloudWatch Logs to send data to the specified AWS resource
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the physical target where the log events are delivered (for example, a Kinesis stream)
        """
        return pulumi.get(self, "target_arn")

