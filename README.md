# To-Do App

A minimalistic To-Do application built with Django, allowing users to manage tasks with categories and priorities.

## Features

- **User Authentication**: Custom user authentication with profile image.
- **Task Management**: Add, update, delete, and view tasks.
- **Category Management**: Categories can be added or deleted.
- **Task Priority**: Tasks are color-coded based on priority levels (Low, Medium, High).
- **Message Display**: User notifications and feedback on actions.

## Technologies Used

- **Python**: (Programming language)
- **Django**: Python-based framework for backend development.
- **Bootstrap**: For front-end styling.
- **PostgreSQL**: For managing accounts, tasks, images and categories.
- **HTML**: For templates structure and design.

## Setup

```bash
1. Clone the repository:
   git clone https://github.com/MohammadEslahi/ToDo-web-app
   cd ToDo-web-app

2. Set up a virtual environment:
   python -m venv env

3. Install dependencies: 
   pip install -r requirements.txt

4. Setup the database:

  For SQLite (default):
  No additional steps are needed, the database will be created automatically when you run migrations.
  
  For PostgreSQL:
  Install PostgreSQL and set up a new database.
  Create a new database and user in PostgreSQL. Example:

  CREATE DATABASE ToDo-web-app;
  CREATE USER ToDo-web-app_user WITH PASSWORD 'your_password';
  ALTER ROLE ToDo-web-app_user SET client_encoding TO 'utf8';
  ALTER ROLE ToDo-web-app_user SET default_transaction_isolation TO 'read committed';
  ALTER ROLE ToDo-web-app_user SET timezone TO 'UTC';
  GRANT ALL PRIVILEGES ON DATABASE ToDo-web-app TO ToDo-web-app_user;

  Update the DATABASES setting in your settings.py to use PostgreSQL:

  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'ToDo-web-app',
          'USER': 'ToDo-web-app_user',
          'PASSWORD': 'your_password',
          'HOST': 'localhost',
          'PORT': '5432',
      }
  }


5. Setup Secret Key
   Create a `.env` file in the root of the project directory.
   Add the following line to the file:
   SECRET_KEY="your-secret-key-here"
   Replace `your-secret-key-here` with your actual secret_key (do not share this file).


6. Run migrations:
   python manage.py migrate

7. Collect static files:
   python manage.py collectstatic

8. Create a superuser (optional for admin access):
   python manage.py createsuperuser

9. Run the development server:
   python manage.py runserver

   The app will be available at http://127.0.0.1:8000/.
