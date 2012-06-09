from __future__ import unicode_literals, print_function 
from com.gmail.takashi316.lib.sqlite import getSqliteUrl

from sqlalchemy import create_engine as _create_engine
engine = _create_engine(getSqliteUrl(), echo=False)
from sqlalchemy.orm.session import sessionmaker as _sessionmaker
Session = _sessionmaker(bind=engine, autocommit=False)
PersistentSession = _sessionmaker(bind=engine, autocommit=True)

from unittest import TestCase, main
if __name__ == "__main__":
    main()