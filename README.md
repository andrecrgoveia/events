# Events-app
Author: André Castelo

## Description
I created a project called 'events' where users can:
- Register with email and password
- Login with email and password
- Change Password
- Change registered email
- Create your own events
- Edit your own events
- Disable and enable your own events
- Delete your own events
- View all logged events
- Register and withdraw from an event

## Project Details
- Active events with the earliest date are presented on the front-end in table format
- In this same table, the fields, title, date, number of participants and the owner are shown (presented with the email part before the '@')
- Custom middleware to handle errors
- All validations are done in the backend

## Technologies and tools used
- Python
- Django
- SQLite
- HTML5
- Bootstrap
- Docker

## Database populated for demo
superuser
- email: admin@admin.com
- password: superuser

user
- email: andre@andre.com
- password: normaluser

## Database relations
![Database relations](https://raw.githubusercontent.com/andrecrgoveia/events/db_relations.png)

## How to run the project?

### Python:
Run the command in the project root (where the manage.py file are located)
- python3 manage.py runserver <YOUR_PORT>
- In your browser go to the address http://0.0.0.0:<YOUR_PORT>/

### Gunicorn:
Run the command in the project root (where the manage.py file are located)
- gunicorn -c gunicorn_config.py project.wsgi:application
- In your browser go to the address http://0.0.0.0:8000/
- If you can, run gunicorn -b 0.0.0.0:<YOUR_PORT> project.wsgi:application
- In your browser go to the address http://0.0.0.0:<YOUR_PORT>/

### Docker:
Run these two Docker commands in the project root (where the docker files are located):
- docker-compose build
- docker-compose up

Through dockerhub pull the image and run:
- docker run --name <CONTAINER_NAME> -p <YOUR_PORT>:8000 andrecrgoveia/events-app:latest
- In your browser go to the address http://0.0.0.0:<YOUR_PORT>/

