FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /proyecto

COPY requirements.txt /proyecto/

RUN pip install -r requirements.txt


COPY . /proyecto/


