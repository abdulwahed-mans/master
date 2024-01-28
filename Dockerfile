FROM python:3.10

# Create a working directory
WORKDIR /usr/src/app

# Copy project files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Migrate database
RUN python manage.py makemigrations
RUN python manage.py migrate

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
