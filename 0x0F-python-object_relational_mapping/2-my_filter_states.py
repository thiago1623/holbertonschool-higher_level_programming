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
    cursor.execute("SELECT id, name FROM states\
                    WHERE name='{}'\
                    ORDER BY id ASC""".format(argv[4]))
    states = cursor.fetchall()

    for state in states:
        if state[1] == argv[4]:
            print(state)

    cursor.close
    db.close
