# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['VpcEndpointConnectionNotificationArgs', 'VpcEndpointConnectionNotification']

@pulumi.input_type
class VpcEndpointConnectionNotificationArgs:
    def __init__(__self__, *,
                 connection_events: pulumi.Input[Sequence[pulumi.Input[str]]],
                 connection_notification_arn: pulumi.Input[str],
                 service_id: Optional[pulumi.Input[str]] = None,
                 vpc_endpoint_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VpcEndpointConnectionNotification resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] connection_events: The endpoint events for which to receive notifications.
        :param pulumi.Input[str] connection_notification_arn: The ARN of the SNS topic for the notifications.
        :param pulumi.Input[str] service_id: The ID of the endpoint service.
        :param pulumi.Input[str] vpc_endpoint_id: The ID of the endpoint.
        """
        VpcEndpointConnectionNotificationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            connection_events=connection_events,
            connection_notification_arn=connection_notification_arn,
            service_id=service_id,
            vpc_endpoint_id=vpc_endpoint_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             connection_events: pulumi.Input[Sequence[pulumi.Input[str]]],
             connection_notification_arn: pulumi.Input[str],
             service_id: Optional[pulumi.Input[str]] = None,
             vpc_endpoint_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("connection_events", connection_events)
        _setter("connection_notification_arn", connection_notification_arn)
        if service_id is not None:
            _setter("service_id", service_id)
        if vpc_endpoint_id is not None:
            _setter("vpc_endpoint_id", vpc_endpoint_id)

    @property
    @pulumi.getter(name="connectionEvents")
    def connection_events(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The endpoint events for which to receive notifications.
        """
        return pulumi.get(self, "connection_events")

    @connection_events.setter
    def connection_events(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "connection_events", value)

    @property
    @pulumi.getter(name="connectionNotificationArn")
    def connection_notification_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the SNS topic for the notifications.
        """
        return pulumi.get(self, "connection_notification_arn")

    @connection_notification_arn.setter
    def connection_notification_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "connection_notification_arn", value)

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the endpoint service.
        """
        return pulumi.get(self, "service_id")

    @service_id.setter
    def service_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_id", value)

    @property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the endpoint.
        """
        return pulumi.get(self, "vpc_endpoint_id")

    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_endpoint_id", value)


class VpcEndpointConnectionNotification(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_events: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 connection_notification_arn: Optional[pulumi.Input[str]] = None,
                 service_id: Optional[pulumi.Input[str]] = None,
                 vpc_endpoint_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EC2::VPCEndpointConnectionNotification

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] connection_events: The endpoint events for which to receive notifications.
        :param pulumi.Input[str] connection_notification_arn: The ARN of the SNS topic for the notifications.
        :param pulumi.Input[str] service_id: The ID of the endpoint service.
        :param pulumi.Input[str] vpc_endpoint_id: The ID of the endpoint.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VpcEndpointConnectionNotificationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EC2::VPCEndpointConnectionNotification

        :param str resource_name: The name of the resource.
        :param VpcEndpointConnectionNotificationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpcEndpointConnectionNotificationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            VpcEndpointConnectionNotificationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_events: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 connection_notification_arn: Optional[pulumi.Input[str]] = None,
                 service_id: Optional[pulumi.Input[str]] = None,
                 vpc_endpoint_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpcEndpointConnectionNotificationArgs.__new__(VpcEndpointConnectionNotificationArgs)

            if connection_events is None and not opts.urn:
                raise TypeError("Missing required property 'connection_events'")
            __props__.__dict__["connection_events"] = connection_events
            if connection_notification_arn is None and not opts.urn:
                raise TypeError("Missing required property 'connection_notification_arn'")
            __props__.__dict__["connection_notification_arn"] = connection_notification_arn
            __props__.__dict__["service_id"] = service_id
            __props__.__dict__["vpc_endpoint_id"] = vpc_endpoint_id
            __props__.__dict__["vpc_endpoint_connection_notification_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["service_id", "vpc_endpoint_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(VpcEndpointConnectionNotification, __self__).__init__(
            'aws-native:ec2:VpcEndpointConnectionNotification',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VpcEndpointConnectionNotification':
        """
        Get an existing VpcEndpointConnectionNotification resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VpcEndpointConnectionNotificationArgs.__new__(VpcEndpointConnectionNotificationArgs)

        __props__.__dict__["connection_events"] = None
        __props__.__dict__["connection_notification_arn"] = None
        __props__.__dict__["service_id"] = None
        __props__.__dict__["vpc_endpoint_connection_notification_id"] = None
        __props__.__dict__["vpc_endpoint_id"] = None
        return VpcEndpointConnectionNotification(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectionEvents")
    def connection_events(self) -> pulumi.Output[Sequence[str]]:
        """
        The endpoint events for which to receive notifications.
        """
        return pulumi.get(self, "connection_events")

    @property
    @pulumi.getter(name="connectionNotificationArn")
    def connection_notification_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the SNS topic for the notifications.
        """
        return pulumi.get(self, "connection_notification_arn")

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the endpoint service.
        """
        return pulumi.get(self, "service_id")

    @property
    @pulumi.getter(name="vpcEndpointConnectionNotificationId")
    def vpc_endpoint_connection_notification_id(self) -> pulumi.Output[str]:
        """
        VPC Endpoint Connection ID generated by service
        """
        return pulumi.get(self, "vpc_endpoint_connection_notification_id")

    @property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the endpoint.
        """
        return pulumi.get(self, "vpc_endpoint_id")

