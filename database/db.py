import sqlite3
import os
from contextlib import closing
from datetime import datetime
from werkzeug.security import generate_password_hash

# Path to the SQLite database file in project root
DATABASE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'spendly.db')


def get_db():
    """Return a SQLite connection with row_factory and foreign keys enabled."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    # Enable foreign key constraints
    conn.execute('PRAGMA foreign_keys = ON')
    return conn


def init_db():
    """Create all tables using CREATE TABLE IF NOT EXISTS."""
    with closing(get_db()) as conn:
        # Users table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT DEFAULT (datetime('now'))
            )
        ''')

        # Expenses table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL,
                description TEXT,
                created_at TEXT DEFAULT (datetime('now')),
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        ''')

        conn.commit()


def seed_db():
    """Insert sample data for development."""
    with closing(get_db()) as conn:
        # Check if users table already contains data
        existing_user = conn.execute('SELECT id FROM users LIMIT 1').fetchone()
        if existing_user:
            return  # Already seeded

        # Insert demo user
        password_hash = generate_password_hash('demo123', method='pbkdf2:sha256')
        conn.execute(
            'INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)',
            ('Demo User', 'demo@spendly.com', password_hash)
        )

        # Get the demo user ID
        user = conn.execute('SELECT id FROM users WHERE email = ?', ('demo@spendly.com',)).fetchone()
        if not user:
            return

        user_id = user['id']

        # Current month for dates
        now = datetime.now()
        current_month = now.strftime('%Y-%m')

        # 8 sample expenses covering all 7 categories + one extra (Food)
        sample_expenses = [
            (user_id, 25.50, 'Food', f'{current_month}-02', 'Lunch at cafe'),
            (user_id, 15.00, 'Transport', f'{current_month}-05', 'Bus fare'),
            (user_id, 120.00, 'Bills', f'{current_month}-08', 'Electricity bill'),
            (user_id, 35.00, 'Health', f'{current_month}-10', 'Pharmacy'),
            (user_id, 18.00, 'Entertainment', f'{current_month}-12', 'Movie ticket'),
            (user_id, 89.99, 'Shopping', f'{current_month}-15', 'New headphones'),
            (user_id, 45.00, 'Food', f'{current_month}-18', 'Dinner with friends'),
            (user_id, 20.00, 'Other', f'{current_month}-20', 'Miscellaneous'),
        ]

        for expense in sample_expenses:
            conn.execute(
                '''INSERT INTO expenses (user_id, amount, category, date, description)
                   VALUES (?, ?, ?, ?, ?)''',
                expense
            )

        conn.commit()


if __name__ == '__main__':
    # Allow running this file directly to initialize and seed the database
    init_db()
    seed_db()
    print("Database initialized and seeded successfully!")