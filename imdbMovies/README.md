


## Authentication API
- All request body in api is in json-format
#### User signup API [POST]
 API : https://imdb-movies-apps.herokuapp.com/v1/user/signup

```
User can be only of two types ADMIN and CLIENT
- "ADMIN" users allowed to add,edit and delete movie API'S mentioned below
1. https://imdb-movies-apps.herokuapp.com/api/v1/add/movies
2. https://imdb-movies-apps.herokuapp.com/api/v1/update/movies?movieid=5be4060e-0967-4e32-b7c4-dd37803e5bb3
3. https://imdb-movies-apps.herokuapp.com/api/v1/remove/movies?movieid=5be4060e-0967-4e32-b7c4-dd37803e5bb3

- "CLIENT" users can only access search and getmovies api's mentioned below
4. https://imdb-movies-apps.herokuapp.com/api/v1/get/movies
5. https://imdb-movies-apps.herokuapp.com/api/v1/get/search/movies?name=Batman
```
 ```
Request body = {
"username" : "admin",
"password" : "admin",
"usertype" : "ADMIN"
}
```
OR

 ```
Request body = {
"username" : "client",
"password" : "client",
"usertype" : "CLIENT"
}
```

    """
    A POST API to singup user-account

    Request API : /v1/user/signup
    Request Body:
    {
        "username" : "admin",
        "password" : "admin",
        "usertype" : "ADMIN"
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
------------------------------------
### User login AP [POST]
 API : https://imdb-movies-apps.herokuapp.com/v1/user/login
```
Request body = {
"username" : "admin",
"password" : "admin"
}
```

    """
    A POST API to login user-account

    Request API : /v1/user/login
    Request Body:
    {
        "username" : "admin",
        "password" : "admin"
    }

    Response :
    :RETURN : {
                "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
              }
    :RETURN : 400, Bad Request
    :RETURN : 500, Internal Server Error

    """
## IMDB-APP API

### Add movie to API [POST]
API : https://imdb-movies-apps.herokuapp.com/api/v1/add/movies

- Get jwt-token using login api
- **ADMIN** user authorized to access this api

```  
Header = {
    "jwt-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
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
```

    """
    A POST API to add movie record on database
    Request API : /api/v1/add/movies

    headers = {"Content-Type": "application/json",
        "jwt-token" : "token-value"
     }

    Request body :  {
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
--------------------------------
### Edit movie to API [PUT]
API : https://imdb-movies-apps.herokuapp.com/api/v1/update/movies?movieid=5be4060e-0967-4e32-b7c4-dd37803e5bb3

- Get jwt-token using login api
-  **ADMIN** user authorized to access this api

```  
Header = {
    "jwt-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
         }
```
```
Request Body :  {
                    "99popularity": 90.0,
                    "director": "George Thomas",
                    "genre": [
                      "Action",
                      " Sci-Fi"
                    ],
                    "imdb_score": 9.9,
                    "name": "Star Wars-II"
        }
```

    """
    A PUT API to add movie record on database
    Request API : /api/v1/update/movies?movieid=5be4060e-0967-4e32-b7c4-dd37803e5bb3

    headers = {"Content-Type": "application/json",
        "jwt-token" : "token-value"
     }

    Request body :  {
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
 ----------------------------------------
  ### List movies API [GET]
  API : https://imdb-movies-apps.herokuapp.com/api/v1/get/movies
 -- **CLIENT** users authorized to access this api
 ```
 Header = {
    "jwt-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
         }
```
    """
    A GET API to get list of all movies in database
    Request API : /api/v1/get/movies
    headers = {"Content-Type": "application/json",
        "jwt-token" : "token-value"
     }
     
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
    
-------------------------------------------------------------------------------
### Delete movie API [DELETE]
API : https://imdb-movies-apps.herokuapp.com/api/v1/remove/movies?movieid=5be4060e-0967-4e32-b7c4-dd37803e5bb3

-- **ADMIN** user authorized to access this api
```
Header = {
    "jwt-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
         }
```

    """
    A DELETE API to remove databse record from Movies datamodel based on uid parameter
    Request API : /api/v1/remove/movies?movieid=rad123omodzoipaosd
    
    headers = {"Content-Type": "application/json",
        "jwt-token" : "token-value"
     }
     
    Response:
    :RETURN : 200, {"status" : "sucess"}
    :RETURN : 400 Bad Request
    :RETURN : 500 Internal Server Error
    """
-------------------------------------------------------------------------
 ### Search movie API [GET]
API : https://imdb-movies-apps.herokuapp.com/api/v1/get/search/movies?name=Batman
-- **CLIENT** user authorized to access this api
```
Header = {
    "jwt-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
         }
```

```
optional-parameters 
{name=movie-name}
{imdbscore = 8}
{page=1}
{popularity=80}
{genre = choose from below list}
```

```
Genre list
["Fiction", "Fantasy", "Adventure", "Family", "Musical"
, "Action", "Sci-Fi", "Drama", "War", "Mystery", "Thriller"]
```
```
https://imdb-movies-apps.herokuapp.com/api/v1/get/search/movies?popularity=90&name=Batman&genre=Adventure&imdbscore=9&page=0
```

     """
    A GET API to search for movies based on different parameters
    Request API : /api/v1/get/search/movies?popularity=90&name=Batman&genre=Adventure&imdbscore=9&page=0
    
    All are optional parameters

    genre (can be choosen form below list) : ["Fiction", "Fantasy", "Adventure", "Family", "Musical"
    , "Action", "Sci-Fi", "Drama", "War", "Mystery", "Thriller"]
    
    headers = {"Content-Type": "application/json",
        "jwt-token" : "token-value"
     }

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
