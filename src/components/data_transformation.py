import os, sys
import pandas as pd 
import numpy as np


from src.exception import CustomException
from src.logger import logging
from src.utils import save_obj

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    preprocessor_obj_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transform(self):
        try:
            imputer =  ("imputer", SimpleImputer(strategy="mean"))
            scaler = ("scaler", StandardScaler())

            preprocessor = Pipeline(
                [
                    imputer,
                    scaler
                ]
            ) 
            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            logging.info("Reading the data for Preprocessing")
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            target_col = "strength"

            x_train_df = train_df.drop([target_col], axis=1)
            y_train_df = train_df[target_col]

            x_test_df = test_df.drop([target_col], axis=1)
            y_test_df = test_df[target_col]

            preprocessor = self.get_data_transform()

            logging.info("Applying preprocessor")

            x_train_scaled = preprocessor.fit_transform(x_train_df)
            x_test_scaled = preprocessor.transform(x_test_df)

            train_arr = np.c_[x_train_scaled, np.array(y_train_df)]
            test_arr = np.c_[x_test_scaled, np.array(y_test_df)]

            logging.info("Saving the preprocessor object")
            save_obj(self.data_transformation_config.preprocessor_obj_path, 
                    obj = preprocessor)
            
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_path
            )
        except Exception as e:
            raise CustomException(e, sys)
