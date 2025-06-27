#!/usr/bin/python3
"""
Script that lists all the cities associated to their state
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Validate the number of arguments passed
    if len(sys.argv) != 4:
        print("Usage : {} <user> <password> <db_name>".format(sys.argv[0]))
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

    # Find all 'City' objects associated to their states
    cities_list = (
        session.query(City, State)
        .join(State)
        .order_by(City.id.asc())
        .all()
    )

    for c_name, s_name in cities_list:
        print(f"{s_name.name}: ({c_name.id}) {c_name.name}")

    # Close the session to release database resources
    session.close()
