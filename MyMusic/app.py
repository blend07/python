import streamlit as st
import sqlite3
import pandas as pd

# -----------------------
# Database Connection
# -----------------------
def get_connection():
    conn = sqlite3.connect("music.db")
    return conn


# -----------------------
# Data Loaders
# -----------------------
def load_users():
    return pd.read_sql("SELECT * FROM users", get_connection())


def load_artists():
    return pd.read_sql("SELECT * FROM artists", get_connection())


def load_songs():
    query = """
    SELECT songs.id, songs.title, artists.name AS artist,
           songs.duration, songs.release_year
    FROM songs
    JOIN artists ON songs.artist_id = artists.id
    """
    return pd.read_sql(query, get_connection())


def load_playlists():
    query = """
    SELECT playlists.id, playlists.name AS playlist,
           users.username
    FROM playlists
    JOIN users ON playlists.user_id = users.id
    """
    return pd.read_sql(query, get_connection())


def load_playlist_songs():
    query = """
    SELECT playlists.name AS p
