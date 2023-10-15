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
    'GetPortalResult',
    'AwaitableGetPortalResult',
    'get_portal',
    'get_portal_output',
]

@pulumi.output_type
class GetPortalResult:
    def __init__(__self__, alarms=None, notification_sender_email=None, portal_arn=None, portal_client_id=None, portal_contact_email=None, portal_description=None, portal_id=None, portal_name=None, portal_start_url=None, role_arn=None):
        if alarms and not isinstance(alarms, dict):
            raise TypeError("Expected argument 'alarms' to be a dict")
        pulumi.set(__self__, "alarms", alarms)
        if notification_sender_email and not isinstance(notification_sender_email, str):
            raise TypeError("Expected argument 'notification_sender_email' to be a str")
        pulumi.set(__self__, "notification_sender_email", notification_sender_email)
        if portal_arn and not isinstance(portal_arn, str):
            raise TypeError("Expected argument 'portal_arn' to be a str")
        pulumi.set(__self__, "portal_arn", portal_arn)
        if portal_client_id and not isinstance(portal_client_id, str):
            raise TypeError("Expected argument 'portal_client_id' to be a str")
        pulumi.set(__self__, "portal_client_id", portal_client_id)
        if portal_contact_email and not isinstance(portal_contact_email, str):
            raise TypeError("Expected argument 'portal_contact_email' to be a str")
        pulumi.set(__self__, "portal_contact_email", portal_contact_email)
        if portal_description and not isinstance(portal_description, str):
            raise TypeError("Expected argument 'portal_description' to be a str")
        pulumi.set(__self__, "portal_description", portal_description)
        if portal_id and not isinstance(portal_id, str):
            raise TypeError("Expected argument 'portal_id' to be a str")
        pulumi.set(__self__, "portal_id", portal_id)
        if portal_name and not isinstance(portal_name, str):
            raise TypeError("Expected argument 'portal_name' to be a str")
        pulumi.set(__self__, "portal_name", portal_name)
        if portal_start_url and not isinstance(portal_start_url, str):
            raise TypeError("Expected argument 'portal_start_url' to be a str")
        pulumi.set(__self__, "portal_start_url", portal_start_url)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)

    @property
    @pulumi.getter
    def alarms(self) -> Optional['outputs.AlarmsProperties']:
        """
        Contains the configuration information of an alarm created in an AWS IoT SiteWise Monitor portal. You can use the alarm to monitor an asset property and get notified when the asset property value is outside a specified range.
        """
        return pulumi.get(self, "alarms")

    @property
    @pulumi.getter(name="notificationSenderEmail")
    def notification_sender_email(self) -> Optional[str]:
        """
        The email address that sends alarm notifications.
        """
        return pulumi.get(self, "notification_sender_email")

    @property
    @pulumi.getter(name="portalArn")
    def portal_arn(self) -> Optional[str]:
        """
        The ARN of the portal, which has the following format.
        """
        return pulumi.get(self, "portal_arn")

    @property
    @pulumi.getter(name="portalClientId")
    def portal_client_id(self) -> Optional[str]:
        """
        The AWS SSO application generated client ID (used with AWS SSO APIs).
        """
        return pulumi.get(self, "portal_client_id")

    @property
    @pulumi.getter(name="portalContactEmail")
    def portal_contact_email(self) -> Optional[str]:
        """
        The AWS administrator's contact email address.
        """
        return pulumi.get(self, "portal_contact_email")

    @property
    @pulumi.getter(name="portalDescription")
    def portal_description(self) -> Optional[str]:
        """
        A description for the portal.
        """
        return pulumi.get(self, "portal_description")

    @property
    @pulumi.getter(name="portalId")
    def portal_id(self) -> Optional[str]:
        """
        The ID of the portal.
        """
        return pulumi.get(self, "portal_id")

    @property
    @pulumi.getter(name="portalName")
    def portal_name(self) -> Optional[str]:
        """
        A friendly name for the portal.
        """
        return pulumi.get(self, "portal_name")

    @property
    @pulumi.getter(name="portalStartUrl")
    def portal_start_url(self) -> Optional[str]:
        """
        The public root URL for the AWS IoT AWS IoT SiteWise Monitor application portal.
        """
        return pulumi.get(self, "portal_start_url")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[str]:
        """
        The ARN of a service role that allows the portal's users to access your AWS IoT SiteWise resources on your behalf.
        """
        return pulumi.get(self, "role_arn")


class AwaitableGetPortalResult(GetPortalResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPortalResult(
            alarms=self.alarms,
            notification_sender_email=self.notification_sender_email,
            portal_arn=self.portal_arn,
            portal_client_id=self.portal_client_id,
            portal_contact_email=self.portal_contact_email,
            portal_description=self.portal_description,
            portal_id=self.portal_id,
            portal_name=self.portal_name,
            portal_start_url=self.portal_start_url,
            role_arn=self.role_arn)


def get_portal(portal_id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPortalResult:
    """
    Resource schema for AWS::IoTSiteWise::Portal


    :param str portal_id: The ID of the portal.
    """
    __args__ = dict()
    __args__['portalId'] = portal_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:iotsitewise:getPortal', __args__, opts=opts, typ=GetPortalResult).value

    return AwaitableGetPortalResult(
        alarms=pulumi.get(__ret__, 'alarms'),
        notification_sender_email=pulumi.get(__ret__, 'notification_sender_email'),
        portal_arn=pulumi.get(__ret__, 'portal_arn'),
        portal_client_id=pulumi.get(__ret__, 'portal_client_id'),
        portal_contact_email=pulumi.get(__ret__, 'portal_contact_email'),
        portal_description=pulumi.get(__ret__, 'portal_description'),
        portal_id=pulumi.get(__ret__, 'portal_id'),
        portal_name=pulumi.get(__ret__, 'portal_name'),
        portal_start_url=pulumi.get(__ret__, 'portal_start_url'),
        role_arn=pulumi.get(__ret__, 'role_arn'))


@_utilities.lift_output_func(get_portal)
def get_portal_output(portal_id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPortalResult]:
    """
    Resource schema for AWS::IoTSiteWise::Portal


    :param str portal_id: The ID of the portal.
    """
    ...
