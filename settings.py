import os
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.ext.declarative.api import declarative_base
import sqlalchemy


BASE = os.path.dirname(__file__)
Engine = sqlalchemy.create_engine('sqlite:///%s'%(os.path.join(BASE, "data.db")), echo=True)
Entity = declarative_base(bind=Engine)

session_factory = sessionmaker(bind=Engine)
session = scoped_session(session_factory=session_factory)