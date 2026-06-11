# Задача 1
import threading
import time
import random

running = True

def sensor_polling():
    sensors = ['Температура', 'Влажность', 'CO2']
    while running:
        print('\nНачало опроса датчиков')
        for sensor in sensors:
            delay = random.uniform(0.1, 0.2)
            time.sleep(delay)
            value = random.randint(15, 60)
            print(f'Датчик {sensor}: {value} (задержка {delay:.2f}с)')
        time.sleep(0.5)

def backup_logs():
    while running:
        time.sleep(5)
        print('\n начало записи логов')
        with open('backup.txt', 'a', encoding='utf-8') as f:
            f.write(f'лог сохранен в {time.strftime('%Y-%m-%d %H:%M:%S')}\n')


def user_interface():
    global running
    print('Интерфейс запущен')
    while running:
        command = input().strip().lower()
        if command == 'status':
            print('Система работает')
        elif command == 'reboot':
            print('Перезапуск модулей ядра')
        elif command == 'exit':
            print('Завершение работы умного дома')
            running = False
            break
        else:
            print('неизвестная команда')

def main():
    polling = threading.Thread(target=sensor_polling, daemon=True)
    backup = threading.Thread(target=backup_logs, daemon=True)

    polling.start()
    backup.start()
    user_interface()

main()