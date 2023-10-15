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

__all__ = ['CustomerGatewayArgs', 'CustomerGateway']

@pulumi.input_type
class CustomerGatewayArgs:
    def __init__(__self__, *,
                 bgp_asn: pulumi.Input[int],
                 ip_address: pulumi.Input[str],
                 type: pulumi.Input[str],
                 device_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['CustomerGatewayTagArgs']]]] = None):
        """
        The set of arguments for constructing a CustomerGateway resource.
        :param pulumi.Input[int] bgp_asn: For devices that support BGP, the customer gateway's BGP ASN.
        :param pulumi.Input[str] ip_address: The internet-routable IP address for the customer gateway's outside interface. The address must be static.
        :param pulumi.Input[str] type: The type of VPN connection that this customer gateway supports.
        :param pulumi.Input[str] device_name: A name for the customer gateway device.
        :param pulumi.Input[Sequence[pulumi.Input['CustomerGatewayTagArgs']]] tags: One or more tags for the customer gateway.
        """
        CustomerGatewayArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            bgp_asn=bgp_asn,
            ip_address=ip_address,
            type=type,
            device_name=device_name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             bgp_asn: pulumi.Input[int],
             ip_address: pulumi.Input[str],
             type: pulumi.Input[str],
             device_name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['CustomerGatewayTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("bgp_asn", bgp_asn)
        _setter("ip_address", ip_address)
        _setter("type", type)
        if device_name is not None:
            _setter("device_name", device_name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="bgpAsn")
    def bgp_asn(self) -> pulumi.Input[int]:
        """
        For devices that support BGP, the customer gateway's BGP ASN.
        """
        return pulumi.get(self, "bgp_asn")

    @bgp_asn.setter
    def bgp_asn(self, value: pulumi.Input[int]):
        pulumi.set(self, "bgp_asn", value)

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Input[str]:
        """
        The internet-routable IP address for the customer gateway's outside interface. The address must be static.
        """
        return pulumi.get(self, "ip_address")

    @ip_address.setter
    def ip_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "ip_address", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of VPN connection that this customer gateway supports.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[pulumi.Input[str]]:
        """
        A name for the customer gateway device.
        """
        return pulumi.get(self, "device_name")

    @device_name.setter
    def device_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "device_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CustomerGatewayTagArgs']]]]:
        """
        One or more tags for the customer gateway.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CustomerGatewayTagArgs']]]]):
        pulumi.set(self, "tags", value)


class CustomerGateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bgp_asn: Optional[pulumi.Input[int]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomerGatewayTagArgs']]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EC2::CustomerGateway

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] bgp_asn: For devices that support BGP, the customer gateway's BGP ASN.
        :param pulumi.Input[str] device_name: A name for the customer gateway device.
        :param pulumi.Input[str] ip_address: The internet-routable IP address for the customer gateway's outside interface. The address must be static.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomerGatewayTagArgs']]]] tags: One or more tags for the customer gateway.
        :param pulumi.Input[str] type: The type of VPN connection that this customer gateway supports.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CustomerGatewayArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EC2::CustomerGateway

        :param str resource_name: The name of the resource.
        :param CustomerGatewayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomerGatewayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            CustomerGatewayArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bgp_asn: Optional[pulumi.Input[int]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomerGatewayTagArgs']]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CustomerGatewayArgs.__new__(CustomerGatewayArgs)

            if bgp_asn is None and not opts.urn:
                raise TypeError("Missing required property 'bgp_asn'")
            __props__.__dict__["bgp_asn"] = bgp_asn
            __props__.__dict__["device_name"] = device_name
            if ip_address is None and not opts.urn:
                raise TypeError("Missing required property 'ip_address'")
            __props__.__dict__["ip_address"] = ip_address
            __props__.__dict__["tags"] = tags
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["customer_gateway_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["bgp_asn", "device_name", "ip_address", "type"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(CustomerGateway, __self__).__init__(
            'aws-native:ec2:CustomerGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CustomerGateway':
        """
        Get an existing CustomerGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CustomerGatewayArgs.__new__(CustomerGatewayArgs)

        __props__.__dict__["bgp_asn"] = None
        __props__.__dict__["customer_gateway_id"] = None
        __props__.__dict__["device_name"] = None
        __props__.__dict__["ip_address"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return CustomerGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bgpAsn")
    def bgp_asn(self) -> pulumi.Output[int]:
        """
        For devices that support BGP, the customer gateway's BGP ASN.
        """
        return pulumi.get(self, "bgp_asn")

    @property
    @pulumi.getter(name="customerGatewayId")
    def customer_gateway_id(self) -> pulumi.Output[str]:
        """
        CustomerGateway ID generated after customer gateway is created. Each customer gateway has a unique ID.
        """
        return pulumi.get(self, "customer_gateway_id")

    @property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Output[Optional[str]]:
        """
        A name for the customer gateway device.
        """
        return pulumi.get(self, "device_name")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[str]:
        """
        The internet-routable IP address for the customer gateway's outside interface. The address must be static.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.CustomerGatewayTag']]]:
        """
        One or more tags for the customer gateway.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of VPN connection that this customer gateway supports.
        """
        return pulumi.get(self, "type")

