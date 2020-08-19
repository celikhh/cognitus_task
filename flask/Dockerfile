FROM python:3.5

ENV PYTHONUNBUFFERED 1
ENV FLASK_ENV dev

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

COPY . /code/
WORKDIR /code/

EXPOSE 5000