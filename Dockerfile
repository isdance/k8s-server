FROM python:3.7.3-stretch

## Step 1:
# Create a working directory
WORKDIR /app

## Step 2:
# Copy source code to working directory
COPY . /app

## Step 3:
# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --upgrade pip &&\
    pip install build-deps gcc python3-dev musl-dev postgresql-dev

RUN  pip install --trusted-host pypi.python.org -r requirements.txt

## Step 4:
# Load env variables
ENV APP_SETTINGS config.DevelopmentConfig
ENV DATABASE_URL postgres://isdance:51315704@localhost:5432/demo

## Step 5:
# Expose port 5000
EXPOSE 5000

## Step 6:
# Run app.py at container launch
ENTRYPOINT gunicorn \
    --access-logfile="-"                   \
    --error-logfile="-"                    \
    --bind=0.0.0.0:5000                    \
    --worker-class=sync                    \
    --workers=1                            \
    --keep-alive=10                        \
    --graceful-timeout=10                  \
    app:app
