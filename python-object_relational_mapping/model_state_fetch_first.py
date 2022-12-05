#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa """

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == "__main__":
    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create session
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query
    state = session.query(State).first()
    if state is not None:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    # Close session
    session.close()
