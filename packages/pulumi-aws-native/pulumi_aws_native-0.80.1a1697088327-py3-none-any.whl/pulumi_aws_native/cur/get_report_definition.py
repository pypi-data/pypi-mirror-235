# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'GetReportDefinitionResult',
    'AwaitableGetReportDefinitionResult',
    'get_report_definition',
    'get_report_definition_output',
]

@pulumi.output_type
class GetReportDefinitionResult:
    def __init__(__self__, additional_artifacts=None, compression=None, format=None, refresh_closed_reports=None, s3_bucket=None, s3_prefix=None, s3_region=None):
        if additional_artifacts and not isinstance(additional_artifacts, list):
            raise TypeError("Expected argument 'additional_artifacts' to be a list")
        pulumi.set(__self__, "additional_artifacts", additional_artifacts)
        if compression and not isinstance(compression, str):
            raise TypeError("Expected argument 'compression' to be a str")
        pulumi.set(__self__, "compression", compression)
        if format and not isinstance(format, str):
            raise TypeError("Expected argument 'format' to be a str")
        pulumi.set(__self__, "format", format)
        if refresh_closed_reports and not isinstance(refresh_closed_reports, bool):
            raise TypeError("Expected argument 'refresh_closed_reports' to be a bool")
        pulumi.set(__self__, "refresh_closed_reports", refresh_closed_reports)
        if s3_bucket and not isinstance(s3_bucket, str):
            raise TypeError("Expected argument 's3_bucket' to be a str")
        pulumi.set(__self__, "s3_bucket", s3_bucket)
        if s3_prefix and not isinstance(s3_prefix, str):
            raise TypeError("Expected argument 's3_prefix' to be a str")
        pulumi.set(__self__, "s3_prefix", s3_prefix)
        if s3_region and not isinstance(s3_region, str):
            raise TypeError("Expected argument 's3_region' to be a str")
        pulumi.set(__self__, "s3_region", s3_region)

    @property
    @pulumi.getter(name="additionalArtifacts")
    def additional_artifacts(self) -> Optional[Sequence['ReportDefinitionAdditionalArtifactsItem']]:
        """
        A list of manifests that you want Amazon Web Services to create for this report.
        """
        return pulumi.get(self, "additional_artifacts")

    @property
    @pulumi.getter
    def compression(self) -> Optional['ReportDefinitionCompression']:
        """
        The compression format that AWS uses for the report.
        """
        return pulumi.get(self, "compression")

    @property
    @pulumi.getter
    def format(self) -> Optional['ReportDefinitionFormat']:
        """
        The format that AWS saves the report in.
        """
        return pulumi.get(self, "format")

    @property
    @pulumi.getter(name="refreshClosedReports")
    def refresh_closed_reports(self) -> Optional[bool]:
        """
        Whether you want Amazon Web Services to update your reports after they have been finalized if Amazon Web Services detects charges related to previous months. These charges can include refunds, credits, or support fees.
        """
        return pulumi.get(self, "refresh_closed_reports")

    @property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> Optional[str]:
        """
        The S3 bucket where AWS delivers the report.
        """
        return pulumi.get(self, "s3_bucket")

    @property
    @pulumi.getter(name="s3Prefix")
    def s3_prefix(self) -> Optional[str]:
        """
        The prefix that AWS adds to the report name when AWS delivers the report. Your prefix can't include spaces.
        """
        return pulumi.get(self, "s3_prefix")

    @property
    @pulumi.getter(name="s3Region")
    def s3_region(self) -> Optional[str]:
        """
        The region of the S3 bucket that AWS delivers the report into.
        """
        return pulumi.get(self, "s3_region")


class AwaitableGetReportDefinitionResult(GetReportDefinitionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReportDefinitionResult(
            additional_artifacts=self.additional_artifacts,
            compression=self.compression,
            format=self.format,
            refresh_closed_reports=self.refresh_closed_reports,
            s3_bucket=self.s3_bucket,
            s3_prefix=self.s3_prefix,
            s3_region=self.s3_region)


def get_report_definition(report_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReportDefinitionResult:
    """
    The AWS::CUR::ReportDefinition resource creates a Cost & Usage Report with user-defined settings. You can use this resource to define settings like time granularity (hourly, daily, monthly), file format (Parquet, CSV), and S3 bucket for delivery of these reports.


    :param str report_name: The name of the report that you want to create. The name must be unique, is case sensitive, and can't include spaces.
    """
    __args__ = dict()
    __args__['reportName'] = report_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:cur:getReportDefinition', __args__, opts=opts, typ=GetReportDefinitionResult).value

    return AwaitableGetReportDefinitionResult(
        additional_artifacts=pulumi.get(__ret__, 'additional_artifacts'),
        compression=pulumi.get(__ret__, 'compression'),
        format=pulumi.get(__ret__, 'format'),
        refresh_closed_reports=pulumi.get(__ret__, 'refresh_closed_reports'),
        s3_bucket=pulumi.get(__ret__, 's3_bucket'),
        s3_prefix=pulumi.get(__ret__, 's3_prefix'),
        s3_region=pulumi.get(__ret__, 's3_region'))


@_utilities.lift_output_func(get_report_definition)
def get_report_definition_output(report_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReportDefinitionResult]:
    """
    The AWS::CUR::ReportDefinition resource creates a Cost & Usage Report with user-defined settings. You can use this resource to define settings like time granularity (hourly, daily, monthly), file format (Parquet, CSV), and S3 bucket for delivery of these reports.


    :param str report_name: The name of the report that you want to create. The name must be unique, is case sensitive, and can't include spaces.
    """
    ...
