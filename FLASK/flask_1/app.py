from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

df = pd.read_csv(r"C:\Users\adity\OneDrive\Desktop\45_days_Training\my_flask\Dataset Heart Disease.csv")


X = df[["age"]]
y = df["target"]


model = LogisticRegression()
model.fit(X, y)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    age = int(request.form["age"])

    prediction = model.predict([[age]])

    if prediction == 1:
        result = "Heart Disease Detected"
    else:
        result = "No Heart Disease"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
