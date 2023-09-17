#!/usr/bin/python3
"""
This is the script that defines a City class
to work with MySQLAlchemy ORM
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class

    Attributes:
        __tablename__ (str): This is the table name of the class
        id (int): This is the id of the class
        name (str): This is the name of the class
        state_id (int): This is the state the city belongs to

    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
