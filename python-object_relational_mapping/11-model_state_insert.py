#!/usr/bin/python3
"""adds the State object “Louisiana” to the hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    nw_xx = State(name='Lousiana')
    session.add(nw_xx)
    session.commit()
    print(nw_xx.id)
    session.close()