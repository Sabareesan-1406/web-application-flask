from setup.database import db


# Model is the definition of a table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(200), unique=True)
    phone = db.Column(db.String(12), unique=True)
    age = db.Column(db.Integer)
