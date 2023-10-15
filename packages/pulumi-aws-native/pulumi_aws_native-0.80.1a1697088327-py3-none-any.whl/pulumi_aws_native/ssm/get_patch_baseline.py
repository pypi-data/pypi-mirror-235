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

__all__ = [
    'GetPatchBaselineResult',
    'AwaitableGetPatchBaselineResult',
    'get_patch_baseline',
    'get_patch_baseline_output',
]

@pulumi.output_type
class GetPatchBaselineResult:
    def __init__(__self__, approval_rules=None, approved_patches=None, approved_patches_compliance_level=None, approved_patches_enable_non_security=None, description=None, global_filters=None, id=None, name=None, patch_groups=None, rejected_patches=None, rejected_patches_action=None, sources=None, tags=None):
        if approval_rules and not isinstance(approval_rules, dict):
            raise TypeError("Expected argument 'approval_rules' to be a dict")
        pulumi.set(__self__, "approval_rules", approval_rules)
        if approved_patches and not isinstance(approved_patches, list):
            raise TypeError("Expected argument 'approved_patches' to be a list")
        pulumi.set(__self__, "approved_patches", approved_patches)
        if approved_patches_compliance_level and not isinstance(approved_patches_compliance_level, str):
            raise TypeError("Expected argument 'approved_patches_compliance_level' to be a str")
        pulumi.set(__self__, "approved_patches_compliance_level", approved_patches_compliance_level)
        if approved_patches_enable_non_security and not isinstance(approved_patches_enable_non_security, bool):
            raise TypeError("Expected argument 'approved_patches_enable_non_security' to be a bool")
        pulumi.set(__self__, "approved_patches_enable_non_security", approved_patches_enable_non_security)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if global_filters and not isinstance(global_filters, dict):
            raise TypeError("Expected argument 'global_filters' to be a dict")
        pulumi.set(__self__, "global_filters", global_filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if patch_groups and not isinstance(patch_groups, list):
            raise TypeError("Expected argument 'patch_groups' to be a list")
        pulumi.set(__self__, "patch_groups", patch_groups)
        if rejected_patches and not isinstance(rejected_patches, list):
            raise TypeError("Expected argument 'rejected_patches' to be a list")
        pulumi.set(__self__, "rejected_patches", rejected_patches)
        if rejected_patches_action and not isinstance(rejected_patches_action, str):
            raise TypeError("Expected argument 'rejected_patches_action' to be a str")
        pulumi.set(__self__, "rejected_patches_action", rejected_patches_action)
        if sources and not isinstance(sources, list):
            raise TypeError("Expected argument 'sources' to be a list")
        pulumi.set(__self__, "sources", sources)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="approvalRules")
    def approval_rules(self) -> Optional['outputs.PatchBaselineRuleGroup']:
        return pulumi.get(self, "approval_rules")

    @property
    @pulumi.getter(name="approvedPatches")
    def approved_patches(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "approved_patches")

    @property
    @pulumi.getter(name="approvedPatchesComplianceLevel")
    def approved_patches_compliance_level(self) -> Optional[str]:
        return pulumi.get(self, "approved_patches_compliance_level")

    @property
    @pulumi.getter(name="approvedPatchesEnableNonSecurity")
    def approved_patches_enable_non_security(self) -> Optional[bool]:
        return pulumi.get(self, "approved_patches_enable_non_security")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="globalFilters")
    def global_filters(self) -> Optional['outputs.PatchBaselinePatchFilterGroup']:
        return pulumi.get(self, "global_filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="patchGroups")
    def patch_groups(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "patch_groups")

    @property
    @pulumi.getter(name="rejectedPatches")
    def rejected_patches(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "rejected_patches")

    @property
    @pulumi.getter(name="rejectedPatchesAction")
    def rejected_patches_action(self) -> Optional[str]:
        return pulumi.get(self, "rejected_patches_action")

    @property
    @pulumi.getter
    def sources(self) -> Optional[Sequence['outputs.PatchBaselinePatchSource']]:
        return pulumi.get(self, "sources")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.PatchBaselineTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetPatchBaselineResult(GetPatchBaselineResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPatchBaselineResult(
            approval_rules=self.approval_rules,
            approved_patches=self.approved_patches,
            approved_patches_compliance_level=self.approved_patches_compliance_level,
            approved_patches_enable_non_security=self.approved_patches_enable_non_security,
            description=self.description,
            global_filters=self.global_filters,
            id=self.id,
            name=self.name,
            patch_groups=self.patch_groups,
            rejected_patches=self.rejected_patches,
            rejected_patches_action=self.rejected_patches_action,
            sources=self.sources,
            tags=self.tags)


def get_patch_baseline(id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPatchBaselineResult:
    """
    Resource Type definition for AWS::SSM::PatchBaseline
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ssm:getPatchBaseline', __args__, opts=opts, typ=GetPatchBaselineResult).value

    return AwaitableGetPatchBaselineResult(
        approval_rules=pulumi.get(__ret__, 'approval_rules'),
        approved_patches=pulumi.get(__ret__, 'approved_patches'),
        approved_patches_compliance_level=pulumi.get(__ret__, 'approved_patches_compliance_level'),
        approved_patches_enable_non_security=pulumi.get(__ret__, 'approved_patches_enable_non_security'),
        description=pulumi.get(__ret__, 'description'),
        global_filters=pulumi.get(__ret__, 'global_filters'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        patch_groups=pulumi.get(__ret__, 'patch_groups'),
        rejected_patches=pulumi.get(__ret__, 'rejected_patches'),
        rejected_patches_action=pulumi.get(__ret__, 'rejected_patches_action'),
        sources=pulumi.get(__ret__, 'sources'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_patch_baseline)
def get_patch_baseline_output(id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPatchBaselineResult]:
    """
    Resource Type definition for AWS::SSM::PatchBaseline
    """
    ...
