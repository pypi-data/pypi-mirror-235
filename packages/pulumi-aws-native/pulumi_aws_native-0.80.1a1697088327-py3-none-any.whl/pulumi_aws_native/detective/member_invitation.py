# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['MemberInvitationArgs', 'MemberInvitation']

@pulumi.input_type
class MemberInvitationArgs:
    def __init__(__self__, *,
                 graph_arn: pulumi.Input[str],
                 member_email_address: pulumi.Input[str],
                 member_id: pulumi.Input[str],
                 disable_email_notification: Optional[pulumi.Input[bool]] = None,
                 message: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a MemberInvitation resource.
        :param pulumi.Input[str] graph_arn: The ARN of the graph to which the member account will be invited
        :param pulumi.Input[str] member_email_address: The root email address for the account to be invited, for validation. Updating this field has no effect.
        :param pulumi.Input[str] member_id: The AWS account ID to be invited to join the graph as a member
        :param pulumi.Input[bool] disable_email_notification: When set to true, invitation emails are not sent to the member accounts. Member accounts must still accept the invitation before they are added to the behavior graph. Updating this field has no effect.
        :param pulumi.Input[str] message: A message to be included in the email invitation sent to the invited account. Updating this field has no effect.
        """
        MemberInvitationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            graph_arn=graph_arn,
            member_email_address=member_email_address,
            member_id=member_id,
            disable_email_notification=disable_email_notification,
            message=message,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             graph_arn: pulumi.Input[str],
             member_email_address: pulumi.Input[str],
             member_id: pulumi.Input[str],
             disable_email_notification: Optional[pulumi.Input[bool]] = None,
             message: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("graph_arn", graph_arn)
        _setter("member_email_address", member_email_address)
        _setter("member_id", member_id)
        if disable_email_notification is not None:
            _setter("disable_email_notification", disable_email_notification)
        if message is not None:
            _setter("message", message)

    @property
    @pulumi.getter(name="graphArn")
    def graph_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the graph to which the member account will be invited
        """
        return pulumi.get(self, "graph_arn")

    @graph_arn.setter
    def graph_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "graph_arn", value)

    @property
    @pulumi.getter(name="memberEmailAddress")
    def member_email_address(self) -> pulumi.Input[str]:
        """
        The root email address for the account to be invited, for validation. Updating this field has no effect.
        """
        return pulumi.get(self, "member_email_address")

    @member_email_address.setter
    def member_email_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "member_email_address", value)

    @property
    @pulumi.getter(name="memberId")
    def member_id(self) -> pulumi.Input[str]:
        """
        The AWS account ID to be invited to join the graph as a member
        """
        return pulumi.get(self, "member_id")

    @member_id.setter
    def member_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "member_id", value)

    @property
    @pulumi.getter(name="disableEmailNotification")
    def disable_email_notification(self) -> Optional[pulumi.Input[bool]]:
        """
        When set to true, invitation emails are not sent to the member accounts. Member accounts must still accept the invitation before they are added to the behavior graph. Updating this field has no effect.
        """
        return pulumi.get(self, "disable_email_notification")

    @disable_email_notification.setter
    def disable_email_notification(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_email_notification", value)

    @property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[str]]:
        """
        A message to be included in the email invitation sent to the invited account. Updating this field has no effect.
        """
        return pulumi.get(self, "message")

    @message.setter
    def message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message", value)


class MemberInvitation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disable_email_notification: Optional[pulumi.Input[bool]] = None,
                 graph_arn: Optional[pulumi.Input[str]] = None,
                 member_email_address: Optional[pulumi.Input[str]] = None,
                 member_id: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource schema for AWS::Detective::MemberInvitation

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] disable_email_notification: When set to true, invitation emails are not sent to the member accounts. Member accounts must still accept the invitation before they are added to the behavior graph. Updating this field has no effect.
        :param pulumi.Input[str] graph_arn: The ARN of the graph to which the member account will be invited
        :param pulumi.Input[str] member_email_address: The root email address for the account to be invited, for validation. Updating this field has no effect.
        :param pulumi.Input[str] member_id: The AWS account ID to be invited to join the graph as a member
        :param pulumi.Input[str] message: A message to be included in the email invitation sent to the invited account. Updating this field has no effect.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MemberInvitationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::Detective::MemberInvitation

        :param str resource_name: The name of the resource.
        :param MemberInvitationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MemberInvitationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            MemberInvitationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disable_email_notification: Optional[pulumi.Input[bool]] = None,
                 graph_arn: Optional[pulumi.Input[str]] = None,
                 member_email_address: Optional[pulumi.Input[str]] = None,
                 member_id: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MemberInvitationArgs.__new__(MemberInvitationArgs)

            __props__.__dict__["disable_email_notification"] = disable_email_notification
            if graph_arn is None and not opts.urn:
                raise TypeError("Missing required property 'graph_arn'")
            __props__.__dict__["graph_arn"] = graph_arn
            if member_email_address is None and not opts.urn:
                raise TypeError("Missing required property 'member_email_address'")
            __props__.__dict__["member_email_address"] = member_email_address
            if member_id is None and not opts.urn:
                raise TypeError("Missing required property 'member_id'")
            __props__.__dict__["member_id"] = member_id
            __props__.__dict__["message"] = message
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["graph_arn", "member_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(MemberInvitation, __self__).__init__(
            'aws-native:detective:MemberInvitation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'MemberInvitation':
        """
        Get an existing MemberInvitation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MemberInvitationArgs.__new__(MemberInvitationArgs)

        __props__.__dict__["disable_email_notification"] = None
        __props__.__dict__["graph_arn"] = None
        __props__.__dict__["member_email_address"] = None
        __props__.__dict__["member_id"] = None
        __props__.__dict__["message"] = None
        return MemberInvitation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="disableEmailNotification")
    def disable_email_notification(self) -> pulumi.Output[Optional[bool]]:
        """
        When set to true, invitation emails are not sent to the member accounts. Member accounts must still accept the invitation before they are added to the behavior graph. Updating this field has no effect.
        """
        return pulumi.get(self, "disable_email_notification")

    @property
    @pulumi.getter(name="graphArn")
    def graph_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the graph to which the member account will be invited
        """
        return pulumi.get(self, "graph_arn")

    @property
    @pulumi.getter(name="memberEmailAddress")
    def member_email_address(self) -> pulumi.Output[str]:
        """
        The root email address for the account to be invited, for validation. Updating this field has no effect.
        """
        return pulumi.get(self, "member_email_address")

    @property
    @pulumi.getter(name="memberId")
    def member_id(self) -> pulumi.Output[str]:
        """
        The AWS account ID to be invited to join the graph as a member
        """
        return pulumi.get(self, "member_id")

    @property
    @pulumi.getter
    def message(self) -> pulumi.Output[Optional[str]]:
        """
        A message to be included in the email invitation sent to the invited account. Updating this field has no effect.
        """
        return pulumi.get(self, "message")

