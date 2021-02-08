# PurBeurreWeb
Repository for Project 8 from Openclassrooms cursus in Software Development

Website address : https://purbeurreweb.herokuapp.com/

## Project Description
This project is a web application built with **Django** to help users find healthier products to their favorite food.
The application is deployed on **Heroku**.

## Features
* Register
* Login
* Search a product
* Browse substitutes
* Add them to your favorites
* View your favorite products
* Access your Profile page
* Logout

## APIs
The following API was used in this project :
* [Open Food Facts](https://developers.google.com/maps/get-started/)

## Getting Started

1. Clone the repository:
```
git clone https://github.com/JN-Lab/OC-Pr8-OpenFoodFacts-App.git
```

When you are in your directory (root):

2. Set-up your virtual environment
```
python3 -m venv env
```

3. Activate your virtual environment:
```
source env/bin/activate
```

5. Install all necessary frameworks and libraries
```
pip install -r requirements.txt
```

6. Set-up your database in **settings.py** file

7. Go in purbeurre platform directory to have access to manage.py file to launch the initialisation of the database with the basic data:
```
./manage.py inject_db
```

8. Run the django local server:
```
./manage.py runserver
```

9. You go on your favorite browser and copy paste this url:
```
http://127.0.0.1:8000/
```

## Running the tests
To run all the tests:
```
coverage run --source='.' --omit='venv/*' ./manage.py test apps.purbeurreweb.tests apps.favorites.tests apps.users.tests
```
To view the report:
```
coverage report
```

## Deploying on Heroku
- Download and install Heroku CLI
https://devcenter.heroku.com/articles/heroku-cli#download-and-install
sudo snap install --classic heroku

- heroku login

- heroku:apps create yourappname

- heroku addons:create heroku-postgresql:hobby-dev

- heroku config:set SECRET_KEY=yoursecretkey
- heroku config:set EMAIL_USER=youruseremail
- heroku config:set EMAIL_PASSWORD=youruserpassword
- heroku config:set ENV=production

Dans venv:
- pip install django-heroku
Dans settings.py:
- ajouter:
import django_heroku
django_heroku.settings(locals())
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
ALLOWED_HOSTS = [".herokuapp.com", "localhost", "127.0.0.1"]
DEBUG = False if os.getenv("ENV", "development") == "production" else True

- pip install gunicorn

Créer un Procfile:
web: gunicorn config.wsgi --log-file -

Créer requirements.txt

git add
git commit
git push heroku master


## Built With
* Django
* psycopg2
* requests

## Deployed With
* Heroku
