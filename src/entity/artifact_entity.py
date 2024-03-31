from src.constants import *
from dataclasses import dataclass


@dataclass
class DataIngestionArtifacts:
    data_file_path: str


@dataclass
class DataPreprocessingArtifacts:
    pm2_5_file_path: str
    pm10_file_path: str
    no2_file_path: str
