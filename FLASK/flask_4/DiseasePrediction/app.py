from flask import Flask,render_template,request
import numpy as np
import pickle

app=Flask(__name__)

with open("model/heart.pkl","rb") as file:
    model=pickle.load(file)

with open("model/scaler.pkl","rb") as file:
    model=pickle.load(file)

with open("model/encoders.pkl","rb") as file:
    model=pickle.load(file)


@app.route("/")

def home():
    return render_template('index2.html')
@app.route("/login",methods=["POST"])  #used to tell the browser to use as a post function 

def Predict():
    oldpeak=float(request.form["oldpeak"])

   
if(__name__)=='__main__':
    app.run(debug=True)
