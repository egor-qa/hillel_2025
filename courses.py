from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.db.orm_lesson.tables.base import Base


# Defining a data model (tables) using a class
class Courses(Base):
    __tablename__ = 'courses_orm'

    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String, nullable=False, unique=True)

    # one course has many students
    students = relationship("Students", back_populates="course")