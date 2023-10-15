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
from ._inputs import *

__all__ = ['InputArgs', 'Input']

@pulumi.input_type
class InputArgs:
    def __init__(__self__, *,
                 input_definition: pulumi.Input['InputDefinitionArgs'],
                 input_description: Optional[pulumi.Input[str]] = None,
                 input_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['InputTagArgs']]]] = None):
        """
        The set of arguments for constructing a Input resource.
        :param pulumi.Input[str] input_description: A brief description of the input.
        :param pulumi.Input[str] input_name: The name of the input.
        :param pulumi.Input[Sequence[pulumi.Input['InputTagArgs']]] tags: An array of key-value pairs to apply to this resource.
               
               For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
        """
        InputArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            input_definition=input_definition,
            input_description=input_description,
            input_name=input_name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             input_definition: pulumi.Input['InputDefinitionArgs'],
             input_description: Optional[pulumi.Input[str]] = None,
             input_name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['InputTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("input_definition", input_definition)
        if input_description is not None:
            _setter("input_description", input_description)
        if input_name is not None:
            _setter("input_name", input_name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="inputDefinition")
    def input_definition(self) -> pulumi.Input['InputDefinitionArgs']:
        return pulumi.get(self, "input_definition")

    @input_definition.setter
    def input_definition(self, value: pulumi.Input['InputDefinitionArgs']):
        pulumi.set(self, "input_definition", value)

    @property
    @pulumi.getter(name="inputDescription")
    def input_description(self) -> Optional[pulumi.Input[str]]:
        """
        A brief description of the input.
        """
        return pulumi.get(self, "input_description")

    @input_description.setter
    def input_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "input_description", value)

    @property
    @pulumi.getter(name="inputName")
    def input_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the input.
        """
        return pulumi.get(self, "input_name")

    @input_name.setter
    def input_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "input_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InputTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.

        For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InputTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Input(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 input_definition: Optional[pulumi.Input[pulumi.InputType['InputDefinitionArgs']]] = None,
                 input_description: Optional[pulumi.Input[str]] = None,
                 input_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputTagArgs']]]]] = None,
                 __props__=None):
        """
        The AWS::IoTEvents::Input resource creates an input. To monitor your devices and processes, they must have a way to get telemetry data into AWS IoT Events. This is done by sending messages as *inputs* to AWS IoT Events. For more information, see [How to Use AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html) in the *AWS IoT Events Developer Guide*.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] input_description: A brief description of the input.
        :param pulumi.Input[str] input_name: The name of the input.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
               
               For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InputArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::IoTEvents::Input resource creates an input. To monitor your devices and processes, they must have a way to get telemetry data into AWS IoT Events. This is done by sending messages as *inputs* to AWS IoT Events. For more information, see [How to Use AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html) in the *AWS IoT Events Developer Guide*.

        :param str resource_name: The name of the resource.
        :param InputArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InputArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            InputArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 input_definition: Optional[pulumi.Input[pulumi.InputType['InputDefinitionArgs']]] = None,
                 input_description: Optional[pulumi.Input[str]] = None,
                 input_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InputArgs.__new__(InputArgs)

            if input_definition is not None and not isinstance(input_definition, InputDefinitionArgs):
                input_definition = input_definition or {}
                def _setter(key, value):
                    input_definition[key] = value
                InputDefinitionArgs._configure(_setter, **input_definition)
            if input_definition is None and not opts.urn:
                raise TypeError("Missing required property 'input_definition'")
            __props__.__dict__["input_definition"] = input_definition
            __props__.__dict__["input_description"] = input_description
            __props__.__dict__["input_name"] = input_name
            __props__.__dict__["tags"] = tags
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["input_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Input, __self__).__init__(
            'aws-native:iotevents:Input',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Input':
        """
        Get an existing Input resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InputArgs.__new__(InputArgs)

        __props__.__dict__["input_definition"] = None
        __props__.__dict__["input_description"] = None
        __props__.__dict__["input_name"] = None
        __props__.__dict__["tags"] = None
        return Input(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="inputDefinition")
    def input_definition(self) -> pulumi.Output['outputs.InputDefinition']:
        return pulumi.get(self, "input_definition")

    @property
    @pulumi.getter(name="inputDescription")
    def input_description(self) -> pulumi.Output[Optional[str]]:
        """
        A brief description of the input.
        """
        return pulumi.get(self, "input_description")

    @property
    @pulumi.getter(name="inputName")
    def input_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the input.
        """
        return pulumi.get(self, "input_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.InputTag']]]:
        """
        An array of key-value pairs to apply to this resource.

        For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
        """
        return pulumi.get(self, "tags")

