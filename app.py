from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__, static_url_path="/")

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "flask"

mysql = MySQL(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/signup")
def form():
    return render_template("signup.html")


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
