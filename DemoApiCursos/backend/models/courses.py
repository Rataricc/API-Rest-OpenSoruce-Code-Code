from sqlalchemy import Table, Column, Boolean, ForeignKey, Integer, String, DateTime
#from backend.db.connection import Base 
from sqlalchemy.orm import relationship 
from backend.db.connection import engine, Base, meta
#from .users_courses import UsersCourses
from .users_courses import user_course_association
"""
users_courses = Table('user_courses', Base.metadata,
    Column('id_user', ForeignKey('users.id'), primary_key=True),
    Column('id_course', ForeignKey('courses.id'), primary_key=True)
)

class UsersCourses(Base): 
    __tablename__ = "users_courses"

    id_user = Column(Integer, ForeignKey('users.id'), primary_key=True)
    id_course = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    users = relationship("User", secondary=users_courses, back_populates="courses")
    courses = relationship("Course", secondary=users_courses, back_populates="users")
"""


class Course(Base): 
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(10000), index=True)
    description = Column(String(1000000), index=True)
    instructor = Column(String, index=True)
    category = Column(String, index=True)
    url = Column(String(255), index=True)
    #users = relationship("User", secondary=users_courses, back_populates="courses")
    #users = relationship("UserCourses", back_populates="course")
    users = relationship("User", secondary=user_course_association, back_populates="courses")

#Base.metadata.create_all(engine)


