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

Musakalamz

Copy

Delete

Querying Power

Python Generators

Milestone 1

How PLDs Work (Step-by-Step) - Get it started!

Milestone 1: Setup and Database Configuration

Milestone 1: Setup and Database Configuration

Weight: 1

Project will start Oct 27, 2025 12:00 AM, must end by Nov 3, 2025 12:00 AM

Manual QA review must be done (request it when you are done with the project)

About the Project

The alx travel app project is a real-world Django application that serves as the foundation for a travel listing platform. This milestone focuses on setting up the initial project structure, configuring a robust database, and integrating tools to ensure API documentation and maintainable configurations. The aim is to equip learners with industry-standard best practices for starting and managing Django-based projects efficiently.

This milestone will teach you to set up a scalable backend, integrate MySQL for database management, and use Swagger for automated API documentation. These foundational steps are critical in preparing the application for future features and seamless team collaboration.

Learning Objective

As a professional developer, this task will enable you to:

Master Advanced Project Initialization :

Learn to bootstrap Django projects with modular, production-ready configurations.

Employ environment variable management for secure and scalable settings.

Integrate Key Developer Tools :

Set up and use Swagger (via drf-yasg) for API documentation.

Implement CORS headers and MySQL configurations for robust API interactions.

Collaborate Effectively Using Git :

Structure your projects for team collaboration with a version-controlled setup.

Adopt Industry Best Practices :

Follow best practices in managing dependencies, database configurations, and application structure.

Requirements

To successfully complete this milestone, ensure you meet the following prerequisites:

Familiarity with Django and Django REST Framework.

Knowledge of MySQL and database management.

Understanding of version control using Git.

A basic grasp of environment variable management using django-environ .

Key Highlights

Project Initialization :

Create a Django project named alx travel app .

Add an app named listings to encapsulate core functionalities.

Dependency Management :

Install essential packages:

django : Core framework for application development.

djangorestframework : REST API development.

django-cors-headers : Cross-Origin Resource Sharing setup.

drf-yasg : Swagger API documentation.

celery and rabbitmq : For future task queuing and background processes.

Settings Configuration :

Use django-environ to securely handle environment variables in .env files.

Configure MySQL as the primary database, ensuring proper connection handling in settings.py .

Set up REST framework and CORS headers for API support.

Swagger Integration :

Integrate Swagger for comprehensive API documentation.

Ensure all APIs are automatically documented and accessible at /swagger/ .

Version Control and Submission :

Initialize a Git repository and commit all project setup files.

Push your code to a GitHub repository named alx travel app with the specified structure.

Additional Resources

Build a CRUD API

Django Best Practices

Manage settings securely

Integrating drf-yasg for Swagger

📝 Project Assessment (Hybrid)

Your project will be evaluated primarily through manual reviews . To ensure you receive your full score, please:

✅ Complete your project on time

📄 Submit all required files

🔗 Generate your review link

👥 Have your peers review your work

An auto-check will also be in place to verify the presence of core files needed for manual review.

⏰ Important Note

If the deadline passes, you won’t be able to generate your review link—so be sure to submit on time!

We’re here to support your learning journey. Happy coding! ✨

Tasks

0. Django Project Setup with API Documentation and Database Configuration

mandatory

Objective

Set up the Django project with the necessary dependencies, configure the database, and add Swagger for API documentation.

Instructions

Create a Django Project:

Set up a new Django project named alx_travel_app .

Create an app within the project named listings .

Install necessary packages, including django, djangorestframework, django-cors- headers, celery, rabbitmq , and drf-yasg for Swagger documentation.

Configure Settings:

In settings.py , configure the project for REST framework and CORS headers.

Set up the database configuration to use MYSQL. Use environment variables for sensitive information such as database credentials. (Hint: Use the django-environ package to handle .env files).

Add Swagger:

Install drf-yasg for Swagger documentation.

Configure Swagger to automatically document all APIs. The documentation should be available at /swagger/ .

Initialize Git Repository:

Initialize a Git repository and make your initial commit with the project setup files.

Repo:

GitHub repository: alx_travel_app

Directory: alx_travel_app

