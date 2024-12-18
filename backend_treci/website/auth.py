from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db
from flask_login import login_user, logout_user,login_required,current_user
auth = Blueprint('auth', __name__)

@auth.route('/hello')
def hello():
    return"<h1>Hello<h1>"

@auth.route('/login',methods =['GET','POST'])
def login():
    if request.method == 'POST':
        form_email = request.form.get('email')
        form_password = request.form.get('password')

        user = User.query.filter_by(email=form_email).first()
        if user:
            if check_password_hash(user.password, form_password):
                flash('Uspijesno ste se ulogovali', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Pogresan email ili password', category='error')
        else:
            flash('Pogresan email ili password', category='error')    
    return render_template("login.html",user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up',methods =['GET','POST'])
def signup():
    if request.method =='POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        #ovo je nase

        is_admin = request.form.get('is_admin')

        #ovo je kraj naseg
        user= User.query.filter_by(email=email).first()
        if user:
            flash("Email vec postoji", category="error")
        elif len(email) <4:
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
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))
    return render_template("sign_up.html",user=current_user)
