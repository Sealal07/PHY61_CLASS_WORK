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
    # print(response.url)
    # print(response.json())
    # шаг 1.3
    if response.status_code != 200:
        raise RuntimeError(
            f'Ошибка запроса! Код ответа: {response.status_code}. Текст: {response.text}'
        )

    return response.json()

# print(fetch_movies_data())

# шаг 1.4 локальное кэширование данных
def cache_data_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f'Данные закэширвоанны в файл {filename}')


# шаг 2.1
def load_cached_movies(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
            print("Ошибка: Файл кэша отсутствует. Сначала запустите скрипт из Части 1.")
            return None

# шаг 2.2.аналитический движок
def analyze_movies(data):
    pass



def main():
    print('ЧАСТЬ 1. Получение и кэширование данных')
    try:
        data = fetch_movies_data()
        cache_data_to_json(data, 'cache_movies.json')
    except Exception as e:
        print(f'Ошибка в ЧАСТИ 1: {e}')

    print('ЧАСТЬ 2. Локальный анализ данных')
main()


