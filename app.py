from flask import Flask

from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
 
#create the object of Flask
app  = Flask(__name__)
 
app.config['SECRET_KEY'] = 'hardsecretkey'
 
 
#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost:8888/flask' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
#our model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True)
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))
 
 
    def __init__(self, name, email, password):
        self.name = username
        self.email = email
        self.password = password
 


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")



@app.route('/signup' , methods = ['GET', 'POST'])
def Login():
 
    return render_template('signup.html')


@app.route("/register", methods=["POST", "GET"])
def co():
    if request.method == "GET":
        return "Login via the login Form"

    if request.method == "POST":
        name = request.form["nom"]
        email = request.form["email"]
        password = request.form["password"]
        cursor = mysql.connection.cursor()
        cursor.execute(
            """ INSERT INTO info_table VALUES(%s,%s,%s)""", (name, email, password)
        )
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"




@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/logout")
def logout():
    return "Logout"


if __name__ == "__main__":
    app.run(host="localhost", port=8080)
