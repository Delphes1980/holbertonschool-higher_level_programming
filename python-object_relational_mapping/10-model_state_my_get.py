#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
Displays only the states.id if found, otherwise "Not found"
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Validate the number of arguments passed
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql pwd> <db name> <state search>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Get database connection details from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    name_to_search = sys.argv[4]

    # Create the SQLAlchemy engine to manage database connections
    # using the database URL
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, db_name),
        pool_pre_ping=True
    )

    # Create all tables defined in Base's metadata (e.g., 'states' table)
    # This ensures the table exists in the database
    Base.metadata.create_all(engine)

    # Create a configured Session class
    Session = sessionmaker(bind=engine)
    # Create a new Session instance
    session = Session()

    state = (
        session.query(State)
        .filter(State.name == name_to_search)
        .first()
    )

    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session to release database resources
    session.close()
