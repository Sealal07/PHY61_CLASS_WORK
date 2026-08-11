import sqlite3
import os

SQL_FILE = 'script_work.sql'
DB_NAME = 'work.db'

def create_database():
    if not os.path.exists(SQL_FILE):
        print(f'файл {SQL_FILE} не найден')
        return

    print('читаем скрипт')
    with open(SQL_FILE, 'r', encoding='utf-8') as f:
        sql_script = f.read()

    print('подключение к БД')
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.executescript(sql_script)
        conn.commit()
        print('бд создана и данные добавлены')
    except sqlite3.Error as e:
        print(f'Ошибка: {e}')
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    create_database()