#!/usr/bin/python3
""" takes in arguments and displays all values in the states of hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    kursor = db.cursor()
    kursor.execute (sys.argv[4])
    rows = kursor.fetchall()
    for row in rows:
        print(row)
    kursor.close()
    db.close()
