from flask import Flask
from forms import LoginForm, RegistrationForm
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



@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
 
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method = 'sha256')
        name = form.name.data
        email = form.email.data
        password = hashed_password
 
        new_register = Users(name=name, email=email, password=password)
 
        db.session.add(new_register)
 
        db.session.commit()
 
        flash("Registration was successfull, please login")
 
        return redirect(url_for('index'))
 
    return render_template('registration.html', form=form)


@app.route("/login")
def Login():
    form = LoginForm()
    if form.validate_on_submit():
        if request.form['username'] != 'codeloop' or request.form['password'] != '12345':
            flash("Invalid Credentials, Please Try Again")
        else:
            return redirect(url_for('index'))
    return render_template('index.html', form = form)


@app.route("/logout")
def logout():
    return "Logout"


if __name__ == "__main__":
    app.run(host="localhost", port=8080)
