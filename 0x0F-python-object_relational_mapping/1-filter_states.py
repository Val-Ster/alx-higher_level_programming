#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

def get_states(username, password, database):
    """
    Retrieve and print all states with names starting with 'N' sorted by id
    """
    db = MySQLdb.connect(host='localhost', port=3306,
            user=username, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    username, password, database = sys.argv[1:]
    get_states(username, password, database)

