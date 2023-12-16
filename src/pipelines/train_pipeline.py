import os, sys
from src.logger import logging
from src.exception import CustomException

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

# To run Each componets Indivisualy

# if __name__ == "__main__":
#     # data ingestion initialization
#     ingestion_obj = DataIngestion()
#     train_path, test_path = ingestion_obj.initiate_data_ingestion()

#     # data transformation initiated here 
#     transformation_obj = DataTransformation()
#     train_arr, test_arr, preprocessor_path = transformation_obj.initiate_data_transformation(train_path, test_path)

#     # model training initialization here 
#     trainer_obj = ModelTrainer()
#     trainer_obj.initiate_model_trainer(train_arr, test_arr, preprocessor_path)

class TrainPipeline:
    def __init__(self):
        # data ingestion initialization
        self.ingestion_obj = DataIngestion()

        # data transformation initiated here 
        self.transformation_obj = DataTransformation()
        
        # model training initialization here 
        self.trainer_obj = ModelTrainer()

    def run_pipeline(self):

        try:
            logging.info("Initializing Training Pipeline")
            
            train_path, test_path = self.ingestion_obj.initiate_data_ingestion()

            train_arr, test_arr, preprocessor_path = self.transformation_obj.initiate_data_transformation(train_path, test_path)

            self.trainer_obj.initiate_model_trainer(train_arr, test_arr, preprocessor_path)
            
            logging.info("Model Training is Sucsessfully Done!")
            
        except Exception as e:
            raise CustomException(e, sys)
