import sys
from src.exception import CustomException
from src.entity.artifact_entity import DataPreprocessingArtifacts
from src.visualization.h_bar_plot import BarPlot
from src.visualization.hist_plot import HistPlot
from src.visualization.v_bar_visual import VerticalBarPlot


class PlotPipeline:
    def __init__(self, data_preprocessing_artifacts: DataPreprocessingArtifacts):
        self.data_preprocessing_artifacts = data_preprocessing_artifacts

    def start_bar_plot(self):
        try:
            bar_plot = BarPlot(self.data_preprocessing_artifacts)
            bar_plot.create_bar_plot()
        except Exception as e:
            raise CustomException(e, sys)

    def start_hist_plot(self):
        try:
            hist_plot = HistPlot(self.data_preprocessing_artifacts)
            hist_plot.create_hist_plot()
        except Exception as e:
            raise CustomException(e, sys)

    def start_vertical_bar_plot(self):
        try:
            vertical_bar_plot = VerticalBarPlot(self.data_preprocessing_artifacts)
            vertical_bar_plot.create_vertical_bar_plot()
        except Exception as e:
            raise CustomException(e, sys)

    def run_plot_pipeline(self):
        try:
            self.start_bar_plot()
            self.start_hist_plot()
            self.start_vertical_bar_plot()

        except Exception as e:
            raise CustomException(e, sys)
