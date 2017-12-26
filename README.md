# EMPLOYEE MANAGEMENT [BETA]

A basic system to employees management

## Installation

* Instructions
   - sudo pip install virtualenv
   - git clone git@github.com:kteixeira/management-employee.git
   - virtualenv -p python3 envname
   - pip install --upgrade virtualenv
   - source env/bin/activate
   - pip install --upgrade pip
   - cd management-employee
   - pip install -r requirements.txt
   - *(if you have not created it, create database: 
   CREATE DATABASE management_employee CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci)*
   - create a new settings file from 
   /management-employee/settings.example.py 
   and change the name to settings.py **(will stay /management-employee/settings.py)**
   - configure database on file /management-employee/settings.py
   - run migrate: python manage.py migrate
   - python manage.py makemigrations src
   - python manage.py migrate src

### Create a user admin
  - python manage.py createsuperuser
  
### Run Project
  - python manage.py runserver

### Run Tests
  - pytest


### OBS
  - In api authentication is being used Basic Auth 
and the credential is that of the administrative user.

  - The documentation it's in the endpoint /docs

  - **The tests are under construction**

### Routes
  - home          | host:port/
  - admin panel   | host:port/admin/
  - api endpoints | host:port/api/
  - documentation | host:port/docs/