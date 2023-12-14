import sys
import pandas as pd 
from flask import Flask, request, render_template, jsonify, send_file

from src.exception import CustomException
from src.logger import logging

from src.pipelines.train_pipeline import TrainPipeline
from src.pipelines.predict_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/train")
def train():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()

        return jsonify("Training Successfull.")
    except Exception as e:
        raise CustomException(e, sys)
    
# route for single value prediction
@app.route("/predict", methods = ["POST", "GET"])
def pred():
    try:
        if request.method == "POST":
            data = dict(request.form.items())
            # print(data)
            # return jsonify("done")
            new_Data = pd.DataFrame(data)
            prediction_pipeline = PredictionPipeline()
            pred = prediction_pipeline.predict(new_Data)
            result =  pred[0]
            return render_template("index.html", context=result)
        else:
            return render_template('index.html')
    except Exception as e:
        raise CustomException(e,sys)

@app.route("/upload", methods = ["POST", "GET"])
def upload():
    try:
        if request.method == "POST":
            prediction_pipeline = PredictionPipeline(request=request)
            prediction_file_detail= prediction_pipeline.run_pipeline()

            logging.info("prediction completed. Downloading prediction file.")
            return send_file(prediction_file_detail.prediction_file_path,
                            download_name = prediction_file_detail.prediction_file_name,
                            as_attachment = True)
        else:
            return render_template('upload_file.html')
    except Exception as e:
        raise CustomException(e,sys)
    
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=8080, debug= True )