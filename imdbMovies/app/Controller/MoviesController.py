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
from app.Config.settings import LIMIT
from app.Exceptions import Exceptions
from app.Utils.StatusCodes import StatusCodes

blueprint = Blueprint("movies", __name__)


@blueprint.route("/")
def homepageView():
    """
    A test API to check if flask is properly configured
    :return:
    """
    return "Welcome to IMDB API"


@blueprint.route("/v1/add/movies", methods=["POST"])
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

            response = {"status": "sucess"}
            return make_response(jsonify(response), 200)

        except Exceptions.InputOutOfBounds:
            response = Exceptions.getReponseMessage("InputOutOfBounds", "input value not valid")
            return make_response(jsonify(response), StatusCodes.ResponsesCode_400)

        except Exceptions.ParameterError:
            response = Exceptions.getReponseMessage("ParameterError", "missing input parameter")
            return make_response(jsonify(response), StatusCodes.ResponsesCode_400)

        except Exception as e:
            response = Exceptions.getReponseMessage("InternalServerError", (str(e)))
            return make_response(jsonify(response), StatusCodes.ResponsesCode_500)


@blueprint.route("/v1/get/movies", methods=["GET"])
def get_movies():

    if request.method == "GET":

        try:
            page = int(request.args.get("page", 0))

            queryResp = MoviesDAO.getMovieList(page, LIMIT)
            response = MoviesSerializer(queryResp).getReponse()
            resp = {"status": "sucess", "data": response}

            return make_response(jsonify(resp), 200)

        except Exception as e:
            response = Exceptions.getReponseMessage("InternalServerError", (str(e)))
            return make_response(jsonify(response), StatusCodes.ResponsesCode_500)


@blueprint.route("/v1/get/search/movies", methods=["GET"])
def search_movies():

    if request.method == "GET":

        try: 
            page = int(request.args.get("page", 0))
            popularity = float(request.args.get("popularity", 0.0))
            movieName = request.args.get("name", None)
            director = request.args.get("director", None)
            genre = request.args.get("genre", None)
            imdbScore = request.args.get("imdbscore", 0)

            searchResult = MoviesDAO.getSearchResult(
                popularity, movieName, director, genre, imdbScore, page, LIMIT
            )

            response = MoviesSerializer(searchResult).getReponse()

            resp = {"status": "sucess", "data": response}
            return make_response(jsonify(resp), 200)
            
        except Exception as e:
            response = Exceptions.getReponseMessage("InternalServerError", (str(e)))
            return make_response(jsonify(response), StatusCodes.ResponsesCode_500)