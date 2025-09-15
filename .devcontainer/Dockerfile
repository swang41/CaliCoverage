# Use a slim Python 3.13 image
FROM python:3.13-slim

# Install git and git-lfs
RUN apt-get update && apt-get install -y git git-lfs && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install pipenv globally
RUN pip install --no-cache-dir pipenv

# Set the working directory
WORKDIR /workspace
