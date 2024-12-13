from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

my_client = MongoClient("localhost", 27017)
my_db = my_client["calci"] # database is calsi
students = my_db["results"] # collection, table name is results

@app.route("/", methods = ["GET","POST"])
def homepage():
    return render_template("index.html")

@app.route("/admissions", methods = ["GET"])
def admission():
    return render_template("admissions.html")

@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        _id = int(request.form["rid"])
        name = request.form["rname"]
        email = request.form["rmail"]
        phone = request.form["rphone"]
        percentage = request.form["rpercentage"]
        rank = request.form["rrank"]
        course = request.form["rcourse"]
        address = request.form["raddress"]
        students.insert_one({"id":_id, "name":name, "email":email, "phone":phone, "percentage":percentage, "rank":rank, "course":course, "address":address})
        #return "data inserted"
    return render_template("register.html")

@app.route("/view", methods = ["GET"])
def view():
    raw = list(students.find())
    return render_template("view.html", output=raw)
@app.route("/update", methods = ["GET", "POST"])
def update():
    if request.method == "POST":
        _id = int(request.form["rid"])
        old_data = request.form["old_data"]
        new_data = request.form["new_data"]
        students.update_one({"id" : _id},{"$set":{old_data:new_data}})
        return "data updated"
    return render_template("update.html")

@app.route("/delete", methods = ["GET", "POST"])
def delete():
    if request.method == "POST":
        _id = int(request.form["rid"])
        students.delete_one({"id" : _id})
        return "deleted"
    return render_template("delete.html")

app.run(debug=True)