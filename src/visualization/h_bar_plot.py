import sys
import pandas as pd
import numpy as np

from src.constants import *
from src.logger import logging
from src.utils.utils import plot_bar
from src.exception import CustomException
from src.entity.artifact_entity import DataPreprocessingArtifacts


class BarPlot:
    def __init__(self, data_preprocessing_artifacts: DataPreprocessingArtifacts):
        self.data_preprocessing_artifacts = data_preprocessing_artifacts

    def save_visual_pm2_5(self):
        try:
            logging.info("Saving horizontal bar plot for PM 2.5 ...")
            df_pm2_5 = pd.read_csv(self.data_preprocessing_artifacts.pm2_5_file_path)

            arr_dfs_pm2_5 = {
                "arr_african_pm2_5": None,
                "arr_east_pm2_5": None,
                "arr_europe_pm2_5": None,
                "arr_america_pm2_5": None,
                "arr_se_asia_pm2_5": None,
                "arr_west_pacific_pm2_5": None,
            }
            img_list = [
                AFRICAN_PM2_5,
                EAST_PM2_5,
                EUROPE_PM2_5,
                AMERICA_PM2_5,
                ASIA_PM2_5,
                PACIFIC_PM2_5,
            ]
            figsizes = [(28, 8), (28, 8), (28, 25), (28, 17), (26, 6), (23, 8)]
            minimum_vals = [20, 20, 15.5, 12, 20, 12]
            length = np.arange(len(WHO_REGIONS))

            for i, who_region, (key, _) in zip(
                length, WHO_REGIONS, arr_dfs_pm2_5.items()
            ):

                arr_dfs_pm2_5[key] = df_pm2_5[df_pm2_5[WHO_REGION] == who_region][
                    ["WHO Country Name", PM2_5]
                ].values

                arr_dfs_pm2_5[key] = pd.DataFrame(
                    arr_dfs_pm2_5[key], columns=["country", "pm_2.5"]
                )

                plot_bar(
                    arr_dfs_pm2_5[key],
                    who_region,
                    "PM 2.5",
                    img_list[i],
                    False,
                    figsizes[i],
                    minimum_vals[i],
                )
                logging.info("Successfully saved horizontal bar plot for PM 2.5 ...")
        except Exception as e:
            raise CustomException(e, sys)

    def save_visual_pm10(self):
        try:
            logging.info("Saving horizontal bar plot for PM 10 ...")
            df_pm10 = pd.read_csv(self.data_preprocessing_artifacts.pm10_file_path)
            """ Don't change the order of the following dict """
            arr_dfs_pm10 = {
                "arr_african_pm10": None,
                "arr_east_pm10": None,
                "arr_europe_pm10": None,
                "arr_america_pm10": None,
                "arr_se_asia_pm10": None,
                "arr_pacific_pm10": None,
            }

            img_list = [
                AFRICAN_PM10,
                EAST_PM10,
                EUROPE_PM10,
                AMERICA_PM10,
                ASIA_PM10,
                PACIFIC_PM10,
            ]
            figsizes = [(28, 9), (28, 12), (28, 25), (28, 15), (28, 7), (28, 8)]
            minimum_vals = [20, 30, 20, 10, 15, 10]
            length = np.arange(len(WHO_REGIONS))

            for i, who_region, (key, _) in zip(
                length, WHO_REGIONS, arr_dfs_pm10.items()
            ):

                arr_dfs_pm10[key] = df_pm10[df_pm10[WHO_REGION] == who_region][
                    ["WHO Country Name", PM10]
                ].values

                arr_dfs_pm10[key] = pd.DataFrame(
                    arr_dfs_pm10[key], columns=["country", "pm_10"]
                )

                plot_bar(
                    arr_dfs_pm10[key],
                    who_region,
                    "PM 10",
                    img_list[i],
                    False,
                    figsizes[i],
                    minimum_vals[i],
                )
                logging.info("Successfully saved horizontal bar plot for PM 10 ...")

        except Exception as e:
            raise CustomException(e, sys)

    def save_visual_no2(self):
        try:
            logging.info("Saving horizontal bar plot for NO2 ...")
            df_NO2 = pd.read_csv(self.data_preprocessing_artifacts.no2_file_path)

            arr_dfs_no2 = {
                "arr_african_no2": None,
                "arr_east_no2": None,
                "arr_europe_no2": None,
                "arr_america_no2": None,
                "arr_se_asia_no2": None,
                "arr_pacific_no2": None,
            }

            img_list = [
                AFRICAN_NO2,
                EAST_NO2,
                EUROPE_NO2,
                AMERICA_NO2,
                ASIA_NO2,
                PACIFIC_NO2,
            ]
            figsizes = [(28, 3), (28, 10), (28, 26), (28, 12), (28, 4), (28, 8)]
            minimum_vals = [20, 20, 10, 10, 7, 10]
            length = np.arange(len(WHO_REGIONS))

            for i, who_region, (key, _) in zip(
                length, WHO_REGIONS, arr_dfs_no2.items()
            ):

                arr_dfs_no2[key] = df_NO2[df_NO2[WHO_REGION] == who_region][
                    ["WHO Country Name", NO2]
                ].values

                arr_dfs_no2[key] = pd.DataFrame(
                    arr_dfs_no2[key], columns=["country", "NO2"]
                )

                plot_bar(
                    arr_dfs_no2[key],
                    who_region,
                    "NO2",
                    img_list[i],
                    True,
                    figsizes[i],
                    minimum_vals[i],
                )
                logging.info("Successfully saved horizontal bar plot for NO2 ...")

        except Exception as e:
            raise CustomException(e, sys)

    def create_bar_plot(self):
        try:
            self.save_visual_pm2_5()
            self.save_visual_pm10()
            self.save_visual_no2()

        except Exception as e:
            raise CustomException(e, sys)
