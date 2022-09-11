#!/usr/bin/python3
"""
update state: given id, change state name
parameters given to script: mysql username, mysql password,
mysql database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # make engine for database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # find and update state
    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"  # update state name

    session.commit()
    session.close()
