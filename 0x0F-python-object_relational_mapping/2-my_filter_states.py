#!/usr/bin/python3
"""
Return matching states
parameters given to script: mysql username, mysql password,
mysql database, state to match
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # create cursor to exec queries using SQL; match arg given
    cursor = db.cursor()
    query = """SELECT *
                 FROM states
                 WHERE name LIKE '{:s}' ORDER BY id ASC""".format(argv[4])
    cursor.execute(query)
    for row in cursor.fetchall():
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    db.close()
