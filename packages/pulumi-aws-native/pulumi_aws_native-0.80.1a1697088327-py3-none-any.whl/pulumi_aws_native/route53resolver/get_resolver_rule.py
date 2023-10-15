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
    'GetResolverRuleResult',
    'AwaitableGetResolverRuleResult',
    'get_resolver_rule',
    'get_resolver_rule_output',
]

@pulumi.output_type
class GetResolverRuleResult:
    def __init__(__self__, arn=None, domain_name=None, name=None, resolver_endpoint_id=None, resolver_rule_id=None, tags=None, target_ips=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if domain_name and not isinstance(domain_name, str):
            raise TypeError("Expected argument 'domain_name' to be a str")
        pulumi.set(__self__, "domain_name", domain_name)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resolver_endpoint_id and not isinstance(resolver_endpoint_id, str):
            raise TypeError("Expected argument 'resolver_endpoint_id' to be a str")
        pulumi.set(__self__, "resolver_endpoint_id", resolver_endpoint_id)
        if resolver_rule_id and not isinstance(resolver_rule_id, str):
            raise TypeError("Expected argument 'resolver_rule_id' to be a str")
        pulumi.set(__self__, "resolver_rule_id", resolver_rule_id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if target_ips and not isinstance(target_ips, list):
            raise TypeError("Expected argument 'target_ips' to be a list")
        pulumi.set(__self__, "target_ips", target_ips)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the resolver rule.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[str]:
        """
        DNS queries for this domain name are forwarded to the IP addresses that are specified in TargetIps
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name for the Resolver rule
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resolverEndpointId")
    def resolver_endpoint_id(self) -> Optional[str]:
        """
        The ID of the endpoint that the rule is associated with.
        """
        return pulumi.get(self, "resolver_endpoint_id")

    @property
    @pulumi.getter(name="resolverRuleId")
    def resolver_rule_id(self) -> Optional[str]:
        """
        The ID of the endpoint that the rule is associated with.
        """
        return pulumi.get(self, "resolver_rule_id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ResolverRuleTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetIps")
    def target_ips(self) -> Optional[Sequence['outputs.ResolverRuleTargetAddress']]:
        """
        An array that contains the IP addresses and ports that an outbound endpoint forwards DNS queries to. Typically, these are the IP addresses of DNS resolvers on your network. Specify IPv4 addresses. IPv6 is not supported.
        """
        return pulumi.get(self, "target_ips")


class AwaitableGetResolverRuleResult(GetResolverRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResolverRuleResult(
            arn=self.arn,
            domain_name=self.domain_name,
            name=self.name,
            resolver_endpoint_id=self.resolver_endpoint_id,
            resolver_rule_id=self.resolver_rule_id,
            tags=self.tags,
            target_ips=self.target_ips)


def get_resolver_rule(resolver_rule_id: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResolverRuleResult:
    """
    Resource Type definition for AWS::Route53Resolver::ResolverRule


    :param str resolver_rule_id: The ID of the endpoint that the rule is associated with.
    """
    __args__ = dict()
    __args__['resolverRuleId'] = resolver_rule_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:route53resolver:getResolverRule', __args__, opts=opts, typ=GetResolverRuleResult).value

    return AwaitableGetResolverRuleResult(
        arn=pulumi.get(__ret__, 'arn'),
        domain_name=pulumi.get(__ret__, 'domain_name'),
        name=pulumi.get(__ret__, 'name'),
        resolver_endpoint_id=pulumi.get(__ret__, 'resolver_endpoint_id'),
        resolver_rule_id=pulumi.get(__ret__, 'resolver_rule_id'),
        tags=pulumi.get(__ret__, 'tags'),
        target_ips=pulumi.get(__ret__, 'target_ips'))


@_utilities.lift_output_func(get_resolver_rule)
def get_resolver_rule_output(resolver_rule_id: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResolverRuleResult]:
    """
    Resource Type definition for AWS::Route53Resolver::ResolverRule


    :param str resolver_rule_id: The ID of the endpoint that the rule is associated with.
    """
    ...
