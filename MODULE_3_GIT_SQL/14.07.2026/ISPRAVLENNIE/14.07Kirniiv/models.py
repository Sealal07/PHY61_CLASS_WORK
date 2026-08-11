# В классе InstructorProfile вы используете backref='profile',
# а в классе Instructor пытаетесь создать еще одно отношение с тем же именем profile
# через back_populates='instructor'. Это создает конфликт.


from typing import List, Optional
from sqlalchemy import ForeignKey, String, Table, Column, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


# Ассоциативная таблица для N:N Student<-->Course
student_course_association = Table(
    'student_course',
    Base.metadata,
    Column('student_id', ForeignKey('students.id', ondelete="CASCADE"), primary_key=True),
    Column('course_id', ForeignKey('courses.id', ondelete="CASCADE"), primary_key=True)
)


class InstructorProfile(Base):
    __tablename__ = "instructor_profiles"

    id: Mapped[int] = mapped_column(primary_key=True)
    bio: Mapped[Optional[str]] = mapped_column(String(500))
    experience_years: Mapped[int] = mapped_column(default=0)
    instructor_id: Mapped[int] = mapped_column(ForeignKey("instructors.id", ondelete="CASCADE"), unique=True)

    # Убираем backref, используем back_populates
    instructor: Mapped["Instructor"] = relationship(back_populates='profile')


class Instructor(Base):
    __tablename__ = 'instructors'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, index=True)

    # Убираем дублирующее определение profile и используем правильное отношение
    profile: Mapped["InstructorProfile"] = relationship(back_populates='instructor', cascade="all, delete-orphan")

    # 1:N с курсами
    courses: Mapped[list["Course"]] = relationship(back_populates='instructor')


class Course(Base):
    __tablename__ = 'courses'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    # Изменяем тип на Integer, так как цена - это число
    price: Mapped[int] = mapped_column(Integer, nullable=False)  # Было String
    instructor_id: Mapped[int] = mapped_column(ForeignKey("instructors.id", ondelete="SET NULL"))

    # Добавляем отношение к instructor
    instructor: Mapped["Instructor"] = relationship(back_populates='courses')

    students: Mapped[List["Student"]] = relationship(
        secondary=student_course_association,
        back_populates="courses"
    )


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    courses: Mapped[List["Course"]] = relationship(
        secondary=student_course_association,
        back_populates="students"
    )
