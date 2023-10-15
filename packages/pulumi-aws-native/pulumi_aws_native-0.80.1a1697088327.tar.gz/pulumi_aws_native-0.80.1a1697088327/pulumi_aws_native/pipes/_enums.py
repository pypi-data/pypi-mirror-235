# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'PipeAssignPublicIp',
    'PipeBatchJobDependencyType',
    'PipeBatchResourceRequirementType',
    'PipeDynamoDbStreamStartPosition',
    'PipeEcsEnvironmentFileType',
    'PipeEcsResourceRequirementType',
    'PipeKinesisStreamStartPosition',
    'PipeLaunchType',
    'PipeMskStartPosition',
    'PipeOnPartialBatchItemFailureStreams',
    'PipePlacementConstraintType',
    'PipePlacementStrategyType',
    'PipePropagateTags',
    'PipeRequestedPipeState',
    'PipeSelfManagedKafkaStartPosition',
    'PipeState',
    'PipeTargetInvocationType',
]


class PipeAssignPublicIp(str, Enum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class PipeBatchJobDependencyType(str, Enum):
    N_TO_N = "N_TO_N"
    SEQUENTIAL = "SEQUENTIAL"


class PipeBatchResourceRequirementType(str, Enum):
    GPU = "GPU"
    MEMORY = "MEMORY"
    VCPU = "VCPU"


class PipeDynamoDbStreamStartPosition(str, Enum):
    TRIM_HORIZON = "TRIM_HORIZON"
    LATEST = "LATEST"


class PipeEcsEnvironmentFileType(str, Enum):
    S3 = "s3"


class PipeEcsResourceRequirementType(str, Enum):
    GPU = "GPU"
    INFERENCE_ACCELERATOR = "InferenceAccelerator"


class PipeKinesisStreamStartPosition(str, Enum):
    TRIM_HORIZON = "TRIM_HORIZON"
    LATEST = "LATEST"
    AT_TIMESTAMP = "AT_TIMESTAMP"


class PipeLaunchType(str, Enum):
    EC2 = "EC2"
    FARGATE = "FARGATE"
    EXTERNAL = "EXTERNAL"


class PipeMskStartPosition(str, Enum):
    TRIM_HORIZON = "TRIM_HORIZON"
    LATEST = "LATEST"


class PipeOnPartialBatchItemFailureStreams(str, Enum):
    AUTOMATIC_BISECT = "AUTOMATIC_BISECT"


class PipePlacementConstraintType(str, Enum):
    DISTINCT_INSTANCE = "distinctInstance"
    MEMBER_OF = "memberOf"


class PipePlacementStrategyType(str, Enum):
    RANDOM = "random"
    SPREAD = "spread"
    BINPACK = "binpack"


class PipePropagateTags(str, Enum):
    TASK_DEFINITION = "TASK_DEFINITION"


class PipeRequestedPipeState(str, Enum):
    RUNNING = "RUNNING"
    STOPPED = "STOPPED"


class PipeSelfManagedKafkaStartPosition(str, Enum):
    TRIM_HORIZON = "TRIM_HORIZON"
    LATEST = "LATEST"


class PipeState(str, Enum):
    RUNNING = "RUNNING"
    STOPPED = "STOPPED"
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    STARTING = "STARTING"
    STOPPING = "STOPPING"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATE_FAILED = "UPDATE_FAILED"
    START_FAILED = "START_FAILED"
    STOP_FAILED = "STOP_FAILED"


class PipeTargetInvocationType(str, Enum):
    REQUEST_RESPONSE = "REQUEST_RESPONSE"
    FIRE_AND_FORGET = "FIRE_AND_FORGET"
