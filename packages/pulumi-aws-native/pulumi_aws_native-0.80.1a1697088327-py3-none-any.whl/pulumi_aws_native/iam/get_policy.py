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
    'GetPolicyResult',
    'AwaitableGetPolicyResult',
    'get_policy',
    'get_policy_output',
]

@pulumi.output_type
class GetPolicyResult:
    def __init__(__self__, groups=None, id=None, policy_document=None, policy_name=None, roles=None, users=None):
        if groups and not isinstance(groups, list):
            raise TypeError("Expected argument 'groups' to be a list")
        pulumi.set(__self__, "groups", groups)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if policy_document and not isinstance(policy_document, dict):
            raise TypeError("Expected argument 'policy_document' to be a dict")
        pulumi.set(__self__, "policy_document", policy_document)
        if policy_name and not isinstance(policy_name, str):
            raise TypeError("Expected argument 'policy_name' to be a str")
        pulumi.set(__self__, "policy_name", policy_name)
        if roles and not isinstance(roles, list):
            raise TypeError("Expected argument 'roles' to be a list")
        pulumi.set(__self__, "roles", roles)
        if users and not isinstance(users, list):
            raise TypeError("Expected argument 'users' to be a list")
        pulumi.set(__self__, "users", users)

    @property
    @pulumi.getter
    def groups(self) -> Optional[Sequence[str]]:
        """
        The name of the group to associate the policy with. This parameter allows (through its regex pattern) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-.
        """
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The provider-assigned unique ID for this resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[Any]:
        """
        The policy document. You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.
        """
        return pulumi.get(self, "policy_document")

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[str]:
        """
        The name of the policy document. This parameter allows (through its regex pattern) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        """
        return pulumi.get(self, "policy_name")

    @property
    @pulumi.getter
    def roles(self) -> Optional[Sequence[str]]:
        """
        The name of the role to associate the policy with. This parameter allows (per its regex pattern) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        """
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter
    def users(self) -> Optional[Sequence[str]]:
        """
        The name of the user to associate the policy with. This parameter allows (through its regex pattern) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        """
        return pulumi.get(self, "users")


class AwaitableGetPolicyResult(GetPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPolicyResult(
            groups=self.groups,
            id=self.id,
            policy_document=self.policy_document,
            policy_name=self.policy_name,
            roles=self.roles,
            users=self.users)


def get_policy(id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPolicyResult:
    """
    Resource Type definition for AWS::IAM::Policy


    :param str id: The provider-assigned unique ID for this resource
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:iam:getPolicy', __args__, opts=opts, typ=GetPolicyResult).value

    return AwaitableGetPolicyResult(
        groups=pulumi.get(__ret__, 'groups'),
        id=pulumi.get(__ret__, 'id'),
        policy_document=pulumi.get(__ret__, 'policy_document'),
        policy_name=pulumi.get(__ret__, 'policy_name'),
        roles=pulumi.get(__ret__, 'roles'),
        users=pulumi.get(__ret__, 'users'))


@_utilities.lift_output_func(get_policy)
def get_policy_output(id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPolicyResult]:
    """
    Resource Type definition for AWS::IAM::Policy


    :param str id: The provider-assigned unique ID for this resource
    """
    ...
