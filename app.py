import json
import sqlite3

from flask import Flask, Response, jsonify

app = Flask(__name__)

db_connect = sqlite3.connect('database.db')
db_connect.execute(
    'CREATE TABLE IF NOT EXISTS Users (name TEXT, \
    email TEXT, city TEXT, country TEXT, phone TEXT, age INTEGER)')


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


# default landing
# @app.route('/api/user')
# def user():
#     res = {"name": "siva", "age": "40"}
#
#     response = jsonify(res)
#     return response


# default landing
@app.route('/api/city')
def city():
    res = {"name": "pondicherry", "country": "india"}
    jres = json.dumps(res)
    response = Response(jres, mimetype="application/json", status=200)
    return response


@app.route('/api/user', methods=['POST', 'GET', 'DELETE'])
def add_user():
    return jsonify({"name": "siva", "age": "40"})


app.run(port=5000, debug=True)
