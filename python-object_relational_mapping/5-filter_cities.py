#!/usr/bin/python3
"""takes in the name of a state argument and lists all cities of that state"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    lh = "localhost"
    stnam = (argv[4],)

    conextion = MySQLdb.connect(host=lh, port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3])
    cursor = conextion.cursor()

    request = "SELECT c.name FROM cities AS c \
              INNER JOIN states AS s ON c.state_id = s.id \
              WHERE s.name=%s \
              ORDER BY c.id"
    cursor.execute(request, stnam)
    result = cursor.fetchall()

    xx = [row[0] for row in result]
    print(", ".join(xx))

    cursor.close()
    conextion.close()
