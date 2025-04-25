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
ajax_crud_project/ ├── core/ # Main Django app │ ├── static/ # Static files (CSS, JS) │ ├── templates/ # HTML templates │ ├── urls.py # App-level routes │ ├── views.py # AJAX views │ └── models.py # Database models ├── ajax_crud_project/ │ ├── settings.py # Project settings │ └── urls.py # Project-level routes ├── db.sqlite3 └── manage.py



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



