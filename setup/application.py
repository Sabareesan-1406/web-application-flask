from flask import Flask
from setup.database import initialize_db


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zaq1xsw2@localhost:3306/flaskapp'
    initialize_db(app)
    return app
