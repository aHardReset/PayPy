import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "paypy.db"


def get_connection():
    """Get a connection to the SQLite database."""
    return sqlite3.connect(DB_PATH)


def init_db():
    """Initialize the database with tables and populate with dummy data if needed."""
    conn = get_connection()
    cursor = conn.cursor()

    # Track if we need to populate data (true if tables were just created)
    should_populate = False

    # Check if tables exist
    cursor.execute("""
        SELECT name FROM sqlite_master
        WHERE type='table' AND name='users'
    """)

    if cursor.fetchone() is None:
        should_populate = True

    # Create tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS countries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            country_code TEXT NOT NULL UNIQUE,
            country_name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            legal_name TEXT NOT NULL,
            nickname TEXT NOT NULL,
            password TEXT NOT NULL,
            country_id INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (country_id) REFERENCES countries(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            sender_id INTEGER,
            recipient_id INTEGER,
            amount REAL NOT NULL,
            note TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (sender_id) REFERENCES users(id),
            FOREIGN KEY (recipient_id) REFERENCES users(id)
        )
    """)

    conn.commit()

    # Populate dummy data if tables were just created
    if should_populate:
        _populate_dummy_data(conn)

    conn.close()

    return should_populate


def _populate_dummy_data(conn):
    """Populate the database with dummy data."""
    cursor = conn.cursor()

    # Insert countries
    cursor.executemany("""
        INSERT INTO countries (country_code, country_name) VALUES (?, ?)
    """, [
        ('US', 'Estados Unidos'),
        ('CA', 'Canadá'),
        ('MX', 'México'),
        ('GB', 'Reino Unido'),
        ('DE', 'Alemania'),
    ])

    # Insert users
    cursor.executemany("""
        INSERT INTO users (legal_name, nickname, password, country_id) VALUES (?, ?, ?, ?)
    """, [
        ('John Doe', 'johnd', 'password123', 1),
        ('Jane Smith', 'janes', 'password456', 1),
        ('Bob Johnson', 'bobj', 'password789', 2),
        ('Alice Williams', 'alicew', 'passwordabc', 1),
        ('Carlos García', 'carlosg', 'password321', 3),
        ('María López', 'marial', 'password654', 3),
    ])

    # Insert initial transactions (deposits to give users starting balance)
    cursor.executemany("""
        INSERT INTO transactions (user_id, sender_id, recipient_id, amount, note) VALUES (?, ?, ?, ?, ?)
    """, [
        (1, 1, None, 1000.00, 'Depósito inicial'),
        (2, 2, None, 500.00, 'Depósito inicial'),
        (3, 3, None, 750.00, 'Depósito inicial'),
        (4, 4, None, 1200.00, 'Depósito inicial'),
        (5, 5, None, 800.00, 'Depósito inicial'),
        (6, 6, None, 950.00, 'Depósito inicial'),
    ])

    conn.commit()
    print("✓ Database populated with dummy data")


if __name__ == "__main__":
    was_created = init_db()
    if was_created:
        print("✓ Database tables created and populated")
    else:
        print("✓ Database already exists")
