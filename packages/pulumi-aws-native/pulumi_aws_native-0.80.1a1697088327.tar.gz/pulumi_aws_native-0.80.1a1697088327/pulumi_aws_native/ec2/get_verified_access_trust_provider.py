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
    'GetVerifiedAccessTrustProviderResult',
    'AwaitableGetVerifiedAccessTrustProviderResult',
    'get_verified_access_trust_provider',
    'get_verified_access_trust_provider_output',
]

@pulumi.output_type
class GetVerifiedAccessTrustProviderResult:
    def __init__(__self__, creation_time=None, description=None, last_updated_time=None, oidc_options=None, tags=None, verified_access_trust_provider_id=None):
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if last_updated_time and not isinstance(last_updated_time, str):
            raise TypeError("Expected argument 'last_updated_time' to be a str")
        pulumi.set(__self__, "last_updated_time", last_updated_time)
        if oidc_options and not isinstance(oidc_options, dict):
            raise TypeError("Expected argument 'oidc_options' to be a dict")
        pulumi.set(__self__, "oidc_options", oidc_options)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if verified_access_trust_provider_id and not isinstance(verified_access_trust_provider_id, str):
            raise TypeError("Expected argument 'verified_access_trust_provider_id' to be a str")
        pulumi.set(__self__, "verified_access_trust_provider_id", verified_access_trust_provider_id)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[str]:
        """
        The creation time.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description for the Amazon Web Services Verified Access trust provider.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[str]:
        """
        The last updated time.
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter(name="oidcOptions")
    def oidc_options(self) -> Optional['outputs.VerifiedAccessTrustProviderOidcOptions']:
        return pulumi.get(self, "oidc_options")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.VerifiedAccessTrustProviderTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="verifiedAccessTrustProviderId")
    def verified_access_trust_provider_id(self) -> Optional[str]:
        """
        The ID of the Amazon Web Services Verified Access trust provider.
        """
        return pulumi.get(self, "verified_access_trust_provider_id")


class AwaitableGetVerifiedAccessTrustProviderResult(GetVerifiedAccessTrustProviderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVerifiedAccessTrustProviderResult(
            creation_time=self.creation_time,
            description=self.description,
            last_updated_time=self.last_updated_time,
            oidc_options=self.oidc_options,
            tags=self.tags,
            verified_access_trust_provider_id=self.verified_access_trust_provider_id)


def get_verified_access_trust_provider(verified_access_trust_provider_id: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVerifiedAccessTrustProviderResult:
    """
    The AWS::EC2::VerifiedAccessTrustProvider type describes a verified access trust provider


    :param str verified_access_trust_provider_id: The ID of the Amazon Web Services Verified Access trust provider.
    """
    __args__ = dict()
    __args__['verifiedAccessTrustProviderId'] = verified_access_trust_provider_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getVerifiedAccessTrustProvider', __args__, opts=opts, typ=GetVerifiedAccessTrustProviderResult).value

    return AwaitableGetVerifiedAccessTrustProviderResult(
        creation_time=pulumi.get(__ret__, 'creation_time'),
        description=pulumi.get(__ret__, 'description'),
        last_updated_time=pulumi.get(__ret__, 'last_updated_time'),
        oidc_options=pulumi.get(__ret__, 'oidc_options'),
        tags=pulumi.get(__ret__, 'tags'),
        verified_access_trust_provider_id=pulumi.get(__ret__, 'verified_access_trust_provider_id'))


@_utilities.lift_output_func(get_verified_access_trust_provider)
def get_verified_access_trust_provider_output(verified_access_trust_provider_id: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVerifiedAccessTrustProviderResult]:
    """
    The AWS::EC2::VerifiedAccessTrustProvider type describes a verified access trust provider


    :param str verified_access_trust_provider_id: The ID of the Amazon Web Services Verified Access trust provider.
    """
    ...
