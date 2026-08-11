import sqlite3


try:
    # подключение
    conn = sqlite3.connect("example.db")

    # временная область памяти
    cursor = conn.cursor()

    # выполнение запросов:
    #  .execute() - один SQL запрос
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT
                )
                ''')

    # параметризированный запрос
    cursor.execute('''
                INSERT INTO users (id, name)
                VALUES (?, ?)
                ''', (1, "Alice"))


    # Login: ''
    # Password: '' or 1=1

    # SELECT id FROM users WHERE login = '' AND password ='' or 1=1

    #  .executemany() - один запрос со множеством данных
    data = [(2, "Bob"), (3, "Mike"), (4, "Sasha")]
    cursor.executemany('''
                INSERT INTO users (id, name)
                VALUES (?, ?)
                ''', data)
    #  .executescript() - выполнение нескольких запросов (;-разделитель)
    cursor.executescript('''
                CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT);
                INSERT INTO books (id, title) VALUES (1, 'Book A');
            ''')

    conn.commit()


    cursor.execute('SELECT * FROM users')
    # .fetchone() - получает одну строку
    # .fetchall() - получает все строки из результата
    # .fetchmany(n) n-кол-во строк
    rows = cursor.fetchall()
    print(rows)
    print(rows[0])
    print(rows[0][1])

except sqlite3.Error as e:
    print('Ошибка:', e)

finally:
    # закрытие
    cursor.close()
    conn.close()