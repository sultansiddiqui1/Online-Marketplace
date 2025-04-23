# 🛍️ Django Online Marketplace

A full-stack online marketplace web application built with Django, allowing users to register, buy, sell, and communicate around listed items. This project was developed by following the YouTube tutorial [Learn Django by Building a Marketplace](https://www.youtube.com/watch?v=ZxMB6Njs3ck&t=6838s) by Dennis Ivy.

## 🚀 Features

- 🔐 **Authentication**: Secure user registration and login system.
- 📬 **User Communication**: Integrated messaging between users regarding listed items.
- 📦 **Dashboard**: Personalized dashboards for managing items.
- 📝 **Form Handling**: Custom Django forms with validations and user feedback.
- 📚 **Admin Panel**: Utilizes Django's built-in admin interface for backend management.

## 🛠️ Tech Stack

- **Backend**: Django, Python
- **Database**: SQLite (default; easy to swap with PostgreSQL)
- **Frontend**: HTML, CSS, Bootstrap
- **Other Tools**: Django ORM, Django Admin

## 📸 Screenshots

*(Add screenshots of your app here if available — optional)*

## 🧑‍💻 Getting Started

```bash
# Clone the repository
git clone https://github.com/yourusername/django-marketplace.git
cd django-marketplace

#Create and activate a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

#  Install dependencies
pip install -r requirements.txt

#  Run database migrations
python manage.py migrate

# Create a superuser (admin account)
python manage.py createsuperuser

#  Start the development server
python manage.py runserver

#  Access the admin panel
# Visit http://127.0.0.1:8000/admin/ and log in with your superuser credentials.


#folder structure:
django-marketplace/
├── marketplace/         # Main app for listing items
│   ├── templates/       # HTML templates
│   ├── static/          # CSS, JS, images
│   ├── views.py         # App views
│   └── models.py        # Database models
├── users/               # Custom user model & auth
├── db.sqlite3           # Default SQLite database
├── manage.py            # Django project runner
└── requirements.txt     # Python package list
