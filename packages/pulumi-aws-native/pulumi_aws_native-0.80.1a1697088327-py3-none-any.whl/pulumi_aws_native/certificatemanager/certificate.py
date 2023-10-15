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
from ._inputs import *

__all__ = ['CertificateArgs', 'Certificate']

@pulumi.input_type
class CertificateArgs:
    def __init__(__self__, *,
                 domain_name: pulumi.Input[str],
                 certificate_authority_arn: Optional[pulumi.Input[str]] = None,
                 certificate_transparency_logging_preference: Optional[pulumi.Input[str]] = None,
                 domain_validation_options: Optional[pulumi.Input[Sequence[pulumi.Input['CertificateDomainValidationOptionArgs']]]] = None,
                 key_algorithm: Optional[pulumi.Input[str]] = None,
                 subject_alternative_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['CertificateTagArgs']]]] = None,
                 validation_method: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Certificate resource.
        """
        CertificateArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            domain_name=domain_name,
            certificate_authority_arn=certificate_authority_arn,
            certificate_transparency_logging_preference=certificate_transparency_logging_preference,
            domain_validation_options=domain_validation_options,
            key_algorithm=key_algorithm,
            subject_alternative_names=subject_alternative_names,
            tags=tags,
            validation_method=validation_method,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             domain_name: pulumi.Input[str],
             certificate_authority_arn: Optional[pulumi.Input[str]] = None,
             certificate_transparency_logging_preference: Optional[pulumi.Input[str]] = None,
             domain_validation_options: Optional[pulumi.Input[Sequence[pulumi.Input['CertificateDomainValidationOptionArgs']]]] = None,
             key_algorithm: Optional[pulumi.Input[str]] = None,
             subject_alternative_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['CertificateTagArgs']]]] = None,
             validation_method: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("domain_name", domain_name)
        if certificate_authority_arn is not None:
            _setter("certificate_authority_arn", certificate_authority_arn)
        if certificate_transparency_logging_preference is not None:
            _setter("certificate_transparency_logging_preference", certificate_transparency_logging_preference)
        if domain_validation_options is not None:
            _setter("domain_validation_options", domain_validation_options)
        if key_algorithm is not None:
            _setter("key_algorithm", key_algorithm)
        if subject_alternative_names is not None:
            _setter("subject_alternative_names", subject_alternative_names)
        if tags is not None:
            _setter("tags", tags)
        if validation_method is not None:
            _setter("validation_method", validation_method)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "certificate_authority_arn")

    @certificate_authority_arn.setter
    def certificate_authority_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_authority_arn", value)

    @property
    @pulumi.getter(name="certificateTransparencyLoggingPreference")
    def certificate_transparency_logging_preference(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "certificate_transparency_logging_preference")

    @certificate_transparency_logging_preference.setter
    def certificate_transparency_logging_preference(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_transparency_logging_preference", value)

    @property
    @pulumi.getter(name="domainValidationOptions")
    def domain_validation_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CertificateDomainValidationOptionArgs']]]]:
        return pulumi.get(self, "domain_validation_options")

    @domain_validation_options.setter
    def domain_validation_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CertificateDomainValidationOptionArgs']]]]):
        pulumi.set(self, "domain_validation_options", value)

    @property
    @pulumi.getter(name="keyAlgorithm")
    def key_algorithm(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "key_algorithm")

    @key_algorithm.setter
    def key_algorithm(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_algorithm", value)

    @property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "subject_alternative_names")

    @subject_alternative_names.setter
    def subject_alternative_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subject_alternative_names", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CertificateTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CertificateTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="validationMethod")
    def validation_method(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "validation_method")

    @validation_method.setter
    def validation_method(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "validation_method", value)


warnings.warn("""Certificate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Certificate(pulumi.CustomResource):
    warnings.warn("""Certificate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_authority_arn: Optional[pulumi.Input[str]] = None,
                 certificate_transparency_logging_preference: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 domain_validation_options: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CertificateDomainValidationOptionArgs']]]]] = None,
                 key_algorithm: Optional[pulumi.Input[str]] = None,
                 subject_alternative_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CertificateTagArgs']]]]] = None,
                 validation_method: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::CertificateManager::Certificate

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::CertificateManager::Certificate

        :param str resource_name: The name of the resource.
        :param CertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            CertificateArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_authority_arn: Optional[pulumi.Input[str]] = None,
                 certificate_transparency_logging_preference: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 domain_validation_options: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CertificateDomainValidationOptionArgs']]]]] = None,
                 key_algorithm: Optional[pulumi.Input[str]] = None,
                 subject_alternative_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CertificateTagArgs']]]]] = None,
                 validation_method: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""Certificate is deprecated: Certificate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CertificateArgs.__new__(CertificateArgs)

            __props__.__dict__["certificate_authority_arn"] = certificate_authority_arn
            __props__.__dict__["certificate_transparency_logging_preference"] = certificate_transparency_logging_preference
            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            __props__.__dict__["domain_validation_options"] = domain_validation_options
            __props__.__dict__["key_algorithm"] = key_algorithm
            __props__.__dict__["subject_alternative_names"] = subject_alternative_names
            __props__.__dict__["tags"] = tags
            __props__.__dict__["validation_method"] = validation_method
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["certificate_authority_arn", "domain_name", "domain_validation_options[*]", "key_algorithm", "subject_alternative_names[*]", "validation_method"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Certificate, __self__).__init__(
            'aws-native:certificatemanager:Certificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Certificate':
        """
        Get an existing Certificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CertificateArgs.__new__(CertificateArgs)

        __props__.__dict__["certificate_authority_arn"] = None
        __props__.__dict__["certificate_transparency_logging_preference"] = None
        __props__.__dict__["domain_name"] = None
        __props__.__dict__["domain_validation_options"] = None
        __props__.__dict__["key_algorithm"] = None
        __props__.__dict__["subject_alternative_names"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["validation_method"] = None
        return Certificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "certificate_authority_arn")

    @property
    @pulumi.getter(name="certificateTransparencyLoggingPreference")
    def certificate_transparency_logging_preference(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "certificate_transparency_logging_preference")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="domainValidationOptions")
    def domain_validation_options(self) -> pulumi.Output[Optional[Sequence['outputs.CertificateDomainValidationOption']]]:
        return pulumi.get(self, "domain_validation_options")

    @property
    @pulumi.getter(name="keyAlgorithm")
    def key_algorithm(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "key_algorithm")

    @property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "subject_alternative_names")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.CertificateTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="validationMethod")
    def validation_method(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "validation_method")

