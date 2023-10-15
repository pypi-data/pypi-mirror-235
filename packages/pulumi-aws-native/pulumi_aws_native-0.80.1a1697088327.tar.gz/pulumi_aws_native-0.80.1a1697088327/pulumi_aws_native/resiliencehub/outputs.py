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
    'AppEventSubscription',
    'AppPermissionModel',
    'AppPhysicalResourceId',
    'AppResourceMapping',
    'AppTagMap',
    'ResiliencyPolicyPolicyMap',
    'ResiliencyPolicyTagMap',
]

@pulumi.output_type
class AppEventSubscription(dict):
    """
    Indicates an event you would like to subscribe and get notification for.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "eventType":
            suggest = "event_type"
        elif key == "snsTopicArn":
            suggest = "sns_topic_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AppEventSubscription. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AppEventSubscription.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AppEventSubscription.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 event_type: 'AppEventSubscriptionEventType',
                 name: str,
                 sns_topic_arn: Optional[str] = None):
        """
        Indicates an event you would like to subscribe and get notification for.
        :param 'AppEventSubscriptionEventType' event_type: The type of event you would like to subscribe and get notification for.
        :param str name: Unique name to identify an event subscription.
        :param str sns_topic_arn: Amazon Resource Name (ARN) of the Amazon Simple Notification Service topic.
        """
        AppEventSubscription._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            event_type=event_type,
            name=name,
            sns_topic_arn=sns_topic_arn,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             event_type: 'AppEventSubscriptionEventType',
             name: str,
             sns_topic_arn: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("event_type", event_type)
        _setter("name", name)
        if sns_topic_arn is not None:
            _setter("sns_topic_arn", sns_topic_arn)

    @property
    @pulumi.getter(name="eventType")
    def event_type(self) -> 'AppEventSubscriptionEventType':
        """
        The type of event you would like to subscribe and get notification for.
        """
        return pulumi.get(self, "event_type")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Unique name to identify an event subscription.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> Optional[str]:
        """
        Amazon Resource Name (ARN) of the Amazon Simple Notification Service topic.
        """
        return pulumi.get(self, "sns_topic_arn")


@pulumi.output_type
class AppPermissionModel(dict):
    """
    Defines the roles and credentials that AWS Resilience Hub would use while creating the application, importing its resources, and running an assessment.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "crossAccountRoleArns":
            suggest = "cross_account_role_arns"
        elif key == "invokerRoleName":
            suggest = "invoker_role_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AppPermissionModel. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AppPermissionModel.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AppPermissionModel.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: 'AppPermissionModelType',
                 cross_account_role_arns: Optional[Sequence[str]] = None,
                 invoker_role_name: Optional[str] = None):
        """
        Defines the roles and credentials that AWS Resilience Hub would use while creating the application, importing its resources, and running an assessment.
        :param 'AppPermissionModelType' type: Defines how AWS Resilience Hub scans your resources. It can scan for the resources by using a pre-existing role in your AWS account, or by using the credentials of the current IAM user.
        :param Sequence[str] cross_account_role_arns: Defines a list of role Amazon Resource Names (ARNs) to be used in other accounts. These ARNs are used for querying purposes while importing resources and assessing your application.
        :param str invoker_role_name: Existing AWS IAM role name in the primary AWS account that will be assumed by AWS Resilience Hub Service Principle to obtain a read-only access to your application resources while running an assessment.
        """
        AppPermissionModel._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            type=type,
            cross_account_role_arns=cross_account_role_arns,
            invoker_role_name=invoker_role_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             type: 'AppPermissionModelType',
             cross_account_role_arns: Optional[Sequence[str]] = None,
             invoker_role_name: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("type", type)
        if cross_account_role_arns is not None:
            _setter("cross_account_role_arns", cross_account_role_arns)
        if invoker_role_name is not None:
            _setter("invoker_role_name", invoker_role_name)

    @property
    @pulumi.getter
    def type(self) -> 'AppPermissionModelType':
        """
        Defines how AWS Resilience Hub scans your resources. It can scan for the resources by using a pre-existing role in your AWS account, or by using the credentials of the current IAM user.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="crossAccountRoleArns")
    def cross_account_role_arns(self) -> Optional[Sequence[str]]:
        """
        Defines a list of role Amazon Resource Names (ARNs) to be used in other accounts. These ARNs are used for querying purposes while importing resources and assessing your application.
        """
        return pulumi.get(self, "cross_account_role_arns")

    @property
    @pulumi.getter(name="invokerRoleName")
    def invoker_role_name(self) -> Optional[str]:
        """
        Existing AWS IAM role name in the primary AWS account that will be assumed by AWS Resilience Hub Service Principle to obtain a read-only access to your application resources while running an assessment.
        """
        return pulumi.get(self, "invoker_role_name")


@pulumi.output_type
class AppPhysicalResourceId(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "awsAccountId":
            suggest = "aws_account_id"
        elif key == "awsRegion":
            suggest = "aws_region"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AppPhysicalResourceId. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AppPhysicalResourceId.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AppPhysicalResourceId.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 identifier: str,
                 type: str,
                 aws_account_id: Optional[str] = None,
                 aws_region: Optional[str] = None):
        AppPhysicalResourceId._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            identifier=identifier,
            type=type,
            aws_account_id=aws_account_id,
            aws_region=aws_region,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             identifier: str,
             type: str,
             aws_account_id: Optional[str] = None,
             aws_region: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("identifier", identifier)
        _setter("type", type)
        if aws_account_id is not None:
            _setter("aws_account_id", aws_account_id)
        if aws_region is not None:
            _setter("aws_region", aws_region)

    @property
    @pulumi.getter
    def identifier(self) -> str:
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[str]:
        return pulumi.get(self, "aws_account_id")

    @property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> Optional[str]:
        return pulumi.get(self, "aws_region")


@pulumi.output_type
class AppResourceMapping(dict):
    """
    Resource mapping is used to map logical resources from template to physical resource
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "mappingType":
            suggest = "mapping_type"
        elif key == "physicalResourceId":
            suggest = "physical_resource_id"
        elif key == "eksSourceName":
            suggest = "eks_source_name"
        elif key == "logicalStackName":
            suggest = "logical_stack_name"
        elif key == "resourceName":
            suggest = "resource_name"
        elif key == "terraformSourceName":
            suggest = "terraform_source_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AppResourceMapping. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AppResourceMapping.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AppResourceMapping.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 mapping_type: str,
                 physical_resource_id: 'outputs.AppPhysicalResourceId',
                 eks_source_name: Optional[str] = None,
                 logical_stack_name: Optional[str] = None,
                 resource_name: Optional[str] = None,
                 terraform_source_name: Optional[str] = None):
        """
        Resource mapping is used to map logical resources from template to physical resource
        """
        AppResourceMapping._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            mapping_type=mapping_type,
            physical_resource_id=physical_resource_id,
            eks_source_name=eks_source_name,
            logical_stack_name=logical_stack_name,
            resource_name=resource_name,
            terraform_source_name=terraform_source_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             mapping_type: str,
             physical_resource_id: 'outputs.AppPhysicalResourceId',
             eks_source_name: Optional[str] = None,
             logical_stack_name: Optional[str] = None,
             resource_name: Optional[str] = None,
             terraform_source_name: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("mapping_type", mapping_type)
        _setter("physical_resource_id", physical_resource_id)
        if eks_source_name is not None:
            _setter("eks_source_name", eks_source_name)
        if logical_stack_name is not None:
            _setter("logical_stack_name", logical_stack_name)
        if resource_name is not None:
            _setter("resource_name", resource_name)
        if terraform_source_name is not None:
            _setter("terraform_source_name", terraform_source_name)

    @property
    @pulumi.getter(name="mappingType")
    def mapping_type(self) -> str:
        return pulumi.get(self, "mapping_type")

    @property
    @pulumi.getter(name="physicalResourceId")
    def physical_resource_id(self) -> 'outputs.AppPhysicalResourceId':
        return pulumi.get(self, "physical_resource_id")

    @property
    @pulumi.getter(name="eksSourceName")
    def eks_source_name(self) -> Optional[str]:
        return pulumi.get(self, "eks_source_name")

    @property
    @pulumi.getter(name="logicalStackName")
    def logical_stack_name(self) -> Optional[str]:
        return pulumi.get(self, "logical_stack_name")

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[str]:
        return pulumi.get(self, "resource_name")

    @property
    @pulumi.getter(name="terraformSourceName")
    def terraform_source_name(self) -> Optional[str]:
        return pulumi.get(self, "terraform_source_name")


@pulumi.output_type
class AppTagMap(dict):
    def __init__(__self__):
        pass
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             opts: Optional[pulumi.ResourceOptions]=None):
        pass


@pulumi.output_type
class ResiliencyPolicyPolicyMap(dict):
    def __init__(__self__):
        pass
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             opts: Optional[pulumi.ResourceOptions]=None):
        pass


@pulumi.output_type
class ResiliencyPolicyTagMap(dict):
    def __init__(__self__):
        pass
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             opts: Optional[pulumi.ResourceOptions]=None):
        pass


