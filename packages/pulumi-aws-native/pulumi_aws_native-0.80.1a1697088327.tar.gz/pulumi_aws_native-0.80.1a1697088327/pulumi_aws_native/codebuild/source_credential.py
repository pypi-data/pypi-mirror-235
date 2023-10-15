# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SourceCredentialArgs', 'SourceCredential']

@pulumi.input_type
class SourceCredentialArgs:
    def __init__(__self__, *,
                 auth_type: pulumi.Input[str],
                 server_type: pulumi.Input[str],
                 token: pulumi.Input[str],
                 username: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SourceCredential resource.
        """
        SourceCredentialArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            auth_type=auth_type,
            server_type=server_type,
            token=token,
            username=username,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             auth_type: pulumi.Input[str],
             server_type: pulumi.Input[str],
             token: pulumi.Input[str],
             username: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("auth_type", auth_type)
        _setter("server_type", server_type)
        _setter("token", token)
        if username is not None:
            _setter("username", username)

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "auth_type")

    @auth_type.setter
    def auth_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "auth_type", value)

    @property
    @pulumi.getter(name="serverType")
    def server_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "server_type")

    @server_type.setter
    def server_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_type", value)

    @property
    @pulumi.getter
    def token(self) -> pulumi.Input[str]:
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: pulumi.Input[str]):
        pulumi.set(self, "token", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


warnings.warn("""SourceCredential is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class SourceCredential(pulumi.CustomResource):
    warnings.warn("""SourceCredential is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_type: Optional[pulumi.Input[str]] = None,
                 server_type: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::CodeBuild::SourceCredential

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SourceCredentialArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::CodeBuild::SourceCredential

        :param str resource_name: The name of the resource.
        :param SourceCredentialArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SourceCredentialArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            SourceCredentialArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_type: Optional[pulumi.Input[str]] = None,
                 server_type: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""SourceCredential is deprecated: SourceCredential is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SourceCredentialArgs.__new__(SourceCredentialArgs)

            if auth_type is None and not opts.urn:
                raise TypeError("Missing required property 'auth_type'")
            __props__.__dict__["auth_type"] = auth_type
            if server_type is None and not opts.urn:
                raise TypeError("Missing required property 'server_type'")
            __props__.__dict__["server_type"] = server_type
            if token is None and not opts.urn:
                raise TypeError("Missing required property 'token'")
            __props__.__dict__["token"] = token
            __props__.__dict__["username"] = username
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["server_type"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(SourceCredential, __self__).__init__(
            'aws-native:codebuild:SourceCredential',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SourceCredential':
        """
        Get an existing SourceCredential resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SourceCredentialArgs.__new__(SourceCredentialArgs)

        __props__.__dict__["auth_type"] = None
        __props__.__dict__["server_type"] = None
        __props__.__dict__["token"] = None
        __props__.__dict__["username"] = None
        return SourceCredential(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "auth_type")

    @property
    @pulumi.getter(name="serverType")
    def server_type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "server_type")

    @property
    @pulumi.getter
    def token(self) -> pulumi.Output[str]:
        return pulumi.get(self, "token")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "username")