File: alx_travel_app/requirement.txt, alx_travel_app/listings, alx_travel_app/settings.py, alx_travel_app/urls.py

1. Manual Review

mandatory

Repo:

GitHub repository: alx_travel_app

Directory: alx_travel_app

Trae

I'll help you set up the Django travel app project according to the specifications. Let me start by creating a comprehensive todo list to track our progress.

Let me start by examining the current directory structure and then proceed with setting up the Django project.

alx_travel_app

Perfect! The directory is empty, so we can start fresh. Let me begin by creating the Django project and installing the required dependencies.

First, let's create the Django project:

```
django-admin startproject 
alx_travel_app .
```

Let me start by creating the Django project structure. First, I'll create the requirements.txt file with all the necessary dependencies:

```
django>=4.2.0
djangorestframework>=3.14.0
django-cors-headers>=4.0.0
drf-yasg>=1.21.0
django-environ>=0.10.0
celery>=5.3.0
mysqlclient>=2.2.0
```

Now let me create the main Django project structure. I'll start by creating the manage.py file and the main project directory:

```
#!/usr/bin/env python
"""Django's command-line utility 
for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault
    ('DJANGO_SETTINGS_MODULE', 
    'alx_travel_app.settings')
    try:
        from django.core.management 
        import 
        execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import 
            Django. Are you sure 
            it's installed and "
            "available on your 
            PYTHONPATH environment 
            variable? Did you "
            "forget to activate a 
            virtual environment?"
        ) from exc
    execute_from_command_line(sys.
    argv)


if __name__ == '__main__':
    main()
```

Now let me create the main project directory and its files:

```
"""
ASGI config for alx_travel_app 
project.

It exposes the ASGI callable as a 
module-level variable named 
``application``.

For more information on this file, 
see
https://docs.djangoproject.com/en/4.
2/howto/deployment/asgi/
"""

import os

from django.core.asgi import 
get_asgi_application

os.environ.setdefault
('DJANGO_SETTINGS_MODULE', 
'alx_travel_app.settings')

application = get_asgi_application()
```

```
"""
WSGI config for alx_travel_app 
project.

It exposes the WSGI callable as a 
module-level variable named 
``application``.

For more information on this file, 
see
https://docs.djangoproject.com/en/4.
2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import 
get_wsgi_application

os.environ.setdefault
('DJANGO_SETTINGS_MODULE', 
'alx_travel_app.settings')

application = get_wsgi_application()
```

Now let me create the main settings.py file with all the required configurations:

