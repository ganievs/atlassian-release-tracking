import sqlite3
from contextlib import contextmanager


@contextmanager
def db_ops(database: str):
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    yield cur
    conn.commit()
    conn.close()
