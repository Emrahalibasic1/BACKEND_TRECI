from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db
auth = Blueprint('auth', __name__)

@auth.route('/hello')
def hello():
    return"<h1>Hello<h1>"

@auth.route('/login',methods =['GET','POST'])
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return render_template("home.html")


@auth.route('/sign-up',methods =['GET','POST'])
def signup():
    if request.method =='POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) <4:
            flash("Email mora biti duzi od 3 karaktera", category="error")
        elif len(first_name) <2:
            flash("Ime mora biti duze od 1 karaktera", category="error")
        elif password1 != password2:
            flash("Password netacan", category="error")
        elif len(password1) <7:
            flash("Password mora biti duzi od 6 karaktera", category="error")
        else:
            #dodaj korisnika u bazu
            new_user = User(email=email,password=generate_password_hash(password1,method='pbkdf2:sha256'),first_name=first_name)
            db.session.add(new_user)
            db.session.commit()
        
            flash("Racun je kreiran", category="success")
            return redirect(url_for('views.home'))
    return render_template("sign_up.html",fghfg=123)