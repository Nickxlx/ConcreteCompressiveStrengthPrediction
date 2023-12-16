import os
import sys

from src.exception import CustomException
from src.logger import logging
from src.utils import save_obj, load_obj, train_evaluate_model, read_yaml_file

from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV 
from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    model_obj_path = os.path.join("artifacts", "model.pkl")
    model_config_file_path = os.path.join("config", "model.yaml")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    # tunning the best model
    def finetune_best_model(self, best_model_name, best_model_object,
                            x_train, y_train):
        try:
            model_param_grid = read_yaml_file(self.model_trainer_config.model_config_file_path)["model_selection"]["model"][best_model_name]["search_param_grid"]

            grid_search = GridSearchCV(best_model_object, 
                                    param_grid= model_param_grid,
                                    cv=5, n_jobs=-1, verbose=1)
            
            grid_search.fit(x_train, y_train)
            best_params = grid_search.best_params_

            print("best params are: ", best_params)

            finetune_model = best_model_object.set_params(**best_params)
            return finetune_model
        
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_model_trainer(self, train_arr, test_arr, preprocessor_path):
        try:
            logging.info("Spliting Train and Test data")

            x_train, y_train, x_test, y_test = (
                                                train_arr[:, :-1],
                                                train_arr[:, -1],
                                                test_arr[:, :-1],
                                                test_arr[:, -1]
            )

            models = {
                        'Linear Regression': LinearRegression(),
                        'Ridge Regression': Ridge(),
                        'Lasso Regression': Lasso(),
                        'Random Forest Regression': RandomForestRegressor(),
                        'Gradient Boosting Regression':GradientBoostingRegressor()
                        }

            logging.info(f"Extracting model config file path")
            model_report = train_evaluate_model(x_train, y_train, models)

            # best score model from the dict
            best_model_score = max(model_report.values())

            # best score model name from dict
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            logging.info(f"Tuning the best model")
            best_model = self.finetune_best_model(
                best_model_name= best_model_name,
                best_model_object = best_model,
                x_train = x_train,
                y_train = y_train
            )

            logging.info(f"Tunned model training ")
            best_model.fit(x_train, y_train)
            y_pred = best_model.predict(x_test)
            best_model_score = r2_score(y_test, y_pred)

            if best_model_score < 0.6:
                raise Exception("No best model found with an accuracy greater than the threshold 0.6")
            else:
                print(f"Best Model Found , Model Name :{best_model_name}, R2 Score: {best_model_score*100:.2f}%")

            logging.info(
                f"Saving model at path: {self.model_trainer_config.model_obj_path}"
            )
            
            save_obj(
                    file_path=self.model_trainer_config.model_obj_path,
                    obj=best_model
                    )
            print ("Model Training is Sucsessfully Done! ")
            return
        except Exception as e:
            raise CustomException(e, sys)