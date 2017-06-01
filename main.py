from flask import Flask
from os import getenv

from application.controllers import main_controller

app = Flask(__name__, template_folder="application/templates")
app.register_blueprint(main_controller.blueprint, url_prefix='/')
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:////tmp/test.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == "__main__":
    app.run(debug=bool(getenv("FLASK_DEBUG", False)))
