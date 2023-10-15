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

__all__ = [
    'GetPrefixListResult',
    'AwaitableGetPrefixListResult',
    'get_prefix_list',
    'get_prefix_list_output',
]

@pulumi.output_type
class GetPrefixListResult:
    def __init__(__self__, address_family=None, arn=None, entries=None, max_entries=None, owner_id=None, prefix_list_id=None, prefix_list_name=None, tags=None, version=None):
        if address_family and not isinstance(address_family, str):
            raise TypeError("Expected argument 'address_family' to be a str")
        pulumi.set(__self__, "address_family", address_family)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if entries and not isinstance(entries, list):
            raise TypeError("Expected argument 'entries' to be a list")
        pulumi.set(__self__, "entries", entries)
        if max_entries and not isinstance(max_entries, int):
            raise TypeError("Expected argument 'max_entries' to be a int")
        pulumi.set(__self__, "max_entries", max_entries)
        if owner_id and not isinstance(owner_id, str):
            raise TypeError("Expected argument 'owner_id' to be a str")
        pulumi.set(__self__, "owner_id", owner_id)
        if prefix_list_id and not isinstance(prefix_list_id, str):
            raise TypeError("Expected argument 'prefix_list_id' to be a str")
        pulumi.set(__self__, "prefix_list_id", prefix_list_id)
        if prefix_list_name and not isinstance(prefix_list_name, str):
            raise TypeError("Expected argument 'prefix_list_name' to be a str")
        pulumi.set(__self__, "prefix_list_name", prefix_list_name)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if version and not isinstance(version, int):
            raise TypeError("Expected argument 'version' to be a int")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> Optional['PrefixListAddressFamily']:
        """
        Ip Version of Prefix List.
        """
        return pulumi.get(self, "address_family")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the Prefix List.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def entries(self) -> Optional[Sequence['outputs.PrefixListEntry']]:
        """
        Entries of Prefix List.
        """
        return pulumi.get(self, "entries")

    @property
    @pulumi.getter(name="maxEntries")
    def max_entries(self) -> Optional[int]:
        """
        Max Entries of Prefix List.
        """
        return pulumi.get(self, "max_entries")

    @property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[str]:
        """
        Owner Id of Prefix List.
        """
        return pulumi.get(self, "owner_id")

    @property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> Optional[str]:
        """
        Id of Prefix List.
        """
        return pulumi.get(self, "prefix_list_id")

    @property
    @pulumi.getter(name="prefixListName")
    def prefix_list_name(self) -> Optional[str]:
        """
        Name of Prefix List.
        """
        return pulumi.get(self, "prefix_list_name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.PrefixListTag']]:
        """
        Tags for Prefix List
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def version(self) -> Optional[int]:
        """
        Version of Prefix List.
        """
        return pulumi.get(self, "version")


class AwaitableGetPrefixListResult(GetPrefixListResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrefixListResult(
            address_family=self.address_family,
            arn=self.arn,
            entries=self.entries,
            max_entries=self.max_entries,
            owner_id=self.owner_id,
            prefix_list_id=self.prefix_list_id,
            prefix_list_name=self.prefix_list_name,
            tags=self.tags,
            version=self.version)


def get_prefix_list(prefix_list_id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrefixListResult:
    """
    Resource schema of AWS::EC2::PrefixList Type


    :param str prefix_list_id: Id of Prefix List.
    """
    __args__ = dict()
    __args__['prefixListId'] = prefix_list_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getPrefixList', __args__, opts=opts, typ=GetPrefixListResult).value

    return AwaitableGetPrefixListResult(
        address_family=pulumi.get(__ret__, 'address_family'),
        arn=pulumi.get(__ret__, 'arn'),
        entries=pulumi.get(__ret__, 'entries'),
        max_entries=pulumi.get(__ret__, 'max_entries'),
        owner_id=pulumi.get(__ret__, 'owner_id'),
        prefix_list_id=pulumi.get(__ret__, 'prefix_list_id'),
        prefix_list_name=pulumi.get(__ret__, 'prefix_list_name'),
        tags=pulumi.get(__ret__, 'tags'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_prefix_list)
def get_prefix_list_output(prefix_list_id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPrefixListResult]:
    """
    Resource schema of AWS::EC2::PrefixList Type


    :param str prefix_list_id: Id of Prefix List.
    """
    ...