```
"""
Django settings for alx_travel_app 
project.

Generated by 'django-admin 
startproject' using Django 4.2.

For more information on this file, 
see
https://docs.djangoproject.com/en/4.
2/topics/settings/

For the full list of settings and 
their values, see
https://docs.djangoproject.com/en/4.
2/ref/settings/
"""

import environ
from pathlib import Path

# Build paths inside the project 
like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().
parent.parent

# Initialize environment variables
env = environ.Env(
    # Set casting, default value
    DEBUG=(bool, False)
)

# Take environment variables from .
env file
environ.Env.read_env(BASE_DIR / '.
env')

# Quick-start development settings 
- unsuitable for production
# See https://docs.djangoproject.
com/en/4.2/howto/deployment/
checklist/

# SECURITY WARNING: keep the secret 
key used in production secret!
SECRET_KEY = env('SECRET_KEY', 
default='django-insecure-change-me-i
n-production')

# SECURITY WARNING: don't run with 
debug turned on in production!
DEBUG = env('DEBUG', default=True)

ALLOWED_HOSTS = env.list
('ALLOWED_HOSTS', default=
['localhost', '127.0.0.1'])

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'corsheaders',
    'drf_yasg',
]

LOCAL_APPS = [
    'listings',
]

INSTALLED_APPS = DJANGO_APPS + 
THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'corsheaders.middleware.
    CorsMiddleware',
    'django.middleware.security.
    SecurityMiddleware',
    'django.contrib.sessions.
    middleware.SessionMiddleware',
    'django.middleware.common.
    CommonMiddleware',
    'django.middleware.csrf.
    CsrfViewMiddleware',
    'django.contrib.auth.middleware.
    AuthenticationMiddleware',
    'django.contrib.messages.
    middleware.MessageMiddleware',
    'django.middleware.clickjacking.
    XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'alx_travel_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.
        backends.django.
        DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.
                context_processors.
                debug',
                'django.template.
                context_processors.
                request',
                'django.contrib.
                auth.
                context_processors.
                auth',
                'django.contrib.
                messages.
                context_processors.
                messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'alx_travel_app.
wsgi.application'

# Database
# https://docs.djangoproject.com/en/
4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.
        backends.mysql',
        'NAME': env('DB_NAME', 
        default='alx_travel_app'),
        'USER': env('DB_USER', 
        default='root'),
        'PASSWORD': env
        ('DB_PASSWORD', default=''),
        'HOST': env('DB_HOST', 
        default='localhost'),
        'PORT': env('DB_PORT', 
        default='3306'),
        'OPTIONS': {
            'init_command': "SET 
            sql_mode='STRICT_TRANS_T
            ABLES'",
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/
4.2/ref/settings/
#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.
        auth.password_validation.
        UserAttributeSimilarityValid
        ator',
    },
    {
        'NAME': 'django.contrib.
        auth.password_validation.
        MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.
        auth.password_validation.
        CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.
        auth.password_validation.
        NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/
4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, 
Images)
# https://docs.djangoproject.com/en/
4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 
'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/
4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.
models.BigAutoField'

# Django REST Framework 
Configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES'
    : [
        'rest_framework.
        authentication.
        SessionAuthentication',
        'rest_framework.
        authentication.
        TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.
        IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 
    'rest_framework.pagination.
    PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.
        JSONRenderer',
        'rest_framework.renderers.
        BrowsableAPIRenderer',
    ],
}

# CORS Configuration
CORS_ALLOWED_ORIGINS = env.list
('CORS_ALLOWED_ORIGINS', default=[
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
])

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# Swagger Settings
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Token': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'USE_SESSION_AUTH': False,
    'JSON_EDITOR': True,
    'SUPPORTED_SUBMIT_METHODS': [
        'get',
        'post',
        'put',
        'delete',
        'patch'
    ],
    'OPERATIONS_SORTER': 'alpha',
    'TAGS_SORTER': 'alpha',
    'DOC_EXPANSION': 'none',
    'DEEP_LINKING': True,
    'SHOW_EXTENSIONS': True,
    'SHOW_COMMON_EXTENSIONS': True,
}

REDOC_SETTINGS = {
    'LAZY_RENDERING': False,
}

# Celery Configuration (for future 
use)
CELERY_BROKER_URL = env
('CELERY_BROKER_URL', 
default='pyamqp://guest@localhost//
')
CELERY_RESULT_BACKEND = env
('CELERY_RESULT_BACKEND', 
default='rpc://')
CELERY_ACCEPT_CONTENT = 
['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
```

Now let me create the main URLs configuration with Swagger integration:

```
"""
URL configuration for 
alx_travel_app project.

The `urlpatterns` list routes URLs 
to views. For more information 
please see:
    https://docs.djangoproject.com/
    en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app 
    import views
    2. Add a URL to urlpatterns:  
    path('', views.home, 
    name='home')
Class-based views
    1. Add an import:  from 
    other_app.views import Home
    2. Add a URL to urlpatterns:  
    path('', Home.as_view(), 
    name='home')
Including another URLconf
    1. Import the include() 
    function: from django.urls 
    import include, path
    2. Add a URL to urlpatterns:  
    path('blog/', include('blog.
    urls'))
"""
from django.contrib import admin
from django.urls import path, 
include, re_path
from rest_framework import 
permissions
from drf_yasg.views import 
get_schema_view
from drf_yasg import openapi

# Swagger/OpenAPI Schema 
Configuration
schema_view = get_schema_view(
    openapi.Info(
        title="ALX Travel App API",
        default_version='v1',
        description="A 
        comprehensive travel 
        listing platform API",
        terms_of_service="https://
        www.google.com/policies/
        terms/",
        contact=openapi.Contact
        (email="contact@alxtravelapp
        .local"),
        license=openapi.License
        (name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.
    AllowAny,),
)

urlpatterns = [
    # Admin interface
    path('admin/', admin.site.urls),
    
    # API endpoints
    path('api/v1/', include
    ('listings.urls')),
    
    # API Documentation
    path('swagger<format>/', 
    schema_view.without_ui
    (cache_timeout=0), 
    name='schema-json'),
    path('swagger/', schema_view.
    with_ui('swagger', 
    cache_timeout=0), 
    name='schema-swagger-ui'),
    path('redoc/', schema_view.
    with_ui('redoc', 
    cache_timeout=0), 
    name='schema-redoc'),
    
    # API Root
    re_path(r'^api/v1/', include
    ('rest_framework.urls', 
    namespace='rest_framework')),
]
```

