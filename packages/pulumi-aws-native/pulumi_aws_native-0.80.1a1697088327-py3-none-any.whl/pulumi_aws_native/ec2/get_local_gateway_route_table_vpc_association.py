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
    'GetLocalGatewayRouteTableVpcAssociationResult',
    'AwaitableGetLocalGatewayRouteTableVpcAssociationResult',
    'get_local_gateway_route_table_vpc_association',
    'get_local_gateway_route_table_vpc_association_output',
]

@pulumi.output_type
class GetLocalGatewayRouteTableVpcAssociationResult:
    def __init__(__self__, local_gateway_id=None, local_gateway_route_table_vpc_association_id=None, state=None, tags=None):
        if local_gateway_id and not isinstance(local_gateway_id, str):
            raise TypeError("Expected argument 'local_gateway_id' to be a str")
        pulumi.set(__self__, "local_gateway_id", local_gateway_id)
        if local_gateway_route_table_vpc_association_id and not isinstance(local_gateway_route_table_vpc_association_id, str):
            raise TypeError("Expected argument 'local_gateway_route_table_vpc_association_id' to be a str")
        pulumi.set(__self__, "local_gateway_route_table_vpc_association_id", local_gateway_route_table_vpc_association_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="localGatewayId")
    def local_gateway_id(self) -> Optional[str]:
        """
        The ID of the local gateway.
        """
        return pulumi.get(self, "local_gateway_id")

    @property
    @pulumi.getter(name="localGatewayRouteTableVpcAssociationId")
    def local_gateway_route_table_vpc_association_id(self) -> Optional[str]:
        """
        The ID of the association.
        """
        return pulumi.get(self, "local_gateway_route_table_vpc_association_id")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The state of the association.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.LocalGatewayRouteTableVpcAssociationTag']]:
        """
        The tags for the association.
        """
        return pulumi.get(self, "tags")


class AwaitableGetLocalGatewayRouteTableVpcAssociationResult(GetLocalGatewayRouteTableVpcAssociationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLocalGatewayRouteTableVpcAssociationResult(
            local_gateway_id=self.local_gateway_id,
            local_gateway_route_table_vpc_association_id=self.local_gateway_route_table_vpc_association_id,
            state=self.state,
            tags=self.tags)


def get_local_gateway_route_table_vpc_association(local_gateway_route_table_vpc_association_id: Optional[str] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLocalGatewayRouteTableVpcAssociationResult:
    """
    Describes an association between a local gateway route table and a VPC.


    :param str local_gateway_route_table_vpc_association_id: The ID of the association.
    """
    __args__ = dict()
    __args__['localGatewayRouteTableVpcAssociationId'] = local_gateway_route_table_vpc_association_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getLocalGatewayRouteTableVpcAssociation', __args__, opts=opts, typ=GetLocalGatewayRouteTableVpcAssociationResult).value

    return AwaitableGetLocalGatewayRouteTableVpcAssociationResult(
        local_gateway_id=pulumi.get(__ret__, 'local_gateway_id'),
        local_gateway_route_table_vpc_association_id=pulumi.get(__ret__, 'local_gateway_route_table_vpc_association_id'),
        state=pulumi.get(__ret__, 'state'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_local_gateway_route_table_vpc_association)
def get_local_gateway_route_table_vpc_association_output(local_gateway_route_table_vpc_association_id: Optional[pulumi.Input[str]] = None,
                                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLocalGatewayRouteTableVpcAssociationResult]:
    """
    Describes an association between a local gateway route table and a VPC.


    :param str local_gateway_route_table_vpc_association_id: The ID of the association.
    """
    ...
