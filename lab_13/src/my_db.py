import sqlite3
from sqlite3 import Connection, Cursor


class MyDb:
    def __init__(self, connection):
        self.connection: Connection = connection
        self.cursor: Cursor = connection.cursor()

    def table_exists(self):
        self.cursor.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='student'; ''')
        return self.cursor.fetchone()[0] == 1

    def reset_db(self):
        self.cursor.execute('drop table student')
        self.create_db()

    def create_db(self):
        if self.table_exists():
            return
            # self.cursor.execute('drop table student')
        self.cursor.execute('''create table student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            full_name TEXT,
            indeks TEXT
        );''')
