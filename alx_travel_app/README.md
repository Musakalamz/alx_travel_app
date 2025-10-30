# ALX Travel App

A comprehensive travel listing platform built with Django and Django REST Framework.

## Features

- RESTful API architecture
- MySQL database integration
- Swagger/OpenAPI documentation
- CORS support for frontend integration
- Environment-based configuration
- Celery support for background tasks

## Setup Instructions

### Prerequisites

- Python 3.8+
- MySQL 5.7+
- Git

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/alx_travel_app.git
cd alx_travel_app
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver
```

## API Documentation

Once the server is running, you can access the API documentation at:

- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/

## Project Structure

alx_travel_app/
│
├── alx_travel_app/
│ ├── **init**.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── listings/
│ ├── **init**.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ └── tests.py
│
├── manage.py
├── requirements.txt
└── .env
