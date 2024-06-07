#!/usr/bin/python3
"""Script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument,
using parameterized queries to prevent SQL injection."""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./safe_select_states.py <mysql username> "
              "<mysql password> <database name> <state name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query with a parameterized query
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"

    try:
        # Execute the SQL query with the state name as parameter
        cursor.execute(query, (state_name,))

        # Fetch all the rows in a list of tuples
        results = cursor.fetchall()

        # Display the results
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))

    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()
