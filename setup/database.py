from flask_sqlalchemy import SQLAlchemy
import logging
db = SQLAlchemy()
def initialize_db(app):
    with app.app_context():
        try:
            db.init_app(app)
            db.create_all()
            return True
        except Exception as e:
            logging.critical(f"Error initializing Database : {str(e)}")
            return False
