# HTTP протокол
# http-не защищенный
# https://example.com
# s - SSL сертификат (сертификат безопасности)
# request - запрос, response - ответ
#
# GET - получить
# POST - отправить (создать)
#
# status code
# 1xx
# 2xx
# 3xx
# 4xx
# 5xx

import json
from base64 import encode

# 1)Сериализация - объект Python переводим в строку формата JSON
dict_user = {'id': 1, 'login': 'admin', 'password': '123AA', 'numbers': [1, 2, 3], 'name': 'Иван'}
serialize = json.dumps(dict_user)
print(serialize)

with open('user.json', 'w', encoding='utf8') as f:
    # .dump(что записываем, куда записываем, indent(отступы), кодировка)
    json.dump(dict_user, f, indent=4, ensure_ascii=False)

# 2)Десериализация - строку формата JSON переводим в объект Python
json_str = '{"order": 1, "product": "phone"}'
dict_order = json.loads(json_str)
print(dict_order)
print(type(dict_order))

with open('user.json', 'r', encoding='utf8') as f:
    user = json.load(f)
    print(user)


