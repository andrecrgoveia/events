# Use an official Python runtime as base image
FROM python:3.10

# Set environment variable to ensure Python output is sent straight to terminal without buffering
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        graphviz \
        libgraphviz-dev \
        pkg-config && \
    rm -rf /var/lib/apt/lists/*

# Create working directory and set working directory
WORKDIR /events-app

# Copy files from current directory into container at working directory
COPY . /events-app/

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose the port where the Django app runs
EXPOSE 8000

# Command to start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
