# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AddonResolveConflicts',
    'ClusterKubernetesNetworkConfigIpFamily',
    'ClusterLoggingTypeConfigType',
    'IdentityProviderConfigType',
]


class AddonResolveConflicts(str, Enum):
    """
    Resolve parameter value conflicts
    """
    NONE = "NONE"
    OVERWRITE = "OVERWRITE"
    PRESERVE = "PRESERVE"


class ClusterKubernetesNetworkConfigIpFamily(str, Enum):
    """
    Ipv4 or Ipv6. You can only specify ipv6 for 1.21 and later clusters that use version 1.10.1 or later of the Amazon VPC CNI add-on
    """
    IPV4 = "ipv4"
    IPV6 = "ipv6"


class ClusterLoggingTypeConfigType(str, Enum):
    """
    name of the log type
    """
    API = "api"
    AUDIT = "audit"
    AUTHENTICATOR = "authenticator"
    CONTROLLER_MANAGER = "controllerManager"
    SCHEDULER = "scheduler"


class IdentityProviderConfigType(str, Enum):
    """
    The type of the identity provider configuration.
    """
    OIDC = "oidc"
