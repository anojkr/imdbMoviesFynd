import os
import json
import base64

import unittest
import requests


from mongoengine import connect
import copy

HOST = "http://localhost:5000"


class TestMovies(unittest.TestCase):

    data = {
        "director": "Test Director",
        "genre": [" Fiction", " Fantasy"],
        "99popularity": 87,
        "imdb_score": 8.3,
        "name": "Test Movie",
    }

    def test_add_movies_01(self):

        data = copy.deepcopy(TestMovies.data)
        URL = HOST + "/api/v1/add/movies"
        headers = {"Content-Type": "application/json"}

        response = requests.post(url=URL, data=json.dumps(data), headers=headers)

        self.assertEqual(response.status_code, 200)

    def test_add_movies_02(self):

        data = copy.deepcopy(TestMovies.data)
        data.pop("director")

        URL = HOST + "/api/v1/add/movies"
        headers = {"Content-Type": "application/json"}

        response = requests.post(url=URL, data=json.dumps(data), headers=headers)

        self.assertEqual(response.status_code, 400)

    def test_add_movies_03(self):

        data = copy.deepcopy(TestMovies.data)
        data["imdb_score"] = 100

        URL = HOST + "/api/v1/add/movies"
        headers = {"Content-Type": "application/json"}

        response = requests.post(url=URL, data=json.dumps(data), headers=headers)

        self.assertEqual(response.status_code, 400)

    def test_get_movies_04(self):

        GETURL = HOST + "/api/v1/get/search/movies?name=Test Movie"
        headers = {"Content-Type": "application/json"}

        response = requests.get(url=GETURL, headers=headers)
        response_data = json.loads(response.content)["data"]["Test Movie"]["movieName"]

        self.assertEqual(response_data, "Test Movie")
