#!/usr/bin/python3
# Script that lists all states from a database

if __name__ == "__main__":

    from sys import argv
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    import MySQLdb
    db = MySQLdb.connect(host='localhost', user=username, port=3306,
                         passwd=password, db=database)

    cur = db.cursor()
    sql = "SELECT * FROM states WHERE name = '{}'\
            ORDER BY id ASC".format(state_name)
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
            print("{}".format(row))
