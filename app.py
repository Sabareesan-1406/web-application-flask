from api.route import apis
from setup import application

if __name__ == '__main__':
    app = application.create_app()
    app.register_blueprint(apis, url_prefix="/api")
    app.run(port=5000, debug=True)
