# Dependencies Setup
import pandas as pd
from flask import Flask, request, redirect, url_for, flash, jsonify, render_template
import requests
import numpy as np
import json
import sqlite3 as sql
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model


#Set up data base
conn = sql.connect('data/test_final.db', check_same_thread=False)

# Create an instance of the Flask class
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/historicaldata")
def historical():
    return render_template("data.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/models")
def getmodels():
    return render_template("models.html")

@app.route("/class/<test_id>")
def test(test_id):
    x = pd.read_sql(f'SELECT * FROM final WHERE ID_code == "{test_id}"', conn)
    x = x.drop("index", axis=1)
    x= x.drop("ID_code", axis=1)
    model = load_model("models/neuronal_network_07.h5")
    pred_class = model.predict_classes(x)
    probability = model.predict(x)
    no_transaction = probability[0][0]
    transaction = probability[0][1]
    result = []
    pred_class = pred_class[0]
    if pred_class == 0:
        result_dict = {}
        result_dict['prediction'] = 'NO Transaction'
        result_dict['No transaction'] = str(no_transaction)
        result_dict['transaction'] = str(transaction)
        result.append(result_dict)

    else:
        result_dict = {}
        result_dict['prediction'] = 'Transaction'
        result_dict['No transaction'] = str(no_transaction)
        result_dict['transaction'] = str(transaction)
        result.append(result_dict)

    return jsonify(result)

@app.route('/predict', methods=["GET", "POST"])
def predict():

    if request.method == "POST": 

        # getting user input from HTML form
        hour = request.form["hour"]
        hour = f"test_{hour}"

        response = requests.get(f"https://santander-predictor.herokuapp.com/class/{hour}")
        x = response.json()
        prediction = x[0]["prediction"]
        prob1 = x[0]["No transaction"]
        prob2 = x[0]["transaction"]

    return render_template("prediction.html", pred = prediction, pred1 = prob1, pred2 = prob2)


if __name__ == '__main__':
    app.run(debug=True)