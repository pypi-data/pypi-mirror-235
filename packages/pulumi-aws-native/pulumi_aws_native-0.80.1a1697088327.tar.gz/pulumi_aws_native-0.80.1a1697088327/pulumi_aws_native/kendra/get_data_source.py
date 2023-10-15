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
    'GetDataSourceResult',
    'AwaitableGetDataSourceResult',
    'get_data_source',
    'get_data_source_output',
]

@pulumi.output_type
class GetDataSourceResult:
    def __init__(__self__, arn=None, custom_document_enrichment_configuration=None, data_source_configuration=None, description=None, id=None, index_id=None, language_code=None, name=None, role_arn=None, schedule=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if custom_document_enrichment_configuration and not isinstance(custom_document_enrichment_configuration, dict):
            raise TypeError("Expected argument 'custom_document_enrichment_configuration' to be a dict")
        pulumi.set(__self__, "custom_document_enrichment_configuration", custom_document_enrichment_configuration)
        if data_source_configuration and not isinstance(data_source_configuration, dict):
            raise TypeError("Expected argument 'data_source_configuration' to be a dict")
        pulumi.set(__self__, "data_source_configuration", data_source_configuration)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if index_id and not isinstance(index_id, str):
            raise TypeError("Expected argument 'index_id' to be a str")
        pulumi.set(__self__, "index_id", index_id)
        if language_code and not isinstance(language_code, str):
            raise TypeError("Expected argument 'language_code' to be a str")
        pulumi.set(__self__, "language_code", language_code)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)
        if schedule and not isinstance(schedule, str):
            raise TypeError("Expected argument 'schedule' to be a str")
        pulumi.set(__self__, "schedule", schedule)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="customDocumentEnrichmentConfiguration")
    def custom_document_enrichment_configuration(self) -> Optional['outputs.DataSourceCustomDocumentEnrichmentConfiguration']:
        return pulumi.get(self, "custom_document_enrichment_configuration")

    @property
    @pulumi.getter(name="dataSourceConfiguration")
    def data_source_configuration(self) -> Optional['outputs.DataSourceConfiguration']:
        return pulumi.get(self, "data_source_configuration")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="indexId")
    def index_id(self) -> Optional[str]:
        return pulumi.get(self, "index_id")

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[str]:
        return pulumi.get(self, "language_code")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[str]:
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def schedule(self) -> Optional[str]:
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.DataSourceTag']]:
        """
        Tags for labeling the data source
        """
        return pulumi.get(self, "tags")


class AwaitableGetDataSourceResult(GetDataSourceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDataSourceResult(
            arn=self.arn,
            custom_document_enrichment_configuration=self.custom_document_enrichment_configuration,
            data_source_configuration=self.data_source_configuration,
            description=self.description,
            id=self.id,
            index_id=self.index_id,
            language_code=self.language_code,
            name=self.name,
            role_arn=self.role_arn,
            schedule=self.schedule,
            tags=self.tags)


def get_data_source(id: Optional[str] = None,
                    index_id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDataSourceResult:
    """
    Kendra DataSource
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['indexId'] = index_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:kendra:getDataSource', __args__, opts=opts, typ=GetDataSourceResult).value

    return AwaitableGetDataSourceResult(
        arn=pulumi.get(__ret__, 'arn'),
        custom_document_enrichment_configuration=pulumi.get(__ret__, 'custom_document_enrichment_configuration'),
        data_source_configuration=pulumi.get(__ret__, 'data_source_configuration'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        index_id=pulumi.get(__ret__, 'index_id'),
        language_code=pulumi.get(__ret__, 'language_code'),
        name=pulumi.get(__ret__, 'name'),
        role_arn=pulumi.get(__ret__, 'role_arn'),
        schedule=pulumi.get(__ret__, 'schedule'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_data_source)
def get_data_source_output(id: Optional[pulumi.Input[str]] = None,
                           index_id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDataSourceResult]:
    """
    Kendra DataSource
    """
    ...
