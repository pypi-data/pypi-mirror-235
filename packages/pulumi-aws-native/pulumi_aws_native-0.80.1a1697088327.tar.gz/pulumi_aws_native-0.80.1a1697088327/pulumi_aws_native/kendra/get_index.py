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

__all__ = [
    'GetIndexResult',
    'AwaitableGetIndexResult',
    'get_index',
    'get_index_output',
]

@pulumi.output_type
class GetIndexResult:
    def __init__(__self__, arn=None, capacity_units=None, description=None, document_metadata_configurations=None, id=None, name=None, role_arn=None, tags=None, user_context_policy=None, user_token_configurations=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if capacity_units and not isinstance(capacity_units, dict):
            raise TypeError("Expected argument 'capacity_units' to be a dict")
        pulumi.set(__self__, "capacity_units", capacity_units)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if document_metadata_configurations and not isinstance(document_metadata_configurations, list):
            raise TypeError("Expected argument 'document_metadata_configurations' to be a list")
        pulumi.set(__self__, "document_metadata_configurations", document_metadata_configurations)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if user_context_policy and not isinstance(user_context_policy, str):
            raise TypeError("Expected argument 'user_context_policy' to be a str")
        pulumi.set(__self__, "user_context_policy", user_context_policy)
        if user_token_configurations and not isinstance(user_token_configurations, list):
            raise TypeError("Expected argument 'user_token_configurations' to be a list")
        pulumi.set(__self__, "user_token_configurations", user_token_configurations)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="capacityUnits")
    def capacity_units(self) -> Optional['outputs.IndexCapacityUnitsConfiguration']:
        """
        Capacity units
        """
        return pulumi.get(self, "capacity_units")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description for the index
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="documentMetadataConfigurations")
    def document_metadata_configurations(self) -> Optional[Sequence['outputs.IndexDocumentMetadataConfiguration']]:
        """
        Document metadata configurations
        """
        return pulumi.get(self, "document_metadata_configurations")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[str]:
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.IndexTag']]:
        """
        Tags for labeling the index
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="userContextPolicy")
    def user_context_policy(self) -> Optional['IndexUserContextPolicy']:
        return pulumi.get(self, "user_context_policy")

    @property
    @pulumi.getter(name="userTokenConfigurations")
    def user_token_configurations(self) -> Optional[Sequence['outputs.IndexUserTokenConfiguration']]:
        return pulumi.get(self, "user_token_configurations")


class AwaitableGetIndexResult(GetIndexResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIndexResult(
            arn=self.arn,
            capacity_units=self.capacity_units,
            description=self.description,
            document_metadata_configurations=self.document_metadata_configurations,
            id=self.id,
            name=self.name,
            role_arn=self.role_arn,
            tags=self.tags,
            user_context_policy=self.user_context_policy,
            user_token_configurations=self.user_token_configurations)


def get_index(id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIndexResult:
    """
    A Kendra index
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:kendra:getIndex', __args__, opts=opts, typ=GetIndexResult).value

    return AwaitableGetIndexResult(
        arn=pulumi.get(__ret__, 'arn'),
        capacity_units=pulumi.get(__ret__, 'capacity_units'),
        description=pulumi.get(__ret__, 'description'),
        document_metadata_configurations=pulumi.get(__ret__, 'document_metadata_configurations'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        role_arn=pulumi.get(__ret__, 'role_arn'),
        tags=pulumi.get(__ret__, 'tags'),
        user_context_policy=pulumi.get(__ret__, 'user_context_policy'),
        user_token_configurations=pulumi.get(__ret__, 'user_token_configurations'))


@_utilities.lift_output_func(get_index)
def get_index_output(id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIndexResult]:
    """
    A Kendra index
    """
    ...
