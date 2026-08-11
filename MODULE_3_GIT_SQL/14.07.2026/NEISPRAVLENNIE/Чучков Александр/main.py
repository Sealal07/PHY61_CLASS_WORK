import asyncio
from sqlalchemy import select, func, update, delete, and_, or_
from sqlalchemy.orm import selectinload, joinedload

from database import engine, async_session_maker
from models import Instructor, InstructorProfile, Course, Student, Base

async def init_models():
    '''Создание таблиц в БД'''
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        print("[БАЗА] Все таблицы пересозданы")

async def seed_data():
    '''Наполнение тестовыми данными'''
    async with async_session_maker() as session:

        # 1. Преподаватель и его профиль
        inst1 = Instructor(name='Алексей Петров', email='a@scholl.com')
        inst1.profile = InstructorProfile(bio="Senior Python Developer", experience_years=10)
        inst2 = Instructor(name='Мария Сидорова', email='m@school.com')
        inst2.profile = InstructorProfile(bio='Data Scientist', experience_years=5)

        # 2. Курсы 
        course1 = Course(title='Python с нуля до профи', price=15000, instructor=inst1)
        course2 = Course(title='Асинхронное программирование на Python', price=25000, instructor=inst2)
        course3 = Course(title='введение в Data Scientist', price=30000, instructor=inst2)

        # 3. Студенты
        student1 = Student(name='Иван Иванов')
        student2 = Student(name='Сергей Сергеев')
        student3 = Student(name='Анна Кузнецова')

        # 4. Записываем студентов на курсы
        course1.students.extend([student1, student2])
        course2.students.append(student1)
        course3.students.extend([student2, student3])

        # добавляем объекты в сессию
        session.add_all([inst1, inst2, course1, course2, course3, student1, student2, student3])

        await session.commit() # выполнится INSERT
        print('[БАЗА] Данные загружены')

async def run_queries():
    '''CRUD'''
    async with async_session_maker() as session:
        # 1. SELECT и загрузка связей
        print('1. Выборка преподавателей')
        # SELECT * FROM Instructor
        query = select(Instructor)
        # .execute()
        result = await session.execute(query)
        # scalar() scalars()
        instructors = result.scalars().all()
        for inst in instructors:
            print(f'\n-- {inst.name} ({inst.email})')

        # joinedload - для 1 к 1 (left join)
        # selectinload - для 1:N или N:N
        print('2. Курсы с подгрузкой связей')
        query = (
            select(Course)
            .options(
                joinedload(Course.Instructor),
                selectinload(Course.students)
        ) 
    )
    result = await session.execute(query)
    courses = result.scalars().all()
    for course in courses: 
        inst_name = course.instructor.name
        # for s in course.student:
        # list.append(s.name)
        # ['ИМЯ 1', 'ИМЯ 2', 'ИМЯ 3']
        # "ИМЯ 1', 'ИМЯ 2', 'ИМЯ 3"
        student_names = ', '.join([s.name for s in course.students])
        print(f'{course.title} | {inst.name} | [{student_names}]')

    # 3. Фильтрация и сортировка
    print('3. Фильтрация курсов по цене и сортировка по убыванию')
    query (
        select(Course)
        .where(Course.price > 15000)
        .order_by(Course.price.desc())
    )
    result = await session.execute(query)
    courses = result.scalars().all()
    for c in courses:
        print(f'{c.title} - {c.price} руб. ')

    print("4. Фильтрация с AND OR и LIKE")
    query = select(Instructor).where(
        or_(
            Instructor.name.like('А%'),
            Instructor.email.like('%.com')
        )
    )
    result = await session.execute(query)
    filtered_inst = result.scalars().all()
    for fi in filtered_inst:
        print(fi.name)

async def main():
    await init_models()
    await seed_data()
    await run_queries()

if __name__ == '__main__':
    asyncio.run(main())


