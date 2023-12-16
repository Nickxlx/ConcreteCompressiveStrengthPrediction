import os, sys
import pymongo
import yaml

import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

from src.exception import CustomException
from src.logger import logging

def export_collection_as_dataframe(uri, db_name, coll_name):
    try:
        # connect to data mongodb
        client = pymongo.MongoClient(uri)

        # Access the database and collection
        db = client[db_name]
        collection = db[coll_name]

        # Retrive the database 
        cursor = collection.find()
        data_in_json  = list(cursor)

        # Convert the data to a Pandas DataFrame
        df = pd.DataFrame(data_in_json)

        # droping id col
        df = df.drop(["_id"], axis=1)

        df.replace({"na": np.nan}, inplace=True)
        
        return df
    except Exception as e:
        raise CustomException(e, sys)
    
def save_obj(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path) 
        os.makedirs(dir_path, exist_ok=True)  
        
        with open(file_path, "wb") as file:
            pickle.dump(obj, file)
            
    except Exception as e:
        raise CustomException(e, sys)
    

    
def load_obj(file_path):
    try:
        with open(file_path, "rb") as file:
            t = pickle.load(file)
            return t
    except FileNotFoundError as fnf_error:
        logging.error(f"File not found error: {fnf_error}, File path: {file_path}")
        raise CustomException(fnf_error, sys)
    except pickle.UnpicklingError as unpickling_error:
        logging.error(f"Unpickling error: {unpickling_error}, File path: {file_path}")
        raise CustomException(unpickling_error, sys)
    except Exception as e:
        logging.error(f"Unexpected error: {e}, File path: {file_path}")
        raise CustomException(e, sys)

def train_evaluate_model(x, y, models):
    try:
        x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.2, 
                                                            random_state=42)

        report = {}

        for name, model in models.items():

            model.fit(x_train, y_train)
            
            # Evaluation
            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)
            
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            print("Model:", name)
            print("Train Score: {:.2%}".format(train_model_score))
            print("Test Score: {:.2%}".format(test_model_score))
            print("*"*50)
            
            #Store the score in the report dictionary with the model name as the key and value as score
            report[name] = test_model_score
            
        return report
    
    except Exception as e:
        raise CustomException (e,sys)
            
def read_yaml_file(file_name):
    try:
        with open(file_name, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
        
    except Exception as e:
        raise CustomException(e, sys) from e