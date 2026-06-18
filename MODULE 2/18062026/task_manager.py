import asyncio
import threading
import multiprocessing as mp
import logging
import os
import re
import datetime

from django.views.decorators.http import last_modified

# настройка логирование
logging.basicConfig(
    filename='app_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s)',
    encoding='utf-8'
)
# ЧЧ:ММ
TIME_PATTERN = re.compile(r'(\d{2}):(\d{2})')
# print(TIME_PATTERN.search('Пойти спать в 23:59').group())

def load_tasks_from_file(file_path='tasks.txt'):
    """Функция для первичной проверки и чтения строк из файла"""
    if not os.path.exists(file_path):
        logging.error(f'Файл {file_path} не существует')
        print(f'Файл {file_path} не существует')
        return None

    if os.path.getsize(file_path) == 0:
        logging.warning(f'Файл {file_path} пуст')
        print(f'Предупреждение: Файл {file_path} пуст')
        return None

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [l.strip() for l in f if l.strip()]
    return lines

def parse_tasks(lines):
    """Парсит строки из файла, выделяя время и описание задачи"""
    parsed_tasks = []

    for l in lines:
        match = TIME_PATTERN.search(l) #ищем шаблон времени в строке
        if match:
            task_time = match.group(0)  #извлекаем найденное время
            task_text = l
            parsed_tasks.append({
                'time': task_time,
                'text': task_text
            })
    return parsed_tasks



async def check_tasks_loop(active_tasks):
    """Асинхронный цикл проверки наступления времени задач"""
    print('Проверка задач запущена')
    logging.info('Мониторинг времени задач запущен')
    while active_tasks:
        now = datetime.datetime.now().strftime("%H:%M")
        to_remove = []
        for task in active_tasks:
            if task['time'] == now:
                print('\a')
                print(f'НАПОМИНАНИЕ: {task['text']}')
                logging.info(f'Отправлено уведомление для задачи: {task['text']}')
                to_remove.append(task)
        for task in to_remove:
            active_tasks.remove(task)

        await asyncio.sleep(10)

async def monitor_file_changes(file_path, active_tasks):
    """Асинхронно следит за обновлением файла tasks.txt"""
    last_modified = os.path.getmtime(file_path)
    while True:
        await asyncio.sleep(5)
        try:
            current_modified = os.path.getmtime(file_path)
            if last_modified != current_modified:
                last_modified = current_modified
                lines = load_tasks_from_file(file_path)
                if lines:
                    new_tasks = parse_tasks(lines)
                    active_tasks.clear()
                    active_tasks.extend(new_tasks)
                    print('Задачи обновлены')
                    logging.info('Файл задач изменен')
                    for t in active_tasks:
                        print(f'- {t['text']}')

        except Exception as e:
            logging.error(f'Ошибка при мониторинге файла: {e}')


async def main():
    """Главная функция управления жизненным циклом приложения"""
    file_path = 'tasks.txt'
    logging.info('Запуск программы ТАСК-МЕНЕДЖЕР')
    lines = load_tasks_from_file(file_path)
    if lines is None:
        return

    active_tasks = parse_tasks(lines)
    print('Задачи загружены:')
    for t in active_tasks:
        print(f'{t['text']}')

    await  asyncio.gather(check_tasks_loop(active_tasks),
                          monitor_file_changes(file_path, active_tasks)
                          )


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('\nПрограмма остановлена пользователем')
        logging.info('Программа завершила работу по запросу пользователя')







    # logging.info('Программа запущена')
    # tasks = load_tasks_from_file()
    # # print(tasks)
    # result_parse = parse_tasks(tasks)
    # print(result_parse)
