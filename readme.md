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

## Built With
* Django
* psycopg2
* requests
