from  flask_login import UserMixin 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
db = SQLAlchemy()

class Note(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True),default=db.func.now())
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))

class User(db.Model,UserMixin):
    id =  db.Column(db.Integer, primary_key=True)
    email =  db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    is_admin = db.Column(db.Boolean)
