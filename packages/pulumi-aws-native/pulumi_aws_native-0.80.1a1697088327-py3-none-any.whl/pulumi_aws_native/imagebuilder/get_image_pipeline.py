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
    'GetImagePipelineResult',
    'AwaitableGetImagePipelineResult',
    'get_image_pipeline',
    'get_image_pipeline_output',
]

@pulumi.output_type
class GetImagePipelineResult:
    def __init__(__self__, arn=None, container_recipe_arn=None, description=None, distribution_configuration_arn=None, enhanced_image_metadata_enabled=None, image_recipe_arn=None, image_scanning_configuration=None, image_tests_configuration=None, infrastructure_configuration_arn=None, schedule=None, status=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if container_recipe_arn and not isinstance(container_recipe_arn, str):
            raise TypeError("Expected argument 'container_recipe_arn' to be a str")
        pulumi.set(__self__, "container_recipe_arn", container_recipe_arn)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if distribution_configuration_arn and not isinstance(distribution_configuration_arn, str):
            raise TypeError("Expected argument 'distribution_configuration_arn' to be a str")
        pulumi.set(__self__, "distribution_configuration_arn", distribution_configuration_arn)
        if enhanced_image_metadata_enabled and not isinstance(enhanced_image_metadata_enabled, bool):
            raise TypeError("Expected argument 'enhanced_image_metadata_enabled' to be a bool")
        pulumi.set(__self__, "enhanced_image_metadata_enabled", enhanced_image_metadata_enabled)
        if image_recipe_arn and not isinstance(image_recipe_arn, str):
            raise TypeError("Expected argument 'image_recipe_arn' to be a str")
        pulumi.set(__self__, "image_recipe_arn", image_recipe_arn)
        if image_scanning_configuration and not isinstance(image_scanning_configuration, dict):
            raise TypeError("Expected argument 'image_scanning_configuration' to be a dict")
        pulumi.set(__self__, "image_scanning_configuration", image_scanning_configuration)
        if image_tests_configuration and not isinstance(image_tests_configuration, dict):
            raise TypeError("Expected argument 'image_tests_configuration' to be a dict")
        pulumi.set(__self__, "image_tests_configuration", image_tests_configuration)
        if infrastructure_configuration_arn and not isinstance(infrastructure_configuration_arn, str):
            raise TypeError("Expected argument 'infrastructure_configuration_arn' to be a str")
        pulumi.set(__self__, "infrastructure_configuration_arn", infrastructure_configuration_arn)
        if schedule and not isinstance(schedule, dict):
            raise TypeError("Expected argument 'schedule' to be a dict")
        pulumi.set(__self__, "schedule", schedule)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the image pipeline.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="containerRecipeArn")
    def container_recipe_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the container recipe that defines how images are configured and tested.
        """
        return pulumi.get(self, "container_recipe_arn")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the image pipeline.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="distributionConfigurationArn")
    def distribution_configuration_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the distribution configuration associated with this image pipeline.
        """
        return pulumi.get(self, "distribution_configuration_arn")

    @property
    @pulumi.getter(name="enhancedImageMetadataEnabled")
    def enhanced_image_metadata_enabled(self) -> Optional[bool]:
        """
        Collects additional information about the image being created, including the operating system (OS) version and package list.
        """
        return pulumi.get(self, "enhanced_image_metadata_enabled")

    @property
    @pulumi.getter(name="imageRecipeArn")
    def image_recipe_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed.
        """
        return pulumi.get(self, "image_recipe_arn")

    @property
    @pulumi.getter(name="imageScanningConfiguration")
    def image_scanning_configuration(self) -> Optional['outputs.ImagePipelineImageScanningConfiguration']:
        """
        Contains settings for vulnerability scans.
        """
        return pulumi.get(self, "image_scanning_configuration")

    @property
    @pulumi.getter(name="imageTestsConfiguration")
    def image_tests_configuration(self) -> Optional['outputs.ImagePipelineImageTestsConfiguration']:
        """
        The image tests configuration of the image pipeline.
        """
        return pulumi.get(self, "image_tests_configuration")

    @property
    @pulumi.getter(name="infrastructureConfigurationArn")
    def infrastructure_configuration_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.
        """
        return pulumi.get(self, "infrastructure_configuration_arn")

    @property
    @pulumi.getter
    def schedule(self) -> Optional['outputs.ImagePipelineSchedule']:
        """
        The schedule of the image pipeline.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter
    def status(self) -> Optional['ImagePipelineStatus']:
        """
        The status of the image pipeline.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        The tags of this image pipeline.
        """
        return pulumi.get(self, "tags")


class AwaitableGetImagePipelineResult(GetImagePipelineResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetImagePipelineResult(
            arn=self.arn,
            container_recipe_arn=self.container_recipe_arn,
            description=self.description,
            distribution_configuration_arn=self.distribution_configuration_arn,
            enhanced_image_metadata_enabled=self.enhanced_image_metadata_enabled,
            image_recipe_arn=self.image_recipe_arn,
            image_scanning_configuration=self.image_scanning_configuration,
            image_tests_configuration=self.image_tests_configuration,
            infrastructure_configuration_arn=self.infrastructure_configuration_arn,
            schedule=self.schedule,
            status=self.status,
            tags=self.tags)


def get_image_pipeline(arn: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetImagePipelineResult:
    """
    Resource schema for AWS::ImageBuilder::ImagePipeline


    :param str arn: The Amazon Resource Name (ARN) of the image pipeline.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:imagebuilder:getImagePipeline', __args__, opts=opts, typ=GetImagePipelineResult).value

    return AwaitableGetImagePipelineResult(
        arn=pulumi.get(__ret__, 'arn'),
        container_recipe_arn=pulumi.get(__ret__, 'container_recipe_arn'),
        description=pulumi.get(__ret__, 'description'),
        distribution_configuration_arn=pulumi.get(__ret__, 'distribution_configuration_arn'),
        enhanced_image_metadata_enabled=pulumi.get(__ret__, 'enhanced_image_metadata_enabled'),
        image_recipe_arn=pulumi.get(__ret__, 'image_recipe_arn'),
        image_scanning_configuration=pulumi.get(__ret__, 'image_scanning_configuration'),
        image_tests_configuration=pulumi.get(__ret__, 'image_tests_configuration'),
        infrastructure_configuration_arn=pulumi.get(__ret__, 'infrastructure_configuration_arn'),
        schedule=pulumi.get(__ret__, 'schedule'),
        status=pulumi.get(__ret__, 'status'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_image_pipeline)
def get_image_pipeline_output(arn: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetImagePipelineResult]:
    """
    Resource schema for AWS::ImageBuilder::ImagePipeline


    :param str arn: The Amazon Resource Name (ARN) of the image pipeline.
    """
    ...
