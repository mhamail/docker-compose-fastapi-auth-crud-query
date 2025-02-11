from http.client import HTTPException
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from querysqlalchemy.load_env import db

SQLALCHEMY_DATABASE_URL = db

connection_string = str(SQLALCHEMY_DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)

# engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)

engine = create_engine(connection_string, connect_args={}, pool_recycle=300)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    except OperationalError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database operational error")

    finally:
        db.close()
