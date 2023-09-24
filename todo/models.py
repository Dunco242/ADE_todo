from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
	task_name = models.CharField(null=True, blank=True, max_length=45)
	task_description = models.TextField()
	task_priority = models.IntegerField()
	due_date = models.DateTimeField()
	completed =models.BooleanField(default=False)
	task_created_at =models.DateTimeField(auto_now_add=True)
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	notification_sent = models.BooleanField(default=False)




class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)