from api import CityRoutes
from api.UserRoutes import apis
from setup import application


class CityView:
    pass


if __name__ == '__main__':
    app = application.create_app()
    app.register_blueprint(apis, url_prefix="/api")
    cities = CityRoutes.CityAPI.as_view("cities")
    app.add_url_rule("/cities",view_func=cities)
    app.run(port=5000, debug=True)
