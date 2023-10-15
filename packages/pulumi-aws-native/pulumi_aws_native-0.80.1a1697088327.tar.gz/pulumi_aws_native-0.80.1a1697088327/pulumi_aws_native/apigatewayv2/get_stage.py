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
    'GetStageResult',
    'AwaitableGetStageResult',
    'get_stage',
    'get_stage_output',
]

@pulumi.output_type
class GetStageResult:
    def __init__(__self__, access_log_settings=None, access_policy_id=None, auto_deploy=None, client_certificate_id=None, default_route_settings=None, deployment_id=None, description=None, id=None, route_settings=None, stage_variables=None, tags=None):
        if access_log_settings and not isinstance(access_log_settings, dict):
            raise TypeError("Expected argument 'access_log_settings' to be a dict")
        pulumi.set(__self__, "access_log_settings", access_log_settings)
        if access_policy_id and not isinstance(access_policy_id, str):
            raise TypeError("Expected argument 'access_policy_id' to be a str")
        pulumi.set(__self__, "access_policy_id", access_policy_id)
        if auto_deploy and not isinstance(auto_deploy, bool):
            raise TypeError("Expected argument 'auto_deploy' to be a bool")
        pulumi.set(__self__, "auto_deploy", auto_deploy)
        if client_certificate_id and not isinstance(client_certificate_id, str):
            raise TypeError("Expected argument 'client_certificate_id' to be a str")
        pulumi.set(__self__, "client_certificate_id", client_certificate_id)
        if default_route_settings and not isinstance(default_route_settings, dict):
            raise TypeError("Expected argument 'default_route_settings' to be a dict")
        pulumi.set(__self__, "default_route_settings", default_route_settings)
        if deployment_id and not isinstance(deployment_id, str):
            raise TypeError("Expected argument 'deployment_id' to be a str")
        pulumi.set(__self__, "deployment_id", deployment_id)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if route_settings and not isinstance(route_settings, dict):
            raise TypeError("Expected argument 'route_settings' to be a dict")
        pulumi.set(__self__, "route_settings", route_settings)
        if stage_variables and not isinstance(stage_variables, dict):
            raise TypeError("Expected argument 'stage_variables' to be a dict")
        pulumi.set(__self__, "stage_variables", stage_variables)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="accessLogSettings")
    def access_log_settings(self) -> Optional['outputs.StageAccessLogSettings']:
        return pulumi.get(self, "access_log_settings")

    @property
    @pulumi.getter(name="accessPolicyId")
    def access_policy_id(self) -> Optional[str]:
        return pulumi.get(self, "access_policy_id")

    @property
    @pulumi.getter(name="autoDeploy")
    def auto_deploy(self) -> Optional[bool]:
        return pulumi.get(self, "auto_deploy")

    @property
    @pulumi.getter(name="clientCertificateId")
    def client_certificate_id(self) -> Optional[str]:
        return pulumi.get(self, "client_certificate_id")

    @property
    @pulumi.getter(name="defaultRouteSettings")
    def default_route_settings(self) -> Optional['outputs.StageRouteSettings']:
        return pulumi.get(self, "default_route_settings")

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> Optional[str]:
        return pulumi.get(self, "deployment_id")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="routeSettings")
    def route_settings(self) -> Optional[Any]:
        return pulumi.get(self, "route_settings")

    @property
    @pulumi.getter(name="stageVariables")
    def stage_variables(self) -> Optional[Any]:
        return pulumi.get(self, "stage_variables")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        return pulumi.get(self, "tags")


class AwaitableGetStageResult(GetStageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStageResult(
            access_log_settings=self.access_log_settings,
            access_policy_id=self.access_policy_id,
            auto_deploy=self.auto_deploy,
            client_certificate_id=self.client_certificate_id,
            default_route_settings=self.default_route_settings,
            deployment_id=self.deployment_id,
            description=self.description,
            id=self.id,
            route_settings=self.route_settings,
            stage_variables=self.stage_variables,
            tags=self.tags)


def get_stage(id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStageResult:
    """
    Resource Type definition for AWS::ApiGatewayV2::Stage
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:apigatewayv2:getStage', __args__, opts=opts, typ=GetStageResult).value

    return AwaitableGetStageResult(
        access_log_settings=pulumi.get(__ret__, 'access_log_settings'),
        access_policy_id=pulumi.get(__ret__, 'access_policy_id'),
        auto_deploy=pulumi.get(__ret__, 'auto_deploy'),
        client_certificate_id=pulumi.get(__ret__, 'client_certificate_id'),
        default_route_settings=pulumi.get(__ret__, 'default_route_settings'),
        deployment_id=pulumi.get(__ret__, 'deployment_id'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        route_settings=pulumi.get(__ret__, 'route_settings'),
        stage_variables=pulumi.get(__ret__, 'stage_variables'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_stage)
def get_stage_output(id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStageResult]:
    """
    Resource Type definition for AWS::ApiGatewayV2::Stage
    """
    ...
