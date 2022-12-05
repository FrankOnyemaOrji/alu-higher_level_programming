#!/usr/bin/python3
"""Adds the State object “Louisiana” to the database"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    # Create session
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query
    new_state = State(name="Louisiana")
    session.add(new_state)
    state = session.query(State).filter(State.name == "Louisiana").first()
    print("{}".format(state.id))
    session.commit()
    # Close session
    session.close()
