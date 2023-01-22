import falcon

import settings
from resource import Resource

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine(
    '{engine}://{username}@{host}/{db_name}'.format(
        **settings.COCKROACH
    ),
    echo=settings.SQLALCHEMY['debug']
)

session = sessionmaker(
    bind=engine,
    autoflush=settings.SQLALCHEMY['autoflush'],
    autocommit=settings.SQLALCHEMY['autocommit']
)

app = falcon.App()

app.add_route('/pop', Resource(scoped_session(session)))
