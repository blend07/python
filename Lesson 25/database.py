import sqlite3
from models import Movie, MovieCreate

def create_connection():
    connection = sqlite3.connect("movies.db")
    connection.row_factory = sqlite3.Row
    return connection