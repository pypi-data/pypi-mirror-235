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
    'CloudFormationProductCodeStarParameters',
    'CloudFormationProductConnectionParameters',
    'CloudFormationProductProvisioningArtifactProperties',
    'CloudFormationProductSourceConnection',
    'CloudFormationProductTag',
    'CloudFormationProvisionedProductProvisioningParameter',
    'CloudFormationProvisionedProductProvisioningPreferences',
    'CloudFormationProvisionedProductTag',
    'PortfolioTag',
    'ServiceActionDefinitionParameter',
]

@pulumi.output_type
class CloudFormationProductCodeStarParameters(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "artifactPath":
            suggest = "artifact_path"
        elif key == "connectionArn":
            suggest = "connection_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CloudFormationProductCodeStarParameters. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CloudFormationProductCodeStarParameters.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CloudFormationProductCodeStarParameters.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 artifact_path: str,
                 branch: str,
                 connection_arn: str,
                 repository: str):
        CloudFormationProductCodeStarParameters._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            artifact_path=artifact_path,
            branch=branch,
            connection_arn=connection_arn,
            repository=repository,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             artifact_path: str,
             branch: str,
             connection_arn: str,
             repository: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("artifact_path", artifact_path)
        _setter("branch", branch)
        _setter("connection_arn", connection_arn)
        _setter("repository", repository)

    @property
    @pulumi.getter(name="artifactPath")
    def artifact_path(self) -> str:
        return pulumi.get(self, "artifact_path")

    @property
    @pulumi.getter
    def branch(self) -> str:
        return pulumi.get(self, "branch")

    @property
    @pulumi.getter(name="connectionArn")
    def connection_arn(self) -> str:
        return pulumi.get(self, "connection_arn")

    @property
    @pulumi.getter
    def repository(self) -> str:
        return pulumi.get(self, "repository")


@pulumi.output_type
class CloudFormationProductConnectionParameters(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "codeStar":
            suggest = "code_star"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CloudFormationProductConnectionParameters. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CloudFormationProductConnectionParameters.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CloudFormationProductConnectionParameters.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 code_star: Optional['outputs.CloudFormationProductCodeStarParameters'] = None):
        CloudFormationProductConnectionParameters._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            code_star=code_star,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             code_star: Optional['outputs.CloudFormationProductCodeStarParameters'] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if code_star is not None:
            _setter("code_star", code_star)

    @property
    @pulumi.getter(name="codeStar")
    def code_star(self) -> Optional['outputs.CloudFormationProductCodeStarParameters']:
        return pulumi.get(self, "code_star")


@pulumi.output_type
class CloudFormationProductProvisioningArtifactProperties(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "disableTemplateValidation":
            suggest = "disable_template_validation"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CloudFormationProductProvisioningArtifactProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CloudFormationProductProvisioningArtifactProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CloudFormationProductProvisioningArtifactProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 info: Any,
                 description: Optional[str] = None,
                 disable_template_validation: Optional[bool] = None,
                 name: Optional[str] = None,
                 type: Optional[str] = None):
        CloudFormationProductProvisioningArtifactProperties._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            info=info,
            description=description,
            disable_template_validation=disable_template_validation,
            name=name,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             info: Any,
             description: Optional[str] = None,
             disable_template_validation: Optional[bool] = None,
             name: Optional[str] = None,
             type: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("info", info)
        if description is not None:
            _setter("description", description)
        if disable_template_validation is not None:
            _setter("disable_template_validation", disable_template_validation)
        if name is not None:
            _setter("name", name)
        if type is not None:
            _setter("type", type)

    @property
    @pulumi.getter
    def info(self) -> Any:
        return pulumi.get(self, "info")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="disableTemplateValidation")
    def disable_template_validation(self) -> Optional[bool]:
        return pulumi.get(self, "disable_template_validation")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")


@pulumi.output_type
class CloudFormationProductSourceConnection(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "connectionParameters":
            suggest = "connection_parameters"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CloudFormationProductSourceConnection. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CloudFormationProductSourceConnection.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CloudFormationProductSourceConnection.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 connection_parameters: 'outputs.CloudFormationProductConnectionParameters',
                 type: str):
        CloudFormationProductSourceConnection._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            connection_parameters=connection_parameters,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             connection_parameters: 'outputs.CloudFormationProductConnectionParameters',
             type: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("connection_parameters", connection_parameters)
        _setter("type", type)

    @property
    @pulumi.getter(name="connectionParameters")
    def connection_parameters(self) -> 'outputs.CloudFormationProductConnectionParameters':
        return pulumi.get(self, "connection_parameters")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


