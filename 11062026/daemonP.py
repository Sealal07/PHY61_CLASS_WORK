import threading
import time
def background_task():
    print('[Поток] начинаю работу')
    for i in range(1, 6):
        time.sleep(1)
        print(f'[Поток]Шаг {i}')
    print('[Поток]закончил работу')

def normal_thread():
    t = threading.Thread(target=background_task,
                         daemon=False)
    t.start()
    time.sleep(2)
    print('[ОСНОВНОЙ ПОТОК] закончил свою работу')

def daemon_thread():
    t = threading.Thread(target=background_task,
                         daemon=True)
    t.start()
    time.sleep(2)
    print('[ОСНОВНОЙ ПОТОК] закончил свою работу')

# normal_thread()
daemon_thread()




