string = 'Каждую минуту на Земле происходит около 1440 рождений. В течение одного дня это число достигает 2073756, а за год – более 756 миллионов. Статистика показывает, что в 2023 году численность населения мира составила 8 миллиардов человек. Из них примерно 72 процента проживает в Азии, 12 – в Африке, 10 – в Европе, а оставшиеся 6 – в обеих Америках и Океании. Интересно, что 30 процентов населения имеют доступ к бесплатному образованию, а около 12 живут за чертой бедности. В то же время, средняя продолжительность жизни увеличилась до 72 лет. Текущая рождаемость – 18 на каждую тысячу человек, а уровень смертности – 7 на тысячу. Ожидается, что к 2050 году численность населения достигнет 10 миллиардов. Для поддержания такого роста необходимо более 50 миллионов тонн продовольствия ежегодно, что требует колоссальных усилий по сохранению экологии планеты.'
# sdgs 1400.
# print('aaa'.isdigit()) #false
# print('463574'.isdigit()) #true
# print('dh5678gff'.isdigit()) #false
# 1
clean_str = string.replace('. ', ' ')
print(clean_str)
# 2 превращаем строку в список
list_from_str = clean_str.split(' ')
print(list_from_str)
# 3 фильтруем список и оставляем только цифры
filter_str = list(filter(lambda x: x.isdigit(), list_from_str))
print(filter_str)
# 4 цикл в котором устанавливаем порядковые номера и считаем частоту
results = {}
# {'1440': 1, '756': 1, '10':2 }
# {'число': частота(ков-раз)}
res = []

for i in range(len(filter_str)): #i-индекс элемента
    if filter_str[i] in results:
        results[filter_str[i]] += 1
    else:
        results[filter_str[i]] = 1


# неправильно
# for i in range(len(filter_str)): # [0, 1, 2, 3]
#     for key, value in results.items(): #[('1440', 1), ('756', 1), ('2023', 1)]
#         res.append((i, key, value))
# print(results)
# print(res)
# enumerate()
print(results)
for i, num in enumerate(results): # i-индекс, num-ключ, results[num]-значение
    res.append((i, num, results[num]))
print(res)

t = {'id': 1, 'name': 'Sasha', 'city': 'NSK'}
print(t.keys())
print(t.values())
print(t.items())

# for hour in range(24):
#     for minute in range(60):
#         for seconds in range(60):
#             print(f'{hour}:{minute}:{seconds}') #0:1, 0:2, 0:3



