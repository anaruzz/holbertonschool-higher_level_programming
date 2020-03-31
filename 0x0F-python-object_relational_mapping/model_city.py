#!/usr/bin/python3
"""
Module that contains a class definition of a city
and an instance Base = declarative_base()
"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey



class City(Base):
    """
    State class that is mapped to the table cities
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('State.id'), nullable=False)
