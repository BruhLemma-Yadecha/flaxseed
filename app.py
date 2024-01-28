from flask import Flask, render_template
import joblib
import pandas as pd
import numpy as np

model = joblib.load("static/gnb_model.joblib")
app = Flask(__name__)
app.config["SECRET_KEY"] = 'cypher.ai flaxseed'

@app.route("/")
def home():

    return render_template("flaxseed.html")

def predict(df_test):
    df_test = pd.get_dummies(df_test, columns = ["Payment_currency"], dtype=int) 
    df_test = pd.get_dummies(df_test, columns = ["Received_currency"], dtype=int) 
    df_test = pd.get_dummies(df_test, columns = ["Sender_bank_location"], dtype=int) 
    df_test = pd.get_dummies(df_test, columns = ["Receiver_bank_location"], dtype=int) 
    df_test = pd.get_dummies(df_test, columns = ["Payment_type"], dtype=int) 
    
    prediction = model.predict(df_test)
    return prediction


    

    


