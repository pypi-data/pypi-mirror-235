# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'DocumentClassifierAugmentedManifestsListItemSplit',
    'DocumentClassifierDocumentReaderConfigDocumentReadAction',
    'DocumentClassifierDocumentReaderConfigDocumentReadMode',
    'DocumentClassifierDocumentReaderConfigFeatureTypesItem',
    'DocumentClassifierInputDataConfigDataFormat',
    'DocumentClassifierInputDataConfigDocumentType',
    'DocumentClassifierLanguageCode',
    'DocumentClassifierMode',
    'FlywheelDocumentClassificationConfigMode',
    'FlywheelModelType',
    'FlywheelTaskConfigLanguageCode',
]


class DocumentClassifierAugmentedManifestsListItemSplit(str, Enum):
    TRAIN = "TRAIN"
    TEST = "TEST"


class DocumentClassifierDocumentReaderConfigDocumentReadAction(str, Enum):
    TEXTRACT_DETECT_DOCUMENT_TEXT = "TEXTRACT_DETECT_DOCUMENT_TEXT"
    TEXTRACT_ANALYZE_DOCUMENT = "TEXTRACT_ANALYZE_DOCUMENT"


class DocumentClassifierDocumentReaderConfigDocumentReadMode(str, Enum):
    SERVICE_DEFAULT = "SERVICE_DEFAULT"
    FORCE_DOCUMENT_READ_ACTION = "FORCE_DOCUMENT_READ_ACTION"


class DocumentClassifierDocumentReaderConfigFeatureTypesItem(str, Enum):
    TABLES = "TABLES"
    FORMS = "FORMS"


class DocumentClassifierInputDataConfigDataFormat(str, Enum):
    COMPREHEND_CSV = "COMPREHEND_CSV"
    AUGMENTED_MANIFEST = "AUGMENTED_MANIFEST"


class DocumentClassifierInputDataConfigDocumentType(str, Enum):
    PLAIN_TEXT_DOCUMENT = "PLAIN_TEXT_DOCUMENT"
    SEMI_STRUCTURED_DOCUMENT = "SEMI_STRUCTURED_DOCUMENT"


class DocumentClassifierLanguageCode(str, Enum):
    EN = "en"
    ES = "es"
    FR = "fr"
    IT = "it"
    DE = "de"
    PT = "pt"


class DocumentClassifierMode(str, Enum):
    MULTI_CLASS = "MULTI_CLASS"
    MULTI_LABEL = "MULTI_LABEL"


class FlywheelDocumentClassificationConfigMode(str, Enum):
    MULTI_CLASS = "MULTI_CLASS"
    MULTI_LABEL = "MULTI_LABEL"


class FlywheelModelType(str, Enum):
    DOCUMENT_CLASSIFIER = "DOCUMENT_CLASSIFIER"
    ENTITY_RECOGNIZER = "ENTITY_RECOGNIZER"


class FlywheelTaskConfigLanguageCode(str, Enum):
    EN = "en"
    ES = "es"
    FR = "fr"
    IT = "it"
    DE = "de"
    PT = "pt"
