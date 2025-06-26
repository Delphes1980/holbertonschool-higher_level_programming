#!/usr/bin/python3
"""
This module lists all cities from a specified database,
displaying their ID, name, and the name of the state they belong to
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL credentials and database name from command_line arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Establish database connection
    db = MySQLdb.connect(host='localhost', user=user,
                         passwd=password, database=db_name, port=3306)

    # Create a cursor to execute queries
    cur = db.cursor()

    # SQL query: Selects city ID, city name, and the corresponding state name
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                INNER JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id ASC;""")
    # Fetch all results from the executed query
    city = cur.fetchall()

    # Print each state
    for id, c_name, s_name in city:
        print(f"({id}, '{c_name}', '{s_name}')")

    # Close the cursor and the database connection
    cur.close()
    db.close()
