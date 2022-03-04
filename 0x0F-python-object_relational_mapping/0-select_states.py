#!/usr/bin/python3

"""The script lists all states from the database"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Accesses the database and retrieves the states from the database"""

    connection = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                                 password=argv[2], database=argv[3])
    cur = connection.cursor()
    cur.execute("SELECT * FROM states")
    data = cur.fetchall()

    for row in data:
        print(row)
    cur.close()
    connection.close()
