#!/usr/bin/python3
"""
Lists all State objects and
corresponding City objects from the database hbtn_0e_101_usa.
Usage: ./101-relationship_states_cities_list.py
<mysql username> <mysql password> <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City


def main():
    if len(sys.argv) != 4:
        print("Usage: ./101-relationship_states_cities_list.py "
              "<mysql username> <mysql password> <database name>")
        return

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        for state in session.query(State).order_by(State.id):
            print("{}: {}".format(state.id, state.name))
            for city in state.cities:
                print("    {}: {}".format(city.id, city.name))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    main()
