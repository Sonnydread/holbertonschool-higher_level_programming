#!/usr/bin/python3
"""script that list all states from hbtn_0e_0_usa"""


import sys
import MySQLdb

if __name__ == "__main__":
    host = "localhost"
    user = sys.argv[1]
    password = sys.argv[2]
    data_base = sys.argv[3]

    conection = MySQLdb.connect(host=host, user=user, passwd=password,
                                db=data_base, port=3306)
    cursor = conection.cursor()

    querie = "SELECT * FROM states ORDER BY id"
    cursor.execute(querie)

    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    conection.close()
