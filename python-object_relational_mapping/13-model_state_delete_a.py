#!/usr/bin/python3
"""
Script that updates a state in the 'state' table from the database
hbtn_0e_6_usa
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    # Validate the number of arguments passed
    if len(sys.argv) != 4:
        print("Usage: {} <user> <password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get database connection details from command-line arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

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

    # Delete all states containing the letter 'a'
    delete_state = session.query(State).filter(State.name.like('%a%')).all()

    if delete_state:
        for erase in delete_state:
            session.delete(erase)
        session.commit()

    # Close the session to release database resources
    session.close()
