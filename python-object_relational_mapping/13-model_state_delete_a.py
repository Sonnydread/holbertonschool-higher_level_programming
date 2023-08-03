#!/usr/bin/python3
"""deletes all states objects with the letter a from hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import relationship, sessionmaker
import sys

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Sesion = sessionmaker(bind=engine)
    sesion = Sesion()
    sesion.query(State).filter(State.name.like("%a%")).delete(
                               synchronize_session=False)
    sesion.commit()
    sesion.close()
