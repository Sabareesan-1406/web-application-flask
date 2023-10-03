import json
import sqlite3

from api.route import apis
from database.User import User
from flask import Flask, Response, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from database.connection import db

app = Flask(__name__)

# # option 1 : Database Connection Details - configured into flask app
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'zaq1xsw@'
# app.config['MYSQL_DB'] = 'flask_app'

# option 2 using connection string
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://usera:passw0rd@localhost:3306/flask_app'

app.register_blueprint(apis, url_prefix="/api")


# default landing
@app.route('/')
def home():
    return "Hi I am Home"


# default landing
@app.route('/about')
def about():
    res = "This is user A"

    response = Response(res, status=200)
    return response


app.run(port=5000, debug=True)
