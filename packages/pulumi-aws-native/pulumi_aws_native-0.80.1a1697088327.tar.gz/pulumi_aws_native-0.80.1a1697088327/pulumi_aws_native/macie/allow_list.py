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

__all__ = ['AllowListArgs', 'AllowList']

@pulumi.input_type
class AllowListArgs:
    def __init__(__self__, *,
                 criteria: pulumi.Input['AllowListCriteriaArgs'],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['AllowListTagArgs']]]] = None):
        """
        The set of arguments for constructing a AllowList resource.
        :param pulumi.Input['AllowListCriteriaArgs'] criteria: AllowList criteria.
        :param pulumi.Input[str] description: Description of AllowList.
        :param pulumi.Input[str] name: Name of AllowList.
        :param pulumi.Input[Sequence[pulumi.Input['AllowListTagArgs']]] tags: A collection of tags associated with a resource
        """
        AllowListArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            criteria=criteria,
            description=description,
            name=name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             criteria: pulumi.Input['AllowListCriteriaArgs'],
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['AllowListTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("criteria", criteria)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter
    def criteria(self) -> pulumi.Input['AllowListCriteriaArgs']:
        """
        AllowList criteria.
        """
        return pulumi.get(self, "criteria")

    @criteria.setter
    def criteria(self, value: pulumi.Input['AllowListCriteriaArgs']):
        pulumi.set(self, "criteria", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of AllowList.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of AllowList.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AllowListTagArgs']]]]:
        """
        A collection of tags associated with a resource
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AllowListTagArgs']]]]):
        pulumi.set(self, "tags", value)


class AllowList(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 criteria: Optional[pulumi.Input[pulumi.InputType['AllowListCriteriaArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AllowListTagArgs']]]]] = None,
                 __props__=None):
        """
        Macie AllowList resource schema

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AllowListCriteriaArgs']] criteria: AllowList criteria.
        :param pulumi.Input[str] description: Description of AllowList.
        :param pulumi.Input[str] name: Name of AllowList.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AllowListTagArgs']]]] tags: A collection of tags associated with a resource
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AllowListArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Macie AllowList resource schema

        :param str resource_name: The name of the resource.
        :param AllowListArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AllowListArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            AllowListArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 criteria: Optional[pulumi.Input[pulumi.InputType['AllowListCriteriaArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AllowListTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AllowListArgs.__new__(AllowListArgs)

            if criteria is not None and not isinstance(criteria, AllowListCriteriaArgs):
                criteria = criteria or {}
                def _setter(key, value):
                    criteria[key] = value
                AllowListCriteriaArgs._configure(_setter, **criteria)
            if criteria is None and not opts.urn:
                raise TypeError("Missing required property 'criteria'")
            __props__.__dict__["criteria"] = criteria
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["status"] = None
        super(AllowList, __self__).__init__(
            'aws-native:macie:AllowList',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AllowList':
        """
        Get an existing AllowList resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AllowListArgs.__new__(AllowListArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["criteria"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        return AllowList(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        AllowList ARN.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def criteria(self) -> pulumi.Output['outputs.AllowListCriteria']:
        """
        AllowList criteria.
        """
        return pulumi.get(self, "criteria")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of AllowList.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of AllowList.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['AllowListStatus']:
        """
        AllowList status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.AllowListTag']]]:
        """
        A collection of tags associated with a resource
        """
        return pulumi.get(self, "tags")

