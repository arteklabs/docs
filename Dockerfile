# app container
# Use a Python base image
FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY app.py /app/

# Install any required dependencies
RUN pip install click

# Expose the port for debugging (optional)
EXPOSE 5678

# Specify the entry point for the container
CMD ["python", "app.py"]
