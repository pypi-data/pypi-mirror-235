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

__all__ = ['VpcAttachmentArgs', 'VpcAttachment']

@pulumi.input_type
class VpcAttachmentArgs:
    def __init__(__self__, *,
                 core_network_id: pulumi.Input[str],
                 subnet_arns: pulumi.Input[Sequence[pulumi.Input[str]]],
                 vpc_arn: pulumi.Input[str],
                 options: Optional[pulumi.Input['VpcAttachmentVpcOptionsArgs']] = None,
                 proposed_segment_change: Optional[pulumi.Input['VpcAttachmentProposedSegmentChangeArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['VpcAttachmentTagArgs']]]] = None):
        """
        The set of arguments for constructing a VpcAttachment resource.
        :param pulumi.Input[str] core_network_id: The ID of a core network for the VPC attachment.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_arns: Subnet Arn list
        :param pulumi.Input[str] vpc_arn: The ARN of the VPC.
        :param pulumi.Input['VpcAttachmentVpcOptionsArgs'] options: Vpc options of the attachment.
        :param pulumi.Input['VpcAttachmentProposedSegmentChangeArgs'] proposed_segment_change: The attachment to move from one segment to another.
        :param pulumi.Input[Sequence[pulumi.Input['VpcAttachmentTagArgs']]] tags: Tags for the attachment.
        """
        VpcAttachmentArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            core_network_id=core_network_id,
            subnet_arns=subnet_arns,
            vpc_arn=vpc_arn,
            options=options,
            proposed_segment_change=proposed_segment_change,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             core_network_id: pulumi.Input[str],
             subnet_arns: pulumi.Input[Sequence[pulumi.Input[str]]],
             vpc_arn: pulumi.Input[str],
             options: Optional[pulumi.Input['VpcAttachmentVpcOptionsArgs']] = None,
             proposed_segment_change: Optional[pulumi.Input['VpcAttachmentProposedSegmentChangeArgs']] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['VpcAttachmentTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("core_network_id", core_network_id)
        _setter("subnet_arns", subnet_arns)
        _setter("vpc_arn", vpc_arn)
        if options is not None:
            _setter("options", options)
        if proposed_segment_change is not None:
            _setter("proposed_segment_change", proposed_segment_change)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> pulumi.Input[str]:
        """
        The ID of a core network for the VPC attachment.
        """
        return pulumi.get(self, "core_network_id")

    @core_network_id.setter
    def core_network_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "core_network_id", value)

    @property
    @pulumi.getter(name="subnetArns")
    def subnet_arns(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Subnet Arn list
        """
        return pulumi.get(self, "subnet_arns")

    @subnet_arns.setter
    def subnet_arns(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "subnet_arns", value)

    @property
    @pulumi.getter(name="vpcArn")
    def vpc_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the VPC.
        """
        return pulumi.get(self, "vpc_arn")

    @vpc_arn.setter
    def vpc_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_arn", value)

    @property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input['VpcAttachmentVpcOptionsArgs']]:
        """
        Vpc options of the attachment.
        """
        return pulumi.get(self, "options")

    @options.setter
    def options(self, value: Optional[pulumi.Input['VpcAttachmentVpcOptionsArgs']]):
        pulumi.set(self, "options", value)

    @property
    @pulumi.getter(name="proposedSegmentChange")
    def proposed_segment_change(self) -> Optional[pulumi.Input['VpcAttachmentProposedSegmentChangeArgs']]:
        """
        The attachment to move from one segment to another.
        """
        return pulumi.get(self, "proposed_segment_change")

    @proposed_segment_change.setter
    def proposed_segment_change(self, value: Optional[pulumi.Input['VpcAttachmentProposedSegmentChangeArgs']]):
        pulumi.set(self, "proposed_segment_change", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VpcAttachmentTagArgs']]]]:
        """
        Tags for the attachment.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VpcAttachmentTagArgs']]]]):
        pulumi.set(self, "tags", value)


class VpcAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 core_network_id: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[pulumi.InputType['VpcAttachmentVpcOptionsArgs']]] = None,
                 proposed_segment_change: Optional[pulumi.Input[pulumi.InputType['VpcAttachmentProposedSegmentChangeArgs']]] = None,
                 subnet_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpcAttachmentTagArgs']]]]] = None,
                 vpc_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        AWS::NetworkManager::VpcAttachment Resoruce Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] core_network_id: The ID of a core network for the VPC attachment.
        :param pulumi.Input[pulumi.InputType['VpcAttachmentVpcOptionsArgs']] options: Vpc options of the attachment.
        :param pulumi.Input[pulumi.InputType['VpcAttachmentProposedSegmentChangeArgs']] proposed_segment_change: The attachment to move from one segment to another.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_arns: Subnet Arn list
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpcAttachmentTagArgs']]]] tags: Tags for the attachment.
        :param pulumi.Input[str] vpc_arn: The ARN of the VPC.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VpcAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        AWS::NetworkManager::VpcAttachment Resoruce Type

        :param str resource_name: The name of the resource.
        :param VpcAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpcAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            VpcAttachmentArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 core_network_id: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[pulumi.InputType['VpcAttachmentVpcOptionsArgs']]] = None,
                 proposed_segment_change: Optional[pulumi.Input[pulumi.InputType['VpcAttachmentProposedSegmentChangeArgs']]] = None,
                 subnet_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpcAttachmentTagArgs']]]]] = None,
                 vpc_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpcAttachmentArgs.__new__(VpcAttachmentArgs)

            if core_network_id is None and not opts.urn:
                raise TypeError("Missing required property 'core_network_id'")
            __props__.__dict__["core_network_id"] = core_network_id
            if options is not None and not isinstance(options, VpcAttachmentVpcOptionsArgs):
                options = options or {}
                def _setter(key, value):
                    options[key] = value
                VpcAttachmentVpcOptionsArgs._configure(_setter, **options)
            __props__.__dict__["options"] = options
            if proposed_segment_change is not None and not isinstance(proposed_segment_change, VpcAttachmentProposedSegmentChangeArgs):
                proposed_segment_change = proposed_segment_change or {}
                def _setter(key, value):
                    proposed_segment_change[key] = value
                VpcAttachmentProposedSegmentChangeArgs._configure(_setter, **proposed_segment_change)
            __props__.__dict__["proposed_segment_change"] = proposed_segment_change
            if subnet_arns is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_arns'")
            __props__.__dict__["subnet_arns"] = subnet_arns
            __props__.__dict__["tags"] = tags
            if vpc_arn is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_arn'")
            __props__.__dict__["vpc_arn"] = vpc_arn
            __props__.__dict__["attachment_id"] = None
            __props__.__dict__["attachment_policy_rule_number"] = None
            __props__.__dict__["attachment_type"] = None
            __props__.__dict__["core_network_arn"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["edge_location"] = None
            __props__.__dict__["owner_account_id"] = None
            __props__.__dict__["resource_arn"] = None
            __props__.__dict__["segment_name"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["updated_at"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["core_network_id", "vpc_arn"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(VpcAttachment, __self__).__init__(
            'aws-native:networkmanager:VpcAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VpcAttachment':
        """
        Get an existing VpcAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VpcAttachmentArgs.__new__(VpcAttachmentArgs)

        __props__.__dict__["attachment_id"] = None
        __props__.__dict__["attachment_policy_rule_number"] = None
        __props__.__dict__["attachment_type"] = None
        __props__.__dict__["core_network_arn"] = None
        __props__.__dict__["core_network_id"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["edge_location"] = None
        __props__.__dict__["options"] = None
        __props__.__dict__["owner_account_id"] = None
        __props__.__dict__["proposed_segment_change"] = None
        __props__.__dict__["resource_arn"] = None
        __props__.__dict__["segment_name"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["subnet_arns"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["updated_at"] = None
        __props__.__dict__["vpc_arn"] = None
        return VpcAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> pulumi.Output[str]:
        """
        Id of the attachment.
        """
        return pulumi.get(self, "attachment_id")

    @property
    @pulumi.getter(name="attachmentPolicyRuleNumber")
    def attachment_policy_rule_number(self) -> pulumi.Output[int]:
        """
        The policy rule number associated with the attachment.
        """
        return pulumi.get(self, "attachment_policy_rule_number")

    @property
    @pulumi.getter(name="attachmentType")
    def attachment_type(self) -> pulumi.Output[str]:
        """
        Attachment type.
        """
        return pulumi.get(self, "attachment_type")

    @property
    @pulumi.getter(name="coreNetworkArn")
    def core_network_arn(self) -> pulumi.Output[str]:
        """
        The ARN of a core network for the VPC attachment.
        """
        return pulumi.get(self, "core_network_arn")

    @property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> pulumi.Output[str]:
        """
        The ID of a core network for the VPC attachment.
        """
        return pulumi.get(self, "core_network_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Creation time of the attachment.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="edgeLocation")
    def edge_location(self) -> pulumi.Output[str]:
        """
        The Region where the edge is located.
        """
        return pulumi.get(self, "edge_location")

    @property
    @pulumi.getter
    def options(self) -> pulumi.Output[Optional['outputs.VpcAttachmentVpcOptions']]:
        """
        Vpc options of the attachment.
        """
        return pulumi.get(self, "options")

    @property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> pulumi.Output[str]:
        """
        Owner account of the attachment.
        """
        return pulumi.get(self, "owner_account_id")

    @property
    @pulumi.getter(name="proposedSegmentChange")
    def proposed_segment_change(self) -> pulumi.Output[Optional['outputs.VpcAttachmentProposedSegmentChange']]:
        """
        The attachment to move from one segment to another.
        """
        return pulumi.get(self, "proposed_segment_change")

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the Resource.
        """
        return pulumi.get(self, "resource_arn")

    @property
    @pulumi.getter(name="segmentName")
    def segment_name(self) -> pulumi.Output[str]:
        """
        The name of the segment attachment..
        """
        return pulumi.get(self, "segment_name")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        State of the attachment.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="subnetArns")
    def subnet_arns(self) -> pulumi.Output[Sequence[str]]:
        """
        Subnet Arn list
        """
        return pulumi.get(self, "subnet_arns")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.VpcAttachmentTag']]]:
        """
        Tags for the attachment.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        Last update time of the attachment.
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter(name="vpcArn")
    def vpc_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the VPC.
        """
        return pulumi.get(self, "vpc_arn")

