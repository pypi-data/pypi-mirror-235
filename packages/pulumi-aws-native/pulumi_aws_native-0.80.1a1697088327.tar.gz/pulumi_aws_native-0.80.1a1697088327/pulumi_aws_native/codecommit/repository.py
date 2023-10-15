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

__all__ = ['RepositoryArgs', 'Repository']

@pulumi.input_type
class RepositoryArgs:
    def __init__(__self__, *,
                 code: Optional[pulumi.Input['RepositoryCodeArgs']] = None,
                 repository_description: Optional[pulumi.Input[str]] = None,
                 repository_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['RepositoryTagArgs']]]] = None,
                 triggers: Optional[pulumi.Input[Sequence[pulumi.Input['RepositoryTriggerArgs']]]] = None):
        """
        The set of arguments for constructing a Repository resource.
        """
        RepositoryArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            code=code,
            repository_description=repository_description,
            repository_name=repository_name,
            tags=tags,
            triggers=triggers,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             code: Optional[pulumi.Input['RepositoryCodeArgs']] = None,
             repository_description: Optional[pulumi.Input[str]] = None,
             repository_name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['RepositoryTagArgs']]]] = None,
             triggers: Optional[pulumi.Input[Sequence[pulumi.Input['RepositoryTriggerArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if code is not None:
            _setter("code", code)
        if repository_description is not None:
            _setter("repository_description", repository_description)
        if repository_name is not None:
            _setter("repository_name", repository_name)
        if tags is not None:
            _setter("tags", tags)
        if triggers is not None:
            _setter("triggers", triggers)

    @property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input['RepositoryCodeArgs']]:
        return pulumi.get(self, "code")

    @code.setter
    def code(self, value: Optional[pulumi.Input['RepositoryCodeArgs']]):
        pulumi.set(self, "code", value)

    @property
    @pulumi.getter(name="repositoryDescription")
    def repository_description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "repository_description")

    @repository_description.setter
    def repository_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repository_description", value)

    @property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "repository_name")

    @repository_name.setter
    def repository_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repository_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RepositoryTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RepositoryTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def triggers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RepositoryTriggerArgs']]]]:
        return pulumi.get(self, "triggers")

    @triggers.setter
    def triggers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RepositoryTriggerArgs']]]]):
        pulumi.set(self, "triggers", value)


warnings.warn("""Repository is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Repository(pulumi.CustomResource):
    warnings.warn("""Repository is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 code: Optional[pulumi.Input[pulumi.InputType['RepositoryCodeArgs']]] = None,
                 repository_description: Optional[pulumi.Input[str]] = None,
                 repository_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepositoryTagArgs']]]]] = None,
                 triggers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepositoryTriggerArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::CodeCommit::Repository

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[RepositoryArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::CodeCommit::Repository

        :param str resource_name: The name of the resource.
        :param RepositoryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RepositoryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            RepositoryArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 code: Optional[pulumi.Input[pulumi.InputType['RepositoryCodeArgs']]] = None,
                 repository_description: Optional[pulumi.Input[str]] = None,
                 repository_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepositoryTagArgs']]]]] = None,
                 triggers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepositoryTriggerArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""Repository is deprecated: Repository is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RepositoryArgs.__new__(RepositoryArgs)

            if code is not None and not isinstance(code, RepositoryCodeArgs):
                code = code or {}
                def _setter(key, value):
                    code[key] = value
                RepositoryCodeArgs._configure(_setter, **code)
            __props__.__dict__["code"] = code
            __props__.__dict__["repository_description"] = repository_description
            __props__.__dict__["repository_name"] = repository_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["triggers"] = triggers
            __props__.__dict__["arn"] = None
            __props__.__dict__["clone_url_http"] = None
            __props__.__dict__["clone_url_ssh"] = None
            __props__.__dict__["name"] = None
        super(Repository, __self__).__init__(
            'aws-native:codecommit:Repository',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Repository':
        """
        Get an existing Repository resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RepositoryArgs.__new__(RepositoryArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["clone_url_http"] = None
        __props__.__dict__["clone_url_ssh"] = None
        __props__.__dict__["code"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["repository_description"] = None
        __props__.__dict__["repository_name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["triggers"] = None
        return Repository(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="cloneUrlHttp")
    def clone_url_http(self) -> pulumi.Output[str]:
        return pulumi.get(self, "clone_url_http")

    @property
    @pulumi.getter(name="cloneUrlSsh")
    def clone_url_ssh(self) -> pulumi.Output[str]:
        return pulumi.get(self, "clone_url_ssh")

    @property
    @pulumi.getter
    def code(self) -> pulumi.Output[Optional['outputs.RepositoryCode']]:
        return pulumi.get(self, "code")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="repositoryDescription")
    def repository_description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "repository_description")

    @property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "repository_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.RepositoryTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def triggers(self) -> pulumi.Output[Optional[Sequence['outputs.RepositoryTrigger']]]:
        return pulumi.get(self, "triggers")

