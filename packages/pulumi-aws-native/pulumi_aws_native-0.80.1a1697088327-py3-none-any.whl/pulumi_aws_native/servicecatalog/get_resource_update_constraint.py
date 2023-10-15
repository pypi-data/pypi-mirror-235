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
    'GetResourceUpdateConstraintResult',
    'AwaitableGetResourceUpdateConstraintResult',
    'get_resource_update_constraint',
    'get_resource_update_constraint_output',
]

@pulumi.output_type
class GetResourceUpdateConstraintResult:
    def __init__(__self__, accept_language=None, description=None, id=None, tag_update_on_provisioned_product=None):
        if accept_language and not isinstance(accept_language, str):
            raise TypeError("Expected argument 'accept_language' to be a str")
        pulumi.set(__self__, "accept_language", accept_language)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if tag_update_on_provisioned_product and not isinstance(tag_update_on_provisioned_product, str):
            raise TypeError("Expected argument 'tag_update_on_provisioned_product' to be a str")
        pulumi.set(__self__, "tag_update_on_provisioned_product", tag_update_on_provisioned_product)

    @property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[str]:
        return pulumi.get(self, "accept_language")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="tagUpdateOnProvisionedProduct")
    def tag_update_on_provisioned_product(self) -> Optional[str]:
        return pulumi.get(self, "tag_update_on_provisioned_product")


class AwaitableGetResourceUpdateConstraintResult(GetResourceUpdateConstraintResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResourceUpdateConstraintResult(
            accept_language=self.accept_language,
            description=self.description,
            id=self.id,
            tag_update_on_provisioned_product=self.tag_update_on_provisioned_product)


def get_resource_update_constraint(id: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResourceUpdateConstraintResult:
    """
    Resource Type definition for AWS::ServiceCatalog::ResourceUpdateConstraint
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:servicecatalog:getResourceUpdateConstraint', __args__, opts=opts, typ=GetResourceUpdateConstraintResult).value

    return AwaitableGetResourceUpdateConstraintResult(
        accept_language=pulumi.get(__ret__, 'accept_language'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        tag_update_on_provisioned_product=pulumi.get(__ret__, 'tag_update_on_provisioned_product'))


@_utilities.lift_output_func(get_resource_update_constraint)
def get_resource_update_constraint_output(id: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResourceUpdateConstraintResult]:
    """
    Resource Type definition for AWS::ServiceCatalog::ResourceUpdateConstraint
    """
    ...
