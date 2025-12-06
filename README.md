# RecycleLink
RecycleLink

RecycleLink is a Django-based web application designed to help users, landlords, and garbage collectors find nearby recycling companies. Users can deliver recyclable waste or request pickups, making recycling easier, more organized, and accessible.

Features (MVP – Initial Setup)

Homepage with all-in-one layout: search, company browsing, and pickup request options.

Responsive navigation bar (Home, Companies, Request Pickup, Profile dropdown).

Role-based structure for future enhancements (users, landlords, garbage collectors).

Basic Django project structure ready for expansion.

Technologies Used

Python 3.x

Django 4.x

HTML, Bootstrap 5, CSS

SQLite (default for development; can be switched to MySQL/PostgreSQL)

Installation

Clone the repository:

git clone https://github.com/yourusername/RecycleLink.git
cd RecycleLink


Create a virtual environment:

python -m venv env
- source env/Scripts/activate



Install dependencies:

-pip install -r requirements.txt


Applying migrations:

-python manage.py migrate


Create a superuser (for admin access):

-python manage.py createsuperuser


Run the development server:

  -python manage.py runserver