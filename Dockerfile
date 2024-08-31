# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Git if you want Git integration inside the container
RUN apt-get update && apt-get install -y git

# Suppress Git warning from MLflow
ENV GIT_PYTHON_REFRESH=quiet

# Run load_data.py when the container launches
CMD ["python", "src/models/train_model.py"]
