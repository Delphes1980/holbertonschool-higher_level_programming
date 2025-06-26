#!/usr/bin/python3
"""
This module displays all values in the states table where 'name' matches the
argument 'state name searched' (safe from MySQL injection) 
"""
import MySQLdb
import sys


if __name__ =="__main__":
	user = sys.argv[1]
	password = sys.argv[2]
	db_name = sys.argv[3]
	state_name_search = sys.argv[4]

	db = MySQLdb.connect(host='localhost',
						 user=user,
						 passwd=password,
						 database=db_name,
						 port=3306)

	cur = db.cursor()

	query = """SELECT *
				FROM states
				WHERE BINARY name = %s
				ORDER BY id ASC;""".format(state_name_search)

	cur.execute(query, (state_name_search,))

	states = cur.fetchall()

	for id, name in states:
		print(f"({id}, '{name}')")

	cur.close()
	db.close()
