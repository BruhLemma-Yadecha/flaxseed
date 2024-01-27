from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("flaxseed.html")

def predict(df_test):
    import joblib
    import pandas as pd
    import numpy as np
    df_test = pd.get_dummies(df_test, columns = ["Payment_currency"], dtype=int) 
    df_test = pd.get_dummies(df_test, columns = ["Received_currency"], dtype=int) 
    df_test = pd.get_dummies(df_test, columns = ["Sender_bank_location"], dtype=int) 
    df_test = pd.get_dummies(df_test, columns = ["Receiver_bank_location"], dtype=int) 
    df_test = pd.get_dummies(df_test, columns = ["Payment_type"], dtype=int) 
    model = joblib.load("/static/gnb_model.joblib")

    

    


