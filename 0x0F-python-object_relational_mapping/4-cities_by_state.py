#!/usr/bin/python3
# Script that lists all states from a database

if __name__ == "__main__":

    from sys import argv
    username = argv[1]
    password = argv[2]
    database = argv[3]

    import MySQLdb
    db = MySQLdb.connect(host='localhost', user=username, port=3306,
                         passwd=password, db=database)

    cur = db.cursor()
    sql = "SELECT cities.id, cities.name, states.name\
           FROM cities\
           INNER JOIN states\
           ON cities.state_id=states.id\
           ORDER BY id ASC"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
