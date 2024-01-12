#!/usr/bin/env python3
"""
lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """
    Connecting to th mysql server
    """
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    """
    executing the cursor funciotn of the database
    """
    cur = db.cursor()

    """
    obtaining th query results
    and fetch them all
    """
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
