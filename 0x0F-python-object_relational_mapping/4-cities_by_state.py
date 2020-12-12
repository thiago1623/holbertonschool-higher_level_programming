#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
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
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                    INNER JOIN states ON cities.state_id = states.id\
                    ORDER BY cities.id")

    cities = cursor.fetchall()
    for city in cities:
        print(city)

    cursor.close()
    db.close()
