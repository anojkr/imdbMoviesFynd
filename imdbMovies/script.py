import json, requests

f = open(
    "imdb.json",
)
data = json.load(f)

for record in data:
    url = "http://localhost:5000/v1/movies"
    header = {"Content-Type": "application/json"}
    response = requests.post(url=url, data=json.dumps(record), headers=header)
    print(response)
    # breaka
