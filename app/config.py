from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create sqlite engine instance

# engine = create_engine("sqlite:///todo.db")
engine = create_engine("mysql+pymysql://root:admin@127.0.0.1:3306/test")

# Create declaritive base meta instance
Base = declarative_base()

# Create session local class for session maker
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
