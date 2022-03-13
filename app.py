from flask import Flask
from webpage_blueprint.routes import webpage
app = Flask(__name__)
app.register_blueprint(webpage)

if __name__ == "__main__":
	app.run()