import os, sys
import pandas as pd

from flask import request

from src.logger import logging
from src.exception import CustomException
from src.utils import load_obj

from dataclasses import dataclass

@dataclass
class PredictionFileDetail:
    prediction_output_dirname: str = "predictions"
    prediction_file_name: str = "predicted_file.csv"
    
    # Update path
    prediction_file_path: str = os.path.join(prediction_output_dirname,prediction_file_name)  

class PredictionPipeline:
    def __init__(self, request: request):
        
        self.request = request
        self.prediction_file_detail = PredictionFileDetail()

    def save_input_files(self) -> str:
        try:
            pred_file_input_dir = "prediction_artifacts"
            os.makedirs(pred_file_input_dir, exist_ok=True)

            input_csv_file = self.request.files['file']
            pred_file_path = os.path.join(pred_file_input_dir, input_csv_file.filename)
            os.makedirs(os.path.dirname(pred_file_path), exist_ok=True)
            input_csv_file.save(pred_file_path)

            return pred_file_path
        except Exception as e:
            raise CustomException(e, sys)

    def predict(self, features):
        try:
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            model_path = os.path.join("artifacts","model.pkl")

            preprocessor = load_obj(file_path=preprocessor_path)
            model = load_obj(file_path=model_path)

            feature_scaled = preprocessor.transform(features)
            preds = model.predict(feature_scaled)
            return preds

        except Exception as e:
            raise CustomException(e, sys)

    def get_predicted_dataframe(self, input_dataframe_path: pd.DataFrame):
        try:
            # Load the input data
            input_dataframe: pd.DataFrame = pd.read_csv(input_dataframe_path)

            # Predict using the model
            predictions = self.predict(input_dataframe.drop(columns=["strength"])) 

            # Add predictions to the DataFrame
            input_dataframe["predicted_strength"] = predictions
            
            os.makedirs(self.prediction_file_detail.prediction_output_dirname, exist_ok=True)
            input_dataframe.to_csv(self.prediction_file_detail.prediction_file_path, index=False)
            logging.info("Predictions completed.")

        except Exception as e:
            raise CustomException(e, sys) from e

    def run_pipeline(self):
        try:
            input_csv_path = self.save_input_files()
            self.get_predicted_dataframe(input_csv_path)

            return self.prediction_file_detail

        except Exception as e:
            raise CustomException(e, sys)
