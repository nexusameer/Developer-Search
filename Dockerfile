# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
