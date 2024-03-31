import sys

from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.entity.artifact_entity import DataIngestionArtifacts
from src.components.data_preprocessing import DataPreprocessing
from src.entity.config_entity import DataIngestionConfig, DataPreprocessingConfig


class DataPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_preprocessing_config = DataPreprocessingConfig()

    def start_data_ingestion(self):
        try:
            logging.info("Data ingestion started..")
            data_ingestion = DataIngestion(self.data_ingestion_config)
            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logging.info("Data ingestion completed..")

            return data_ingestion_artifacts

        except Exception as e:
            raise CustomException(e, sys)

    def start_data_preprocessing(
        self, data_ingestion_artifacts: DataIngestionArtifacts
    ):
        try:
            logging.info("Data preprocesing started..")
            data_preprocessing = DataPreprocessing(
                data_ingestion_artifacts, self.data_preprocessing_config
            )
            data_preprocessing_artifacts = (
                data_preprocessing.initiate_data_preprocessing()
            )
            logging.info("Data preprocesing completed..")

            return data_preprocessing_artifacts

        except Exception as e:
            raise CustomException(e, sys)

    def run_data_pipeline(self):
        try:
            logging.info("Running data pipeline..")
            data_ingestion_artifacts = self.start_data_ingestion()
            data_preprocessing_artifacts = self.start_data_preprocessing(
                data_ingestion_artifacts
            )
            logging.info("Data pipeline run successfully..")
            return data_preprocessing_artifacts

        except Exception as e:
            raise CustomException(e, sys)
