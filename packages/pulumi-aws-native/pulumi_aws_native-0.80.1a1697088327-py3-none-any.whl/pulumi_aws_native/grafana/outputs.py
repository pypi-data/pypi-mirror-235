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
    'WorkspaceAssertionAttributes',
    'WorkspaceIdpMetadata',
    'WorkspaceNetworkAccessControl',
    'WorkspaceRoleValues',
    'WorkspaceSamlConfiguration',
    'WorkspaceVpcConfiguration',
]

@pulumi.output_type
class WorkspaceAssertionAttributes(dict):
    """
    Maps Grafana friendly names to the IdPs SAML attributes.
    """
    def __init__(__self__, *,
                 email: Optional[str] = None,
                 groups: Optional[str] = None,
                 login: Optional[str] = None,
                 name: Optional[str] = None,
                 org: Optional[str] = None,
                 role: Optional[str] = None):
        """
        Maps Grafana friendly names to the IdPs SAML attributes.
        :param str email: Name of the attribute within the SAML assert to use as the users email in Grafana.
        :param str groups: Name of the attribute within the SAML assert to use as the users groups in Grafana.
        :param str login: Name of the attribute within the SAML assert to use as the users login handle in Grafana.
        :param str name: Name of the attribute within the SAML assert to use as the users name in Grafana.
        :param str org: Name of the attribute within the SAML assert to use as the users organizations in Grafana.
        :param str role: Name of the attribute within the SAML assert to use as the users roles in Grafana.
        """
        WorkspaceAssertionAttributes._configure(
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
             email: Optional[str] = None,
             groups: Optional[str] = None,
             login: Optional[str] = None,
             name: Optional[str] = None,
             org: Optional[str] = None,
             role: Optional[str] = None,
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
    def email(self) -> Optional[str]:
        """
        Name of the attribute within the SAML assert to use as the users email in Grafana.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def groups(self) -> Optional[str]:
        """
        Name of the attribute within the SAML assert to use as the users groups in Grafana.
        """
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter
    def login(self) -> Optional[str]:
        """
        Name of the attribute within the SAML assert to use as the users login handle in Grafana.
        """
        return pulumi.get(self, "login")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the attribute within the SAML assert to use as the users name in Grafana.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def org(self) -> Optional[str]:
        """
        Name of the attribute within the SAML assert to use as the users organizations in Grafana.
        """
        return pulumi.get(self, "org")

    @property
    @pulumi.getter
    def role(self) -> Optional[str]:
        """
        Name of the attribute within the SAML assert to use as the users roles in Grafana.
        """
        return pulumi.get(self, "role")


@pulumi.output_type
class WorkspaceIdpMetadata(dict):
    """
    IdP Metadata used to configure SAML authentication in Grafana.
    """
    def __init__(__self__, *,
                 url: Optional[str] = None,
                 xml: Optional[str] = None):
        """
        IdP Metadata used to configure SAML authentication in Grafana.
        :param str url: URL that vends the IdPs metadata.
        :param str xml: XML blob of the IdPs metadata.
        """
        WorkspaceIdpMetadata._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            url=url,
            xml=xml,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             url: Optional[str] = None,
             xml: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if url is not None:
            _setter("url", url)
        if xml is not None:
            _setter("xml", xml)

    @property
    @pulumi.getter
    def url(self) -> Optional[str]:
        """
        URL that vends the IdPs metadata.
        """
        return pulumi.get(self, "url")

    @property
    @pulumi.getter
    def xml(self) -> Optional[str]:
        """
        XML blob of the IdPs metadata.
        """
        return pulumi.get(self, "xml")


@pulumi.output_type
class WorkspaceNetworkAccessControl(dict):
    """
    The configuration settings for Network Access Control.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "prefixListIds":
            suggest = "prefix_list_ids"
        elif key == "vpceIds":
            suggest = "vpce_ids"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WorkspaceNetworkAccessControl. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WorkspaceNetworkAccessControl.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WorkspaceNetworkAccessControl.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 prefix_list_ids: Optional[Sequence[str]] = None,
                 vpce_ids: Optional[Sequence[str]] = None):
        """
        The configuration settings for Network Access Control.
        :param Sequence[str] prefix_list_ids: The list of prefix list IDs. A prefix list is a list of CIDR ranges of IP addresses. The IP addresses specified are allowed to access your workspace. If the list is not included in the configuration then no IP addresses will be allowed to access the workspace.
        :param Sequence[str] vpce_ids: The list of Amazon VPC endpoint IDs for the workspace. If a NetworkAccessConfiguration is specified then only VPC endpoints specified here will be allowed to access the workspace.
        """
        WorkspaceNetworkAccessControl._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            prefix_list_ids=prefix_list_ids,
            vpce_ids=vpce_ids,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             prefix_list_ids: Optional[Sequence[str]] = None,
             vpce_ids: Optional[Sequence[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if prefix_list_ids is not None:
            _setter("prefix_list_ids", prefix_list_ids)
        if vpce_ids is not None:
            _setter("vpce_ids", vpce_ids)

    @property
    @pulumi.getter(name="prefixListIds")
    def prefix_list_ids(self) -> Optional[Sequence[str]]:
        """
        The list of prefix list IDs. A prefix list is a list of CIDR ranges of IP addresses. The IP addresses specified are allowed to access your workspace. If the list is not included in the configuration then no IP addresses will be allowed to access the workspace.
        """
        return pulumi.get(self, "prefix_list_ids")

    @property
    @pulumi.getter(name="vpceIds")
    def vpce_ids(self) -> Optional[Sequence[str]]:
        """
        The list of Amazon VPC endpoint IDs for the workspace. If a NetworkAccessConfiguration is specified then only VPC endpoints specified here will be allowed to access the workspace.
        """
        return pulumi.get(self, "vpce_ids")


@pulumi.output_type
class WorkspaceRoleValues(dict):
    """
    Maps SAML roles to the Grafana Editor and Admin roles.
    """
    def __init__(__self__, *,
                 admin: Optional[Sequence[str]] = None,
                 editor: Optional[Sequence[str]] = None):
        """
        Maps SAML roles to the Grafana Editor and Admin roles.
        :param Sequence[str] admin: List of SAML roles which will be mapped into the Grafana Admin role.
        :param Sequence[str] editor: List of SAML roles which will be mapped into the Grafana Editor role.
        """
        WorkspaceRoleValues._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            admin=admin,
            editor=editor,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             admin: Optional[Sequence[str]] = None,
             editor: Optional[Sequence[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if admin is not None:
            _setter("admin", admin)
        if editor is not None:
            _setter("editor", editor)

    @property
    @pulumi.getter
    def admin(self) -> Optional[Sequence[str]]:
        """
        List of SAML roles which will be mapped into the Grafana Admin role.
        """
        return pulumi.get(self, "admin")

    @property
    @pulumi.getter
    def editor(self) -> Optional[Sequence[str]]:
        """
        List of SAML roles which will be mapped into the Grafana Editor role.
        """
        return pulumi.get(self, "editor")


@pulumi.output_type
class WorkspaceSamlConfiguration(dict):
    """
    SAML configuration data associated with an AMG workspace.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "idpMetadata":
            suggest = "idp_metadata"
        elif key == "allowedOrganizations":
            suggest = "allowed_organizations"
        elif key == "assertionAttributes":
            suggest = "assertion_attributes"
        elif key == "loginValidityDuration":
            suggest = "login_validity_duration"
        elif key == "roleValues":
            suggest = "role_values"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WorkspaceSamlConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WorkspaceSamlConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WorkspaceSamlConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 idp_metadata: 'outputs.WorkspaceIdpMetadata',
                 allowed_organizations: Optional[Sequence[str]] = None,
                 assertion_attributes: Optional['outputs.WorkspaceAssertionAttributes'] = None,
                 login_validity_duration: Optional[float] = None,
                 role_values: Optional['outputs.WorkspaceRoleValues'] = None):
        """
        SAML configuration data associated with an AMG workspace.
        :param Sequence[str] allowed_organizations: List of SAML organizations allowed to access Grafana.
        :param float login_validity_duration: The maximum lifetime an authenticated user can be logged in (in minutes) before being required to re-authenticate.
        """
        WorkspaceSamlConfiguration._configure(
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
             idp_metadata: 'outputs.WorkspaceIdpMetadata',
             allowed_organizations: Optional[Sequence[str]] = None,
             assertion_attributes: Optional['outputs.WorkspaceAssertionAttributes'] = None,
             login_validity_duration: Optional[float] = None,
             role_values: Optional['outputs.WorkspaceRoleValues'] = None,
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
    def idp_metadata(self) -> 'outputs.WorkspaceIdpMetadata':
        return pulumi.get(self, "idp_metadata")

    @property
    @pulumi.getter(name="allowedOrganizations")
    def allowed_organizations(self) -> Optional[Sequence[str]]:
        """
        List of SAML organizations allowed to access Grafana.
        """
        return pulumi.get(self, "allowed_organizations")

    @property
    @pulumi.getter(name="assertionAttributes")
    def assertion_attributes(self) -> Optional['outputs.WorkspaceAssertionAttributes']:
        return pulumi.get(self, "assertion_attributes")

    @property
    @pulumi.getter(name="loginValidityDuration")
    def login_validity_duration(self) -> Optional[float]:
        """
        The maximum lifetime an authenticated user can be logged in (in minutes) before being required to re-authenticate.
        """
        return pulumi.get(self, "login_validity_duration")

    @property
    @pulumi.getter(name="roleValues")
    def role_values(self) -> Optional['outputs.WorkspaceRoleValues']:
        return pulumi.get(self, "role_values")


@pulumi.output_type
class WorkspaceVpcConfiguration(dict):
    """
    The configuration settings for an Amazon VPC that contains data sources for your Grafana workspace to connect to.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "securityGroupIds":
            suggest = "security_group_ids"
        elif key == "subnetIds":
            suggest = "subnet_ids"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WorkspaceVpcConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WorkspaceVpcConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WorkspaceVpcConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 security_group_ids: Sequence[str],
                 subnet_ids: Sequence[str]):
        """
        The configuration settings for an Amazon VPC that contains data sources for your Grafana workspace to connect to.
        :param Sequence[str] security_group_ids: The list of Amazon EC2 security group IDs attached to the Amazon VPC for your Grafana workspace to connect.
        :param Sequence[str] subnet_ids: The list of Amazon EC2 subnet IDs created in the Amazon VPC for your Grafana workspace to connect.
        """
        WorkspaceVpcConfiguration._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            security_group_ids=security_group_ids,
            subnet_ids=subnet_ids,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             security_group_ids: Sequence[str],
             subnet_ids: Sequence[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("security_group_ids", security_group_ids)
        _setter("subnet_ids", subnet_ids)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[str]:
        """
        The list of Amazon EC2 security group IDs attached to the Amazon VPC for your Grafana workspace to connect.
        """
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[str]:
        """
        The list of Amazon EC2 subnet IDs created in the Amazon VPC for your Grafana workspace to connect.
        """
        return pulumi.get(self, "subnet_ids")


