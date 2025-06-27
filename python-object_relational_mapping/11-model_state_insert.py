#!/usr/bin/python3
"""
Script that add a new state in the 'state' table from the database
hbtn_0e_6_usa
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    # Validate number of arguments
    if len(sys.argv) < 4:
        print("Usage: {} <user><password><db_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get database connection details from command-line arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Construct the database URL for SQLAlchemy
    DB_URL = f"mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}"

    # Create the SQLAlchemy engine to manage database connections
    engine = create_engine(DB_URL)

    # Create all tables defined in Base's metadata (e.g., 'states' table)
    # This ensures the table exists in the database
    Base.metadata.create_all(engine)

    # Create a configured Session class
    Session = sessionmaker(bind=engine)

    # Create a new Session instance
    session = Session()

    # Create a new State object
    new_state = State(name="Louisiana")
    # Add the new State object to the current session
    session.add(new_state)
    # Commit the transaction to save the new state to the database
    session.commit()
    print(new_state.id)

    # Close the session to release database resources
    session.close()
