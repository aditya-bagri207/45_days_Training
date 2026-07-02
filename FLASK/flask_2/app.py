from flask import Flask , render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

    
@app.route("/search")    
def search():
    name = request.args.get("name")
    age = request.args.get("age")
    return f"welcome {name} and age is {age}"


if __name__ == "__main__":
    app.run(debug=True)


