# Set up a database connection, handle transactions and initialize the base model using SQLAlchemy engine. 
# Handled get_database and create_database functions to provide database sessions and create tables.

from sqlalchemy import create_engine

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)

from app.config import DATABASE_URL



# Creating database engine
engine = create_engine(

    DATABASE_URL,

    connect_args={

        "check_same_thread": False

    }

    if DATABASE_URL.startswith("sqlite")

    else {}

)



# Creating database session
SessionLocal = sessionmaker(

    autocommit=False,

    autoflush=False,

    bind=engine

)



# Creating database base class
Base = declarative_base()



# Providing database session
def get_database():

    db = SessionLocal()

    try:

        # Yielding database session
        yield db

    finally:

        # Closing database session
        db.close()



# Creating database tables
def create_database():

    from database import models

    # Creating tables from models
    Base.metadata.create_all(

        bind=engine

    )