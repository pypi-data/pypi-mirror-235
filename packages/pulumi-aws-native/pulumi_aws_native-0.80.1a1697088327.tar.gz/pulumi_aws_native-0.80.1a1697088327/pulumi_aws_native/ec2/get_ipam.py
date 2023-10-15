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
    'GetIpamResult',
    'AwaitableGetIpamResult',
    'get_ipam',
    'get_ipam_output',
]

@pulumi.output_type
class GetIpamResult:
    def __init__(__self__, arn=None, default_resource_discovery_association_id=None, default_resource_discovery_id=None, description=None, ipam_id=None, operating_regions=None, private_default_scope_id=None, public_default_scope_id=None, resource_discovery_association_count=None, scope_count=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if default_resource_discovery_association_id and not isinstance(default_resource_discovery_association_id, str):
            raise TypeError("Expected argument 'default_resource_discovery_association_id' to be a str")
        pulumi.set(__self__, "default_resource_discovery_association_id", default_resource_discovery_association_id)
        if default_resource_discovery_id and not isinstance(default_resource_discovery_id, str):
            raise TypeError("Expected argument 'default_resource_discovery_id' to be a str")
        pulumi.set(__self__, "default_resource_discovery_id", default_resource_discovery_id)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if ipam_id and not isinstance(ipam_id, str):
            raise TypeError("Expected argument 'ipam_id' to be a str")
        pulumi.set(__self__, "ipam_id", ipam_id)
        if operating_regions and not isinstance(operating_regions, list):
            raise TypeError("Expected argument 'operating_regions' to be a list")
        pulumi.set(__self__, "operating_regions", operating_regions)
        if private_default_scope_id and not isinstance(private_default_scope_id, str):
            raise TypeError("Expected argument 'private_default_scope_id' to be a str")
        pulumi.set(__self__, "private_default_scope_id", private_default_scope_id)
        if public_default_scope_id and not isinstance(public_default_scope_id, str):
            raise TypeError("Expected argument 'public_default_scope_id' to be a str")
        pulumi.set(__self__, "public_default_scope_id", public_default_scope_id)
        if resource_discovery_association_count and not isinstance(resource_discovery_association_count, int):
            raise TypeError("Expected argument 'resource_discovery_association_count' to be a int")
        pulumi.set(__self__, "resource_discovery_association_count", resource_discovery_association_count)
        if scope_count and not isinstance(scope_count, int):
            raise TypeError("Expected argument 'scope_count' to be a int")
        pulumi.set(__self__, "scope_count", scope_count)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the IPAM.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="defaultResourceDiscoveryAssociationId")
    def default_resource_discovery_association_id(self) -> Optional[str]:
        """
        The Id of the default association to the default resource discovery, created with this IPAM.
        """
        return pulumi.get(self, "default_resource_discovery_association_id")

    @property
    @pulumi.getter(name="defaultResourceDiscoveryId")
    def default_resource_discovery_id(self) -> Optional[str]:
        """
        The Id of the default resource discovery, created with this IPAM.
        """
        return pulumi.get(self, "default_resource_discovery_id")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="ipamId")
    def ipam_id(self) -> Optional[str]:
        """
        Id of the IPAM.
        """
        return pulumi.get(self, "ipam_id")

    @property
    @pulumi.getter(name="operatingRegions")
    def operating_regions(self) -> Optional[Sequence['outputs.IpamOperatingRegion']]:
        """
        The regions IPAM is enabled for. Allows pools to be created in these regions, as well as enabling monitoring
        """
        return pulumi.get(self, "operating_regions")

    @property
    @pulumi.getter(name="privateDefaultScopeId")
    def private_default_scope_id(self) -> Optional[str]:
        """
        The Id of the default scope for publicly routable IP space, created with this IPAM.
        """
        return pulumi.get(self, "private_default_scope_id")

    @property
    @pulumi.getter(name="publicDefaultScopeId")
    def public_default_scope_id(self) -> Optional[str]:
        """
        The Id of the default scope for publicly routable IP space, created with this IPAM.
        """
        return pulumi.get(self, "public_default_scope_id")

    @property
    @pulumi.getter(name="resourceDiscoveryAssociationCount")
    def resource_discovery_association_count(self) -> Optional[int]:
        """
        The count of resource discoveries associated with this IPAM.
        """
        return pulumi.get(self, "resource_discovery_association_count")

    @property
    @pulumi.getter(name="scopeCount")
    def scope_count(self) -> Optional[int]:
        """
        The number of scopes that currently exist in this IPAM.
        """
        return pulumi.get(self, "scope_count")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.IpamTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetIpamResult(GetIpamResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIpamResult(
            arn=self.arn,
            default_resource_discovery_association_id=self.default_resource_discovery_association_id,
            default_resource_discovery_id=self.default_resource_discovery_id,
            description=self.description,
            ipam_id=self.ipam_id,
            operating_regions=self.operating_regions,
            private_default_scope_id=self.private_default_scope_id,
            public_default_scope_id=self.public_default_scope_id,
            resource_discovery_association_count=self.resource_discovery_association_count,
            scope_count=self.scope_count,
            tags=self.tags)


def get_ipam(ipam_id: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIpamResult:
    """
    Resource Schema of AWS::EC2::IPAM Type


    :param str ipam_id: Id of the IPAM.
    """
    __args__ = dict()
    __args__['ipamId'] = ipam_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getIpam', __args__, opts=opts, typ=GetIpamResult).value

    return AwaitableGetIpamResult(
        arn=pulumi.get(__ret__, 'arn'),
        default_resource_discovery_association_id=pulumi.get(__ret__, 'default_resource_discovery_association_id'),
        default_resource_discovery_id=pulumi.get(__ret__, 'default_resource_discovery_id'),
        description=pulumi.get(__ret__, 'description'),
        ipam_id=pulumi.get(__ret__, 'ipam_id'),
        operating_regions=pulumi.get(__ret__, 'operating_regions'),
        private_default_scope_id=pulumi.get(__ret__, 'private_default_scope_id'),
        public_default_scope_id=pulumi.get(__ret__, 'public_default_scope_id'),
        resource_discovery_association_count=pulumi.get(__ret__, 'resource_discovery_association_count'),
        scope_count=pulumi.get(__ret__, 'scope_count'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_ipam)
def get_ipam_output(ipam_id: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIpamResult]:
    """
    Resource Schema of AWS::EC2::IPAM Type


    :param str ipam_id: Id of the IPAM.
    """
    ...
