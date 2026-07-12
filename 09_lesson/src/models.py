from sqlalchemy import Column, Integer, String
from src.database import Base


class Student(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
