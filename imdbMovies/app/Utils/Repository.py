from app.Models.UserModels import User
import jwt
from app.Config.settings import Config
from functools import wraps
from flask import request, jsonify
from app.Utils.StatusCodes import StatusCodes

SECRET_KEY = Config.SECRET_KEY

# Decorator to verify jwt-token
def admin_jwt_token_verify(f):
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
            if data["usertype"] == "ADMIN":
                User.objects(username=data["username"]).first()
            else:
                return (
                    jsonify({"message": "User not permitted to access api !!"}),
                    StatusCodes.ResponsesCode_400,
                )
        except:
            return (
                jsonify({"message": "authentication token is invalid !!"}),
                StatusCodes.ResponsesCode_400,
            )
        return f(*args, **kwargs)

    return decorated


# Decorator to verify jwt-token
def client_jwt_token_verify(f):
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
            if data["usertype"] == "CLIENT":
                User.objects(username=data["username"]).first()
            else:
                return (
                    jsonify({"message": "User not permitted to access api!!"}),
                    StatusCodes.ResponsesCode_400,
                )
        except:
            return (
                jsonify({"message": "authentication token is invalid !!"}),
                StatusCodes.ResponsesCode_400,
            )
        return f(*args, **kwargs)

    return decorated