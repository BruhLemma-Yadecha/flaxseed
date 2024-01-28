from flask import Flask, render_template, request, session, flash, url_for, redirect
import joblib
import pandas as pd
import numpy as np

model = joblib.load("static/gnb_model.joblib")
print(model)
app = Flask(__name__)

@app.route("/", methods =["GET", "POST"])
def home():
    if request.method == "POST":
        s_account = request.form.get("s_account")
        r_account = request.form.get("r_account")
        amount = request.form.get("amount")
        p_currency = request.form.get("p_currency")
        r_currency = request.form.get("r_currency")
        sb_location = request.form.get("sb_location")
        rb_location = request.form.get("rb_location")
        p_type = request.form.get("p_type")
        values = [s_account, r_account, amount, p_currency, r_currency, sb_location, rb_location, p_type]
        df_test = pd.DataFrame({"Test": values})
        prediction = predict(df_test)
        session['prediction'] = 'prediction'
        redirect(output)
    else:
        return render_template("flaxseed.html")

@app.route("/output", methods =["GET", "POST"])
def output():
    if request.method == "GET":
        prediction = session.get('prediction', None)
        return render_template("flaxseed_2.html", prediction = prediction)
    


def predict(df_test):
    df_test = pd.get_dummies(df_test, columns = ["Payment_currency"], dtype=int)
    df_test = pd.get_dummies(df_test, columns = ["Received_currency"], dtype=int)
    df_test = pd.get_dummies(df_test, columns = ["Sender_bank_location"], dtype=int)
    df_test = pd.get_dummies(df_test, columns = ["Receiver_bank_location"], dtype=int) 
    df_test = pd.get_dummies(df_test, columns = ["Payment_type"], dtype=int) 
    
    prediction = model.predict(df_test)
    return prediction


    

    


