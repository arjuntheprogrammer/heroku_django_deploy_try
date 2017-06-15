# Heroku Django Starter Template

## How to Use

To use this project, follow these steps:

1. Create your working environment.
2. Install Django (`$ pip install django`)
3. Create a new project using this template

## Creating Your Project

Using this template to create a new Django app is easy::

    $ django-admin.py startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile helloworld

(If this doesn't work on windows, replace `django-admin.py` with `django-admin`)

You can replace ``helloworld`` with your desired project name.

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

## My helping commands
    wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh //download and install heroku cli

    heroku --version

    heroku login

    mkdir myapp

    cd myapp

    heroku create

    django-admin startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile  myproject

    source ../virenv/bin/activate

    sudo apt-get install postgresql
    sudo apt-get install python-psycopg2
    sudo apt-get install libpq-dev
    pip install -r requirements.txt 

    heroku local web //to run locallly


    git add .
    git commit -m "Added a Procfile."
    heroku login
    heroku create
    git push heroku master
    
## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
