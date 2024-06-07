#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database hbtn_0e_0_usa.
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>
"""
import sys
import MySQLdb


def list_states_starting_with_N(username, password, db_name):
    """
    Connects to MySQL database and lists states starting with
    N in ascending order by id.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        db_name (str): The database name.
    """
    db = MySQLdb.connect(user=username, passwd=password, db=db_name, port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
              "ORDER BY id ASC")
    [print(state) for state in c.fetchall()]
    c.close()
    db.close()


if __name__ == "__main__":
    list_states_starting_with_N(sys.argv[1], sys.argv[2], sys.argv[3])
