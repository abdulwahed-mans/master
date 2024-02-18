from django.shortcuts import render
from .models import Employee

def employee_list(request):
    # Initialize the queryset
    employees = Employee.objects.all()

    # Get query parameters for filtering
    department = request.GET.get('department')
    city = request.GET.get('city')
    salary_min = request.GET.get('salary_min')
    salary_max = request.GET.get('salary_max')

    # Apply filters if the parameters are provided
    if department:
        employees = employees.filter(department__icontains=department)
    if city:
        employees = employees.filter(city_of_residence__icontains=city)
    if salary_min:
        employees = employees.filter(salary__gte=salary_min)
    if salary_max:
        employees = employees.filter(salary__lte=salary_max)

    return render(request, 'employees/employee_list.html', {'employees': employees})
