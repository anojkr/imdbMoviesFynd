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
from app.Exceptions import Exceptions
from app.Utils.StatusCodes import StatusCodes


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
	try:
		if "username" not in data.keys() or "password" not in data.keys():
			raise Exceptions.ParameterError

		username = data["username"]
		password = data["password"]

		user = User.objects.filter(username = username).first() 

		if user is None: 
			user = User(username = username, password = generate_password_hash(password)).save() 
			response = { "status" : "sucess", "message" :'Successfully registered.'} 
			return make_response(jsonify(response), StatusCodes.ResponsesCode_200) 
		else:
			response = { "status" : "sucess", "message" :'User already exists. Please Log in.'} 
			return make_response(jsonify(response), StatusCodes.ResponsesCode_200)

	except Exceptions.ParameterError:
		response = Exceptions.getReponseMessage(
		"ParameterError", "username or password missing"
		)
		logger.error('username or password missing in request')
		return make_response(jsonify(response), StatusCodes.ResponsesCode_400)


	except Exception as e:
		logger.warning(str(e))
		response = Exceptions.getReponseMessage("InternalServerError", (str(e)))
		return make_response(jsonify(response), StatusCodes.ResponsesCode_500)
