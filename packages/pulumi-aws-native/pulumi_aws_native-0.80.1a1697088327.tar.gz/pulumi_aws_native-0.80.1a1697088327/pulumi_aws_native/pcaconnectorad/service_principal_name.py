# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ServicePrincipalNameArgs', 'ServicePrincipalName']

@pulumi.input_type
class ServicePrincipalNameArgs:
    def __init__(__self__, *,
                 connector_arn: Optional[pulumi.Input[str]] = None,
                 directory_registration_arn: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ServicePrincipalName resource.
        """
        ServicePrincipalNameArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            connector_arn=connector_arn,
            directory_registration_arn=directory_registration_arn,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             connector_arn: Optional[pulumi.Input[str]] = None,
             directory_registration_arn: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if connector_arn is not None:
            _setter("connector_arn", connector_arn)
        if directory_registration_arn is not None:
            _setter("directory_registration_arn", directory_registration_arn)

    @property
    @pulumi.getter(name="connectorArn")
    def connector_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "connector_arn")

    @connector_arn.setter
    def connector_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connector_arn", value)

    @property
    @pulumi.getter(name="directoryRegistrationArn")
    def directory_registration_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "directory_registration_arn")

    @directory_registration_arn.setter
    def directory_registration_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "directory_registration_arn", value)


class ServicePrincipalName(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connector_arn: Optional[pulumi.Input[str]] = None,
                 directory_registration_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Definition of AWS::PCAConnectorAD::ServicePrincipalName Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ServicePrincipalNameArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::PCAConnectorAD::ServicePrincipalName Resource Type

        :param str resource_name: The name of the resource.
        :param ServicePrincipalNameArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServicePrincipalNameArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ServicePrincipalNameArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connector_arn: Optional[pulumi.Input[str]] = None,
                 directory_registration_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServicePrincipalNameArgs.__new__(ServicePrincipalNameArgs)

            __props__.__dict__["connector_arn"] = connector_arn
            __props__.__dict__["directory_registration_arn"] = directory_registration_arn
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["connector_arn", "directory_registration_arn"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ServicePrincipalName, __self__).__init__(
            'aws-native:pcaconnectorad:ServicePrincipalName',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServicePrincipalName':
        """
        Get an existing ServicePrincipalName resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServicePrincipalNameArgs.__new__(ServicePrincipalNameArgs)

        __props__.__dict__["connector_arn"] = None
        __props__.__dict__["directory_registration_arn"] = None
        return ServicePrincipalName(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectorArn")
    def connector_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "connector_arn")

    @property
    @pulumi.getter(name="directoryRegistrationArn")
    def directory_registration_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "directory_registration_arn")

