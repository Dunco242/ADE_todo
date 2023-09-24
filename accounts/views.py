from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from todo.views import task_index

@login_required
def home(request):
    return render('todo:index', request)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('accounts:home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Custom logout view
def custom_logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('todo:index')  # Redirect to the desired page after logout

