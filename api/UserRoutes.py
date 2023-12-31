import json

from flask import Blueprint, request, jsonify, Response
from sqlalchemy.exc import DataError
import logging
from models.User import User
from setup.database import db

apis = Blueprint('api', __name__)


@apis.route('/user', methods=['POST', 'GET', 'DELETE', 'PUT'])
def manage_user():
    logging.info("Got Request for user")
    if request.method == 'POST':
        logging.info("Request is for adding a user")
        req_data = request.get_json()
        logging.info(f"request data - {req_data}")
        user = User()
        try:
            user.name = req_data["name"]
            user.email = req_data["email"]
            user.phone = req_data["phone"]
            user.age = req_data["age"]
            db.session.add(user)
            db.session.commit()
            logging.debug(f"user added to database")
        except DataError:
            logging.info(f"user addition to database failed")
            return Response(json.dumps({"error": "bad request, age cannot be a string"}), mimetype="application/json",
                            status=400)
        except Exception as e:
            logging.error(f"something went wrong while adding to database - {str(e)}")
            return Response(json.dumps({"error": "unexcepted error when adding user - str(e)"}),
                            mimetype="application/json",
                            status=500)
    elif request.method == 'DELETE':
        req_data = request.get_json()
        user = User.query.filter_by(name=req_data["name"]).first()
        db.session.delete(user)
        db.session.commit()
    elif request.method == 'PUT':
        req_data = request.get_json()
        user = User.query.filter_by(name=req_data["name"]).first()
        user.phone = req_data["phone"]
        user.email = req_data["email"]
        db.session.add(user)
        db.session.commit()
    # GET is the default method
    u = []
    users = User.query.all()
    for user in users:
        u.append({"name": user.name, "phone": user.phone, "email": user.email, "age": user.age})
    logging.debug(f"response - {u}")
    return jsonify(u)

# .query.filter_by(firstname='Sammy').all()

# # default landing
# @apis.route('/api/city')
# def city():
#     res = {"name": "pondicherry", "country": "india"}
#     jres = json.dumps(res)
#     response = Response(jres, mimetype="application/json", status=200)
#     return response
#
#
