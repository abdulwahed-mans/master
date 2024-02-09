
from django.urls import path
from django.contrib.auth import views as auth_views  # Built-in auth views
from . import views  # Import your custom views from the 'users' app

app_name = 'users'


urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.password_reset_done_view, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.password_reset_confirm_view, name='password_reset_confirm'),
    path('reset/done/', auth_views.password_reset_complete_view, name='password_reset_complete'),
    # ... other password reset URLs ...

    # Your custom URLs
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    # ... more custom URLs ...
]


"""
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_change/', views.password_change_view, name='password_change'),
    path('password_change/done/', views.password_change_done_view, name='password_change_done'),
    path('password_reset/', views.password_reset_view, name='password_reset'),
    path('password_reset/done/', views.password_reset_done_view, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm_view, name='password_reset_confirm'),
    path('reset/done/', views.password_reset_complete_view, name='password_reset_complete'),
    # Add other URL patterns for user-related views as needed
]


"""
