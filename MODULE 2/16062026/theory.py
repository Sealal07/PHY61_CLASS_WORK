# #GIL
# # import threading
# #
# # def heavy():
# #     # ПОТОКИ И АССИНХРОННОСТЬ БЕСПОЛЕЗНЫ
# #     for _ in range(10000000):
# #         print('_')
# #     for _ in range(10):
# #         print('__')
#
#
# # ПРОЦЕСС ПОД КАПОТОМ
# # print('hello')
# # 1) Процесс инициализируется
# # 2)Процесс получает:
# # - PID
# # - Память
# # - Таблицу файлов
# # - Потоки
#
# # import multiprocessing
# import time
# import os
#
# def worker():
#     print('процесс начал работу')
#     time.sleep(3)
#     print('процесс завершил работу')
#     print(os.getpid())
#
# def main():
#     p = multiprocessing.Process(target=worker)
#     p.start()
#     p.join() #ждем завершения процесса
#     print('главный процесс завершен')
#     print(os.getpid())
#
# # if __name__ == '__main__':
# #     main()
#
# #     ПАРАЛЛЕЛЬНОСТЬ РАБОТЫ ПРОЦЕССОВ
# def task():
#     time.sleep(3)
#
# # if __name__ == '__main__':
# #     start = time.time()
# #     p1 = multiprocessing.Process(target=task)
# #     p2 = multiprocessing.Process(target=task)
# #     p1.start()
# #     p2.start()
# #     p1.join()
# #     p2.join()
# #     print(time.time()-start)
#
# # РАЗДЕЛЕНИЕ ПАМЯТИ
# counter = 0
#
# def p_count(name):
#     global counter
#     counter += 1
#     print(f'в процессе: {counter}')
#     print(name)
#
# # if __name__=='__main__':
# #     p = multiprocessing.Process(target=p_count,
# #                                 args=('IVAN',))
# #     p.start()
# #     p.join()
# #     print(f'в главном: {counter}')
#
# def square(x):
#    return x * x
#
# # if __name__ == '__main__':
# #     p = multiprocessing.Process(target=square,
# #                                 args=(5,))
# #     p.start()
# #     p.join()
# #     print(p)
#
# # from multiprocessing import Process, Queue
#
# def worker_p(q):
#     for i in range(5):
#         q.put(i)
#     # q.put('Привет из процесса')
#
# # if __name__ == '__main__':
# #     q = Queue()
# #     p = Process(target=worker_p, args=(q,))
# #     p.start()
# #     # message = q.get()
# #     for _ in range(3):
# #         print(q.get())
# #     print(q.get())
# #     p.join()
# #     # print(message)
#
# # PIPE
# from multiprocessing import Process, Pipe
# # PIPE возвращает кортеж, принимает и отправляет данные
# # с обоих концов
# import time
#
# def worker_pipe(conn):
#     print('[worker] процесс запущен')
#     time.sleep(2)
#     conn.send('привет из дочернего процесса')#отправка
#     parent_msg = conn.recv() #получение
#     print('[worker]',parent_msg)
#     conn.close() #ЗАКРЫВАЕМ КАНАЛ СВЯЗИ
#
# # if __name__ == '__main__':
# #     #  создаем две стороны одного канала
# #     #  conn = Pipe(); parent_conn = conn[0]; child_conn = conn[1]
# #     parent_conn, child_conn = Pipe()#(1, 2)
# #     p = Process(target=worker_pipe, args=(child_conn,))
# #     p.start()
# #     print('[main] ожидание данных')
# #     received_msg = parent_conn.recv() #recv() блокирующий
# #     print('[main] получено', received_msg)
# #     parent_conn.send('и тебе привет')
# #     p.join()
# #     print('[main] дочерний процесс завершен')
#
# # ПУЛ ПРОЦЕССОВ
# '''
# 1)пул создает процессы = кол ядер (или нужное кол-во)
# 2)передаем ему задачу и список данных
# 3)сам распределяет элементы по свободным процессам
# 4)соберет результаты
# 5)вернет нам в правильном порядке
# '''
#
# from multiprocessing import Process
# from concurrent.futures import ProcessPoolExecutor
# import os
#
# def square_worker(x):
#     print(f'число {x} обрабатывается в процессе [PID] {os.getpid()}')
#     return x * x
#
# # if __name__ == '__main__':
# #     numbers = [x for x in range(1000)]
# #     # max_workers максимальное кол-во процессов
# #     print(os.cpu_count())
# #     with ProcessPoolExecutor(max_workers=4) as executor:
# #         results = executor.map(square_worker, numbers)
# #     print('\nФинальный результат')
# #     print(list(results))
#
# # CPU-bound (зависимые от процессора)
# # I/O-bound (зависимые от ввода/вывода)
# # GIL - global interpreter lock
#
# # DAEMON PROCESS
# from multiprocessing import Process
# import time
# import sys
#
# def heavy_worker():
#     print('[worker] начинаем бесконечный цикл')
#     try:
#         while True:
#             print('[worker] я работаю')
#             time.sleep(0.5)
#     except BaseException as e:
#         print(f'[worker] Получен сигнал прерывания', e)
#
# if __name__ == '__main__':
#     p = Process(target=heavy_worker)
#     p.start()
#     time.sleep(3)
#     print('[main] процесс работает слишком долго')
#     p.terminate() # посылает сигнал SIGTERM
#     p.join()
#     print(f'[main] процесс остановки, код выхода: {p.exitcode}')
#
#
#
#
#
#
#
#
#
#
#
#
#

print("\a")