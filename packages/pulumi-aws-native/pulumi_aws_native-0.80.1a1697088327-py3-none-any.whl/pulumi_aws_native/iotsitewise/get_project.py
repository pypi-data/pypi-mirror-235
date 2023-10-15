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

__all__ = [
    'GetProjectResult',
    'AwaitableGetProjectResult',
    'get_project',
    'get_project_output',
]

@pulumi.output_type
class GetProjectResult:
    def __init__(__self__, asset_ids=None, project_arn=None, project_description=None, project_id=None, project_name=None, tags=None):
        if asset_ids and not isinstance(asset_ids, list):
            raise TypeError("Expected argument 'asset_ids' to be a list")
        pulumi.set(__self__, "asset_ids", asset_ids)
        if project_arn and not isinstance(project_arn, str):
            raise TypeError("Expected argument 'project_arn' to be a str")
        pulumi.set(__self__, "project_arn", project_arn)
        if project_description and not isinstance(project_description, str):
            raise TypeError("Expected argument 'project_description' to be a str")
        pulumi.set(__self__, "project_description", project_description)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if project_name and not isinstance(project_name, str):
            raise TypeError("Expected argument 'project_name' to be a str")
        pulumi.set(__self__, "project_name", project_name)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="assetIds")
    def asset_ids(self) -> Optional[Sequence[str]]:
        """
        The IDs of the assets to be associated to the project.
        """
        return pulumi.get(self, "asset_ids")

    @property
    @pulumi.getter(name="projectArn")
    def project_arn(self) -> Optional[str]:
        """
        The ARN of the project.
        """
        return pulumi.get(self, "project_arn")

    @property
    @pulumi.getter(name="projectDescription")
    def project_description(self) -> Optional[str]:
        """
        A description for the project.
        """
        return pulumi.get(self, "project_description")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[str]:
        """
        The ID of the project.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> Optional[str]:
        """
        A friendly name for the project.
        """
        return pulumi.get(self, "project_name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ProjectTag']]:
        """
        A list of key-value pairs that contain metadata for the project.
        """
        return pulumi.get(self, "tags")


class AwaitableGetProjectResult(GetProjectResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProjectResult(
            asset_ids=self.asset_ids,
            project_arn=self.project_arn,
            project_description=self.project_description,
            project_id=self.project_id,
            project_name=self.project_name,
            tags=self.tags)


def get_project(project_id: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProjectResult:
    """
    Resource schema for AWS::IoTSiteWise::Project


    :param str project_id: The ID of the project.
    """
    __args__ = dict()
    __args__['projectId'] = project_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:iotsitewise:getProject', __args__, opts=opts, typ=GetProjectResult).value

    return AwaitableGetProjectResult(
        asset_ids=pulumi.get(__ret__, 'asset_ids'),
        project_arn=pulumi.get(__ret__, 'project_arn'),
        project_description=pulumi.get(__ret__, 'project_description'),
        project_id=pulumi.get(__ret__, 'project_id'),
        project_name=pulumi.get(__ret__, 'project_name'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_project)
def get_project_output(project_id: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProjectResult]:
    """
    Resource schema for AWS::IoTSiteWise::Project


    :param str project_id: The ID of the project.
    """
    ...
