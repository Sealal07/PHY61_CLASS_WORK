# Анонимные функции и функции высшего порядка

# 1) lambda функции
# def - постоянная, сохраняется в памяти
# lamda - создается на лету

# lambda аргументы: выражение
# def sum(x, y):
#     return x + y
# print(sum(6, 8))
#
# sum1 = lambda x, y: x + y
# print(sum1(6, 8))

# ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# 8 95 9999 99 9
# aA sasha Sasha
# .lower()  .upper()
# .split(), .replace(), .strip()
str1 = '   ax-5540-wq' # 'AX-5540-WQ'
print(str1.strip())
str2 = 'lh-99-z      '# "LH-99-Z"

clean_str = lambda s: s.strip().upper()
print(clean_str(str1))
print(clean_str(str2))

# x = 7
# def g():
#     y = 5
#     return x + y
#
# print(g())
# print(y)

tax_rate = 0.20 #НДС 20%
calculate_total = lambda price: price + (price * tax_rate)
print(calculate_total(1000)) #1200.0
tax_rate = 0.10
print(calculate_total(1000)) #1100.0


employees = [
    ('Алексей', 34, 95000),
    ('Мария', 26, 120000),
    ('Иван', 42, 80000)
]
for e in employees:
    print(e[2])

salary = [95000, 120000, 80000]
sorted_salary = sorted(salary, reverse=True)
print(sorted_salary)
# сортируем по третьему элементу кортежа (индекс 2)
sorted_employees = sorted(employees, key=lambda emp: emp[2])
print(sorted_employees)


# ФУНКЦИЯ map()
# map(function, iterable) - берет каждый элемент
# из коллекции и применяет к нему функцию и
# формирует новую последоваьтельность из результатов работы

raw_ids = ['1024', '4096', '512', '99'] # int()
int_ids = []
for i in raw_ids:
    int_ids.append(int(i))
print(int_ids)

parsed_ids = list(map(int, raw_ids))
print(parsed_ids)
# map возвращает ленивый итератор для экономии оперативки

prices = [1250.50, 430.00, 9900.99, 105.10]
# 15% скидка и округлить до 2х знаков после запятой
# round()
# a=45.768533
# print(round(a, 3))

discount = list(map(lambda p: round(p * 0.85, 2), prices))
print(discount)

users = [
    {'id': 1, 'username': 'alice', 'role': 'admin'},
    {'id': 2, 'username': 'bob', 'role': 'qa'},
    {'id': 3, 'username': 'smit', 'role': 'admin'},
    {'id': 4, 'username': 'kate', 'role': 'pm'}
]
print(users[2]['username'])
usernames = list(map(lambda u: u['username'], users))
print(usernames)


nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nums[1][1])

# filter(function, iterable)

numbers = [5, 7, 2, 9, 0, 1, 10, 23, 45]
# / % //  n % 2 == 0
chet_nums = list(filter(lambda n: n % 2 == 0, numbers))
print(chet_nums)

comments = ['отличный товар', ' ', 'быстрая доставка', ' ']
# strip() вернет пустоту для пробелов, пустая строка-False
valid_comments = list(filter(lambda c: c.strip(), comments))
print(valid_comments)

infrastructure = [
    {'ip': '127.0.0.1', 'cpu': 45},
    {'ip': '192.168.0.1', 'cpu': 89},
    {'ip': '192.0.0.2', 'cpu': 92},
    {'ip': '192.0.0.4', 'cpu': 12}
]
# данные о загрузке процессора. 85%-критический порог

overloaded = list(filter(lambda host: host['cpu'] > 85, infrastructure))
ips = [over['ip'] for over in overloaded] #списковое включение
# ips2 = []
# for over in overloaded:
#     ips2.append(over['ip'])
print(overloaded)
print(ips)


mixed_data = [42, 'hello', 3.14, True, 100, 'world', 0]
# оставить только целые числа
clean_int = list(filter(lambda x: type(x) == int or type(x) == float, mixed_data))
print(clean_int)
import math
print(math.pi)
pi = list(filter(lambda x: x == round(math.pi, 2), mixed_data))
print(pi)
