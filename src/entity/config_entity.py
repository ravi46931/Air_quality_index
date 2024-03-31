import os
from src.constants import *
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    DATA_INGESTION_ARTIFACTS_DIR = os.path.join(ARTIFACTS, DATA_INGESTION_ARTIFACTS_DIR)
    DATA_FILE_PATH = os.path.join(DATA_INGESTION_ARTIFACTS_DIR, DATA_FILE_NAME)


@dataclass
class DataPreprocessingConfig:
    DATA_PREPROCESSING_ARTIFACTS_DIR = os.path.join(
        ARTIFACTS, DATA_PREPROCESSING_ARTIFACTS_DIR
    )
    PM2_5_FILE_PATH = os.path.join(DATA_PREPROCESSING_ARTIFACTS_DIR, PM2_5_FILE_NAME)
    PM10_FILE_PATH = os.path.join(DATA_PREPROCESSING_ARTIFACTS_DIR, PM10_FILE_NAME)
    NO2_FILE_PATH = os.path.join(DATA_PREPROCESSING_ARTIFACTS_DIR, NO2_FILE_NAME)
