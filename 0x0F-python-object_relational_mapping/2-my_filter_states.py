#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
Usage: ./2-my_filter_states.py <mysql username>
<mysql password> <database name> <state name searched>
"""
import sys
import MySQLdb


def filter_states_by_name(username, password, db_name, state_name):
    """
    Connects to the MySQL database and displays all values in the states table
    where name matches the argument, sorted in ascending order by states.id.
    """
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=db_name, port=3306)
    c = db.cursor()
    query = ("SELECT * FROM states "
             "WHERE name LIKE BINARY '{}' "
             "ORDER BY id ASC").format(state_name)

    c.execute(query)
    [print(state) for state in c.fetchall()]


if __name__ == "__main__":
    filter_states_by_name(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
