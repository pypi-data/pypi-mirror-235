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
    'ExecutionPlanCapacityUnitsConfiguration',
    'ExecutionPlanTag',
]

@pulumi.output_type
class ExecutionPlanCapacityUnitsConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "rescoreCapacityUnits":
            suggest = "rescore_capacity_units"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ExecutionPlanCapacityUnitsConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ExecutionPlanCapacityUnitsConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ExecutionPlanCapacityUnitsConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 rescore_capacity_units: int):
        ExecutionPlanCapacityUnitsConfiguration._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            rescore_capacity_units=rescore_capacity_units,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             rescore_capacity_units: int,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("rescore_capacity_units", rescore_capacity_units)

    @property
    @pulumi.getter(name="rescoreCapacityUnits")
    def rescore_capacity_units(self) -> int:
        return pulumi.get(self, "rescore_capacity_units")


@pulumi.output_type
class ExecutionPlanTag(dict):
    """
    A label for tagging KendraRanking resources
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A label for tagging KendraRanking resources
        :param str key: A string used to identify this tag
        :param str value: A string containing the value for the tag
        """
        ExecutionPlanTag._configure(
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
        """
        A string used to identify this tag
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        A string containing the value for the tag
        """
        return pulumi.get(self, "value")


