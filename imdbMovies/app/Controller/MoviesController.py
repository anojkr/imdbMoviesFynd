"""
This file contains API endpoints which would be exposed to the outer world
"""
import json
from flask import Blueprint, request
from flask import jsonify, make_response
from app.Validations.Validatior import Validator

from app.DAO.MoviesDao import MoviesDAO
import uuid
from mongoengine import *
from mongoengine import connect

blueprint = Blueprint("movies", __name__)


class MissingFields(Exception):
    pass


@blueprint.route("/")
def homepageView():
    """
    A test API to check if flask is properly configured
    :return:
    """
    return "Welcome to IMDB API"


@blueprint.route("/v1/movies", methods=["POST"])
def add_movies():
    # try:
    # data = json.loads(request.data)

    # if not data:
    #     raise MissingFields

    data = {
        "99popularity": 83.0,
        "director": "Victor Fleming",
        "genre": ["Adventure", " Family", " Fantasy", " Musical", "Adventure"],
        "imdb_score": 8.3,
        "name": "The Wizard of Oz",
    }
    # popularity, director, genre_list, imdb_score, name = Validator.parse_json(data)
    popularity = data["99popularity"]
    director = data["director"]
    genreList = data["genre"]
    imdbScore = data["imdb_score"]
    movieName = data["name"]

    movie = MoviesDAO.addMovies(
        popularity=popularity,
        director=director,
        imdbScore=imdbScore,
        movieName=movieName,
        genreList=genreList,
    )
    print(movie.movieName)
    d = {"data": "movie"}
    print(d)
    return make_response(jsonify(d), 200)


# except Exception as e:
# 	d = {"details" : "failure"}
# 	return make_response(jsonify(d), 200)


@blueprint.route("/v1/getmovies", methods=["GET"])
def get_movies():
    #     try:
    # with terminating_sn() as session:
    resp = MoviesDAO.getMovie(10, 0)
    movie_list = []
    for movie in resp:
        print(movie.movieName)
        # movie_id, popularity, director, genre_blob, imdb_score, name = movie
        # movie_list.append({'id': movie_id, '99popularity': popularity, 'director': director,
        # 'imdb_score': imdb_score, 'name': name})
        movie_list.append({"movie": movie.movieName})

    resp = {"total": 1, "data": movie_list}
    return make_response(jsonify(resp), 200)


#     except as E:
#         d = {"details" : "failure"}
#         return make_response(jsonify(d), 200)
