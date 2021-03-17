import os
import json
import unittest
import requests
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

    useruid = None
    movieid = None
    token = None

    def test_user_01(self):

        LOGIN_URL = HOST + "/v1/user/signup"
        login_data = {"username": "test", "password": "test"}

        response = requests.post(
            url=LOGIN_URL,
            data=json.dumps(login_data),
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(response.status_code, 200)

    def test_user_02(self):

        LOGIN_URL = HOST + "/v1/user/login"
        login_data = {"username": "test", "password": "test"}

        response = requests.post(
            url=LOGIN_URL,
            data=json.dumps(login_data),
            headers={"Content-Type": "application/json"},
        )
        self.token = json.loads(response.content)["token"]
        self.assertEqual(response.status_code, 200)

    def test_add_movies_01(self):

        data = copy.deepcopy(TestMovies.data)
        URL = HOST + "/api/v1/add/movies"
        headers = {"Content-Type": "application/json", "jwt-token": self.token}

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
