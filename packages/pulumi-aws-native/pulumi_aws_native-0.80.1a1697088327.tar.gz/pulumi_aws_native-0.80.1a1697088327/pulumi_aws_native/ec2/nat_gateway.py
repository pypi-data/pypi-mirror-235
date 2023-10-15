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

__all__ = ['NatGatewayArgs', 'NatGateway']

@pulumi.input_type
class NatGatewayArgs:
    def __init__(__self__, *,
                 subnet_id: pulumi.Input[str],
                 allocation_id: Optional[pulumi.Input[str]] = None,
                 connectivity_type: Optional[pulumi.Input[str]] = None,
                 max_drain_duration_seconds: Optional[pulumi.Input[int]] = None,
                 private_ip_address: Optional[pulumi.Input[str]] = None,
                 secondary_allocation_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 secondary_private_ip_address_count: Optional[pulumi.Input[int]] = None,
                 secondary_private_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['NatGatewayTagArgs']]]] = None):
        """
        The set of arguments for constructing a NatGateway resource.
        """
        NatGatewayArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            subnet_id=subnet_id,
            allocation_id=allocation_id,
            connectivity_type=connectivity_type,
            max_drain_duration_seconds=max_drain_duration_seconds,
            private_ip_address=private_ip_address,
            secondary_allocation_ids=secondary_allocation_ids,
            secondary_private_ip_address_count=secondary_private_ip_address_count,
            secondary_private_ip_addresses=secondary_private_ip_addresses,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             subnet_id: pulumi.Input[str],
             allocation_id: Optional[pulumi.Input[str]] = None,
             connectivity_type: Optional[pulumi.Input[str]] = None,
             max_drain_duration_seconds: Optional[pulumi.Input[int]] = None,
             private_ip_address: Optional[pulumi.Input[str]] = None,
             secondary_allocation_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             secondary_private_ip_address_count: Optional[pulumi.Input[int]] = None,
             secondary_private_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['NatGatewayTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("subnet_id", subnet_id)
        if allocation_id is not None:
            _setter("allocation_id", allocation_id)
        if connectivity_type is not None:
            _setter("connectivity_type", connectivity_type)
        if max_drain_duration_seconds is not None:
            _setter("max_drain_duration_seconds", max_drain_duration_seconds)
        if private_ip_address is not None:
            _setter("private_ip_address", private_ip_address)
        if secondary_allocation_ids is not None:
            _setter("secondary_allocation_ids", secondary_allocation_ids)
        if secondary_private_ip_address_count is not None:
            _setter("secondary_private_ip_address_count", secondary_private_ip_address_count)
        if secondary_private_ip_addresses is not None:
            _setter("secondary_private_ip_addresses", secondary_private_ip_addresses)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "allocation_id")

    @allocation_id.setter
    def allocation_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "allocation_id", value)

    @property
    @pulumi.getter(name="connectivityType")
    def connectivity_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "connectivity_type")

    @connectivity_type.setter
    def connectivity_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connectivity_type", value)

    @property
    @pulumi.getter(name="maxDrainDurationSeconds")
    def max_drain_duration_seconds(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "max_drain_duration_seconds")

    @max_drain_duration_seconds.setter
    def max_drain_duration_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_drain_duration_seconds", value)

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "private_ip_address")

    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_ip_address", value)

    @property
    @pulumi.getter(name="secondaryAllocationIds")
    def secondary_allocation_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "secondary_allocation_ids")

    @secondary_allocation_ids.setter
    def secondary_allocation_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "secondary_allocation_ids", value)

    @property
    @pulumi.getter(name="secondaryPrivateIpAddressCount")
    def secondary_private_ip_address_count(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "secondary_private_ip_address_count")

    @secondary_private_ip_address_count.setter
    def secondary_private_ip_address_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "secondary_private_ip_address_count", value)

    @property
    @pulumi.getter(name="secondaryPrivateIpAddresses")
    def secondary_private_ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "secondary_private_ip_addresses")

    @secondary_private_ip_addresses.setter
    def secondary_private_ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "secondary_private_ip_addresses", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NatGatewayTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NatGatewayTagArgs']]]]):
        pulumi.set(self, "tags", value)


class NatGateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allocation_id: Optional[pulumi.Input[str]] = None,
                 connectivity_type: Optional[pulumi.Input[str]] = None,
                 max_drain_duration_seconds: Optional[pulumi.Input[int]] = None,
                 private_ip_address: Optional[pulumi.Input[str]] = None,
                 secondary_allocation_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 secondary_private_ip_address_count: Optional[pulumi.Input[int]] = None,
                 secondary_private_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NatGatewayTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EC2::NatGateway

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NatGatewayArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EC2::NatGateway

        :param str resource_name: The name of the resource.
        :param NatGatewayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NatGatewayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            NatGatewayArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allocation_id: Optional[pulumi.Input[str]] = None,
                 connectivity_type: Optional[pulumi.Input[str]] = None,
                 max_drain_duration_seconds: Optional[pulumi.Input[int]] = None,
                 private_ip_address: Optional[pulumi.Input[str]] = None,
                 secondary_allocation_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 secondary_private_ip_address_count: Optional[pulumi.Input[int]] = None,
                 secondary_private_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NatGatewayTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NatGatewayArgs.__new__(NatGatewayArgs)

            __props__.__dict__["allocation_id"] = allocation_id
            __props__.__dict__["connectivity_type"] = connectivity_type
            __props__.__dict__["max_drain_duration_seconds"] = max_drain_duration_seconds
            __props__.__dict__["private_ip_address"] = private_ip_address
            __props__.__dict__["secondary_allocation_ids"] = secondary_allocation_ids
            __props__.__dict__["secondary_private_ip_address_count"] = secondary_private_ip_address_count
            __props__.__dict__["secondary_private_ip_addresses"] = secondary_private_ip_addresses
            if subnet_id is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_id'")
            __props__.__dict__["subnet_id"] = subnet_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["nat_gateway_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["allocation_id", "connectivity_type", "private_ip_address", "subnet_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(NatGateway, __self__).__init__(
            'aws-native:ec2:NatGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NatGateway':
        """
        Get an existing NatGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NatGatewayArgs.__new__(NatGatewayArgs)

        __props__.__dict__["allocation_id"] = None
        __props__.__dict__["connectivity_type"] = None
        __props__.__dict__["max_drain_duration_seconds"] = None
        __props__.__dict__["nat_gateway_id"] = None
        __props__.__dict__["private_ip_address"] = None
        __props__.__dict__["secondary_allocation_ids"] = None
        __props__.__dict__["secondary_private_ip_address_count"] = None
        __props__.__dict__["secondary_private_ip_addresses"] = None
        __props__.__dict__["subnet_id"] = None
        __props__.__dict__["tags"] = None
        return NatGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "allocation_id")

    @property
    @pulumi.getter(name="connectivityType")
    def connectivity_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "connectivity_type")

    @property
    @pulumi.getter(name="maxDrainDurationSeconds")
    def max_drain_duration_seconds(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "max_drain_duration_seconds")

    @property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "nat_gateway_id")

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "private_ip_address")

    @property
    @pulumi.getter(name="secondaryAllocationIds")
    def secondary_allocation_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "secondary_allocation_ids")

    @property
    @pulumi.getter(name="secondaryPrivateIpAddressCount")
    def secondary_private_ip_address_count(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "secondary_private_ip_address_count")

    @property
    @pulumi.getter(name="secondaryPrivateIpAddresses")
    def secondary_private_ip_addresses(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "secondary_private_ip_addresses")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.NatGatewayTag']]]:
        return pulumi.get(self, "tags")

