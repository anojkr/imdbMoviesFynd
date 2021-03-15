from flask import Flask

# from helpers.db import load_db
# from helpers.parser import Parser
# export FLASK_APP=webapp.py
# sudo systemctl enable mongod
# sudo service mongod start

from app.Controller.MoviesController import blueprint
from mongoengine import connect

connectObject = connect("imdb", host="127.0.0.1", port=27017)


def create_app():
    # Create DB
    # load_db()

    # parser = Parser('imdb.json')
    # parser.populate()

    # Instantiate flask app
    app = Flask(__name__)

    # Register Blueprint
    app.register_blueprint(blueprint)

    # Return app
    return app
