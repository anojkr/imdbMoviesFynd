from flask import Flask

# from helpers.db import load_db
# from helpers.parser import Parser
# export FLASK_APP=webapp.py
# sudo systemctl enable mongod
# sudo service mongod start

from app.Controller.MoviesController import blueprint
from app.Controller.UserController import auth_blueprint
from mongoengine import connect
from app.Config.settings import Config


connectObject = connect(host=Config.DB_URI)


def create_app():

    # Instantiate flask app
    app = Flask(__name__)

    # Register Blueprint
    app.register_blueprint(blueprint)
    app.register_blueprint(auth_blueprint)

    # Return app
    return app
