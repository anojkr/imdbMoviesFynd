from app.Models.UserModels import User
import jwt
from app.Config.settings import Config
from functools import wraps
from flask import request, jsonify
from app.Utils.StatusCodes import StatusCodes

SECRET_KEY = Config.SECRET_KEY


def jwt_token_verify(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "jwt-token" in request.headers:
            token = request.headers["jwt-token"]

        if not token:
            return (
                jsonify({"message": "authentication token missing !!"}),
                StatusCodes.ResponsesCode_400,
            )

        try:
            data = jwt.decode(token, SECRET_KEY)
            User.objects(username=data["username"]).first()
        except:
            return (
                jsonify({"message": "authentication token is invalid !!"}),
                StatusCodes.ResponsesCode_400,
            )
        return f(*args, **kwargs)

    return decorated
