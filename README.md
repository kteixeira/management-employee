# EMPLOYEE MANAGEMENT [BETA]

A basic system to employees management

## Instalação

* Instructions
   - sudo pip install virtualenv
   - virtualenv --no-site-packages projects
   - cd /projects/
   - git clone git@github.com:kteixeira/management-employee.git
   - cd management-employee
   - pip install -r requirements.txt
   - create a new settings file from 
   /management-employee/settings.example.py 
   and change the name to settings.py **(will stay /management-employee/settings.py)**
   - configure database on file /management-employee/settings.py
   - run migrate "python manager.py makemigrations"
   - run migrate tables "python manager.py migrate"

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