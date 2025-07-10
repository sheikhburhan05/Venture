from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

load_dotenv()

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

try:
    if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
        engine = create_engine(
            SQLALCHEMY_DATABASE_URL,
            connect_args={"check_same_thread": False}
        )
    else:
        engine = create_engine(SQLALCHEMY_DATABASE_URL)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()

except SQLAlchemyError as e:
    raise HTTPException(
        status_code=500,
        detail=f"Database connection error: {str(e)}"
    )

def get_db():
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )
    finally:
        db.close()
