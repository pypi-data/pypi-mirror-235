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

__all__ = ['VerifiedAccessGroupArgs', 'VerifiedAccessGroup']

@pulumi.input_type
class VerifiedAccessGroupArgs:
    def __init__(__self__, *,
                 verified_access_instance_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 policy_document: Optional[pulumi.Input[str]] = None,
                 policy_enabled: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['VerifiedAccessGroupTagArgs']]]] = None):
        """
        The set of arguments for constructing a VerifiedAccessGroup resource.
        :param pulumi.Input[str] verified_access_instance_id: The ID of the AWS Verified Access instance.
        :param pulumi.Input[str] description: A description for the AWS Verified Access group.
        :param pulumi.Input[str] policy_document: The AWS Verified Access policy document.
        :param pulumi.Input[bool] policy_enabled: The status of the Verified Access policy.
        :param pulumi.Input[Sequence[pulumi.Input['VerifiedAccessGroupTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        VerifiedAccessGroupArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            verified_access_instance_id=verified_access_instance_id,
            description=description,
            policy_document=policy_document,
            policy_enabled=policy_enabled,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             verified_access_instance_id: pulumi.Input[str],
             description: Optional[pulumi.Input[str]] = None,
             policy_document: Optional[pulumi.Input[str]] = None,
             policy_enabled: Optional[pulumi.Input[bool]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['VerifiedAccessGroupTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("verified_access_instance_id", verified_access_instance_id)
        if description is not None:
            _setter("description", description)
        if policy_document is not None:
            _setter("policy_document", policy_document)
        if policy_enabled is not None:
            _setter("policy_enabled", policy_enabled)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="verifiedAccessInstanceId")
    def verified_access_instance_id(self) -> pulumi.Input[str]:
        """
        The ID of the AWS Verified Access instance.
        """
        return pulumi.get(self, "verified_access_instance_id")

    @verified_access_instance_id.setter
    def verified_access_instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "verified_access_instance_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the AWS Verified Access group.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[pulumi.Input[str]]:
        """
        The AWS Verified Access policy document.
        """
        return pulumi.get(self, "policy_document")

    @policy_document.setter
    def policy_document(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_document", value)

    @property
    @pulumi.getter(name="policyEnabled")
    def policy_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        The status of the Verified Access policy.
        """
        return pulumi.get(self, "policy_enabled")

    @policy_enabled.setter
    def policy_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "policy_enabled", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VerifiedAccessGroupTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VerifiedAccessGroupTagArgs']]]]):
        pulumi.set(self, "tags", value)


class VerifiedAccessGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 policy_document: Optional[pulumi.Input[str]] = None,
                 policy_enabled: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VerifiedAccessGroupTagArgs']]]]] = None,
                 verified_access_instance_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The AWS::EC2::VerifiedAccessGroup resource creates an AWS EC2 Verified Access Group.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description for the AWS Verified Access group.
        :param pulumi.Input[str] policy_document: The AWS Verified Access policy document.
        :param pulumi.Input[bool] policy_enabled: The status of the Verified Access policy.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VerifiedAccessGroupTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        :param pulumi.Input[str] verified_access_instance_id: The ID of the AWS Verified Access instance.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VerifiedAccessGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::EC2::VerifiedAccessGroup resource creates an AWS EC2 Verified Access Group.

        :param str resource_name: The name of the resource.
        :param VerifiedAccessGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VerifiedAccessGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            VerifiedAccessGroupArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 policy_document: Optional[pulumi.Input[str]] = None,
                 policy_enabled: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VerifiedAccessGroupTagArgs']]]]] = None,
                 verified_access_instance_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VerifiedAccessGroupArgs.__new__(VerifiedAccessGroupArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["policy_document"] = policy_document
            __props__.__dict__["policy_enabled"] = policy_enabled
            __props__.__dict__["tags"] = tags
            if verified_access_instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'verified_access_instance_id'")
            __props__.__dict__["verified_access_instance_id"] = verified_access_instance_id
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["last_updated_time"] = None
            __props__.__dict__["owner"] = None
            __props__.__dict__["verified_access_group_arn"] = None
            __props__.__dict__["verified_access_group_id"] = None
        super(VerifiedAccessGroup, __self__).__init__(
            'aws-native:ec2:VerifiedAccessGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VerifiedAccessGroup':
        """
        Get an existing VerifiedAccessGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VerifiedAccessGroupArgs.__new__(VerifiedAccessGroupArgs)

        __props__.__dict__["creation_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["last_updated_time"] = None
        __props__.__dict__["owner"] = None
        __props__.__dict__["policy_document"] = None
        __props__.__dict__["policy_enabled"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["verified_access_group_arn"] = None
        __props__.__dict__["verified_access_group_id"] = None
        __props__.__dict__["verified_access_instance_id"] = None
        return VerifiedAccessGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        Time this Verified Access Group was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for the AWS Verified Access group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> pulumi.Output[str]:
        """
        Time this Verified Access Group was last updated.
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[str]:
        """
        The AWS account number that owns the group.
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Output[Optional[str]]:
        """
        The AWS Verified Access policy document.
        """
        return pulumi.get(self, "policy_document")

    @property
    @pulumi.getter(name="policyEnabled")
    def policy_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        The status of the Verified Access policy.
        """
        return pulumi.get(self, "policy_enabled")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.VerifiedAccessGroupTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="verifiedAccessGroupArn")
    def verified_access_group_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the Verified Access group.
        """
        return pulumi.get(self, "verified_access_group_arn")

    @property
    @pulumi.getter(name="verifiedAccessGroupId")
    def verified_access_group_id(self) -> pulumi.Output[str]:
        """
        The ID of the AWS Verified Access group.
        """
        return pulumi.get(self, "verified_access_group_id")

    @property
    @pulumi.getter(name="verifiedAccessInstanceId")
    def verified_access_instance_id(self) -> pulumi.Output[str]:
        """
        The ID of the AWS Verified Access instance.
        """
        return pulumi.get(self, "verified_access_instance_id")

