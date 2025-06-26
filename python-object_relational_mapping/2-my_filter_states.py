#!/usr/bin/python3
"""
This module displays all values in the states table where 'name' matches the
argument 'state name searched'
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL credentials and database name from command_line arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name_search = sys.argv[4]

    # Establish database connection
    db = MySQLdb.connect(host='localhost',
                         user=user,
                         passwd=password,
                         database=db_name,
                         port=3306)

    # Create a cursor to execute queries
    cur = db.cursor()

    # SQL query: Selects all states where the 'name' column exactly matches
    # the provided argument
    query = """SELECT *
                FROM states
                WHERE name = '{}'
                ORDER BY id ASC;""".format(state_name_search)
    cur.execute(query)

    # Fetch all results from the executed query
    states = cur.fetchall()

    # Print each state
    for id, name in states:
        print(f"({id}, '{name}')")

    # Close the cursor and the database connection
    cur.close()
    db.close()
