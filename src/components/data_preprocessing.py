import os
import sys
import pandas as pd

from src.constants import *
from src.logger import logging
from src.exception import CustomException
from src.entity.config_entity import DataPreprocessingConfig
from src.entity.artifact_entity import (
    DataIngestionArtifacts,
    DataPreprocessingArtifacts,
)


class DataPreprocessing:
    def __init__(
        self,
        data_ingestion_artifacts: DataIngestionArtifacts,
        data_preprocessing_config: DataPreprocessingConfig,
    ):
        self.data_ingestion_artifacts = data_ingestion_artifacts
        self.data_preprocessing_config = data_preprocessing_config

    def data_preprocessing(self):
        try:
            logging.info("Data Preprocessing Started...")
            df = pd.read_csv(self.data_ingestion_artifacts.data_file_path)
            # Drop Status Column
            df.drop(DROP_COLUMN, axis=1, inplace=True)

            """ Taking not null records in PM2.5, PM10 and NO2 for visualizaton """

            df_pm2_5 = df[df[PM2_5].notna()]
            df_pm10 = df[df[PM10].notna()]
            df_NO2 = df[df[NO2].notna()]

            df_pm10 = df_pm10.dropna(subset=[WHO_REGION])
            df_NO2 = df_NO2.dropna(subset=[WHO_REGION])

            df_pm2_5.drop(ARCHIEVED_COLUMN, axis=1, inplace=True)
            # df_pm10.drop(ARCHIEVED_COLUMN,axis=1,inplace=True)
            # df_NO2.drop(ARCHIEVED_COLUMN,axis=1,inplace=True)
            logging.info("Data Preprocessing Completed...")

            return df_pm2_5, df_pm10, df_NO2

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_preprocessing(self):
        try:
            logging.info("Enter into data preprocessing component...")
            df_pm2_5, df_pm10, df_NO2 = self.data_preprocessing()
            os.makedirs(
                self.data_preprocessing_config.DATA_PREPROCESSING_ARTIFACTS_DIR,
                exist_ok=True,
            )
            df_pm2_5.to_csv(self.data_preprocessing_config.PM2_5_FILE_PATH)
            df_pm10.to_csv(self.data_preprocessing_config.PM10_FILE_PATH)
            df_NO2.to_csv(self.data_preprocessing_config.NO2_FILE_PATH)

            data_preprocessing_artifacts = DataPreprocessingArtifacts(
                self.data_preprocessing_config.PM2_5_FILE_PATH,
                self.data_preprocessing_config.PM10_FILE_PATH,
                self.data_preprocessing_config.NO2_FILE_PATH,
            )
            logging.info("Exit from data preprocessing component...")
            return data_preprocessing_artifacts

        except Exception as e:
            raise CustomException(e, sys)
