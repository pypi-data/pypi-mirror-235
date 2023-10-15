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

__all__ = [
    'GetNatGatewayResult',
    'AwaitableGetNatGatewayResult',
    'get_nat_gateway',
    'get_nat_gateway_output',
]

@pulumi.output_type
class GetNatGatewayResult:
    def __init__(__self__, nat_gateway_id=None, secondary_allocation_ids=None, secondary_private_ip_address_count=None, secondary_private_ip_addresses=None, tags=None):
        if nat_gateway_id and not isinstance(nat_gateway_id, str):
            raise TypeError("Expected argument 'nat_gateway_id' to be a str")
        pulumi.set(__self__, "nat_gateway_id", nat_gateway_id)
        if secondary_allocation_ids and not isinstance(secondary_allocation_ids, list):
            raise TypeError("Expected argument 'secondary_allocation_ids' to be a list")
        pulumi.set(__self__, "secondary_allocation_ids", secondary_allocation_ids)
        if secondary_private_ip_address_count and not isinstance(secondary_private_ip_address_count, int):
            raise TypeError("Expected argument 'secondary_private_ip_address_count' to be a int")
        pulumi.set(__self__, "secondary_private_ip_address_count", secondary_private_ip_address_count)
        if secondary_private_ip_addresses and not isinstance(secondary_private_ip_addresses, list):
            raise TypeError("Expected argument 'secondary_private_ip_addresses' to be a list")
        pulumi.set(__self__, "secondary_private_ip_addresses", secondary_private_ip_addresses)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> Optional[str]:
        return pulumi.get(self, "nat_gateway_id")

    @property
    @pulumi.getter(name="secondaryAllocationIds")
    def secondary_allocation_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "secondary_allocation_ids")

    @property
    @pulumi.getter(name="secondaryPrivateIpAddressCount")
    def secondary_private_ip_address_count(self) -> Optional[int]:
        return pulumi.get(self, "secondary_private_ip_address_count")

    @property
    @pulumi.getter(name="secondaryPrivateIpAddresses")
    def secondary_private_ip_addresses(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "secondary_private_ip_addresses")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.NatGatewayTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetNatGatewayResult(GetNatGatewayResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNatGatewayResult(
            nat_gateway_id=self.nat_gateway_id,
            secondary_allocation_ids=self.secondary_allocation_ids,
            secondary_private_ip_address_count=self.secondary_private_ip_address_count,
            secondary_private_ip_addresses=self.secondary_private_ip_addresses,
            tags=self.tags)


def get_nat_gateway(nat_gateway_id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNatGatewayResult:
    """
    Resource Type definition for AWS::EC2::NatGateway
    """
    __args__ = dict()
    __args__['natGatewayId'] = nat_gateway_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getNatGateway', __args__, opts=opts, typ=GetNatGatewayResult).value

    return AwaitableGetNatGatewayResult(
        nat_gateway_id=pulumi.get(__ret__, 'nat_gateway_id'),
        secondary_allocation_ids=pulumi.get(__ret__, 'secondary_allocation_ids'),
        secondary_private_ip_address_count=pulumi.get(__ret__, 'secondary_private_ip_address_count'),
        secondary_private_ip_addresses=pulumi.get(__ret__, 'secondary_private_ip_addresses'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_nat_gateway)
def get_nat_gateway_output(nat_gateway_id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNatGatewayResult]:
    """
    Resource Type definition for AWS::EC2::NatGateway
    """
    ...
