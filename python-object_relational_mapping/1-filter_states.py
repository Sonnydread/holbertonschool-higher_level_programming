#!/usr/bin/python3
"""list all states names starting with N"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    request = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id"
    rows_number = cursor.execute(request)

    for row in range(rows_number):
        print(cursor.fetchone())

    cursor.close()
    db.close()
