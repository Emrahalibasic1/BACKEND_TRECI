from flask import Blueprint, render_template, request, flash 

auth = Blueprint('auth', __name__)

@auth.route('/hello')
def hello():
    return"<h1>Hello<h1>"

@auth.route('/login',methods =['GET','POST'])
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return render_template("<p>Logout</p>")


@auth.route('/sign-up',methods =['GET','POST'])
def signup():
    if request.method =='POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) <4:
            flash("Email mora biti duzi od 3 karaktera", category="error")
        elif len(firstName) <2:
            flash("Ime mora biti duze od 1 karaktera", category="error")
        elif password1 != password2:
            flash("Password netacan", category="error")
        elif len(password1) <7:
            flash("Password mora biti duzi od 6 karaktera", category="error")
        else:
            #dodaj korisnika u bazu
            flash("Racun je kreiran", category="error")
    return render_template("sign_up.html")