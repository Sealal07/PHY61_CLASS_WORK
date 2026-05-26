# РАБОТА С ФАЙЛАМИ
# чтение  'r'  read
# ПРИ 'a' и 'w' автоматически создаст файл если его еще не существует
# дозапись  'a'  append
# запись (перезаписывает все содержимое)  'w'  write

# открытие файла open(nameFile, режим, кодировка)
file = open('example.txt', 'r', encoding='utf8')
# чтение всего содержимого файла .read()
# print(file.read())

# чтение одной строки в файле .readline()
# print(file.readline())
# print(file.readline())
# print(file.readline())

# чтение всех строк (возвращает список строк) .readlines()
# print(file.readlines())

# чтение циклом файла
for line in file:
    print(line)
#    закрытие файла
file.close()


#  не требует ручного закрытия
with open('example.txt', 'a', encoding='utf8') as f:
    string = '\nnew line'
    # метод записи в файл .write()
    f.write(string)
    # запись нескольких строк .writelines(list_str)
    list_str = ['a\n', 'b\n', 'c\n']
    f.writelines(list_str)

with open('example.txt', 'w', encoding='utf8') as f:
    f.write('ВСЕ СОДЕРЖИМОЕ СТЕРЛОСЬ')