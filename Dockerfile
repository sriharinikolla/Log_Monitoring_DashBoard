# Use Python 3.9 slim as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy everything from the current directory to /app inside the container
COPY . .

# Install Flask inside the container
RUN pip install flask

# Define the command to run when the container starts
CMD ["python", "app.py"]
