import json
from django.core.management.base import BaseCommand
from employees.models import Employee

class Command(BaseCommand):
    help = 'Load a list of employees from a JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file containing employee data')

    def handle(self, *args, **kwargs):
        json_file_path = kwargs['json_file']
        with open(json_file_path, 'r') as file:
            employees = json.load(file)
            for emp in employees:
                employee = Employee(
                    id=emp['pk'],
                    first_name=emp['fields']['first_name'],
                    last_name=emp['fields']['last_name'],
                    email=emp['fields']['email'],
                    salary=emp['fields']['salary'],
                    department=emp['fields']['department'],
                    date_of_employment=emp['fields']['date_of_employment'],
                    city_of_residence=emp['fields']['city_of_residence'],
                    overtime_hours=emp['fields']['overtime_hours']
                )
                employee.save()
        self.stdout.write(self.style.SUCCESS('Successfully loaded all employees'))
