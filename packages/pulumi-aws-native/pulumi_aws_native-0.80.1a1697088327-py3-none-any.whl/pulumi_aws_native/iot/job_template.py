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
from ._inputs import *

__all__ = ['JobTemplateArgs', 'JobTemplate']

@pulumi.input_type
class JobTemplateArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 job_template_id: pulumi.Input[str],
                 abort_config: Optional[pulumi.Input['AbortConfigPropertiesArgs']] = None,
                 destination_package_versions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 document: Optional[pulumi.Input[str]] = None,
                 document_source: Optional[pulumi.Input[str]] = None,
                 job_arn: Optional[pulumi.Input[str]] = None,
                 job_executions_retry_config: Optional[pulumi.Input['JobExecutionsRetryConfigPropertiesArgs']] = None,
                 job_executions_rollout_config: Optional[pulumi.Input['JobExecutionsRolloutConfigPropertiesArgs']] = None,
                 maintenance_windows: Optional[pulumi.Input[Sequence[pulumi.Input['JobTemplateMaintenanceWindowArgs']]]] = None,
                 presigned_url_config: Optional[pulumi.Input['PresignedUrlConfigPropertiesArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['JobTemplateTagArgs']]]] = None,
                 timeout_config: Optional[pulumi.Input['TimeoutConfigPropertiesArgs']] = None):
        """
        The set of arguments for constructing a JobTemplate resource.
        :param pulumi.Input[str] description: A description of the Job Template.
        :param pulumi.Input['AbortConfigPropertiesArgs'] abort_config: The criteria that determine when and how a job abort takes place.
        :param pulumi.Input[str] document: The job document. Required if you don't specify a value for documentSource.
        :param pulumi.Input[str] document_source: An S3 link to the job document to use in the template. Required if you don't specify a value for document.
        :param pulumi.Input[str] job_arn: Optional for copying a JobTemplate from a pre-existing Job configuration.
        :param pulumi.Input['JobExecutionsRolloutConfigPropertiesArgs'] job_executions_rollout_config: Allows you to create a staged rollout of a job.
        :param pulumi.Input['PresignedUrlConfigPropertiesArgs'] presigned_url_config: Configuration for pre-signed S3 URLs.
        :param pulumi.Input[Sequence[pulumi.Input['JobTemplateTagArgs']]] tags: Metadata that can be used to manage the JobTemplate.
        :param pulumi.Input['TimeoutConfigPropertiesArgs'] timeout_config: Specifies the amount of time each device has to finish its execution of the job.
        """
        JobTemplateArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            description=description,
            job_template_id=job_template_id,
            abort_config=abort_config,
            destination_package_versions=destination_package_versions,
            document=document,
            document_source=document_source,
            job_arn=job_arn,
            job_executions_retry_config=job_executions_retry_config,
            job_executions_rollout_config=job_executions_rollout_config,
            maintenance_windows=maintenance_windows,
            presigned_url_config=presigned_url_config,
            tags=tags,
            timeout_config=timeout_config,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             description: pulumi.Input[str],
             job_template_id: pulumi.Input[str],
             abort_config: Optional[pulumi.Input['AbortConfigPropertiesArgs']] = None,
             destination_package_versions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             document: Optional[pulumi.Input[str]] = None,
             document_source: Optional[pulumi.Input[str]] = None,
             job_arn: Optional[pulumi.Input[str]] = None,
             job_executions_retry_config: Optional[pulumi.Input['JobExecutionsRetryConfigPropertiesArgs']] = None,
             job_executions_rollout_config: Optional[pulumi.Input['JobExecutionsRolloutConfigPropertiesArgs']] = None,
             maintenance_windows: Optional[pulumi.Input[Sequence[pulumi.Input['JobTemplateMaintenanceWindowArgs']]]] = None,
             presigned_url_config: Optional[pulumi.Input['PresignedUrlConfigPropertiesArgs']] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['JobTemplateTagArgs']]]] = None,
             timeout_config: Optional[pulumi.Input['TimeoutConfigPropertiesArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("description", description)
        _setter("job_template_id", job_template_id)
        if abort_config is not None:
            _setter("abort_config", abort_config)
        if destination_package_versions is not None:
            _setter("destination_package_versions", destination_package_versions)
        if document is not None:
            _setter("document", document)
        if document_source is not None:
            _setter("document_source", document_source)
        if job_arn is not None:
            _setter("job_arn", job_arn)
        if job_executions_retry_config is not None:
            _setter("job_executions_retry_config", job_executions_retry_config)
        if job_executions_rollout_config is not None:
            _setter("job_executions_rollout_config", job_executions_rollout_config)
        if maintenance_windows is not None:
            _setter("maintenance_windows", maintenance_windows)
        if presigned_url_config is not None:
            _setter("presigned_url_config", presigned_url_config)
        if tags is not None:
            _setter("tags", tags)
        if timeout_config is not None:
            _setter("timeout_config", timeout_config)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        A description of the Job Template.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="jobTemplateId")
    def job_template_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "job_template_id")

    @job_template_id.setter
    def job_template_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "job_template_id", value)

    @property
    @pulumi.getter(name="abortConfig")
    def abort_config(self) -> Optional[pulumi.Input['AbortConfigPropertiesArgs']]:
        """
        The criteria that determine when and how a job abort takes place.
        """
        return pulumi.get(self, "abort_config")

    @abort_config.setter
    def abort_config(self, value: Optional[pulumi.Input['AbortConfigPropertiesArgs']]):
        pulumi.set(self, "abort_config", value)

    @property
    @pulumi.getter(name="destinationPackageVersions")
    def destination_package_versions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "destination_package_versions")

    @destination_package_versions.setter
    def destination_package_versions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "destination_package_versions", value)

    @property
    @pulumi.getter
    def document(self) -> Optional[pulumi.Input[str]]:
        """
        The job document. Required if you don't specify a value for documentSource.
        """
        return pulumi.get(self, "document")

    @document.setter
    def document(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "document", value)

    @property
    @pulumi.getter(name="documentSource")
    def document_source(self) -> Optional[pulumi.Input[str]]:
        """
        An S3 link to the job document to use in the template. Required if you don't specify a value for document.
        """
        return pulumi.get(self, "document_source")

    @document_source.setter
    def document_source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "document_source", value)

    @property
    @pulumi.getter(name="jobArn")
    def job_arn(self) -> Optional[pulumi.Input[str]]:
        """
        Optional for copying a JobTemplate from a pre-existing Job configuration.
        """
        return pulumi.get(self, "job_arn")

    @job_arn.setter
    def job_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "job_arn", value)

    @property
    @pulumi.getter(name="jobExecutionsRetryConfig")
    def job_executions_retry_config(self) -> Optional[pulumi.Input['JobExecutionsRetryConfigPropertiesArgs']]:
        return pulumi.get(self, "job_executions_retry_config")

    @job_executions_retry_config.setter
    def job_executions_retry_config(self, value: Optional[pulumi.Input['JobExecutionsRetryConfigPropertiesArgs']]):
        pulumi.set(self, "job_executions_retry_config", value)

    @property
    @pulumi.getter(name="jobExecutionsRolloutConfig")
    def job_executions_rollout_config(self) -> Optional[pulumi.Input['JobExecutionsRolloutConfigPropertiesArgs']]:
        """
        Allows you to create a staged rollout of a job.
        """
        return pulumi.get(self, "job_executions_rollout_config")

    @job_executions_rollout_config.setter
    def job_executions_rollout_config(self, value: Optional[pulumi.Input['JobExecutionsRolloutConfigPropertiesArgs']]):
        pulumi.set(self, "job_executions_rollout_config", value)

    @property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['JobTemplateMaintenanceWindowArgs']]]]:
        return pulumi.get(self, "maintenance_windows")

    @maintenance_windows.setter
    def maintenance_windows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['JobTemplateMaintenanceWindowArgs']]]]):
        pulumi.set(self, "maintenance_windows", value)

    @property
    @pulumi.getter(name="presignedUrlConfig")
    def presigned_url_config(self) -> Optional[pulumi.Input['PresignedUrlConfigPropertiesArgs']]:
        """
        Configuration for pre-signed S3 URLs.
        """
        return pulumi.get(self, "presigned_url_config")

    @presigned_url_config.setter
    def presigned_url_config(self, value: Optional[pulumi.Input['PresignedUrlConfigPropertiesArgs']]):
        pulumi.set(self, "presigned_url_config", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['JobTemplateTagArgs']]]]:
        """
        Metadata that can be used to manage the JobTemplate.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['JobTemplateTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="timeoutConfig")
    def timeout_config(self) -> Optional[pulumi.Input['TimeoutConfigPropertiesArgs']]:
        """
        Specifies the amount of time each device has to finish its execution of the job.
        """
        return pulumi.get(self, "timeout_config")

    @timeout_config.setter
    def timeout_config(self, value: Optional[pulumi.Input['TimeoutConfigPropertiesArgs']]):
        pulumi.set(self, "timeout_config", value)


class JobTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 abort_config: Optional[pulumi.Input[pulumi.InputType['AbortConfigPropertiesArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination_package_versions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 document: Optional[pulumi.Input[str]] = None,
                 document_source: Optional[pulumi.Input[str]] = None,
                 job_arn: Optional[pulumi.Input[str]] = None,
                 job_executions_retry_config: Optional[pulumi.Input[pulumi.InputType['JobExecutionsRetryConfigPropertiesArgs']]] = None,
                 job_executions_rollout_config: Optional[pulumi.Input[pulumi.InputType['JobExecutionsRolloutConfigPropertiesArgs']]] = None,
                 job_template_id: Optional[pulumi.Input[str]] = None,
                 maintenance_windows: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['JobTemplateMaintenanceWindowArgs']]]]] = None,
                 presigned_url_config: Optional[pulumi.Input[pulumi.InputType['PresignedUrlConfigPropertiesArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['JobTemplateTagArgs']]]]] = None,
                 timeout_config: Optional[pulumi.Input[pulumi.InputType['TimeoutConfigPropertiesArgs']]] = None,
                 __props__=None):
        """
        Job templates enable you to preconfigure jobs so that you can deploy them to multiple sets of target devices.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AbortConfigPropertiesArgs']] abort_config: The criteria that determine when and how a job abort takes place.
        :param pulumi.Input[str] description: A description of the Job Template.
        :param pulumi.Input[str] document: The job document. Required if you don't specify a value for documentSource.
        :param pulumi.Input[str] document_source: An S3 link to the job document to use in the template. Required if you don't specify a value for document.
        :param pulumi.Input[str] job_arn: Optional for copying a JobTemplate from a pre-existing Job configuration.
        :param pulumi.Input[pulumi.InputType['JobExecutionsRolloutConfigPropertiesArgs']] job_executions_rollout_config: Allows you to create a staged rollout of a job.
        :param pulumi.Input[pulumi.InputType['PresignedUrlConfigPropertiesArgs']] presigned_url_config: Configuration for pre-signed S3 URLs.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['JobTemplateTagArgs']]]] tags: Metadata that can be used to manage the JobTemplate.
        :param pulumi.Input[pulumi.InputType['TimeoutConfigPropertiesArgs']] timeout_config: Specifies the amount of time each device has to finish its execution of the job.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: JobTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Job templates enable you to preconfigure jobs so that you can deploy them to multiple sets of target devices.

        :param str resource_name: The name of the resource.
        :param JobTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(JobTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            JobTemplateArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 abort_config: Optional[pulumi.Input[pulumi.InputType['AbortConfigPropertiesArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination_package_versions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 document: Optional[pulumi.Input[str]] = None,
                 document_source: Optional[pulumi.Input[str]] = None,
                 job_arn: Optional[pulumi.Input[str]] = None,
                 job_executions_retry_config: Optional[pulumi.Input[pulumi.InputType['JobExecutionsRetryConfigPropertiesArgs']]] = None,
                 job_executions_rollout_config: Optional[pulumi.Input[pulumi.InputType['JobExecutionsRolloutConfigPropertiesArgs']]] = None,
                 job_template_id: Optional[pulumi.Input[str]] = None,
                 maintenance_windows: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['JobTemplateMaintenanceWindowArgs']]]]] = None,
                 presigned_url_config: Optional[pulumi.Input[pulumi.InputType['PresignedUrlConfigPropertiesArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['JobTemplateTagArgs']]]]] = None,
                 timeout_config: Optional[pulumi.Input[pulumi.InputType['TimeoutConfigPropertiesArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = JobTemplateArgs.__new__(JobTemplateArgs)

            if abort_config is not None and not isinstance(abort_config, AbortConfigPropertiesArgs):
                abort_config = abort_config or {}
                def _setter(key, value):
                    abort_config[key] = value
                AbortConfigPropertiesArgs._configure(_setter, **abort_config)
            __props__.__dict__["abort_config"] = abort_config
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            __props__.__dict__["destination_package_versions"] = destination_package_versions
            __props__.__dict__["document"] = document
            __props__.__dict__["document_source"] = document_source
            __props__.__dict__["job_arn"] = job_arn
            if job_executions_retry_config is not None and not isinstance(job_executions_retry_config, JobExecutionsRetryConfigPropertiesArgs):
                job_executions_retry_config = job_executions_retry_config or {}
                def _setter(key, value):
                    job_executions_retry_config[key] = value
                JobExecutionsRetryConfigPropertiesArgs._configure(_setter, **job_executions_retry_config)
            __props__.__dict__["job_executions_retry_config"] = job_executions_retry_config
            if job_executions_rollout_config is not None and not isinstance(job_executions_rollout_config, JobExecutionsRolloutConfigPropertiesArgs):
                job_executions_rollout_config = job_executions_rollout_config or {}
                def _setter(key, value):
                    job_executions_rollout_config[key] = value
                JobExecutionsRolloutConfigPropertiesArgs._configure(_setter, **job_executions_rollout_config)
            __props__.__dict__["job_executions_rollout_config"] = job_executions_rollout_config
            if job_template_id is None and not opts.urn:
                raise TypeError("Missing required property 'job_template_id'")
            __props__.__dict__["job_template_id"] = job_template_id
            __props__.__dict__["maintenance_windows"] = maintenance_windows
            if presigned_url_config is not None and not isinstance(presigned_url_config, PresignedUrlConfigPropertiesArgs):
                presigned_url_config = presigned_url_config or {}
                def _setter(key, value):
                    presigned_url_config[key] = value
                PresignedUrlConfigPropertiesArgs._configure(_setter, **presigned_url_config)
            __props__.__dict__["presigned_url_config"] = presigned_url_config
            __props__.__dict__["tags"] = tags
            if timeout_config is not None and not isinstance(timeout_config, TimeoutConfigPropertiesArgs):
                timeout_config = timeout_config or {}
                def _setter(key, value):
                    timeout_config[key] = value
                TimeoutConfigPropertiesArgs._configure(_setter, **timeout_config)
            __props__.__dict__["timeout_config"] = timeout_config
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["abort_config", "description", "document", "document_source", "job_arn", "job_executions_rollout_config", "job_template_id", "presigned_url_config", "tags[*]", "timeout_config"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(JobTemplate, __self__).__init__(
            'aws-native:iot:JobTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'JobTemplate':
        """
        Get an existing JobTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = JobTemplateArgs.__new__(JobTemplateArgs)

        __props__.__dict__["abort_config"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["destination_package_versions"] = None
        __props__.__dict__["document"] = None
        __props__.__dict__["document_source"] = None
        __props__.__dict__["job_arn"] = None
        __props__.__dict__["job_executions_retry_config"] = None
        __props__.__dict__["job_executions_rollout_config"] = None
        __props__.__dict__["job_template_id"] = None
        __props__.__dict__["maintenance_windows"] = None
        __props__.__dict__["presigned_url_config"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["timeout_config"] = None
        return JobTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="abortConfig")
    def abort_config(self) -> pulumi.Output[Optional['outputs.AbortConfigProperties']]:
        """
        The criteria that determine when and how a job abort takes place.
        """
        return pulumi.get(self, "abort_config")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        A description of the Job Template.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="destinationPackageVersions")
    def destination_package_versions(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "destination_package_versions")

    @property
    @pulumi.getter
    def document(self) -> pulumi.Output[Optional[str]]:
        """
        The job document. Required if you don't specify a value for documentSource.
        """
        return pulumi.get(self, "document")

    @property
    @pulumi.getter(name="documentSource")
    def document_source(self) -> pulumi.Output[Optional[str]]:
        """
        An S3 link to the job document to use in the template. Required if you don't specify a value for document.
        """
        return pulumi.get(self, "document_source")

    @property
    @pulumi.getter(name="jobArn")
    def job_arn(self) -> pulumi.Output[Optional[str]]:
        """
        Optional for copying a JobTemplate from a pre-existing Job configuration.
        """
        return pulumi.get(self, "job_arn")

    @property
    @pulumi.getter(name="jobExecutionsRetryConfig")
    def job_executions_retry_config(self) -> pulumi.Output[Optional['outputs.JobExecutionsRetryConfigProperties']]:
        return pulumi.get(self, "job_executions_retry_config")

    @property
    @pulumi.getter(name="jobExecutionsRolloutConfig")
    def job_executions_rollout_config(self) -> pulumi.Output[Optional['outputs.JobExecutionsRolloutConfigProperties']]:
        """
        Allows you to create a staged rollout of a job.
        """
        return pulumi.get(self, "job_executions_rollout_config")

    @property
    @pulumi.getter(name="jobTemplateId")
    def job_template_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "job_template_id")

    @property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> pulumi.Output[Optional[Sequence['outputs.JobTemplateMaintenanceWindow']]]:
        return pulumi.get(self, "maintenance_windows")

    @property
    @pulumi.getter(name="presignedUrlConfig")
    def presigned_url_config(self) -> pulumi.Output[Optional['outputs.PresignedUrlConfigProperties']]:
        """
        Configuration for pre-signed S3 URLs.
        """
        return pulumi.get(self, "presigned_url_config")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.JobTemplateTag']]]:
        """
        Metadata that can be used to manage the JobTemplate.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeoutConfig")
    def timeout_config(self) -> pulumi.Output[Optional['outputs.TimeoutConfigProperties']]:
        """
        Specifies the amount of time each device has to finish its execution of the job.
        """
        return pulumi.get(self, "timeout_config")

