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


def add_task(task_name):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO tasks (name, completed) VALUES (%s, %s)",
        (task_name, False),
    )

    connection.commit()

    cursor.close()
    connection.close()