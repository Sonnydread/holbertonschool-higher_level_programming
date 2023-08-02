#!/usr/bin/python3
""" takes in arguments and displays all values in the states of hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3]), port=3306)
    kur = db.cursor()
    kur.execute("""SELECT id, name
                FROM states
                WHERE BINARY name = %s
                ORDER BY id""", (sys.argv[4],))
    rows = kur.fetchall()
    for row in rows:
        print(row)
    kur.close()
    db.close()
