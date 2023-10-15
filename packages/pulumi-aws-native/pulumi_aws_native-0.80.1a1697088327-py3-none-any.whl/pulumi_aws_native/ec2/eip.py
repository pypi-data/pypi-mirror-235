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

__all__ = ['EipArgs', 'Eip']

@pulumi.input_type
class EipArgs:
    def __init__(__self__, *,
                 domain: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 network_border_group: Optional[pulumi.Input[str]] = None,
                 public_ipv4_pool: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['EipTagArgs']]]] = None,
                 transfer_address: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Eip resource.
        :param pulumi.Input[str] domain: Indicates whether the Elastic IP address is for use with instances in a VPC or instance in EC2-Classic.
        :param pulumi.Input[str] instance_id: The ID of the instance.
        :param pulumi.Input[str] network_border_group: A unique set of Availability Zones, Local Zones, or Wavelength Zones from which Amazon Web Services advertises IP addresses.
        :param pulumi.Input[str] public_ipv4_pool: The ID of an address pool that you own. Use this parameter to let Amazon EC2 select an address from the address pool.
        :param pulumi.Input[Sequence[pulumi.Input['EipTagArgs']]] tags: Any tags assigned to the EIP.
        :param pulumi.Input[str] transfer_address: The PublicIP of the EIP generated by resource through transfer from another account
        """
        EipArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            domain=domain,
            instance_id=instance_id,
            network_border_group=network_border_group,
            public_ipv4_pool=public_ipv4_pool,
            tags=tags,
            transfer_address=transfer_address,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             domain: Optional[pulumi.Input[str]] = None,
             instance_id: Optional[pulumi.Input[str]] = None,
             network_border_group: Optional[pulumi.Input[str]] = None,
             public_ipv4_pool: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['EipTagArgs']]]] = None,
             transfer_address: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if domain is not None:
            _setter("domain", domain)
        if instance_id is not None:
            _setter("instance_id", instance_id)
        if network_border_group is not None:
            _setter("network_border_group", network_border_group)
        if public_ipv4_pool is not None:
            _setter("public_ipv4_pool", public_ipv4_pool)
        if tags is not None:
            _setter("tags", tags)
        if transfer_address is not None:
            _setter("transfer_address", transfer_address)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates whether the Elastic IP address is for use with instances in a VPC or instance in EC2-Classic.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the instance.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="networkBorderGroup")
    def network_border_group(self) -> Optional[pulumi.Input[str]]:
        """
        A unique set of Availability Zones, Local Zones, or Wavelength Zones from which Amazon Web Services advertises IP addresses.
        """
        return pulumi.get(self, "network_border_group")

    @network_border_group.setter
    def network_border_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_border_group", value)

    @property
    @pulumi.getter(name="publicIpv4Pool")
    def public_ipv4_pool(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of an address pool that you own. Use this parameter to let Amazon EC2 select an address from the address pool.
        """
        return pulumi.get(self, "public_ipv4_pool")

    @public_ipv4_pool.setter
    def public_ipv4_pool(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_ipv4_pool", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EipTagArgs']]]]:
        """
        Any tags assigned to the EIP.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EipTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="transferAddress")
    def transfer_address(self) -> Optional[pulumi.Input[str]]:
        """
        The PublicIP of the EIP generated by resource through transfer from another account
        """
        return pulumi.get(self, "transfer_address")

    @transfer_address.setter
    def transfer_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "transfer_address", value)


class Eip(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 network_border_group: Optional[pulumi.Input[str]] = None,
                 public_ipv4_pool: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EipTagArgs']]]]] = None,
                 transfer_address: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EC2::EIP

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain: Indicates whether the Elastic IP address is for use with instances in a VPC or instance in EC2-Classic.
        :param pulumi.Input[str] instance_id: The ID of the instance.
        :param pulumi.Input[str] network_border_group: A unique set of Availability Zones, Local Zones, or Wavelength Zones from which Amazon Web Services advertises IP addresses.
        :param pulumi.Input[str] public_ipv4_pool: The ID of an address pool that you own. Use this parameter to let Amazon EC2 select an address from the address pool.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EipTagArgs']]]] tags: Any tags assigned to the EIP.
        :param pulumi.Input[str] transfer_address: The PublicIP of the EIP generated by resource through transfer from another account
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[EipArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EC2::EIP

        :param str resource_name: The name of the resource.
        :param EipArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EipArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            EipArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 network_border_group: Optional[pulumi.Input[str]] = None,
                 public_ipv4_pool: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EipTagArgs']]]]] = None,
                 transfer_address: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EipArgs.__new__(EipArgs)

            __props__.__dict__["domain"] = domain
            __props__.__dict__["instance_id"] = instance_id
            __props__.__dict__["network_border_group"] = network_border_group
            __props__.__dict__["public_ipv4_pool"] = public_ipv4_pool
            __props__.__dict__["tags"] = tags
            __props__.__dict__["transfer_address"] = transfer_address
            __props__.__dict__["allocation_id"] = None
            __props__.__dict__["public_ip"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["domain", "network_border_group", "transfer_address"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Eip, __self__).__init__(
            'aws-native:ec2:Eip',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Eip':
        """
        Get an existing Eip resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EipArgs.__new__(EipArgs)

        __props__.__dict__["allocation_id"] = None
        __props__.__dict__["domain"] = None
        __props__.__dict__["instance_id"] = None
        __props__.__dict__["network_border_group"] = None
        __props__.__dict__["public_ip"] = None
        __props__.__dict__["public_ipv4_pool"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["transfer_address"] = None
        return Eip(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> pulumi.Output[str]:
        """
        The Allocation ID of the EIP generated by resource.
        """
        return pulumi.get(self, "allocation_id")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[Optional[str]]:
        """
        Indicates whether the Elastic IP address is for use with instances in a VPC or instance in EC2-Classic.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the instance.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="networkBorderGroup")
    def network_border_group(self) -> pulumi.Output[Optional[str]]:
        """
        A unique set of Availability Zones, Local Zones, or Wavelength Zones from which Amazon Web Services advertises IP addresses.
        """
        return pulumi.get(self, "network_border_group")

    @property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> pulumi.Output[str]:
        """
        The PublicIP of the EIP generated by resource.
        """
        return pulumi.get(self, "public_ip")

    @property
    @pulumi.getter(name="publicIpv4Pool")
    def public_ipv4_pool(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of an address pool that you own. Use this parameter to let Amazon EC2 select an address from the address pool.
        """
        return pulumi.get(self, "public_ipv4_pool")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.EipTag']]]:
        """
        Any tags assigned to the EIP.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="transferAddress")
    def transfer_address(self) -> pulumi.Output[Optional[str]]:
        """
        The PublicIP of the EIP generated by resource through transfer from another account
        """
        return pulumi.get(self, "transfer_address")

