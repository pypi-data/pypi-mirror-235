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
    'RotationScheduleHostedRotationLambda',
    'RotationScheduleRotationRules',
    'SecretGenerateSecretString',
    'SecretReplicaRegion',
    'SecretTag',
]

@pulumi.output_type
class RotationScheduleHostedRotationLambda(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "rotationType":
            suggest = "rotation_type"
        elif key == "excludeCharacters":
            suggest = "exclude_characters"
        elif key == "kmsKeyArn":
            suggest = "kms_key_arn"
        elif key == "masterSecretArn":
            suggest = "master_secret_arn"
        elif key == "masterSecretKmsKeyArn":
            suggest = "master_secret_kms_key_arn"
        elif key == "rotationLambdaName":
            suggest = "rotation_lambda_name"
        elif key == "superuserSecretArn":
            suggest = "superuser_secret_arn"
        elif key == "superuserSecretKmsKeyArn":
            suggest = "superuser_secret_kms_key_arn"
        elif key == "vpcSecurityGroupIds":
            suggest = "vpc_security_group_ids"
        elif key == "vpcSubnetIds":
            suggest = "vpc_subnet_ids"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RotationScheduleHostedRotationLambda. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RotationScheduleHostedRotationLambda.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RotationScheduleHostedRotationLambda.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 rotation_type: str,
                 exclude_characters: Optional[str] = None,
                 kms_key_arn: Optional[str] = None,
                 master_secret_arn: Optional[str] = None,
                 master_secret_kms_key_arn: Optional[str] = None,
                 rotation_lambda_name: Optional[str] = None,
                 runtime: Optional[str] = None,
                 superuser_secret_arn: Optional[str] = None,
                 superuser_secret_kms_key_arn: Optional[str] = None,
                 vpc_security_group_ids: Optional[str] = None,
                 vpc_subnet_ids: Optional[str] = None):
        RotationScheduleHostedRotationLambda._configure(
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
             rotation_type: str,
             exclude_characters: Optional[str] = None,
             kms_key_arn: Optional[str] = None,
             master_secret_arn: Optional[str] = None,
             master_secret_kms_key_arn: Optional[str] = None,
             rotation_lambda_name: Optional[str] = None,
             runtime: Optional[str] = None,
             superuser_secret_arn: Optional[str] = None,
             superuser_secret_kms_key_arn: Optional[str] = None,
             vpc_security_group_ids: Optional[str] = None,
             vpc_subnet_ids: Optional[str] = None,
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
    def rotation_type(self) -> str:
        return pulumi.get(self, "rotation_type")

    @property
    @pulumi.getter(name="excludeCharacters")
    def exclude_characters(self) -> Optional[str]:
        return pulumi.get(self, "exclude_characters")

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[str]:
        return pulumi.get(self, "kms_key_arn")

    @property
    @pulumi.getter(name="masterSecretArn")
    def master_secret_arn(self) -> Optional[str]:
        return pulumi.get(self, "master_secret_arn")

    @property
    @pulumi.getter(name="masterSecretKmsKeyArn")
    def master_secret_kms_key_arn(self) -> Optional[str]:
        return pulumi.get(self, "master_secret_kms_key_arn")

    @property
    @pulumi.getter(name="rotationLambdaName")
    def rotation_lambda_name(self) -> Optional[str]:
        return pulumi.get(self, "rotation_lambda_name")

    @property
    @pulumi.getter
    def runtime(self) -> Optional[str]:
        return pulumi.get(self, "runtime")

    @property
    @pulumi.getter(name="superuserSecretArn")
    def superuser_secret_arn(self) -> Optional[str]:
        return pulumi.get(self, "superuser_secret_arn")

    @property
    @pulumi.getter(name="superuserSecretKmsKeyArn")
    def superuser_secret_kms_key_arn(self) -> Optional[str]:
        return pulumi.get(self, "superuser_secret_kms_key_arn")

    @property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[str]:
        return pulumi.get(self, "vpc_security_group_ids")

    @property
    @pulumi.getter(name="vpcSubnetIds")
    def vpc_subnet_ids(self) -> Optional[str]:
        return pulumi.get(self, "vpc_subnet_ids")


@pulumi.output_type
class RotationScheduleRotationRules(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "automaticallyAfterDays":
            suggest = "automatically_after_days"
        elif key == "scheduleExpression":
            suggest = "schedule_expression"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RotationScheduleRotationRules. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RotationScheduleRotationRules.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RotationScheduleRotationRules.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 automatically_after_days: Optional[int] = None,
                 duration: Optional[str] = None,
                 schedule_expression: Optional[str] = None):
        RotationScheduleRotationRules._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            automatically_after_days=automatically_after_days,
            duration=duration,
            schedule_expression=schedule_expression,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             automatically_after_days: Optional[int] = None,
             duration: Optional[str] = None,
             schedule_expression: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if automatically_after_days is not None:
            _setter("automatically_after_days", automatically_after_days)
        if duration is not None:
            _setter("duration", duration)
        if schedule_expression is not None:
            _setter("schedule_expression", schedule_expression)

    @property
    @pulumi.getter(name="automaticallyAfterDays")
    def automatically_after_days(self) -> Optional[int]:
        return pulumi.get(self, "automatically_after_days")

    @property
    @pulumi.getter
    def duration(self) -> Optional[str]:
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> Optional[str]:
        return pulumi.get(self, "schedule_expression")


@pulumi.output_type
class SecretGenerateSecretString(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "excludeCharacters":
            suggest = "exclude_characters"
        elif key == "excludeLowercase":
            suggest = "exclude_lowercase"
        elif key == "excludeNumbers":
            suggest = "exclude_numbers"
        elif key == "excludePunctuation":
            suggest = "exclude_punctuation"
        elif key == "excludeUppercase":
            suggest = "exclude_uppercase"
        elif key == "generateStringKey":
            suggest = "generate_string_key"
        elif key == "includeSpace":
            suggest = "include_space"
        elif key == "passwordLength":
            suggest = "password_length"
        elif key == "requireEachIncludedType":
            suggest = "require_each_included_type"
        elif key == "secretStringTemplate":
            suggest = "secret_string_template"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SecretGenerateSecretString. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SecretGenerateSecretString.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SecretGenerateSecretString.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 exclude_characters: Optional[str] = None,
                 exclude_lowercase: Optional[bool] = None,
                 exclude_numbers: Optional[bool] = None,
                 exclude_punctuation: Optional[bool] = None,
                 exclude_uppercase: Optional[bool] = None,
                 generate_string_key: Optional[str] = None,
                 include_space: Optional[bool] = None,
                 password_length: Optional[int] = None,
                 require_each_included_type: Optional[bool] = None,
                 secret_string_template: Optional[str] = None):
        """
        :param str exclude_characters: A string that excludes characters in the generated password. By default, all characters from the included sets can be used. The string can be a minimum length of 0 characters and a maximum length of 7168 characters. 
        :param bool exclude_lowercase: Specifies the generated password should not include lowercase letters. By default, ecrets Manager disables this parameter, and the generated password can include lowercase False, and the generated password can include lowercase letters.
        :param bool exclude_numbers: Specifies that the generated password should exclude digits. By default, Secrets Manager does not enable the parameter, False, and the generated password can include digits.
        :param bool exclude_punctuation: Specifies that the generated password should not include punctuation characters. The default if you do not include this switch parameter is that punctuation characters can be included. 
        :param bool exclude_uppercase: Specifies that the generated password should not include uppercase letters. The default behavior is False, and the generated password can include uppercase letters. 
        :param str generate_string_key: The JSON key name used to add the generated password to the JSON structure specified by the SecretStringTemplate parameter. If you specify this parameter, then you must also specify SecretStringTemplate. 
        :param bool include_space: Specifies that the generated password can include the space character. By default, Secrets Manager disables this parameter, and the generated password doesn't include space
        :param int password_length: The desired length of the generated password. The default value if you do not include this parameter is 32 characters. 
        :param bool require_each_included_type: Specifies whether the generated password must include at least one of every allowed character type. By default, Secrets Manager enables this parameter, and the generated password includes at least one of every character type.
        :param str secret_string_template: A properly structured JSON string that the generated password can be added to. If you specify this parameter, then you must also specify GenerateStringKey.
        """
        SecretGenerateSecretString._configure(
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
             exclude_characters: Optional[str] = None,
             exclude_lowercase: Optional[bool] = None,
             exclude_numbers: Optional[bool] = None,
             exclude_punctuation: Optional[bool] = None,
             exclude_uppercase: Optional[bool] = None,
             generate_string_key: Optional[str] = None,
             include_space: Optional[bool] = None,
             password_length: Optional[int] = None,
             require_each_included_type: Optional[bool] = None,
             secret_string_template: Optional[str] = None,
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
    def exclude_characters(self) -> Optional[str]:
        """
        A string that excludes characters in the generated password. By default, all characters from the included sets can be used. The string can be a minimum length of 0 characters and a maximum length of 7168 characters. 
        """
        return pulumi.get(self, "exclude_characters")

    @property
    @pulumi.getter(name="excludeLowercase")
    def exclude_lowercase(self) -> Optional[bool]:
        """
        Specifies the generated password should not include lowercase letters. By default, ecrets Manager disables this parameter, and the generated password can include lowercase False, and the generated password can include lowercase letters.
        """
        return pulumi.get(self, "exclude_lowercase")

    @property
    @pulumi.getter(name="excludeNumbers")
    def exclude_numbers(self) -> Optional[bool]:
        """
        Specifies that the generated password should exclude digits. By default, Secrets Manager does not enable the parameter, False, and the generated password can include digits.
        """
        return pulumi.get(self, "exclude_numbers")

    @property
    @pulumi.getter(name="excludePunctuation")
    def exclude_punctuation(self) -> Optional[bool]:
        """
        Specifies that the generated password should not include punctuation characters. The default if you do not include this switch parameter is that punctuation characters can be included. 
        """
        return pulumi.get(self, "exclude_punctuation")

    @property
    @pulumi.getter(name="excludeUppercase")
    def exclude_uppercase(self) -> Optional[bool]:
        """
        Specifies that the generated password should not include uppercase letters. The default behavior is False, and the generated password can include uppercase letters. 
        """
        return pulumi.get(self, "exclude_uppercase")

    @property
    @pulumi.getter(name="generateStringKey")
    def generate_string_key(self) -> Optional[str]:
        """
        The JSON key name used to add the generated password to the JSON structure specified by the SecretStringTemplate parameter. If you specify this parameter, then you must also specify SecretStringTemplate. 
        """
        return pulumi.get(self, "generate_string_key")

    @property
    @pulumi.getter(name="includeSpace")
    def include_space(self) -> Optional[bool]:
        """
        Specifies that the generated password can include the space character. By default, Secrets Manager disables this parameter, and the generated password doesn't include space
        """
        return pulumi.get(self, "include_space")

    @property
    @pulumi.getter(name="passwordLength")
    def password_length(self) -> Optional[int]:
        """
        The desired length of the generated password. The default value if you do not include this parameter is 32 characters. 
        """
        return pulumi.get(self, "password_length")

    @property
    @pulumi.getter(name="requireEachIncludedType")
    def require_each_included_type(self) -> Optional[bool]:
        """
        Specifies whether the generated password must include at least one of every allowed character type. By default, Secrets Manager enables this parameter, and the generated password includes at least one of every character type.
        """
        return pulumi.get(self, "require_each_included_type")

    @property
    @pulumi.getter(name="secretStringTemplate")
    def secret_string_template(self) -> Optional[str]:
        """
        A properly structured JSON string that the generated password can be added to. If you specify this parameter, then you must also specify GenerateStringKey.
        """
        return pulumi.get(self, "secret_string_template")


@pulumi.output_type
class SecretReplicaRegion(dict):
    """
    A custom type that specifies a Region and the KmsKeyId for a replica secret.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "kmsKeyId":
            suggest = "kms_key_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SecretReplicaRegion. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SecretReplicaRegion.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SecretReplicaRegion.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 region: str,
                 kms_key_id: Optional[str] = None):
        """
        A custom type that specifies a Region and the KmsKeyId for a replica secret.
        :param str region: (Optional) A string that represents a Region, for example "us-east-1".
        :param str kms_key_id: The ARN, key ID, or alias of the KMS key to encrypt the secret. If you don't include this field, Secrets Manager uses aws/secretsmanager.
        """
        SecretReplicaRegion._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            region=region,
            kms_key_id=kms_key_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             region: str,
             kms_key_id: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("region", region)
        if kms_key_id is not None:
            _setter("kms_key_id", kms_key_id)

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        (Optional) A string that represents a Region, for example "us-east-1".
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[str]:
        """
        The ARN, key ID, or alias of the KMS key to encrypt the secret. If you don't include this field, Secrets Manager uses aws/secretsmanager.
        """
        return pulumi.get(self, "kms_key_id")


@pulumi.output_type
class SecretTag(dict):
    """
    A list of tags to attach to the secret. Each tag is a key and value pair of strings in a JSON text string.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A list of tags to attach to the secret. Each tag is a key and value pair of strings in a JSON text string.
        :param str key: The value for the tag. You can specify a value that's 1 to 256 characters in length.
        :param str value: The key name of the tag. You can specify a value that's 1 to 128 Unicode characters in length and can't be prefixed with aws.
        """
        SecretTag._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The value for the tag. You can specify a value that's 1 to 256 characters in length.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The key name of the tag. You can specify a value that's 1 to 128 Unicode characters in length and can't be prefixed with aws.
        """
        return pulumi.get(self, "value")


