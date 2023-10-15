# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['TransitGatewayMulticastDomainAssociationArgs', 'TransitGatewayMulticastDomainAssociation']

@pulumi.input_type
class TransitGatewayMulticastDomainAssociationArgs:
    def __init__(__self__, *,
                 subnet_id: pulumi.Input[str],
                 transit_gateway_attachment_id: pulumi.Input[str],
                 transit_gateway_multicast_domain_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a TransitGatewayMulticastDomainAssociation resource.
        :param pulumi.Input[str] subnet_id: The IDs of the subnets to associate with the transit gateway multicast domain.
        :param pulumi.Input[str] transit_gateway_attachment_id: The ID of the transit gateway attachment.
        :param pulumi.Input[str] transit_gateway_multicast_domain_id: The ID of the transit gateway multicast domain.
        """
        TransitGatewayMulticastDomainAssociationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            subnet_id=subnet_id,
            transit_gateway_attachment_id=transit_gateway_attachment_id,
            transit_gateway_multicast_domain_id=transit_gateway_multicast_domain_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             subnet_id: pulumi.Input[str],
             transit_gateway_attachment_id: pulumi.Input[str],
             transit_gateway_multicast_domain_id: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("subnet_id", subnet_id)
        _setter("transit_gateway_attachment_id", transit_gateway_attachment_id)
        _setter("transit_gateway_multicast_domain_id", transit_gateway_multicast_domain_id)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[str]:
        """
        The IDs of the subnets to associate with the transit gateway multicast domain.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> pulumi.Input[str]:
        """
        The ID of the transit gateway attachment.
        """
        return pulumi.get(self, "transit_gateway_attachment_id")

    @transit_gateway_attachment_id.setter
    def transit_gateway_attachment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "transit_gateway_attachment_id", value)

    @property
    @pulumi.getter(name="transitGatewayMulticastDomainId")
    def transit_gateway_multicast_domain_id(self) -> pulumi.Input[str]:
        """
        The ID of the transit gateway multicast domain.
        """
        return pulumi.get(self, "transit_gateway_multicast_domain_id")

    @transit_gateway_multicast_domain_id.setter
    def transit_gateway_multicast_domain_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "transit_gateway_multicast_domain_id", value)


class TransitGatewayMulticastDomainAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 transit_gateway_attachment_id: Optional[pulumi.Input[str]] = None,
                 transit_gateway_multicast_domain_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The AWS::EC2::TransitGatewayMulticastDomainAssociation type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] subnet_id: The IDs of the subnets to associate with the transit gateway multicast domain.
        :param pulumi.Input[str] transit_gateway_attachment_id: The ID of the transit gateway attachment.
        :param pulumi.Input[str] transit_gateway_multicast_domain_id: The ID of the transit gateway multicast domain.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TransitGatewayMulticastDomainAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::EC2::TransitGatewayMulticastDomainAssociation type

        :param str resource_name: The name of the resource.
        :param TransitGatewayMulticastDomainAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TransitGatewayMulticastDomainAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            TransitGatewayMulticastDomainAssociationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 transit_gateway_attachment_id: Optional[pulumi.Input[str]] = None,
                 transit_gateway_multicast_domain_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TransitGatewayMulticastDomainAssociationArgs.__new__(TransitGatewayMulticastDomainAssociationArgs)

            if subnet_id is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_id'")
            __props__.__dict__["subnet_id"] = subnet_id
            if transit_gateway_attachment_id is None and not opts.urn:
                raise TypeError("Missing required property 'transit_gateway_attachment_id'")
            __props__.__dict__["transit_gateway_attachment_id"] = transit_gateway_attachment_id
            if transit_gateway_multicast_domain_id is None and not opts.urn:
                raise TypeError("Missing required property 'transit_gateway_multicast_domain_id'")
            __props__.__dict__["transit_gateway_multicast_domain_id"] = transit_gateway_multicast_domain_id
            __props__.__dict__["resource_id"] = None
            __props__.__dict__["resource_type"] = None
            __props__.__dict__["state"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["subnet_id", "transit_gateway_attachment_id", "transit_gateway_multicast_domain_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(TransitGatewayMulticastDomainAssociation, __self__).__init__(
            'aws-native:ec2:TransitGatewayMulticastDomainAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TransitGatewayMulticastDomainAssociation':
        """
        Get an existing TransitGatewayMulticastDomainAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TransitGatewayMulticastDomainAssociationArgs.__new__(TransitGatewayMulticastDomainAssociationArgs)

        __props__.__dict__["resource_id"] = None
        __props__.__dict__["resource_type"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["subnet_id"] = None
        __props__.__dict__["transit_gateway_attachment_id"] = None
        __props__.__dict__["transit_gateway_multicast_domain_id"] = None
        return TransitGatewayMulticastDomainAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[str]:
        """
        The ID of the resource.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[str]:
        """
        The type of resource, for example a VPC attachment.
        """
        return pulumi.get(self, "resource_type")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the subnet association.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        """
        The IDs of the subnets to associate with the transit gateway multicast domain.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> pulumi.Output[str]:
        """
        The ID of the transit gateway attachment.
        """
        return pulumi.get(self, "transit_gateway_attachment_id")

    @property
    @pulumi.getter(name="transitGatewayMulticastDomainId")
    def transit_gateway_multicast_domain_id(self) -> pulumi.Output[str]:
        """
        The ID of the transit gateway multicast domain.
        """
        return pulumi.get(self, "transit_gateway_multicast_domain_id")

