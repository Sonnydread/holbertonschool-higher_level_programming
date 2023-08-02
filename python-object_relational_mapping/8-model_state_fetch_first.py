#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:\
                           3306/{}'.format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    request = session.request(State).first()

    if request is None:
        print("Nothing")
    else:
        print(f"{request.id}: {request.name}")

    session.close()
