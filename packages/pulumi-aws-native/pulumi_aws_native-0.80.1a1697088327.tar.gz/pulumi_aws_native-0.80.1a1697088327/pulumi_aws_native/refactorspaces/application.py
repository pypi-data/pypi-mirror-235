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
from ._inputs import *

__all__ = ['ApplicationArgs', 'Application']

@pulumi.input_type
class ApplicationArgs:
    def __init__(__self__, *,
                 environment_identifier: pulumi.Input[str],
                 proxy_type: pulumi.Input['ApplicationProxyType'],
                 vpc_id: pulumi.Input[str],
                 api_gateway_proxy: Optional[pulumi.Input['ApplicationApiGatewayProxyInputArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationTagArgs']]]] = None):
        """
        The set of arguments for constructing a Application resource.
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationTagArgs']]] tags: Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.
        """
        ApplicationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            environment_identifier=environment_identifier,
            proxy_type=proxy_type,
            vpc_id=vpc_id,
            api_gateway_proxy=api_gateway_proxy,
            name=name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             environment_identifier: pulumi.Input[str],
             proxy_type: pulumi.Input['ApplicationProxyType'],
             vpc_id: pulumi.Input[str],
             api_gateway_proxy: Optional[pulumi.Input['ApplicationApiGatewayProxyInputArgs']] = None,
             name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("environment_identifier", environment_identifier)
        _setter("proxy_type", proxy_type)
        _setter("vpc_id", vpc_id)
        if api_gateway_proxy is not None:
            _setter("api_gateway_proxy", api_gateway_proxy)
        if name is not None:
            _setter("name", name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="environmentIdentifier")
    def environment_identifier(self) -> pulumi.Input[str]:
        return pulumi.get(self, "environment_identifier")

    @environment_identifier.setter
    def environment_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "environment_identifier", value)

    @property
    @pulumi.getter(name="proxyType")
    def proxy_type(self) -> pulumi.Input['ApplicationProxyType']:
        return pulumi.get(self, "proxy_type")

    @proxy_type.setter
    def proxy_type(self, value: pulumi.Input['ApplicationProxyType']):
        pulumi.set(self, "proxy_type", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_id", value)

    @property
    @pulumi.getter(name="apiGatewayProxy")
    def api_gateway_proxy(self) -> Optional[pulumi.Input['ApplicationApiGatewayProxyInputArgs']]:
        return pulumi.get(self, "api_gateway_proxy")

    @api_gateway_proxy.setter
    def api_gateway_proxy(self, value: Optional[pulumi.Input['ApplicationApiGatewayProxyInputArgs']]):
        pulumi.set(self, "api_gateway_proxy", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationTagArgs']]]]:
        """
        Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.
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
                 api_gateway_proxy: Optional[pulumi.Input[pulumi.InputType['ApplicationApiGatewayProxyInputArgs']]] = None,
                 environment_identifier: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 proxy_type: Optional[pulumi.Input['ApplicationProxyType']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationTagArgs']]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Definition of AWS::RefactorSpaces::Application Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationTagArgs']]]] tags: Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApplicationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::RefactorSpaces::Application Resource Type

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
                 api_gateway_proxy: Optional[pulumi.Input[pulumi.InputType['ApplicationApiGatewayProxyInputArgs']]] = None,
                 environment_identifier: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 proxy_type: Optional[pulumi.Input['ApplicationProxyType']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationTagArgs']]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApplicationArgs.__new__(ApplicationArgs)

            if api_gateway_proxy is not None and not isinstance(api_gateway_proxy, ApplicationApiGatewayProxyInputArgs):
                api_gateway_proxy = api_gateway_proxy or {}
                def _setter(key, value):
                    api_gateway_proxy[key] = value
                ApplicationApiGatewayProxyInputArgs._configure(_setter, **api_gateway_proxy)
            __props__.__dict__["api_gateway_proxy"] = api_gateway_proxy
            if environment_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'environment_identifier'")
            __props__.__dict__["environment_identifier"] = environment_identifier
            __props__.__dict__["name"] = name
            if proxy_type is None and not opts.urn:
                raise TypeError("Missing required property 'proxy_type'")
            __props__.__dict__["proxy_type"] = proxy_type
            __props__.__dict__["tags"] = tags
            if vpc_id is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_id'")
            __props__.__dict__["vpc_id"] = vpc_id
            __props__.__dict__["api_gateway_id"] = None
            __props__.__dict__["application_identifier"] = None
            __props__.__dict__["arn"] = None
            __props__.__dict__["nlb_arn"] = None
            __props__.__dict__["nlb_name"] = None
            __props__.__dict__["proxy_url"] = None
            __props__.__dict__["stage_name"] = None
            __props__.__dict__["vpc_link_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["api_gateway_proxy", "environment_identifier", "name", "proxy_type", "vpc_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Application, __self__).__init__(
            'aws-native:refactorspaces:Application',
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

        __props__.__dict__["api_gateway_id"] = None
        __props__.__dict__["api_gateway_proxy"] = None
        __props__.__dict__["application_identifier"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["environment_identifier"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["nlb_arn"] = None
        __props__.__dict__["nlb_name"] = None
        __props__.__dict__["proxy_type"] = None
        __props__.__dict__["proxy_url"] = None
        __props__.__dict__["stage_name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["vpc_id"] = None
        __props__.__dict__["vpc_link_id"] = None
        return Application(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiGatewayId")
    def api_gateway_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "api_gateway_id")

    @property
    @pulumi.getter(name="apiGatewayProxy")
    def api_gateway_proxy(self) -> pulumi.Output[Optional['outputs.ApplicationApiGatewayProxyInput']]:
        return pulumi.get(self, "api_gateway_proxy")

    @property
    @pulumi.getter(name="applicationIdentifier")
    def application_identifier(self) -> pulumi.Output[str]:
        return pulumi.get(self, "application_identifier")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="environmentIdentifier")
    def environment_identifier(self) -> pulumi.Output[str]:
        return pulumi.get(self, "environment_identifier")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nlbArn")
    def nlb_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "nlb_arn")

    @property
    @pulumi.getter(name="nlbName")
    def nlb_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "nlb_name")

    @property
    @pulumi.getter(name="proxyType")
    def proxy_type(self) -> pulumi.Output['ApplicationProxyType']:
        return pulumi.get(self, "proxy_type")

    @property
    @pulumi.getter(name="proxyUrl")
    def proxy_url(self) -> pulumi.Output[str]:
        return pulumi.get(self, "proxy_url")

    @property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "stage_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationTag']]]:
        """
        Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter(name="vpcLinkId")
    def vpc_link_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "vpc_link_id")

