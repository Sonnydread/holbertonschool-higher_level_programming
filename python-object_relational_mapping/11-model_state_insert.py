#!/usr/bin/python3
"""adds the State object “Louisiana” to the hbtn_0e_6_usa"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from model_state import Base, State
import sys

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Sesion = sessionmaker(bind=engine)
    sesion = Sesion()

    nw_xx = State(name='Lousiana')
    sesion.add(nw_xx)
    sesion.commit()
    st = sesion.query(State).filter_by(name="Louisiana").first()
    print(st.id)

    sesion.close()
