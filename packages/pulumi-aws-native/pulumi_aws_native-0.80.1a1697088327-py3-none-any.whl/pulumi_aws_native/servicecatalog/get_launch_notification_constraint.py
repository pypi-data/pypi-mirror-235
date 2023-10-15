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
    'GetLaunchNotificationConstraintResult',
    'AwaitableGetLaunchNotificationConstraintResult',
    'get_launch_notification_constraint',
    'get_launch_notification_constraint_output',
]

@pulumi.output_type
class GetLaunchNotificationConstraintResult:
    def __init__(__self__, accept_language=None, description=None, id=None, notification_arns=None):
        if accept_language and not isinstance(accept_language, str):
            raise TypeError("Expected argument 'accept_language' to be a str")
        pulumi.set(__self__, "accept_language", accept_language)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if notification_arns and not isinstance(notification_arns, list):
            raise TypeError("Expected argument 'notification_arns' to be a list")
        pulumi.set(__self__, "notification_arns", notification_arns)

    @property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[str]:
        return pulumi.get(self, "accept_language")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="notificationArns")
    def notification_arns(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "notification_arns")


class AwaitableGetLaunchNotificationConstraintResult(GetLaunchNotificationConstraintResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLaunchNotificationConstraintResult(
            accept_language=self.accept_language,
            description=self.description,
            id=self.id,
            notification_arns=self.notification_arns)


def get_launch_notification_constraint(id: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLaunchNotificationConstraintResult:
    """
    Resource Type definition for AWS::ServiceCatalog::LaunchNotificationConstraint
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:servicecatalog:getLaunchNotificationConstraint', __args__, opts=opts, typ=GetLaunchNotificationConstraintResult).value

    return AwaitableGetLaunchNotificationConstraintResult(
        accept_language=pulumi.get(__ret__, 'accept_language'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        notification_arns=pulumi.get(__ret__, 'notification_arns'))


@_utilities.lift_output_func(get_launch_notification_constraint)
def get_launch_notification_constraint_output(id: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLaunchNotificationConstraintResult]:
    """
    Resource Type definition for AWS::ServiceCatalog::LaunchNotificationConstraint
    """
    ...
