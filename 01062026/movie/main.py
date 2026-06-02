import requests
import json

# шаг 1.1
API_URL = 'https://api.poiskkino.dev/v1.4/movie'
TOKEN = 'DP7GYZK-T5W4855-GSS2A69-RJFZ80F'

# шаг 1.2
def fetch_movies_data(limit=30):
    headers = {
        'X-API-KEY': TOKEN
    }
    params = {
        "limit": limit,
        "page": 1,
        "selectFields": [
            "id",
            "name",
            "year",
            "rating",
            "genres",
            "countries",
            "type",
        ],
        "notNullFields": ["name", "rating.kp", "genres.name"],
        "sortField": ["rating.kp"],
        "sortType": ["-1"],
        "type": ["movie"]
}
    response = requests.get(
        API_URL, headers=headers, params=params
    )
    print(response.json())

fetch_movies_data()
