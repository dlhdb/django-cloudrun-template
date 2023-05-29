# Use the official lightweight Python image.
# https://hub.docker.com/_/python
# use platform linux/amd64 to avoid M1 MAC issue
FROM --platform=linux/amd64 python:3.10-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Create the virtual environment
ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH=$VIRTUAL_ENV/bin:$PATH

# Copy local code to the container image.
ENV APP_HOME=/app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN python -m pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt --use-pep517

ENV PORT=8080

# Run the web service on container startup. Here we use the gunicorn
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
#CMD exec gunicorn --bind :$PORT --workers 1 --timeout 0 app_sharespace.wsgi
CMD exec gunicorn djproject.asgi:application -w 1 --threads 8 --timeout 0 -k uvicorn.workers.UvicornWorker