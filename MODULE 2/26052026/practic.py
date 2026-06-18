# ЗАДАЧА 1

name = input('введите ваше имя: ')
age = input('введите ваш возраст: ')
color = input('введите любимый цвет: ')

with open('user.txt', 'w', encoding='utf8') as f:
    f.write(name +'\n')
    f.write(age + '\n')
    f.write(color + '\n')

with open('user.txt', 'r', encoding='utf-8') as f:
    name_l = f.readline().strip()
    age_l = f.readline().strip()
    color_l = f.readline().strip()
    string = f'Пользователь: {name_l}, Возраст: {age_l}, Цвет: {color_l}'
    print(string)

