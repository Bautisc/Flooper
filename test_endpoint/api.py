from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database/flooper.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique=True)
    contraseña = db.Column(db.String(24))
    email = db.Column(db.String(50))

class Tareas(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    contenido =db.Column(db.String(80))
    completada =db.Column(db.Boolean)




