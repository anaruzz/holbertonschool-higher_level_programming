#!/usr/bin/python3
"""
Module that lists all State objects
"""
from model_state import Base, State
from model_city import City
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == '__main__' and len(sys.argv) == 4:
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1],
                            sys.argv[2],
                            sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for c, s in session.query(City, State).filter(City.state_id == State.id):
        print("{}: ({}) {}".format(s.name, c.id, c.name))
