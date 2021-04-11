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


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("405.html")

    if request.method == "POST":
        name = request.form["nom"]
        password = request.form["password"]
        email = request.form["email"]
        cursor = mysql.connection.cursor()
        cursor.execute(
            """ INSERT INTO users FROM flask VALUES(%s,%s,%s)""",
            (name, password, email),
        )

        mysql.connection.commit()
        cursor.close()
        return f"Done!!"

    return render_template(login.html)


@app.route("/logout")
def logout():
    return "Logout"


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
