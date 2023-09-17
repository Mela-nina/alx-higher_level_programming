#!/usr/bin/python3
"""
This is the script that defines a State class and
a Base class to work with MySQLAlchemy ORM
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class

    Attributes:
        __tablename__ (str): This is the table name of the class
        id (int): This is the State id of the class
        name (str): This is the State name of the class

    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
