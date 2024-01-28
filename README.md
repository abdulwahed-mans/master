# master
Backend Django project

```bach
pip install python-dotenv

```

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

### create .env file

```py
DATABASE_NAME=my_database
DATABASE_USER=my_user
DATABASE_PASSWORD=my_password
DATABASE_HOST=localhost
```

```bash
docker-compose up -d
```