@pulumi.output_type
class CloudFormationProductTag(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        CloudFormationProductTag._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class CloudFormationProvisionedProductProvisioningParameter(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        CloudFormationProvisionedProductProvisioningParameter._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class CloudFormationProvisionedProductProvisioningPreferences(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "stackSetAccounts":
            suggest = "stack_set_accounts"
        elif key == "stackSetFailureToleranceCount":
            suggest = "stack_set_failure_tolerance_count"
        elif key == "stackSetFailureTolerancePercentage":
            suggest = "stack_set_failure_tolerance_percentage"
        elif key == "stackSetMaxConcurrencyCount":
            suggest = "stack_set_max_concurrency_count"
        elif key == "stackSetMaxConcurrencyPercentage":
            suggest = "stack_set_max_concurrency_percentage"
        elif key == "stackSetOperationType":
            suggest = "stack_set_operation_type"
        elif key == "stackSetRegions":
            suggest = "stack_set_regions"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CloudFormationProvisionedProductProvisioningPreferences. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CloudFormationProvisionedProductProvisioningPreferences.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CloudFormationProvisionedProductProvisioningPreferences.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 stack_set_accounts: Optional[Sequence[str]] = None,
                 stack_set_failure_tolerance_count: Optional[int] = None,
                 stack_set_failure_tolerance_percentage: Optional[int] = None,
                 stack_set_max_concurrency_count: Optional[int] = None,
                 stack_set_max_concurrency_percentage: Optional[int] = None,
                 stack_set_operation_type: Optional['CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType'] = None,
                 stack_set_regions: Optional[Sequence[str]] = None):
        CloudFormationProvisionedProductProvisioningPreferences._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            stack_set_accounts=stack_set_accounts,
            stack_set_failure_tolerance_count=stack_set_failure_tolerance_count,
            stack_set_failure_tolerance_percentage=stack_set_failure_tolerance_percentage,
            stack_set_max_concurrency_count=stack_set_max_concurrency_count,
            stack_set_max_concurrency_percentage=stack_set_max_concurrency_percentage,
            stack_set_operation_type=stack_set_operation_type,
            stack_set_regions=stack_set_regions,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             stack_set_accounts: Optional[Sequence[str]] = None,
             stack_set_failure_tolerance_count: Optional[int] = None,
             stack_set_failure_tolerance_percentage: Optional[int] = None,
             stack_set_max_concurrency_count: Optional[int] = None,
             stack_set_max_concurrency_percentage: Optional[int] = None,
             stack_set_operation_type: Optional['CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType'] = None,
             stack_set_regions: Optional[Sequence[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if stack_set_accounts is not None:
            _setter("stack_set_accounts", stack_set_accounts)
        if stack_set_failure_tolerance_count is not None:
            _setter("stack_set_failure_tolerance_count", stack_set_failure_tolerance_count)
        if stack_set_failure_tolerance_percentage is not None:
            _setter("stack_set_failure_tolerance_percentage", stack_set_failure_tolerance_percentage)
        if stack_set_max_concurrency_count is not None:
            _setter("stack_set_max_concurrency_count", stack_set_max_concurrency_count)
        if stack_set_max_concurrency_percentage is not None:
            _setter("stack_set_max_concurrency_percentage", stack_set_max_concurrency_percentage)
        if stack_set_operation_type is not None:
            _setter("stack_set_operation_type", stack_set_operation_type)
        if stack_set_regions is not None:
            _setter("stack_set_regions", stack_set_regions)

    @property
    @pulumi.getter(name="stackSetAccounts")
    def stack_set_accounts(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "stack_set_accounts")

    @property
    @pulumi.getter(name="stackSetFailureToleranceCount")
    def stack_set_failure_tolerance_count(self) -> Optional[int]:
        return pulumi.get(self, "stack_set_failure_tolerance_count")

    @property
    @pulumi.getter(name="stackSetFailureTolerancePercentage")
    def stack_set_failure_tolerance_percentage(self) -> Optional[int]:
        return pulumi.get(self, "stack_set_failure_tolerance_percentage")

    @property
    @pulumi.getter(name="stackSetMaxConcurrencyCount")
    def stack_set_max_concurrency_count(self) -> Optional[int]:
        return pulumi.get(self, "stack_set_max_concurrency_count")

    @property
    @pulumi.getter(name="stackSetMaxConcurrencyPercentage")
    def stack_set_max_concurrency_percentage(self) -> Optional[int]:
        return pulumi.get(self, "stack_set_max_concurrency_percentage")

    @property
    @pulumi.getter(name="stackSetOperationType")
    def stack_set_operation_type(self) -> Optional['CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType']:
        return pulumi.get(self, "stack_set_operation_type")

    @property
    @pulumi.getter(name="stackSetRegions")
    def stack_set_regions(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "stack_set_regions")


@pulumi.output_type
class CloudFormationProvisionedProductTag(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        CloudFormationProvisionedProductTag._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class PortfolioTag(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        PortfolioTag._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class ServiceActionDefinitionParameter(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        ServiceActionDefinitionParameter._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


