"""
db.py

Creates a connection to the MySQL database.
"""

import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="taskdb"
    )