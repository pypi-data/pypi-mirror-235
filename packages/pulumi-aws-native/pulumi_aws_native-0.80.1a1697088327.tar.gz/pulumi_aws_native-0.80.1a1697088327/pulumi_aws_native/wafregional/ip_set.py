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

__all__ = ['IpSetArgs', 'IpSet']

@pulumi.input_type
class IpSetArgs:
    def __init__(__self__, *,
                 ip_set_descriptors: Optional[pulumi.Input[Sequence[pulumi.Input['IpSetIpSetDescriptorArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IpSet resource.
        """
        IpSetArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            ip_set_descriptors=ip_set_descriptors,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             ip_set_descriptors: Optional[pulumi.Input[Sequence[pulumi.Input['IpSetIpSetDescriptorArgs']]]] = None,
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if ip_set_descriptors is not None:
            _setter("ip_set_descriptors", ip_set_descriptors)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="ipSetDescriptors")
    def ip_set_descriptors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IpSetIpSetDescriptorArgs']]]]:
        return pulumi.get(self, "ip_set_descriptors")

    @ip_set_descriptors.setter
    def ip_set_descriptors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IpSetIpSetDescriptorArgs']]]]):
        pulumi.set(self, "ip_set_descriptors", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


warnings.warn("""IpSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class IpSet(pulumi.CustomResource):
    warnings.warn("""IpSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ip_set_descriptors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpSetIpSetDescriptorArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::WAFRegional::IPSet

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[IpSetArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::WAFRegional::IPSet

        :param str resource_name: The name of the resource.
        :param IpSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IpSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            IpSetArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ip_set_descriptors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpSetIpSetDescriptorArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""IpSet is deprecated: IpSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IpSetArgs.__new__(IpSetArgs)

            __props__.__dict__["ip_set_descriptors"] = ip_set_descriptors
            __props__.__dict__["name"] = name
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(IpSet, __self__).__init__(
            'aws-native:wafregional:IpSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IpSet':
        """
        Get an existing IpSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IpSetArgs.__new__(IpSetArgs)

        __props__.__dict__["ip_set_descriptors"] = None
        __props__.__dict__["name"] = None
        return IpSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="ipSetDescriptors")
    def ip_set_descriptors(self) -> pulumi.Output[Optional[Sequence['outputs.IpSetIpSetDescriptor']]]:
        return pulumi.get(self, "ip_set_descriptors")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

