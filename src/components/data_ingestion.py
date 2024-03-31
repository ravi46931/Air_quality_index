import os
import sys
import pandas as pd

from src.logger import logging
from src.exception import CustomException
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifacts


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config

    def initiate_data_ingestion(self):
        try:
            logging.info("Data Ingestion Started...")
            df = pd.read_excel("data/air_quality_data.xlsx")
            os.makedirs(
                self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR, exist_ok=True
            )
            df.to_csv(self.data_ingestion_config.DATA_FILE_PATH)

            data_ingestion_artifacts = DataIngestionArtifacts(
                self.data_ingestion_config.DATA_FILE_PATH
            )
            logging.info("Data Ingestion Completed...")
            return data_ingestion_artifacts

        except Exception as e:
            raise CustomException(e, sys)
