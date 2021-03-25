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
from app.Utils.Repository import admin_jwt_token_verify, client_jwt_token_verify


blueprint = Blueprint("movies", __name__)


LIMIT = Config.LIMIT
dictConfig(Config.LOGGER_CONFIGURATION)
logger = logging.getLogger(__name__)


@blueprint.route("/")
def welcome_user():
    return "Imdb api service"


@blueprint.route("/api/v1/add/movies", methods=["POST"])
@admin_jwt_token_verify
def add_movies():
    """
    A POST API to add movie record on database
    Request API : /api/v1/add/movies

    headers = {"Content-Type": "application/json",
        "jwt-token" : "token-value"
     }

    Request Body :  {
        "99popularity": 88.0,
        "director": "George Lucas",
        "genre": [
          "Action",
          " Adventure",
          " Fantasy",
          " Sci-Fi"
        ],
        "imdb_score": 8.8,
        "name": "Star Wars"
    }

    Response:
    :RETURN: 200, {"status" : "sucess", "movieid" : "15a084e7-27da-4818-9e24-1cb88799b46c"}
    :RETURN: 400, Bad Request
    :RETURN: 500, Internal Server Error
    """
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
                response = {"status": "sucess", "movieid": movie.uid}
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


@blueprint.route("/api/v1/update/movies", methods=["PUT"])
@admin_jwt_token_verify
def edit_movies():
    """
    A PUT API to add movie record on database
    Request API : /api/v1/update/movies?movieid=15a084e7-27da-4818-9e24-1cb88799b46c

    headers = {"Content-Type": "application/json",
        "jwt-token" : "token-value"
     }

    Request Body :  {
        "99popularity": 89.0,
        "director": "George Methew",
        "genre": [
          "Action",
          " Fantasy",
          " Sci-Fi"
        ],
        "imdb_score": 8.9,
        "name": "Star Wars"
    }

    Response:
    :RETURN: 200, {"status" : "sucess", "movieid" : "15a084e7-27da-4818-9e24-1cb88799b46c"}
    :RETURN: 400, Bad Request
    :RETURN: 500, Internal Server Error
    """
    if request.method == "PUT":
        movieid = request.args.get("movieid", None)
        try:
            data = request.json
            (
                popularity,
                director,
                genreList,
                imdbScore,
                movieName,
            ) = DataParser.validateRequestData(data)

            movie, flag = MoviesDAO.updateMovies(movieid = movieid,
                popularity=popularity,
                director=director,
                imdbScore=imdbScore,
                movieName=movieName,
                genreList=genreList,
            )

            if flag is True:
                response = {"status": "sucess", "movieid": movie.uid}
                logger.info(
                    "movie = {} sucessfully updated in database".format(movieName)
                )
                return make_response(jsonify(response), StatusCodes.ResponsesCode_200)

            elif flag is False:
                logger.info("error updating movie")
                response = {"status": "fail", "message": "no record found in database"}
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


@blueprint.route("/api/v1/remove/movies", methods=["DELETE"])
@admin_jwt_token_verify
def delete_movie():
    """
    A DELETE API to remove databse record from Movies datamodel based on uid parameter
    Request API : /api/v1/remove/movies?movieid=rad123omodzoipaosd

    Response:
    :RETURN : 200, {"status" : "sucess"}
    :RETURN : 400 Bad Request
    :RETURN : 500 Internal Server Error
    """
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


@blueprint.route("/api/v1/get/movies", methods=["GET"])
@client_jwt_token_verify
def get_movies():
    """
    A GET API to get list of all movies in database
    Request API : /api/v1/get/movies

    Response:
    :RETURN 200, {
                    "data": {
                        "Cabiria": {
                            "director": "Giovanni Pastrone",
                            "genre_list": [
                                "Adventure",
                                "Drama",
                                "War"
                            ],
                            "imdb_score": 6.6,
                            "movieName": "Cabiria",
                            "movieid": "e856a522-8354-400a-bd65-01e9808db743",
                            "popularity": 66.0
                            },
                    "status" : "sucess"
                }

    :RETURN 400, Bad Request
    :RETURN 500, Internal Server Error

    """
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


@blueprint.route("/api/v1/get/search/movies", methods=["GET"])
@client_jwt_token_verify
def search_movies():
    """
    A GET API to search for movies based on different parameters
    Request API : /api/v1/get/search/movies?popularity=90&name=Batman&genre=Adventure&imdbscore=9&page=0
    All are optional parameters

    genre (can be choosen form below list) : ["Fiction", "Fantasy", "Adventure", "Family", "Musical"
    , "Action", "Sci-Fi", "Drama", "War", "Mystery", "Thriller"]

    Response:
    :RETURN 200, {
                    "data": {
                        "Cabiria": {
                            "director": "Giovanni Pastrone",
                            "genre_list": [
                                "Adventure",
                                "Drama",
                                "War"
                            ],
                            "imdb_score": 6.6,
                            "movieName": "Cabiria",
                            "movieid": "e856a522-8354-400a-bd65-01e9808db743",
                            "popularity": 66.0
                            },
                    "status" : "sucess"
                }
    :RETURN: 500, Internal Server Error

    """
    if request.method == "GET":

        try:
            popularity = float(request.args.get("popularity", 0.0))
            movieName = request.args.get("name", None)
            director = request.args.get("director", None)
            genre = request.args.get("genre", None)
            imdbScore = float(request.args.get("imdbscore", 0.0))
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
