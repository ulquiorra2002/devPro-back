FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /proyecto

RUN pip install --upgrade pip

COPY requirements.txt /proyecto/

RUN apt-get -y update && \
    pip install -r requirements.txt


COPY . /proyecto/


