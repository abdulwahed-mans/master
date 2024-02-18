from django.urls import path
from .views import employee_list

urlpatterns = [
    path('', employee_list, name='employee-list'),
]
