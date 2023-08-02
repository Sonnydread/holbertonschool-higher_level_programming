#!/usr/bin/python3
"""script that list all states from hbtn_0e_0_usa"""


import sys
import MySQLdb

if __name__ == "__main__":
    host = "localhost"
    username = sys.argv[1]
    passw = sys.argv[2]
    datbasnam = sys.argv[3]

    konex = MySQLdb.connect(host=host, username=username, passw=passw,
                                datbasnam=datbasnam, port=3306)
    kurs = conection.kurs()

    irie = "SELECT * FROM states ORDER BY id"
    kurs.execute(irie)

    result = kurs.fetchall()
    for row in result:
        print(row)

    kurs.close()
    conection.close()
