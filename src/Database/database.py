from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os 

def load_db_string():
    load_dotenv()
    return os.getenv("DATABASE_URL")

db_url = load_db_string()

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    
    try:
        return db
    except:
        db.close()