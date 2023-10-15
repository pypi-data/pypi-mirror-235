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
    'WorkspaceAssertionAttributesArgs',
    'WorkspaceIdpMetadataArgs',
    'WorkspaceNetworkAccessControlArgs',
    'WorkspaceRoleValuesArgs',
    'WorkspaceSamlConfigurationArgs',
    'WorkspaceVpcConfigurationArgs',
]

@pulumi.input_type
class WorkspaceAssertionAttributesArgs:
    def __init__(__self__, *,
                 email: Optional[pulumi.Input[str]] = None,
                 groups: Optional[pulumi.Input[str]] = None,
                 login: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None):
        """
        Maps Grafana friendly names to the IdPs SAML attributes.
        :param pulumi.Input[str] email: Name of the attribute within the SAML assert to use as the users email in Grafana.
        :param pulumi.Input[str] groups: Name of the attribute within the SAML assert to use as the users groups in Grafana.
        :param pulumi.Input[str] login: Name of the attribute within the SAML assert to use as the users login handle in Grafana.
        :param pulumi.Input[str] name: Name of the attribute within the SAML assert to use as the users name in Grafana.
        :param pulumi.Input[str] org: Name of the attribute within the SAML assert to use as the users organizations in Grafana.
        :param pulumi.Input[str] role: Name of the attribute within the SAML assert to use as the users roles in Grafana.
        """
        WorkspaceAssertionAttributesArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            email=email,
            groups=groups,
            login=login,
            name=name,
            org=org,
            role=role,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             email: Optional[pulumi.Input[str]] = None,
             groups: Optional[pulumi.Input[str]] = None,
             login: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             org: Optional[pulumi.Input[str]] = None,
             role: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if email is not None:
            _setter("email", email)
        if groups is not None:
            _setter("groups", groups)
        if login is not None:
            _setter("login", login)
        if name is not None:
            _setter("name", name)
        if org is not None:
            _setter("org", org)
        if role is not None:
            _setter("role", role)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the attribute within the SAML assert to use as the users email in Grafana.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter
    def groups(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the attribute within the SAML assert to use as the users groups in Grafana.
        """
        return pulumi.get(self, "groups")

    @groups.setter
    def groups(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "groups", value)

    @property
    @pulumi.getter
    def login(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the attribute within the SAML assert to use as the users login handle in Grafana.
        """
        return pulumi.get(self, "login")

    @login.setter
    def login(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "login", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the attribute within the SAML assert to use as the users name in Grafana.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def org(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the attribute within the SAML assert to use as the users organizations in Grafana.
        """
        return pulumi.get(self, "org")

    @org.setter
    def org(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the attribute within the SAML assert to use as the users roles in Grafana.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)


@pulumi.input_type
class WorkspaceIdpMetadataArgs:
    def __init__(__self__, *,
                 url: Optional[pulumi.Input[str]] = None,
                 xml: Optional[pulumi.Input[str]] = None):
        """
        IdP Metadata used to configure SAML authentication in Grafana.
        :param pulumi.Input[str] url: URL that vends the IdPs metadata.
        :param pulumi.Input[str] xml: XML blob of the IdPs metadata.
        """
        WorkspaceIdpMetadataArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            url=url,
            xml=xml,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             url: Optional[pulumi.Input[str]] = None,
             xml: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if url is not None:
            _setter("url", url)
        if xml is not None:
            _setter("xml", xml)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        URL that vends the IdPs metadata.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter
    def xml(self) -> Optional[pulumi.Input[str]]:
        """
        XML blob of the IdPs metadata.
        """
        return pulumi.get(self, "xml")

    @xml.setter
    def xml(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "xml", value)


@pulumi.input_type
class WorkspaceNetworkAccessControlArgs:
    def __init__(__self__, *,
                 prefix_list_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vpce_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The configuration settings for Network Access Control.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] prefix_list_ids: The list of prefix list IDs. A prefix list is a list of CIDR ranges of IP addresses. The IP addresses specified are allowed to access your workspace. If the list is not included in the configuration then no IP addresses will be allowed to access the workspace.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] vpce_ids: The list of Amazon VPC endpoint IDs for the workspace. If a NetworkAccessConfiguration is specified then only VPC endpoints specified here will be allowed to access the workspace.
        """
        WorkspaceNetworkAccessControlArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            prefix_list_ids=prefix_list_ids,
            vpce_ids=vpce_ids,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             prefix_list_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             vpce_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if prefix_list_ids is not None:
            _setter("prefix_list_ids", prefix_list_ids)
        if vpce_ids is not None:
            _setter("vpce_ids", vpce_ids)

    @property
    @pulumi.getter(name="prefixListIds")
    def prefix_list_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of prefix list IDs. A prefix list is a list of CIDR ranges of IP addresses. The IP addresses specified are allowed to access your workspace. If the list is not included in the configuration then no IP addresses will be allowed to access the workspace.
        """
        return pulumi.get(self, "prefix_list_ids")

    @prefix_list_ids.setter
    def prefix_list_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "prefix_list_ids", value)

    @property
    @pulumi.getter(name="vpceIds")
    def vpce_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of Amazon VPC endpoint IDs for the workspace. If a NetworkAccessConfiguration is specified then only VPC endpoints specified here will be allowed to access the workspace.
        """
        return pulumi.get(self, "vpce_ids")

    @vpce_ids.setter
    def vpce_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "vpce_ids", value)


@pulumi.input_type
class WorkspaceRoleValuesArgs:
    def __init__(__self__, *,
                 admin: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 editor: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Maps SAML roles to the Grafana Editor and Admin roles.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] admin: List of SAML roles which will be mapped into the Grafana Admin role.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] editor: List of SAML roles which will be mapped into the Grafana Editor role.
        """
        WorkspaceRoleValuesArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            admin=admin,
            editor=editor,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             admin: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             editor: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if admin is not None:
            _setter("admin", admin)
        if editor is not None:
            _setter("editor", editor)

    @property
    @pulumi.getter
    def admin(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of SAML roles which will be mapped into the Grafana Admin role.
        """
        return pulumi.get(self, "admin")

    @admin.setter
    def admin(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "admin", value)

    @property
    @pulumi.getter
    def editor(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of SAML roles which will be mapped into the Grafana Editor role.
        """
        return pulumi.get(self, "editor")

    @editor.setter
    def editor(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "editor", value)


@pulumi.input_type
class WorkspaceSamlConfigurationArgs:
    def __init__(__self__, *,
                 idp_metadata: pulumi.Input['WorkspaceIdpMetadataArgs'],
                 allowed_organizations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 assertion_attributes: Optional[pulumi.Input['WorkspaceAssertionAttributesArgs']] = None,
                 login_validity_duration: Optional[pulumi.Input[float]] = None,
                 role_values: Optional[pulumi.Input['WorkspaceRoleValuesArgs']] = None):
        """
        SAML configuration data associated with an AMG workspace.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_organizations: List of SAML organizations allowed to access Grafana.
        :param pulumi.Input[float] login_validity_duration: The maximum lifetime an authenticated user can be logged in (in minutes) before being required to re-authenticate.
        """
        WorkspaceSamlConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            idp_metadata=idp_metadata,
            allowed_organizations=allowed_organizations,
            assertion_attributes=assertion_attributes,
            login_validity_duration=login_validity_duration,
            role_values=role_values,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             idp_metadata: pulumi.Input['WorkspaceIdpMetadataArgs'],
             allowed_organizations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             assertion_attributes: Optional[pulumi.Input['WorkspaceAssertionAttributesArgs']] = None,
             login_validity_duration: Optional[pulumi.Input[float]] = None,
             role_values: Optional[pulumi.Input['WorkspaceRoleValuesArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("idp_metadata", idp_metadata)
        if allowed_organizations is not None:
            _setter("allowed_organizations", allowed_organizations)
        if assertion_attributes is not None:
            _setter("assertion_attributes", assertion_attributes)
        if login_validity_duration is not None:
            _setter("login_validity_duration", login_validity_duration)
        if role_values is not None:
            _setter("role_values", role_values)

    @property
    @pulumi.getter(name="idpMetadata")
    def idp_metadata(self) -> pulumi.Input['WorkspaceIdpMetadataArgs']:
        return pulumi.get(self, "idp_metadata")

    @idp_metadata.setter
    def idp_metadata(self, value: pulumi.Input['WorkspaceIdpMetadataArgs']):
        pulumi.set(self, "idp_metadata", value)

    @property
    @pulumi.getter(name="allowedOrganizations")
    def allowed_organizations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of SAML organizations allowed to access Grafana.
        """
        return pulumi.get(self, "allowed_organizations")

    @allowed_organizations.setter
    def allowed_organizations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowed_organizations", value)

    @property
    @pulumi.getter(name="assertionAttributes")
    def assertion_attributes(self) -> Optional[pulumi.Input['WorkspaceAssertionAttributesArgs']]:
        return pulumi.get(self, "assertion_attributes")

    @assertion_attributes.setter
    def assertion_attributes(self, value: Optional[pulumi.Input['WorkspaceAssertionAttributesArgs']]):
        pulumi.set(self, "assertion_attributes", value)

    @property
    @pulumi.getter(name="loginValidityDuration")
    def login_validity_duration(self) -> Optional[pulumi.Input[float]]:
        """
        The maximum lifetime an authenticated user can be logged in (in minutes) before being required to re-authenticate.
        """
        return pulumi.get(self, "login_validity_duration")

    @login_validity_duration.setter
    def login_validity_duration(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "login_validity_duration", value)

    @property
    @pulumi.getter(name="roleValues")
    def role_values(self) -> Optional[pulumi.Input['WorkspaceRoleValuesArgs']]:
        return pulumi.get(self, "role_values")

    @role_values.setter
    def role_values(self, value: Optional[pulumi.Input['WorkspaceRoleValuesArgs']]):
        pulumi.set(self, "role_values", value)


@pulumi.input_type
class WorkspaceVpcConfigurationArgs:
    def __init__(__self__, *,
                 security_group_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 subnet_ids: pulumi.Input[Sequence[pulumi.Input[str]]]):
        """
        The configuration settings for an Amazon VPC that contains data sources for your Grafana workspace to connect to.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: The list of Amazon EC2 security group IDs attached to the Amazon VPC for your Grafana workspace to connect.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: The list of Amazon EC2 subnet IDs created in the Amazon VPC for your Grafana workspace to connect.
        """
        WorkspaceVpcConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            security_group_ids=security_group_ids,
            subnet_ids=subnet_ids,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             security_group_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
             subnet_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("security_group_ids", security_group_ids)
        _setter("subnet_ids", subnet_ids)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The list of Amazon EC2 security group IDs attached to the Amazon VPC for your Grafana workspace to connect.
        """
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The list of Amazon EC2 subnet IDs created in the Amazon VPC for your Grafana workspace to connect.
        """
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "subnet_ids", value)


