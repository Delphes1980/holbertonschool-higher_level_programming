#!/usr/bin/python3
"""
This module lists all states from a specified database
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

    # SQL query: Selects all 'id' and 'name' from the 'states' table
    cur.execute("SELECT id, name FROM states ORDER BY id ASC;")
    # Fetch all results from the executed query
    states = cur.fetchall()

    # Print each state
    for id, name in states:
        print(f"({id}, '{name}')")

    # Close the cursor and the database connection
    cur.close()
    db.close()
