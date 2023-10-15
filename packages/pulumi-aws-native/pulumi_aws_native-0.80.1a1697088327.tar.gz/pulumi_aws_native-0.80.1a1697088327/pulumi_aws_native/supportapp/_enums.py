# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'SlackChannelConfigurationNotifyOnCaseSeverity',
]


class SlackChannelConfigurationNotifyOnCaseSeverity(str, Enum):
    """
    The severity level of a support case that a customer wants to get notified for.
    """
    NONE = "none"
    ALL = "all"
    HIGH = "high"
