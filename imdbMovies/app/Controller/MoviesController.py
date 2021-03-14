"""
This file contains API endpoints which would be exposed to the outer world
"""
import json
from flask import Blueprint, request
from flask import jsonify, make_response
from app.Validations.Validatior import Validator

from app.DAO.CastDao import CastDAO
from app.DAO.GenresDao import GenresDAO
from app.DAO.MovieCastDao import MovieCastDAO
from app.DAO.MovieGenresDao import MovieGenresDAO
from app.DAO.MoviesDao import MoviesDAO
import uuid
from mongoengine import *
from mongoengine import connect

LIMIT = 10
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

    if request.method == "POST":
        try:
            data = request.json
            popularity, director, genreList, imdbScore, movieName = Validator.parse_json(data)
            movie = MoviesDAO.addMovies(
                popularity=popularity,
                director=director,
                imdbScore=imdbScore,
                movieName=movieName,
                genreList=genreList,
            )

            d = {"status": "sucess"}
            return make_response(jsonify(d), 200)
        except Exception as e:
            response = {"status": "fail"}
            return make_response(response, 500)


@blueprint.route("/v1/getmovies", methods=["GET"])
def get_movies():

    if request.method == "GET":
        page = int(request.args.get('page', 0))
        resp = MoviesDAO.getMovie(10, page)
        movie_list = []
        for movie in resp:
            items = MovieGenresDAO.getByMovie(movie.movieName, page, 10)
            movie_list.append({"movie": movie.movieName})

        resp = {"total": 1, "data": movie_list}
        return make_response(jsonify(resp), 200)


@blueprint.route("/v1/search/movies", methods=["GET"])
def search_movies():

    if request.method == "GET":
        page = int(request.args.get('page', 0))
        popularity = float(request.args.get('popularity', 0.0))
        movieName = request.args.get('name', None)
        director = request.args.get('director', None)
        genre = request.args.get('genre', None)
        imdbScore = request.args.get('imdbscore', 0)

        movieSet = set()
        # print('Popularity Result')
        # print(popularity)
        # popularityResponse = MoviesDAO.getmoviesPopularity(popularity, page, LIMIT)
        # print(popularityResponse.count())

        # print('Imdnameb Score Result')
        # print(imdbScore)
        # imdbscoreResponse = MoviesDAO.getmoviesImdbScore(imdbScore, page, 10)
        # print(imdbscoreResponse.count())


        print('Search  Result')
        # print(imdbScore)
        imdbscoreResponse = MoviesDAO.getSearchResult(popularity, movieName, director, genre, imdbScore, page, 10)
        # print(imdbscoreResponse)
        for item in imdbscoreResponse:
            print(item.popularity, item.imdbScore, item.movieName)
        # resp = MoviesDAO.getMovie(10, page)
        # movie_list = []
        # for movie in resp:

        #     items = MovieGenresDAO.getByMovie(movie.movieName, page, LIMIT)
        #     movie_list.append({"movie": movie.movieName})

        resp = {"total": 1, "data": 'movie_list'}
        return make_response(jsonify(resp), 200)