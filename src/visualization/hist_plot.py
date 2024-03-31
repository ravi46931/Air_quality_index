import sys
import pandas as pd

from src.constants import *
from src.logger import logging
from src.utils.utils import plot_hist
from src.exception import CustomException
from src.entity.artifact_entity import DataPreprocessingArtifacts


class HistPlot:
    def __init__(self, data_preprocessing_artifacts: DataPreprocessingArtifacts):
        self.data_preprocessing_artifacts = data_preprocessing_artifacts

    def save_hist_plot_pm2_5(self):
        try:
            logging.info("Saving histogram plot for PM 2.5 with cities...")
            df_pm2_5 = pd.read_csv(self.data_preprocessing_artifacts.pm2_5_file_path)
            df_pm2_5_city = df_pm2_5.groupby("City or Locality")[PM2_5].mean()
            df_pm2_5_city = pd.DataFrame(df_pm2_5_city)

            plot_hist(
                df=df_pm2_5_city,
                column=PM2_5,
                color=HIST_PM2_5_COLOR,
                plot_attr="PM 2.5",
                bins="auto",
                image_name=HIST_PM2_5,
                figsize=(9, 4.5),
            )
            logging.info("Successfully saved histogram plot for PM 2.5 with cities...")
        except Exception as e:
            raise CustomException(e, sys)

    def save_hist_plot_pm10(self):
        try:
            logging.info("Saving histogram plot for PM 10 with cities...")
            df_pm10 = pd.read_csv(self.data_preprocessing_artifacts.pm10_file_path)
            df_pm10_city = df_pm10.groupby("City or Locality")[PM10].mean()
            df_pm10_city = pd.DataFrame(df_pm10_city)

            plot_hist(
                df=df_pm10_city,
                column=PM10,
                color=HIST_PM10_COLOR,
                plot_attr="PM 10",
                image_name=HIST_PM10,
                bins=90,
            )
            logging.info("Successfully saved histogram plot for PM 10 with cities...")

        except Exception as e:
            raise CustomException(e, sys)

    def save_hist_plot_no2(self):
        try:
            logging.info("Saving histogram plot for NO2 with cities...")
            df_NO2 = pd.read_csv(self.data_preprocessing_artifacts.no2_file_path)
            df_NO2_city = df_NO2.groupby("City or Locality")[NO2].mean()
            df_NO2_city = pd.DataFrame(df_NO2_city)

            plot_hist(
                df=df_NO2_city,
                column=NO2,
                color=HIST_NO2_COLOR,
                plot_attr="NO2",
                image_name=HIST_NO2,
                bins=77,
            )
            logging.info("Successfully saved histogram plot for NO2 with cities...")

        except Exception as e:
            raise CustomException(e, sys)

    def create_hist_plot(self):
        try:
            logging.info("Creating Histogram plots with cities...")
            self.save_hist_plot_pm2_5()
            self.save_hist_plot_pm10()
            self.save_hist_plot_no2()
            logging.info("Histogram plots created successfully...")

        except Exception as e:
            raise CustomException(e, sys)
