from django.shortcuts import render, redirect,  get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from .forms import TaskForm
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib import messages





# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('todo:index')  # Redirect to the desired page after login
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('todo:index')  # Redirect to the desired page after logout




@login_required
def task_index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.creator = request.user
            task.save()
            messages.success(request, 'Task created successfully.')
            return redirect('todo:index')
    else:
        form = TaskForm()

    tasks = Task.objects.filter(creator=request.user)
    context = {'form': form, 'tasks': tasks}
    return render(request, 'index.html', context)




def list_tasks(request):
    todo = Task.objects.all()
    context = {'todo':todo}
    return render(request, 'list.html', context)


def update_task(request, id):
    obj = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()  # Save the updated form data to the database
            return redirect('todo:list-tasks')  # Redirect to the list view after updating
    else:
        form = TaskForm(instance=obj)

    context = {'form': form}
    return render(request, 'update.html', context)


def delete_task(request, id):
    obj = get_object_or_404(Task, id=id)
    obj.delete()
    return render(request, 'list.html', context=mydictionary)



@login_required
def calendar_view(request):
    tasks = Task.objects.filter(creator=request.user, due_date__isnull=False)
    context = {'tasks': tasks}
    return render(request, 'calendar.html', context)
