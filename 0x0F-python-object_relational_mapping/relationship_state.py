#!/usr/bin/python3
"""
Module that contains a class definition of a state
and an instance Base = declarative_base()
"""

from relationship_city import Base, City
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, inspect
from sqlalchemy.orm import relationship, backref


class State(Base):
    """
    State class that is mapped to the table states
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all,delete', backref='state')
