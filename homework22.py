from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session
from core.db.orm_lesson.tables.base import Base
from core.db.orm_lesson.tables.courses import Courses
from core.db.orm_lesson.tables.students import Students

import logging.config
import pathlib


def init_db():

    PG_SQL = "postgresql://yehor.bulhakov@localhost:5432/hillel_2025"
    engine = create_engine(PG_SQL)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    return Session

Session = init_db()

def default_values():
    session = Session()

    # add default courses
    courses = [
        'Math',
        'Chemistry',
        'Physics',
        'ART',
        'Philosophy',
    ]

    # check that there are no identical courses
    existing_courses = {c.course_name for c in session.query(Courses).all()}
    add_courses = [Courses(course_name=name) for name in courses if name not in existing_courses]

    session.add_all(add_courses)

    # add default students
    students = [
        ('John', 21, 1),
        ('Yehor', 22, 2),
        ('Taras', 23, 3),
        ('Oleh', 24, 4),
        ('Oksana', 25, 5),
        ('Olesia', 18, 2),
        ('Ann', 19, 4),
        ('Ihor', 20, 4),
        ('Peter', 21, 5),
        ('Vadim', 22, 1),
        ('Den', 23, 2),
        ('Irina', 24, 3),
        ('Juliana', 25, 5),
        ('Vasyl', 18, 1),
        ('Andrii', 19, 1),
        ('Ekaterina', 20, 2),
        ('Kate', 21, 5),
        ('Serhii', 22, 4),
        ('Anastasia', 23, 3),
        ('Karlo', 24, 1),
        ('Sirena', 25, 4)
    ]

    # check that one student cannot have courses with the same id
    for name, age, course_id in students:
        exists = session.query(Students).filter_by(student_name=name, course_id=course_id).first()
        if not exists:
            session.add(Students(student_name=name, student_age=age, course_id=course_id))

    session.commit()
    session.close()

default_values()

def add_course(course_name):
    session = Session()
    #course = [(course_name)]

    # check that there are no identical courses
    existing_courses = session.query(Courses).filter_by(course_name=course_name).first()
    if existing_courses:
        logging.error(f"Course {course_name} already exists")
    else:
        course = Courses(course_name=course_name)
        session.add(course)
        session.commit()
        logging.info(f"A course has been added to the Courses_orm database: {course_name}")

    session.close()

add_course('Geometry')

# INSERT - add student (entity)
def add_student(name, age, course_id):
    session = Session()
    student = [(name, age, course_id)]

    # check that one student cannot have courses with the same id
    for name, age, course_id in student:
        exists = session.query(Students).filter_by(student_name=name, course_id=course_id).first()
        logging.error(f"Unable to add student {name}. Course №{course_id} already has a student of this name.")
        if not exists:
            session.add(Students(student_name=name, student_age=age, course_id=course_id))
            logging.info(f"Student: {name}, age: {age}, course: {course_id} was added to the Students_orm database")

    session.commit()
    session.close()

add_student('Yehor', 21, 3)

# UPDATE - update attributes for one entity with a given name
def upd_one_student_age(name, age, course_id):
    session = Session()

    student = session.query(Students).filter_by(student_name=name, course_id=course_id).first()

    # attribute that we will update
    student.student_age = age
    logging.info(f"Student {name} from course №{course_id} has had their age changed to {age}")

    session.commit()
    session.close()

upd_one_student_age("Yehor", 28, 3)

# UPDATE - update attributes for all entities with the given name
def upd_all_student(name,age):
    session = Session()
    students = session.query(Students).filter_by(student_name=name).all()

    for student in students:
        student.student_age = age
    logging.info(f"All students with the name: {name} have had their age changed to: {age}")

    session.commit()
    session.close()

upd_all_student("Yehor",30)

# JOIN - by course_id
def display_students(course_id):
    session = Session()

    result = (
        session.query(Students, Courses)
        .join(Courses, Students.course_id == Courses.course_id)
        .filter(Students.course_id == course_id) .all()
    )

    for student, course in result:
        print(f"Student: {student.student_name}, age: {student.student_age}, Curse: {course.course_name}")

    print("-" * 20)
    session.close()

display_students(2)

# JOIN - by name
def display_students(name):
    session = Session()

    result = (
        session.query(Students, Courses)
        .join(Courses, Students.course_id == Courses.course_id)
        .filter(Students.student_name == name) .all()
    )

    for student, course in result:
        print(f"Student: {student.student_name}, Age: {student.student_age}, Course: {course.course_name}")

    session.close()

display_students("Yehor")