# 🍽️ Restaurant Kitchen Service

This is a web application to manage a restaurant kitchen. Admins can create, update, and view **dishes**, **dish types**, and **cooks** with their experience. The app also has search, user login, and an admin panel.

---

## ⚙️ Features

- User authentication (custom Cook user model)
- Create, read, update, delete (CRUD) for:
  - Dishes
  - Dish types
  - Cooks
- Search dishes by name
- Assign cooks to dishes (many-to-many)
- Admin panel
- Count visits on the homepage
- User registration form with extra fields

---

## 🧰 Technologies

- Python 3.11+
- Django 5.2.3
- Django REST Framework 3.16.0
- SQLite (default database)
- Bootstrap 4 with crispy-forms
- Testing with pytest and pytest-django
- Linting with flake8 and plugins
- Environment variables with python-dotenv
- pip

---

### ⚙️ Requirements

- asgiref==3.8.1
- attrs==25.3.0
- colorama==0.4.6
- Django~=5.2.3
- djangorestframework==3.16.0
- flake8==5.0.4
- flake8-annotations==2.9.1
- flake8-quotes==3.3.1
- flake8-variables-names==0.0.5
- iniconfig==2.0.0
- mccabe==0.7.0
- packaging==24.2
- pep8-naming==0.13.2
- pluggy==1.5.0
- py==1.11.0
- pycodestyle==2.9.1
- pyflakes==2.5.0
- pytest==7.1.3
- pytest-django==4.5.2
- sqlparse==0.5.3
- tomli==2.2.1
- tzdata==2024.2
- django-crispy-forms==2.4
- crispy-bootstrap4==2025.6

- dotenv~=0.9.9
- python-dotenv~=1.1.1


### Steps

```bash
# 1. Clone the project
git clone https://github.com/Bogdanneww/restaurant-kitchen-service.git
cd restaurant-kitchen-service

# 2. Create and activate virtual environment
python -m venv .venv
# On Linux/macOS
source .venv/bin/activate
# On Windows
.venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create a .env file and add necessary environment variables

# 5. Run migrations
python manage.py migrate

# 6. Create a superuser
python manage.py createsuperuser

# 7. Start the development server
python manage.py runserver

---

✍️ Author
Name: https://github.com/Bogdanneww

Email: bogdannew@i.ua
