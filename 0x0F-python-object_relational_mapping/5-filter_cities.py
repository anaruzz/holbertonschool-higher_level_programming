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
    sql = "SELECT cities.name\
           FROM cities\
           INNER JOIN states\
           ON cities.state_id=states.id\
           WHERE states.name = '{}'".format(state_name)
    cur.execute(sql)
    rows = cur.fetchall()
    results = []
    for city in rows:
        results.append(city[0])
    results = ', '.join(results)

    print(results)

    cur.close()
    db.close()
