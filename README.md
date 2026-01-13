# Vehicle Management System

Vehicle Management System is a Django-based web application designed to manage vehicles and related data.
The project focuses on backend development, database integration, and application configuration, simulating a real-world management system.

This application was developed as a personal project to practice backend development with Django and relational databases.

---

## Features

- Create, update, and delete vehicle records
- Backend logic implemented with Django
- Database integration using Django ORM
- CRUD operations for vehicle management
- Environment-based configuration using local settings

---

## Technologies Used

- Python
- Django
- HTML
- CSS
- Relational Database (PostgreSQL or SQLite)
- Git

---

## Project Structure

- Django project structure with clear separation of apps
- Local configuration handled via `local_settings.py`
- Database migrations managed with Django ORM

---

## Run Locally

Follow these steps to run the project on your local machine:

### 1. Clone the repository
```bash
git clone https://github.com/Daviz96/Veichle-Management-System.git
cd Veichle-Management-System
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment settings

Create a file named `local_settings.py` inside the project directory and add:

```python
SECRET_KEY = 'your-secret-key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
```

*(PostgreSQL can also be configured if preferred.)*

---

### 5. Apply migrations
```bash
python manage.py migrate
```

### 6. Run the development server
```bash
python manage.py runserver
```

Open your browser at:
```
http://127.0.0.1:8000/
```

---

## Purpose of the Project

The goal of this project was to:
- Practice backend development with Django
- Work with relational databases and ORM
- Manage structured data with CRUD operations
- Configure and run a Django project in a local environment

---

## Author

Developed by **Dawid Sebastian Wrzesiński**

GitHub: https://github.com/Daviz96
