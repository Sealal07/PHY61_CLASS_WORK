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