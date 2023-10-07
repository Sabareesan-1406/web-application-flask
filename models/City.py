from setup.database import db


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    state = db.Column(db.String(3), unique=True)

