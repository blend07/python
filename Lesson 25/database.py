import sqlite3
from models import Movie, MovieCreate

def create_connection():
    connection = sqlite3.connect("movies.db")
    connection.row_factory = sqlite3.Row
    return connection

def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS movies(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT NOT NULL,
                   director TEXT NOT NULL
                   ) 
                    """
    )
