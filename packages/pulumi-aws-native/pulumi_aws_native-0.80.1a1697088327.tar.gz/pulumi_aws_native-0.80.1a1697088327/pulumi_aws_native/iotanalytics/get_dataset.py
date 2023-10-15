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
    'GetDatasetResult',
    'AwaitableGetDatasetResult',
    'get_dataset',
    'get_dataset_output',
]

@pulumi.output_type
class GetDatasetResult:
    def __init__(__self__, actions=None, content_delivery_rules=None, id=None, late_data_rules=None, retention_period=None, tags=None, triggers=None, versioning_configuration=None):
        if actions and not isinstance(actions, list):
            raise TypeError("Expected argument 'actions' to be a list")
        pulumi.set(__self__, "actions", actions)
        if content_delivery_rules and not isinstance(content_delivery_rules, list):
            raise TypeError("Expected argument 'content_delivery_rules' to be a list")
        pulumi.set(__self__, "content_delivery_rules", content_delivery_rules)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if late_data_rules and not isinstance(late_data_rules, list):
            raise TypeError("Expected argument 'late_data_rules' to be a list")
        pulumi.set(__self__, "late_data_rules", late_data_rules)
        if retention_period and not isinstance(retention_period, dict):
            raise TypeError("Expected argument 'retention_period' to be a dict")
        pulumi.set(__self__, "retention_period", retention_period)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if triggers and not isinstance(triggers, list):
            raise TypeError("Expected argument 'triggers' to be a list")
        pulumi.set(__self__, "triggers", triggers)
        if versioning_configuration and not isinstance(versioning_configuration, dict):
            raise TypeError("Expected argument 'versioning_configuration' to be a dict")
        pulumi.set(__self__, "versioning_configuration", versioning_configuration)

    @property
    @pulumi.getter
    def actions(self) -> Optional[Sequence['outputs.DatasetAction']]:
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter(name="contentDeliveryRules")
    def content_delivery_rules(self) -> Optional[Sequence['outputs.DatasetContentDeliveryRule']]:
        return pulumi.get(self, "content_delivery_rules")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lateDataRules")
    def late_data_rules(self) -> Optional[Sequence['outputs.DatasetLateDataRule']]:
        return pulumi.get(self, "late_data_rules")

    @property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional['outputs.DatasetRetentionPeriod']:
        return pulumi.get(self, "retention_period")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.DatasetTag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def triggers(self) -> Optional[Sequence['outputs.DatasetTrigger']]:
        return pulumi.get(self, "triggers")

    @property
    @pulumi.getter(name="versioningConfiguration")
    def versioning_configuration(self) -> Optional['outputs.DatasetVersioningConfiguration']:
        return pulumi.get(self, "versioning_configuration")


class AwaitableGetDatasetResult(GetDatasetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatasetResult(
            actions=self.actions,
            content_delivery_rules=self.content_delivery_rules,
            id=self.id,
            late_data_rules=self.late_data_rules,
            retention_period=self.retention_period,
            tags=self.tags,
            triggers=self.triggers,
            versioning_configuration=self.versioning_configuration)


def get_dataset(dataset_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatasetResult:
    """
    Resource Type definition for AWS::IoTAnalytics::Dataset
    """
    __args__ = dict()
    __args__['datasetName'] = dataset_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:iotanalytics:getDataset', __args__, opts=opts, typ=GetDatasetResult).value

    return AwaitableGetDatasetResult(
        actions=pulumi.get(__ret__, 'actions'),
        content_delivery_rules=pulumi.get(__ret__, 'content_delivery_rules'),
        id=pulumi.get(__ret__, 'id'),
        late_data_rules=pulumi.get(__ret__, 'late_data_rules'),
        retention_period=pulumi.get(__ret__, 'retention_period'),
        tags=pulumi.get(__ret__, 'tags'),
        triggers=pulumi.get(__ret__, 'triggers'),
        versioning_configuration=pulumi.get(__ret__, 'versioning_configuration'))


@_utilities.lift_output_func(get_dataset)
def get_dataset_output(dataset_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatasetResult]:
    """
    Resource Type definition for AWS::IoTAnalytics::Dataset
    """
    ...
