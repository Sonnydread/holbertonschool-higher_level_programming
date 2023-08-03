#!/usr/bin/python3
"""prints all city objects from hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Sesion = sessionmaker(bind=engine)
    sesion = Sesion()
    result = sesion.query(City, State).filter(City.state_id == State.id) \
                                      .order_by(City.id)
    for city, state in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    sesion.close()
