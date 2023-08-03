#!/usr/bin/python3
"""prints all city objects from hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":

    engine = create_engine(f"""mysql+mysqldb://{sys.argv[1]}:
                           {sys.argv[2]}@localhost:3306/{sys.argv[3]}""",
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    sesion = Session()
    rows = sesion.query(City).order_by(City.id).all()
    for row in rows:
        print(f"{row.state.name}:", f"({row.id})", row.name)
    sesion.close()
