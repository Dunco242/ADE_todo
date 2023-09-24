from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
	path('', views.task_index, name='index'),
	path('task_index/', views.task_index, name='index'),
	path('list_tasks/', views.list_tasks, name='list-tasks'),
	path('update_task/<int:id>', views.update_task, name="update-task"),
	path('delete_task/<int:id>', views.delete_task, name="delete-task"),
	path('calendar/', views.calendar_view, name="calendar"),
	]