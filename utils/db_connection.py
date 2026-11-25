"""
utils/db_connection.py
----------------------
Database connection helper using mysql-connector-python.
"""

import logging
import mysql.connector
from mysql.connector import Error
from config import Config

logger = logging.getLogger(__name__)


class DBConnection:
    """Wraps a MySQL connection with execute helpers."""

    def __init__(self):
        self._conn = None
        self.connect()

    def connect(self):
        try:
            self._conn = mysql.connector.connect(
                host=Config.DB_HOST,
                port=int(Config.DB_PORT or 3306),
                database=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                autocommit=False,
            )
        except Error as e:
            logger.error("DB connection failed: %s", e)
            raise

    def _ensure_connected(self):
        if self._conn is None or not self._conn.is_connected():
            self.connect()

    def execute_query(self, query, params=None, fetch=True):
        """Run a query and optionally return rows as list of dicts."""
        self._ensure_connected()
        try:
            cursor = self._conn.cursor(dictionary=True)
            cursor.execute(query, params or ())
            if fetch:
                result = cursor.fetchall()
            else:
                self._conn.commit()
                result = cursor.lastrowid
            cursor.close()
            return result
        except Error as e:
            self._conn.rollback()
            logger.error("Query failed: %s", e)
            raise

    def execute_many(self, query, values):
        self._ensure_connected()
        try:
            cursor = self._conn.cursor()
            cursor.executemany(query, values)
            self._conn.commit()
            rows = cursor.rowcount
            cursor.close()
            return rows
        except Error as e:
            self._conn.rollback()
            raise

    def commit(self):
        if self._conn:
            self._conn.commit()

    def rollback(self):
        if self._conn:
            self._conn.rollback()

    def close(self):
        if self._conn and self._conn.is_connected():
            self._conn.close()


_instance = None


def get_db_connection() -> DBConnection:
    global _instance
    if _instance is None or not _instance._conn or not _instance._conn.is_connected():
        _instance = DBConnection()
    return _instance
