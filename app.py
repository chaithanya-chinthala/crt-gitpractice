from flask import Flask ,render_template,request
from pymongo import MongoClient

app = Flask(__name__)
my_client=MongoClient("localhost",27017)
my_db=my_client["calci_project"]
results=my_db["results"]

@app.route("/", methods=["GET"])
def homepage():
    return "<h1>Hey Coder, Welcome to homepage</h1>"
@app.route("/project",methods=["GET","POST"])
def calculator():
    if request.method == "POST":
        num1=int(request.form["num1"])
        num2=int(request.form["num2"])
        opr=request.form["opr"]
        if opr == "add":
            output = f"{num1} + {num2} = {num1+num2}"
            results.insert_one({"num1":num1,"num2":num2,"opr":opr,"result":num1+num2})
            return render_template("index.html", data=output)
        elif opr == "sub":
            output = f"{num1} - {num2} = {num1-num2}"
            results.insert_one({"num1":num1,"num2":num2,"opr":opr,"result":num1-num2})
            return render_template("index.html", data=output) 
        elif opr == "mul":
            output = f"{num1} x {num2} = {num1*num2}"
            results.insert_one({"num1":num1,"num2":num2,"opr":opr,"result":num1*num2})
            return render_template("index.html", data=output) 
        elif opr == "div":
            try:
              output = f"{num1} / {num2} = {num1/num2}"
              results.insert_one({"num1":num1,"num2":num2,"opr":opr,"result":num1/num2})
              return render_template("index.html", data=output) 
            except  Exception:
                error="change num2 value"
                return render_template("index.html", data=error)
        else:
            return "Invalid Operation"
    else:
        return render_template("index.html")