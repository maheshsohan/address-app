FROM python:3.6-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
RUN pip install --upgrade pip
COPY requirments.txt /code/

RUN pip install -r /code/requirments.txt
COPY . /code/

WORKDIR /code/app/
