# tasks.py

from celery import shared_task
from datetime import date
from django.core.mail import send_mail
from .models import Task

@shared_task
def check_overdue_tasks():
    today = date.today()
    overdue_tasks = Task.objects.filter(due_date__lt=today, completed=False)

    for task in overdue_tasks:
        # Send notifications (e.g., email) for overdue tasks
        send_mail(
            'Task Overdue',
            f'Task "{task.title}" is overdue.',
            'your_email@example.com',
            [task.user.email],
            fail_silently=False,
        )
