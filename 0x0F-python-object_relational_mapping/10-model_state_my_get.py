#!/usr/bin/python3
"""
Module that lists all State objects
"""

from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == '__main__' and len(sys.argv) == 5:
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1],
                            sys.argv[2],
                            sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).filter(State.name == sys.argv[4]).first()
    if instance is not None:
        print(instance.id)
    else:
        print('Not found')
