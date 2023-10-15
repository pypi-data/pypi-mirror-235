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
from ._enums import *

__all__ = [
    'GetVpcIngressConnectionResult',
    'AwaitableGetVpcIngressConnectionResult',
    'get_vpc_ingress_connection',
    'get_vpc_ingress_connection_output',
]

@pulumi.output_type
class GetVpcIngressConnectionResult:
    def __init__(__self__, domain_name=None, ingress_vpc_configuration=None, status=None, vpc_ingress_connection_arn=None):
        if domain_name and not isinstance(domain_name, str):
            raise TypeError("Expected argument 'domain_name' to be a str")
        pulumi.set(__self__, "domain_name", domain_name)
        if ingress_vpc_configuration and not isinstance(ingress_vpc_configuration, dict):
            raise TypeError("Expected argument 'ingress_vpc_configuration' to be a dict")
        pulumi.set(__self__, "ingress_vpc_configuration", ingress_vpc_configuration)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if vpc_ingress_connection_arn and not isinstance(vpc_ingress_connection_arn, str):
            raise TypeError("Expected argument 'vpc_ingress_connection_arn' to be a str")
        pulumi.set(__self__, "vpc_ingress_connection_arn", vpc_ingress_connection_arn)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[str]:
        """
        The Domain name associated with the VPC Ingress Connection.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="ingressVpcConfiguration")
    def ingress_vpc_configuration(self) -> Optional['outputs.VpcIngressConnectionIngressVpcConfiguration']:
        return pulumi.get(self, "ingress_vpc_configuration")

    @property
    @pulumi.getter
    def status(self) -> Optional['VpcIngressConnectionStatus']:
        """
        The current status of the VpcIngressConnection.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="vpcIngressConnectionArn")
    def vpc_ingress_connection_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the VpcIngressConnection.
        """
        return pulumi.get(self, "vpc_ingress_connection_arn")


class AwaitableGetVpcIngressConnectionResult(GetVpcIngressConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpcIngressConnectionResult(
            domain_name=self.domain_name,
            ingress_vpc_configuration=self.ingress_vpc_configuration,
            status=self.status,
            vpc_ingress_connection_arn=self.vpc_ingress_connection_arn)


def get_vpc_ingress_connection(vpc_ingress_connection_arn: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpcIngressConnectionResult:
    """
    The AWS::AppRunner::VpcIngressConnection resource is an App Runner resource that specifies an App Runner VpcIngressConnection.


    :param str vpc_ingress_connection_arn: The Amazon Resource Name (ARN) of the VpcIngressConnection.
    """
    __args__ = dict()
    __args__['vpcIngressConnectionArn'] = vpc_ingress_connection_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:apprunner:getVpcIngressConnection', __args__, opts=opts, typ=GetVpcIngressConnectionResult).value

    return AwaitableGetVpcIngressConnectionResult(
        domain_name=pulumi.get(__ret__, 'domain_name'),
        ingress_vpc_configuration=pulumi.get(__ret__, 'ingress_vpc_configuration'),
        status=pulumi.get(__ret__, 'status'),
        vpc_ingress_connection_arn=pulumi.get(__ret__, 'vpc_ingress_connection_arn'))


@_utilities.lift_output_func(get_vpc_ingress_connection)
def get_vpc_ingress_connection_output(vpc_ingress_connection_arn: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVpcIngressConnectionResult]:
    """
    The AWS::AppRunner::VpcIngressConnection resource is an App Runner resource that specifies an App Runner VpcIngressConnection.


    :param str vpc_ingress_connection_arn: The Amazon Resource Name (ARN) of the VpcIngressConnection.
    """
    ...
