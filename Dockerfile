# Pull python base image
FROM python:3.7.4-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy Project to the container
RUN mkdir -p /my-blog
WORKDIR /my-blog
COPY . /my-blog


# Installing requirements
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt

