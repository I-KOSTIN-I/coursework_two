from flask import Flask
from webpage_blueprint.routes import webpage
from api.routes import api_bp


def my_app():
    app = Flask(__name__)
    app.register_blueprint(webpage)
    app.register_blueprint(api_bp, url_prefix='/api')
    return app


if __name__ == "__main__":
    app = my_app()
    app.run(debug=True)
