from flask import Flask, render_template,request, redirect, url_for, flash




app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "password"
app.config["MYSQL_HOST"] = "localhost"




@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add_contact", methods= ["POST"])
def add_contact():
    if request.method =="POST":
        fullname = request.form["fullname"]
        phone = request.form["phone"]
        email = request.form["email"]

        flash ("Contacto añadido correctamene")
        return redirect(url_for("home"))



@app.route("/edit")
def edit_contact():
    return "edit contact"

@app.route("/delite_contact")
def delit_contact():
    return "delite contact"


if __name__ == "__main__":
    app.run(debug= True)