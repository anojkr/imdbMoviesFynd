"""
This file contains API endpoints which would be exposed to the outer world
"""
import json
from flask import Blueprint, request
from flask import jsonify, make_response

import uuid
import jwt
from datetime import datetime, timedelta
from mongoengine import connect

from app.Exceptions import Exceptions
from app.Utils.StatusCodes import StatusCodes
from app.Models.UserModels import User

import logging
from app.Config.settings import Config
from logging.config import dictConfig
from werkzeug.security import generate_password_hash, check_password_hash
from app.Exceptions import Exceptions
from app.Utils.StatusCodes import StatusCodes


auth_blueprint = Blueprint("auth", __name__)

LIMIT = Config.LIMIT
SECRET_KEY = Config.SECRET_KEY
dictConfig(Config.LOGGER_CONFIGURATION)
logger = logging.getLogger(__name__)


@auth_blueprint.route("/user/login")
def homepageView():
    """
    A test API to check if flask is properly configured
    :return:
    """
    return "Welcome to login API"


@auth_blueprint.route("/v1/user/signup", methods=["POST"])
def signup_user():
    """
    A POST API to singup user-account
    
    Request API : /v1/user/signup
    Request Body:
    {
        "username" : "testing",
        "password" : "testing",
    }

    Response :
    :RETURN : {
                "status": "sucess",
                "message": "Successfully registered.",
                "uid": "35898034-a4rf-5d5e-9cb6-1be25923db04",
              }
    :RETURN : 400, Bad Request
    :RETURN : 500, Internal Server Error

    """
    data = request.json
    try:
        if "username" not in data.keys() or "password" not in data.keys():
            raise Exceptions.ParameterError

        username = data["username"]
        password = data["password"]

        if username == "" or password == "":
            response = {
                "status": "fail",
                "message": "username or password cannot be empty",
            }
            return make_response(jsonify(response), StatusCodes.ResponsesCode_400)

        user = User.objects.filter(username=username).first()

        if user is None:
            user = User(
                username=username, password=generate_password_hash(password)
            ).save()
            response = {
                "status": "sucess",
                "message": "Successfully registered.",
                "uid": user.uid,
            }
            return make_response(jsonify(response), StatusCodes.ResponsesCode_200)
        else:
            response = {
                "status": "fail",
                "message": "User already exists. Please Log in.",
            }
            return make_response(jsonify(response), StatusCodes.ResponsesCode_200)

    except Exceptions.ParameterError:
        response = Exceptions.getReponseMessage(
            "ParameterError", "username or password missing"
        )
        logger.error("username or password missing in request")
        return make_response(jsonify(response), StatusCodes.ResponsesCode_400)

    except Exception as e:
        logger.warning(str(e))
        response = Exceptions.getReponseMessage("InternalServerError", (str(e)))
        return make_response(jsonify(response), StatusCodes.ResponsesCode_500)


@auth_blueprint.route("/v1/user/login", methods=["POST"])
def login():
    """
    A POST API to login user-account
    
    Request API : /v1/user/login
    Request Body:
    {
        "username" : "testing",
        "password" : "testing",
    }

    Response :
    :RETURN : {
                "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
              }
    :RETURN : 400, Bad Request
    :RETURN : 500, Internal Server Error

    """
    try:
        data = request.json

        if "username" not in data.keys() or "password" not in data.keys():
            raise Exceptions.ParameterError

        username = data["username"]
        password = data["password"]

        user = User.objects.filter(username=username).first()

        if user is None:
            response = {"status": "fail", "message": "User does not exist"}
            return make_response(jsonify(response), StatusCodes.ResponsesCode_200)

        if check_password_hash(user.password, password):
            token = jwt.encode(
                {
                    "username": user.username,
                    "exp": datetime.utcnow() + timedelta(minutes=30),
                },
                SECRET_KEY,
            )

            return make_response(
                jsonify({"token": token.decode("UTF-8")}), StatusCodes.ResponsesCode_200
            )

        response = {"status": "fail", "message": "Wrong password"}
        return make_response(jsonify(response), StatusCodes.ResponsesCode_200)

    except Exceptions.ParameterError:
        response = Exceptions.getReponseMessage(
            "ParameterError", "username or password missing"
        )
        logger.error("username or password missing in request")
        return make_response(jsonify(response), StatusCodes.ResponsesCode_400)

    except Exception as e:
        logger.warning(str(e))
        response = Exceptions.getReponseMessage("InternalServerError", (str(e)))
        return make_response(jsonify(response), StatusCodes.ResponsesCode_500)
