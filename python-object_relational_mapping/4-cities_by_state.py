#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    request = "SELECT cities.id, cities.name, states.name \
              FROM cities \
              JOIN states WHERE cities.state_id = states.id"

    cursor.execute(request)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
