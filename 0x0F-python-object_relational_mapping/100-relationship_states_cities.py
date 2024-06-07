#!/usr/bin/python3
"""
Creates the State “California” with City “San Francisco”
in the database hbtn_0e_100_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def main():
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}'
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)
    session.add(california)
    session.commit()

    print(f"{california.id}")
    session.close()


if __name__ == "__main__":
    main()
