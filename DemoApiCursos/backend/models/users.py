from sqlalchemy import Table, Column, Boolean, ForeignKey, Integer, String, DateTime
#from backend.db.connection import Base 
from sqlalchemy.orm import relationship
#from .users_courses import UsersCourses
from backend.db.connection import engine, Base ,meta
from .users_courses import user_course_association

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    username = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    datetime = Column(DateTime)
    #courses = relationship("Course", secondary=users_courses, back_populates="users")
    #courses = relationship("UserCourses", back_populates="user")
    courses = relationship("Course", secondary=user_course_association, back_populates="users") 

