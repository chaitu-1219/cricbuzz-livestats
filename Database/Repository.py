"""
Repository Layer
----------------
Reusable CRUD operations for database access.
"""

import logging
from utils.db_connection import get_db_connection

logger = logging.getLogger(__name__)


class Repository:
    """
    Repository pattern implementation for database operations.
    Provides reusable CRUD methods with proper error handling.
    """

    def __init__(self):
        self.db = get_db_connection()

    def fetch_all(self, query, params=None):
        """
        Fetch all rows matching the query.
        
        Args:
            query (str): SQL query to execute
            params (tuple): Query parameters
            
        Returns:
            list: List of dictionaries containing query results or empty list
        """
        try:
            result = self.db.execute_query(query, params, fetch=True)
            return result if result is not None else []
        except Exception as e:
            logger.error(f"Error in fetch_all: {e}")
            return []

    def fetch_one(self, query, params=None):
        """
        Fetch a single row matching the query.
        
        Args:
            query (str): SQL query to execute
            params (tuple): Query parameters
            
        Returns:
            dict: Single row result or None
        """
        results = self.db.execute_query(query, params, fetch=True)
        return results[0] if results else None

    def execute(self, query, params=None):
        """
        Execute a query without fetching results (INSERT, UPDATE, DELETE).

        Args:
            query (str): SQL query to execute
            params (tuple): Query parameters

        Returns:
            int: Last insert ID or number of affected rows
        """
        return self.db.execute_query(query, params, fetch=False)

    def execute_many(self, query, values):
        """
        Execute a query with multiple sets of parameters (bulk operations).
        
        Args:
            query (str): SQL query to execute
            values (list): List of parameter tuples
            
        Returns:
            int: Number of affected rows
        """
        return self.db.execute_many(query, values)

    def execute_query(self, query, params=None):
        """
        Execute a custom SQL query and return results.
        Wrapper method for backward compatibility.
        
        Args:
            query (str): SQL query to execute
            params (tuple): Query parameters
            
        Returns:
            list: Query results
        """
        return self.fetch_all(query, params)


# Note: do not instantiate at module level — DB may not be ready at import time.