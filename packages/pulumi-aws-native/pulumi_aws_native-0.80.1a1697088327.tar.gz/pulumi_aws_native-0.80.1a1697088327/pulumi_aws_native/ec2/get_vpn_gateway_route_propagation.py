# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetVpnGatewayRoutePropagationResult',
    'AwaitableGetVpnGatewayRoutePropagationResult',
    'get_vpn_gateway_route_propagation',
    'get_vpn_gateway_route_propagation_output',
]

@pulumi.output_type
class GetVpnGatewayRoutePropagationResult:
    def __init__(__self__, id=None, route_table_ids=None, vpn_gateway_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if route_table_ids and not isinstance(route_table_ids, list):
            raise TypeError("Expected argument 'route_table_ids' to be a list")
        pulumi.set(__self__, "route_table_ids", route_table_ids)
        if vpn_gateway_id and not isinstance(vpn_gateway_id, str):
            raise TypeError("Expected argument 'vpn_gateway_id' to be a str")
        pulumi.set(__self__, "vpn_gateway_id", vpn_gateway_id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="routeTableIds")
    def route_table_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "route_table_ids")

    @property
    @pulumi.getter(name="vpnGatewayId")
    def vpn_gateway_id(self) -> Optional[str]:
        return pulumi.get(self, "vpn_gateway_id")


class AwaitableGetVpnGatewayRoutePropagationResult(GetVpnGatewayRoutePropagationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpnGatewayRoutePropagationResult(
            id=self.id,
            route_table_ids=self.route_table_ids,
            vpn_gateway_id=self.vpn_gateway_id)


def get_vpn_gateway_route_propagation(id: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpnGatewayRoutePropagationResult:
    """
    Resource Type definition for AWS::EC2::VPNGatewayRoutePropagation
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getVpnGatewayRoutePropagation', __args__, opts=opts, typ=GetVpnGatewayRoutePropagationResult).value

    return AwaitableGetVpnGatewayRoutePropagationResult(
        id=pulumi.get(__ret__, 'id'),
        route_table_ids=pulumi.get(__ret__, 'route_table_ids'),
        vpn_gateway_id=pulumi.get(__ret__, 'vpn_gateway_id'))


@_utilities.lift_output_func(get_vpn_gateway_route_propagation)
def get_vpn_gateway_route_propagation_output(id: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVpnGatewayRoutePropagationResult]:
    """
    Resource Type definition for AWS::EC2::VPNGatewayRoutePropagation
    """
    ...
