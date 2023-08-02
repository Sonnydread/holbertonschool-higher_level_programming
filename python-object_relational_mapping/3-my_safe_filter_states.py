#!/usr/bin/python3
""" takes in arguments and displays all values in the states of hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    usnam = argv[1]
    pssw = argv[2]
    dbas = argv[3]
    stname = argv[4]

    db = MySQLdb.connect(host="localhost", user=usnam, passwd=pssw,
                         db=stname, port=3306)
    cursor = db.cursor()
    request = "SELECT * FROM states WHERE name LIKE \
               BINARY %s ORDER BY states.id ASC"
    cursor.execute(request, (stname,))
    
    for row in cursor.fetchall():
        print(row)
        
    cursor.close()
    db.close()
