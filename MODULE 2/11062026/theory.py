# Состояние гонки (race condition)
#
# import asyncio
#
# shared_balance = 100
# balance_lock = asyncio.Lock()
#
# async def withdraw(amount, account_holder):
#     global shared_balance
#     # запрашиваем блокировку. если она занята-корутина подождет здесь
#     async with balance_lock:
#         print(f'[{account_holder}] проверяет баланс: {shared_balance}')
#         if shared_balance >= amount:
#             await asyncio.sleep(0.1)
#             shared_balance -= amount
#             print(f'[{account_holder}], {amount}.Баланс: {shared_balance}')
#         else:
#             print(f'{account_holder}. Недостаточно средств')
#
# async def main():
#     await asyncio.gather(
#         withdraw(80, 'Вася'),
#         withdraw(60, 'Петя')
#     )
# asyncio.run(main())
#
# '''asyncio.Lock - делает операцию атомарной. Механизм синхронизации
# блокировка'''
#
# '''ГЛАВНОЕ ПРАВИЛО АССИНХРОННОСТИ: если между проверкой общего
# состояния и его изменением есть хотябы один await-этот кусок
# кода обязан быть защищен блокировкой'''
#
#
# # ПЛОХОЙ ПРИМЕР: ТАК ДЕЛАТЬ НЕЛЬЗЯ!!!
# is_locked = False
#
# async def bad_withdraw():
#     global is_locked
#     if not is_locked:
#         is_locked = True
#         await asyncio.sleep(0.1)
#         is_locked = False
#
# '''if not is_locked и ее изменение должны происходить атомарно,
#     без единого await
# '''


'''
ПОТОКИ - позволяют выполнять код ПАРАЛЛЕЛЬНО.
Threads - обработка, выполнение которой назначается ОС.
Работают внутри одного ПРОЦЕССА и делят между собой общую память
'''
# переключением управляет ОС
import threading
import time

def worker(name, delay):
    print(f'поток {name} начинает работу')
    time.sleep(delay)
    print(f'поток {name} завершил работу')

def main():
    print(f'[главный поток]. запуск дочерних потоков')
    thread_1 = threading.Thread(target=worker, args=('Петя', 2))
    thread_2 = threading.Thread(target=worker, args=('Вася', 1))
    # запускаем потоки (они начинают выполняться параллельно)
    thread_1.start()
    thread_2.start()
    print(f'[главный поток]. ждем завершения пети и васи')
    thread_1.join()
    thread_2.join()
    print('[главный поток]. программа окончена')

# main()

shared_balance = 100
balance_lock = threading.Lock()

def withdraw(account_holder, amount):
    global shared_balance
    with balance_lock:
        print(account_holder, shared_balance)
        if shared_balance >= amount:
            time.sleep(0.1)
            shared_balance -= amount
            print(account_holder, amount, shared_balance)
        else:
            print(account_holder, 'недостаточно средств')

def main_2():
    t1 = threading.Thread(target=withdraw, args=('Петя', 80))
    t2 = threading.Thread(target=withdraw, args=('Вася', 60))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

main_2()






