# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.10

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /events-app

# Set the working directory to /events-app
WORKDIR /events-app

# Copy the current directory contents into the container at /events-app
ADD . /events-app/

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get upgrade -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# port where the Django app runs
EXPOSE 8000

# start server
CMD python manage.py runserver 0.0.0.0:8000
