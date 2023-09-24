# middleware.py
from datetime import date
from django.contrib import messages
from .models import Task

class TaskNotificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            today = date.today()
            incomplete_tasks = Task.objects.filter(
                due_date__lt=today, completed=False, creator=request.user
            )

            if incomplete_tasks.exists():
                message = (
                    f"You have incomplete tasks. "
                    f"Please complete or delete them to remove this notification."
                )
                messages.warning(request, message)

        response = self.get_response(request)
        return response
