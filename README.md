# Django AJAX CRUD Operations

This project demonstrates how to perform **CRUD (Create, Read, Update, Delete)** operations in Django using **AJAX** and **jQuery** to enhance user experience by avoiding full page reloads.

## ✨ Features

- Create new records without reloading the page.
- Read/fetch records dynamically.
- Update records via modal forms with AJAX.
- Delete records with confirmation prompts using AJAX.
- Clean, modular Django app with jQuery and Bootstrap.

## 🛠️ Tech Stack

- Django (Backend)
- SQLite (Default DB)
- jQuery (AJAX requests)
- Bootstrap (Frontend styling)

## 📁 Project Structure

ajax_crud_project/
├── core/                     # Main Django app
│   ├── static/               # Static files (CSS, JS)
│   ├── templates/            # HTML templates
│   ├── models.py             # Database models
│   ├── urls.py               # App-level URL configurations
│   └── views.py              # Views handling AJAX requests
│
├── ajax_crud_project/        # Project configuration
│   ├── settings.py           # Django settings
│   └── urls.py               # Project-level URL configurations
│
├── db.sqlite3                # SQLite database
├── manage.py                 # Django management script




## 🚀 Getting Started

### 1. Clone the Repository

```bash```
git clone https://github.com/yourusername/django-ajax-crud.git
cd django-ajax-crud

## Set Up Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

## Install Dependencies
 - pip install -r requirements.txt

## Apply Migrations
 - python manage.py makemigrations
 - python manage.py migrate

##  Run the Server
 - python manage.py runserver



