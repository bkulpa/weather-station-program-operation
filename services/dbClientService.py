import os

import mysql.connector


def get_database_instance():
    """Create and return a MySQL database connection."""
    try:
        return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_DATABASE"),
        )
    except mysql.connector.Error as error:
        print(f"MySQL error: {error}")
        return None
