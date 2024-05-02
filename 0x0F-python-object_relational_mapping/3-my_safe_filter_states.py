#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument (safe from MySQL injection)
"""

import sys
import MySQLdb

def get_states(username, password, database, state_name):
    """
    Retrieve and print all states with names matching the provided state_name
    """
    db = MySQLdb.connect(host='localhost', port=3306,
            user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Using parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cursor.execute(query, (state_name,))

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]
    get_states(username, password, database, state_name)

