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

__all__ = ['Ec2FleetArgs', 'Ec2Fleet']

@pulumi.input_type
class Ec2FleetArgs:
    def __init__(__self__, *,
                 launch_template_configs: pulumi.Input[Sequence[pulumi.Input['Ec2FleetFleetLaunchTemplateConfigRequestArgs']]],
                 target_capacity_specification: pulumi.Input['Ec2FleetTargetCapacitySpecificationRequestArgs'],
                 context: Optional[pulumi.Input[str]] = None,
                 excess_capacity_termination_policy: Optional[pulumi.Input['Ec2FleetExcessCapacityTerminationPolicy']] = None,
                 on_demand_options: Optional[pulumi.Input['Ec2FleetOnDemandOptionsRequestArgs']] = None,
                 replace_unhealthy_instances: Optional[pulumi.Input[bool]] = None,
                 spot_options: Optional[pulumi.Input['Ec2FleetSpotOptionsRequestArgs']] = None,
                 tag_specifications: Optional[pulumi.Input[Sequence[pulumi.Input['Ec2FleetTagSpecificationArgs']]]] = None,
                 terminate_instances_with_expiration: Optional[pulumi.Input[bool]] = None,
                 type: Optional[pulumi.Input['Ec2FleetType']] = None,
                 valid_from: Optional[pulumi.Input[str]] = None,
                 valid_until: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Ec2Fleet resource.
        """
        Ec2FleetArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            launch_template_configs=launch_template_configs,
            target_capacity_specification=target_capacity_specification,
            context=context,
            excess_capacity_termination_policy=excess_capacity_termination_policy,
            on_demand_options=on_demand_options,
            replace_unhealthy_instances=replace_unhealthy_instances,
            spot_options=spot_options,
            tag_specifications=tag_specifications,
            terminate_instances_with_expiration=terminate_instances_with_expiration,
            type=type,
            valid_from=valid_from,
            valid_until=valid_until,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             launch_template_configs: pulumi.Input[Sequence[pulumi.Input['Ec2FleetFleetLaunchTemplateConfigRequestArgs']]],
             target_capacity_specification: pulumi.Input['Ec2FleetTargetCapacitySpecificationRequestArgs'],
             context: Optional[pulumi.Input[str]] = None,
             excess_capacity_termination_policy: Optional[pulumi.Input['Ec2FleetExcessCapacityTerminationPolicy']] = None,
             on_demand_options: Optional[pulumi.Input['Ec2FleetOnDemandOptionsRequestArgs']] = None,
             replace_unhealthy_instances: Optional[pulumi.Input[bool]] = None,
             spot_options: Optional[pulumi.Input['Ec2FleetSpotOptionsRequestArgs']] = None,
             tag_specifications: Optional[pulumi.Input[Sequence[pulumi.Input['Ec2FleetTagSpecificationArgs']]]] = None,
             terminate_instances_with_expiration: Optional[pulumi.Input[bool]] = None,
             type: Optional[pulumi.Input['Ec2FleetType']] = None,
             valid_from: Optional[pulumi.Input[str]] = None,
             valid_until: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("launch_template_configs", launch_template_configs)
        _setter("target_capacity_specification", target_capacity_specification)
        if context is not None:
            _setter("context", context)
        if excess_capacity_termination_policy is not None:
            _setter("excess_capacity_termination_policy", excess_capacity_termination_policy)
        if on_demand_options is not None:
            _setter("on_demand_options", on_demand_options)
        if replace_unhealthy_instances is not None:
            _setter("replace_unhealthy_instances", replace_unhealthy_instances)
        if spot_options is not None:
            _setter("spot_options", spot_options)
        if tag_specifications is not None:
            _setter("tag_specifications", tag_specifications)
        if terminate_instances_with_expiration is not None:
            _setter("terminate_instances_with_expiration", terminate_instances_with_expiration)
        if type is not None:
            _setter("type", type)
        if valid_from is not None:
            _setter("valid_from", valid_from)
        if valid_until is not None:
            _setter("valid_until", valid_until)

    @property
    @pulumi.getter(name="launchTemplateConfigs")
    def launch_template_configs(self) -> pulumi.Input[Sequence[pulumi.Input['Ec2FleetFleetLaunchTemplateConfigRequestArgs']]]:
        return pulumi.get(self, "launch_template_configs")

    @launch_template_configs.setter
    def launch_template_configs(self, value: pulumi.Input[Sequence[pulumi.Input['Ec2FleetFleetLaunchTemplateConfigRequestArgs']]]):
        pulumi.set(self, "launch_template_configs", value)

    @property
    @pulumi.getter(name="targetCapacitySpecification")
    def target_capacity_specification(self) -> pulumi.Input['Ec2FleetTargetCapacitySpecificationRequestArgs']:
        return pulumi.get(self, "target_capacity_specification")

    @target_capacity_specification.setter
    def target_capacity_specification(self, value: pulumi.Input['Ec2FleetTargetCapacitySpecificationRequestArgs']):
        pulumi.set(self, "target_capacity_specification", value)

    @property
    @pulumi.getter
    def context(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "context")

    @context.setter
    def context(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "context", value)

    @property
    @pulumi.getter(name="excessCapacityTerminationPolicy")
    def excess_capacity_termination_policy(self) -> Optional[pulumi.Input['Ec2FleetExcessCapacityTerminationPolicy']]:
        return pulumi.get(self, "excess_capacity_termination_policy")

    @excess_capacity_termination_policy.setter
    def excess_capacity_termination_policy(self, value: Optional[pulumi.Input['Ec2FleetExcessCapacityTerminationPolicy']]):
        pulumi.set(self, "excess_capacity_termination_policy", value)

    @property
    @pulumi.getter(name="onDemandOptions")
    def on_demand_options(self) -> Optional[pulumi.Input['Ec2FleetOnDemandOptionsRequestArgs']]:
        return pulumi.get(self, "on_demand_options")

    @on_demand_options.setter
    def on_demand_options(self, value: Optional[pulumi.Input['Ec2FleetOnDemandOptionsRequestArgs']]):
        pulumi.set(self, "on_demand_options", value)

    @property
    @pulumi.getter(name="replaceUnhealthyInstances")
    def replace_unhealthy_instances(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "replace_unhealthy_instances")

    @replace_unhealthy_instances.setter
    def replace_unhealthy_instances(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "replace_unhealthy_instances", value)

    @property
    @pulumi.getter(name="spotOptions")
    def spot_options(self) -> Optional[pulumi.Input['Ec2FleetSpotOptionsRequestArgs']]:
        return pulumi.get(self, "spot_options")

    @spot_options.setter
    def spot_options(self, value: Optional[pulumi.Input['Ec2FleetSpotOptionsRequestArgs']]):
        pulumi.set(self, "spot_options", value)

    @property
    @pulumi.getter(name="tagSpecifications")
    def tag_specifications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['Ec2FleetTagSpecificationArgs']]]]:
        return pulumi.get(self, "tag_specifications")

    @tag_specifications.setter
    def tag_specifications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['Ec2FleetTagSpecificationArgs']]]]):
        pulumi.set(self, "tag_specifications", value)

    @property
    @pulumi.getter(name="terminateInstancesWithExpiration")
    def terminate_instances_with_expiration(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "terminate_instances_with_expiration")

    @terminate_instances_with_expiration.setter
    def terminate_instances_with_expiration(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "terminate_instances_with_expiration", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input['Ec2FleetType']]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input['Ec2FleetType']]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="validFrom")
    def valid_from(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "valid_from")

    @valid_from.setter
    def valid_from(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "valid_from", value)

    @property
    @pulumi.getter(name="validUntil")
    def valid_until(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "valid_until")

    @valid_until.setter
    def valid_until(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "valid_until", value)


class Ec2Fleet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 context: Optional[pulumi.Input[str]] = None,
                 excess_capacity_termination_policy: Optional[pulumi.Input['Ec2FleetExcessCapacityTerminationPolicy']] = None,
                 launch_template_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['Ec2FleetFleetLaunchTemplateConfigRequestArgs']]]]] = None,
                 on_demand_options: Optional[pulumi.Input[pulumi.InputType['Ec2FleetOnDemandOptionsRequestArgs']]] = None,
                 replace_unhealthy_instances: Optional[pulumi.Input[bool]] = None,
                 spot_options: Optional[pulumi.Input[pulumi.InputType['Ec2FleetSpotOptionsRequestArgs']]] = None,
                 tag_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['Ec2FleetTagSpecificationArgs']]]]] = None,
                 target_capacity_specification: Optional[pulumi.Input[pulumi.InputType['Ec2FleetTargetCapacitySpecificationRequestArgs']]] = None,
                 terminate_instances_with_expiration: Optional[pulumi.Input[bool]] = None,
                 type: Optional[pulumi.Input['Ec2FleetType']] = None,
                 valid_from: Optional[pulumi.Input[str]] = None,
                 valid_until: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EC2::EC2Fleet

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Ec2FleetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EC2::EC2Fleet

        :param str resource_name: The name of the resource.
        :param Ec2FleetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(Ec2FleetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            Ec2FleetArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 context: Optional[pulumi.Input[str]] = None,
                 excess_capacity_termination_policy: Optional[pulumi.Input['Ec2FleetExcessCapacityTerminationPolicy']] = None,
                 launch_template_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['Ec2FleetFleetLaunchTemplateConfigRequestArgs']]]]] = None,
                 on_demand_options: Optional[pulumi.Input[pulumi.InputType['Ec2FleetOnDemandOptionsRequestArgs']]] = None,
                 replace_unhealthy_instances: Optional[pulumi.Input[bool]] = None,
                 spot_options: Optional[pulumi.Input[pulumi.InputType['Ec2FleetSpotOptionsRequestArgs']]] = None,
                 tag_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['Ec2FleetTagSpecificationArgs']]]]] = None,
                 target_capacity_specification: Optional[pulumi.Input[pulumi.InputType['Ec2FleetTargetCapacitySpecificationRequestArgs']]] = None,
                 terminate_instances_with_expiration: Optional[pulumi.Input[bool]] = None,
                 type: Optional[pulumi.Input['Ec2FleetType']] = None,
                 valid_from: Optional[pulumi.Input[str]] = None,
                 valid_until: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = Ec2FleetArgs.__new__(Ec2FleetArgs)

            __props__.__dict__["context"] = context
            __props__.__dict__["excess_capacity_termination_policy"] = excess_capacity_termination_policy
            if launch_template_configs is None and not opts.urn:
                raise TypeError("Missing required property 'launch_template_configs'")
            __props__.__dict__["launch_template_configs"] = launch_template_configs
            if on_demand_options is not None and not isinstance(on_demand_options, Ec2FleetOnDemandOptionsRequestArgs):
                on_demand_options = on_demand_options or {}
                def _setter(key, value):
                    on_demand_options[key] = value
                Ec2FleetOnDemandOptionsRequestArgs._configure(_setter, **on_demand_options)
            __props__.__dict__["on_demand_options"] = on_demand_options
            __props__.__dict__["replace_unhealthy_instances"] = replace_unhealthy_instances
            if spot_options is not None and not isinstance(spot_options, Ec2FleetSpotOptionsRequestArgs):
                spot_options = spot_options or {}
                def _setter(key, value):
                    spot_options[key] = value
                Ec2FleetSpotOptionsRequestArgs._configure(_setter, **spot_options)
            __props__.__dict__["spot_options"] = spot_options
            __props__.__dict__["tag_specifications"] = tag_specifications
            if target_capacity_specification is not None and not isinstance(target_capacity_specification, Ec2FleetTargetCapacitySpecificationRequestArgs):
                target_capacity_specification = target_capacity_specification or {}
                def _setter(key, value):
                    target_capacity_specification[key] = value
                Ec2FleetTargetCapacitySpecificationRequestArgs._configure(_setter, **target_capacity_specification)
            if target_capacity_specification is None and not opts.urn:
                raise TypeError("Missing required property 'target_capacity_specification'")
            __props__.__dict__["target_capacity_specification"] = target_capacity_specification
            __props__.__dict__["terminate_instances_with_expiration"] = terminate_instances_with_expiration
            __props__.__dict__["type"] = type
            __props__.__dict__["valid_from"] = valid_from
            __props__.__dict__["valid_until"] = valid_until
            __props__.__dict__["fleet_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["launch_template_configs[*]", "on_demand_options", "replace_unhealthy_instances", "spot_options", "tag_specifications[*]", "terminate_instances_with_expiration", "type", "valid_from", "valid_until"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Ec2Fleet, __self__).__init__(
            'aws-native:ec2:Ec2Fleet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Ec2Fleet':
        """
        Get an existing Ec2Fleet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = Ec2FleetArgs.__new__(Ec2FleetArgs)

        __props__.__dict__["context"] = None
        __props__.__dict__["excess_capacity_termination_policy"] = None
        __props__.__dict__["fleet_id"] = None
        __props__.__dict__["launch_template_configs"] = None
        __props__.__dict__["on_demand_options"] = None
        __props__.__dict__["replace_unhealthy_instances"] = None
        __props__.__dict__["spot_options"] = None
        __props__.__dict__["tag_specifications"] = None
        __props__.__dict__["target_capacity_specification"] = None
        __props__.__dict__["terminate_instances_with_expiration"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["valid_from"] = None
        __props__.__dict__["valid_until"] = None
        return Ec2Fleet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def context(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "context")

    @property
    @pulumi.getter(name="excessCapacityTerminationPolicy")
    def excess_capacity_termination_policy(self) -> pulumi.Output[Optional['Ec2FleetExcessCapacityTerminationPolicy']]:
        return pulumi.get(self, "excess_capacity_termination_policy")

    @property
    @pulumi.getter(name="fleetId")
    def fleet_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "fleet_id")

    @property
    @pulumi.getter(name="launchTemplateConfigs")
    def launch_template_configs(self) -> pulumi.Output[Sequence['outputs.Ec2FleetFleetLaunchTemplateConfigRequest']]:
        return pulumi.get(self, "launch_template_configs")

    @property
    @pulumi.getter(name="onDemandOptions")
    def on_demand_options(self) -> pulumi.Output[Optional['outputs.Ec2FleetOnDemandOptionsRequest']]:
        return pulumi.get(self, "on_demand_options")

    @property
    @pulumi.getter(name="replaceUnhealthyInstances")
    def replace_unhealthy_instances(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "replace_unhealthy_instances")

    @property
    @pulumi.getter(name="spotOptions")
    def spot_options(self) -> pulumi.Output[Optional['outputs.Ec2FleetSpotOptionsRequest']]:
        return pulumi.get(self, "spot_options")

    @property
    @pulumi.getter(name="tagSpecifications")
    def tag_specifications(self) -> pulumi.Output[Optional[Sequence['outputs.Ec2FleetTagSpecification']]]:
        return pulumi.get(self, "tag_specifications")

    @property
    @pulumi.getter(name="targetCapacitySpecification")
    def target_capacity_specification(self) -> pulumi.Output['outputs.Ec2FleetTargetCapacitySpecificationRequest']:
        return pulumi.get(self, "target_capacity_specification")

    @property
    @pulumi.getter(name="terminateInstancesWithExpiration")
    def terminate_instances_with_expiration(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "terminate_instances_with_expiration")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional['Ec2FleetType']]:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="validFrom")
    def valid_from(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "valid_from")

    @property
    @pulumi.getter(name="validUntil")
    def valid_until(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "valid_until")

