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
    'GetServerResult',
    'AwaitableGetServerResult',
    'get_server',
    'get_server_output',
]

@pulumi.output_type
class GetServerResult:
    def __init__(__self__, arn=None, certificate=None, endpoint_details=None, endpoint_type=None, identity_provider_details=None, logging_role=None, post_authentication_login_banner=None, pre_authentication_login_banner=None, protocol_details=None, protocols=None, security_policy_name=None, server_id=None, structured_log_destinations=None, tags=None, workflow_details=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if certificate and not isinstance(certificate, str):
            raise TypeError("Expected argument 'certificate' to be a str")
        pulumi.set(__self__, "certificate", certificate)
        if endpoint_details and not isinstance(endpoint_details, dict):
            raise TypeError("Expected argument 'endpoint_details' to be a dict")
        pulumi.set(__self__, "endpoint_details", endpoint_details)
        if endpoint_type and not isinstance(endpoint_type, str):
            raise TypeError("Expected argument 'endpoint_type' to be a str")
        pulumi.set(__self__, "endpoint_type", endpoint_type)
        if identity_provider_details and not isinstance(identity_provider_details, dict):
            raise TypeError("Expected argument 'identity_provider_details' to be a dict")
        pulumi.set(__self__, "identity_provider_details", identity_provider_details)
        if logging_role and not isinstance(logging_role, str):
            raise TypeError("Expected argument 'logging_role' to be a str")
        pulumi.set(__self__, "logging_role", logging_role)
        if post_authentication_login_banner and not isinstance(post_authentication_login_banner, str):
            raise TypeError("Expected argument 'post_authentication_login_banner' to be a str")
        pulumi.set(__self__, "post_authentication_login_banner", post_authentication_login_banner)
        if pre_authentication_login_banner and not isinstance(pre_authentication_login_banner, str):
            raise TypeError("Expected argument 'pre_authentication_login_banner' to be a str")
        pulumi.set(__self__, "pre_authentication_login_banner", pre_authentication_login_banner)
        if protocol_details and not isinstance(protocol_details, dict):
            raise TypeError("Expected argument 'protocol_details' to be a dict")
        pulumi.set(__self__, "protocol_details", protocol_details)
        if protocols and not isinstance(protocols, list):
            raise TypeError("Expected argument 'protocols' to be a list")
        pulumi.set(__self__, "protocols", protocols)
        if security_policy_name and not isinstance(security_policy_name, str):
            raise TypeError("Expected argument 'security_policy_name' to be a str")
        pulumi.set(__self__, "security_policy_name", security_policy_name)
        if server_id and not isinstance(server_id, str):
            raise TypeError("Expected argument 'server_id' to be a str")
        pulumi.set(__self__, "server_id", server_id)
        if structured_log_destinations and not isinstance(structured_log_destinations, list):
            raise TypeError("Expected argument 'structured_log_destinations' to be a list")
        pulumi.set(__self__, "structured_log_destinations", structured_log_destinations)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if workflow_details and not isinstance(workflow_details, dict):
            raise TypeError("Expected argument 'workflow_details' to be a dict")
        pulumi.set(__self__, "workflow_details", workflow_details)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def certificate(self) -> Optional[str]:
        return pulumi.get(self, "certificate")

    @property
    @pulumi.getter(name="endpointDetails")
    def endpoint_details(self) -> Optional['outputs.ServerEndpointDetails']:
        return pulumi.get(self, "endpoint_details")

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[str]:
        return pulumi.get(self, "endpoint_type")

    @property
    @pulumi.getter(name="identityProviderDetails")
    def identity_provider_details(self) -> Optional['outputs.ServerIdentityProviderDetails']:
        return pulumi.get(self, "identity_provider_details")

    @property
    @pulumi.getter(name="loggingRole")
    def logging_role(self) -> Optional[str]:
        return pulumi.get(self, "logging_role")

    @property
    @pulumi.getter(name="postAuthenticationLoginBanner")
    def post_authentication_login_banner(self) -> Optional[str]:
        return pulumi.get(self, "post_authentication_login_banner")

    @property
    @pulumi.getter(name="preAuthenticationLoginBanner")
    def pre_authentication_login_banner(self) -> Optional[str]:
        return pulumi.get(self, "pre_authentication_login_banner")

    @property
    @pulumi.getter(name="protocolDetails")
    def protocol_details(self) -> Optional['outputs.ServerProtocolDetails']:
        return pulumi.get(self, "protocol_details")

    @property
    @pulumi.getter
    def protocols(self) -> Optional[Sequence['outputs.ServerProtocol']]:
        return pulumi.get(self, "protocols")

    @property
    @pulumi.getter(name="securityPolicyName")
    def security_policy_name(self) -> Optional[str]:
        return pulumi.get(self, "security_policy_name")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> Optional[str]:
        return pulumi.get(self, "server_id")

    @property
    @pulumi.getter(name="structuredLogDestinations")
    def structured_log_destinations(self) -> Optional[Sequence['outputs.ServerStructuredLogDestination']]:
        return pulumi.get(self, "structured_log_destinations")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ServerTag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="workflowDetails")
    def workflow_details(self) -> Optional['outputs.ServerWorkflowDetails']:
        return pulumi.get(self, "workflow_details")


class AwaitableGetServerResult(GetServerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerResult(
            arn=self.arn,
            certificate=self.certificate,
            endpoint_details=self.endpoint_details,
            endpoint_type=self.endpoint_type,
            identity_provider_details=self.identity_provider_details,
            logging_role=self.logging_role,
            post_authentication_login_banner=self.post_authentication_login_banner,
            pre_authentication_login_banner=self.pre_authentication_login_banner,
            protocol_details=self.protocol_details,
            protocols=self.protocols,
            security_policy_name=self.security_policy_name,
            server_id=self.server_id,
            structured_log_destinations=self.structured_log_destinations,
            tags=self.tags,
            workflow_details=self.workflow_details)


def get_server(server_id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerResult:
    """
    Resource Type definition for AWS::Transfer::Server
    """
    __args__ = dict()
    __args__['serverId'] = server_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:transfer:getServer', __args__, opts=opts, typ=GetServerResult).value

    return AwaitableGetServerResult(
        arn=pulumi.get(__ret__, 'arn'),
        certificate=pulumi.get(__ret__, 'certificate'),
        endpoint_details=pulumi.get(__ret__, 'endpoint_details'),
        endpoint_type=pulumi.get(__ret__, 'endpoint_type'),
        identity_provider_details=pulumi.get(__ret__, 'identity_provider_details'),
        logging_role=pulumi.get(__ret__, 'logging_role'),
        post_authentication_login_banner=pulumi.get(__ret__, 'post_authentication_login_banner'),
        pre_authentication_login_banner=pulumi.get(__ret__, 'pre_authentication_login_banner'),
        protocol_details=pulumi.get(__ret__, 'protocol_details'),
        protocols=pulumi.get(__ret__, 'protocols'),
        security_policy_name=pulumi.get(__ret__, 'security_policy_name'),
        server_id=pulumi.get(__ret__, 'server_id'),
        structured_log_destinations=pulumi.get(__ret__, 'structured_log_destinations'),
        tags=pulumi.get(__ret__, 'tags'),
        workflow_details=pulumi.get(__ret__, 'workflow_details'))


@_utilities.lift_output_func(get_server)
def get_server_output(server_id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServerResult]:
    """
    Resource Type definition for AWS::Transfer::Server
    """
    ...
