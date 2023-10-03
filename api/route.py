import json

from flask import Blueprint, request, jsonify, Response

from database.User import User
from database.connection import db

apis = Blueprint('api', __name__)


@apis.route('/api/user', methods=['POST', 'GET'])
def add_user():
    db.create_all()  # Create table if table does not exist
    if request.method == 'POST':
        user = User()
        user.name = "firstuser"
        user.email = "firstuser.abc.com"
        user.phone = "123-234-3456"
        db.session.add(user)
        db.session.commit()
        users = User.query.all()
    elif request.method == 'GET':
        users = User.query.all()
    return jsonify(users)


# default landing
@apis.route('/api/city')
def city():
    res = {"name": "pondicherry", "country": "india"}
    jres = json.dumps(res)
    response = Response(jres, mimetype="application/json", status=200)
    return response
