#!/usr/bin/python3
"""
Return info from both tables (tables 'cities' 'states)
parameters given to script: mysql username, mysql password,
mysql database
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

    # create cursor to exec queries using SQL; join two tables for all info
    cursor = db.cursor()
    query = """SELECT cities.id, cities.name, states.name
                 FROM states
                 INNER JOIN cities ON states.id = cities.state_id
                 ORDER BY cities.id ASC"""
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
