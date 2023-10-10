import sys

from flask import Flask
from flask_log_request_id import RequestID
from setup.database import initialize_db
from setup.log import initialize_logger


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zaq1xsw2@localhost:3306/flaskapp'
    db_initialized = initialize_db(app)
    initialize_logger(log_level="DEBUG")
    RequestID(app)
    if not db_initialized:
        sys.exit()
    return app
