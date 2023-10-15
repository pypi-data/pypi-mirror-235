# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetComponentVersionResult',
    'AwaitableGetComponentVersionResult',
    'get_component_version',
    'get_component_version_output',
]

@pulumi.output_type
class GetComponentVersionResult:
    def __init__(__self__, arn=None, component_name=None, component_version=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if component_name and not isinstance(component_name, str):
            raise TypeError("Expected argument 'component_name' to be a str")
        pulumi.set(__self__, "component_name", component_name)
        if component_version and not isinstance(component_version, str):
            raise TypeError("Expected argument 'component_version' to be a str")
        pulumi.set(__self__, "component_version", component_version)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="componentName")
    def component_name(self) -> Optional[str]:
        return pulumi.get(self, "component_name")

    @property
    @pulumi.getter(name="componentVersion")
    def component_version(self) -> Optional[str]:
        return pulumi.get(self, "component_version")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        return pulumi.get(self, "tags")


class AwaitableGetComponentVersionResult(GetComponentVersionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetComponentVersionResult(
            arn=self.arn,
            component_name=self.component_name,
            component_version=self.component_version,
            tags=self.tags)


def get_component_version(arn: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetComponentVersionResult:
    """
    Resource for Greengrass component version.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:greengrassv2:getComponentVersion', __args__, opts=opts, typ=GetComponentVersionResult).value

    return AwaitableGetComponentVersionResult(
        arn=pulumi.get(__ret__, 'arn'),
        component_name=pulumi.get(__ret__, 'component_name'),
        component_version=pulumi.get(__ret__, 'component_version'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_component_version)
def get_component_version_output(arn: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetComponentVersionResult]:
    """
    Resource for Greengrass component version.
    """
    ...
