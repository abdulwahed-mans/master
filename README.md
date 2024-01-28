## Django Backend

This is Backend Django project.

### Setup

#### 1. Create a virtual environment

```bash
python3 -m venv venv
```
#### 2. Activate the virtual environment
On Windows:
```bash
venv\Scripts\activate
```
On Unix or macOS:
```bash
source venv/bin/activate
```
#### 3. Install dependencies
```bash
pip install -r requirements.txt
```
#### 3. Apply migrations & run the development server
```bash
python manage.py migrate
python manage.py runserver
```
The Django backend will be running at http://localhost:8000/

#### Environment Variables
Create a .env file in the project root and configure the following environment variables:

```bach
pip install python-dotenv

```
#### Add this to the .env 

```py
DATABASE_NAME=my_database
DATABASE_USER=my_user
DATABASE_PASSWORD=my_password
DATABASE_HOST=localhost
```

#### Update sitting.py

```py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables using os.getenv()
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
```

## Docker
Alternatively, you can use Docker and Docker Compose to run the backend:
### Build the Docker image
```bash
docker-compose build
```
### Run the Docker containers
```bash
docker-compose up -d
```

