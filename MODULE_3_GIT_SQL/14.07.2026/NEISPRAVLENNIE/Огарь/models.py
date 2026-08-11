from operator import index

from typing import List, Optional
from sqlalchemy import ForeignKey, String, Table, Column
from sqlalchemy.orm import Mapped, DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

#Ассоциативная таблица для связи многие ко многим N:N Student <--> Course

student_course_association = Table(
    'student_course',
    Base.metadata,
    Column('student_id', ForeignKey('students.id', ondelete='CASCADE'), primary_key=True),
    Column('course_id', ForeignKey('courses.id', ondelete='CASCADE'), primary_key=True)
)

#Mapped[int] - указыват Python , что после при извлечении из БД будет имет тип данных int

class InstructorProfile(Base):
    __tablename__ = 'instructor_profiles'
    id: Mapped[int] = mapped_column(primary_key=True)
    bio: Mapped[Optional[str]] = mapped_column(String(500))
    expertience_years: Mapped[int] = mapped_column(default=0)
    instructor_id: Mapped[int] = mapped_column(ForeignKey("instructors.id", ondelete = "CASCADE"))

# Обратная связь "1:1"
    instructor: Mapped["Instructor"] = relationship(back_populates="profile")
)

class Instructor(Base):
    __tablename__ = 'instructors'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(string(150), unique=True, index=True)
    profile: Mapped[InstructorProfile] = relationship(back_populates="instructor", cascade="all, delete-orphan")

    # 1:N с курсами
    courses: Mapped[List["Course"]] = relationship(back_populates="instructor")

class course(Base):
    __tablename__ = 'courses'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    price: Mapped[int] = mapped_column(default=0)
    instructor_id: Mapped[int] = mapped_column(ForeignKey("instructors.id", ondelete = "SET NULL"))

    instructor: Mapped["Instructor"] = relationship(back_populates="courses")
    students: Mapped[List["Student"]] = relationship(
        secondary=student_course_association,
        back_populates="courses"
    )
class Student(Base):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    course: Mapped[List["Course"]} = relationship(
        secondary=student_course_association,
        back_populates="students"
    )