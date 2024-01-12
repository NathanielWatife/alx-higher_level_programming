"""
	Listing all states 	from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == '__main__':
	"""
	_summary_
	Connecting to the MySQL server.
	"""
	db = MySQLdb.connect(
		username = sys.argv[1], 
		password=sys.argv[2],
		db = sys.argv[3],	
		port = 3306
	)

	"""	
	_summary_
	Creating a cursor object to interact with the database
	"""
	cursorObject = db.cursor()

	"""
	_summary_
	Executing the query to retrieve the states
	"""
	cursorObject.execute("SELECT * FROM states;")

	"""_summary_
	we fetch all the rows
	"""
	states = cursorObject.fetchall()

	for state in states:
		print(state)

	cursorObject.close()
	db.close()