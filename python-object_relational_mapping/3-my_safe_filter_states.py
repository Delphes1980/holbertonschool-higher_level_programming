#!/usr/bin/python3
"""
This module displays all values in the states table where 'name' matches the
argument 'state name searched' (safe from MySQL injection)
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

    # Using '%s' as a placeholder for the variable makes the query safe from SQL injection
    query = """SELECT *
                FROM states
                WHERE BINARY name = %s
                ORDER BY id ASC;"""

    cur.execute(query, (state_name_search,))

    # Fetch all results from the executed query
    states = cur.fetchall()

    for id, name in states:
        print(f"({id}, '{name}')")

    # Close the cursor and the database connection
    cur.close()
    db.close()
