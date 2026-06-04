restaurants_data = [
    {
        "name": "Уголек",
        "cuisine": "русская",
        "year_opened": 2015,
        "rating": 4.8,
        "signature_dishes": [
            {"name": "борщ", "type": "суп"},
            {"name": "пельмени", "type": "основное"},
            {"name": "медовик", "type": "десерт"}
        ]
    },
    {
        "name": "Сакура",
        "cuisine": "японская",
        "year_opened": 2018,
        "rating": 4.9,
        "signature_dishes": [
            {"name": "роллы Филадельфия", "type": "основное"},
            {"name": "рами", "type": "суп"},
            {"name": "моти", "type": "десерт"},
            {"name": "сашими", "type": "основное"}
        ]
    },
    {
        "name": "Мясо & Огонь",
        "cuisine": "европейская",
        "year_opened": 2010,
        "rating": 4.7,
        "signature_dishes": [
            {"name": "стейк рибай", "type": "основное"},
            {"name": "карпаччо", "type": "закуска"}
        ]
    },
    {
        "name": "Веранда",
        "cuisine": "средиземноморская",
        "year_opened": 2020,
        "rating": 4.6,
        "signature_dishes": [
            {"name": "паста карбонара", "type": "основное"},
            {"name": "тирамису", "type": "десерт"},
            {"name": "капрезе", "type": "закуска"}
        ]
    },
    {
        "name": "Чайхана",
        "cuisine": "узбекская",
        "year_opened": 2012,
        "rating": 4.5,
        "signature_dishes": [
            {"name": "плов", "type": "основное"},
            {"name": "самса", "type": "закуска"},
            {"name": "шурпа", "type": "суп"},
            {"name": "лагман", "type": "основное"}
        ]
    },
    {
        "name": "Франсуа",
        "cuisine": "французская",
        "year_opened": 2008,
        "rating": 4.9,
        "signature_dishes": [
            {"name": "луковый суп", "type": "суп"},
            {"name": "утиное филе", "type": "основное"},
            {"name": "крем-брюле", "type": "десерт"},
            {"name": "фуа-гра", "type": "закуска"}
        ]
    }
]

# Метрика количества
total_rest = len(restaurants_data)
print(f'Всего ресторанов: {total_rest}')

# Метрика экстремумов рейтинга (самый высокий и самый низкий)
# print(min([3, 7, 9]))
# print(max([3, 7, 9]))
best_rest = max(restaurants_data, key=lambda x: x.get('rating', 0)) # .get(key, default) x['rating']
worst_rest = min(restaurants_data, key=lambda x: x.get('rating', 0))
print(f'Лидер: {best_rest['name']} ({best_rest['rating']})')
print(f'Аутсайдер: {worst_rest['name']} ({worst_rest['rating']})')

#  Самый старый ресторан
oldest_rest = min(restaurants_data, key=lambda x:x.get('year_opened', 0))
print(f'Самый старый ресторан: {oldest_rest['name']}')

# Агрегация типы блюд (частотный анализ)
# rest["signature_dishes"][i]['type']
type_counts = {} # ключ =тип блюда, значение=кол-во
# проходим по каждому ресторану
for rest in restaurants_data:
    for dish in rest['signature_dishes']:
        dish_type = dish['type']

        if dish_type in type_counts:
            type_counts[dish_type] += 1 #если уже встречалось
        else:
            type_counts[dish_type] = 1  #если встретилось впервые
print(type_counts)
print(type_counts.items())
sort_type = sorted(type_counts.items(), key=lambda x: x[1], reverse=True)
print(sort_type[:3])




l = [26, 81, 11, 38, 9, 99]
print(sorted(l, reverse=True)[:3])
# [start:end:step]
print(l[2::2])
