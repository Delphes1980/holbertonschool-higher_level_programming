#!/usr/bin/python3
"""
This module lists all states from a specified database
"""
import MySQLdb
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost",port=3306, user=user,
                         passwd=password, database=db_name)

    cur = db.cursor()

    cur.execute("SELECT id, name FROM states ORDER BY id ASC;")
    states = cur.fetchall()

    for id, name in states:
        print(f"({id}, '{name}'")

    cur.close()
    db.close()
