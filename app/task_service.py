"""
task_service.py

Provides task data for the application.

Currently returns hardcoded sample tasks.
Later, this module will fetch tasks from MySQL.
"""


def get_tasks():
    return [
        {"name": "Configure GitHub Actions", "completed": True},
        
        {"name": "Deploy Docker Container", "completed": False},
        
        {"name": "Deploy to Kubernetes", "completed": False},
    ]