Now let me create the listings app structure:

```
from django.apps import AppConfig


class ListingsConfig(AppConfig):
    default_auto_field = 'django.db.
    models.BigAutoField'
    name = 'listings'
```

```
from django.contrib import admin

# Register your models here.
```

```
from django.db import models

# Create your models here.
```

```
from django.shortcuts import render
from rest_framework.decorators 
import api_view
from rest_framework.response import 
Response
from rest_framework import status
from drf_yasg.utils import 
swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

@swagger_auto_schema(
    method='get',
    operation_description="Welcome 
    endpoint for the ALX Travel App 
    API",
    responses={
        200: openapi.Response(
            description="Welcome 
            message",
            examples={
                "application/json": 
                {
                    "message": 
                    "Welcome to ALX 
                    Travel App API",
                    "version": "v1",
                    "status": 
                    "active"
                }
            }
        )
    }
)
@api_view(['GET'])
def welcome_view(request):
    """
    Welcome endpoint for the ALX 
    Travel App API
    """
    return Response({
        "message": "Welcome to ALX 
        Travel App API",
        "version": "v1",
        "status": "active"
    }, status=status.HTTP_200_OK)
```

```
from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.welcome_view, 
    name='welcome'),
]
```

```
from django.test import TestCase

# Create your tests here.
```

Now let me create the .env template file:

```
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DB_NAME=alx_travel_app
DB_USER=root
DB_PASSWORD=your-mysql-password
DB_HOST=localhost
DB_PORT=3306

# CORS Configuration
CORS_ALLOWED_ORIGINS=http://
localhost:3000,http://127.0.0.1:3000

# Celery Configuration
CELERY_BROKER_URL=pyamqp://
guest@localhost//
CELERY_RESULT_BACKEND=rpc://
```

Let me also create a basic .env file for development:

```
# Django Settings
SECRET_KEY=django-insecure-developme
nt-key-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DB_NAME=alx_travel_app
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306

# CORS Configuration
CORS_ALLOWED_ORIGINS=http://
localhost:3000,http://127.0.0.1:3000

# Celery Configuration
CELERY_BROKER_URL=pyamqp://
guest@localhost//
CELERY_RESULT_BACKEND=rpc://
```

Now let me create a .gitignore file:

```
# Byte-compiled / optimized / DLL 
files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written 
by a python script from a template
#  before PyInstaller builds the 
exe, so as to inject date/other 
infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
#   According to pypa/pipenv#598, 
it is recommended to include 
Pipfile.lock in version control.
#   However, in case of 
collaboration, if having 
platform-specific dependencies or 
dependencies
#   having no cross-platform 
support, pipenv may install 
dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/
David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Media files
media/

# Static files
staticfiles/
```

Now let me create a README.md file to document the project:

````
# ALX Travel App

A Django-based travel listing 
platform with REST API and 
comprehensive documentation.

## Features

- Django REST Framework for API 
development
- MySQL database integration
- Swagger/OpenAPI documentation
- CORS headers configuration
- Environment variable management
- Celery integration for background 
tasks
- Comprehensive API documentation 
at `/swagger/`

## Prerequisites

- Python 3.8+
- MySQL 5.7+
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/
yourusername/alx_travel_app.git
cd alx_travel_app
````

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On 
Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

```bash
cp .env.example .env
# Edit .env with your database 
credentials and other settings
```

