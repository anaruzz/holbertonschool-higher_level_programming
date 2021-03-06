#!/usr/bin/python3
"""
Module that lists all State objects
"""
from relationship_state import Base, State
from relationship_city import City
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1],
                            sys.argv[2],
                            sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    parent = State(name='California')
    child = City(name='San Francisco')
    parent.cities.append(child)
    session.add(parent)
    session.commit()
