
import sqlite3
from typing import Optional
from layers.models import User

class SQLiteUserRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    #  Agrega una constraint (p. ej., first NOT NULL)
    def _create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            first TEXT NOT NULL,
            last TEXT
        )
        """)

    def find_by_id(self, user_id: int) -> Optional[User]:
        cur = self.conn.cursor()
        cur.execute("SELECT id, first, last FROM users WHERE id = ?", (user_id,))
        row = cur.fetchone()
        if row is None:
            return None
        return User(id=row[0], first=row[1], last=row[2])