5. Set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver
```

## API Documentation

- Swagger UI: http://localhost:8000/
swagger/
- ReDoc: http://localhost:8000/
redoc/
- Admin Interface: http://
localhost:8000/admin/

## Project Structure

```
alx_travel_app/
├── alx_travel_app/          # Main project directory
│   ├── init .py
│   ├── settings.py          # Django settings with environment variables
│   ├── urls.py              # Main URL configuration with Swagger
│   ├── wsgi.py
│   └── asgi.py
├── listings/                # Listings app
│   ├── init .py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── requirements.txt         # Project dependencies
├── manage.py               # Django management script
├── .env.example           # Environment variables template
├── .gitignore            # Git ignore file
└── README.md             # This file

```

## Environment Variables

Create a `.env` file in the project 
root with the following variables:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=alx_travel_app
DB_USER=root
DB_PASSWORD=your-mysql-password
DB_HOST=localhost
DB_PORT=3306

CORS_ALLOWED_ORIGINS=http://
localhost:3000,http://127.0.0.1:3000
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the 
MIT License.

```
Now let me initialize the Git repository and create the initial commit. First, let me check the current directory structure:

alx_travel_app

I'll help you set up the ALX Travel App Django project according to the milestone requirements. Let me start by creating the Django project structure and all necessary files.

## Step 1: Create Django Project and App
First, let me create the Django project structure:

```

#!/usr/bin/env python
"""Django's command-line utility 
for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault
    ('DJANGO_SETTINGS_MODULE', 
    'alx_travel_app.settings')
    try:
        from django.core.management 
        import 
        execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import 
            Django. Are you sure 
            it's installed and "
            "available on your 
            PYTHONPATH environment 
            variable? Did you "
            "forget to activate a 
            virtual environment?"
        ) from exc
    execute_from_command_line(sys.
    argv)

if **name** == '**main**':
    main()

```

```

"""
ASGI config for alx_travel_app 
project.

It exposes the ASGI callable as a 
module-level variable named 
`application`.

For more information on this file, 
see
https://docs.djangoproject.com/en/4.
2/howto/deployment/asgi/
"""

import os

from django.core.asgi import 
get_asgi_application

os.environ.setdefault
('DJANGO_SETTINGS_MODULE', 
'alx_travel_app.settings')

application = get_asgi_application()

```

