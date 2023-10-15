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

__all__ = ['ViewArgs', 'View']

@pulumi.input_type
class ViewArgs:
    def __init__(__self__, *,
                 filters: Optional[pulumi.Input['ViewFiltersArgs']] = None,
                 included_properties: Optional[pulumi.Input[Sequence[pulumi.Input['ViewIncludedPropertyArgs']]]] = None,
                 tags: Optional[pulumi.Input['ViewTagMapArgs']] = None,
                 view_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a View resource.
        """
        ViewArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            filters=filters,
            included_properties=included_properties,
            tags=tags,
            view_name=view_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             filters: Optional[pulumi.Input['ViewFiltersArgs']] = None,
             included_properties: Optional[pulumi.Input[Sequence[pulumi.Input['ViewIncludedPropertyArgs']]]] = None,
             tags: Optional[pulumi.Input['ViewTagMapArgs']] = None,
             view_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if filters is not None:
            _setter("filters", filters)
        if included_properties is not None:
            _setter("included_properties", included_properties)
        if tags is not None:
            _setter("tags", tags)
        if view_name is not None:
            _setter("view_name", view_name)

    @property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input['ViewFiltersArgs']]:
        return pulumi.get(self, "filters")

    @filters.setter
    def filters(self, value: Optional[pulumi.Input['ViewFiltersArgs']]):
        pulumi.set(self, "filters", value)

    @property
    @pulumi.getter(name="includedProperties")
    def included_properties(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ViewIncludedPropertyArgs']]]]:
        return pulumi.get(self, "included_properties")

    @included_properties.setter
    def included_properties(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ViewIncludedPropertyArgs']]]]):
        pulumi.set(self, "included_properties", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input['ViewTagMapArgs']]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input['ViewTagMapArgs']]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="viewName")
    def view_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "view_name")

    @view_name.setter
    def view_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "view_name", value)


class View(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 filters: Optional[pulumi.Input[pulumi.InputType['ViewFiltersArgs']]] = None,
                 included_properties: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ViewIncludedPropertyArgs']]]]] = None,
                 tags: Optional[pulumi.Input[pulumi.InputType['ViewTagMapArgs']]] = None,
                 view_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Definition of AWS::ResourceExplorer2::View Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ViewArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::ResourceExplorer2::View Resource Type

        :param str resource_name: The name of the resource.
        :param ViewArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ViewArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ViewArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 filters: Optional[pulumi.Input[pulumi.InputType['ViewFiltersArgs']]] = None,
                 included_properties: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ViewIncludedPropertyArgs']]]]] = None,
                 tags: Optional[pulumi.Input[pulumi.InputType['ViewTagMapArgs']]] = None,
                 view_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ViewArgs.__new__(ViewArgs)

            if filters is not None and not isinstance(filters, ViewFiltersArgs):
                filters = filters or {}
                def _setter(key, value):
                    filters[key] = value
                ViewFiltersArgs._configure(_setter, **filters)
            __props__.__dict__["filters"] = filters
            __props__.__dict__["included_properties"] = included_properties
            if tags is not None and not isinstance(tags, ViewTagMapArgs):
                tags = tags or {}
                def _setter(key, value):
                    tags[key] = value
                ViewTagMapArgs._configure(_setter, **tags)
            __props__.__dict__["tags"] = tags
            __props__.__dict__["view_name"] = view_name
            __props__.__dict__["view_arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["view_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(View, __self__).__init__(
            'aws-native:resourceexplorer2:View',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'View':
        """
        Get an existing View resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ViewArgs.__new__(ViewArgs)

        __props__.__dict__["filters"] = None
        __props__.__dict__["included_properties"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["view_arn"] = None
        __props__.__dict__["view_name"] = None
        return View(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def filters(self) -> pulumi.Output[Optional['outputs.ViewFilters']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter(name="includedProperties")
    def included_properties(self) -> pulumi.Output[Optional[Sequence['outputs.ViewIncludedProperty']]]:
        return pulumi.get(self, "included_properties")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional['outputs.ViewTagMap']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="viewArn")
    def view_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "view_arn")

    @property
    @pulumi.getter(name="viewName")
    def view_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "view_name")

