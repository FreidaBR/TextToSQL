from pathlib import Path
import sqlite3

DATABASE = Path(__file__).resolve().parent.parent / "database" / "ecommerce.db"

def get_connection():
    return sqlite3.connect(DATABASE)