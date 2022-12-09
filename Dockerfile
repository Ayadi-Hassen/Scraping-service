FROM python:3.8.10-slim-buster

WORKDIR /app 
COPY main.py /app
COPY test_api /app
COPY requirements.txt /app

RUN pip install -r /app/requirements.txt

