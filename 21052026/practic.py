# ЗАДАЧА 1

passwords = ["qwerty123", "SecretPassword", "Root!2026", "12345", "SuperAdmin"]
#
# str1 = "SecretPassword"
# num = False
# for char in str1:
#     if char.isdigit():
#          num = True
#          break
# print(num)
# # print("qwerty123".isdigit())
secure_password = []
for pwd in passwords:
    if len(pwd) > 8:
        has_digit = False

        for char in pwd:
            if char.isdigit():
                has_digit = True
                break
        if has_digit:
            secure_password.append(pwd)

print(secure_password)
# nums = [2, 5, 6, 7]
# print(any(n > 5 for n in nums))

sec_pass = list(filter(lambda pwd: len(pwd)>8 and any(char.isdigit() for char in pwd), passwords))
print(sec_pass)
# слева-направо и изнутри-наружу
# char.isdigit() for char in pwd - превращает pwd в последовательность  логических значений
# qwerty123
# False False False True

# ЗАДАЧА 2
weapons = ["Стальной меч", "Лук странника", "Посох хаоса", "Кинжал тени"]
rarity_multipliers = [1.0, 1.2, 1.5, 2.0]
# for i in range(2, 10, 2):  2  4 6 8
results = []
for i in range(len(weapons)):
    item = {'name':weapons[i], 'damage': 100*rarity_multipliers[i]}
    results.append(item)
print(results)

inventory = list(map(lambda item: {'name': item[0], 'damage': 100*item[1]},
                     zip(weapons, rarity_multipliers)))
print(inventory)

# 100 Х Коэффициент
#
# [
# {'name': 'Стальной меч', 'damage': 100.0},
# {'name': 'Лук странника', 'damage': 120.0},
# {'name': 'Посох хаоса', 'damage': 150.0},
# {'name': 'Кинжал тени', 'damage': 200.0}
# ]