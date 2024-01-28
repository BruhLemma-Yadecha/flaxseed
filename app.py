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


        countries = ["Albania","Austria","France","Germany","India","Italy","Japan","Mexico","Morocco","Netherlands","Nigeria","Pakistan",
                 "Spain","Switzerland", "Turkey","UAE","UK","USA"]
        currency = ["Albania","Euro","India","Japan","Mexico","Morocco","Nigeria","Pakistan","Switzerland","Turkey","UAE","UK","USA"]
        payment_type = ["ACH","CashDeposit","CashWithdrawal","Cheque","CreditCard","CrossBorder","DebitCard"]
       
        list_payment_currency = []
        list_received_currency = []
        list_sender_bank_location = []
        list_receiver_bank_location = []
        list_payment_type = []
        


        for i in currency:
            if i == p_currency:
                list_payment_currency.append(1)
            else:
                list_payment_currency.append(0)
            if i == r_currency:
                list_received_currency.append(1)
            else:
                list_received_currency.append(0)

        for i in countries:
            if i == sb_location:
                list_sender_bank_location.append(1)
            else:
                list_sender_bank_location.append(0)
            if i == rb_location:
                list_receiver_bank_location.append(1)
            else:
                list_receiver_bank_location.append(0)    

        for i in payment_type:
            if i == p_type:
                list_payment_type.append(1)
            else:
                list_payment_type.append(0)    

        final_test_list = [s_account,r_account,amount]+list_payment_currency+list_received_currency+list_sender_bank_location+list_receiver_bank_location+list_payment_type


        df_test = pd.DataFrame({"Test": final_test_list})
        session['df_test'] = df_test
        redirect(output)
    else:
        return render_template("flaxseed.html")

@app.route("/output", methods =["GET", "POST"])
def output():
    
    df_test = session.get('df_test', None)
    prediction = predict(df_test)

    # flash('prediction')
    return render_template("flaxseed_2.html", prediction = prediction)
    


def predict(df_test):

    prediction = model.predict(df_test)
    return prediction


    

    


