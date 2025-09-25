from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.db.orm_lesson.tables.base import Base
# Base class for defining data models


# Defining a data model (tables) using a class
class Students(Base):
    __tablename__ = 'students_orm'

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    student_name = Column(String, nullable=False)
    student_age = Column(Integer)
    course_id = Column(Integer, ForeignKey("courses_orm.course_id"))

    # each student belongs to one course
    course = relationship("Courses", back_populates="students")