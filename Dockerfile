# Use the official Python image as the base image
FROM python:3.10

# Set the environment variable
ENV APP_HOME /app

# Set the working directory inside the container
WORKDIR $APP_HOME

# Copy the local files necessar for the build into the container
COPY infinity/ /app/infinity
COPY requirements.txt /app/

# Install dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# Specify port, which docker container exposes
# EXPOSE 5000

# Create a volume for persistent remote storage outside the docker container
VOLUME ["/app"]

# Specify the entry point for your application
ENTRYPOINT ["python", "infinity/main.py"]
