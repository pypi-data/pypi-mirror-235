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
    'GroupMembershipMemberId',
]

@pulumi.output_type
class GroupMembershipMemberId(dict):
    """
    An object containing the identifier of a group member.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "userId":
            suggest = "user_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GroupMembershipMemberId. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GroupMembershipMemberId.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GroupMembershipMemberId.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 user_id: str):
        """
        An object containing the identifier of a group member.
        :param str user_id: The identifier for a user in the identity store.
        """
        GroupMembershipMemberId._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            user_id=user_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             user_id: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("user_id", user_id)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> str:
        """
        The identifier for a user in the identity store.
        """
        return pulumi.get(self, "user_id")


