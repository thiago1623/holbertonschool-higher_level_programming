#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the states
safe from MySQL injections!
"""


if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         database=argv[3],
                         host='localhost',
                         port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states\
                    WHERE name LIKE %s\
                    ORDER BY states.id", (argv[4],))

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
