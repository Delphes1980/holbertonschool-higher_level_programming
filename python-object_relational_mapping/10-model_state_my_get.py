#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
Displays only the states.id if found, otherwise "Not found"
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    # Validate the number of arguments passed
    if len(sys.argv) != 5:
        print("Usage: {} <user> <password> <db_name> <state_name_to_search>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Get database connection details from command-line arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name_to_search = sys.argv[4]

    # Construct the database URL for SQLAlchemy
    DB_URL = f"mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}"

    # Create the SQLAlchemy engine to manage database connections
    engine = create_engine(DB_URL, pool_pre_ping=True)

    # Create all tables defined in Base's metadata (e.g., 'states' table)
    # This ensures the table exists in the database
    Base.metadata.create_all(engine)

    # Create a configured Session class
    Session = sessionmaker(bind=engine)

    # Create a new Session instance
    session = Session()

    arg_states = (
        session.query(State)
        .filter(State.name == state_name_to_search)
        .first()
    )

    if arg_states is not None:  # Checks if the list is empty
        print(arg_states.id)
    else:
        # Get the first (and assumedly only) State object from the list
        print("Not found")

    # Close the session to release database resources
    session.close()
