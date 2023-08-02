#!/usr/bin/python3
"""list all states objects that contain the letter a"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import relationship, sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Sesion = sessionmaker(bind=engine)
    sesion = Sesion()

    state = sesion.query(State).all()
    for S in state:
        if "a" in S.name:
            print("{}: {}".format(S.id, S.name))

    sesion.close()
