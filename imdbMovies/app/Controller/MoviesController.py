"""
This file contains API endpoints which would be exposed to the outer world
"""
import json
from flask import Blueprint, request
from flask import jsonify, make_response

from app.DAO.CastDao import CastDAO
from app.DAO.GenresDao import GenresDAO
from app.DAO.MovieCastDao import MovieCastDAO
from app.DAO.MovieGenresDao import MovieGenresDAO
from app.DAO.MoviesDao import MoviesDAO

import uuid
from app.DTO.MoviesSerializer import MoviesSerializer
from app.Utils.DataParser import DataParser
from mongoengine import connect

from app.Exceptions import Exceptions
from app.Utils.StatusCodes import StatusCodes

import logging
from app.Config.settings import Config
from logging.config import dictConfig
from app.Utils.Repository import jwt_token_verify


blueprint = Blueprint("movies", __name__)


LIMIT = Config.LIMIT
dictConfig(Config.LOGGER_CONFIGURATION)
logger = logging.getLogger(__name__)


@blueprint.route("/")
def welcome_user():
    return "Imdb api service"


@blueprint.route("/api/v1/add/movies", methods=["POST"])
# @jwt_token_verify
def add_movies():

    if request.method == "POST":
        try:
            data = request.json
            (
                popularity,
                director,
                genreList,
                imdbScore,
                movieName,
            ) = DataParser.validateRequestData(data)

            movie, flag = MoviesDAO.addMovies(
                popularity=popularity,
                director=director,
                imdbScore=imdbScore,
                movieName=movieName,
                genreList=genreList,
            )

            if flag is True:
                response = {"status": "sucess", "movieid" : movie.uid}
                logger.info(
                    "movie = {} sucessfully saved in database".format(movieName)
                )
                return make_response(jsonify(response), StatusCodes.ResponsesCode_200)

            elif flag is False:
                logger.info("duplicate data issue")
                response = {"status": "fail", "message": "duplicate data"}
                return make_response(jsonify(response), StatusCodes.ResponsesCode_200)

        except Exceptions.InputOutOfBounds:
            response = Exceptions.getReponseMessage(
                "InputOutOfBounds", "input value not valid"
            )
            logger.error("parameter value outofbound in request")
            return make_response(jsonify(response), StatusCodes.ResponsesCode_400)

        except Exceptions.ParameterError:
            response = Exceptions.getReponseMessage(
                "ParameterError", "missing input parameter"
            )
            logger.error("missing parameter in request")
            return make_response(jsonify(response), StatusCodes.ResponsesCode_400)

        except Exception as e:
            logger.warning(str(e))
            response = Exceptions.getReponseMessage("InternalServerError", (str(e)))
            return make_response(jsonify(response), StatusCodes.ResponsesCode_500)


@blueprint.route("/api/v1/get/movies", methods=["GET"])
def get_movies():

    if request.method == "GET":

        try:
            page = int(request.args.get("page", 0))

            queryResp = MoviesDAO.getMovieList(page, LIMIT)
            response = MoviesSerializer(queryResp).getReponse()
            resp = {"status": "sucess", "data": response}
            return make_response(jsonify(resp), StatusCodes.ResponsesCode_200)

        except Exception as e:
            logger.warning(str(e))
            response = Exceptions.getReponseMessage("InternalServerError", (str(e)))
            return make_response(jsonify(response), StatusCodes.ResponsesCode_500)


@blueprint.route("/api/v1/remove/movies", methods=["DELETE"])
@jwt_token_verify
def delete_movie():

    if request.method == "DELETE":

        try:
            movieID = request.args.get("movieid", None)

            if movieID is None:
                raise Exceptions.ParameterError

            response = MoviesDAO.deleteMovie(movieID)

            if response is True:
                resp = {"status": "sucess"}
                logger.info("movie sucessfully deleted from records")
                return make_response(jsonify(resp), StatusCodes.ResponsesCode_200)
            else:
                raise Exceptions.InvalidOperation

        except Exceptions.ParameterError:
            response = Exceptions.getReponseMessage(
                "ParameterError", "missing input parameter"
            )
            logger.error("missing parameter in request")
            return make_response(jsonify(response), StatusCodes.ResponsesCode_400)

        except Exceptions.InvalidOperation:
            response = Exceptions.getReponseMessage(
                "InvalidOperation", "invalid movieid"
            )
            logger.error("invalid movieid in request")
            return make_response(jsonify(response), StatusCodes.ResponsesCode_400)

        except Exception as e:
            logger.warning(str(e))
            response = Exceptions.getReponseMessage("InternalServerError", (str(e)))
            return make_response(jsonify(response), StatusCodes.ResponsesCode_500)


@blueprint.route("/api/v1/get/search/movies", methods=["GET"])
def search_movies():

    if request.method == "GET":

        try:
            popularity = float(request.args.get("popularity", 0.0))
            movieName = request.args.get("name", None)
            director = request.args.get("director", None)
            genre = request.args.get("genre", None)
            imdbScore = request.args.get("imdbscore", 0)
            page = int(request.args.get("page", 0))

            searchResult = MoviesDAO.getSearchResult(
                popularity, movieName, director, genre, imdbScore, page, LIMIT
            )

            response = MoviesSerializer(searchResult).getReponse()
            resp = {"status": "sucess", "data": response}
            return make_response(jsonify(resp), StatusCodes.ResponsesCode_200)

        except Exception as e:
            logger.warning(str(e))
            response = Exceptions.getReponseMessage("InternalServerError", (str(e)))
            return make_response(jsonify(response), StatusCodes.ResponsesCode_500)
