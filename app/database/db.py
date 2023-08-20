""" SQLITE3 Database Config """
from sqlalchemy import create_engine

DATABASE_URL = 'sqlite:///app/database/app.db'
engine = create_engine(DATABASE_URL, echo=False)
