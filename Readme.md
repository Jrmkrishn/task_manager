Here’s a basic README for your Django project, detailing how to set up, configure, and run the project.

---

# Task Manager Project

This is a Django-based task management application that allows users to create, update, and delete tasks. The application supports Google OAuth login for authentication and integrates the `django-allauth` package.

## Requirements

- Python 3.8 or higher
- Django 5.1.3
- PostgreSQL (or SQLite for development)
- `django-allauth` for OAuth authentication
- `django-invitations` for email-based invites

## Setup and Installation

Follow the steps below to set up and run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/Jrmkrishn/task_manager.git
cd task-manager
```

### 2. Create a Virtual Environment

It is recommended to use a virtual environment to isolate dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # For MacOS/Linux
venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory of the project and add the following variables:

```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3 
SMTP_EMAIL=your-email@gmail.com
SMTP_EMAIL_PASS=your-email-password
```

You can generate a secret key using Django's `django.core.management.utils.get_random_secret_key()`.

### 5. Apply Migrations

Run the following commands to create the database schema:

```bash
python manage.py migrate
```

### 6. Create a Superuser

To access the Django admin panel and manage tasks, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the admin account.

### 7. Start the Development Server

You can start the Django development server using the following command:

```bash
python manage.py runserver
```

By default, the app will be available at `http://127.0.0.1:8000`.

### 8. Access the Application

- **Admin Panel**: Access the Django admin panel by going to `http://127.0.0.1:8000/admin/`. Use the superuser credentials created earlier to log in.
- **Task List**: After logging in, you'll be able to create, update, and delete tasks.

### 9. Google OAuth Setup

To enable Google login, you need to set up a Google OAuth client ID. Follow these steps:

1. Go to the [Google Developer Console](https://console.developers.google.com/).
2. Create a new project.
3. Enable the "Google+ API" (required for authentication).
4. Create OAuth credentials (choose Web application).
5. Add the redirect URI in the format: `http://127.0.0.1:8000/accounts/google/login/callback/`.
6. Copy the **Client ID** and **Client Secret** and add them to the `.env` file.

### 10. Invite Users (Optional)

If you're using `django-invitations` to invite users:

- Make sure `INVITATIONS_INVITE_ONLY = True` is set in the settings.
- You can invite users via the admin panel or by using Django shell:

```bash
python manage.py shell
```

```python
from invitations.models import Invitation
Invitation.create(email="user@example.com")
```

---

## Project Structure

```
task-manager/
│
├── task_manager/               # Project folder containing settings.py
│   ├── __init__.py
│   ├── settings.py             # Settings for the Django app
│   ├── urls.py                 # URL routing
│   └── wsgi.py
│
├── tasks/                      # Application for managing tasks
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py               # Task model
│   ├── views.py                # Views for task management
│   ├── forms.py                # Form for creating and editing tasks
│   └── urls.py
│
├── templates/                  # HTML templates
│   ├── tasks/
│   │   ├── task_list.html
│   │   ├── task_form.html
│   │   ├── task_confirm_delete.html
│   │   └── base.html
│
├── static/                     # Static files (CSS, JS)
│
├── manage.py                   # Django management script
└── requirements.txt            # Python dependencies
```

---

## Additional Notes

- **OAuth**: The app uses Google OAuth for authentication via `django-allauth`.
- **Task Management**: Users can create, edit, and delete tasks that are linked to their accounts.
- **Email Invites**: Users can be invited using email if the invite-only setting is enabled.

---

### License

This project is licensed under the MIT License.

---
