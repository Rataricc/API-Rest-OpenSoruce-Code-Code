from sqlalchemy import Table, Column, Boolean, ForeignKey, Integer, String, DateTime
#from backend.db.connection import Base 
from sqlalchemy.orm import relationship 
from backend.db.connection import engine, Base, meta

"""
class UsersCourses(Base): 
    __tablename__ = "users_courses"

    id_user = Column(Integer, ForeignKey('users.id'), primary_key=True)
    id_course = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    user = relationship("User", back_populates="courses")
    course = relationship("Course", back_populates="users")
"""
user_course_association = Table(
    "user_course",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("course_id", Integer, ForeignKey("courses.id")),
)