from django.urls import path
from .views import home, RegisterView  # Import the view here
from .views import profile


urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),  # This is what we added
    path('profile/', profile, name='users-profile'),
]
