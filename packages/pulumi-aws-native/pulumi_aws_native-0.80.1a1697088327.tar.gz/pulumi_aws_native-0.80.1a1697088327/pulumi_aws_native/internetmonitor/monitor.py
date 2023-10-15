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

__all__ = ['MonitorArgs', 'Monitor']

@pulumi.input_type
class MonitorArgs:
    def __init__(__self__, *,
                 health_events_config: Optional[pulumi.Input['MonitorHealthEventsConfigArgs']] = None,
                 internet_measurements_log_delivery: Optional[pulumi.Input['MonitorInternetMeasurementsLogDeliveryArgs']] = None,
                 max_city_networks_to_monitor: Optional[pulumi.Input[int]] = None,
                 monitor_name: Optional[pulumi.Input[str]] = None,
                 resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resources_to_add: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resources_to_remove: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 status: Optional[pulumi.Input['MonitorConfigState']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['MonitorTagArgs']]]] = None,
                 traffic_percentage_to_monitor: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Monitor resource.
        """
        MonitorArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            health_events_config=health_events_config,
            internet_measurements_log_delivery=internet_measurements_log_delivery,
            max_city_networks_to_monitor=max_city_networks_to_monitor,
            monitor_name=monitor_name,
            resources=resources,
            resources_to_add=resources_to_add,
            resources_to_remove=resources_to_remove,
            status=status,
            tags=tags,
            traffic_percentage_to_monitor=traffic_percentage_to_monitor,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             health_events_config: Optional[pulumi.Input['MonitorHealthEventsConfigArgs']] = None,
             internet_measurements_log_delivery: Optional[pulumi.Input['MonitorInternetMeasurementsLogDeliveryArgs']] = None,
             max_city_networks_to_monitor: Optional[pulumi.Input[int]] = None,
             monitor_name: Optional[pulumi.Input[str]] = None,
             resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             resources_to_add: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             resources_to_remove: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             status: Optional[pulumi.Input['MonitorConfigState']] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['MonitorTagArgs']]]] = None,
             traffic_percentage_to_monitor: Optional[pulumi.Input[int]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if health_events_config is not None:
            _setter("health_events_config", health_events_config)
        if internet_measurements_log_delivery is not None:
            _setter("internet_measurements_log_delivery", internet_measurements_log_delivery)
        if max_city_networks_to_monitor is not None:
            _setter("max_city_networks_to_monitor", max_city_networks_to_monitor)
        if monitor_name is not None:
            _setter("monitor_name", monitor_name)
        if resources is not None:
            _setter("resources", resources)
        if resources_to_add is not None:
            _setter("resources_to_add", resources_to_add)
        if resources_to_remove is not None:
            _setter("resources_to_remove", resources_to_remove)
        if status is not None:
            _setter("status", status)
        if tags is not None:
            _setter("tags", tags)
        if traffic_percentage_to_monitor is not None:
            _setter("traffic_percentage_to_monitor", traffic_percentage_to_monitor)

    @property
    @pulumi.getter(name="healthEventsConfig")
    def health_events_config(self) -> Optional[pulumi.Input['MonitorHealthEventsConfigArgs']]:
        return pulumi.get(self, "health_events_config")

    @health_events_config.setter
    def health_events_config(self, value: Optional[pulumi.Input['MonitorHealthEventsConfigArgs']]):
        pulumi.set(self, "health_events_config", value)

    @property
    @pulumi.getter(name="internetMeasurementsLogDelivery")
    def internet_measurements_log_delivery(self) -> Optional[pulumi.Input['MonitorInternetMeasurementsLogDeliveryArgs']]:
        return pulumi.get(self, "internet_measurements_log_delivery")

    @internet_measurements_log_delivery.setter
    def internet_measurements_log_delivery(self, value: Optional[pulumi.Input['MonitorInternetMeasurementsLogDeliveryArgs']]):
        pulumi.set(self, "internet_measurements_log_delivery", value)

    @property
    @pulumi.getter(name="maxCityNetworksToMonitor")
    def max_city_networks_to_monitor(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "max_city_networks_to_monitor")

    @max_city_networks_to_monitor.setter
    def max_city_networks_to_monitor(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_city_networks_to_monitor", value)

    @property
    @pulumi.getter(name="monitorName")
    def monitor_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "monitor_name")

    @monitor_name.setter
    def monitor_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "monitor_name", value)

    @property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "resources")

    @resources.setter
    def resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "resources", value)

    @property
    @pulumi.getter(name="resourcesToAdd")
    def resources_to_add(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "resources_to_add")

    @resources_to_add.setter
    def resources_to_add(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "resources_to_add", value)

    @property
    @pulumi.getter(name="resourcesToRemove")
    def resources_to_remove(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "resources_to_remove")

    @resources_to_remove.setter
    def resources_to_remove(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "resources_to_remove", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input['MonitorConfigState']]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input['MonitorConfigState']]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MonitorTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MonitorTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="trafficPercentageToMonitor")
    def traffic_percentage_to_monitor(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "traffic_percentage_to_monitor")

    @traffic_percentage_to_monitor.setter
    def traffic_percentage_to_monitor(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "traffic_percentage_to_monitor", value)


class Monitor(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 health_events_config: Optional[pulumi.Input[pulumi.InputType['MonitorHealthEventsConfigArgs']]] = None,
                 internet_measurements_log_delivery: Optional[pulumi.Input[pulumi.InputType['MonitorInternetMeasurementsLogDeliveryArgs']]] = None,
                 max_city_networks_to_monitor: Optional[pulumi.Input[int]] = None,
                 monitor_name: Optional[pulumi.Input[str]] = None,
                 resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resources_to_add: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resources_to_remove: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 status: Optional[pulumi.Input['MonitorConfigState']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MonitorTagArgs']]]]] = None,
                 traffic_percentage_to_monitor: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Represents a monitor, which defines the monitoring boundaries for measurements that Internet Monitor publishes information about for an application

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[MonitorArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a monitor, which defines the monitoring boundaries for measurements that Internet Monitor publishes information about for an application

        :param str resource_name: The name of the resource.
        :param MonitorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MonitorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            MonitorArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 health_events_config: Optional[pulumi.Input[pulumi.InputType['MonitorHealthEventsConfigArgs']]] = None,
                 internet_measurements_log_delivery: Optional[pulumi.Input[pulumi.InputType['MonitorInternetMeasurementsLogDeliveryArgs']]] = None,
                 max_city_networks_to_monitor: Optional[pulumi.Input[int]] = None,
                 monitor_name: Optional[pulumi.Input[str]] = None,
                 resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resources_to_add: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resources_to_remove: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 status: Optional[pulumi.Input['MonitorConfigState']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MonitorTagArgs']]]]] = None,
                 traffic_percentage_to_monitor: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MonitorArgs.__new__(MonitorArgs)

            if health_events_config is not None and not isinstance(health_events_config, MonitorHealthEventsConfigArgs):
                health_events_config = health_events_config or {}
                def _setter(key, value):
                    health_events_config[key] = value
                MonitorHealthEventsConfigArgs._configure(_setter, **health_events_config)
            __props__.__dict__["health_events_config"] = health_events_config
            if internet_measurements_log_delivery is not None and not isinstance(internet_measurements_log_delivery, MonitorInternetMeasurementsLogDeliveryArgs):
                internet_measurements_log_delivery = internet_measurements_log_delivery or {}
                def _setter(key, value):
                    internet_measurements_log_delivery[key] = value
                MonitorInternetMeasurementsLogDeliveryArgs._configure(_setter, **internet_measurements_log_delivery)
            __props__.__dict__["internet_measurements_log_delivery"] = internet_measurements_log_delivery
            __props__.__dict__["max_city_networks_to_monitor"] = max_city_networks_to_monitor
            __props__.__dict__["monitor_name"] = monitor_name
            __props__.__dict__["resources"] = resources
            __props__.__dict__["resources_to_add"] = resources_to_add
            __props__.__dict__["resources_to_remove"] = resources_to_remove
            __props__.__dict__["status"] = status
            __props__.__dict__["tags"] = tags
            __props__.__dict__["traffic_percentage_to_monitor"] = traffic_percentage_to_monitor
            __props__.__dict__["created_at"] = None
            __props__.__dict__["modified_at"] = None
            __props__.__dict__["monitor_arn"] = None
            __props__.__dict__["processing_status"] = None
            __props__.__dict__["processing_status_info"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["monitor_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Monitor, __self__).__init__(
            'aws-native:internetmonitor:Monitor',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Monitor':
        """
        Get an existing Monitor resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MonitorArgs.__new__(MonitorArgs)

        __props__.__dict__["created_at"] = None
        __props__.__dict__["health_events_config"] = None
        __props__.__dict__["internet_measurements_log_delivery"] = None
        __props__.__dict__["max_city_networks_to_monitor"] = None
        __props__.__dict__["modified_at"] = None
        __props__.__dict__["monitor_arn"] = None
        __props__.__dict__["monitor_name"] = None
        __props__.__dict__["processing_status"] = None
        __props__.__dict__["processing_status_info"] = None
        __props__.__dict__["resources"] = None
        __props__.__dict__["resources_to_add"] = None
        __props__.__dict__["resources_to_remove"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["traffic_percentage_to_monitor"] = None
        return Monitor(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="healthEventsConfig")
    def health_events_config(self) -> pulumi.Output[Optional['outputs.MonitorHealthEventsConfig']]:
        return pulumi.get(self, "health_events_config")

    @property
    @pulumi.getter(name="internetMeasurementsLogDelivery")
    def internet_measurements_log_delivery(self) -> pulumi.Output[Optional['outputs.MonitorInternetMeasurementsLogDelivery']]:
        return pulumi.get(self, "internet_measurements_log_delivery")

    @property
    @pulumi.getter(name="maxCityNetworksToMonitor")
    def max_city_networks_to_monitor(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "max_city_networks_to_monitor")

    @property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> pulumi.Output[str]:
        return pulumi.get(self, "modified_at")

    @property
    @pulumi.getter(name="monitorArn")
    def monitor_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "monitor_arn")

    @property
    @pulumi.getter(name="monitorName")
    def monitor_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "monitor_name")

    @property
    @pulumi.getter(name="processingStatus")
    def processing_status(self) -> pulumi.Output['MonitorProcessingStatusCode']:
        return pulumi.get(self, "processing_status")

    @property
    @pulumi.getter(name="processingStatusInfo")
    def processing_status_info(self) -> pulumi.Output[str]:
        return pulumi.get(self, "processing_status_info")

    @property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "resources")

    @property
    @pulumi.getter(name="resourcesToAdd")
    def resources_to_add(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "resources_to_add")

    @property
    @pulumi.getter(name="resourcesToRemove")
    def resources_to_remove(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "resources_to_remove")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional['MonitorConfigState']]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.MonitorTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trafficPercentageToMonitor")
    def traffic_percentage_to_monitor(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "traffic_percentage_to_monitor")

