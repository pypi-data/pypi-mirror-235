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
    'ChannelDestinationArgs',
    'ChannelTagArgs',
    'EventDataStoreAdvancedEventSelectorArgs',
    'EventDataStoreAdvancedFieldSelectorArgs',
    'EventDataStoreTagArgs',
    'TrailAdvancedEventSelectorArgs',
    'TrailAdvancedFieldSelectorArgs',
    'TrailDataResourceArgs',
    'TrailEventSelectorArgs',
    'TrailInsightSelectorArgs',
    'TrailTagArgs',
]

@pulumi.input_type
class ChannelDestinationArgs:
    def __init__(__self__, *,
                 location: pulumi.Input[str],
                 type: pulumi.Input['ChannelDestinationType']):
        """
        The resource that receives events arriving from a channel.
        :param pulumi.Input[str] location: The ARN of a resource that receives events from a channel.
        :param pulumi.Input['ChannelDestinationType'] type: The type of destination for events arriving from a channel.
        """
        ChannelDestinationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            location=location,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             location: pulumi.Input[str],
             type: pulumi.Input['ChannelDestinationType'],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("location", location)
        _setter("type", type)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        The ARN of a resource that receives events from a channel.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input['ChannelDestinationType']:
        """
        The type of destination for events arriving from a channel.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input['ChannelDestinationType']):
        pulumi.set(self, "type", value)


@pulumi.input_type
class ChannelTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        ChannelTagArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: pulumi.Input[str],
             value: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class EventDataStoreAdvancedEventSelectorArgs:
    def __init__(__self__, *,
                 field_selectors: pulumi.Input[Sequence[pulumi.Input['EventDataStoreAdvancedFieldSelectorArgs']]],
                 name: Optional[pulumi.Input[str]] = None):
        """
        Advanced event selectors let you create fine-grained selectors for the following AWS CloudTrail event record ﬁelds. They help you control costs by logging only those events that are important to you.
        :param pulumi.Input[Sequence[pulumi.Input['EventDataStoreAdvancedFieldSelectorArgs']]] field_selectors: Contains all selector statements in an advanced event selector.
        :param pulumi.Input[str] name: An optional, descriptive name for an advanced event selector, such as "Log data events for only two S3 buckets".
        """
        EventDataStoreAdvancedEventSelectorArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            field_selectors=field_selectors,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             field_selectors: pulumi.Input[Sequence[pulumi.Input['EventDataStoreAdvancedFieldSelectorArgs']]],
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("field_selectors", field_selectors)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="fieldSelectors")
    def field_selectors(self) -> pulumi.Input[Sequence[pulumi.Input['EventDataStoreAdvancedFieldSelectorArgs']]]:
        """
        Contains all selector statements in an advanced event selector.
        """
        return pulumi.get(self, "field_selectors")

    @field_selectors.setter
    def field_selectors(self, value: pulumi.Input[Sequence[pulumi.Input['EventDataStoreAdvancedFieldSelectorArgs']]]):
        pulumi.set(self, "field_selectors", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        An optional, descriptive name for an advanced event selector, such as "Log data events for only two S3 buckets".
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class EventDataStoreAdvancedFieldSelectorArgs:
    def __init__(__self__, *,
                 field: pulumi.Input[str],
                 ends_with: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 equals: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 not_ends_with: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 not_equals: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 not_starts_with: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 starts_with: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        A single selector statement in an advanced event selector.
        :param pulumi.Input[str] field: A field in an event record on which to filter events to be logged. Supported fields include readOnly, eventCategory, eventSource (for management events), eventName, resources.type, and resources.ARN.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ends_with: An operator that includes events that match the last few characters of the event record field specified as the value of Field.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] equals: An operator that includes events that match the exact value of the event record field specified as the value of Field. This is the only valid operator that you can use with the readOnly, eventCategory, and resources.type fields.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] not_ends_with: An operator that excludes events that match the last few characters of the event record field specified as the value of Field.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] not_equals: An operator that excludes events that match the exact value of the event record field specified as the value of Field.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] not_starts_with: An operator that excludes events that match the first few characters of the event record field specified as the value of Field.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] starts_with: An operator that includes events that match the first few characters of the event record field specified as the value of Field.
        """
        EventDataStoreAdvancedFieldSelectorArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            field=field,
            ends_with=ends_with,
            equals=equals,
            not_ends_with=not_ends_with,
            not_equals=not_equals,
            not_starts_with=not_starts_with,
            starts_with=starts_with,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             field: pulumi.Input[str],
             ends_with: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             equals: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             not_ends_with: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             not_equals: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             not_starts_with: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             starts_with: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("field", field)
        if ends_with is not None:
            _setter("ends_with", ends_with)
        if equals is not None:
            _setter("equals", equals)
        if not_ends_with is not None:
            _setter("not_ends_with", not_ends_with)
        if not_equals is not None:
            _setter("not_equals", not_equals)
        if not_starts_with is not None:
            _setter("not_starts_with", not_starts_with)
        if starts_with is not None:
            _setter("starts_with", starts_with)

    @property
    @pulumi.getter
    def field(self) -> pulumi.Input[str]:
        """
        A field in an event record on which to filter events to be logged. Supported fields include readOnly, eventCategory, eventSource (for management events), eventName, resources.type, and resources.ARN.
        """
        return pulumi.get(self, "field")

    @field.setter
    def field(self, value: pulumi.Input[str]):
        pulumi.set(self, "field", value)

    @property
    @pulumi.getter(name="endsWith")
    def ends_with(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An operator that includes events that match the last few characters of the event record field specified as the value of Field.
        """
        return pulumi.get(self, "ends_with")

    @ends_with.setter
    def ends_with(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ends_with", value)

    @property
    @pulumi.getter
    def equals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An operator that includes events that match the exact value of the event record field specified as the value of Field. This is the only valid operator that you can use with the readOnly, eventCategory, and resources.type fields.
        """
        return pulumi.get(self, "equals")

    @equals.setter
    def equals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "equals", value)

    @property
    @pulumi.getter(name="notEndsWith")
    def not_ends_with(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An operator that excludes events that match the last few characters of the event record field specified as the value of Field.
        """
        return pulumi.get(self, "not_ends_with")

    @not_ends_with.setter
    def not_ends_with(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "not_ends_with", value)

    @property
    @pulumi.getter(name="notEquals")
    def not_equals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An operator that excludes events that match the exact value of the event record field specified as the value of Field.
        """
        return pulumi.get(self, "not_equals")

    @not_equals.setter
    def not_equals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "not_equals", value)

    @property
    @pulumi.getter(name="notStartsWith")
    def not_starts_with(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An operator that excludes events that match the first few characters of the event record field specified as the value of Field.
        """
        return pulumi.get(self, "not_starts_with")

    @not_starts_with.setter
    def not_starts_with(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "not_starts_with", value)

    @property
    @pulumi.getter(name="startsWith")
    def starts_with(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An operator that includes events that match the first few characters of the event record field specified as the value of Field.
        """
        return pulumi.get(self, "starts_with")

    @starts_with.setter
    def starts_with(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "starts_with", value)


@pulumi.input_type
class EventDataStoreTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        An arbitrary set of tags (key-value pairs) for this event data store.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        EventDataStoreTagArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: pulumi.Input[str],
             value: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class TrailAdvancedEventSelectorArgs:
    def __init__(__self__, *,
                 field_selectors: pulumi.Input[Sequence[pulumi.Input['TrailAdvancedFieldSelectorArgs']]],
                 name: Optional[pulumi.Input[str]] = None):
        """
        Advanced event selectors let you create fine-grained selectors for the following AWS CloudTrail event record ﬁelds. They help you control costs by logging only those events that are important to you.
        :param pulumi.Input[Sequence[pulumi.Input['TrailAdvancedFieldSelectorArgs']]] field_selectors: Contains all selector statements in an advanced event selector.
        :param pulumi.Input[str] name: An optional, descriptive name for an advanced event selector, such as "Log data events for only two S3 buckets".
        """
        TrailAdvancedEventSelectorArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            field_selectors=field_selectors,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             field_selectors: pulumi.Input[Sequence[pulumi.Input['TrailAdvancedFieldSelectorArgs']]],
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("field_selectors", field_selectors)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="fieldSelectors")
    def field_selectors(self) -> pulumi.Input[Sequence[pulumi.Input['TrailAdvancedFieldSelectorArgs']]]:
        """
        Contains all selector statements in an advanced event selector.
        """
        return pulumi.get(self, "field_selectors")

    @field_selectors.setter
    def field_selectors(self, value: pulumi.Input[Sequence[pulumi.Input['TrailAdvancedFieldSelectorArgs']]]):
        pulumi.set(self, "field_selectors", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        An optional, descriptive name for an advanced event selector, such as "Log data events for only two S3 buckets".
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class TrailAdvancedFieldSelectorArgs:
    def __init__(__self__, *,
                 field: pulumi.Input[str],
                 ends_with: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 equals: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 not_ends_with: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 not_equals: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 not_starts_with: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 starts_with: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        A single selector statement in an advanced event selector.
        :param pulumi.Input[str] field: A field in an event record on which to filter events to be logged. Supported fields include readOnly, eventCategory, eventSource (for management events), eventName, resources.type, and resources.ARN.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ends_with: An operator that includes events that match the last few characters of the event record field specified as the value of Field.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] equals: An operator that includes events that match the exact value of the event record field specified as the value of Field. This is the only valid operator that you can use with the readOnly, eventCategory, and resources.type fields.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] not_ends_with: An operator that excludes events that match the last few characters of the event record field specified as the value of Field.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] not_equals: An operator that excludes events that match the exact value of the event record field specified as the value of Field.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] not_starts_with: An operator that excludes events that match the first few characters of the event record field specified as the value of Field.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] starts_with: An operator that includes events that match the first few characters of the event record field specified as the value of Field.
        """
        TrailAdvancedFieldSelectorArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            field=field,
            ends_with=ends_with,
            equals=equals,
            not_ends_with=not_ends_with,
            not_equals=not_equals,
            not_starts_with=not_starts_with,
            starts_with=starts_with,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             field: pulumi.Input[str],
             ends_with: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             equals: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             not_ends_with: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             not_equals: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             not_starts_with: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             starts_with: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("field", field)
        if ends_with is not None:
            _setter("ends_with", ends_with)
        if equals is not None:
            _setter("equals", equals)
        if not_ends_with is not None:
            _setter("not_ends_with", not_ends_with)
        if not_equals is not None:
            _setter("not_equals", not_equals)
        if not_starts_with is not None:
            _setter("not_starts_with", not_starts_with)
        if starts_with is not None:
            _setter("starts_with", starts_with)

    @property
    @pulumi.getter
    def field(self) -> pulumi.Input[str]:
        """
        A field in an event record on which to filter events to be logged. Supported fields include readOnly, eventCategory, eventSource (for management events), eventName, resources.type, and resources.ARN.
        """
        return pulumi.get(self, "field")

    @field.setter
    def field(self, value: pulumi.Input[str]):
        pulumi.set(self, "field", value)

    @property
    @pulumi.getter(name="endsWith")
    def ends_with(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An operator that includes events that match the last few characters of the event record field specified as the value of Field.
        """
        return pulumi.get(self, "ends_with")

    @ends_with.setter
    def ends_with(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ends_with", value)

    @property
    @pulumi.getter
    def equals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An operator that includes events that match the exact value of the event record field specified as the value of Field. This is the only valid operator that you can use with the readOnly, eventCategory, and resources.type fields.
        """
        return pulumi.get(self, "equals")

    @equals.setter
    def equals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "equals", value)

    @property
    @pulumi.getter(name="notEndsWith")
    def not_ends_with(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An operator that excludes events that match the last few characters of the event record field specified as the value of Field.
        """
        return pulumi.get(self, "not_ends_with")

    @not_ends_with.setter
    def not_ends_with(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "not_ends_with", value)

    @property
    @pulumi.getter(name="notEquals")
    def not_equals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An operator that excludes events that match the exact value of the event record field specified as the value of Field.
        """
        return pulumi.get(self, "not_equals")

    @not_equals.setter
    def not_equals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "not_equals", value)

    @property
    @pulumi.getter(name="notStartsWith")
    def not_starts_with(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An operator that excludes events that match the first few characters of the event record field specified as the value of Field.
        """
        return pulumi.get(self, "not_starts_with")

    @not_starts_with.setter
    def not_starts_with(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "not_starts_with", value)

    @property
    @pulumi.getter(name="startsWith")
    def starts_with(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An operator that includes events that match the first few characters of the event record field specified as the value of Field.
        """
        return pulumi.get(self, "starts_with")

    @starts_with.setter
    def starts_with(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "starts_with", value)


@pulumi.input_type
class TrailDataResourceArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        CloudTrail supports data event logging for Amazon S3 objects and AWS Lambda functions. You can specify up to 250 resources for an individual event selector, but the total number of data resources cannot exceed 250 across all event selectors in a trail. This limit does not apply if you configure resource logging for all data events.
        :param pulumi.Input[str] type: The resource type in which you want to log data events. You can specify AWS::S3::Object or AWS::Lambda::Function resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] values: An array of Amazon Resource Name (ARN) strings or partial ARN strings for the specified objects.
        """
        TrailDataResourceArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            type=type,
            values=values,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             type: pulumi.Input[str],
             values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("type", type)
        if values is not None:
            _setter("values", values)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The resource type in which you want to log data events. You can specify AWS::S3::Object or AWS::Lambda::Function resources.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An array of Amazon Resource Name (ARN) strings or partial ARN strings for the specified objects.
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "values", value)


@pulumi.input_type
class TrailEventSelectorArgs:
    def __init__(__self__, *,
                 data_resources: Optional[pulumi.Input[Sequence[pulumi.Input['TrailDataResourceArgs']]]] = None,
                 exclude_management_event_sources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 include_management_events: Optional[pulumi.Input[bool]] = None,
                 read_write_type: Optional[pulumi.Input['TrailEventSelectorReadWriteType']] = None):
        """
        The type of email sending events to publish to the event destination.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] exclude_management_event_sources: An optional list of service event sources from which you do not want management events to be logged on your trail. In this release, the list can be empty (disables the filter), or it can filter out AWS Key Management Service events by containing "kms.amazonaws.com". By default, ExcludeManagementEventSources is empty, and AWS KMS events are included in events that are logged to your trail.
        :param pulumi.Input[bool] include_management_events: Specify if you want your event selector to include management events for your trail.
        :param pulumi.Input['TrailEventSelectorReadWriteType'] read_write_type: Specify if you want your trail to log read-only events, write-only events, or all. For example, the EC2 GetConsoleOutput is a read-only API operation and RunInstances is a write-only API operation.
        """
        TrailEventSelectorArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            data_resources=data_resources,
            exclude_management_event_sources=exclude_management_event_sources,
            include_management_events=include_management_events,
            read_write_type=read_write_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             data_resources: Optional[pulumi.Input[Sequence[pulumi.Input['TrailDataResourceArgs']]]] = None,
             exclude_management_event_sources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             include_management_events: Optional[pulumi.Input[bool]] = None,
             read_write_type: Optional[pulumi.Input['TrailEventSelectorReadWriteType']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if data_resources is not None:
            _setter("data_resources", data_resources)
        if exclude_management_event_sources is not None:
            _setter("exclude_management_event_sources", exclude_management_event_sources)
        if include_management_events is not None:
            _setter("include_management_events", include_management_events)
        if read_write_type is not None:
            _setter("read_write_type", read_write_type)

    @property
    @pulumi.getter(name="dataResources")
    def data_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TrailDataResourceArgs']]]]:
        return pulumi.get(self, "data_resources")

    @data_resources.setter
    def data_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TrailDataResourceArgs']]]]):
        pulumi.set(self, "data_resources", value)

    @property
    @pulumi.getter(name="excludeManagementEventSources")
    def exclude_management_event_sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An optional list of service event sources from which you do not want management events to be logged on your trail. In this release, the list can be empty (disables the filter), or it can filter out AWS Key Management Service events by containing "kms.amazonaws.com". By default, ExcludeManagementEventSources is empty, and AWS KMS events are included in events that are logged to your trail.
        """
        return pulumi.get(self, "exclude_management_event_sources")

    @exclude_management_event_sources.setter
    def exclude_management_event_sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "exclude_management_event_sources", value)

    @property
    @pulumi.getter(name="includeManagementEvents")
    def include_management_events(self) -> Optional[pulumi.Input[bool]]:
        """
        Specify if you want your event selector to include management events for your trail.
        """
        return pulumi.get(self, "include_management_events")

    @include_management_events.setter
    def include_management_events(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_management_events", value)

    @property
    @pulumi.getter(name="readWriteType")
    def read_write_type(self) -> Optional[pulumi.Input['TrailEventSelectorReadWriteType']]:
        """
        Specify if you want your trail to log read-only events, write-only events, or all. For example, the EC2 GetConsoleOutput is a read-only API operation and RunInstances is a write-only API operation.
        """
        return pulumi.get(self, "read_write_type")

    @read_write_type.setter
    def read_write_type(self, value: Optional[pulumi.Input['TrailEventSelectorReadWriteType']]):
        pulumi.set(self, "read_write_type", value)


@pulumi.input_type
class TrailInsightSelectorArgs:
    def __init__(__self__, *,
                 insight_type: Optional[pulumi.Input[str]] = None):
        """
        A string that contains insight types that are logged on a trail.
        :param pulumi.Input[str] insight_type: The type of insight to log on a trail.
        """
        TrailInsightSelectorArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            insight_type=insight_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             insight_type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if insight_type is not None:
            _setter("insight_type", insight_type)

    @property
    @pulumi.getter(name="insightType")
    def insight_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of insight to log on a trail.
        """
        return pulumi.get(self, "insight_type")

    @insight_type.setter
    def insight_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "insight_type", value)


@pulumi.input_type
class TrailTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        An arbitrary set of tags (key-value pairs) for this trail.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        TrailTagArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: pulumi.Input[str],
             value: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


