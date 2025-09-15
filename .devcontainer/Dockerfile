# Use a slim Python 3.13 image
FROM python:3.13-slim

# Install git and pipenv
RUN apt-get update && apt-get install -y git && pip install --no-cache-dir pipenv

# Set the working directory
WORKDIR /workspace