```

"""
WSGI config for alx_travel_app 
project.

It exposes the WSGI callable as a 
module-level variable named 
`application`.

For more information on this file, 
see
https://docs.djangoproject.com/en/4.
2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import 
get_wsgi_application

os.environ.setdefault
('DJANGO_SETTINGS_MODULE', 
'alx_travel_app.settings')

application = get_wsgi_application()

```
## Step 2: Configure Settings with Environment Variables
```

"""
Django settings for alx_travel_app 
project.

Generated by 'django-admin 
startproject' using Django 4.2.

For more information on this file, 
see
https://docs.djangoproject.com/en/4.
2/topics/settings/

For the full list of settings and 
their values, see
https://docs.djangoproject.com/en/4.
2/ref/settings/
"""

import environ
from pathlib import Path

# Build paths inside the project 
like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(**file**).resolve().
parent.parent

# Initialize environment variables
env = environ.Env(
    # Set casting, default value
    DEBUG=(bool, False)
)

# Take environment variables from .
env file
environ.Env.read_env(BASE_DIR / '.
env')

# Quick-start development settings 
- unsuitable for production
# See https://docs.djangoproject.
com/en/4.2/howto/deployment/
checklist/

# SECURITY WARNING: keep the secret 
key used in production secret!
SECRET_KEY = env('SECRET_KEY', 
default='django-insecure-change-me-i
n-production')

# SECURITY WARNING: don't run with 
debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env.list
('ALLOWED_HOSTS', default=
['localhost', '127.0.0.1'])

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

# Third party apps
    'rest_framework',
    'corsheaders',
    'drf_yasg',

# Local apps
    'listings',
]

MIDDLEWARE = [
    'corsheaders.middleware.
    CorsMiddleware',
    'django.middleware.security.
    SecurityMiddleware',
    'django.contrib.sessions.
    middleware.SessionMiddleware',
    'django.middleware.common.
    CommonMiddleware',
    'django.middleware.csrf.
    CsrfViewMiddleware',
    'django.contrib.auth.middleware.
    AuthenticationMiddleware',
    'django.contrib.messages.
    middleware.MessageMiddleware',
    'django.middleware.clickjacking.
    XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'alx_travel_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.
        backends.django.
        DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.
                context_processors.
                debug',
                'django.template.
                context_processors.
                request',
                'django.contrib.
                auth.
                context_processors.
                auth',
                'django.contrib.
                messages.
                context_processors.
                messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'alx_travel_app.
wsgi.application'

# Database
# https://docs.djangoproject.com/en/
4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.
        backends.mysql',
        'NAME': env('DB_NAME', 
        default='alx_travel_app'),
        'USER': env('DB_USER', 
        default='root'),
        'PASSWORD': env
        ('DB_PASSWORD', default=''),
        'HOST': env('DB_HOST', 
        default='localhost'),
        'PORT': env('DB_PORT', 
        default='3306'),
        'OPTIONS': {
            'init_command': "SET 
            sql_mode='STRICT_TRANS_T
            ABLES'",
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/
4.2/ref/settings/
#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.
        auth.password_validation.
        UserAttributeSimilarityValid
        ator',
    },
    {
        'NAME': 'django.contrib.
        auth.password_validation.
        MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.
        auth.password_validation.
        CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.
        auth.password_validation.
        NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/
4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, 
Images)
# https://docs.djangoproject.com/en/
4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 
'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/
4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.
models.BigAutoField'

# Django REST Framework 
configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES'
    : [
        'rest_framework.
        authentication.
        SessionAuthentication',
        'rest_framework.
        authentication.
        TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.
        IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 
    'rest_framework.pagination.
    PageNumberPagination',
    'PAGE_SIZE': 20,
}

# CORS settings
CORS_ALLOWED_ORIGINS = env.list
('CORS_ALLOWED_ORIGINS', default=[
    "http://localhost:3000",
    "http://127.0.0.1:3000",
])

CORS_ALLOW_CREDENTIALS = True

# Swagger settings
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Token': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'USE_SESSION_AUTH': False,
    'JSON_EDITOR': True,
    'SUPPORTED_SUBMIT_METHODS': [
        'get',
        'post',
        'put',
        'delete',
        'patch'
    ],
}

REDOC_SETTINGS = {
    'LAZY_RENDERING': False,
}

# Celery Configuration (for future 
use)
CELERY_BROKER_URL = env
('CELERY_BROKER_URL', 
default='pyamqp://guest@localhost//
')
CELERY_RESULT_BACKEND = env
('CELERY_RESULT_BACKEND', 
default='rpc://')
CELERY_ACCEPT_CONTENT = 
['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE

```
## Step 3: Configure URLs with Swagger Integration
```

"""alx_travel_app URL Configuration

The `urlpatterns` list routes URLs 
to views. For more information 
please see:
    https://docs.djangoproject.com/
    en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app 
    import views
    2. Add a URL to urlpatterns:  
    path('', views.home, 
    name='home')
Class-based views
    1. Add an import:  from 
    other_app.views import Home
    2. Add a URL to urlpatterns:  
    path('', Home.as_view(), 
    name='home')
Including another URLconf
    1. Import the include() 
    function: from django.urls 
    import include, path
    2. Add a URL to urlpatterns:  
    path('blog/', include('blog.
    urls'))
"""
from django.contrib import admin
from django.urls import path, 
include, re_path
from rest_framework import 
permissions
from drf_yasg.views import 
get_schema_view
from drf_yasg import openapi

# Swagger/OpenAPI schema 
configuration
schema_view = get_schema_view(
    openapi.Info(
        title="ALX Travel App API",
        default_version='v1',
        description="A 
        comprehensive travel 
        listing platform API",
        terms_of_service="https://
        www.google.com/policies/
        terms/",
        contact=openapi.Contact
        (email="contact@alxtravelapp
        .local"),
        license=openapi.License
        (name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.
    AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

# API endpoints
    path('api/v1/', include
    ('listings.urls')),

# Swagger/OpenAPI documentation
    re_path(r'^swagger(?P<format>\.
    json|\.yaml)$', schema_view.
    without_ui(cache_timeout=0), 
    name='schema-json'),
    path('swagger/', schema_view.
    with_ui('swagger', 
    cache_timeout=0), 
    name='schema-swagger-ui'),
    path('redoc/', schema_view.
    with_ui('redoc', 
    cache_timeout=0), 
    name='schema-redoc'),
]

```
## Step 4: Create the Listings App
```

from django.apps import AppConfig

class ListingsConfig(AppConfig):
    default_auto_field = 'django.db.
    models.BigAutoField'
    name = 'listings'

```

