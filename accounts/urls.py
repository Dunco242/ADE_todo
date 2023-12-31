from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', views.custom_logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),  # You can set this to your task_index view
    # Add more authentication-related URLs as needed
]

