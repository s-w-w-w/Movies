import sqlite3
from config.config import DBFile

"""
DBConnect() - Establish connection to a Sqlite3 database
"""
class DBConnect():
    """
    __init__() - constructor
    """
    def __init__(self):
        connection = sqlite3.connect(DBFile)
        connection.row_factory = sqlite3.Row
        self._connection = connection
        self._cursor = connection.cursor()
        

