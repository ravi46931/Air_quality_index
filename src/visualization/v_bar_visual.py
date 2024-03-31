import sys
import pandas as pd

from src.constants import *
from src.logger import logging
from src.utils.utils import plot_vertical_bar
from src.exception import CustomException
from src.entity.artifact_entity import DataPreprocessingArtifacts


class VerticalBarPlot:
    def __init__(self, data_preprocessing_artifacts: DataPreprocessingArtifacts):
        self.data_preprocessing_artifacts = data_preprocessing_artifacts

    def save_vertical_bar_pm2_5(self):
        try:
            logging.info("Saving vertical bar plot for PM 2.5 ...")
            df_pm2_5 = pd.read_csv(self.data_preprocessing_artifacts.pm2_5_file_path)
            img_names = [
                PM2_5_2010,
                PM2_5_2011,
                PM2_5_2012,
                PM2_5_2013,
                PM2_5_2014,
                PM2_5_2015,
                PM2_5_2016,
                PM2_5_2017,
                PM2_5_2018,
                PM2_5_2019,
                PM2_5_2020,
                PM2_5_2021,
            ]
            bbox_vals = [
                (0.55, 0.7),
                (0.25, 0.8),
                (0.25, 0.8),
                (0.25, 0.8),
                (0.25, 0.8),
                (0.55, 0.75),
                (0.55, 0.7),
                (0.55, 0.5),
                (0.55, 0.65),
                (0.55, 0.65),
                (0.55, 0.65),
                (0.25, 0.85),
            ]

            for i in range(len(YEARS)):
                plot_vertical_bar(
                    df_pm2_5,
                    PM2_5,
                    YEARS[i],
                    COLOR_PALLETE_PM2_5,
                    img_names[i],
                    bbox_vals[i],
                )
                logging.info("Successfully saved vertical bar plot for PM 2.5 ...")

        except Exception as e:
            raise CustomException(e, sys)

    def save_vertical_bar_pm10(self):
        try:
            logging.info("Saving vertical bar plot for PM 10 ...")
            df_pm10 = pd.read_csv(self.data_preprocessing_artifacts.pm10_file_path)
            img_names = [
                PM10_2010,
                PM10_2011,
                PM10_2012,
                PM10_2013,
                PM10_2014,
                PM10_2015,
                PM10_2016,
                PM10_2017,
                PM10_2018,
                PM10_2019,
                PM10_2020,
                PM10_2021,
            ]
            bbox_vals = [
                (0.45, 0.7),
                (0.45, 0.7),
                (0.45, 0.7),
                (0.45, 0.7),
                (0.7, 0.78),
                (0.45, 0.7),
                (0.45, 0.7),
                (0.45, 0.7),
                (0.45, 0.7),
                (0.45, 0.7),
                (0.7, 0.81),
                (0.25, 0.85),
            ]

            for i in range(len(YEARS)):
                plot_vertical_bar(
                    df_pm10,
                    PM10,
                    YEARS[i],
                    COLOR_PALLETE_PM10,
                    img_names[i],
                    bbox_vals[i],
                )
                logging.info("Successfully saved vertical bar plot for PM 10 ...")

        except Exception as e:
            raise CustomException(e, sys)

    def save_vertical_bar_no2(self):
        try:
            logging.info("Saving vertical bar plot for NO2 ...")
            df_NO2 = pd.read_csv(self.data_preprocessing_artifacts.no2_file_path)
            img_names = [
                NO2_2010,
                NO2_2011,
                NO2_2012,
                NO2_2013,
                NO2_2014,
                NO2_2015,
                NO2_2016,
                NO2_2017,
                NO2_2018,
                NO2_2019,
                NO2_2020,
                NO2_2021,
            ]
            bbox_vals = [
                (0.6, 0.7),
                (0.6, 0.83),
                (0.75, 0.8),
                (0.6, 0.8),
                (0.6, 0.8),
                (0.6, 0.8),
                (0.6, 0.8),
                (0.6, 0.8),
                (0.51, 0.83),
                (0.7, 0.81),
                (0.25, 0.8),
                (0.25, 0.85),
            ]

            for i in range(len(YEARS)):
                plot_vertical_bar(
                    df_NO2, NO2, YEARS[i], COLOR_PALLETE_NO2, img_names[i], bbox_vals[i]
                )
            logging.info("Successfully saved vertical bar plot for NO2 ...")

        except Exception as e:
            raise CustomException(e, sys)

    def create_vertical_bar_plot(self):
        try:
            self.save_vertical_bar_pm2_5()
            self.save_vertical_bar_pm10()
            self.save_vertical_bar_no2()

        except Exception as e:
            raise CustomException(e, sys)