```

from django.contrib import admin

# Register your models here.

```

```

from django.db import models

# Create your models here.

```

```

from django.shortcuts import render
from rest_framework.decorators 
import api_view
from rest_framework.response import 
Response
from drf_yasg.utils import 
swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

@swagger_auto_schema(
    method='get',
    operation_description="Welcome 
    endpoint for the ALX Travel App 
    API",
    responses={200: openapi.Response
    ('Success', openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'message': openapi.
            Schema(type=openapi.
            TYPE_STRING),
            'status': openapi.Schema
            (type=openapi.
            TYPE_STRING),
        }
    ))}
)
@api_view(['GET'])
def welcome_view(request):
    """
    Welcome endpoint for the ALX 
    Travel App API
    """
    return Response({
        'message': 'Welcome to ALX 
        Travel App API',
        'status': 'success'
    })

```

```

from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view, 
    name='welcome'),
]

```

```

from django.test import TestCase

# Create your tests here.

```
## Step 5: Create Requirements File
```

Django==4.2.7
djangorestframework==3.14.0
django-cors-headers==4.3.1
drf-yasg==1.21.7
django-environ==0.11.2
mysqlclient==2.2.0
celery==5.3.4
kombu==5.3.4

```
## Step 6: Create Environment File Template
```

# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DB_NAME=alx_travel_app
DB_USER=root
DB_PASSWORD=your-mysql-password
DB_HOST=localhost
DB_PORT=3306

# CORS Settings
CORS_ALLOWED_ORIGINS=http://
localhost:3000,http://127.0.0.1:3000

# Celery Configuration
CELERY_BROKER_URL=pyamqp://
guest@localhost//
CELERY_RESULT_BACKEND=rpc://

```
## Step 7: Create Git Configuration Files
```

# Byte-compiled / optimized / DLL 
files
**pycache**/
_.py[cod]
_$py.class

# C extensions
\*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
_.egg-info/
.installed.cfg
_.egg
MANIFEST

# PyInstaller
#  Usually these files are written 
by a python script from a template
#  before PyInstaller builds the 
exe, so as to inject date/other 
infos into it.
_.manifest
_.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage._
.cache
nosetests.xml
coverage.xml
_.cover
\*.py,cover
.hypothesis/
.pytest_cache/

# Translations
_.mo
_.pot

# Django stuff:
\*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/\_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
#   According to pypa/pipenv#598, 
it is recommended to include 
Pipfile.lock in version control.
#   However, in case of 
collaboration, if having 
platform-specific dependencies or 
dependencies
#   having no cross-platform 
support, pipenv may install 
dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/
David-OConnor/pyflow
**pypackages**/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
\*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# IDE
.vscode/
.idea/
_.swp
_.swo

# OS
.DS_Store
Thumbs.db

# Static files
staticfiles/
media/

```
## Step 8: Create README File
```

# ALX Travel App

A comprehensive travel listing 
platform built with Django and 
Django REST Framework.

## Features

- RESTful API architecture
- MySQL database integration
- Swagger/OpenAPI documentation
- CORS support for frontend 
integration
- Environment-based configuration
- Celery support for background 
tasks

## Setup Instructions

### Prerequisites

- Python 3.8+
- MySQL 5.7+
- Git

### Installation

1. Clone the repository:

```bash
git clone https://github.com/
yourusername/alx_travel_app.git
cd alx_travel_app
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On 
Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver
```

## API Documentation

Once the server is running, you can 
access the API documentation at:

- Swagger UI: http://localhost:8000/
swagger/
- ReDoc: http://localhost:8000/
redoc/

## Project Structure

```
alx_travel_app/
├── alx_travel_app/
│   ├── init .py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── listings/
│   ├── init .py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.