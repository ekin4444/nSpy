# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Create a non-privileged user
ARG UID=10001
RUN adduser --disabled-password --gecos "" --home "/nonexistent" --shell "/sbin/nologin" --no-create-home --uid "${UID}" appuser

# Copy the requirements.txt file and install the dependencies
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Switch to non-root user
USER appuser

# Copy the rest of the application files
COPY . .

# Expose the port that Django listens on
EXPOSE 8000

# Run the Django app using Gunicorn
CMD gunicorn 'nSpy.wsgi:application' --bind=0.0.0.0:8000
