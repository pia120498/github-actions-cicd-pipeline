"""
task_service.py

Provides task-related operations.
"""

from db import get_connection


def get_tasks():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT
            id,
            name,
            completed
        FROM tasks
        ORDER BY id;
        """
    )

    tasks = cursor.fetchall()

    cursor.close()
    connection.close()

    return tasks