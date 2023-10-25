# app container
# Use a Python base image
FROM python:3.8

# Set the working directory
WORKDIR /app

COPY requirements.txt /app/

# Copy the application code into the container
COPY app.py /app/

# global deps
RUN pip install -r ../app/requirements.txt

# Specify the entry point for the container
CMD ["bash"]
