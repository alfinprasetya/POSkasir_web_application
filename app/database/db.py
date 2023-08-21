""" SQLITE3 Database Config """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///app/database/app.db'
engine = create_engine(DATABASE_URL, echo=False)

Session = sessionmaker(bind=engine)
session = Session()
