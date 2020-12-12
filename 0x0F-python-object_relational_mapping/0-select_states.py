#!/usr/bin/python3
"""
List all states from a given db sorted in ascending order by id
Username, password, and database names are given as user args
"""


if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         database=argv[3],
                         host='localhost',
                         port=3306
                         )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close
    db.close
