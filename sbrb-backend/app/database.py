from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False)
engine = None

def initialize_db(url):
    global SessionLocal, engine
    engine = create_engine(url, echo=True)
    # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    SessionLocal.configure(bind=engine)
    return engine
