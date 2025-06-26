#!./venv/bin/python3
"""
This module  a script that takes in the name of a state as an argument and
lists all cities of that state from a specified database
"""
import MySQLdb
import sys


if __name__ == "__main__":
	# Get MySQL credentials and database name from command_line arguments
	user = sys.argv[1]
	password = sys.argv[2]
	db_name = sys.argv[3]
	state_name = sys.argv[4]

	# Establish database connection
	db = MySQLdb.connect(host='localhost',
						 user=user,
						 passwd=password,
						 database=db_name,
						 port=3306)

	# Create a cursor to execute queries
	cur = db.cursor()

	# SQL query: Selects city name for cities belonging to the specified state
	query = """SELECT cities.id, cities.name, states.name
			FROM cities
			INNER JOIN states
			ON cities.state_id = states.id
			WHERE states.name = %s
			ORDER BY cities.id ASC;"""

	cur.execute(query, (state_name,))

	# Fetch all results from the executed query
	city = cur.fetchall()

	# Collect city names into a list
	city_names = [row[1] for row in city]

	# Initialize an empty string to build the output
	list_names = ""
	# Loop through the city names to add them to the string
	for i in range(len(city_names)):
		list_names += city_names[i]
		if i < len(city_names) -1:
			list_names += ","
	print(list_names)

	# Close the cursor and the database connection
	cur.close()
	db.close()