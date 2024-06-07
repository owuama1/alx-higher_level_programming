#!/usr/bin/python3


# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb


def list_states(username, password, db_name):
    try:
        db = MySQLdb.connect(user=username, passwd=password, db=db_name)
        c = db.cursor()
        c.execute("SELECT * FROM states")
        states = c.fetchall()
        for state in states:
            print(state)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        if 'db' in locals() and db.open:
            c.close()
            db.close()


if __name__ == "__main__":
    #if len(sys.argv) != 4:
     #   print("Usage: ./0-select_states.py <mysql username> <mysql password> <database name>")
      #  sys.exit(1)
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
