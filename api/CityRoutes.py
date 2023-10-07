import json

from flask import jsonify, request, Response
from flask.views import MethodView

from models.City import City
from setup.database import db


class CityAPI(MethodView):
    def get_all_cities(self):
        cities = City.query.all()
        c = []
        for city in cities:
            c.append({"name": city.name, "state": city.state})
        return jsonify(c)

    def get(self):
        try:
            c = self.get_all_cities()
            return jsonify(c)

        except Exception as e:
            print("error - ", str(e))
            return Response({"error": "something went wrong while processing the request"}, mimetype="application/json",
                            status=500)

    def post(self):
        req = request.get_json()
        city = City()
        try:
            city.name = req["name"]
            city.state = req["state"]
        except KeyError:
            return Response(json.dumps({"error": "bad request, one of the required field is missing"}), mimetype="application/json",
                            status=400)
        db.session.add(city)
        db.session.commit()
        c = self.get_all_cities()
        return jsonify(c)

    def delete(self):
        req = request.get_json()
        city = City.query.filter_by(name=req["name"]).first()
        db.session.delete(city)
        db.session.commit()
        c = self.get_all_cities()
        return jsonify(c)
