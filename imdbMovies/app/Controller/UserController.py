"""
This file contains API endpoints which would be exposed to the outer world
"""
import json
from flask import Blueprint, request
from flask import jsonify, make_response

import uuid
from mongoengine import connect

from app.Exceptions import Exceptions
from app.Utils.StatusCodes import StatusCodes
from app.Models.UserModels import User

import logging
from app.Config.settings import Config
from logging.config import dictConfig
from  werkzeug.security import generate_password_hash, check_password_hash 

auth_blueprint = Blueprint("auth", __name__)

LIMIT = Config.LIMIT
dictConfig(Config.LOGGER_CONFIGURATION)
logger = logging.getLogger(__name__)


@auth_blueprint.route("/user/login")
def homepageView():
    """
    A test API to check if flask is properly configured
    :return:
    """
    return "Welcome to login API"


@auth_blueprint.route('/user/signup', methods =['POST']) 
def signup_user(): 

	data = request.json

	if "username" not in data.keys() or "password" not in data.keys():
		raise Error("Parameter error")
	username = data["username"]
	password = data["password"]

	print(username, password)
	user = User.objects.filter(username = username).first() 
	# print(user)
	if user is None: 
		user = User(username = username, password = generate_password_hash(password)).save()  
		return make_response('Successfully registered.', 201) 
	else: 
		return make_response('User already exists. Please Log in.', 202) 