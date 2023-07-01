from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
### database settings
"""
Path to Sqlite3 database file path
"""
DBFile = BASE_DIR / 'data' / 'data.db'


