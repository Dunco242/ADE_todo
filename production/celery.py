from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'production.settings')

# Create a Celery instance.
app = Celery('production')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover tasks in all installed apps, including Django apps.
app.autodiscover_tasks()

# Define your task routes (if needed).
# app.conf.task_routes = {
#     'your_app.tasks.*': {'queue': 'your_queue_name'},
# }

# You can add more configuration options as needed.

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
