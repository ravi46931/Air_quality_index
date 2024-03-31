import sys

from src.logger import logging
from src.exception import CustomException
from src.pipeline.data_pipeline import DataPipeline
from src.pipeline.plot_pipeline import PlotPipeline


class MainPipeline:
    def __init__(self):
        pass

    def start_data_pipeline(self):
        try:
            logging.info("Data pipeline started")
            data_pipeline = DataPipeline()
            data_preprocessing_artifacts = data_pipeline.run_data_pipeline()
            logging.info("Data pipeline completed")
            return data_preprocessing_artifacts

        except Exception as e:
            raise CustomException(e, sys)

    def start_plot_pipeline(self, data_preprocessing_artifacts):
        try:
            logging.info("Plot pipeline started")
            plot_pipeline = PlotPipeline(data_preprocessing_artifacts)
            plot_pipeline.run_plot_pipeline()
            logging.info("Plot pipeline completed")

        except Exception as e:
            raise CustomException(e, sys)

    def run_pipeline(self):
        try:
            data_preprocessing_artifacts = self.start_data_pipeline()
            self.start_plot_pipeline(data_preprocessing_artifacts)
        except Exception as e:
            raise CustomException(e, sys)
