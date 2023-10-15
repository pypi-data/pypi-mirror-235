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
    'GetSamlProviderResult',
    'AwaitableGetSamlProviderResult',
    'get_saml_provider',
    'get_saml_provider_output',
]

@pulumi.output_type
class GetSamlProviderResult:
    def __init__(__self__, arn=None, saml_metadata_document=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if saml_metadata_document and not isinstance(saml_metadata_document, str):
            raise TypeError("Expected argument 'saml_metadata_document' to be a str")
        pulumi.set(__self__, "saml_metadata_document", saml_metadata_document)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        Amazon Resource Name (ARN) of the SAML provider
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="samlMetadataDocument")
    def saml_metadata_document(self) -> Optional[str]:
        return pulumi.get(self, "saml_metadata_document")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.SamlProviderTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetSamlProviderResult(GetSamlProviderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSamlProviderResult(
            arn=self.arn,
            saml_metadata_document=self.saml_metadata_document,
            tags=self.tags)


def get_saml_provider(arn: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSamlProviderResult:
    """
    Resource Type definition for AWS::IAM::SAMLProvider


    :param str arn: Amazon Resource Name (ARN) of the SAML provider
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:iam:getSamlProvider', __args__, opts=opts, typ=GetSamlProviderResult).value

    return AwaitableGetSamlProviderResult(
        arn=pulumi.get(__ret__, 'arn'),
        saml_metadata_document=pulumi.get(__ret__, 'saml_metadata_document'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_saml_provider)
def get_saml_provider_output(arn: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSamlProviderResult]:
    """
    Resource Type definition for AWS::IAM::SAMLProvider


    :param str arn: Amazon Resource Name (ARN) of the SAML provider
    """
    ...
