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
    'GetDatasetGroupResult',
    'AwaitableGetDatasetGroupResult',
    'get_dataset_group',
    'get_dataset_group_output',
]

@pulumi.output_type
class GetDatasetGroupResult:
    def __init__(__self__, dataset_arns=None, dataset_group_arn=None, domain=None, tags=None):
        if dataset_arns and not isinstance(dataset_arns, list):
            raise TypeError("Expected argument 'dataset_arns' to be a list")
        pulumi.set(__self__, "dataset_arns", dataset_arns)
        if dataset_group_arn and not isinstance(dataset_group_arn, str):
            raise TypeError("Expected argument 'dataset_group_arn' to be a str")
        pulumi.set(__self__, "dataset_group_arn", dataset_group_arn)
        if domain and not isinstance(domain, str):
            raise TypeError("Expected argument 'domain' to be a str")
        pulumi.set(__self__, "domain", domain)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="datasetArns")
    def dataset_arns(self) -> Optional[Sequence[str]]:
        """
        An array of Amazon Resource Names (ARNs) of the datasets that you want to include in the dataset group.
        """
        return pulumi.get(self, "dataset_arns")

    @property
    @pulumi.getter(name="datasetGroupArn")
    def dataset_group_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the dataset group to delete.
        """
        return pulumi.get(self, "dataset_group_arn")

    @property
    @pulumi.getter
    def domain(self) -> Optional['DatasetGroupDomain']:
        """
        The domain associated with the dataset group. When you add a dataset to a dataset group, this value and the value specified for the Domain parameter of the CreateDataset operation must match.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.DatasetGroupTag']]:
        """
        The tags of Application Insights application.
        """
        return pulumi.get(self, "tags")


class AwaitableGetDatasetGroupResult(GetDatasetGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatasetGroupResult(
            dataset_arns=self.dataset_arns,
            dataset_group_arn=self.dataset_group_arn,
            domain=self.domain,
            tags=self.tags)


def get_dataset_group(dataset_group_arn: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatasetGroupResult:
    """
    Represents a dataset group that holds a collection of related datasets


    :param str dataset_group_arn: The Amazon Resource Name (ARN) of the dataset group to delete.
    """
    __args__ = dict()
    __args__['datasetGroupArn'] = dataset_group_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:forecast:getDatasetGroup', __args__, opts=opts, typ=GetDatasetGroupResult).value

    return AwaitableGetDatasetGroupResult(
        dataset_arns=pulumi.get(__ret__, 'dataset_arns'),
        dataset_group_arn=pulumi.get(__ret__, 'dataset_group_arn'),
        domain=pulumi.get(__ret__, 'domain'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_dataset_group)
def get_dataset_group_output(dataset_group_arn: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatasetGroupResult]:
    """
    Represents a dataset group that holds a collection of related datasets


    :param str dataset_group_arn: The Amazon Resource Name (ARN) of the dataset group to delete.
    """
    ...
