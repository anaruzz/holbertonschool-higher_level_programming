#!/usr/bin/python3
"""
Module that lists all State objects
"""

from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == '__main__' and len(sys.argv) == 4:

    arg = sys.argv
    url_base = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    db_url = url_base.format(arg[1], arg[2], arg[3])
    engine = create_engine(db_url, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana = State(name='Louisiana')
    session.add(louisiana)
    session.commit()
    print(louisiana.id)
