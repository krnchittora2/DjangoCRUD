***REQUIREMENTS***
Windows OS with python3 installed
MySQL Server


***SETUP***
> pip install mysqlclient
> pip install django
> django-admin startproject DjangoCRUD
> cd DjangoCRUD
> python manage.py startapp app

-- After moving all the code to the project directory
-- Make sure the database credentials are correct in settings.py

> python manage.py makemigrations
> python manage.py migrate
> python manage.py createsuperuser
:username: admin
:email:
:password: Django@123

> python manage.py runserver


***SUPERUSER***
Admin User: admin
Password: Django@123

