# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['IpamAllocationArgs', 'IpamAllocation']

@pulumi.input_type
class IpamAllocationArgs:
    def __init__(__self__, *,
                 ipam_pool_id: pulumi.Input[str],
                 cidr: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 netmask_length: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a IpamAllocation resource.
        :param pulumi.Input[str] ipam_pool_id: Id of the IPAM Pool.
        :param pulumi.Input[int] netmask_length: The desired netmask length of the allocation. If set, IPAM will choose a block of free space with this size and return the CIDR representing it.
        """
        IpamAllocationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            ipam_pool_id=ipam_pool_id,
            cidr=cidr,
            description=description,
            netmask_length=netmask_length,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             ipam_pool_id: pulumi.Input[str],
             cidr: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             netmask_length: Optional[pulumi.Input[int]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("ipam_pool_id", ipam_pool_id)
        if cidr is not None:
            _setter("cidr", cidr)
        if description is not None:
            _setter("description", description)
        if netmask_length is not None:
            _setter("netmask_length", netmask_length)

    @property
    @pulumi.getter(name="ipamPoolId")
    def ipam_pool_id(self) -> pulumi.Input[str]:
        """
        Id of the IPAM Pool.
        """
        return pulumi.get(self, "ipam_pool_id")

    @ipam_pool_id.setter
    def ipam_pool_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "ipam_pool_id", value)

    @property
    @pulumi.getter
    def cidr(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cidr")

    @cidr.setter
    def cidr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cidr", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="netmaskLength")
    def netmask_length(self) -> Optional[pulumi.Input[int]]:
        """
        The desired netmask length of the allocation. If set, IPAM will choose a block of free space with this size and return the CIDR representing it.
        """
        return pulumi.get(self, "netmask_length")

    @netmask_length.setter
    def netmask_length(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "netmask_length", value)


class IpamAllocation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidr: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 netmask_length: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Resource Schema of AWS::EC2::IPAMAllocation Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] ipam_pool_id: Id of the IPAM Pool.
        :param pulumi.Input[int] netmask_length: The desired netmask length of the allocation. If set, IPAM will choose a block of free space with this size and return the CIDR representing it.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IpamAllocationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Schema of AWS::EC2::IPAMAllocation Type

        :param str resource_name: The name of the resource.
        :param IpamAllocationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IpamAllocationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            IpamAllocationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidr: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 netmask_length: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IpamAllocationArgs.__new__(IpamAllocationArgs)

            __props__.__dict__["cidr"] = cidr
            __props__.__dict__["description"] = description
            if ipam_pool_id is None and not opts.urn:
                raise TypeError("Missing required property 'ipam_pool_id'")
            __props__.__dict__["ipam_pool_id"] = ipam_pool_id
            __props__.__dict__["netmask_length"] = netmask_length
            __props__.__dict__["ipam_pool_allocation_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["cidr", "description", "ipam_pool_id", "netmask_length"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(IpamAllocation, __self__).__init__(
            'aws-native:ec2:IpamAllocation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IpamAllocation':
        """
        Get an existing IpamAllocation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IpamAllocationArgs.__new__(IpamAllocationArgs)

        __props__.__dict__["cidr"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["ipam_pool_allocation_id"] = None
        __props__.__dict__["ipam_pool_id"] = None
        __props__.__dict__["netmask_length"] = None
        return IpamAllocation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cidr(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "cidr")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="ipamPoolAllocationId")
    def ipam_pool_allocation_id(self) -> pulumi.Output[str]:
        """
        Id of the allocation.
        """
        return pulumi.get(self, "ipam_pool_allocation_id")

    @property
    @pulumi.getter(name="ipamPoolId")
    def ipam_pool_id(self) -> pulumi.Output[str]:
        """
        Id of the IPAM Pool.
        """
        return pulumi.get(self, "ipam_pool_id")

    @property
    @pulumi.getter(name="netmaskLength")
    def netmask_length(self) -> pulumi.Output[Optional[int]]:
        """
        The desired netmask length of the allocation. If set, IPAM will choose a block of free space with this size and return the CIDR representing it.
        """
        return pulumi.get(self, "netmask_length")

