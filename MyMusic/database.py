import sqlite3

# -------------------------
# Database Connection
# -------------------------
def get_db_connection():
    conn = sqlite3.connect("music.db")
    conn.row_factory = sqlite3.Row
    return conn


# -------------------------
# Create Database & Tables
# -------------------------
def create_database():
    conn = sqlite3.connect("music.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS artists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            artist_id INTEGER,
            song_link TEXT,
            duration INTEGER,              -- duration in seconds
            release_year INTEGER,
            FOREIGN KEY (artist_id) REFERENCES artists(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS playlists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            user_id INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS playlist_songs (
            playlist_id INTEGER,
            song_id INTEGER,
            PRIMARY KEY (playlist_id, song_id),
            FOREIGN KEY (playlist_id) REFERENCES playlists(id),
            FOREIGN KEY (song_id) REFERENCES songs(id)
        )
    """)

    conn.commit()
    return conn, cursor


# -------------------------
# Insert Artists
# -------------------------
def insert_artists(artists, cursor):
    artist_ids = {}

    for artist in artists:
        cursor.execute(
            "INSERT OR IGNORE INTO artists (name) VALUES (?)",
            (artist,)
        )
        cursor.execute(
            "SELECT id FROM artists WHERE name = ?",
            (artist,)
        )
        artist_ids[artist] = cursor.fetchone()[0]

    return artist_ids


# -------------------------
# Insert Users
# -------------------------
def insert_users(users, cursor):
    user_ids = {}

    for user in users:
        cursor.execute(
            "INSERT OR IGNORE INTO users (username, email) VALUES (?, ?)",
            (user["username"], user.get("email"))
        )
        cursor.execute(
            "SELECT id FROM users WHERE username = ?",
            (user["username"],)
        )
        user_ids[user["username"]] = cursor.fetchone()[0]

    return user_ids


# -------------------------
# Insert Songs
# -------------------------
def insert_songs(songs_dict, artist_ids, cursor):
    """
    songs_dict format:
    {
        ("Song Title", "Artist Name"): {
            "link": "...",
            "duration": 210,
            "release_year": 2023
        }
    }
    """
    song_ids = {}

    for (title, artist), info in songs_dict.items():
        cursor.execute("""
            INSERT INTO songs (title, artist_id, song_link, duration, release_year)
            VALUES (?, ?, ?, ?, ?)
        """, (
            title,
            artist_ids[artist],
            info.get("link"),
            info.get("duration"),
            info.get("release_year")
        ))

        song_ids[(title, artist)] = cursor.lastrowid

    return song_ids


# -------------------------
# Insert Playlists
# -------------------------
def insert_playlists(playlists, user_ids, cursor):
    """
    playlists format:
    {
        "Chill Vibes": {
            "username": "john",
            "songs": [(title, artist), ...]
        }
    }
    """
    playlist_ids = {}

    for playlist_name, data in playlists.items():
        cursor.execute("""
            INSERT INTO playlists (name, user_id)
            VALUES (?, ?)
        """, (
            playlist_name,
            user_ids[data["username"]]
        ))

        playlist_id = cursor.lastrowid
        playlist_ids[playlist_name] = playlist_id

    return playlist_ids


# -------------------------
# Link Songs to Playlists
# -------------------------
def insert_playlist_songs(playlists, playlist_ids, song_ids, cursor):
    for playlist_name, data in playlists.items():
        for song in data["songs"]:
            cursor.execute("""
                INSERT OR IGNORE INTO playlist_songs (playlist_id, song_id)
                VALUES (?, ?)
            """, (
                playlist_ids[playlist_name],
                song_ids[song]
            ))


# -------------------------
# Main Insert Function
# -------------------------
def insert_data(users, artists, songs_dict, playlists):
    conn, cursor = create_database()

    user_ids = insert_users(users, cursor)
    artist_ids = insert_artists(artists, cursor)
    song_ids = insert_songs(songs_dict, artist_ids, cursor)
    playlist_ids = insert_playlists(playlists, user_ids, cursor)
    insert_playlist_songs(playlists, playlist_ids, song_ids, cursor)

    conn.commit()
    conn.close()


# -------------------------
# Example Usage
# -------------------------
if __name__ == "__main__":
    users = [
        {"username": "john", "email": "john@example.com"},
        {"username": "sarah", "email": "sarah@example.com"}
    ]

    artists = ["Coldplay", "Adele"]

    songs_dict = {
        ("Yellow", "Coldplay"): {
            "link": "https://example.com/yellow",
            "duration": 270,
            "release_year": 2000
        },
        ("Hello", "Adele"): {
            "link": "https://example.com/hello",
            "duration": 295,
            "release_year": 2015
        }
    }

    playlists = {
        "My Favorites": {
            "username": "john",
            "songs": [("Yellow", "Coldplay"), ("Hello", "Adele")]
        }
    }

    insert_data(users, artists, songs_dict, playlists)
