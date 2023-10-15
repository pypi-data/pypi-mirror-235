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
    'GetClientVpnRouteResult',
    'AwaitableGetClientVpnRouteResult',
    'get_client_vpn_route',
    'get_client_vpn_route_output',
]

@pulumi.output_type
class GetClientVpnRouteResult:
    def __init__(__self__, id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetClientVpnRouteResult(GetClientVpnRouteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClientVpnRouteResult(
            id=self.id)


def get_client_vpn_route(id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClientVpnRouteResult:
    """
    Resource Type definition for AWS::EC2::ClientVpnRoute
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getClientVpnRoute', __args__, opts=opts, typ=GetClientVpnRouteResult).value

    return AwaitableGetClientVpnRouteResult(
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_client_vpn_route)
def get_client_vpn_route_output(id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClientVpnRouteResult]:
    """
    Resource Type definition for AWS::EC2::ClientVpnRoute
    """
    ...
