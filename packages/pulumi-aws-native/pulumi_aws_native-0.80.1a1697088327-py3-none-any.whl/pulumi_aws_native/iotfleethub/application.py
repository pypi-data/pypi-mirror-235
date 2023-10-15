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

__all__ = ['ApplicationArgs', 'Application']

@pulumi.input_type
class ApplicationArgs:
    def __init__(__self__, *,
                 role_arn: pulumi.Input[str],
                 application_description: Optional[pulumi.Input[str]] = None,
                 application_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationTagArgs']]]] = None):
        """
        The set of arguments for constructing a Application resource.
        :param pulumi.Input[str] role_arn: The ARN of the role that the web application assumes when it interacts with AWS IoT Core. For more info on configuring this attribute, see https://docs.aws.amazon.com/iot/latest/apireference/API_iotfleethub_CreateApplication.html#API_iotfleethub_CreateApplication_RequestSyntax
        :param pulumi.Input[str] application_description: Application Description, should be between 1 and 2048 characters.
        :param pulumi.Input[str] application_name: Application Name, should be between 1 and 256 characters.
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationTagArgs']]] tags: A list of key-value pairs that contain metadata for the application.
        """
        ApplicationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            role_arn=role_arn,
            application_description=application_description,
            application_name=application_name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             role_arn: pulumi.Input[str],
             application_description: Optional[pulumi.Input[str]] = None,
             application_name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("role_arn", role_arn)
        if application_description is not None:
            _setter("application_description", application_description)
        if application_name is not None:
            _setter("application_name", application_name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the role that the web application assumes when it interacts with AWS IoT Core. For more info on configuring this attribute, see https://docs.aws.amazon.com/iot/latest/apireference/API_iotfleethub_CreateApplication.html#API_iotfleethub_CreateApplication_RequestSyntax
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="applicationDescription")
    def application_description(self) -> Optional[pulumi.Input[str]]:
        """
        Application Description, should be between 1 and 2048 characters.
        """
        return pulumi.get(self, "application_description")

    @application_description.setter
    def application_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_description", value)

    @property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> Optional[pulumi.Input[str]]:
        """
        Application Name, should be between 1 and 256 characters.
        """
        return pulumi.get(self, "application_name")

    @application_name.setter
    def application_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationTagArgs']]]]:
        """
        A list of key-value pairs that contain metadata for the application.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Application(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_description: Optional[pulumi.Input[str]] = None,
                 application_name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::IoTFleetHub::Application

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_description: Application Description, should be between 1 and 2048 characters.
        :param pulumi.Input[str] application_name: Application Name, should be between 1 and 256 characters.
        :param pulumi.Input[str] role_arn: The ARN of the role that the web application assumes when it interacts with AWS IoT Core. For more info on configuring this attribute, see https://docs.aws.amazon.com/iot/latest/apireference/API_iotfleethub_CreateApplication.html#API_iotfleethub_CreateApplication_RequestSyntax
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationTagArgs']]]] tags: A list of key-value pairs that contain metadata for the application.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApplicationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::IoTFleetHub::Application

        :param str resource_name: The name of the resource.
        :param ApplicationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplicationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ApplicationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_description: Optional[pulumi.Input[str]] = None,
                 application_name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApplicationArgs.__new__(ApplicationArgs)

            __props__.__dict__["application_description"] = application_description
            __props__.__dict__["application_name"] = application_name
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
            __props__.__dict__["tags"] = tags
            __props__.__dict__["application_arn"] = None
            __props__.__dict__["application_creation_date"] = None
            __props__.__dict__["application_id"] = None
            __props__.__dict__["application_last_update_date"] = None
            __props__.__dict__["application_state"] = None
            __props__.__dict__["application_url"] = None
            __props__.__dict__["error_message"] = None
            __props__.__dict__["sso_client_id"] = None
        super(Application, __self__).__init__(
            'aws-native:iotfleethub:Application',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Application':
        """
        Get an existing Application resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApplicationArgs.__new__(ApplicationArgs)

        __props__.__dict__["application_arn"] = None
        __props__.__dict__["application_creation_date"] = None
        __props__.__dict__["application_description"] = None
        __props__.__dict__["application_id"] = None
        __props__.__dict__["application_last_update_date"] = None
        __props__.__dict__["application_name"] = None
        __props__.__dict__["application_state"] = None
        __props__.__dict__["application_url"] = None
        __props__.__dict__["error_message"] = None
        __props__.__dict__["role_arn"] = None
        __props__.__dict__["sso_client_id"] = None
        __props__.__dict__["tags"] = None
        return Application(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationArn")
    def application_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the application.
        """
        return pulumi.get(self, "application_arn")

    @property
    @pulumi.getter(name="applicationCreationDate")
    def application_creation_date(self) -> pulumi.Output[int]:
        """
        When the Application was created
        """
        return pulumi.get(self, "application_creation_date")

    @property
    @pulumi.getter(name="applicationDescription")
    def application_description(self) -> pulumi.Output[Optional[str]]:
        """
        Application Description, should be between 1 and 2048 characters.
        """
        return pulumi.get(self, "application_description")

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[str]:
        """
        The ID of the application.
        """
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter(name="applicationLastUpdateDate")
    def application_last_update_date(self) -> pulumi.Output[int]:
        """
        When the Application was last updated
        """
        return pulumi.get(self, "application_last_update_date")

    @property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> pulumi.Output[str]:
        """
        Application Name, should be between 1 and 256 characters.
        """
        return pulumi.get(self, "application_name")

    @property
    @pulumi.getter(name="applicationState")
    def application_state(self) -> pulumi.Output[str]:
        """
        The current state of the application.
        """
        return pulumi.get(self, "application_state")

    @property
    @pulumi.getter(name="applicationUrl")
    def application_url(self) -> pulumi.Output[str]:
        """
        The URL of the application.
        """
        return pulumi.get(self, "application_url")

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> pulumi.Output[str]:
        """
        A message indicating why Create or Delete Application failed.
        """
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the role that the web application assumes when it interacts with AWS IoT Core. For more info on configuring this attribute, see https://docs.aws.amazon.com/iot/latest/apireference/API_iotfleethub_CreateApplication.html#API_iotfleethub_CreateApplication_RequestSyntax
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="ssoClientId")
    def sso_client_id(self) -> pulumi.Output[str]:
        """
        The AWS SSO application generated client ID (used with AWS SSO APIs).
        """
        return pulumi.get(self, "sso_client_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationTag']]]:
        """
        A list of key-value pairs that contain metadata for the application.
        """
        return pulumi.get(self, "tags")

