#!/usr/bin/python3
"""prints the State object with the name passed argument from hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:\
                           3306/{}'.format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter_by(name=f"{argv[4]}").first()

    if query:
        print(query.id)
    else:
        print("Not found")

    session.close()
