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
    'RotationScheduleHostedRotationLambdaArgs',
    'RotationScheduleRotationRulesArgs',
    'SecretGenerateSecretStringArgs',
    'SecretReplicaRegionArgs',
    'SecretTagArgs',
]

@pulumi.input_type
class RotationScheduleHostedRotationLambdaArgs:
    def __init__(__self__, *,
                 rotation_type: pulumi.Input[str],
                 exclude_characters: Optional[pulumi.Input[str]] = None,
                 kms_key_arn: Optional[pulumi.Input[str]] = None,
                 master_secret_arn: Optional[pulumi.Input[str]] = None,
                 master_secret_kms_key_arn: Optional[pulumi.Input[str]] = None,
                 rotation_lambda_name: Optional[pulumi.Input[str]] = None,
                 runtime: Optional[pulumi.Input[str]] = None,
                 superuser_secret_arn: Optional[pulumi.Input[str]] = None,
                 superuser_secret_kms_key_arn: Optional[pulumi.Input[str]] = None,
                 vpc_security_group_ids: Optional[pulumi.Input[str]] = None,
                 vpc_subnet_ids: Optional[pulumi.Input[str]] = None):
        RotationScheduleHostedRotationLambdaArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            rotation_type=rotation_type,
            exclude_characters=exclude_characters,
            kms_key_arn=kms_key_arn,
            master_secret_arn=master_secret_arn,
            master_secret_kms_key_arn=master_secret_kms_key_arn,
            rotation_lambda_name=rotation_lambda_name,
            runtime=runtime,
            superuser_secret_arn=superuser_secret_arn,
            superuser_secret_kms_key_arn=superuser_secret_kms_key_arn,
            vpc_security_group_ids=vpc_security_group_ids,
            vpc_subnet_ids=vpc_subnet_ids,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             rotation_type: pulumi.Input[str],
             exclude_characters: Optional[pulumi.Input[str]] = None,
             kms_key_arn: Optional[pulumi.Input[str]] = None,
             master_secret_arn: Optional[pulumi.Input[str]] = None,
             master_secret_kms_key_arn: Optional[pulumi.Input[str]] = None,
             rotation_lambda_name: Optional[pulumi.Input[str]] = None,
             runtime: Optional[pulumi.Input[str]] = None,
             superuser_secret_arn: Optional[pulumi.Input[str]] = None,
             superuser_secret_kms_key_arn: Optional[pulumi.Input[str]] = None,
             vpc_security_group_ids: Optional[pulumi.Input[str]] = None,
             vpc_subnet_ids: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("rotation_type", rotation_type)
        if exclude_characters is not None:
            _setter("exclude_characters", exclude_characters)
        if kms_key_arn is not None:
            _setter("kms_key_arn", kms_key_arn)
        if master_secret_arn is not None:
            _setter("master_secret_arn", master_secret_arn)
        if master_secret_kms_key_arn is not None:
            _setter("master_secret_kms_key_arn", master_secret_kms_key_arn)
        if rotation_lambda_name is not None:
            _setter("rotation_lambda_name", rotation_lambda_name)
        if runtime is not None:
            _setter("runtime", runtime)
        if superuser_secret_arn is not None:
            _setter("superuser_secret_arn", superuser_secret_arn)
        if superuser_secret_kms_key_arn is not None:
            _setter("superuser_secret_kms_key_arn", superuser_secret_kms_key_arn)
        if vpc_security_group_ids is not None:
            _setter("vpc_security_group_ids", vpc_security_group_ids)
        if vpc_subnet_ids is not None:
            _setter("vpc_subnet_ids", vpc_subnet_ids)

    @property
    @pulumi.getter(name="rotationType")
    def rotation_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "rotation_type")

    @rotation_type.setter
    def rotation_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "rotation_type", value)

    @property
    @pulumi.getter(name="excludeCharacters")
    def exclude_characters(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "exclude_characters")

    @exclude_characters.setter
    def exclude_characters(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "exclude_characters", value)

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "kms_key_arn")

    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_arn", value)

    @property
    @pulumi.getter(name="masterSecretArn")
    def master_secret_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "master_secret_arn")

    @master_secret_arn.setter
    def master_secret_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "master_secret_arn", value)

    @property
    @pulumi.getter(name="masterSecretKmsKeyArn")
    def master_secret_kms_key_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "master_secret_kms_key_arn")

    @master_secret_kms_key_arn.setter
    def master_secret_kms_key_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "master_secret_kms_key_arn", value)

    @property
    @pulumi.getter(name="rotationLambdaName")
    def rotation_lambda_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "rotation_lambda_name")

    @rotation_lambda_name.setter
    def rotation_lambda_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rotation_lambda_name", value)

    @property
    @pulumi.getter
    def runtime(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "runtime")

    @runtime.setter
    def runtime(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "runtime", value)

    @property
    @pulumi.getter(name="superuserSecretArn")
    def superuser_secret_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "superuser_secret_arn")

    @superuser_secret_arn.setter
    def superuser_secret_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "superuser_secret_arn", value)

    @property
    @pulumi.getter(name="superuserSecretKmsKeyArn")
    def superuser_secret_kms_key_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "superuser_secret_kms_key_arn")

    @superuser_secret_kms_key_arn.setter
    def superuser_secret_kms_key_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "superuser_secret_kms_key_arn", value)

    @property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "vpc_security_group_ids")

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_security_group_ids", value)

    @property
    @pulumi.getter(name="vpcSubnetIds")
    def vpc_subnet_ids(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "vpc_subnet_ids")

    @vpc_subnet_ids.setter
    def vpc_subnet_ids(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_subnet_ids", value)


@pulumi.input_type
class RotationScheduleRotationRulesArgs:
    def __init__(__self__, *,
                 automatically_after_days: Optional[pulumi.Input[int]] = None,
                 duration: Optional[pulumi.Input[str]] = None,
                 schedule_expression: Optional[pulumi.Input[str]] = None):
        RotationScheduleRotationRulesArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            automatically_after_days=automatically_after_days,
            duration=duration,
            schedule_expression=schedule_expression,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             automatically_after_days: Optional[pulumi.Input[int]] = None,
             duration: Optional[pulumi.Input[str]] = None,
             schedule_expression: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if automatically_after_days is not None:
            _setter("automatically_after_days", automatically_after_days)
        if duration is not None:
            _setter("duration", duration)
        if schedule_expression is not None:
            _setter("schedule_expression", schedule_expression)

    @property
    @pulumi.getter(name="automaticallyAfterDays")
    def automatically_after_days(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "automatically_after_days")

    @automatically_after_days.setter
    def automatically_after_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "automatically_after_days", value)

    @property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "duration")

    @duration.setter
    def duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "duration", value)

    @property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "schedule_expression")

    @schedule_expression.setter
    def schedule_expression(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schedule_expression", value)


@pulumi.input_type
class SecretGenerateSecretStringArgs:
    def __init__(__self__, *,
                 exclude_characters: Optional[pulumi.Input[str]] = None,
                 exclude_lowercase: Optional[pulumi.Input[bool]] = None,
                 exclude_numbers: Optional[pulumi.Input[bool]] = None,
                 exclude_punctuation: Optional[pulumi.Input[bool]] = None,
                 exclude_uppercase: Optional[pulumi.Input[bool]] = None,
                 generate_string_key: Optional[pulumi.Input[str]] = None,
                 include_space: Optional[pulumi.Input[bool]] = None,
                 password_length: Optional[pulumi.Input[int]] = None,
                 require_each_included_type: Optional[pulumi.Input[bool]] = None,
                 secret_string_template: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] exclude_characters: A string that excludes characters in the generated password. By default, all characters from the included sets can be used. The string can be a minimum length of 0 characters and a maximum length of 7168 characters. 
        :param pulumi.Input[bool] exclude_lowercase: Specifies the generated password should not include lowercase letters. By default, ecrets Manager disables this parameter, and the generated password can include lowercase False, and the generated password can include lowercase letters.
        :param pulumi.Input[bool] exclude_numbers: Specifies that the generated password should exclude digits. By default, Secrets Manager does not enable the parameter, False, and the generated password can include digits.
        :param pulumi.Input[bool] exclude_punctuation: Specifies that the generated password should not include punctuation characters. The default if you do not include this switch parameter is that punctuation characters can be included. 
        :param pulumi.Input[bool] exclude_uppercase: Specifies that the generated password should not include uppercase letters. The default behavior is False, and the generated password can include uppercase letters. 
        :param pulumi.Input[str] generate_string_key: The JSON key name used to add the generated password to the JSON structure specified by the SecretStringTemplate parameter. If you specify this parameter, then you must also specify SecretStringTemplate. 
        :param pulumi.Input[bool] include_space: Specifies that the generated password can include the space character. By default, Secrets Manager disables this parameter, and the generated password doesn't include space
        :param pulumi.Input[int] password_length: The desired length of the generated password. The default value if you do not include this parameter is 32 characters. 
        :param pulumi.Input[bool] require_each_included_type: Specifies whether the generated password must include at least one of every allowed character type. By default, Secrets Manager enables this parameter, and the generated password includes at least one of every character type.
        :param pulumi.Input[str] secret_string_template: A properly structured JSON string that the generated password can be added to. If you specify this parameter, then you must also specify GenerateStringKey.
        """
        SecretGenerateSecretStringArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            exclude_characters=exclude_characters,
            exclude_lowercase=exclude_lowercase,
            exclude_numbers=exclude_numbers,
            exclude_punctuation=exclude_punctuation,
            exclude_uppercase=exclude_uppercase,
            generate_string_key=generate_string_key,
            include_space=include_space,
            password_length=password_length,
            require_each_included_type=require_each_included_type,
            secret_string_template=secret_string_template,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             exclude_characters: Optional[pulumi.Input[str]] = None,
             exclude_lowercase: Optional[pulumi.Input[bool]] = None,
             exclude_numbers: Optional[pulumi.Input[bool]] = None,
             exclude_punctuation: Optional[pulumi.Input[bool]] = None,
             exclude_uppercase: Optional[pulumi.Input[bool]] = None,
             generate_string_key: Optional[pulumi.Input[str]] = None,
             include_space: Optional[pulumi.Input[bool]] = None,
             password_length: Optional[pulumi.Input[int]] = None,
             require_each_included_type: Optional[pulumi.Input[bool]] = None,
             secret_string_template: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if exclude_characters is not None:
            _setter("exclude_characters", exclude_characters)
        if exclude_lowercase is not None:
            _setter("exclude_lowercase", exclude_lowercase)
        if exclude_numbers is not None:
            _setter("exclude_numbers", exclude_numbers)
        if exclude_punctuation is not None:
            _setter("exclude_punctuation", exclude_punctuation)
        if exclude_uppercase is not None:
            _setter("exclude_uppercase", exclude_uppercase)
        if generate_string_key is not None:
            _setter("generate_string_key", generate_string_key)
        if include_space is not None:
            _setter("include_space", include_space)
        if password_length is not None:
            _setter("password_length", password_length)
        if require_each_included_type is not None:
            _setter("require_each_included_type", require_each_included_type)
        if secret_string_template is not None:
            _setter("secret_string_template", secret_string_template)

    @property
    @pulumi.getter(name="excludeCharacters")
    def exclude_characters(self) -> Optional[pulumi.Input[str]]:
        """
        A string that excludes characters in the generated password. By default, all characters from the included sets can be used. The string can be a minimum length of 0 characters and a maximum length of 7168 characters. 
        """
        return pulumi.get(self, "exclude_characters")

    @exclude_characters.setter
    def exclude_characters(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "exclude_characters", value)

    @property
    @pulumi.getter(name="excludeLowercase")
    def exclude_lowercase(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies the generated password should not include lowercase letters. By default, ecrets Manager disables this parameter, and the generated password can include lowercase False, and the generated password can include lowercase letters.
        """
        return pulumi.get(self, "exclude_lowercase")

    @exclude_lowercase.setter
    def exclude_lowercase(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "exclude_lowercase", value)

    @property
    @pulumi.getter(name="excludeNumbers")
    def exclude_numbers(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies that the generated password should exclude digits. By default, Secrets Manager does not enable the parameter, False, and the generated password can include digits.
        """
        return pulumi.get(self, "exclude_numbers")

    @exclude_numbers.setter
    def exclude_numbers(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "exclude_numbers", value)

    @property
    @pulumi.getter(name="excludePunctuation")
    def exclude_punctuation(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies that the generated password should not include punctuation characters. The default if you do not include this switch parameter is that punctuation characters can be included. 
        """
        return pulumi.get(self, "exclude_punctuation")

    @exclude_punctuation.setter
    def exclude_punctuation(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "exclude_punctuation", value)

    @property
    @pulumi.getter(name="excludeUppercase")
    def exclude_uppercase(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies that the generated password should not include uppercase letters. The default behavior is False, and the generated password can include uppercase letters. 
        """
        return pulumi.get(self, "exclude_uppercase")

    @exclude_uppercase.setter
    def exclude_uppercase(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "exclude_uppercase", value)

    @property
    @pulumi.getter(name="generateStringKey")
    def generate_string_key(self) -> Optional[pulumi.Input[str]]:
        """
        The JSON key name used to add the generated password to the JSON structure specified by the SecretStringTemplate parameter. If you specify this parameter, then you must also specify SecretStringTemplate. 
        """
        return pulumi.get(self, "generate_string_key")

    @generate_string_key.setter
    def generate_string_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "generate_string_key", value)

    @property
    @pulumi.getter(name="includeSpace")
    def include_space(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies that the generated password can include the space character. By default, Secrets Manager disables this parameter, and the generated password doesn't include space
        """
        return pulumi.get(self, "include_space")

    @include_space.setter
    def include_space(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_space", value)

    @property
    @pulumi.getter(name="passwordLength")
    def password_length(self) -> Optional[pulumi.Input[int]]:
        """
        The desired length of the generated password. The default value if you do not include this parameter is 32 characters. 
        """
        return pulumi.get(self, "password_length")

    @password_length.setter
    def password_length(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "password_length", value)

    @property
    @pulumi.getter(name="requireEachIncludedType")
    def require_each_included_type(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether the generated password must include at least one of every allowed character type. By default, Secrets Manager enables this parameter, and the generated password includes at least one of every character type.
        """
        return pulumi.get(self, "require_each_included_type")

    @require_each_included_type.setter
    def require_each_included_type(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "require_each_included_type", value)

    @property
    @pulumi.getter(name="secretStringTemplate")
    def secret_string_template(self) -> Optional[pulumi.Input[str]]:
        """
        A properly structured JSON string that the generated password can be added to. If you specify this parameter, then you must also specify GenerateStringKey.
        """
        return pulumi.get(self, "secret_string_template")

    @secret_string_template.setter
    def secret_string_template(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_string_template", value)


@pulumi.input_type
class SecretReplicaRegionArgs:
    def __init__(__self__, *,
                 region: pulumi.Input[str],
                 kms_key_id: Optional[pulumi.Input[str]] = None):
        """
        A custom type that specifies a Region and the KmsKeyId for a replica secret.
        :param pulumi.Input[str] region: (Optional) A string that represents a Region, for example "us-east-1".
        :param pulumi.Input[str] kms_key_id: The ARN, key ID, or alias of the KMS key to encrypt the secret. If you don't include this field, Secrets Manager uses aws/secretsmanager.
        """
        SecretReplicaRegionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            region=region,
            kms_key_id=kms_key_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             region: pulumi.Input[str],
             kms_key_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("region", region)
        if kms_key_id is not None:
            _setter("kms_key_id", kms_key_id)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        """
        (Optional) A string that represents a Region, for example "us-east-1".
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN, key ID, or alias of the KMS key to encrypt the secret. If you don't include this field, Secrets Manager uses aws/secretsmanager.
        """
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)


@pulumi.input_type
class SecretTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A list of tags to attach to the secret. Each tag is a key and value pair of strings in a JSON text string.
        :param pulumi.Input[str] key: The value for the tag. You can specify a value that's 1 to 256 characters in length.
        :param pulumi.Input[str] value: The key name of the tag. You can specify a value that's 1 to 128 Unicode characters in length and can't be prefixed with aws.
        """
        SecretTagArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: pulumi.Input[str],
             value: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that's 1 to 256 characters in length.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The key name of the tag. You can specify a value that's 1 to 128 Unicode characters in length and can't be prefixed with aws.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


