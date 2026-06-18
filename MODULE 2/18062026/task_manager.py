import asyncio
import threading
import multiprocessing as mp
import logging
import os

# настройка логирование
logging.basicConfig(
    filename='app_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s)',
    encoding='utf-8'
)

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
