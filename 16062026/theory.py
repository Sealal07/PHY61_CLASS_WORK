#GIL
# import threading
#
# def heavy():
#     # ПОТОКИ И АССИНХРОННОСТЬ БЕСПОЛЕЗНЫ
#     for _ in range(10000000):
#         print('_')
#     for _ in range(10):
#         print('__')


# ПРОЦЕСС ПОД КАПОТОМ
# print('hello')
# 1) Процесс инициализируется
# 2)Процесс получает:
# - PID
# - Память
# - Таблицу файлов
# - Потоки

# import multiprocessing
import time
import os

def worker():
    print('процесс начал работу')
    time.sleep(3)
    print('процесс завершил работу')
    print(os.getpid())

def main():
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join() #ждем завершения процесса
    print('главный процесс завершен')
    print(os.getpid())

# if __name__ == '__main__':
#     main()

#     ПАРАЛЛЕЛЬНОСТЬ РАБОТЫ ПРОЦЕССОВ
def task():
    time.sleep(3)

# if __name__ == '__main__':
#     start = time.time()
#     p1 = multiprocessing.Process(target=task)
#     p2 = multiprocessing.Process(target=task)
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print(time.time()-start)

# РАЗДЕЛЕНИЕ ПАМЯТИ
counter = 0

def p_count(name):
    global counter
    counter += 1
    print(f'в процессе: {counter}')
    print(name)

# if __name__=='__main__':
#     p = multiprocessing.Process(target=p_count,
#                                 args=('IVAN',))
#     p.start()
#     p.join()
#     print(f'в главном: {counter}')

def square(x):
   return x * x

# if __name__ == '__main__':
#     p = multiprocessing.Process(target=square,
#                                 args=(5,))
#     p.start()
#     p.join()
#     print(p)

from multiprocessing import Process, Queue

def worker_p(q):
    for i in range(5):
        q.put(i)
    # q.put('Привет из процесса')

if __name__ == '__main__':
    q = Queue()
    p = Process(target=worker_p, args=(q,))
    p.start()
    # message = q.get()
    for _ in range(3):
        print(q.get())
    print(q.get())
    p.join()
    # print(message)









