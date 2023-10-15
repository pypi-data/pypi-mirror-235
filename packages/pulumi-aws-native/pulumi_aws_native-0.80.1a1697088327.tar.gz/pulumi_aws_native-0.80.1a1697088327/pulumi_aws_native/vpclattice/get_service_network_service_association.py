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
    'GetServiceNetworkServiceAssociationResult',
    'AwaitableGetServiceNetworkServiceAssociationResult',
    'get_service_network_service_association',
    'get_service_network_service_association_output',
]

@pulumi.output_type
class GetServiceNetworkServiceAssociationResult:
    def __init__(__self__, arn=None, created_at=None, dns_entry=None, id=None, service_arn=None, service_id=None, service_name=None, service_network_arn=None, service_network_id=None, service_network_name=None, status=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if dns_entry and not isinstance(dns_entry, dict):
            raise TypeError("Expected argument 'dns_entry' to be a dict")
        pulumi.set(__self__, "dns_entry", dns_entry)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if service_arn and not isinstance(service_arn, str):
            raise TypeError("Expected argument 'service_arn' to be a str")
        pulumi.set(__self__, "service_arn", service_arn)
        if service_id and not isinstance(service_id, str):
            raise TypeError("Expected argument 'service_id' to be a str")
        pulumi.set(__self__, "service_id", service_id)
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        pulumi.set(__self__, "service_name", service_name)
        if service_network_arn and not isinstance(service_network_arn, str):
            raise TypeError("Expected argument 'service_network_arn' to be a str")
        pulumi.set(__self__, "service_network_arn", service_network_arn)
        if service_network_id and not isinstance(service_network_id, str):
            raise TypeError("Expected argument 'service_network_id' to be a str")
        pulumi.set(__self__, "service_network_id", service_network_id)
        if service_network_name and not isinstance(service_network_name, str):
            raise TypeError("Expected argument 'service_network_name' to be a str")
        pulumi.set(__self__, "service_network_name", service_network_name)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="dnsEntry")
    def dns_entry(self) -> Optional['outputs.ServiceNetworkServiceAssociationDnsEntry']:
        return pulumi.get(self, "dns_entry")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="serviceArn")
    def service_arn(self) -> Optional[str]:
        return pulumi.get(self, "service_arn")

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[str]:
        return pulumi.get(self, "service_id")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[str]:
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter(name="serviceNetworkArn")
    def service_network_arn(self) -> Optional[str]:
        return pulumi.get(self, "service_network_arn")

    @property
    @pulumi.getter(name="serviceNetworkId")
    def service_network_id(self) -> Optional[str]:
        return pulumi.get(self, "service_network_id")

    @property
    @pulumi.getter(name="serviceNetworkName")
    def service_network_name(self) -> Optional[str]:
        return pulumi.get(self, "service_network_name")

    @property
    @pulumi.getter
    def status(self) -> Optional['ServiceNetworkServiceAssociationStatus']:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ServiceNetworkServiceAssociationTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetServiceNetworkServiceAssociationResult(GetServiceNetworkServiceAssociationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceNetworkServiceAssociationResult(
            arn=self.arn,
            created_at=self.created_at,
            dns_entry=self.dns_entry,
            id=self.id,
            service_arn=self.service_arn,
            service_id=self.service_id,
            service_name=self.service_name,
            service_network_arn=self.service_network_arn,
            service_network_id=self.service_network_id,
            service_network_name=self.service_network_name,
            status=self.status,
            tags=self.tags)


def get_service_network_service_association(arn: Optional[str] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceNetworkServiceAssociationResult:
    """
    Associates a service with a service network.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:vpclattice:getServiceNetworkServiceAssociation', __args__, opts=opts, typ=GetServiceNetworkServiceAssociationResult).value

    return AwaitableGetServiceNetworkServiceAssociationResult(
        arn=pulumi.get(__ret__, 'arn'),
        created_at=pulumi.get(__ret__, 'created_at'),
        dns_entry=pulumi.get(__ret__, 'dns_entry'),
        id=pulumi.get(__ret__, 'id'),
        service_arn=pulumi.get(__ret__, 'service_arn'),
        service_id=pulumi.get(__ret__, 'service_id'),
        service_name=pulumi.get(__ret__, 'service_name'),
        service_network_arn=pulumi.get(__ret__, 'service_network_arn'),
        service_network_id=pulumi.get(__ret__, 'service_network_id'),
        service_network_name=pulumi.get(__ret__, 'service_network_name'),
        status=pulumi.get(__ret__, 'status'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_service_network_service_association)
def get_service_network_service_association_output(arn: Optional[pulumi.Input[str]] = None,
                                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServiceNetworkServiceAssociationResult]:
    """
    Associates a service with a service network.
    """
    ...
