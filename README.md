# Sherpany Code Challenge: Backend Engineer
Author: André Castelo

### Description
I created a project called 'events' where users can:
- Register with email and password
- Login with email and password
- Change Password
- Change registered email
- Create events
- Edit your own events
- Disable and enable your own events
- Delete your own events
- View all logged events
- Register and withdraw from an event

### Project Details
- Active events with the earliest date are presented on the front-end in table format
- In this same table, the fields, title, date, number of participants and the owner are shown (presented with the email part before the '@')

### Technologies and tools used
- Python
- Django
- SQLite
- HTML5
- Bootstrap
- Docker

### Database populated for demo
superuser
- email: admin@admin.com
- password: superuser

user
- email: andre@andre.com
- password: normaluser

### How to access the project?
Run these two Docker commands in the project root (where the docker files are located):
- docker-compose build
- docker-compose up

Through dockerhub pull the image and run:
- docker pull andrecrgoveia/events-app:latest
- docker run --publish <YOUR_PORT>:8000 andrecrgoveia/events-app:v1
- In your browser go to the address http://0.0.0.0:<YOUR_PORT>/

Access via browser
- Just access the url https://andrecastelo-events-app.herokuapp.com/
