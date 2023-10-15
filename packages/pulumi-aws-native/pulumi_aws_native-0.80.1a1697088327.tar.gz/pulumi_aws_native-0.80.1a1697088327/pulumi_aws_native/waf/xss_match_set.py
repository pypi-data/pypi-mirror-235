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

__all__ = ['XssMatchSetArgs', 'XssMatchSet']

@pulumi.input_type
class XssMatchSetArgs:
    def __init__(__self__, *,
                 xss_match_tuples: pulumi.Input[Sequence[pulumi.Input['XssMatchSetXssMatchTupleArgs']]],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a XssMatchSet resource.
        """
        XssMatchSetArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            xss_match_tuples=xss_match_tuples,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             xss_match_tuples: pulumi.Input[Sequence[pulumi.Input['XssMatchSetXssMatchTupleArgs']]],
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("xss_match_tuples", xss_match_tuples)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="xssMatchTuples")
    def xss_match_tuples(self) -> pulumi.Input[Sequence[pulumi.Input['XssMatchSetXssMatchTupleArgs']]]:
        return pulumi.get(self, "xss_match_tuples")

    @xss_match_tuples.setter
    def xss_match_tuples(self, value: pulumi.Input[Sequence[pulumi.Input['XssMatchSetXssMatchTupleArgs']]]):
        pulumi.set(self, "xss_match_tuples", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


warnings.warn("""XssMatchSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class XssMatchSet(pulumi.CustomResource):
    warnings.warn("""XssMatchSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 xss_match_tuples: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['XssMatchSetXssMatchTupleArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::WAF::XssMatchSet

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: XssMatchSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::WAF::XssMatchSet

        :param str resource_name: The name of the resource.
        :param XssMatchSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(XssMatchSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            XssMatchSetArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 xss_match_tuples: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['XssMatchSetXssMatchTupleArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""XssMatchSet is deprecated: XssMatchSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = XssMatchSetArgs.__new__(XssMatchSetArgs)

            __props__.__dict__["name"] = name
            if xss_match_tuples is None and not opts.urn:
                raise TypeError("Missing required property 'xss_match_tuples'")
            __props__.__dict__["xss_match_tuples"] = xss_match_tuples
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(XssMatchSet, __self__).__init__(
            'aws-native:waf:XssMatchSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'XssMatchSet':
        """
        Get an existing XssMatchSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = XssMatchSetArgs.__new__(XssMatchSetArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["xss_match_tuples"] = None
        return XssMatchSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="xssMatchTuples")
    def xss_match_tuples(self) -> pulumi.Output[Sequence['outputs.XssMatchSetXssMatchTuple']]:
        return pulumi.get(self, "xss_match_tuples")

