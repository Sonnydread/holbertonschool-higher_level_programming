#!/usr/bin/python3
""" takes in arguments and displays all values in the states of hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cursor = db.cursor()
    request = "SELECT * FROM states WHERE name LIKE \
               BINARY %s ORDER BY states.id ASC"
    cursor.execute(request, (argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
