import sqlite3
import os

DB_NAME = 'work.db'

def connect_db():
    if not os.path.exists(DB_NAME):
        print(f'WARN: файл {DB_NAME} не найден')
    conn = sqlite3.connect(DB_NAME)
    return conn

def show_all_employees(conn):
    """ 1. Полный список сотрудников (ФИО, отдел, email) """
    query = '''
        SELECT e.full_name, d.department_name, c.email
        FROM Employees e 
        LEFT JOIN Departments d ON e.department_id = d.department_id
        LEFT JOIN Contacts c ON e.contact_id = c.contact_id
    '''
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    print("\n===ПОЛНЫЙ СПИСОК СОТРУДНИКОВ===")
    print(f'{"ФИО":<20} | {"Отдел":<20} | {"Email":<20}')
    # [(name, dept, email), (), (), ()]
    print("-"*66)
    for name, dept, email in rows:
        print(f"{name:<20} | {str(dept):<20} | {str(email):<20}")

# show_all_employees(connect_db())

def show_employees_without(conn):
    """2. Сотрудники без отдела/контакта """
    query = '''
        SELECT e.employee_id, e.full_name, d.department_name, c.email
        FROM Employees e 
        LEFT JOIN Departments d ON e.department_id = d.department_id
        LEFT JOIN Contacts c ON e.contact_id = c.contact_id
        WHERE e.department_id IS NULL OR e.contact_id IS NULL
    '''
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    print("\n===Сотрудники без отдела/контакта===")
    print(f'{"ID":<5} | {"ФИО":<20} | {"Отдел":<20} | {"Email":<20}')
    print("-" * 68)
    for id, name, dept, email in rows:
        print(f"{id:<5} | {name:<20} | {str(dept):<20} | {str(email):<20}")

# show_employees_without(connect_db())

def show_employee_projects(conn):
    # 3. Информация о проектах сотрудника (по ID или ФИО)
    search = input("\nВведите ID или ФИО сотрудника: ").strip()
    query = """
        SELECT e.full_name, p.project_name, p.status
        FROM Employees e
        INNER JOIN ProjectAssignments pa ON e.employee_id = pa.employee_id
        INNER JOIN Projects p ON pa.project_id = p.project_id
        WHERE e.employee_id = ? OR e.full_name LIKE ?  
    """
    cursor = conn.cursor()
    cursor.execute(query, (search,  f'%{search}%'))
    rows = cursor.fetchall()
    if not rows:
        print("Проекты не найдены")
        return
    print(f'\n===Проекты сотрудника: {rows[0][0]}===')
    print(f'{'Название проекта':<25} | {'Статус':<15}')
    print('-'*44)
    for _, project, status in rows:
        print(f'{project:<25} | {status:<15}')

# show_employee_projects(connect_db())

def show_department_summary(conn):
    """4. Сводка по отделам (Кол-во сотрудников в каждом отделе)"""
    query = '''
        SELECT d.department_name, COUNT(e.employee_id) AS emp_count
        FROM Departments d 
        LEFT JOIN Employees e ON d.department_id = e.department_id
        GROUP BY d.department_id, d.department_name
    '''
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    print("\n=== Сводка по отделам ===")
    print(f"{'Отдел':<20} | {'Количество сотрудников':<20}")
    print("-"*43)
    for dept_name, count in rows:
        print(f"{dept_name:<20} | {count:<20} ")

# show_department_summary(connect_db())

def assign_employee_to_department(conn):
#     5. Назначить сотрудника на отдел
    emp_id = input('\nВведите ID сотрудника: ')
    dept_id = input('\nВведите ID отдела: ')
    cursor = conn.cursor()
    cursor.execute("""
                SELECT employee_id 
                FROM Employees
                WHERE employee_id = ?
            """, (emp_id,) )
    if not cursor.fetchone():
        print('Сотрудник не найден')
        return

    cursor.execute("""
        SELECT department_id 
        FROM Departments
        WHERE department_id = ?
    """, (dept_id,))
    if not cursor.fetchone():
        print('Такой отдел не найден')
        return

    cursor.execute("""
        UPDATE Employees SET department_id = ?
        WHERE employee_id = ?
    """, (dept_id, emp_id))
    conn.commit()
    print('Данные добавлены!')

def main_menu():
    conn = connect_db()
    while True:
        print('1. Полный список сотрудников')
        print('2. Сотрудники без отдела/контакта')
        print('3. Информация о проектах сотрудника')
        print('4. Сводка по отделам')
        print('5. Назначить сотрудника на отдел')
        print('0. Выход')

        choice = input('Выберите действие: ')
        if choice == '1':
            show_all_employees(conn)
        elif choice == '2':
            show_employees_without(conn)
        elif choice == '3':
            show_employee_projects(conn)
        elif choice == '4':
            show_department_summary(conn)
        elif choice == '5':
            assign_employee_to_department(conn)
        elif choice == '0':
            conn.close()
            break
        else:
            print('Неверный ввод')
if __name__ == '__main__':
    main_menu()




