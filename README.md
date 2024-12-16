# To-Do App

A simple, minimalistic To-Do application built with Django, allowing users to manage tasks with categories and priorities.

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
- **SQLite**: Default database.
- **HTML**: For templates structure and design.

## Setup

```bash
1. Clone the repository:
   git clone https://github.com/yourusername/todo-app.git
   cd todo-app

2. Set up a virtual environment:
   python -m venv env

3. Install dependencies:
   pip install -r requirements.txt

4. Setup Secret Key
   Create a `.env` file in the root of the project directory.
   Add the following line to the file:
   SECRET_KEY="your-secret-key-here"
   Replace `your-secret-key-here` with your actual secret_key (do not share this file).

5. Run migrations:
   python manage.py migrate

6. Create a superuser (optional for admin access):
   python manage.py createsuperuser

7. Run the development server:
   python manage.py runserver

   The app will be available at http://127.0.0.1:8000/.