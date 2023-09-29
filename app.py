import json

from flask import Flask, Response

app = Flask(__name__)


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


app.run(port=8000, debug=True)
