#!/usr/bin/python3
"""
script that prints the State object with the name
 passed as argument from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import Session

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = Session(engine)

    rows = Session.query(State).all()
    element = ""

    for row in rows:
        if sys.argv[4] in row.name:
            element = row.id
    if element != "":
        print(element)
    else:
        print("Not Found")

    Session.close()
