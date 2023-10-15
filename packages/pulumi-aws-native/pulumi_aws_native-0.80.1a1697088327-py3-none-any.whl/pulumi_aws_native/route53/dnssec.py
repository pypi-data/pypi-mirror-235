# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DnssecArgs', 'Dnssec']

@pulumi.input_type
class DnssecArgs:
    def __init__(__self__, *,
                 hosted_zone_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a Dnssec resource.
        :param pulumi.Input[str] hosted_zone_id: The unique string (ID) used to identify a hosted zone.
        """
        DnssecArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            hosted_zone_id=hosted_zone_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             hosted_zone_id: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("hosted_zone_id", hosted_zone_id)

    @property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Input[str]:
        """
        The unique string (ID) used to identify a hosted zone.
        """
        return pulumi.get(self, "hosted_zone_id")

    @hosted_zone_id.setter
    def hosted_zone_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "hosted_zone_id", value)


class Dnssec(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hosted_zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource used to control (enable/disable) DNSSEC in a specific hosted zone.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] hosted_zone_id: The unique string (ID) used to identify a hosted zone.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DnssecArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource used to control (enable/disable) DNSSEC in a specific hosted zone.

        :param str resource_name: The name of the resource.
        :param DnssecArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DnssecArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DnssecArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hosted_zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DnssecArgs.__new__(DnssecArgs)

            if hosted_zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'hosted_zone_id'")
            __props__.__dict__["hosted_zone_id"] = hosted_zone_id
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["hosted_zone_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Dnssec, __self__).__init__(
            'aws-native:route53:Dnssec',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Dnssec':
        """
        Get an existing Dnssec resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DnssecArgs.__new__(DnssecArgs)

        __props__.__dict__["hosted_zone_id"] = None
        return Dnssec(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Output[str]:
        """
        The unique string (ID) used to identify a hosted zone.
        """
        return pulumi.get(self, "hosted_zone_id")

