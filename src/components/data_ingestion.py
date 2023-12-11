import os, sys
import pymongo 
import pandas as pd

from src.logger import logging
from src.exception import CustomException
from src.utils import export_collection_as_dataframe

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path = os.path.join("artifacts", "raw.csv")
    train_data_path = os.path.join("artifacts", "train.csv")
    test_data_path = os.path.join("artifacts", "test.csv")

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion just initialization")

        try:
            uri  = r"mongodb+srv://nikhilsinghxlx:Nikhilsinghxlx@cluster0.9kjhcgg.mongodb.net/?retryWrites=true&w=majority"
            DataBase_Name = "Projects" 
            Collection_Name = "Cement_Strength"

            logging.info("Exporting the data from mongoDB as df")
            df = export_collection_as_dataframe(uri, DataBase_Name, Collection_Name)

            logging.info("Data as DataFrame is Successfully exported")

            # storing the raw data
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.data_ingestion_config.raw_data_path, index = False)

            # spliting 
            train_set, test_set = train_test_split(df, test_size=0.25, random_state=42)
            
            # also storing the training and test data
            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path), exist_ok=True)
            train_set.to_csv(self.data_ingestion_config.train_data_path, index = False, header = True)

            os.makedirs(os.path.dirname(self.data_ingestion_config.test_data_path), exist_ok=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path, index = False, header = True)
            
            logging.info("Succsefully stored train, test and raw data ")

            return (
                self.data_ingestion_config.train_data_path, 
                self.data_ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)