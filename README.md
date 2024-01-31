# Events-app
Author: André Castelo

## Description
This project is an event management system, developed using the Django framework for Python. It allows users to create, manage and participate in events. Key features include:
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
![Database relations](https://raw.githubusercontent.com/andrecrgoveia/events/master/db_relations.png)

## How to run the project?
Clone the project:
```shell
git clone https://github.com/andrecrgoveia/events.git
```

Navigate into the folder that was cloned

Install virtualenv (if not already installed):
```shell
pip install virtualenv
```

Windows:
```shell
venv_events\Scripts\activate
```

Linux:
```shell
source venv_events/bin/activate
```

Install dependencies:
```shell
pip install -r requirements.txt
```

### Python:
Run the command in the project root (where the manage.py file are located)
```shell
python3 manage.py runserver <YOUR_PORT>
```
- In your browser go to the address http://0.0.0.0:<YOUR_PORT>/

### Gunicorn:
Run the command in the project root (where the manage.py file are located)
```shell
gunicorn -c gunicorn_config.py project.wsgi:application
```
- In your browser go to the address http://0.0.0.0:8000/
- If you want, you can run the project on the port of your choice
```shell
gunicorn -b 0.0.0.0:<YOUR_PORT> project.wsgi:application
```
- In your browser go to the address http://0.0.0.0:<YOUR_PORT>/

### Docker:
Run these two Docker commands in the project root (where the docker files are located):
```shell
docker-compose build
```
```shell
docker-compose up
```
- In your browser go to the address http://0.0.0.0:<YOUR_PORT>/

Through dockerhub pull the image and run:
```shell
docker run --name <CONTAINER_NAME> -p <YOUR_PORT>:8000 andrecrgoveia/events-app:latest
```
- In your browser go to the address http://0.0.0.0:<YOUR_PORT>/

## Contribution

### Contributions are welcome. To contribute:
- Fork the project
- Create a new branch (git checkout -b feature/NewFunctionality)
- Make your changes
- Commit your changes (git commit -m 'Adding new functionality')
- Push to the branch (git push origin feature/NovaFuncionalidade)
- Open a Pull Request

## License
This project is under the MIT license. See the LICENSE file for more details.

## Credits
Special thanks to the contributors and the libraries and tools used, including Python, Django, SQLite and Docker.
