# Exception

# KeyError FileNotFoundError IndexError ZeroDivisionError

try:
    x = int(input())
    y = int(input())
    print(x / y)
except ValueError:
    print('нужно ввести цифру')
except ZeroDivisionError:
    print('на ноль делить нельзя')
except Exception as e:
    print(e)
finally:
    print('вывод finally')


age = int(input())
if age >= 18:
    print('доступ есть')
else:
    raise ValueError('человек должен быть совершеннолетним')

