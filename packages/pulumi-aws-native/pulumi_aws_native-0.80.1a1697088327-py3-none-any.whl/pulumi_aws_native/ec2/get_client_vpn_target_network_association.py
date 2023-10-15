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
    'GetClientVpnTargetNetworkAssociationResult',
    'AwaitableGetClientVpnTargetNetworkAssociationResult',
    'get_client_vpn_target_network_association',
    'get_client_vpn_target_network_association_output',
]

@pulumi.output_type
class GetClientVpnTargetNetworkAssociationResult:
    def __init__(__self__, id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetClientVpnTargetNetworkAssociationResult(GetClientVpnTargetNetworkAssociationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClientVpnTargetNetworkAssociationResult(
            id=self.id)


def get_client_vpn_target_network_association(id: Optional[str] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClientVpnTargetNetworkAssociationResult:
    """
    Resource Type definition for AWS::EC2::ClientVpnTargetNetworkAssociation
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getClientVpnTargetNetworkAssociation', __args__, opts=opts, typ=GetClientVpnTargetNetworkAssociationResult).value

    return AwaitableGetClientVpnTargetNetworkAssociationResult(
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_client_vpn_target_network_association)
def get_client_vpn_target_network_association_output(id: Optional[pulumi.Input[str]] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClientVpnTargetNetworkAssociationResult]:
    """
    Resource Type definition for AWS::EC2::ClientVpnTargetNetworkAssociation
    """
    ...
