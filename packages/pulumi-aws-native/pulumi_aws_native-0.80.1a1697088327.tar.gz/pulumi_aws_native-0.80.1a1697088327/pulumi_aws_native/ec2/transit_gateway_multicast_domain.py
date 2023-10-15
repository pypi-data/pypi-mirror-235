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

__all__ = ['TransitGatewayMulticastDomainArgs', 'TransitGatewayMulticastDomain']

@pulumi.input_type
class TransitGatewayMulticastDomainArgs:
    def __init__(__self__, *,
                 transit_gateway_id: pulumi.Input[str],
                 options: Optional[pulumi.Input['OptionsPropertiesArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['TransitGatewayMulticastDomainTagArgs']]]] = None):
        """
        The set of arguments for constructing a TransitGatewayMulticastDomain resource.
        :param pulumi.Input[str] transit_gateway_id: The ID of the transit gateway.
        :param pulumi.Input['OptionsPropertiesArgs'] options: The options for the transit gateway multicast domain.
        :param pulumi.Input[Sequence[pulumi.Input['TransitGatewayMulticastDomainTagArgs']]] tags: The tags for the transit gateway multicast domain.
        """
        TransitGatewayMulticastDomainArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            transit_gateway_id=transit_gateway_id,
            options=options,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             transit_gateway_id: pulumi.Input[str],
             options: Optional[pulumi.Input['OptionsPropertiesArgs']] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['TransitGatewayMulticastDomainTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("transit_gateway_id", transit_gateway_id)
        if options is not None:
            _setter("options", options)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> pulumi.Input[str]:
        """
        The ID of the transit gateway.
        """
        return pulumi.get(self, "transit_gateway_id")

    @transit_gateway_id.setter
    def transit_gateway_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "transit_gateway_id", value)

    @property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input['OptionsPropertiesArgs']]:
        """
        The options for the transit gateway multicast domain.
        """
        return pulumi.get(self, "options")

    @options.setter
    def options(self, value: Optional[pulumi.Input['OptionsPropertiesArgs']]):
        pulumi.set(self, "options", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TransitGatewayMulticastDomainTagArgs']]]]:
        """
        The tags for the transit gateway multicast domain.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TransitGatewayMulticastDomainTagArgs']]]]):
        pulumi.set(self, "tags", value)


class TransitGatewayMulticastDomain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 options: Optional[pulumi.Input[pulumi.InputType['OptionsPropertiesArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TransitGatewayMulticastDomainTagArgs']]]]] = None,
                 transit_gateway_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The AWS::EC2::TransitGatewayMulticastDomain type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['OptionsPropertiesArgs']] options: The options for the transit gateway multicast domain.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TransitGatewayMulticastDomainTagArgs']]]] tags: The tags for the transit gateway multicast domain.
        :param pulumi.Input[str] transit_gateway_id: The ID of the transit gateway.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TransitGatewayMulticastDomainArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::EC2::TransitGatewayMulticastDomain type

        :param str resource_name: The name of the resource.
        :param TransitGatewayMulticastDomainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TransitGatewayMulticastDomainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            TransitGatewayMulticastDomainArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 options: Optional[pulumi.Input[pulumi.InputType['OptionsPropertiesArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TransitGatewayMulticastDomainTagArgs']]]]] = None,
                 transit_gateway_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TransitGatewayMulticastDomainArgs.__new__(TransitGatewayMulticastDomainArgs)

            if options is not None and not isinstance(options, OptionsPropertiesArgs):
                options = options or {}
                def _setter(key, value):
                    options[key] = value
                OptionsPropertiesArgs._configure(_setter, **options)
            __props__.__dict__["options"] = options
            __props__.__dict__["tags"] = tags
            if transit_gateway_id is None and not opts.urn:
                raise TypeError("Missing required property 'transit_gateway_id'")
            __props__.__dict__["transit_gateway_id"] = transit_gateway_id
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["transit_gateway_multicast_domain_arn"] = None
            __props__.__dict__["transit_gateway_multicast_domain_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["transit_gateway_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(TransitGatewayMulticastDomain, __self__).__init__(
            'aws-native:ec2:TransitGatewayMulticastDomain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TransitGatewayMulticastDomain':
        """
        Get an existing TransitGatewayMulticastDomain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TransitGatewayMulticastDomainArgs.__new__(TransitGatewayMulticastDomainArgs)

        __props__.__dict__["creation_time"] = None
        __props__.__dict__["options"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["transit_gateway_id"] = None
        __props__.__dict__["transit_gateway_multicast_domain_arn"] = None
        __props__.__dict__["transit_gateway_multicast_domain_id"] = None
        return TransitGatewayMulticastDomain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        The time the transit gateway multicast domain was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def options(self) -> pulumi.Output[Optional['outputs.OptionsProperties']]:
        """
        The options for the transit gateway multicast domain.
        """
        return pulumi.get(self, "options")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the transit gateway multicast domain.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.TransitGatewayMulticastDomainTag']]]:
        """
        The tags for the transit gateway multicast domain.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> pulumi.Output[str]:
        """
        The ID of the transit gateway.
        """
        return pulumi.get(self, "transit_gateway_id")

    @property
    @pulumi.getter(name="transitGatewayMulticastDomainArn")
    def transit_gateway_multicast_domain_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the transit gateway multicast domain.
        """
        return pulumi.get(self, "transit_gateway_multicast_domain_arn")

    @property
    @pulumi.getter(name="transitGatewayMulticastDomainId")
    def transit_gateway_multicast_domain_id(self) -> pulumi.Output[str]:
        """
        The ID of the transit gateway multicast domain.
        """
        return pulumi.get(self, "transit_gateway_multicast_domain_id")

