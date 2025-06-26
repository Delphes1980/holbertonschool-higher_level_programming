#!/usr/bin/python3
"""
This script connects to a MySQL database using SQLAlchemy and
attempts to list State objects based on a name filter.
It takes MySQL username, password, and database name as command-line arguments
"""
from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
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

    # Query states where the name contains the letter 'a'
    a_state = session.query(State).filter(State.name.like('%a%')).all()

    for state in a_state:
        print(f"{state.id}: {state.name}")

    # Close the session to release database resources
    session.close()
