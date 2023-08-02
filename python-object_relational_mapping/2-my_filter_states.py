#!/usr/bin/python3
"""takes an argument and displays all values in the states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states \
             WHERE name LIKE BINARY '{}'\
             ORDER BY states.id ASC".format(argv[4]))

    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()
